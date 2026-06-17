#!/usr/bin/env python3
"""Fetch the Consumer Rights Wiki Cargo export used by editor workflows."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import urllib.request


DEFAULT_URL = "https://raw.githubusercontent.com/FULU-Foundation/CRW-Extension/refs/heads/export_cargo/all_cargo_combined.json"
DEFAULT_OUT = pathlib.Path("data/snapshots/all_cargo_combined.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL, help="Cargo JSON URL to fetch")
    parser.add_argument("--out", type=pathlib.Path, default=DEFAULT_OUT, help="Output JSON path")
    parser.add_argument(
        "--dated-copy",
        action="store_true",
        help="Also write a date-stamped copy next to the output file",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    req = urllib.request.Request(args.url, headers={"User-Agent": "crw-editor-workflow/0.1"})
    with urllib.request.urlopen(req, timeout=60) as response:
        body = response.read()

    args.out.write_bytes(body)
    print(f"Wrote {len(body):,} bytes to {args.out}")

    if args.dated_copy:
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        dated = args.out.with_name(f"{args.out.stem}-{stamp}{args.out.suffix}")
        dated.write_bytes(body)
        print(f"Wrote dated copy to {dated}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

