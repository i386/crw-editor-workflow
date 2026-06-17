#!/usr/bin/env python3
"""Fetch Article suggestions wikitext and produce a rough editor queue."""

from __future__ import annotations

import argparse
import json
import re
import urllib.parse
import urllib.request


API_URL = "https://consumerrights.wiki/api.php"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page", default="Article suggestions", help="Wiki page to fetch")
    parser.add_argument(
        "--section",
        default="List of incidents not yet covered",
        help="Heading to extract before parsing rows; use --all-sections to parse the whole page",
    )
    parser.add_argument("--all-sections", action="store_true", help="Parse the whole page")
    parser.add_argument("--limit", type=int, default=0, help="Limit rows; 0 means all")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of markdown")
    return parser.parse_args()


def fetch_wikitext(page: str) -> str:
    query = urllib.parse.urlencode(
        {
            "action": "parse",
            "page": page,
            "prop": "wikitext",
            "format": "json",
            "formatversion": "2",
        }
    )
    req = urllib.request.Request(f"{API_URL}?{query}", headers={"User-Agent": "crw-editor-workflow/0.1"})
    with urllib.request.urlopen(req, timeout=60) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data["parse"]["wikitext"]


def clean_cell(value: str) -> str:
    value = re.sub(r"<ref[^>]*>.*?</ref>", "[ref]", value, flags=re.I | re.S)
    value = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"\2", value)
    value = re.sub(r"\[\[([^\]]+)\]\]", r"\1", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def extract_rows(wikitext: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for raw_row in re.split(r"\n\|-", wikitext)[1:]:
        if "\n|" not in raw_row:
            continue
        cells = [clean_cell(cell) for cell in re.split(r"\n\|", raw_row) if cell.strip()]
        cells = [cell for cell in cells if not cell.startswith("}")]
        if len(cells) < 2:
            continue
        company = cells[0].lstrip("|").strip()
        summary = cells[1].strip()
        refs = cells[2].strip() if len(cells) > 2 else ""
        if company.lower() in {"company", "theme", "summary of incident"}:
            continue
        rows.append({"subject": company, "summary": summary, "refs": refs})
    return rows


def extract_section(wikitext: str, heading: str) -> str:
    pattern = re.compile(rf"^==\s*{re.escape(heading)}\s*==.*$", re.M)
    match = pattern.search(wikitext)
    if not match:
        return wikitext
    next_heading = re.search(r"^==[^=].*==\s*$", wikitext[match.end() :], re.M)
    end = match.end() + next_heading.start() if next_heading else len(wikitext)
    return wikitext[match.end() : end]


def as_markdown(rows: list[dict[str, str]]) -> str:
    lines = [
        "# Article Suggestion Queue",
        "",
        "| Subject | Summary | Ref notes |",
        "| --- | --- | --- |",
    ]
    for row in rows:
        lines.append(f"| {row['subject']} | {row['summary']} | {row['refs']} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    wikitext = fetch_wikitext(args.page)
    if not args.all_sections:
        wikitext = extract_section(wikitext, args.section)
    rows = extract_rows(wikitext)
    if args.limit:
        rows = rows[: args.limit]
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        print(as_markdown(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
