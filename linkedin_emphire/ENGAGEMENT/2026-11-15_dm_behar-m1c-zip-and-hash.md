---
deliverable: dm
id: 2026-11-15_dm_behar-m1c-zip-and-hash
date: 2026-11-15
audience: direct
status: ready
approved: no
warm: yes
time_checked: >-
  checked: 2026-11-15 14:20 WAT, read from the system clock before this file was written.
profile_checked: >-
  Behar Dalipi, Skopje. He asked for the zip and its full SHA-256 at 13:44, and said he will rerun
  both cases and f21 against the pinned baseline and the updated patch.
premise: >-
  He wants the artefact and the hash, and he intends to run it in both directions. The message hands
  over the four hashes and warns him where the two directions differ, so a correct result on the
  baseline is not mistaken for a defect.
sources_read: >-
  read: the pack as committed, the zip rebuilt from it at 14:20 WAT, and the runs made earlier today
  on both revisions.
premise_checked: >-
  checked: the zip rebuilt from the committed folder lands on 21a5efbf… again, so the hash printed
  here is reproducible rather than a value copied from an earlier line. Both the "not applicable" and
  the "MISSED on baseline" results were run, not assumed.
---

# Zip and hash for Behar Dalipi, 15 November 2026, 14:20 WAT

What this is: the handover, with the hashes and one warning about what the baseline will say. What to
do next: send it with the zip attached. No link, as before.

## Why the warning is in the message

He said he will run both directions: pinned baseline, then updated patch. Two of those four runs will
look wrong to anyone who has not read the code.

The new cases cannot be arranged on the pinned baseline at all, because the states they test do not
exist on it. And the revised f21 fails on the baseline, deliberately, because the baseline claims an
unchanged disk while the record's bytes are still in the file.

Saying that before he runs them costs four lines. Not saying it costs a round of him reporting a
failure that is the point of the work.

## The count, before the block

**1340 characters, 186 words.** The hash lines are long and are meant to be copied, not read.

## Message, paste this

Attached, and here's the hash in full.

ZIP 21a5efbfa976d08fff2cbf80898c492e8916f2c277d54a1e5afc5b9a0acceaf0, 36,202 bytes, 23 files. It builds from the folder every time and lands on that hash, so you can rebuild it rather than trust the copy.

Inside, the two files and the diff, which are the three things worth checking:
bench/store.py ee42139cab14fdb02dd82ad88d6421afc4af7a808cf0f561cc15f2db3a0bde85
audit/regressions.py 68a87228fb13f46c1db0d65affd2320cf841c1c38ad7ad65fc65513d474f2db0
patch 5dfd7dc3da646d914367ac0c84e91ef822c0a41311427dd3128f33d9832cf53e
Those three are the ones to check.

Before you run it, so an expected result doesn't read as a mistake.

Neither new case can be arranged on the pinned baseline. It has no unconfirmed-rollback state and no unterminated-tail state, so the probe reports both as not applicable there rather than as passes. The before-and-after sits one revision later, in 02-previous-change: b987cc49, the file delivered at 09:47 on 15 November. Both cases fail there.

f21 behaves the same way. On the pinned baseline the revised check reports MISSED, because the baseline says the disk is unchanged while the record's bytes are still in the file. That's the counterexample it now catches, not a fault in the check.

The two commands and both hashes are in 00-README, so I won't repeat them here.

## What was checked before writing

The zip was rebuilt from the committed folder at 14:20 WAT and produced
`21a5efbfa976d08fff2cbf80898c492e8916f2c277d54a1e5afc5b9a0acceaf0` again: 23 files, 36,202 bytes.
The same build run twice gave the same bytes, which is what makes the hash worth printing.

The patch hash, the store hash and the audit hash were read from the files that are in the zip, not
from the pack's notes.

## Not done here

The zip is not in the repository. It is 36 KB of build output and it regenerates from the folder, so
it travels as an attachment and the repository keeps the inputs. No link, matching the earlier
delivery.
