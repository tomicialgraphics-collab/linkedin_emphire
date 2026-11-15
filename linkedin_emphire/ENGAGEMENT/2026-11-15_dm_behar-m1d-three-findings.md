---
deliverable: dm
id: 2026-11-15_dm_behar-m1d-three-findings
date: 2026-11-15
audience: direct
status: ready
approved: no
warm: yes
time_checked: >-
  checked: 2026-11-15 22:25 WAT, read from the system clock before this file was written.
profile_checked: >-
  Behar Dalipi, Skopje. He tested the pack at 15:10 and found three things: a conflict pointing at
  the wrong verdict after a retry, a conflict naming a record replay withholds, and a write
  acknowledged after an EIO on the recovery read. He holds the merge until the regression exercises
  the retry, checks the conflict pointer after restart, and refuses writes when the recovery read
  fails.
premise: >-
  All three reproduced on the revision he holds, one of them introduced by the 09:47 fix on 15 November. The
  message names the cause of each, what changed, and the pack with the numbers, and it does not ask
  him for anything.
sources_read: >-
  read: his 15:10 message, the two revision trees, and the audit output on both. Every figure in the
  message comes from a run made on this machine on 15 November.
fix_verified: true
fix_evidence: >-
  CLIENTS/hfb/2026-11-15_m1d-pack/03-this-change/f23.log and regressions.log, both produced on
  2026-11-15 at 22:20 WAT on the patched tree; the same check on the delivered revision is in
  02-previous-change/f23.log.
premise_checked: >-
  checked: the conflict numbers on the revision he holds are 2 and 3 with the verdict at 4, which is
  what he described, and 2 and 4 here. The failed-read case answered as an acknowledgement there and
  as unknown here. Both were produced by running f23 against each tree, not by reading the code.
---

# Reply to Behar Dalipi, 15 November 2026, 22:25 WAT

What this is: the three findings, each with its cause, and the pack that shows them closed. What to
do next: paste with the Drive link. He asked for a link last time because the attachment did not
arrive, so the link is in the message body.

## Why it opens with the admission

One of the three was introduced by the fix he reviewed at 09:47 on 15 November. Saying so in the first line
costs nothing and buys the rest of the message the right to be believed. A reply that presented
three pre-existing defects would be a small lie that he would catch, because the recovery-read path
did not exist in the 09:47 revision.

## What each paragraph does

The conflict paragraph gives the mechanism in one sentence and the exact numbers, because those
numbers are his: 3 while the verdict was at 4.

The read paragraph is the shortest and the plainest, because it is my error and the description
should not be decorated.

The regression paragraph says what f23 does rather than that it exists, and states both directions:
MISSED on the revision he holds, passing here.

## The count, before the block

**1,433 characters, 237 words.**

## Message, paste this

All three reproduced, and all three are fixed. You're right to hold it.

The conflict pointer: the record was built from memory, and after an unknown the memory disagrees with the file. It took 3 as its second number while the verdict it was raised against was written at 4. The store reloads its index from the journal before it composes anything now, not only before it writes, so the numbers in a conflict come from what's on disk.

Recovery read: my resync caught its own read failure and carried on, so the next write was acknowledged and reused a number having just failed to read the file. That one's mine, from the 09:47 pack. A failed recovery read raises unknown now and refuses the write.

Regression: f23 does both. Issue, verdict, a differing verdict whose pair is cut with the rollback refused, then the same verdict retried, and the conflict has to name two records replay keeps, the first being the stored verdict and the second being the one it was raised against. Second case, same rollback then an EIO on the read: the write gets refused, and succeeds once the read works. On the revision you hold it reports MISSED with the numbers you saw. Here it passes, 23 modes, and the suite still says every check holds.

bench/store.py 837ca42d, audit/regressions.py f4204cc, patch ebaaea3d, zip 4049c7b8, 14 files.
Folder: https://drive.google.com/drive/folders/1eLAwk_d6q9ZizDgEpCsdqAJWoJhzqq0Q
That link stays the same.

## What was checked before writing

f23 was run against both trees on 15 November at 22:20 WAT. On `ee42139c`: `conflict 5 pointing at 2 and 3, verdict 4`,
and the write after the failed read answered as an acknowledgement. On this change: `pointing at 2
and 4`, and the write answered unknown, then succeeded once the read worked. Those two lines are in
the pack, one folder each.

The full audit was run on this change: twenty-three modes, all caught. `verify.py` was run: every
check holds. The patch was applied to a clean copy of the pinned baseline and produced the two
hashes printed in the message byte for byte.

## Not done here

No request, no date, no argument for the merge. He sets that condition and it is his to release.
