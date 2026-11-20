---
deliverable: internal
id: 2026-11-20_readme_attribution_block
date: 2026-11-20
audience: internal
status: ready
approved: yes
title: The reviewed line for the Host-Failure Benchmark README, and where it goes
time_checked: >-
  checked: 2026-11-20 13:29 WAT, read from the system clock before this file was written.
profile_checked: >-
  Behar Dalipi, the reviewer whose name goes on the line, who approved it at 13:21 with one clarification and who reads
  hashes precisely enough to know which kind dab7483e is. Nothing here is published without his approval already given.
premise_checked: >-
  checked: dab7483e is the SHA-256 prefix of the version 3 ZIP, confirmed in this repository at 13:29 WAT on 20 November
  from the pack record, not from the reviewer's message; full hash dab7483efc8022ee9d924da2d1410457bb8d27eaeee9d19817cf52bbf388c3ae,
  md5 7c216d2f, 23 files. Every other word of the line is the reviewer's own or was approved by him at 13:21.
sources_read: >-
  read: STATE/OPEN-LOOPS.md and the Behar exchange files in ENGAGEMENT. No page opened.
approval: >-
  Behar Dalipi approved the attribution at 13:21 WAT on 20 November, conditional on one technical clarification:
  dab7483e must be identified explicitly as the SHA-256 prefix of the version 3 ZIP. That clarification was made and he
  approved the exact wording at 13:39 WAT, unchanged. This is the approved text and the only place it goes.
---

# Where it goes

The public README of the Host-Failure Benchmark repository, one line under the opening paragraph, as agreed with the
reviewer on 20 November. Nowhere else. It does not go into the ERI work, because he has not seen that and it would be a
claim he never agreed to.

# What to paste

Version 3 of this benchmark, held at dab7483e (the SHA-256 prefix of the version 3 ZIP), was reviewed independently by
Behar Dalipi, a research collaborator who coordinated two rounds of AI-assisted technical review. Every finding he
raised is answered in the register, either by the patch that closes it or by the reason it stays open; the corrections
and the verdicts are mine. His contribution is verification and adversarial testing, and expressly not an endorsement of
the benchmark. The results cover the modes tested, and other filesystems and concurrent writers are unverified.

# The correction he caught

`dab7483e` is not a commit. It is the SHA-256 prefix of the version 3 ZIP, 23 files, full hash
`dab7483efc8022ee9d924da2d1410457bb8d27eaeee9d19817cf52bbf388c3ae`, md5 `7c216d2f1e118601665db36293bca3cf`. The
sentence as first drafted said "held at dab7483e" and nothing else, which invites a reader to assume it is a git
reference, and the owner's own covering message then treated it as one. The parenthetical exists because of that, and it
is the reviewer's correction, not the owner's.

# After publishing

1. Send him the live page.
2. Send him the commit that carries the line, named as a commit, so the two kinds of hash are never confused in the
   record again.
3. Record both in the exchange log, with the time of publication, so the approval and the publication are dated within
   the same day.

# How to publish it, in order

1. Open the edit page for the README: https://github.com/Teamthy/host-failure-benchmark/edit/main/README.md
2. Put the cursor at the end of the opening paragraph, the one that begins "A small local suite about one question", and press enter twice. The block goes between that paragraph and the line that begins "Repository:".
3. Paste the text above as a single paragraph. No heading, no bullet, no bold.
4. Commit message: `README: record the independent review of version 3 (approved by Behar Dalipi, 20 Nov 2026)`
5. Commit straight to `main`, which is the default branch and the only branch a reader will arrive on.
6. Open the commit page and copy the commit SHA from it. That is the second hash, and it is not the ZIP.
7. Send him the live page and that commit in the message drafted in the DM of the same date.

The repository page is https://github.com/Teamthy/host-failure-benchmark and the rendered file is at
https://github.com/Teamthy/host-failure-benchmark/blob/main/README.md , which is the page to send him once it is up.
