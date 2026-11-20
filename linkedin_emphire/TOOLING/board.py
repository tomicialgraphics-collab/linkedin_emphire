#!/usr/bin/env python3
"""board.py - the four boards that say what is due, in one screen.

    python3 TOOLING/board.py            # everything
    python3 TOOLING/board.py --brief    # three lines, for the boot brief

Nothing here is a new ledger. It reads what already exists and answers the only
question a session start should answer: what is late, and what is due today.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = dt.date.today()
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def table_rows(path: Path, first_col: re.Pattern) -> list[list[str]]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("|"):
            row = cells(line)
            if row and first_col.match(row[0]):
                out.append(row)
    return out


def date_at(row: list[str]) -> dt.date | None:
    for c in row:
        if ISO.match(c):
            return dt.date.fromisoformat(c)
    return None


def pace_line() -> str:
    log = ROOT / "analytics" / "follower-log.md"
    rows = [r for r in table_rows(log, re.compile(r"^\d{4}-\d{2}-\d{2}$"))
            if len(r) > 1 and re.fullmatch(r"[\d,]+", r[1])]
    if not rows:
        return "pace        no follower rows at all"
    last = rows[-1]
    try:
        n = int(last[1].replace(",", ""))
    except (IndexError, ValueError):
        return "pace        last row is unreadable"
    d = dt.date.fromisoformat(last[0])
    age = (TODAY - d).days
    stale = " TODAY'S ROW IS MISSING" if d != TODAY else ""
    return f"pace        {n:,} on {d}, {age} day(s) ago{stale}"


def replies() -> tuple[list[str], list[str]]:
    path = ROOT / "STATE" / "REPLY-QUEUE.md"
    late, due = [], []
    for row in table_rows(path, re.compile(r"^\d{4}-\d{2}-\d{2}$")):
        if len(row) < 5:
            continue
        got = dt.date.fromisoformat(row[0])
        who = row[1] or "?"
        due_d = dt.date.fromisoformat(row[3]) if ISO.match(row[3]) else None
        state = row[4].lower()
        if state not in ("open", "drafted"):
            continue
        if due_d and due_d < TODAY:
            late.append(f"{who} asked {got}, was due {due_d}, still {state}")
        elif due_d and due_d == TODAY:
            due.append(f"{who} asked {got}, due today")
    return late, due


def borrowed() -> tuple[str, list[str]]:
    path = ROOT / "STATE" / "BORROWED-AUDIENCE.md"
    rows = table_rows(path, re.compile(r"^B\d+$"))
    if not rows:
        return "borrowed    no rows on the board", []
    prospect = sum(1 for r in rows if len(r) > 8 and r[8] == "prospect")
    pitched = [r for r in rows if len(r) > 8 and r[8] == "pitched"]
    week = TODAY - dt.timedelta(days=7)
    sent_recent = [r for r in pitched if len(r) > 6 and ISO.match(r[6]) and dt.date.fromisoformat(r[6]) >= week]
    lines = []
    for r in pitched:
        if len(r) > 7 and ISO.match(r[7]):
            due = dt.date.fromisoformat(r[7])
            if due <= TODAY:
                lines.append(f"{r[0]} {r[1]}: follow-up due {due}")
    flag = "" if len(sent_recent) >= 2 else " (R42 wants two a week)"
    return (f"borrowed    {len(pitched)} pitched, {len(sent_recent)} in the last 7 days, "
            f"{prospect} prospect(s){flag}"), lines


def case_studies() -> tuple[str, list[str]]:
    path = ROOT / "STATE" / "CASE-STUDY-INDEX.md"
    rows = table_rows(path, re.compile(r"^C\d+$"))
    if not rows:
        return "studies     no rows in the index", []
    waiting = [r for r in rows if len(r) > 4 and not r[4].startswith("granted")]
    lines = [f"{r[0]} {r[1]}: permission {r[4]}, {r[5] if len(r) > 5 else '?'}" for r in waiting]
    return f"studies     {len(rows)} row(s), {len(waiting)} awaiting permission", lines


def main(argv: list[str]) -> int:
    late, due = replies()
    b_line, b_due = borrowed()
    c_line, c_lines = case_studies()

    if "--brief" in argv:
        print(f"  {pace_line()}")
        print(f"  replies     {len(late)} late, {len(due)} due today")
        print(f"  {b_line}")
        print(f"  {c_line}")
        return 0

    print("BOARD")
    print("=" * 68)
    print(f"  {pace_line()}")
    print(f"  replies     {len(late)} late, {len(due)} due today")
    print(f"  {b_line}")
    print(f"  {c_line}")
    for group, items in (("LATE REPLIES", late), ("DUE TODAY", due), ("FOLLOW-UPS", b_due), ("PERMISSION", c_lines)):
        if items:
            print()
            print(f"  {group}")
            for it in items:
                print(f"    {it}")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
