---
deliverable: doc
id: 2026-11-15_m1c-classification-log
date: 2026-11-15
audience: collaborator
status: ready
approved: no
---
# Classification log, M1c

What moved, what did not, and how each claim was measured. Every line here was produced by a run,
not by reading the code and hoping.

## The two cases

### Case C, duplicate sequence numbers after an unconfirmed rollback

**Mechanism.** `append_batch` writes the whole blob in one call. With the partial-write failpoint
armed, half the blob reaches the disk: the first record complete with its terminator, the second
cut mid-line. The write raises, `_rollback` is refused by the failpoint, and `JournalStateUnknown`
is raised. The reply says `durable: unknown`, which is right.

The defect was what came next. `self.seq` had not advanced, because the batch was never
acknowledged. The next append therefore numbered itself from a counter that had never seen the
record already on disk, and wrote a record with the same `store_seq`.

**Fix.** A journal that has answered `unknown` marks the state. The next append or batch re-reads
the file before it numbers anything: it takes the highest `store_seq` present, copies the bytes
that never became a whole line into the quarantine, and cuts them. The block that established the
condition is `_resync()`; the two call sites are the first lines of `append` and `append_batch`,
which is the only place where numbering has not yet happened.

**Measured.** Previous change: `all_seq = [1, 2, 2]`, `c_unique_seq` FAIL. This change:
`all_seq = [1, 2, 3]`, `c_unique_seq` hold. Logs in `02-previous-change/` and `03-this-change/`.

### Case D, a malformed line before an unterminated final record

**Mechanism.** `replay()` reads the unterminated tail first and withholds it, which is why restart
1 reports it. A malformed line earlier in the file sets `bad`, and the repair path rewrote the file
from `good` alone. The withheld tail was in neither list. It was deleted from the journal, it was
not in the quarantine, and restart 2 saw a file that ended cleanly.

**Fix.** The repair now reads the withheld bytes before it rewrites, writes `good` plus those bytes,
and appends them to the quarantine file after the damaged bytes it already saved, with the offset
recorded in the quarantine record. The gap's `start` is updated to where the tail now sits, and the
quarantine file and offset are named in it.

**Measured.** Previous change: `d_gap_on_restart_2` FAIL, `d_record_in_journal` FAIL,
`d_record_in_quarantine` FAIL. This change: all nine checks hold, and the journal is byte-identical
between restarts 2 and 3, which is what stops the evidence from being consumed by a second repair.

### The check that could not tell them apart

`custom_f21` tested `reply["durable"] is False` for all three situations it arranges. With an
unconfirmed rollback in the code, two of those situations answer `unknown`, and the check read that
as a failure to answer. It also let a false `refused` through, because nothing compared the claim
to the file.

**Now.** Four named states, and a requirement on each: `refused` only if the bytes are absent from
the journal, `unknown` only with `disk_state: unknown` and a reason, `acknowledged` only if memory
and the next restart agree, `raised` never. The rollback-failure case is arranged without the
journal's failpoint, by a file object that takes half a line and by refusing the `+` mode the
rollback needs, so the same case runs on the pinned baseline and on any change to it.

**Measured.** This change: `22 of 22` caught. The revision delivered on 15 November, under the
revised check: `f21 MISSED`, because it answered `unknown` when `open()` had failed and nothing
could have been written, and because its retry reused a number.

## What did not move

The verifier output for the suite is byte-identical to the one in the pack of 15 November
(`diff` of `03-this-change/suite-verify.log` against that pack's copy returns nothing), and it ends
`VERDICT: every check holds`. The cut probe still holds at 5 of 5 cuts. The two cases delivered on
15 November still hold, unchanged, in `03-this-change/two-cases.log`.

The other twenty-one audit modes are untouched and are caught in the same run:
`03-this-change/regressions.log`.

## What is not claimed here

The baseline cannot express either case: there is no unconfirmed-rollback state and no
unterminated-tail state on it. `probe_new_cases.py` reports both as not applicable there rather
than as passes, and that output is not in this pack as evidence of anything.

No timestamp provenance, no independent attestation, no claim about any store other than this one
at these three hashes.
