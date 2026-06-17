#!/usr/bin/env python3
"""Extract top-level wikitext templates and parameters from a page file."""

from __future__ import annotations

import argparse
import json
import pathlib


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=pathlib.Path, help="Wikitext file")
    parser.add_argument("--template", help="Only show templates with this name")
    return parser.parse_args()


def split_top_level(text: str, delimiter: str = "|") -> list[str]:
    parts: list[str] = []
    start = 0
    depth = 0
    i = 0
    while i < len(text):
        if text.startswith("{{", i):
            depth += 1
            i += 2
            continue
        if text.startswith("}}", i):
            depth = max(0, depth - 1)
            i += 2
            continue
        if text[i] == delimiter and depth == 0:
            parts.append(text[start:i])
            start = i + 1
        i += 1
    parts.append(text[start:])
    return parts


def extract_templates(text: str) -> list[str]:
    templates: list[str] = []
    i = 0
    while i < len(text):
        start = text.find("{{", i)
        if start == -1:
            break
        depth = 0
        j = start
        while j < len(text):
            if text.startswith("{{", j):
                depth += 1
                j += 2
                continue
            if text.startswith("}}", j):
                depth -= 1
                j += 2
                if depth == 0:
                    templates.append(text[start + 2 : j - 2].strip())
                    break
                continue
            j += 1
        i = j if j > start else start + 2
    return templates


def parse_template(raw: str) -> dict[str, object]:
    parts = split_top_level(raw)
    name = parts[0].strip()
    params: dict[str, str] = {}
    positional: list[str] = []
    for part in parts[1:]:
        if "=" in part:
            key, value = part.split("=", 1)
            params[key.strip()] = value.strip()
        else:
            positional.append(part.strip())
    return {"name": name, "params": params, "positional": positional}


def main() -> int:
    args = parse_args()
    text = args.path.read_text(encoding="utf-8")
    templates = [parse_template(raw) for raw in extract_templates(text)]
    if args.template:
        templates = [item for item in templates if str(item["name"]).lower() == args.template.lower()]
    print(json.dumps(templates, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

