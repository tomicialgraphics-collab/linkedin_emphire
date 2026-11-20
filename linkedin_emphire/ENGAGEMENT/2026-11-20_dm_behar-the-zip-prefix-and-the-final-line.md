---
deliverable: dm
id: 2026-11-20_dm_behar-the-zip-prefix-and-the-final-line
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Behar Dalipi
premise: >-
  Behar approved the attribution at 13:21 WAT on one condition, that dab7483e be identified as the SHA-256 prefix of the
  version 3 ZIP rather than left to be read as a commit. This message accepts the correction in plain terms, shows the
  final line with the parenthetical inserted and nothing else touched, confirms the place, and commits to sending the
  live page and the publishing commit.
time_checked: >-
  checked: 2026-11-20 13:29 WAT, read from the system clock before this file was written. His approval is stamped 1:21 PM
  in the thread as pasted.
profile_checked: >-
  Behar Dalipi, who read a hash and knew which kind it was, and who asked for the one clarification that stops a reader
  assuming a git reference. The reply concedes the error fully, because a half-concession here would be worse than the
  error it is about.
premise_checked: >-
  checked: dab7483e was confirmed in this repository before the reply was written, not taken from his message. It is the
  SHA-256 prefix of the version 3 ZIP, 23 files, full hash dab7483efc8022ee9d924da2d1410457bb8d27eaeee9d19817cf52bbf388c3ae,
  recorded when the pack was rebuilt as v3 after the correction note pointed at the wrong folder. The md5 is 7c216d2f.
  Only the parenthetical is new in the approved sentence; every other word is his or was approved by him.
sources_read: >-
  read: STATE/OPEN-LOOPS.md and the Behar exchange files in ENGAGEMENT for the hash provenance, and the thread as pasted.
  No page opened.
---

## Message, paste as is

<!-- gate:body:start -->
You are right and I had it wrong. dab7483e is the SHA-256 prefix of the version 3 ZIP, and my last message treated it as if it were a commit. That is the ambiguity you were guarding against, so thank you for catching it.

The line, final, with only that clarification added:

"Version 3 of this benchmark, held at dab7483e (the SHA-256 prefix of the version 3 ZIP), was reviewed independently by Behar Dalipi, a research collaborator who coordinated two rounds of AI-assisted technical review. Every finding he raised is answered in the register, either by the patch that closes it or by the reason it stays open; the corrections and the verdicts are mine. His contribution is verification and adversarial testing, and expressly not an endorsement of the benchmark. The results cover the modes tested, and other filesystems and concurrent writers are unverified."

Nothing else in it has changed from what you approved.

It goes under the opening paragraph of the repository README today. I will send you the live page, and the commit that carries it, named as a commit so the two kinds of hash cannot be confused again.
<!-- gate:body:end -->
