#!/usr/bin/env python3
"""Read the clock, and print the line that goes into a deliverable.

    python3 TOOLING/clock.py                # the reading, then a paste-ready time_checked block
    python3 TOOLING/clock.py --date         # just the date, for a filename or a front-matter date
    python3 TOOLING/clock.py --line         # just the time_checked block
    python3 TOOLING/clock.py --utc          # both zones, when the reader is not in Lagos

Why this exists: every rule in this repo about dates assumes somebody read one. A draft written on
Saturday and delivered on Sunday carries Saturday's date unless a person checks, and the failure is
quiet, because the file looks finished. So the reading is one command, and the output is already in
the shape the gate wants.

WAT is UTC+1 all year. Nigeria has no daylight saving, so there is no ambiguity to reason about.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta, timezone

WAT = timezone(timedelta(hours=1))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Read the clock and print the time_checked block.")
    ap.add_argument("--date", action="store_true", help="print only the date in WAT")
    ap.add_argument("--line", action="store_true", help="print only the front-matter block")
    ap.add_argument("--utc", action="store_true", help="also print the UTC reading")
    ap.add_argument("--source", default="the system clock in the sandbox",
                    help="what was read, for the record: the system clock, the owner's handset, ...")
    args = ap.parse_args(argv)

    now = datetime.now(WAT)
    label = "%Y-%m-%d %H:%M WAT"
    if args.date:
        print(now.strftime("%Y-%m-%d"))
        return 0

    block = "time_checked: >-\n  checked: %s, read from %s before this file was sent for gate." % (
        now.strftime(label), args.source)
    if args.line:
        print(block)
        return 0

    print(now.strftime("WAT   %Y-%m-%d %H:%M %A"))
    if args.utc:
        print(datetime.now(timezone.utc).strftime("UTC   %Y-%m-%d %H:%M %A"))
    print()
    print(block)
    return 0


if __name__ == "__main__":
    sys.exit(main())
