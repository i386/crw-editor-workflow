#!/usr/bin/env python3
"""Generate a lightweight Cargo quality report from a CRW Cargo JSON export."""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import pathlib
import re
from typing import Any
from urllib.parse import urlparse


DATE_RE = re.compile(r"^\d{4}(?:-\d{2}(?:-\d{2})?)?$")
URLISH_RE = re.compile(r"https?://|www\.|^[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
RELATION_FIELDS = ("Company", "Product", "ProductLine", "ParentCompany")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_path", type=pathlib.Path, help="Cargo export JSON path")
    parser.add_argument("--markdown", type=pathlib.Path, help="Optional markdown report path")
    parser.add_argument("--json", type=pathlib.Path, dest="json_out", help="Optional JSON findings path")
    parser.add_argument("--min-match-length", type=int, default=2, help="Minimum token length for matching")
    parser.add_argument("--limit", type=int, default=0, help="Limit markdown rows; 0 means all")
    return parser.parse_args()


def load_records(path: pathlib.Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    if isinstance(data, dict):
        for key in ("entries", "rows", "data", "pages", "cargo"):
            value = data.get(key)
            if isinstance(value, list):
                return [x for x in value if isinstance(x, dict)]
        flattened: list[dict[str, Any]] = []
        for table_name, rows in data.items():
            if isinstance(rows, list):
                for row in rows:
                    if isinstance(row, dict):
                        item = dict(row)
                        item.setdefault("_table", table_name)
                        flattened.append(item)
        if flattened:
            return flattened
    raise ValueError(f"Could not find Cargo records in {path}")


def first_value(record: dict[str, Any], *names: str) -> Any:
    lowered = {k.lower(): k for k in record}
    for name in names:
        if name in record:
            return record[name]
        actual = lowered.get(name.lower())
        if actual:
            return record[actual]
    return None


def text_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ",".join(text_value(item) for item in value)
    if isinstance(value, dict):
        return ",".join(text_value(item) for item in value.values())
    return str(value).strip()


def page_name(record: dict[str, Any]) -> str:
    return text_value(first_value(record, "PageName", "_pageName", "_pageNameOrRedirect", "Title", "Page", "_pageName"))


def record_type(record: dict[str, Any]) -> str:
    raw = text_value(first_value(record, "CargoType", "PageType", "ArticleType", "_table", "table", "Template"))
    for candidate in ("Company", "Incident", "ProductLine", "Product"):
        if raw.lower() == candidate.lower():
            return candidate
    for candidate in ("Company", "Incident", "ProductLine", "Product"):
        if candidate.lower() in raw.lower():
            return candidate
    return raw or "Unknown"


def date_is_valid(value: str) -> bool:
    if not value:
        return False
    if not DATE_RE.match(value):
        return False
    try:
        parts = [int(part) for part in value.split("-")]
        if len(parts) == 1:
            dt.date(parts[0], 1, 1)
        elif len(parts) == 2:
            dt.date(parts[0], parts[1], 1)
        else:
            dt.date(parts[0], parts[1], parts[2])
    except ValueError:
        return False
    return True


def date_sort_key(value: str) -> tuple[int, int, int] | None:
    if not date_is_valid(value):
        return None
    parts = [int(part) for part in value.split("-")]
    parts = parts + [1] * (3 - len(parts))
    return parts[0], parts[1], parts[2]


def website_is_sane(value: str) -> bool:
    if not value:
        return False
    candidates = [part.strip(" []") for part in re.split(r"[,;\n]", value) if part.strip()]
    for candidate in candidates:
        if candidate.startswith("[") and " " in candidate:
            candidate = candidate.strip("[]").split(" ", 1)[0]
        if not URLISH_RE.search(candidate):
            return False
        parsed = urlparse(candidate if "://" in candidate else f"https://{candidate}")
        if not parsed.netloc or "." not in parsed.netloc:
            return False
    return True


def relation_tokens_too_short(record: dict[str, Any], min_len: int) -> list[str]:
    short: list[str] = []
    for field in RELATION_FIELDS:
        value = text_value(first_value(record, field))
        if not value:
            continue
        tokens = [token.strip() for token in re.split(r"[,;|]", value) if token.strip()]
        for token in tokens:
            if len(token) < min_len:
                short.append(f"{field}={token}")
    return short


def build_findings(records: list[dict[str, Any]], min_match_length: int) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for record in records:
        title = page_name(record)
        kind = record_type(record)
        issues: list[str] = []

        if kind in {"Company", "Product", "ProductLine"}:
            description = text_value(first_value(record, "Description"))
            website = text_value(first_value(record, "Website"))
            if not description:
                issues.append("missing description")
            elif len(description) > 150:
                issues.append("description over 150 chars")
            if not website:
                issues.append("missing website")
            elif not website_is_sane(website):
                issues.append("website sanity")
            if len(title) < min_match_length:
                issues.append("page name too short for matching")

        if kind == "Incident":
            status = text_value(first_value(record, "Status"))
            start = text_value(first_value(record, "StartDate", "Start Date"))
            end = text_value(first_value(record, "EndDate", "End Date"))
            if "," in status:
                issues.append("multi-status incident")
            if not start:
                issues.append("missing start date")
            elif not date_is_valid(start):
                issues.append("invalid start date")
            if end and not date_is_valid(end):
                issues.append("invalid end date")
            if start and end and date_sort_key(start) and date_sort_key(end) and date_sort_key(end) < date_sort_key(start):
                issues.append("end date before start date")
            if status.lower() == "resolved" and not end:
                issues.append("resolved incident missing end date")

        short_tokens = relation_tokens_too_short(record, min_match_length)
        if short_tokens:
            issues.append("short relation token: " + "; ".join(short_tokens))

        if issues:
            findings.append(
                {
                    "page": title or "(missing page name)",
                    "type": kind,
                    "issues": issues,
                }
            )
    return findings


def markdown_report(records: list[dict[str, Any]], findings: list[dict[str, Any]], limit: int) -> str:
    by_type = collections.Counter(record_type(record) for record in records)
    by_issue = collections.Counter(issue for finding in findings for issue in finding["issues"])
    rows = findings if not limit else findings[:limit]
    lines = [
        "# Cargo Quality Report",
        "",
        f"- Dataset entries: {len(records)}",
        f"- Total findings: {len(findings)}",
        "- By type: " + ", ".join(f"{key}={value}" for key, value in sorted(by_type.items())),
        "",
        "## Issue Counts",
        "",
        "| Issue | Count |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {issue} | {count} |" for issue, count in by_issue.most_common())
    lines.extend(
        [
            "",
            "## Findings",
            "",
            "| Page | Type | Issues |",
            "| --- | --- | --- |",
        ]
    )
    lines.extend(f"| {item['page']} | {item['type']} | {'; '.join(item['issues'])} |" for item in rows)
    if limit and len(findings) > limit:
        lines.append(f"\n_Showing {limit} of {len(findings)} findings._")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    records = load_records(args.json_path)
    findings = build_findings(records, args.min_match_length)

    print(f"Records: {len(records)}")
    print(f"Findings: {len(findings)}")

    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown_report(records, findings, args.limit), encoding="utf-8")
        print(f"Wrote markdown report to {args.markdown}")

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(findings, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote JSON findings to {args.json_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
