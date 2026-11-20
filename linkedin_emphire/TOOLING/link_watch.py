#!/usr/bin/env python3
"""link_watch.py - rule R49, the daily check on the four Upwork links.

The owner asked for these four pages to be clicked five times a day. The answer
is recorded in UPWORK/2026-11-15_daily-link-check_rule.md: five reads a day is
traffic, traffic is the number being measured, and a counter fed by the owner
measures the owner. So the rule is one pass a day, written down, diffed against
the day before.

This tool does not fetch. It cannot: this sandbox has no route to upwork.com,
and a fetcher with no route would be a tool that always reports "no change".
The read is done by whoever has a browser or a page reader, the result is handed
to this tool as a snapshot, and the tool does the part that a person does badly,
which is remembering yesterday exactly.

Usage
-----
    python3 TOOLING/link_watch.py links
    python3 TOOLING/link_watch.py due            # exit 1 if today is already done
    python3 TOOLING/link_watch.py show           # print the stored baseline
    python3 TOOLING/link_watch.py record <snapshot.json> [--force] [--dry-run]

Snapshot shape
--------------
    {
      "checked_at": "2026-11-15 12:14 WAT",
      "page": {"consultation": {"status": "live", "price": "$40 / 30 min",
                                "views": 3, "orders": 0},
               "red-team": {...}, "chatbot": {...}, "profile": {...}}
    }

Every key present is compared. A key that disappears is reported as removed,
because a field that stops rendering is the change most worth knowing about.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EMPIRE = os.path.abspath(os.path.join(HERE, ".."))
WATCH = os.path.join(EMPIRE, "STATE", "LINK_WATCH.json")
CHECKS = os.path.join(EMPIRE, "STATE", "LINK_CHECKS")


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1, ensure_ascii=False)
        fh.write("\n")


def today_wat() -> str:
    """The owner's date, not the sandbox's. UTC+1 all year, no daylight saving."""
    return (dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=1)).strftime("%Y-%m-%d")


def now_wat() -> str:
    return (dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M WAT")


def diff_pages(old: dict, new: dict) -> list[str]:
    moves: list[str] = []
    for page in sorted(set(old) | set(new)):
        if page not in old:
            moves.append(f"{page}: new page in this record")
            continue
        if page not in new:
            moves.append(f"{page}: dropped out of the record")
            continue
        a, b = old[page], new[page]
        for key in sorted(set(a) | set(b)):
            if key not in b:
                moves.append(f"{page} {key}: removed (was {a[key]!r})")
            elif key not in a:
                moves.append(f"{page} {key}: added ({b[key]!r})")
            elif a[key] != b[key]:
                moves.append(f"{page} {key}: {a[key]!r} -> {b[key]!r}")
    return moves


def cmd_links(_args) -> int:
    data = load(WATCH)
    for key, link in data["links"].items():
        print(f"{key:14} {link['label']}")
        print(f"{'':14} {link['url']}")
        if link.get("note"):
            print(f"{'':14} {link['note']}")
    return 0


def cmd_show(_args) -> int:
    data = load(WATCH)
    print(f"rule {data['rule']}, last checked {data.get('last_checked') or 'never'}")
    base = data.get("baseline") or {}
    print(f"baseline taken {base.get('checked_at', 'none')}")
    for page, fields in (base.get("page") or {}).items():
        print(f"\n[{page}]")
        for k, v in fields.items():
            print(f"  {k}: {v}")
    return 0


def cmd_due(_args) -> int:
    data = load(WATCH)
    today = today_wat()
    last = data.get("last_checked")
    if last == today:
        print(f"R49: already checked today ({today}). One pass is the rule; a second read is traffic.")
        print("If the page changed since, say what changed and record it with --force.")
        return 1
    print(f"R49: due. Today is {today}, last check was {last or 'never'}.")
    print("Read the four pages once, build the snapshot, then: link_watch.py record <file>")
    return 0


def cmd_record(args) -> int:
    data = load(WATCH)
    snap = load(args.snapshot)
    today = today_wat()
    if data.get("last_checked") == today and not args.force and not args.dry_run:
        print(f"R49: refused. {today} is already recorded. Pass --force only if the pages moved since.")
        return 1
    if "page" not in snap:
        print("snapshot has no 'page' key; nothing to compare")
        return 2

    checked_at = snap.get("checked_at") or now_wat()
    base = data.get("baseline") or {}
    first = not base
    moves = diff_pages(base.get("page") or {}, snap["page"])

    lines = [
        f"# Link check, {today}",
        "",
        f"Rule R49. One pass. Recorded as `{checked_at}`, compared against "
        f"`{base.get('checked_at') or 'an empty baseline'}`.",
        "",
    ]
    if first:
        lines += ["## First record", "",
                  "No earlier baseline, so this is the reference every later check is diffed against.", ""]
    elif moves:
        lines += ["## What moved", ""] + [f"- {m}" for m in moves] + [""]
    else:
        lines += ["## Nothing moved", "",
                  "Every field is identical to the previous record. A flat day is a finding too: it means "
                  "the pages are not being seen rather than that they were read and rejected.", ""]

    lines += ["## Fields as read", "", "| page | field | value |", "|---|---|---|"]
    for page, fields in snap["page"].items():
        for k, v in fields.items():
            cell = str(v).replace("|", "\\|")
            lines.append(f"| {page} | {k} | {cell} |")
    lines += ["", f"Recorded by `TOOLING/link_watch.py` at {now_wat()}.", ""]

    report = os.path.join(CHECKS, f"{today}.md")
    if args.dry_run:
        print("\n".join(lines))
        return 0

    os.makedirs(CHECKS, exist_ok=True)
    with open(report, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    data.setdefault("first_baseline", base)
    data["baseline"] = {"checked_at": checked_at, "page": snap["page"]}
    data["last_checked"] = today
    data.setdefault("history", []).append({
        "date": today, "checked_at": checked_at, "file": f"STATE/LINK_CHECKS/{today}.md",
        "changes": 0 if first else len(moves), "first": first,
    })
    save(WATCH, data)

    if first:
        print(f"recorded {report} as the first baseline; later checks diff against it")
        return 0
    print(f"recorded {report} ({len(moves)} change(s))")
    for m in moves:
        print(f"  {m}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="R49 daily check on the four Upwork links")
    ap.add_argument("command", choices=["links", "due", "show", "record"])
    ap.add_argument("snapshot", nargs="?")
    ap.add_argument("--force", action="store_true", help="allow a second record on the same day")
    ap.add_argument("--dry-run", action="store_true", help="print the report, write nothing")
    args = ap.parse_args(argv)

    if not os.path.exists(WATCH):
        print(f"missing watchlist: {WATCH}")
        return 2

    if args.command == "record" and not args.snapshot:
        print("record needs a snapshot file")
        return 2
    return {"links": cmd_links, "due": cmd_due, "show": cmd_show, "record": cmd_record}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
