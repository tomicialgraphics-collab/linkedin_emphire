---
deliverable: internal
id: 2026-11-20_plan_cycle-one-build
date: 2026-11-20
audience: internal
status: ready
title: Cycle one build plan, Monday 23 to Friday 27 November, ten requirements
sources_read: >-
  read: ERI-REQ-v0_3.pdf, now stored beside this file with its extracted text. No page opened.
---

# Cycle one, planned

Ten requirements, 1.6 build days, inside a fifteen-hour week. The point of the week is not to finish ten things; it is
to find out on Monday whether the two things the whole build depends on actually work.

## Monday, first ninety minutes, before any code

**REQ-028 spike.** Send one batch of three test fingerprints to FORAY and read back a transaction ID and a block time.
Then open that transaction on a public explorer and confirm the ID matches. Nothing else.

Three outcomes:
- It works. Log the transaction ID in the daily note and start REQ-001.
- It works but the explorer link does not resolve. REQ-036 and REQ-031 both need re-planning, and Marvin needs to know
  on Monday, not in week three.
- It does not work. Cycle one is unaffected, but cycles three and four are, and the honest message to Marvin is that
  the schedule now has a hole where the anchoring sits.

**Same morning, one line each to Marvin:** is the NIPOST key live or a test key, and can Stele be mounted this week?
Both are assumptions in his own document, and either one failing stops cycle one at REQ-006 or REQ-004.

## The order, and why

1. **REQ-001 skeleton** (0.3). FastAPI, Postgres, one staging URL, health endpoint. Everything else needs it.
2. **REQ-004 Stele sign-in** (0.3). Do this second, not last, because if Stele cannot be mounted you need four days of
   warning, not four hours. If it cannot, agree a dev-only session with Marvin in writing rather than inventing one.
3. **REQ-002 translation files** (0.2) and **REQ-003 brand config** (0.1). Cheap, and they stop English strings leaking
   into every screen built after them. Doing them after REQ-005 to REQ-010 means rewriting the screens twice.
4. **REQ-005 postcode format** (0.1). Pure validation, no network. Test the three cases in the criterion, including
   the eleven-character string with and without spaces.
5. **REQ-006 server-side Lookup** (0.2). Key on the server, header `X-API-Key`, and a test that greps the response,
   the page source and browser storage for the key.
6. **REQ-007 address display** (0.1), **REQ-008 refused postcode** (0.1), **REQ-009 unreachable** (0.1). Three screens
   of the same call, so build them together with the three fixtures: valid, `valid=false`, timeout or 5xx.
7. **REQ-010 create the file** (0.1). Last, because it needs the address from REQ-007 to show.

If NIPOST is a test key that resolves nothing, point REQ-006 to a recorded fixture with the real response shape,
label it in the code and in the daily note as a fixture, and keep the acceptance criterion for the day the live key
arrives. Do not fake a pass and do not silently skip the requirement.

## What each requirement needs before it counts

Every acceptance criterion in this document is observable, so each one becomes one test, named after its ID. The
Friday review then reads as a table, not a story. Two of them are easy to fake and hard to prove:
- **REQ-002**: "no on-screen text outside the translation files" is a grep, so run the grep, and put its output in the
  review.
- **REQ-006**: "the key does not appear anywhere" is also a grep, over the response, the built page source and
  browser storage.

## The amendments to raise in writing, not to build silently

Build to the document as written. Send the six amendments from the review as proposed edits with exact wording, so
Marvin signs them or rejects them. Building them quietly means the acceptance criteria and the build disagree, and
that argument is worse on the Friday call than in a message on Monday.

The two that cannot wait past cycle two are the consent wording (REQ-012) and the name-consent capture (REQ-038),
because both touch a real person's rights and both are cheaper before the recording screen exists.

## The daily three lines, in the format he asked for

    Done:
    Next:
    Blocked:

One line each, no prose, sent every evening. If something is blocked, it says what and who can unblock it. That is
the habit he will judge the four weeks by, more than the code.

## Friday 27 November, what the review should show

A phone on the desk, the staging URL, and ten criteria checked in order with one failure if there is one. Not a
demo. The demo is week four; week one is evidence that the ten work.
