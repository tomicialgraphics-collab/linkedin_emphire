#!/bin/sh
# Regenerate 02 and 03 from two checkouts, and refuse to write a pack that does not reproduce.
#
#   ./rebuild.sh /path/to/pinned-checkout /path/to/patched-checkout
#
# It expects, and stops if it does not get:
#
#   probe on the pinned tree      exit 2, two named failing cuts: line-4 and mid-final-line
#   probe on the patched tree     exit 0, every cut holds
#   suite on either tree          run.py then verify.py, verify exits 0, "every check holds"
#   verifier outputs              byte-identical between the two trees
#
# A pack built by a script that cannot fail is a pack that proves nothing.
set -u

BASE=${1:?usage: rebuild.sh <pinned-checkout> <patched-checkout>}
CHG=${2:?usage: rebuild.sh <pinned-checkout> <patched-checkout>}
HERE=$(cd "$(dirname "$0")" && pwd)

fail() { echo "REFUSED: $1" >&2; exit 1; }

echo "== baseline probe"
python3 "$HERE/harness/probe_conflict_crash.py" --repo "$BASE" --json "$HERE/02-baseline-failure/probe.json" \
  > "$HERE/02-baseline-failure/probe.log" 2>&1
code=$?
[ "$code" = "2" ] || fail "baseline probe exited $code, expected 2"
grep -q "2 of 5 cuts leave the store reporting a conflict it cannot name" "$HERE/02-baseline-failure/probe.log" \
  || fail "baseline probe did not name a failing cut"
grep -q "line-4 at byte" "$HERE/02-baseline-failure/probe.log" \
  || fail "baseline probe did not fail at the write-boundary cut this pack describes"
grep -q "mid-final-line at byte" "$HERE/02-baseline-failure/probe.log" \
  || fail "baseline probe did not fail at the torn-write cut this pack describes"

echo "== change probe"
python3 "$HERE/harness/probe_conflict_crash.py" --repo "$CHG" --json "$HERE/03-change/probe.json" \
  > "$HERE/03-change/probe.log" 2>&1
code=$?
[ "$code" = "0" ] || fail "change probe exited $code, expected 0"

echo "== suite on both trees"
for tree in "$BASE" "$CHG"; do
  ( cd "$tree" && rm -rf artifacts && python3 run.py > "$HERE/$( [ "$tree" = "$BASE" ] && echo 02-baseline-failure || echo 03-change )/suite-run.log" 2>&1 ) \
    || fail "run.py failed on $tree"
  run=$(cd "$tree" && ls artifacts | tail -1)
  ( cd "$tree" && python3 verify.py "artifacts/$run" \
      > "$HERE/$( [ "$tree" = "$BASE" ] && echo 02-baseline-failure || echo 03-change )/suite-verify.log" 2>&1 ) \
    || fail "verify.py did not exit 0 on $tree"
done

echo "== the two verifier outputs"
if ! diff -q "$HERE/02-baseline-failure/suite-verify.log" "$HERE/03-change/suite-verify.log" >/dev/null; then
  fail "the verifier output differs between the revisions, so the change touched a mode"
fi

echo "== hashes"
{
  echo "revision"
  echo "  repository: Teamthy/host-failure-benchmark"
  echo "  commit: $(cd "$BASE" && git rev-parse HEAD)"
  echo "  file the change applies to: bench/store.py"
  echo "  sha256 at this revision: $(sha256sum "$BASE/bench/store.py" | cut -d' ' -f1)"
  echo "  sha256 after the patch:  $(sha256sum "$CHG/bench/store.py" | cut -d' ' -f1)"
  echo "  patch sha256: $(sha256sum "$HERE/03-change/patch.diff" | cut -d' ' -f1)"
} > "$HERE/02-baseline-failure/revision.txt"

( cd "$HERE" && find . -type f ! -name 05-SHA256SUMS.txt ! -name '*.pyc' | sort \
    | xargs sha256sum > 05-SHA256SUMS.txt )

echo "pack rebuilt. Everything in it reproduced from the two checkouts named above."
