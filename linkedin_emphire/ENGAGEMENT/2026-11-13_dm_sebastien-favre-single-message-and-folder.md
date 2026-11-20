---
deliverable: dm
id: 2026-11-13_dm_sebastien-favre-single-message-and-folder
date: 2026-11-13
audience: vendor
status: ready
approved: yes
warm: yes
profile_checked: >-
  Sébastien Favre asked on 13 November at 19:18 for the reproduction steps and the two patch suggestions, after agreeing
  to the Individual Methodological Reviewer designation and to one round each. He is running his own technical review in
  parallel and will compare rather than defend. This message merges the two drafts of the same evening and points at a
  folder rather than pasting diffs into a chat window, because indentation does not survive LinkedIn.
premise_checked: >-
  checked: on 13 November 2026 against a fresh clone of neomundi-io/neomundi-evidence-public at commit
  439d15499a57746904abd561e0f2edc35f925daf, corpus 1.2.0, Python 3.11.2. Corpus with cryptography: 40 PASS, 10
  AMBIGUOUS, 0 FAIL. Without it: 35 PASS, 10 AMBIGUOUS, 5 FAIL, with D-06, D-07 and D-08 reading "REJETE attendu,
  ACCEPTE observe". D-06 with no trust store: 5 PASS, 0 FAIL, 6 NOT TESTED, exit 0; with --strict, exit 2. Both patches
  were applied and run. Drive folder holds exactly three files, all link-shared, none discoverable: 01 reproduction
  steps, 02 patches and measurements, 03 the diff. The message itself is not in the folder.
sources_read: >-
  read: verify_attestation.py (Bilan, code_de_sortie, arguments_de_verification, main), conformance/runners/run.py
  verdict_observe, tests/test_attestation.py cases 4, 15 and 26, docs/EVIDENCE_TECHNICAL_DEMO.md cases A3 and E2.
---

## DM, paste this

<!-- gate:body:start -->
Sébastien,

One message, and the detail lives at https://drive.google.com/drive/folders/1QFj62Z8IQ2dD-bslXZzrCZz1grZjR_dD instead of
in a chat window, where indentation dies and a patch stops being a patch.

Three files. Reproduction steps, with every command and its output. Two patches, each with what I measured before and
after it. The diff itself, ready to apply.

Before any of that, a correction. My first message said six PASS sat above the NOT TESTED lines. It's five. The rest of
that paragraph stands.

Short version, so the folder isn't a surprise. Without a trust store the attestation verifier prints NOT TESTED for
signature and for trust, reaches no level, and exits 0. Without `cryptography` it does the same, and the corpus logs
D-06, D-07 and D-08 as "REJETE attendu, ACCEPTE observe". A tampered attestation reads as accepted because a package
wasn't installed.

What I expect you to push back on is your own suite: cases 4 and 15 both require exit 0 when a pillar is NOT TESTED.
That makes the current behaviour a decision rather than a slip, which is why I've written the patch as a contract change
and left every verdict line untouched. Both patches move only what an automated caller can conclude.

One round each, as agreed. Your reply closes it either way, and the write-up follows.

Timothy
<!-- gate:body:end -->

## What not to say

No apology beyond the one-line correction, no restatement of what is in the folder, and no invitation to merge anything.
The folder is the argument; the message only says where it is and what to expect inside it.

## Why one message and a folder

Three reasons, and only the first is about length. A diff pasted into LinkedIn loses its indentation, which makes a
patch unreadable and unreviewable. Two messages also split one review into two things to answer, and the sequence agreed
with him is one round each. The folder then keeps the files together with their measurements, so a reader who comes back
in a week sees the patch and the numbers that justify it in the same place, rather than a scrollback.

## Supersedes

`2026-11-13_dm_sebastien-favre-repro-steps.md` and `2026-11-13_dm_sebastien-favre-patches.md` are kept as written but
must not be sent. This message replaces both.
