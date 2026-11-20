---
deliverable: doc
id: 2026-11-18_foray-meeting-record
date: 2026-11-18
audience: internal
status: ready
approved: no
client: FORAY (Dunin7)
time_checked: >-
  checked: 2026-11-18 22:12 WAT, read from the system clock before this file was written. The call ran from 14:00 WAT,
  and the notes were auto-generated at 15:02 UTC, which is 16:02 WAT.
premise_checked: >-
  checked: every fact below is taken from the auto-generated notes and transcript of the call, both of which contain
  transcription errors. The correction that matters is that the transcriber wrote 4A throughout where the word spoken
  was FORAY; the owner confirmed this. Dunn and Seven is Dunin7, SPX Enigma is SBX Enigma, and Double Eight is DBL8.
  No figure, date or claim from the transcript is treated as verified, and the personal address that appears in the
  transcript is deliberately excluded from this record.
sources_read: >-
  read: the meeting notes and the full auto transcript supplied by the owner. No external page opened, so the Common
  Criteria claim is recorded as his statement rather than as a verified registration.
---

# Meeting record, Marvin Percival, 18 November 2026

14:00 WAT, 08:00 his time, Google Meet, roughly one hour. Notes auto-generated; transcript has errors. **Wherever the
transcript says 4A, the word spoken was FORAY.**

## What the call was

Not a review call. The register questions were answered in a PDF he had written the same morning and sent before the
call, so the hour became an introduction to what FORAY is, what he has built, and what he wants to do next. The four
answers he gave are already recorded in the owner's notes; the substance here is everything after them.

## What he said about FORAY

- **The specification is the judge.** Where the checker and the specification disagree, the specification is what is
  promised to the world and the checker is one program trying to follow it. He gave both directions: the program was
  wrong in the record-matching case, and the specification text was wrong when an amendment still described the
  segments serialiser as unbuilt. Both were fixed, and the superseded wording was left visible.
- **A segment is a note in the header** saying pages 3 to 5 are in this batch and page 5 ends with a given
  fingerprint. He states the checker reads both forms: two live tests with the note in the header directly, and one
  inside an aggregate. Three batches, pages 0 to 8, checker says valid.
- **The service never sees client data.** The argument is contractual rather than technical: the moment it stores or
  manages client data it becomes part of the transaction and takes on a duty it does not want. Adapters on the client
  side accumulate and hash; only hashes reach the service.
- **Batching.** Buffers expand and contract with volume, including by time of day. A client can ask for immediate
  anchoring of a single transaction and get the reference back at once. Batches are segmented by sender and each batch
  gets a Merkle tree, so one hash per batch goes on chain.
- **Attestations and binary objects.** A hashed document, such as a signed lease, can be registered so the record of
  its state at registration persists. An attestation is a notarisation: a third party stating that something was true
  on a date, and it can be anchored the same way.
- **Agentic work is the next load.** Agent identity, millions of transactions a second, and, in his words, agents
  submitting the reasons they allowed a loan and not only the loan. An **Agent Wallet** enforces spending permissions
  through blockchain covenants and proof checks, with instant shutdown, and he is explicit that shutdown cannot depend
  on a human because humans cannot keep up.
- **Reconstruction and normalisation.** An adapter reads any database, SQL or MongoDB, from any year, and turns its
  transactions into FORAY records. That normalises manufacturing, financial and supply chain history into one place.

## What else he has built

Barclays New Zealand banking system, built alone and sold after a one-transaction-type demonstration; the same software
into three Australian banks, which is what moved him to Sydney; an international banking system in the United States;
cancer registry systems for a hospital network; a security patent; **SBX Enigma, Common Criteria certified in 2009**,
for protecting high value data, which he says is now re-created as a current project called **OVA**. Alongside those:
**DBL8**, Bluetooth low energy readers and beacons, used to track patients and staff in medical practices, and
**Stele**, identity management for humans and for agents, deliberately not built on email or text verification because
both are compromisable.

He also had Claude produce a ranked list of **24 projects** from his own work, with tamper-evident records first,
the FORAY adapter second.

## What he offered

- The SBX Enigma certification documents, and the diabetes documents he wrote recently, one of them on Ghana.
- Four or five DBL8 readers and a set of beacons, to play with, as he has done for contacts in Suriname and Trinidad.
- Help turning one idea into a requirements document, function by function, using his own method, which he
  distinguishes sharply from vibe coding.
- To read one idea and come back with his interpretation and a structural roadmap.

## What was promised in return

One project idea, documented, in one of three areas the owner named: healthcare and clinical trials, fintech and
blockchain, or property. One test case, not a portfolio.

## Read of the call

He is not buying a review. He is offering to mentor and co-design, and he said so more than once, including that he is
not a competitor and has nothing to sell. He is 74, retired, and says plainly that he does it because he loves it.

Two things follow. The register work stays finished and the W-04 re-run stays a separate, small, priced item that he
has not asked about. And the collaboration he is offering is real but unpriced, so it should be bounded at one test
case until somebody puts a number on something.

## Risks

- **Enthusiasm without revenue.** Twenty-four projects and an offer of hardware is a large surface and none of it is
  income. One test case, one written interpretation, then a decision.
- **Free work in the wrong direction.** Designing his projects for him is not the same as building something the owner
  can sell. The test case has to be in the owner's market, which is what he asked for anyway.
- **Transcript accuracy.** Nothing from the auto transcript should be quoted back to him as his own words without
  checking, and the personal address in it is not to be repeated or stored.
