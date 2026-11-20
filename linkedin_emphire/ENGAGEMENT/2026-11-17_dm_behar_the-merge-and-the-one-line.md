---
deliverable: dm
id: 2026-11-17_dm_behar_the-merge-and-the-one-line
date: 2026-11-17
audience: outbound
status: ready
approved: no
recipient: Behar Dalipi
premise: >-
  He has completed an independent rerun of the M1f source snapshot, reported that both archive hashes and all three
  source-file hashes matched, that all twenty-two regression modes passed, that the verification pass held on the
  artifacts of his own fresh run, that the f24 and f25 checks reproduced including the failure at the open call, and
  that he is comfortable merging M1f for the documented scope. He found one remaining defect: line 54 of the correction
  note points at a folder that does not exist, since the folder is numbered 06 and not 05. This reply corrects it,
  carries the rebuilt pack, and asks what the merge is for.
time_checked: >-
  checked: 2026-11-17 00:47 WAT, read from the system clock before this file was written.
profile_checked: >-
  Behar Dalipi, whose messages are short, exact and free of ceremony, and who checks hashes before he says yes. He has
  now put in a full independent rerun on his own machine, so the reply treats his verification as the authority rather
  than thanking him around it.
premise_checked: >-
  checked: the two hashes quoted here were recomputed from the rebuilt archive on this machine and then re-read from the
  Drive upload, md5 7c216d2f and sha256 dab7483e, and the tree hash is the one he verified. Nothing is claimed about his
  pipeline, his employer or what the merge covers beyond the scope he named.
sources_read: >-
  read: his message of 23:17 and the correction note in the pack. No page opened. The only external facts are the
  hashes of artefacts built and uploaded tonight.
---

## Message, paste as is

<!-- gate:body:start -->
Behar, that is the gate cleared on your side, and I am recording it as yours rather than mine. Hash-matching someone else's artefact is the part that makes the rest of it mean anything.

Your fix is done. Line 54 of the correction note pointed at a folder numbered 05 when the folder is 06. The note is corrected and the checksum list regenerated, so the pack hash has moved.

Corrected pack: https://drive.google.com/file/d/1HBGxi3rkylL--mblWXvhKbz--1O12Mtw/view
sha256 dab7483efc8022ee9d924da2d1410457bb8d27eaeee9d19817cf52bbf388c3ae, md5 7c216d2f1e118601665db36293bca3cf, 23 files.

What changed is one path in the correction note and the one checksum line covering it. No code line, no log, no register entry. The source snapshot you reran is untouched at c8a56695 and stays the reference.

The f25 description change I offered is still unwritten, deliberately. It is one line and it belongs in the next revision, not in a pack you are about to merge.

One question so the register stays useful afterwards: what does it get used for there? If it is vendored into your pipeline, I will keep the defect register in the shape your runners expect. If the next step is running the suite against your own stack, that is a scoped piece with a fixed fee and a fixed deliverable, and I will write it as a short proposal when you want one.
<!-- gate:body:end -->

## Why the correction ships rather than gets acknowledged

He is about to merge. A pack that names a folder that does not exist is a small thing now and an annoying thing in six months, when somebody follows the note during an audit and finds nothing there. Rebuilding costs a hash and a minute.

## Why the tree is untouched

The snapshot he verified is the one thing in this exchange that should never move. Rebuilding it to look tidy would invalidate the rerun he just did, which is the only independent evidence either of us has.

## Why the question is about use

The register is worth more if it is maintained in the shape his runners consume. That is also the only honest way to find out whether this ends at a merge or continues into work on their own stack, and asking about use is a better question than asking about budget.

## Held back

No fee is named. A scope without a written deliverable is a number that gets negotiated down before anybody knows what it buys, and the last quote in this thread went below the floor for exactly that reason.
