---
deliverable: internal
id: 2026-11-20_review_eri-requirements-v0-3
date: 2026-11-20
audience: internal
status: ready
title: Review of Ẹ̀rí prototype requirements v0.3, with the six gaps and the week-one test
sources_read: >-
  read: ERI-REQ-v0_3.pdf, eight pages, supplied by Marvin on 19 November. Text extracted page by page and every
  requirement read. No page opened.
---

# v0.3, read in full

45 requirements across four cycles. The document is better than most client specs: every requirement has an
acceptance criterion a stranger could run, nearly every criterion names the exact screen text, and the exclusions
list is specific enough to refuse work against.

## The arithmetic, checked

| Cycle | Requirements | Build days |
| --- | --- | --- |
| 1, foundation and postcode | REQ-001 to 010, ten | 1.6 |
| 2, capture | REQ-011 to 020, ten | 1.5 |
| 3, attestation and anchoring | REQ-021 to 030, ten | 1.3 |
| 4, certificate and public check | REQ-031 to 045, fifteen | 2.1 |
| Total | 45 | 6.5 |

6.5 build days is about 52 hours. Fifteen hours a week over four weeks is 60. The plan fits with eight hours left
for reviews, demo recording and the things that always take an hour. So the schedule is honest, and the answer to
"how much time" is fifteen, not twenty.

Cycle one holds ten requirements, not the eleven asked for on the call. Take the ten.

## The one that carries the rest

REQ-035, with REQ-034 and REQ-036 under it. A stranger with the file and no account is told whether it matches a
sealed item, and the anchor opens on a public explorer. If that fails, the certificate is a private diary with a
QR code, and nothing above it matters.

But the first thing to test is not that. It is REQ-028: does FORAY return a transaction id and a block time that
can be opened on a public explorer, for a batch of fingerprints, today. If it does not, cycles three and four both
fail, and the schedule would discover it in week three. Test it on Monday morning, before writing the first line of
REQ-001.

## Six gaps, in the order they bite

**1. Consent is the verifier's tick, not the speaker's words.** REQ-012 disables save until the verifier ticks
"Speaker gave consent". That records an assertion by the person holding the phone, and it does not say what was
consented to. Recording is not publishing. Proposed addition to REQ-012: the consent prompt names the three
permissions in the speaker's language, the speaker says them aloud, and the exact prompt text, language and
timestamp are stored with the item.

**2. Name consent has no capture step.** REQ-038 says a private person's name shows only when consent to show it is
recorded, and no requirement captures that consent. Without one, REQ-038 cannot be satisfied honestly. Proposed new
requirement: a per-person, per-file consent record, captured by voice or by tick in the person's presence, dated,
and revocable.

**3. Withdrawal has no state.** REQ-026 covers dispute, not recantation. Proposed addition: an attestor may withdraw,
recorded as a new event referring to the attestation, never an edit, shown on the certificate with its date.

**4. Deletion and the anchor contradict each other on paper.** REQ-043 deletes demo data within 30 days. REQ-028
puts fingerprints on a public chain, where they cannot be deleted. The document does not say which survives.
Proposed wording for the certificate and the consent prompt: deletion removes the content and the page; the
fingerprints and their anchor remain, and anyone holding the file can still prove it existed on that date.

**5. A photo carries accuracy in metres with no meaning attached.** REQ-014 is right to store it; nothing says what
it is not. Proposed caption under every photo: the phone's position when the photo was taken, accurate to roughly
N metres, and not a boundary.

**6. Sealing has no failure path.** NIPOST has REQ-009 for unreachable and REQ-008 for refused. FORAY has neither.
Proposed addition: if the anchor call fails, the batch stays unsealed, nothing is shown as anchored, and the screen
says so.

## The addition worth arguing for

A negative control. Seed one item whose stored fingerprint does not match its content, and require REQ-035 to say
"No match" for it, on every release. Without that, the public check is a test that has never failed, which is the
exact failure this workspace spent November documenting. One requirement, half a day, and it is the difference
between a check and a claim.

## Two assumptions that can block week one

NIPOST test keys do not resolve live postcodes (stated in the document), and Stele must mount into the prototype's
server (also an assumption, not a fact). Either one failing stops cycle one at REQ-006 or REQ-004. Ask which is
ready before Monday, and if neither is, agree a fixture path in writing rather than discovering it on Wednesday.

## What not to argue about

The tech stack is sensible, the exclusions are disciplined, and the acceptance criteria are better than the ones
in most paid projects in this workspace. Say so, briefly, and spend the reply on the six gaps.
