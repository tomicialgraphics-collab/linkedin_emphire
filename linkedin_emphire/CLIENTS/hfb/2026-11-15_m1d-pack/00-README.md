---
deliverable: pack-readme
id: 2026-11-15_m1d-pack-readme
date: 2026-11-15
audience: collaborator
status: ready
approved: no
contents: the three findings of 22:10, what caused them, and the regression that now exercises them
---
# M1d: the verdict retry, the conflict pointer, and a read that failed

Behar's message of 15 November at 15:10 found three things. All three reproduced.

**One. A conflict was pointed at the wrong verdict.** `cmd_verdict` builds the conflict record
from `self.verdicts` and `self.journal.seq`, both held in memory. After an unconfirmed rollback the
memory disagrees with the file: a verdict can be on disk and not in the index, and the sequence
counter can lag. So the conflict carried `second_seq = 3` while the verdict it was raised against
was written at 4. The same composition also produced conflicts naming a record that replay
withholds, which is worse: a conflict whose second half the reader cannot find.

**What changed.** The store marks itself stale when a write ends in an unknown state, and reloads
its index from the journal before it composes anything, not only before it writes. The reload sits
at the top of `handle()`, because the number of the record being written is read from memory at the
moment the conflict is built.

**Two. A failing recovery read was answered with an acknowledgement.** `_resync()` caught the
`OSError` from its own read, returned a size, and let the append continue. The store then
acknowledged a write, and reused a sequence number, having just failed to read the file it was
supposed to be resynchronising with. That is the worst shape of error in this store: a reply that
claims more than the process knows.

**What changed.** A failed recovery read raises `JournalStateUnknown`. The reply is
`durable: unknown`, `disk_state: unknown`, and the write does not happen. The same write, retried
once the read works, succeeds and takes the correct number.

**Three. The regression did not exercise any of it.** It does now.

## The new mode: f23

Two cases in one mode, because they are the two halves of the same question: what may the store do
after it has admitted it does not know?

*Case A, verdict retry.* Issue, first verdict, then a second differing verdict whose pair write is
cut with the rollback refused, then the same second verdict retried. The check requires the
conflict to name two records that are both on disk and both kept by replay, that the first number
it names is the stored first verdict, and that the second is the verdict the conflict was raised
against.

*Case B, recovery read.* The same unconfirmed rollback, then a read that raises EIO. The check
requires the next write to be refused as unknown, and to succeed once the read works.

| | on `ee42139c` (delivered) | on this change |
|---|---|---|
| f23 | MISSED. Conflict names 2 and 3 while the verdict is at 4. Failed read answered as an acknowledgement. | caught. Conflict names 2 and 4. Failed read answered unknown. |
| audit | 22 modes | 23 modes, all caught |
| suite verifier | unchanged | `VERDICT: every check holds` |

## Hashes

| | |
|---|---|
| `bench/store.py` before | `99f25cab23b3dea0f6f739a96fae23bc25bbc3d0a0db96e801ac7d701ae1f982` |
| `bench/store.py` after | `837ca42d94d9bfeaee088303ec5f8ea413c782b307feddf2a1fd0596ccebcc90` |
| `audit/regressions.py` after | `f4204cccb64b53873152a9f905d4e36c44bdeb09503a92c3b5b2e7bcdb8d98c1` |
| patch | `ebaaea3dc06f55fc03755ce6c84c5bfbe15729b99fd794ba94d943ef465f2c6f` |

The patch applies to the pinned baseline and was re-applied to a clean copy, producing both hashes
above byte for byte.

## What is in each folder

| item | file |
|---|---|
| f23 on the revision you hold, failing | `02-previous-change/f23.log` |
| f23 on this change, passing | `03-this-change/f23.log` |
| all twenty-three modes on this change | `03-this-change/regressions.log` |
| the suite verifier on this change | `03-this-change/suite-verify.log` |
| the diff | `03-this-change/patch.diff` |
| hashes and the revision each folder is | `*/revision.txt`, `05-SHA256SUMS.txt` |

## What this does not claim

Nothing about the timing or the signing of verdicts, and nothing about any store other than this
one at these hashes. It also does not claim the store is now correct: it claims the three things
reported on 15 November are fixed and that a check now fails if they come back.
