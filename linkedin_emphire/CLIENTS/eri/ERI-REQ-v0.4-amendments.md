---
deliverable: internal
id: ERI-REQ-v0.4-amendments
date: 2026-11-20
audience: outbound
status: ready
approved: no
title: Proposed amendments to Ẹ̀rí Requirements v0.3, for v0.4
sources_read: >-
  read: ERI-REQ-v0_3.pdf, all eight pages, with its extracted text in this folder. Nothing else.
---

# How to read this

This is a patch, not a rewrite. Nothing in v0.3 is deleted. Six new requirements are added at 046 to 051, five existing
requirements get one sentence each, and the build-day cost of every change is stated so the total can be checked
rather than guessed at.

The reason for six new numbers rather than editing 012 and 038 in place: your numbering is the thing that makes
acceptance criteria comparable week to week, and a new number leaves a trace of what was added and why.

## The seven, and where each lands

| # | Gap | Fix | Cycle | Days |
| --- | --- | --- | --- | --- |
| 1 | Consent is the verifier's tick | amend REQ-012, add REQ-046 | 2 | +0.10 |
| 2 | No requirement captures consent to show a name | add REQ-047, point REQ-038 at it | 2 | +0.20 |
| 3 | Withdrawal has no state | add REQ-048 | 3 | +0.20 |
| 4 | Deletion contradicts anchoring | one sentence in REQ-028 and REQ-043 | 3 and 4 | +0.00 |
| 5 | Accuracy in metres with no caption | amend REQ-014 | 2 | +0.05 |
| 6 | Sealing has no failure path | add REQ-049, amend REQ-027 | 3 | +0.15 |
| 7 | No requirement has the agency declare anything | add REQ-050, show it at REQ-031 | 1 and 4 | +0.20 |
| 8 | Public check never fails in a test | add REQ-051, amend REQ-039 | 4 | +0.05 |
| 9 | No NIPOST key, so cycle one runs on samples | add REQ-052 | 1 | +0.10 |
| 10 | The fourth answer has no requirement | add REQ-053 | 4 | +0.10 |

Ten rows for seven gaps and three additions. Total added: **1.15 build days**. REQ-052 was added once Marvin confirmed there is no NIPOST key yet, and REQ-053 once he pointed out that the requirements document already answered the questions put to him, which was true of two of the three and not of the empty register. The document goes from 6.5 to **7.65 build days, roughly 61 hours** over four cycles.

---

## REQ-046, consent in her words (new, cycle 2)

> The consent prompt names what the speaker is allowing, in the language she is speaking: that the recording is kept,
> that it may be shown to buyers, and that it can be deleted on request. The speaker says these aloud before the
> testimony begins, and the item stores the prompt text, the language and the time of the consent.

Acceptance: the consent prompt in the Yoruba set is read aloud on a test recording, the stored item shows the prompt
text and the language and the consent time, and a recording saved without the consent passage cannot pass the
REQ-012 tick because the tick has nothing to confirm.

**Amends REQ-012** by adding, after "confirms consent": *"The tick confirms a consent passage that has been spoken,
not a statement typed by the verifier."*

## REQ-047, consent to be named (new, cycle 2)

> A verifier records, per person and per file, whether a private person agreed to be named on the certificate and the
> public page. The consent is dated, names what it covers, and can be withdrawn later, in which case the name is
> withheld from the next release of the page and the withdrawal is shown as an event.

Acceptance: a file with one speaker who agreed to be named and one who did not shows one name and one role on the
public page; withdrawing the first consent changes the page to show the role alone, with the withdrawal and its date
shown, and no previously published name is claimed to be un-published.

**Amends REQ-038** by adding: *"Consent to be named is recorded under REQ-047 and is not inferred from consent to be
recorded."*

That last clause is the whole point. Agreeing to be recorded is not agreeing to be published, and v0.3 quietly assumes
they are the same thing.

## REQ-048, withdrawn (new, cycle 3)

> An attestor can withdraw an attestation. The withdrawal is a new event that refers to the attestation, is never an
> edit or a deletion, and shows on the certificate with its date and the attestor's name or role.

Acceptance: withdrawing an attestation leaves the original attestation visible with a withdrawal beneath it; the
certificate shows both; a direct edit or delete request on the attestation returns HTTP 403.

