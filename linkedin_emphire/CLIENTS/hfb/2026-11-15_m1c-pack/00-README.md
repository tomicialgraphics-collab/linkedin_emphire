---
deliverable: pack-readme
id: 2026-11-15_m1c-pack-readme
date: 2026-11-15
audience: collaborator
status: ready
approved: no
contents: the two cases raised on 15 November, what covers them, and the check that had to change
---
# M1c: the two cases of 15 November, and the check that could not tell them apart

This pack answers the two cases the reviewer raised after the rebuild of 15 November, and the one
defect he named in the suite itself.

**The two cases.**

*Duplicate sequence numbers after an unconfirmed rollback.* A batch write stops halfway. One
whole record is on disk and half of the next is behind it. The rollback that should cut it back
is refused, so the store answers that it cannot tell what reached the disk. That answer is
correct. What followed it was not: the retry was numbered from memory, which never saw the record
already on disk, so the retry wrote a record carrying a `store_seq` that another record already
held. Two records with one number is a store that cannot say which came first.

*A malformed line before an unterminated final record.* The whole record at the end is readable
and is reported as a gap. A repair that removes the malformed line also removed that record, from
the journal and from the quarantine, and restart 2 saw a clean file. The gap went quiet, which is
worse than the gap.

**The check.** `custom_f21` asked one question of three different situations: did the store answer
`durable: false`. That collapses three states into one, as he said. It is now four named states,
and each is required to be true of the file rather than true of the wording:

| state | what it means | what is required of it |
|---|---|---|
| refused | the store answered, and says the bytes are not there | nothing else may be on disk |
| unknown | the store answered, and says it cannot tell | `disk_state: unknown` and a reason |
| acknowledged | the store answered, and says the record is stored | memory and the next restart agree |
| raised | the store said nothing | fails the check outright |

## The three revisions in this pack

| | file | sha256 |
|---|---|---|
| pinned baseline | `bench/store.py` at `126f1c00…` | `99f25cab23b3dea0f6f739a96fae23bc25bbc3d0a0db96e801ac7d701ae1f982` |
| previous change, delivered 15 November | the file the last pack produced | `b987cc49e186d9281ce86eca76a940319107002d4c5bc05d2ce362f7acc70085` |
| this change | same baseline plus `03-this-change/patch.diff` | `ee42139cab14fdb02dd82ad88d6421afc4af7a808cf0f561cc15f2db3a0bde85` |

`audit/regressions.py` changes as well: `68a87228fb13f46c1db0d65affd2320cf841c1c38ad7ad65fc65513d474f2db0`.
That is disclosed rather than buried. The change is the one he asked for, and a pack that quietly
edits the check that is meant to catch it would be worth nothing.

The patch applies to the pinned baseline and to nothing else. It was re-applied to a clean copy
and produced the two hashes above byte for byte.

## What is in each folder

| item | file | what it is |
|---|---|---|
| the previous change failing both cases | `02-previous-change/new-cases.log` | case C duplicates a sequence number, case D loses the record and the gap |
| | `02-previous-change/new-cases.json` | the same result as data |
| this change holding both | `03-this-change/new-cases.log` | every check holds |
| this change, the original two cases | `03-this-change/two-cases.log` | the 15 November cases still hold, unchanged |
| this change, the cut probe | `03-this-change/probe.log` | the property holds at 5 of 5 cuts |
| this change, the suite | `03-this-change/suite-run.log`, `03-this-change/suite-verify.log` | `VERDICT: every check holds` |
| this change, the audit | `03-this-change/regressions.log` | twenty-two of twenty-two counterexamples caught |
| the diff | `03-this-change/patch.diff` | `bench/store.py` and `audit/regressions.py` |
| environment | `01-environment.txt` | interpreter, platform, and how each run was made |

The pinned baseline is not re-run here. The pack of 15 November holds it, and neither new case
can be arranged on that revision: it has no unconfirmed-rollback state and no unterminated-tail
state, so both cases are reported as not applicable there rather than as passes.

## What changed in the code, in four sentences

The next append after an unconfirmed rollback re-reads the file, copies out and cuts the bytes that
never became a whole line, and takes its next number from the records that are actually there.
A repair that removes damaged bytes now writes the withheld tail back at the end of the journal and
copies it into the quarantine as well, so the gap is reported on every restart rather than
surviving exactly one. An append whose `open()` failed is reported as a refusal rather than as an
unknown state, because a file that was never opened cannot have taken a byte. The journal's own
partial-write failpoint and the probe that arms it are unchanged.

## How to check it without trusting this file

```
patch -p1 < 03-this-change/patch.diff          # against the pinned baseline
sha256sum bench/store.py audit/regressions.py  # ee42139c… and 68a87228…
python3 harness/probe_new_cases.py --repo .    # exit 0, both cases hold
python3 audit/regressions.py                   # exit 0, twenty-two of twenty-two
```

The first line of defence is that the same probe fails on the revision that was delivered on
15 November. It is in `02-previous-change/` and it was run to produce that file, not written by hand.
