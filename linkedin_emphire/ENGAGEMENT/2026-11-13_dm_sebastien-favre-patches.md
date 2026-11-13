---
deliverable: dm
id: 2026-11-13_dm_sebastien-favre-patches
date: 2026-11-13
audience: vendor
status: ready
approved: yes
warm: yes
profile_checked: >-
  Sébastien Favre asked for the reproduction steps and the two patch suggestions on 13 November at 19:18, in the same
  message that accepted the Individual Methodological Reviewer designation and one round each. He is running his own
  review in parallel and will compare rather than defend.
premise_checked: >-
  checked: on 13 November 2026 by writing both patches against a fresh clone and running them. D-06 without a trust store
  moved from exit 0 to exit 2; with its own store and archive it stayed at 1; --strict stayed at 2; --allow-untested
  restored 0. Without cryptography the plain call moved from 0 to 4, and --allow-no-crypto to 2. The corpus with
  cryptography stayed at PASS=40, AMBIGUOUS=10, FAIL=0, and without it moved from PASS=35/FAIL=5 to PASS=33,
  AMBIGUOUS=8, ERROR=9. tests/test_attestation.py was 24/24 before the patch and 24/24 after updating cases 4 and 15,
  which assert the old exit code. Full diff: ENGAGEMENT/patches/2026-11-13_neomundi-fail-closed.diff, 3 files, 95
  insertions, 202 lines, sha256 196aa283cf46125d.
sources_read: >-
  read: verify_attestation.py (Bilan, code_de_sortie, arguments_de_verification, main), conformance/runners/run.py's
  verdict_observe, tests/test_attestation.py cases 4, 15 and 26, docs/EVIDENCE_TECHNICAL_DEMO.md cases A3 and E2.
---

## DM, paste this

<!-- gate:body:start -->
Two patches, and one thing to argue about before them.

Your suite asserts the current behaviour, so this isn't an oversight on your side: cases 4 and 15 in
tests/test_attestation.py both require exit 0 when a pillar is NOT TESTED. That's the contract I'm proposing to change,
in two assertions, and it's the honest way to put it.

Patch one, the exit code fails closed on the verdict:

  def piliers_non_demontres(self):
      return [i for e, i, _ in self.lignes if i in PILIERS and e != PASS]

  def code_de_sortie(self, strict=False, allow_untested=False):
      if self.compte(FAIL):
          return 1
      if self.piliers_non_demontres() and not allow_untested:
          return 2
      if strict and self.requises_non_demontrees():
          return 2
      return 0

Plus --allow-untested, which restores today's 0 for callers that only read 0 and 1. Pillars and not every NOT TESTED
line is deliberate: your store-digest line is hardening, it makes the store harder to swap, and it doesn't decide
whether the verdict holds. Fail on it and every normal run goes red until people stop reading the code, and a check
that's always red is a check people switch off. Only the five pillars are contingent, so those block.

Measured: D-06 with no store 0 to 2; with its own store and archive 1 to 1; --strict 2 to 2; --allow-untested 0; corpus
40 PASS, 10 AMBIGUOUS, 0 FAIL, unchanged.

Patch two, refuse rather than degrade:

  if not CRYPTO and not arguments.allow_no_crypto:
      print("REFUS : `cryptography` est absent de cet environnement ...", file=sys.stderr)
      return 4

Measured: no cryptography, plain call 0 to 4; --allow-no-crypto 0 to 2.

That needed one line outside the verifier. The conformance runner derives the verdict as "REJETE if code == 1 else ACCEPTE", so a 4
would have been logged as ACCEPTE. It now maps 1 to REJETE, 0 to ACCEPTE, and anything else to NON VERIFIE. Without cryptography the
corpus then reads PASS=33, AMBIGUOUS=8, ERROR=9 instead of PASS=35, FAIL=5. ERROR is your existing state
for a technical condition that prevents a conclusion, which is what a refusal is, and it's the better of the two
readings. It still can't distinguish a refusal from a crash, and I didn't invent a fourth state for you.

Your suite is 24/24 with the patch, after I rewrote cases 4 and 15 to expect 2 and 4. 95 lines across three files. Say the word and I'll paste it whole, or send it wherever you want it.

Timothy
<!-- gate:body:end -->

## What not to say

No "this is just a suggestion" hedging, no asking him to merge anything, and no claim that the patches are complete: the
Rust path is untouched and unbuilt here. No praise of the design.

## Why the two assertions come first

Because they are the finding. A verifier that returns 0 when it never verified, with a test that requires it to, is a
decision rather than a slip, and naming it as a decision is what makes this a review instead of a bug report. It also
gives him an honest reason to disagree, which is the point of one round each.
