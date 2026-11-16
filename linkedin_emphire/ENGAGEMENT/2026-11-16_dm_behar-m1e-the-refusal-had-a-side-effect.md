---
deliverable: dm
id: 2026-11-16_dm_behar-m1e-the-refusal-had-a-side-effect
date: 2026-11-16
audience: direct
status: ready
approved: no
warm: yes
time_checked: >-
  checked: 2026-11-16 20:27 WAT, read from the system clock before this file was written.
profile_checked: >-
  Behar Dalipi confirmed all three M1d fixes independently at 09:18 on 16 November, then found one
  combination that still breaks gap preservation: a batch interrupted immediately before its final
  newline, a forced rollback failure, a retry that reported disk_state unchanged while moving the
  final record into quarantine, and a restart after which the gap was gone and writes were accepted.
  He holds the merge until the retry leaves the journal intact and the gap stays visible.
premise: >-
  The combination reproduced byte for byte on the tree he holds, and the cause is one step earlier
  than the symptom: the append refused the write, but resync cut the withheld tail before the refusal
  could run. The fix shares the gap test between start-up and resync, and the refusal now leaves the
  file untouched.
sources_read: >-
  read: his 09:18 message, the M1d tree built from the patch he holds, and the run of the new mode on
  both trees. Every number in the message comes from a run made on this machine on 16 November.
fix_verified: true
fix_evidence: >-
  CLIENTS/hfb/2026-11-16_m1e-pack/03-this-change/f24.log and regressions.log, produced on 2026-11-16
  on the patched tree; the same mode against the revision he holds is
  02-previous-change/f24.log, which reports MISSED with the numbers quoted.
premise_checked: >-
  checked: the before figures are from the mode run against M1d, the tree his merge hold refers to,
  not against an earlier revision. The two trees are identified by file hash in each revision file,
  so the comparison cannot be read as a comparison against something he never had.
---

## DM, paste this

<!-- gate:body:start -->
That combination reproduces, and you're right to hold it. The refused retry cut the record it was refusing to append onto.

The guard was already there and it said the right thing. But resync runs first, and its job was two things: re-derive the sequence from the file, and cut the bytes after the last newline into quarantine. A torn line deserves that cut. A whole record missing only its terminator doesn't, and it was cut anyway, before the refusal could speak.

So the reply said disk_state unchanged on a file that had just changed. On the tree you hold, the journal went from 875 bytes to 551, the withheld conflict moved into quarantine, the gap was gone after the restart, and the next write was accepted.

What changed: the test that tells a gap from damage is now one function, shared by start-up and by resync, so a repair can't apply a looser test than the one that reports. Resync applies it to the tail it's holding, before anything is copied or cut. A whole record sets the gap and raises the same refusal. A torn line takes the old path, because a torn line is damage.

f24 covers it, and the crash is arranged in the case rather than in the store: a file wrapper writes every byte except the last, then raises, and the failpoint refuses the rollback. On your revision f24 reports MISSED with the numbers above. Here the journal stays at 875 bytes, no quarantine file is written, the gap is still named after the restart, and the write is still refused.

f23 still catches its two. The full audit ends with every counterexample caught and none missed, and verify says every check holds.

bench/store.py 9070f970, audit/regressions.py 1c246c61, patch 29302aa0, zip 7a735457, 15 files.
Folder: https://drive.google.com/drive/folders/1c_SgLYnvkr_IRYFgDn4PEJl7__tOq5xe
That folder is the one to use from here.

The rule I've written into the code now: a refusal may not have a side effect. If the reply says the file is unchanged, nothing on the way to that reply may have written to it.

<!-- gate:body:end -->

## Why it opens by agreeing with the hold

He did the work twice: confirmed three fixes independently, then found the combination that survives all of them. The message says so in one clause and moves on, because a paragraph of thanks in front of a defect report reads as stalling.

The concession is specific and it is his: the guard existed, said the right thing, and lost to code that ran earlier. That is a more uncomfortable finding than a missing guard, and naming it plainly is what makes the rest credible.

## What the numbers do

The before and after are the same mode on two trees, identified by file hash, so he can check the comparison rather than take it. 875 to 551 is the cut. 875 to 875 is the refusal that does nothing.

The three assertions in f24 are stated as outcomes rather than as intentions: journal intact, no quarantine file, gap still named, write still refused.

## What is not offered

No apology, no promise, no date. He holds the merge until his own condition is met, and the message hands him the artifact that lets him decide that.

The new line about refusals is the one part that is not about this defect. It is the general rule the case produced, and it is there because he will hold the next one to it.

## If he finds a fifth

Same shape: reproduce it on the tree he holds first, then fix, then a mode that reports MISSED before and caught after. Do not describe a fix that was not run on both trees.
