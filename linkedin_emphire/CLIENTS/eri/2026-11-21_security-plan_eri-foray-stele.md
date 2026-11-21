---
deliverable: doc
id: 2026-11-21_security-plan_eri-foray-stele
date: 2026-11-21
audience: internal
status: ready
approved: no
title: The red team and security plan for the Ẹ̀rí test build, FORAY and Stele
time_checked: >-
  checked: 2026-11-21 07:20 WAT, read from the system clock in the sandbox before this file was written.
sources_read: >-
  read: DUNIN7/eri-test main at 4888b86 and the feat/event-table branch at 733db7a, fetched 21 Nov 2026: the PRD v0.2,
  REQ v0.4, the standards, DEPLOYMENT.md and DATA-RULES.md. Marvin's Stele message of 21 Nov 2026, 00:16 WAT. The
  23-case Stele table has not been read.
---

# Red team and security plan: Ẹ̀rí, FORAY and Stele

Olusanya Timothy · 21 November 2026 · for the Ẹ̀rí test build with Marvin Percival

The idea is simple. The security work runs beside the build instead of arriving at the end, and every step leaves
something behind that can be run again. That is the same thing I sell to clients, done here first.

## 0. Get written permission first

The Mac mini also runs FORAY and Marvin's other services. Before testing anything live, get a short written scope from
Marvin: which hosts, which services, which hours, and what is off limits. Testing code on my own machine needs no
permission. Testing his server does, and asking first protects the relationship.

## 1. Threat model, this week, before more code

Cheapest work, biggest effect, because it changes the design while that is still cheap. A short table of abuse cases:
for each attacker, what they want, how they would try, and whether the requirements catch it, miss it, or leave it out
on purpose.

- A family inventing a history, with a friendly "neighbour" attesting.
- A verifier who seals a story they know is false, or who is paid by one side.
- A rival claimant on the same postcode.
- An outsider forging or copying a certificate or QR code.
- Someone with access to the server, including whoever runs the Mac mini.
- NIPOST or FORAY failing at the moment of sealing.

Every miss becomes a new requirement or a line in the exclusions, so nothing is silently uncovered. It goes into the
repository as a pull request, as `docs/security/threat-model.md`.

## 2. The web app holes to test first

- **The public check page.** It needs no sign-in and shows evidence details, which makes it the obvious place for cross-site scripting. Put a script tag in a name or a statement and see if it runs.
- **Reading other people's files.** Can verifier A open or add to verifier B's draft files by changing an ID?
- **Uploads.** File type checks, size limits, and above all the GPS data hidden inside photos. A phone photo carries its exact location in the file. Strip it, and keep only the position the app means to show.
- **The NIPOST lookup.** Can a crafted postcode change the request the server sends to NIPOST? Does the key ever show up in a log or an error message?
- **The purge.** After content is purged, is it really gone, including logs, backups and Cloudflare's cache?
- **Dependencies.** The package lock is about 2,400 lines. Run `npm audit` and turn on Dependabot.

## 3. Stele recovery tests

Ask Marvin for the 23-case table, then write tests against it:

- Can a stolen recovery sheet be used inside the waiting period?
- What happens when a cancel and a recovery run at the same moment?
- Do the guessing limits survive a restart?
- Is every old session ended after a recovery?
- Does the response differ for an account that exists and one that does not? If it does, accounts can be listed.
- Are the origin and domain checks right when a passkey is registered?

The results go back to him as tests he can rerun, not as an opinion.

## 4. An independent FORAY checker

A small open script that takes a certificate's QR code, recomputes the fingerprints and checks the anchor on the
public explorer, with no help from Ẹ̀rí at all. That is what makes the public check independent. Also test what
happens when FORAY is down at the moment of sealing (REQ-049).

## 5. A red test suite in the repository

Every confirmed abuse case becomes a Vitest test that has to fail safely: the wrong action is refused. Run them on
GitHub's own cloud runners on every pull request. Those never touch the Mac mini, so they fit the deploy plan's rule
against a runner there. The append-only tests on the `feat/event-table` branch are the start.

## 6. Security reviewer on pull requests

Agree with Marvin that I review any pull request touching sign-in, uploads, the check page, anchoring or purging. One
line in the process, and it keeps the security work inside the build.

## 7. A full pass before the cycle 4 demo, written up

One complete attack pass on the finished demo, written in my four-part format (how to reproduce it, which layer
failed, the fix, how to check the fix holds), plus a page saying what was not tested. With Marvin's permission it
becomes my second named case study: an evidence product, tested by someone independent, with rerunnable findings.

**Later.** If speech-to-text or translation is ever added, testimony becomes text the system reads and acts on, which
makes it an injection risk. Flag it now so it is designed in.

## Order

| When | What |
| --- | --- |
| This weekend | 0, permission. 1, threat model |
| Before Monday | 3, Stele recovery cases, as offered to Marvin |
| Cycles 1 and 2 | 2, web app tests. 5, red test suite |
| Cycle 3 | 4, independent FORAY checker |
| Before the demo | 7, full pass and write-up |
| Every pull request | 6, security review |
