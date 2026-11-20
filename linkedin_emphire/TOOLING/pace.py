#!/usr/bin/env python3
"""Read the ledgers and say where the pace is, in one screen.

The repo has a follower log with one row in it and a performance tracker with
snapshots. Neither says anything on its own. This reads them and answers the
three questions the plan turns on: how fast it is going, what that projects to
on 25 December, and which checkpoint is about to be missed.

Run it at the start of a session. It is the only thing in the repo that converts
effort into a verdict.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "analytics" / "follower-log.md"

START_DATE = dt.date(2026, 11, 6)
START_FOLLOWERS = 1007
TARGET_DATE = dt.date(2026, 12, 25)
TARGET_FOLLOWERS = 5007
CHECKPOINTS = [
    (dt.date(2026, 11, 15), 1600, "the 5,000 target is arithmetically gone; decide that day, not on 20 December"),
    (dt.date(2026, 11, 29), 2600, "the series is not converting; change the series, not the effort"),
    (dt.date(2026, 12, 13), 3300, "stop posting more; put the hours behind the two things that brought followers"),
]

ROW = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([\d,]+)\s*\|", re.M)


def rows() -> list[tuple[dt.date, int]]:
    if not LOG.exists():
        return []
    return sorted(
        (dt.date.fromisoformat(d), int(n.replace(",", "")))
        for d, n in ROW.findall(LOG.read_text(encoding="utf-8"))
    )


def main() -> int:
    today = dt.date.today()
    data = rows()
    print()
    print("PACE")
    print("=" * 68)

    if not data:
        print("  No rows in analytics/follower-log.md. Nothing can be said.")
        print("  One line: date | followers | net | posts | comments | best impression | what brought them")
        return 1

    last_date, last_n = data[-1]
    since = max((today - START_DATE).days, 1)
    needed_now = (TARGET_FOLLOWERS - START_FOLLOWERS) / max((TARGET_DATE - START_DATE).days, 1)
    gained = last_n - START_FOLLOWERS
    actual = gained / since
    left_days = max((TARGET_DATE - today).days, 0)
    left_followers = max(TARGET_FOLLOWERS - last_n, 0)

    print(f"  last row           {last_date} ({last_n:,} followers, {(today - last_date).days} day(s) old)")
    print(f"  gained since 6 Nov {gained:+,} over {since} days, {actual:+.1f}/day")
    print(f"  required           {needed_now:+.1f}/day across the whole 49 days")
    if left_days:
        print(f"  required from here {left_followers / left_days:+.1f}/day for the {left_days} days left")
        projected = last_n + actual * left_days
        verdict = "on pace" if projected >= TARGET_FOLLOWERS else f"short by {TARGET_FOLLOWERS - projected:,.0f}"
        print(f"  projected 25 Dec   {projected:,.0f} at the current rate  ->  {verdict}")
    else:
        print("  the target date has passed")

    print()
    print("CHECKPOINTS")
    for when, want, meaning in CHECKPOINTS:
        days = (when - today).days
        state = "passed" if days < 0 else ("today" if days == 0 else f"in {days} days")
        hit = last_n >= want
        print(f"  {when}  need {want:,}  {'met' if hit else 'not met'}  ({state})")
        if not hit and days <= 14:
            print(f"      -> {meaning}")

    if last_date != today:
        print()
        print(f"  The log has no row for {today}. That is the habit the plan depends on, and it")
        print("  takes thirty seconds: followers, net, posts, comments, best impression, what brought them.")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
