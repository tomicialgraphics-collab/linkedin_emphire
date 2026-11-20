---
deliverable: dm
id: 2026-11-13_dm_sebastien-favre-first-pass-and-terms
date: 2026-11-13
audience: vendor
status: ready
approved: yes
warm: yes
profile_checked: >-
  Sébastien Favre invited an independent look at the public Evidence repository on 13 November at 18:10, with no
  predefined conclusions and no development obligation, and asked what can be verified independently, what does not work
  as expected and what could be improved. He is building this in public, he has already conceded the second-reader
  limitation, and he read version 5 of the case study. He responds to evidence rather than to assurances, so the reply
  carries results rather than an offer.
premise_checked: >-
  checked: on 13 November 2026 by cloning neomundi-io/neomundi-evidence-public and running it, on Python 3 without
  cryptography installed and then with it. sha256sum --check on conformance/SHA256SUMS passed for 172 files. The corpus
  ran 50 cases: 40 PASS and 10 AMBIGUOUS with cryptography present, and five failures without it. verify_attestation.py
  on conformance/fixtures/D-tampered/D-06-attestation-signature-invalid/attestation.jws returned exit 0 with no trust
  store, and returned exit 1 with the fixture's own store. verify.py on the tampered archive case returned exit 1.
  The Rust verifiers were not built and are not claimed.
sources_read: >-
  read: the repository README, conformance README and runner, the trust store layout, and the fixtures named above. The
  closed dossiers referenced in the README are private and were not available.
---

## Message, paste as is

<!-- gate:body:start -->
Hi Sébastien,

I did a first pass tonight rather than promising one. Here's what I could check from a clean machine, and the two things
I'd fix before a stranger runs it.

What holds: your corpus verifies. sha256sum --check passes on all 172 files in SHA256SUMS, and the Python verifier runs
the 50 cases offline, 40 PASS and 10 declared AMBIGUOUS, with no undeclared failure. Tampered archive cases fail with a
reason and exit 1. That's a stronger position than most repositories claiming independent verification ever reach.

Your attestation verifier exits 0 when the signature was never checked. Run it on the D-06 fixture with no trust store
and it prints the NOT TESTED lines, with six PASS above them, then returns 0. A CI job gating on the exit code can't
tell that file from a valid attestation. You and I both know NOT TESTED isn't success; the exit code doesn't say so.
Exit 2 under --strict is the right behaviour and shouldn't have to be discovered.

An optional dependency is invisible from the outside. On stock Python the corpus moves from 40 PASS to five failures
purely because cryptography is missing, and the attestation checks quietly turn into NOT TESTED. Better to refuse to run
the corpus without it than to degrade in silence.

What I couldn't test here: the Rust verifiers, for want of a toolchain, and the four open normative questions. I'm not
going to pretend otherwise.

A full pass would be paid work: one week, a written report per area with cases you can re-run, invoice on delivery,
$1,500. Method stays mine to describe; your implementation and your findings stay yours.

Timothy
<!-- gate:body:end -->

## What not to say

No praise of the repository in general, no summary of his own README back at him, and no claims about the Rust verifiers
or about the private Q-2 dossier, neither of which was available. No pricing options beyond the one figure, no retainer
and no equity ask. Nothing that implies the defects found are unusual, because most published verifiers fail in exactly
this direction.

## Why this is worth the slot

He asked for an independent look and invited the criticism, so the answer is three measured results from his own
fixtures rather than an offer to look. The defects named are in the failure path, which is where his own documents say
the value sits, and the price is stated so the next message is a decision rather than a negotiation.
