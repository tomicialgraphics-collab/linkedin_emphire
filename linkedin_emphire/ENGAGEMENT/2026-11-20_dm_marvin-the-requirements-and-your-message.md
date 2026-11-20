---
deliverable: dm
id: 2026-11-20_dm_marvin-the-requirements-and-your-message
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Marvin Percival
premise: >-
  Marvin sent the Ẹ̀rí requirements at v0.3 as a PDF, then sent his own long message covering the product and the
  business. This reply answers both in one message: the arithmetic on the four cycles, the one requirement that carries
  the rest, the test that comes before any code, six gaps with the wording that would close them, one negative
  control, then his four questions answered in a line each, and the two assumptions that decide whether Monday is real.
time_checked: >-
  checked: 2026-11-20 01:49 WAT, read from the system clock before this file was written. That is 20:49 on Thursday in
  New York.
profile_checked: >-
  Marvin Percival, who numbers everything and expects numbered answers, who writes acceptance criteria a stranger can
  run, and who asked to be told where he is wrong. The reply is in his order, gives the document two sentences of
  credit rather than ten, and puts every objection next to the wording that would fix it.
premise_checked: >-
  checked: every requirement number here was read from the eight-page document itself, and the build-day totals were
  added from its own table, 1.6 and 1.5 and 1.3 and 2.1 making 6.5. The schedule claim rests on fifteen hours a week,
  sixty over four weeks, against roughly fifty-two of build. The two weekend windows were converted from his time zone
  to the owner's before being offered. No legal claim, fee, split or ownership term appears.
sources_read: >-
  read: ERI-REQ-v0_3.pdf, all eight pages, stored with its extracted text. His message of 12:06 and the notes of 12:31,
  pasted by the owner.
---

## Message, paste as is

<!-- gate:body:start -->
The PDF opened cleanly, eight pages, so I worked from the file rather than the paste. Read it twice, then read your other message again before writing this, because the two answer each other in places.

The arithmetic first. 1.6, 1.5, 1.3 and 2.1 is 6.5 build days, about 52 hours. Fifteen hours a week over four weeks is 60, so the plan fits with a day spare for reviews and the demo. Cycle one is ten requirements, not the eleven I asked for in my last message. The document says ten, so ten it is.

The one that carries the rest is REQ-035 with 034 and 036 underneath. A stranger with the file and no account is told whether it matches a sealed item, and the anchor opens publicly. If that part fails, the certificate is a private diary with a QR code on it.

But the first thing I'd test isn't that. REQ-028, Monday morning, before the first line of REQ-001. Does FORAY return a transaction id and a block time that opens on a public explorer, for a batch of fingerprints, today? If it doesn't, cycles three and four both fail and we find out in week three.

Six gaps, in the order they bite.

One. Consent is your tick, not her words. REQ-012 keeps save disabled until the verifier ticks a box, which records what the person holding the phone says, not what she agreed to. Recording is not publishing. The prompt should name the three permissions in her own language, she says them aloud, and we keep the prompt text, the language and the time with the item.

Two. REQ-038 needs consent before a private person's name is shown, and nothing in the document captures that consent. As written it can't be met honestly. It needs a step of its own, per person, per file, dated, revocable.

Three. Withdrawal has no state. REQ-026 handles a dispute and there is nothing for an attestor who takes his back. It should be a new event, never an edit, and it should show on the certificate with its date.

Four. Deletion and the anchor contradict each other. REQ-043 deletes the demo in thirty days and REQ-028 puts fingerprints somewhere they can't be deleted. One sentence, used in both places: deletion removes the content and the page, the fingerprints and their anchor stay, and anyone holding the file can still prove it existed on that date.

Five. REQ-014 stores accuracy in metres and nothing says what it isn't. One line under every photo: the phone's position when it was taken, accurate to about N metres, and not a boundary.

Six. Sealing has no failure path. NIPOST has 008 and 009 for refused and unreachable, and FORAY has neither. If the anchor call fails, nothing is anchored, and the screen has to say so.

One addition I'd argue for. Seed a single item whose stored fingerprint doesn't match its content, and require REQ-035 to answer no match for it on every release. Otherwise the public check is a test that has never failed, which is the problem we started this conversation about.

I'll build the document as written and send these six as proposed edits, so the criteria and the code don't drift apart while we argue about wording.

Now your message. On the parts I already answered I won't repeat myself, so the short version of the three that changed my thinking: keying to the parcel is right, and it's the only version of this that survives a forgery. Voice evidence is the strongest idea in the document and the most fragile thing in it, because one phone dying takes the family's account with it. And coordinates are a walk of a boundary, on a date, by a named person with a named phone, never a boundary.

Your four questions. What worries me is the gap between week four and the first agency that actually pays, not the build. Time is fifteen hours, spread over weekdays and one weekend morning. The surveyor who lost the version argument, I'll name him once he's said yes, not before. Same for the lawyer.

Two things I need from you before Monday, and both are in your own assumptions. Is the NIPOST key live or a test key, and can Stele be mounted this week? If neither is ready, agree the fixture path with me in writing today rather than us finding out on Wednesday.

Weekend call, yes. Saturday 2pm to 6pm your time, or Sunday 2pm to 6pm your time, both work for me. Pick one.
<!-- gate:body:end -->
