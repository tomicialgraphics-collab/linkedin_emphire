---
deliverable: dm
id: 2026-11-20_dm_marvin-the-split-and-0003
date: 2026-11-20
audience: outbound
status: draft
approved: no
recipient: Marvin Percival
warm: yes
premise: >-
  Marvin answered at 19:01 on 20 November: PR 5 closed with no purge, PR 4 merged, PR 6 praised, and a design for the
  purge door that splits each event into a record that never goes and a content table that alone can be purged, to be
  written as decision 0003 before PR 6 merges. He asked whether the branch claude/adoring-babbage-jng35n is the owner's.
  This reply accepts the split, adds the two things it pulls in (the address, and the hash chain the standards ask for),
  and explains why the commit label is fixed forward rather than rewritten.
time_checked: >-
  checked: 2026-11-20 19:04 WAT, read from the system clock in the sandbox before this file was written.
profile_checked: >-
  Marvin Percival, architect and reviewer on Ẹ̀rí, who writes short and reads closely. His 19:01 message is about 400
  words and decides four things; the reply matches his length rather than exceeding it, and asks him for nothing tonight.
premise_checked: >-
  checked: DATA-RULES.md on main at 4888b86 lists real home addresses and postcodes as never to be kept, and says
  fingerprints and anchor references stay after the 30-day purge. Standards section 2.4 asks for hash-chained audit rows.
  CLAUDE.md forbids amending a pushed commit. The branch commit e434f72 is signed "Claude <noreply@anthropic.com>" at
  16:03 WAT, not "Claude (for Marvin Percival)" as his own agent signs. All read in DUNIN7/eri-test on 20 November.
sources_read: >-
  read: Marvin's 19:01 message and the files it refers to in DUNIN7/eri-test, 20 November.
---

## Before sending

The last line needs the owner's answer: is `claude/adoring-babbage-jng35n` his? It was made at 16:03 WAT by a plain
"Claude" identity, which is how a claude.ai session signs, after the owner connected GitHub to the shared Claude account
at 13:34. If it is his, keep the sentence as written. If not, replace it with "Not mine. Your agent signs as Claude for
Marvin Percival and this one doesn't, so it's worth a look."

## Message, paste as is

<!-- gate:body:start -->
Thanks Marvin. The split is better than my door, and I'll write it up as 0003 before PR 6 merges.

Two things it pulls in, and I'll put both in the same note. The address on evidence_files is a real home once the data is real, so it goes to the content side with the payload. And the standards ask for hash-chained audit rows, which we don't have yet. If the chain runs over the record half only, it survives every purge, which is the certificate's whole point.

On the CHORE label: the instructions file says never amend a pushed commit, so the REQ-020 and REQ-030 label goes on the next commit and the PR title. The package description and the version bump go in the same pass.

The adoring-babbage branch is mine, an early plan from before your repo layout. I'll close it and fold anything useful into v0.4.
<!-- gate:body:end -->
