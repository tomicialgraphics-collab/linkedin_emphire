---
deliverable: correction-note
id: F9b-CORRECTION-02
date: 2026-11-06
audience: external
status: ready
approved: no
profile_checked: >-
  Evelyne-Claudia Yantony, read from her correspondence of 2026-11-06 and from the earlier exchange:
  she separates artifact correspondence from independent reproduction, treats a withdrawal as its own
  event distinct from acknowledgment and from validation, and asks for the version identifier before
  extending any finding. The note therefore answers in her own three categories rather than merging
  them, and every number below is lifted from run/result.json rather than restated from memory.
thread: F9b, two corrections to the comparison, the benchmark pin, and what stays unmeasured
---

# F9b, correction 02

Two corrections, both yours. The page itself is unchanged and its hash still identifies it. This note
is the corrected version of the two sentences, with the values taken from `run/result.json`.

## 1. The indistinguishability sentence is withdrawn as written

I wrote: *the two worlds are identical only to an observer holding the reply and the host journal.*
That is broader than the evidence, exactly as you say, and the run contradicts it.

Measured across the pair that was actually run:

| surface | control, write accepted | injected, annotation refused |
| --- | --- | --- |
| reply to the second verdict | `ok: true, stored: true, state: "conflicted", conflict: true, conflict_seq: 6` | `ok: false, durable: false` |
| journal | two verdict records and two conflict records | two verdict records, no conflict record |
| host problem list | one entry | four entries |

So the reply differs, the journal differs, and the host's own diagnostic list differs. What is
identical is narrower: the three host event kinds, `wal_commit`, `reply_rejected` and
`effect_withheld`, and the withholding reason, which is `store reply rejected` in both cells.

The sentence that survives is this one. Across the pair that was run, identity holds at the host event
kinds and the withholding reason and nowhere else. What the refused reply fails to do is name which
write was refused: it says `durable: false` while two verdict records sit on disk, and its error text
names a verdict write when the write refused was the conflict annotation.

## 2. The two paths do not carry the same pair of records

You are right, and the page's table let the wire journal stand for both paths. Named properly:

**Wire cells.** Sequence 4 is a verdict, `BLOCK`, rule `R7`, decision time 4, descriptor `…1111`.
Sequence 5 is a verdict, `ALLOW`, rule null, decision time 5, the same descriptor. The disagreement is
in the verdict value.

**Host cells.** Sequence 4 is a verdict, `BLOCK`, rule `R7`, decision time 4, descriptor `…1111`.
Sequence 5 is a verdict, `BLOCK`, rule `R7`, decision time 2, descriptor `3e76ead0…`. Both records say
BLOCK. The disagreement is in the descriptor and the timestamp. Sequence 4 is the verdict the host had
already recorded, which the run states by naming it as the seeded verdict at that sequence, and
sequence 5 is the record the command under test wrote, carrying the earlier decision time and the
other descriptor.

Both pairs are two different verdicts for one action id, which is why the same rule text applies in
both, and they are not the same difference. A comparison across worlds has to say which of the two it
is comparing, and I did not.

## 3. The retry

Agreed, and I will not put it more strongly than you have. The retry is issued by the test script, which
runs every cell the same way. Nothing here observes a client, an operator or a runbook. The finding is only that the reply
invites the retry while denying the durable write, and the invitation is the whole of it.

## What these corrections leave standing

Finding 1, the reply is false about durability, is unaffected: two verdict records were fsynced before
the refusal, and both frame digests recompute.

Finding 2, the event class collapses, is unaffected: a conflict between two signed verdicts reaches
the host as a storage failure with the reason `store reply rejected`.

Finding 3, the annotation is lost and the state is not, is unaffected: replay recomputes `conflicted`
from the two differing verdicts alone, which is why the journal, not the reply, settles the question.

## What is still not measured

The benchmark's own failpoint refuses a verdict write. I never ran that world. So I have no measured
comparison between a genuine verdict refusal and the conflict refusal, and my claim is not that the
two are indistinguishable. It is the smaller one the reply itself supports: the refused conflict write
is reported in the words of a refused verdict write. If a comparison of the two refusals is wanted,
that is a new cell and a new run, and I would rather measure it than argue it.