## Deletion and the anchor, one sentence in both places (amends REQ-028 and REQ-043)

Wording, used identically in both requirements:

> Deletion removes the content and the page. The fingerprints and the anchor reference remain, so a person holding a
> copy of the file can still establish that it existed on the date it was anchored.

**REQ-043** then reads: the demo content, recordings and images are deleted within thirty days, and the fingerprints
and anchor reference for the four seeded items remain under the sentence above.

## REQ-014, the caption (amendment)

Add to the acceptance criterion: *"Under every photo the caption reads: the phone's position when the photo was taken,
accurate to about N metres, and not a boundary."*

## REQ-049, sealing fails (new, cycle 3)

> If the anchor call is refused, times out or returns an error, no items are marked as sealed, the screen says the
> seal did not complete, and the verifier can retry the same batch.

Acceptance: with the anchor service returning a 5xx, pressing Seal leaves every item unsealed, shows "The seal did not
complete. Nothing has been anchored. Try again.", and a retry after the service recovers produces exactly one anchor
reference for the batch.

**Amends REQ-027** by adding: *"An item is marked sealed only after the anchor reference is stored under REQ-028."*

## REQ-050, the agency statement (new, cycle 1, shown from cycle 4)

> When a verifier creates an evidence file, the agency it belongs to records a short statement in its own name, which
> is stored with the file and shown on the certificate under the agency's name. The statement is made once per agency
> and can be changed, with the change dated and the earlier statement kept.

Acceptance: creating a file as an agency with a recorded statement shows that statement on the certificate under the
agency's name; changing the statement does not change the text already shown on files created before the change.

Proposed default text, for the agency to adopt or replace:

> We registered this file on the date shown. We hold a copy of what we registered. We checked it against the document
> given to the buyer. This is a statement of what we did and what we hold, and it is not a warranty of title.

## REQ-051, the negative control (new, cycle 4)

> The seed set includes one item whose stored fingerprint does not match its content. The public check page is tested
> against that item on every release and must answer no match for it.

Acceptance: the seeded bad item appears on the certificate like any other, the public check page reports "No match in
this evidence file." when the file corresponding to the bad item's content is checked, and the test fails loudly if the
page ever reports a match.

**Amends REQ-039** by adding: *"one of the four seeded items is the negative control under REQ-051."*


## REQ-052, sample data is labelled (new, cycle 1)

> When the address shown for a postcode comes from a recorded NIPOST sample rather than a live call, the app says so
> wherever that address appears, and the sample's capture date is shown with it.

Acceptance: with the sample data source selected, the postcode result screen shows the address, the words "sample
response, captured on <date>", and no claim that NIPOST returned it today. Switching the data source to live removes the
label, and the same screen is otherwise identical.

**Why:** Marvin confirmed on 20 November that there is no NIPOST key yet and that live keys need company verification,
so cycle one will run on recorded responses. A reviewer who discovers afterwards that an address was a fixture stops
trusting the rest of the demo, and this product is being sold on the habit of not overstating what it knows.

**Also required with it:** the source is selected by one configuration value with two implementations, sample and live,
so the day a key arrives is a config change and not a rewrite.


## REQ-053, the fourth answer (new, cycle 4)

> A public checker whose file matches nothing in the register is told that no record exists under that fingerprint, in
> the same layout and the same tone as a match, with one line beneath it saying that this only means nobody has
> registered this paper yet.

Acceptance: with one seeded file in the register, checking a file that is not in it shows "No record under this
fingerprint.", styled exactly like a match, with no warning colour, no error icon and no suggestion that the paper is
bad. Checking the seeded file in the same session shows a match. The two results are the same page with one word
changed.

**Why:** REQ-035 tells a checker whether their file matches a sealed item inside one evidence file. Nothing in v0.3
describes what a person sees when their paper matches nothing anywhere, which is the answer most people will get in the
first year and the moment a buyer asks an agent to register. On day one the register is empty, so this is the first
screen of the demo rather than the last.

---

## Sequence, if this is accepted

Nothing here blocks Monday. Cycle one takes REQ-050 only, and it is 0.1 of a day on top of REQ-010. The rest can be
argued about for as long as you like while REQ-001 to REQ-009 are being built.

The two that would be expensive to leave late are REQ-046 and REQ-047, because both change the recording screen, and
the recording screen is cheaper to get right once than twice.
