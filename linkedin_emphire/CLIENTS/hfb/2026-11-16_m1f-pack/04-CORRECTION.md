---
deliverable: pack-correction
id: 2026-11-16_m1f-pack-correction
date: 2026-11-16
audience: collaborator
status: ready
approved: no
contents: the reviewer's finding on the previous-change record, what produced it, and two further defects found while checking it
---

# Correction to the M1f pack

Behar Dalipi, 16 November 22:48: the zip hash matches, the targeted rerun reproduces f23, f24 and
f25 on M1f, and `02-previous-change/revision.txt` labels the tree M1e while listing the M1d hashes.
He is right, and checking it turned up two more things that affect how the pack should be read.
Nothing here changes the code, the mode count or the verdict.

## What he found

`02-previous-change/revision.txt` said:

```
837ca42d94d9bfeaee088303ec5f8ea413c782b307feddf2a1fd0596ccebcc90  bench/store.py
f4204cccb64b53873152a9f905d4e36c44bdeb09503a92c3b5b2e7bcdb8d98c1  audit/regressions.py
b20b4a87801d2df7c722417cef7e4bb0060c5981dbba6c9f57470eeb5a8a68a1  audit/README.md
revision: M1e, the tree cleared at 21:42 on 16 November
```

The first two are the M1d tree, which is what the M1d pack's own revision record carries:
`837ca42d` for `bench/store.py` and `f4204ccc` for `audit/regressions.py`. The third is the
README, which was never edited between the base tree and M1e, so `b20b4a87` is correct for both.

The label is right and the hashes are wrong. The values are what a hash pass taken before the M1e
patch was applied produces, and that is the most likely mechanism: the previous-change record was
generated against the tree that happened to be standing, and the label above it was written from
the intent rather than from the tree.

**The M1e hashes, rebuilt from the chain and verified on this machine:**

```
9070f970ff401c07e8547307e2ac880ddf5352d452bb80d5de017f39f930a5b0  bench/store.py
1c246c61f2e34aeaf1612901b3b8ddd88aa9472154be8113fd57005aa6ec1812  audit/regressions.py
b20b4a87801d2df7c722417cef7e4bb0060c5981dbba6c9f57470eeb5a8a68a1  audit/README.md
```

`02-previous-change/revision.txt` now carries those three lines and says plainly which tree they
describe and which tree they replaced.

## What the tree question cannot be answered from

He asked which checkout produced `02-previous-change/f25.log`. The log cannot answer that, and the
reason matters more than the answer: **f25 produces byte-identical output on M1d, M1e and M1f.**

Run on this machine on 16 November, each against a rebuilt tree, in `05-f25-tree-check/`:

| tree | `bench/store.py` | f25 output |
|---|---|---|
| M1d | `837ca42d` | caught, 44 bytes, 341 to 297, gap None |
| M1e | `9070f970` | caught, 44 bytes, 341 to 297, gap None |
| M1f | `0989c8db` | caught, 44 bytes, 341 to 297, gap None |

All three runs are byte-identical to both logged copies, and the two logged copies are identical to
each other. That is expected rather than suspicious: f25's case is a genuinely torn line, the resync
defect that M1e fixed was about a *complete* record missing its terminator, so no revision in this
chain touches the torn-line path. The consequence is worth stating flatly. **f25 documents behaviour
that none of these revisions changed, and it separates none of them.** The mode that separates M1e
from M1d is f24, not f25.

The claim in the readme that the two revision files mean "the two trees cannot be confused" was too
strong. They could be, and one of them was.

## The patch is a diff from M1d, not from M1e

Found while rebuilding the tree to check the hashes. `03-this-change/patch.diff` contains the
`_gap_from_tail` guard and the `_resync` refusal, which are M1e's change, so its base side is M1d:

```
python3 -m patch -p1 < 03-this-change/patch.diff     # on M1e
  2 out of 3 hunks FAILED in bench/store.py
  1 out of 3 hunks FAILED in audit/regressions.py
```

Applied to M1d instead, it reproduces the M1f tree exactly: `0989c8db`, `490de706`, `ae147a28`.

So the reconstruction chain is `base 99f25cab` → M1d patch → M1f patch. M1e is in the lineage and
its fix is inside the M1f patch, but applying M1e first and M1f second does not work. That is why
the readme now states the chain rather than leaving it to be inferred.

## What does not change

`bench/store.py` still differs from M1e only in its module docstring, verified by diff on the
rebuilt trees: seven lines added, no code line touched. Twenty-two modes, 22 caught, 0 missed, and
`verify.py` ends on `VERDICT: every check holds`, both re-run on the rebuilt M1f tree to build the
snapshot below.

The mode count, the case numbers and the claim about the refusal guarantee stand as delivered.
