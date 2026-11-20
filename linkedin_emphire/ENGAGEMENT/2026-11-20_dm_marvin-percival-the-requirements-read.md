---
deliverable: dm
id: 2026-11-20_dm_marvin-percival-the-requirements-read
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Marvin Percival
premise: >-
  Marvin sent the Ẹ̀rí requirements at v0.3, forty-five requirements over four cycles with acceptance criteria, after
  asking whether the owner could start on Monday 23 November and asking for worries, weekly time, and names of a
  surveyor and a lawyer. This reply confirms the arithmetic, names the one requirement that carries the rest, puts the
  first thing to test before any code, lists six gaps with proposed wording, adds one negative control, and asks which
  of two blocking assumptions will be ready on Monday.
time_checked: >-
  checked: 2026-11-20 00:44 WAT, read from the system clock before this file was written. That is 18:44 on Thursday in
  New York.
profile_checked: >-
  Marvin Percival, who numbers everything and expects numbered answers, who wrote acceptance criteria a stranger could
  run, and who asked to be told where he is wrong. The reply is in his order, credits the document in two sentences
  rather than ten, and puts every objection next to the wording that would fix it.
premise_checked: >-
  checked: every requirement number quoted here was read from the document itself, and the build-day totals were added
  up from its own table: 1.6, 1.5, 1.3 and 2.1 make 6.5. The claim that the schedule fits rests on fifteen hours a
  week, sixty hours over four weeks, against roughly fifty-two of build. No legal claim is made, and no fee, split or
  ownership term appears.
sources_read: >-
  read: ERI-REQ-v0_3.pdf in full, eight pages. No page opened.
---

## Message, paste as is

<!-- gate:body:start -->
Read it twice, all eight pages. The thing that stands out is that almost every requirement has an acceptance criterion a stranger could run, with the exact words on screen. That is rarer than it should be, and it means I can argue about the work instead of arguing about what the words mean.

The arithmetic first. 1.6, 1.5, 1.3 and 2.1 is 6.5 build days, about 52 hours. Fifteen hours a week over four weeks is 60, so the plan fits with a day or so spare for reviews and the demo. Cycle one is ten requirements, not the eleven I asked for on the call. Ten is what the document says, so ten it is.

The one that carries the rest is REQ-035 with 034 and 036 under it. A stranger with the file and no account is told whether it matches a sealed item, and the anchor opens publicly. If that fails, the certificate is a private diary with a QR code.

But the first thing I'd test is not that. It's REQ-028. Does FORAY return a transaction id and a block time I can open on a public explorer, for a batch of fingerprints, today? If it doesn't, cycles three and four both fail and we'd find out in week three. I'd rather know on Monday morning, before writing the first line of REQ-001.

Six gaps, in the order they bite.

One. Consent is your tick, not her words. REQ-012 disables save until the verifier ticks "Speaker gave consent", which records what the person holding the phone says, not what she agreed to. Recording is not publishing. My addition: the consent prompt names the three permissions in her language, she says them aloud, and we store the prompt text, the language and the timestamp with the item.

Two. REQ-038 says a private person's name appears only when consent to show it is recorded, and nothing in the document captures that consent. So the requirement can't be met honestly yet. It needs its own step: per person, per file, dated, revocable.

Three. Withdrawal has no state. You have dispute in REQ-026 and nothing for an attestor who takes his back. It should be a new event, never an edit, and it should show on the certificate with its date.

Four. Deletion and the anchor contradict each other. REQ-043 deletes the demo within thirty days, and REQ-028 puts fingerprints somewhere that cannot be deleted. Pick one sentence and put it in both places: deletion removes the content and the page, the fingerprints and their anchor stay, and anyone holding the file can still prove it existed on that date.

Five. REQ-014 stores accuracy in metres and nothing says what it isn't. One line under every photo: the phone's position when it was taken, accurate to roughly N metres, and not a boundary.

Six. Sealing has no failure path. NIPOST has REQ-008 and REQ-009 for refused and unreachable, and FORAY has neither. If the anchor call fails, nothing is anchored, nothing says it is, and the screen says so.

And one addition I'd argue for. Seed a single item whose stored fingerprint doesn't match its content, and require REQ-035 to say no match for it, on every release. Without it the public check is a test that has never failed, which is the exact problem we started this conversation about.

Two assumptions can block week one. The document says NIPOST test keys don't resolve live postcodes, and that Stele can be mounted into the server. Either one failing stops cycle one at REQ-006 or REQ-004. Which of the two will be working on Monday? If neither, I'd rather agree a fixture path in writing than find out on Wednesday.

Monday the 23rd stands, fifteen hours a week, and the daily three lines start that evening.
<!-- gate:body:end -->
