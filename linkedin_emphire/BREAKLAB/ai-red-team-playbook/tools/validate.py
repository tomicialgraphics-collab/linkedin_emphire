#!/usr/bin/env python3
"""Validate the checklist source file.

Checks shape, not opinion: required fields, unique ids, known categories,
known tiers, no empty test lines, and the house style rules that keep the
rendered documents consistent (no em dashes, no double spaces).

Exits non-zero on any error so CI can block a bad pull request.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "checklist" / "checklist.json"
TIERS = {"core", "standard", "extended"}
REQUIRED = {"id", "category", "name", "tier", "test"}
ID_PATTERN = re.compile(r"^[A-Z]{2}-\d{2}$")


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def validate(data: dict) -> list[str]:
    errors: list[str] = []

    if not isinstance(data.get("items"), list) or not data["items"]:
        return ["no items found"]

    cats = {c.get("slug") for c in data.get("categories", [])}
    if not cats:
        errors.append("no categories declared")

    seen_ids: set[str] = set()
    seen_names: dict[str, str] = {}

    for index, item in enumerate(data["items"]):
        where = f"item {index}"
        missing = REQUIRED - set(item)
        if missing:
            errors.append(f"{where}: missing {', '.join(sorted(missing))}")
            continue

        where = item["id"]
        if not ID_PATTERN.match(item["id"]):
            errors.append(f"{where}: id does not match AA-00")
        if item["id"] in seen_ids:
            errors.append(f"{where}: duplicate id")
        seen_ids.add(item["id"])

        if item["category"] not in cats:
            errors.append(f"{where}: unknown category {item['category']!r}")
        if item["tier"] not in TIERS:
            errors.append(f"{where}: unknown tier {item['tier']!r}")

        name = item["name"].strip()
        if not name:
            errors.append(f"{where}: empty name")
        if name.lower() in seen_names:
            errors.append(f"{where}: duplicate name, also at {seen_names[name.lower()]}")
        seen_names[name.lower()] = item["id"]

        test = item["test"].strip()
        if len(test.split()) < 5:
            errors.append(f"{where}: test line too short to act on")
        if not test.endswith("."):
            errors.append(f"{where}: test line should end with a full stop")

        for field in ("name", "test"):
            value = item[field]
            if "\u2014" in value or "\u2013" in value:
                errors.append(f"{where}: em or en dash in {field}")
            if "  " in value:
                errors.append(f"{where}: double space in {field}")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description="validate checklist.json")
    ap.add_argument("--quiet", action="store_true", help="print only the summary line")
    args = ap.parse_args()

    data = load(SOURCE)
    errors = validate(data)

    if errors:
        for err in errors:
            print(f"FAIL  {err}")
        print(f"\n{len(errors)} error(s) in {SOURCE.name}")
        return 1

    tiers: dict[str, int] = {}
    for item in data["items"]:
        tiers[item["tier"]] = tiers.get(item["tier"], 0) + 1

    if not args.quiet:
        for cat in data["categories"]:
            count = sum(1 for i in data["items"] if i["category"] == cat["slug"])
            print(f"  {cat['prefix']}  {cat['label']:<28} {count:>3}")
        print()
    summary = ", ".join(f"{k} {v}" for k, v in sorted(tiers.items()))
    print(f"OK  {len(data['items'])} items, {len(data['categories'])} categories, {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
