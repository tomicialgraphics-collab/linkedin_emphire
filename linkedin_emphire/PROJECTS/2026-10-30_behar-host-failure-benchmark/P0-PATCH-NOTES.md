# P0 patch: what is in it, and the evidence it works

Against `Teamthy/host-failure-benchmark` at commit `25cd57f`, the commit the
audit reviewed. Two forms, same content:

- `host-failure-benchmark-p0.patch`, a `git diff` that applies cleanly to
  `25cd57f` with `git apply`
- `../host-failure-benchmark-p0.zip`, the same tree unpacked, if you would
  rather replace the folder than patch it

Nothing here is committed to the repository under review. It applies to a
clean clone at `25cd57f` and to nothing else.

## What changed

| change | finding it closes |
| --- | --- |
| WAL records and recovered verdicts are signature-checked, at ingest in the store and in the verifier. An unverified record is stored and visible, and cannot resolve a gap, in `recompute_gaps` as well as in the store | F1, F3, F9 |
| The actor and the policy hash are compared against the constants already in `bench/common.py`, and the decision timestamp has to match a counter step in the host journal | F8, F14, F2 |
| `run.py` writes a versioned manifest naming every required artifact, and the verifier checks each scenario's event chain. A missing journal is a failure, not a scenario with nothing to say | F5 |
| The verifier never raises. An unreadable artifact produces a report with an explicit unreadable state, and a report is written either way | F13 |
| Two claims in the note are corrected, and one phrase: the store registers identifiers rather than issuing them, the suite runs eight scenarios and not nine, and row M3 is a deliberate exit rather than a kill | F6, F16, F4 (scope) |

## The evidence

`audit/regressions.py` in the patch is the seven counterexamples, one mode
each, named after the findings. Each mode copies the tree into a temporary
directory, applies one change and reports whether the checks caught it.

Run against the tree as reviewed, and against the patched tree:

| mode | at `25cd57f` | with the patch |
| --- | --- | --- |
| f1 WAL verdict flipped, stale signature | accepted, no check failed | caught by `B` |
| f2 WAL timestamp only | caught by `B.wal` | caught by `B.wal` |
| f3 unsigned verdict, reframed | gap erased | gap stays named |
| f5 seven host journals deleted | accepted, no check failed | caught by `artifacts-complete` |
| f8 actor and policy rewritten, re-signed | accepted, no check failed | caught by `D` |
| f13 host journal cut mid-line | traceback, no report | caught by `artifacts-parse`, report written |
| f14 timestamp set to an epoch value, re-signed | accepted, no check failed | caught by `D` |

f2 is the one the report reads differently from the code. Changing only the
WAL timestamp already failed `B.wal` before the patch, so nothing needed
fixing there, and the regression pins that behaviour so the report's version
of it cannot come back in a later rewrite.

## The rest of the suite still passes

Run from a clean clone of `25cd57f` with the patch applied:

```
python3 run.py                    # completes
python3 verify.py example/run     # VERDICT: every check holds
python3 challenge.py example/run  # every one of the nine mutations caught
python3 audit/regressions.py      # every counterexample caught
```

The check count went from 14 to 16. Class P is still 8 of 8 and Class V is
still 2 of 2; the two new checks are `artifacts-complete` and `scenarios-ran`,
and `artifacts-parse` appears only when something is unreadable. Two runs of
the suite are still byte-identical, checked file by file.

`example/run` is regenerated, because the artifacts changed shape: verdict
records now carry the state the store computed, and the manifest is version 2
with a required-artifacts list. The old example would fail the new checks,
which is the correct outcome and the reason the patch ships a new one rather
than leaving the old one to look like a regression.

## What this does not fix

These are the P1 and P2 items, and they are still open:

- the store updates memory before the journal append in one path, so an
  acknowledged state can be lost on restart (F11)
- repair truncates the journal without keeping the bytes it discarded (F7)
- duplicate verdicts still resolve to whichever record a component reads first
  (F9, the state half of it; the conflict state is not built)
- the host still does not validate the store's reply before logging an effect
  (F10)
- identifiers are still chosen by the caller; this patch renames the claim, it
  does not mint the id (F6)
- an idle socket can still block the store (F15)
- the verifier still imports the encoder it is checking (5.4 of the audit). It
  is smaller now, since the state and the constants are checked independently,
  but the correlated-oracle problem stays until there is a second encoder
- no CI matrix, so the cross-platform claim is now written as what it is: run
  on both, compared by hand, no published digest trail

## Windows

The first version of `audit/regressions.py` found the run directory by parsing
what `run.py` printed, which uses a backslash on Windows, and it stopped with
`run.py produced no artifact directory` there. It now finds the directory by
listing `artifacts/` before and after the run, which needs no separator at all.
Everything else was already portable: the patch applied to `25cd57f` on
Windows, and `verify.py`, `challenge.py` and the nine built-in mutations all
passed there before this fix.

If you already applied the patch, take the fixed file only:

```powershell
Invoke-WebRequest -Uri "$base/2026-10-30_behar-host-failure-benchmark/regressions.py" -OutFile audit\regressions.py
```

## Applying it

```
git clone https://github.com/Teamthy/host-failure-benchmark
cd host-failure-benchmark
git checkout 25cd57f
git apply /path/to/host-failure-benchmark-p0.patch
python3 verify.py example/run
python3 audit/regressions.py
```

If the patch does not apply, the tree has moved. Send me the commit and I will
rebase it rather than have you resolve a conflict in a file you did not write.
