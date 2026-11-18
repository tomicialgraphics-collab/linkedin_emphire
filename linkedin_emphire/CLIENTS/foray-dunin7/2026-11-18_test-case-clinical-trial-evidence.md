---
deliverable: doc
id: 2026-11-18_foray-test-case-clinical-trials
date: 2026-11-18
audience: client
status: ready
approved: no
client: FORAY (Dunin7)
premise: >-
  He asked for one documented idea, in one of three areas, as a test case, and said he would come back with his
  interpretation and a structural roadmap. This is that document, written to be read in five minutes and answered in
  one message.
premise_checked: >-
  checked: no regulation, standard or trial statistic is cited, because none was read today and a compliance claim is
  a legal claim. The argument is limited to what a system can prove about its own records. The three modules are
  ordered by dependency and the first one is deliberately the smallest thing that demonstrates anything.
sources_read: >-
  read: the meeting record of 18 November and his answers to the four questions. No external page opened.
---

# One test case: evidence a sponsor can check without trusting the site

## The problem, in three sentences

A sponsored trial run at a site produces two records of the same event: the source document the site keeps, and the
transcription that reaches the sponsor. The gap between them is closed today by monitoring visits, which are
expensive, periodic and retrospective. When a dispute arrives months later, the question is what the site's record
looked like at the time, and the honest answer is that nobody outside the site can show it.

## The idea

Write one evidence record per participant event, at the moment the event happens, and anchor it through FORAY. The
record carries a hash of the source document, the event type, the time, and the identity of the person who signed it.
The document itself never leaves the site. The sponsor, or an inspector years later, receives the proof bundle and
checks two things without asking the site or us: that the record existed by a given time, and that it has not changed
since.

## Three modules, in this order

1. **Capture.** An event form for the four event types that carry the most weight, a hash of the attached document,
   and an anchor through FORAY. Small enough to build first and to test honestly.
2. **Verification.** A page where somebody holding the bundle can check the anchors and read a verdict per event, with
   the same discipline as the register: every pass ships with the limit of what it proves.
3. **Identity.** Staff signatures on events, through Stele rather than email, so that a signed event names a person
   rather than an inbox.

## Deliberately out of scope for the test

Integration with an EDC system, electronic signature compliance, and any payment to participants. The first is a
partner conversation, the second is a legal claim rather than an engineering one, and the third belongs to the Agent
Wallet later if it belongs anywhere.

## Why this one, and not property

It uses the two things he has already built rather than asking him to build something new, FORAY for evidence and
Stele for identity. It sits in a domain the owner has studied rather than one being learned from scratch, and it is
the same therapeutic area as the documents he is sending. Property is the next conversation, and what3words and the
DBL8 beacons are the right tools for it, but it needs a registry relationship that does not exist yet.

## Who pays, and why it repeats

The sponsor or the contract research organisation, per trial per site, because the cost of re-monitoring is what the
product replaces. That is a subscription shaped like the thing it substitutes, which is the recurring income argument
he made on the call, applied to one case rather than to a portfolio.

## What I would want back

His interpretation of the record structure, which is the part he will see faster than I will. And one question I
cannot answer from here: in a regulated trial, is anchoring evidence a legal problem or an operational one, because
the answer decides whether the buyer is a quality director or a general counsel.

## The four-week test

A synthetic site, twenty participants, sixty events, three deliberate tamperings introduced afterwards, and one
stranger given the bundle and a browser. What that stranger can verify without either of us in the room is the whole
result.
