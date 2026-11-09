#!/usr/bin/env python3
"""Turn a filled status file into a coverage argument.

Input:  a status file (see examples/status-example.json) that records, per item,
        one of: tested, absent, skipped, open.
Output: markdown, suitable for the coverage section of a report.

The rules it enforces are the point of the tool:

1. An item left out of the file counts as open, not as passed.
2. A skipped item must carry a reason, because a skipped class named honestly is
   a finding about the engagement, and an unnamed one is a claim the reader will
   assume you checked.
3. A tested item with no note is reported as tested without evidence.

Exit code is 1 when the status file breaks rule 2, so it can gate a report build.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKLIST = ROOT / "checklist" / "checklist.json"
VALID = ("tested", "absent", "skipped", "open")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def build(checklist: dict, status: dict) -> tuple[str, list[str]]:
    items = {i["id"]: i for i in checklist["items"]}
    labels = {c["slug"]: c["label"] for c in checklist["categories"]}
    recorded = status.get("items", {})
    problems: list[str] = []

    for item_id in recorded:
        if item_id not in items:
            problems.append(f"{item_id}: not an id in the checklist")
            continue
        state = recorded[item_id].get("status", "open")
        if state not in VALID:
            problems.append(f"{item_id}: unknown status {state!r}")
        if state == "skipped" and not recorded[item_id].get("note"):
            problems.append(f"{item_id}: skipped without a reason")

    rows = []
    for item_id, item in items.items():
        entry = recorded.get(item_id, {})
        rows.append({
            "id": item_id,
            "name": item["name"],
            "category": item["category"],
            "tier": item["tier"],
            "status": entry.get("status", "open"),
            "note": entry.get("note", ""),
        })

    counts = Counter(r["status"] for r in rows)
    by_cat: dict[str, Counter] = defaultdict(Counter)
    for row in rows:
        by_cat[row["category"]][row["status"]] += 1

    lines = [
        f"## Coverage: {status.get('target', 'unnamed target')}",
        "",
        "| | |",
        "|---|---|",
    ]
    for key in ("engagement", "date", "tester", "model_revision", "prompt_version"):
        if status.get(key):
            lines.append(f"| {key.replace('_', ' ').capitalize()} | {status[key]} |")

    lines += [
        "",
        f"{len(rows)} classes in the checklist. "
        f"**{counts['tested']} tested**, {counts['absent']} not present in the target, "
        f"{counts['skipped']} skipped on purpose, {counts['open']} open.",
        "",
        "The number to read first is `open`. A coverage argument that does not state it is an advertisement.",
        "",
        "| Category | Tested | Absent | Skipped | Open |",
        "|---|---|---|---|---|",
    ]
    for slug, label in labels.items():
        c = by_cat[slug]
        lines.append(f"| {label} | {c['tested']} | {c['absent']} | {c['skipped']} | {c['open']} |")

    def section(title: str, state: str, show_note: bool) -> None:
        group = [r for r in rows if r["status"] == state]
        if not group:
            return
        lines.extend(["", f"### {title} ({len(group)})", ""])
        for row in group:
            note = f" {row['note']}" if row["note"] else (" no evidence recorded." if show_note else "")
            lines.append(f"- **{row['id']}** {row['name']}.{note}")

    section("Tested", "tested", True)
    section("Not present in the target", "absent", False)
    section("Skipped on purpose, with the reason", "skipped", True)
    section("Open, not tested", "open", False)

    return "\n".join(lines) + "\n", problems


def main() -> int:
    ap = argparse.ArgumentParser(description="build a coverage argument from a status file")
    ap.add_argument("status", type=Path, help="path to a status json file")
    ap.add_argument("-o", "--out", type=Path, help="write markdown here instead of stdout")
    args = ap.parse_args()

    checklist = load_json(CHECKLIST)
    status = load_json(args.status)
    markdown, problems = build(checklist, status)

    if args.out:
        args.out.write_text(markdown, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(markdown)

    if problems:
        print("\nProblems to fix:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
