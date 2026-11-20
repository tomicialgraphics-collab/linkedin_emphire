---
deliverable: dm
id: 2026-11-13_dm_sebastien-favre-repro-steps
date: 2026-11-13
audience: vendor
status: ready
approved: yes
warm: yes
profile_checked: >-
  Sébastien Favre agreed on 13 November at 19:18 to the reviewer framing and the one-round sequence, and asked for the
  reproduction steps and the two patch suggestions. He says he has started his own technical review of the two issues
  and will compare. He answers evidence with evidence, and he has already conceded the honest limits of his own tool, so
  the message carries commands and exit codes rather than an argument.
premise_checked: >-
  checked: on 13 November 2026 by cloning neomundi-io/neomundi-evidence-public again and re-running every command quoted
  here. Corpus with cryptography: PASS=40, AMBIGUOUS=10, FAIL=0. D-06 with no trust store: 5 PASS, 0 FAIL, 6 NOT TESTED,
  exit 0. Corpus without cryptography, in a fresh venv: PASS=35, FAIL=5, with D-06, D-07 and D-08 reporting "verdict
  attendu REJETE, observe ACCEPTE". The first-pass message said six PASS sat above the NOT TESTED lines; the count is
  five, and this message corrects it rather than letting it stand.
sources_read: >-
  read: conformance/runners/run.py (how a verdict is derived from the exit code), verify_attestation.py's Bilan and
  argparse, tests/test_attestation.py cases 4, 15 and 26, docs/EVIDENCE_TECHNICAL_DEMO.md cases A3 and E2. Not read in
  full: the Rust verifiers, the four open normative questions, and the private dossiers.
---

## DM, paste this

<!-- gate:body:start -->
Sébastien,

Reproduction steps, from a fresh clone. One correction before them: my first message said six PASS sat above the
NOT TESTED lines. It's five. The rest of that paragraph stands as written.

Baseline first, so we know we're on the same build:

  cd conformance && python3 runners/run.py --verifier python

That gives PASS=40, AMBIGUOUS=10, FAIL=0 on this machine.

Defect one, the exit code:

  python3 verify_attestation.py conformance/fixtures/D-tampered/D-06-attestation-signature-invalid/attestation.jws; echo $?

It prints "[NOT TESTED] signature cryptographique - aucun magasin de confiance fourni", then BILAN 5 PASS, 0 FAIL, 6 NOT
TESTED, then echoes 0. Add --strict and it's 2, with the three unmet guarantees named. So the right answer is one flag
away, and the plain call, which is the shape of a CI step, still can't tell this file from a sound one.

Defect two, the dependency:

  python3 -m venv /tmp/nc
  /tmp/nc/bin/python verify_attestation.py conformance/fixtures/D-tampered/D-06-attestation-signature-invalid/attestation.jws; echo $?

Same 0 at the end, signature NOT TESTED, no level reached. Then the corpus under that interpreter:

  /tmp/nc/bin/python conformance/runners/run.py --verifier python

PASS=35, FAIL=5. Three of the five are D-06, D-07 and D-08, each logging "verdict attendu REJETE, observe ACCEPTE". A
tampered attestation reads as accepted because a package was never installed, and nothing in the exit code says so.

Patches next.

Timothy
<!-- gate:body:end -->

## What not to say

No apology beyond the one-line correction, no restatement of his README, and no claim about the Rust verifiers or the
four open questions. The correction is stated once and then dropped: repeating it turns a fact into a performance.

## Why the correction is in here

The first message said six PASS. The count is five, and he is about to re-run the command and count them. Correcting it
before he does is worth more than the sentence, and it is the same rule the case study runs on: the number is checked,
and when it was wrong, it is said.
