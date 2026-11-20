#!/bin/sh
# Regenerate the evidence from two checkouts, and refuse to write a pack that contradicts itself.
#
#   ./rebuild.sh /path/to/previous-change /path/to/this-change
#
# It expects, and stops if it does not get:
#
#   new-cases probe, previous change   exit 2, case C duplicates a sequence number, case D loses the gap
#   new-cases probe, this change       exit 0, every check holds
#   two-cases probe, this change       exit 0, the 15 November cases unchanged
#   cut probe, this change             exit 0, the property at 5 of 5 cuts
#   audit, this change                 exit 0, twenty-two of twenty-two caught
#   suite, this change                 verify.py exit 0 and "every check holds"
set -u
PREV=${1:?usage: rebuild.sh <previous-change> <this-change>}
CHG=${2:?usage: rebuild.sh <previous-change> <this-change>}
HERE=$(cd "$(dirname "$0")" && pwd)

fail() { echo "REFUSED: $1" >&2; exit 1; }

python3 "$HERE/harness/probe_new_cases.py" --repo "$PREV" --json "$HERE/02-previous-change/new-cases.json" \
  > "$HERE/02-previous-change/new-cases.log" 2>&1
[ "$?" = "2" ] || fail "the previous change did not fail the two cases, so there is nothing to fix"
grep -q "c_unique_seq *FAIL" "$HERE/02-previous-change/new-cases.log" || fail "case C did not fail on the previous change"
grep -q "d_gap_on_restart_2 *FAIL" "$HERE/02-previous-change/new-cases.log" || fail "case D did not fail on the previous change"

python3 "$HERE/harness/probe_new_cases.py" --repo "$CHG" --json "$HERE/03-this-change/new-cases.json" \
  > "$HERE/03-this-change/new-cases.log" 2>&1
[ "$?" = "0" ] || fail "the two cases do not hold on this change"
grep -q "both cases hold" "$HERE/03-this-change/new-cases.log" || fail "the probe did not say both cases hold"

python3 "$HERE/harness/probe_two_cases.py" --repo "$CHG" --json "$HERE/03-this-change/two-cases.json" \
  > "$HERE/03-this-change/two-cases.log" 2>&1
[ "$?" = "0" ] || fail "the cases of 15 November no longer hold"

python3 "$HERE/harness/probe_conflict_crash.py" --repo "$CHG" --json "$HERE/03-this-change/probe.json" \
  > "$HERE/03-this-change/probe.log" 2>&1
[ "$?" = "0" ] || fail "the cut probe does not hold"

( cd "$CHG" && python3 audit/regressions.py > "$HERE/03-this-change/regressions.log" 2>&1 ) \
  || fail "the audit did not pass on this change"

( cd "$CHG" && rm -rf artifacts && python3 run.py > "$HERE/03-this-change/suite-run.log" 2>&1 ) \
  || fail "run.py failed"
run=$(cd "$CHG" && ls artifacts | tail -1)
( cd "$CHG" && python3 verify.py "artifacts/$run" > "$HERE/03-this-change/suite-verify.log" 2>&1 ) \
  || fail "verify.py did not exit 0"
grep -q "every check holds" "$HERE/03-this-change/suite-verify.log" || fail "the verifier did not say every check holds"

( cd "$HERE" && find . -type f ! -name 05-SHA256SUMS.txt ! -name '*.zip' ! -name '*.pyc' | sort \
    | xargs sha256sum > 05-SHA256SUMS.txt )

echo "pack rebuilt from the two checkouts named above."
