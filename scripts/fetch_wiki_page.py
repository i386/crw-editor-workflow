#!/usr/bin/env python3
"""Fetch current Consumer Rights Wiki page wikitext."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import urllib.parse
import urllib.request


API_URL = "https://consumerrights.wiki/api.php"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="Wiki page title")
    parser.add_argument("--out", type=pathlib.Path, help="Optional output path")
    parser.add_argument("--api", default=API_URL, help="MediaWiki API URL")
    return parser.parse_args()


def safe_name(title: str) -> str:
    name = title.replace(" ", "_")
    name = re.sub(r"[^A-Za-z0-9_.:-]+", "_", name)
    return name.strip("_") or "page"


def fetch_wikitext(api_url: str, title: str) -> str:
    query = urllib.parse.urlencode(
        {
            "action": "parse",
            "page": title,
            "prop": "wikitext",
            "format": "json",
            "formatversion": "2",
        }
    )
    req = urllib.request.Request(f"{api_url}?{query}", headers={"User-Agent": "crw-editor-workflow/0.1"})
    with urllib.request.urlopen(req, timeout=60) as response:
        data = json.loads(response.read().decode("utf-8"))
    if "error" in data:
        raise RuntimeError(data["error"].get("info", "MediaWiki API error"))
    return data["parse"]["wikitext"]


def main() -> int:
    args = parse_args()
    text = fetch_wikitext(args.api, args.title)
    out = args.out or pathlib.Path("data/snapshots") / f"{safe_name(args.title)}.wiki"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text):,} chars to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

