#!/usr/bin/env python3
"""Wilson score interval for a count out of a number of trials.

    python3 tools/wilson.py 3 20
    3 of 20  =  15.0%  (95% CI 5.2% to 36.0%)

Why Wilson rather than the textbook normal approximation: attack success rates
are usually small and the sample is usually small, and the normal approximation
produces intervals that go below zero and collapse to a point at 0 and 1.
Wilson does neither, which matters when the honest answer is "we saw no
successes in twenty attempts" and the report needs to say what that is worth.
"""

from __future__ import annotations

import argparse
import math
import sys


def wilson(successes: int, trials: int, z: float = 1.96) -> tuple[float, float, float]:
    if trials <= 0:
        raise ValueError("trials must be positive")
    if not 0 <= successes <= trials:
        raise ValueError("successes must be between zero and trials")
    p = successes / trials
    denom = 1 + z * z / trials
    centre = (p + z * z / (2 * trials)) / denom
    margin = z * math.sqrt(p * (1 - p) / trials + z * z / (4 * trials * trials)) / denom
    return p, max(0.0, centre - margin), min(1.0, centre + margin)


def main() -> int:
    ap = argparse.ArgumentParser(description="Wilson interval for a success rate")
    ap.add_argument("successes", type=int)
    ap.add_argument("trials", type=int)
    ap.add_argument("--z", type=float, default=1.96, help="1.96 for 95%%, 2.576 for 99%%")
    args = ap.parse_args()

    try:
        p, low, high = wilson(args.successes, args.trials, args.z)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(f"{args.successes} of {args.trials}  =  {p:.1%}  (95% CI {low:.1%} to {high:.1%})")
    if args.successes == 0:
        print("no successes observed, which is not the same as no risk. Report the upper bound.")
    if args.successes == args.trials:
        print("no failures observed, which is not the same as no failure. Report the lower bound.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
