---
deliverable: dm
id: 2026-11-15_dm_behar-m1c-two-cases-covered
date: 2026-11-15
audience: direct
status: ready
approved: no
warm: yes
time_checked: >-
  checked: 2026-11-15 13:37 WAT, read from the system clock before this file was written.
profile_checked: >-
  Behar Dalipi, Skopje. He is holding the merge on three conditions and named them on 15 November:
  duplicate sequence numbers after an unconfirmed rollback, a record lost by a repair, and f21
  collapsing three states into one. This message answers those three and nothing else.
premise: >-
  He holds the merge until the two reported cases are covered and f21 carries distinct
  expectations. Both are now covered, f21 is rewritten, and the evidence is in a pack whose hashes
  are printed here. The message exists so he can check it rather than take it on trust.
sources_read: >-
  read: his 15 November report of the two cases, the delivered pack of 15 November, and the code at
  both revisions. Every number in this message comes from a run made today, not from reading.
premise_checked: >-
  checked: the two cases reproduce on the revision he holds and hold on this one. The claim that
  the verifier output is unchanged was measured by diffing this run against the log in the pack he
  checked, which returns nothing.
---

# Reply to Behar Dalipi, 15 November 2026, 13:37 WAT

What this is: the answer to the three conditions he set, with the pack that carries the evidence.
What to do next: send this as one message, with the zip attached or handed over, no link.

## Why it is shaped this way

He set three conditions. A message that reports "fixed" without the mechanism gives him nothing to
check, and he has caught that twice today already. So each case is one paragraph: what the store
did, why it was wrong, what it does now. No adjectives and no apology.

The f21 paragraph is the one he will read hardest, because he called it himself. It says four states
rather than "improved", names what each state must be true of, and states the before and after as
measurements: fails on the revision he holds, passes 22 of 22 here.

The hashes are printed because he verifies what he is sent. They are the four he needs: the two
files, the patch, the zip.

## The count, before the block

**1,403 characters, 246 words.**

## Message, paste this

The two cases are covered, and you're right about f21.

Duplicate sequence numbers: the batch write left one whole record on disk and half of the next, the rollback was refused, and the reply said unknown, which was correct. Then the retry numbered itself from a counter that had never seen the record already on disk, so it wrote a store_seq that was already taken. Now the journal re-reads the file after an unknown, cuts out the bytes that never became a whole line, and takes its next number from the records that are actually there.

Lost record: the repair rewrote the file from the good lines alone, so the withheld tail sat in neither the journal nor the quarantine, and restart 2 saw a clean file. It now writes the tail back at the end and copies it into the quarantine, so the gap gets reported on every restart instead of surviving exactly one.

f21 names four states now instead of collapsing them into one boolean, and each has to be true of the file: refused only if the bytes are absent, unknown only with a disk_state and a reason, acknowledged only if memory and the next restart agree, raised never. On the revision you're holding it fails. On this one it passes, 22 of 22.

bench/store.py ee42139c, audit/regressions.py 68a87228, patch 5dfd7dc3, zip 21a5efbf, 23 files, built twice with the same hash. Verifier output is byte-identical to the pack you checked, so nothing else moved.

## What was checked before writing

The two cases fail on `b987cc49` and hold on `ee42139c`, both by running `probe_new_cases.py`
against each tree today; the logs are in the pack, one folder each, and the folder for the failing
revision was produced by running it rather than by writing it.

`f21` was run in both directions: `22 of 22` on this change, `MISSED` on the revision he holds,
under the same revised check. That second run is the one that makes the first mean something.

The verifier output was diffed against the copy in the pack he already checked. It is identical,
which is the evidence for "nothing else moved" and the reason the sentence is in the message.

## Not done here

No date, no promise, no question back. He asked for coverage and for the check to be able to tell
two things apart, and both exist now. The merge decision is his and the message does not ask for it.
