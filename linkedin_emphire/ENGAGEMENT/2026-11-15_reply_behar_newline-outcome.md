---
deliverable: dm
id: 2026-11-15_reply_behar_newline-outcome
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 10:31 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: collaborator
status: ready
approved: no
warm: yes
profile_checked: >-
  Behar Dalipi accepted the three-state reply at 09:44 and asked one question: on restarts 1, 2 and 5 of the same
  journal, should the missing-newline test expect a persistent named gap or a recovered conflict with both sequence
  numbers. He asked so that the two of them check for the same outcome, which means the answer has to be specific enough
  to be run, not a preference.
premise_checked: >-
  checked: the previous message to him contained both outcomes in one breath, a named gap in one sentence and the same
  conflict reported across three restarts in the next, so the question is a fair catch of the owner's own wording. The
  reply picks one and says why. Nothing in it claims a rebuilt pack, a run or a result, because the pack has not been
  rebuilt and the two cases have not been run.
sources_read: >-
  read: his message of 09:44, the reply that went at 10:13, and the classification log's description of withheld
  batches, sequence numbers and the repair record, which is what the gap assertions are built on. No attachment opened.
---

# Reply to Behar: one outcome, and the six assertions that settle it

<!-- gate:body:start -->
Behar,

Persistent named gap, identical on all three restarts. My last message put two outcomes into one sentence and you caught it.

The reason it is the gap and not the recovered conflict: a record missing its terminator cannot establish that the write completed, only that some bytes arrived. Calling that a recovered conflict would be reporting evidence I do not have. The gap names the withheld sequence number and the reason, and the reply is byte-identical on restarts 1, 2 and 5.

What to assert, so we are checking the same thing. The gap names the withheld seq and reads unterminated. The reply on restarts 2 and 5 is byte-identical to restart 1. The store journal's hash is unchanged before and after each restart, so nothing recovered it by rewriting. The withheld record never enters the index.

The recovered-conflict outcome still exists, in the other case. Same journal with the terminator intact, and the conflict is reported with both sequence numbers on every restart, not only the first.

Two cases, two outcomes, and neither is allowed to change between restarts. That is the property, and it is the one the old behaviour failed.

I will send the zip and the hashes when the pack is rebuilt.

Olusanya.
<!-- gate:body:end -->

## Why the gap wins, and what it costs

**The gap is the honest reading of the evidence.** A record whose terminator is missing tells you that bytes arrived and nothing more. It does not establish whether the write completed, and a conflict reported from it would be a claim built on an assumption about how the file ends. Reporting that as recovered would be the same class of error as durable false on an unknown disk state, which is the mistake he caught an hour earlier.

**The cost is real and worth stating plainly.** A named gap says there is a record that cannot be read. It does not say the action was conflicted, so the buyer of the benchmark loses the conflict information that was in fact present in the bytes. That is a deliberate trade: an unreadable record is a gap, and a gap is not a pass.

**The four assertions are what make it runnable.** Naming the outcome without naming the checks is how two people run the same test and disagree about the result. The journal hash staying unchanged across restarts is the one that actually proves nothing recovered it by rewriting, and it is the assertion that would have caught the old behaviour.

**The second case is named so the pair cannot be confused.** A terminator that is present must produce a recovered conflict with both sequence numbers, every time. Without that sentence, a fix for the first case could quietly make the second one pass by never recovering anything.

**No question goes back.** He asked one thing, the reply answers it, and the pack rebuild is the next move. Asking him to confirm the reasoning would only put the decision back in his lap.
