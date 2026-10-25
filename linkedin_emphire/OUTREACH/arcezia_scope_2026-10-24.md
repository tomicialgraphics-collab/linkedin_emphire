# Engagement Scope — Arcezia Action-Gate Red-Team

Date: 2026-10-24 · Written record agreed in DM before keys

## Parties
Tester: Olusanya Timothy · Target owner: Arcezia (Praveen Babu)

## Window
Testing: Tuesday 2026-10-27 and Thursday 2026-10-29 · Private report out: Friday 2026-10-30

## Target
A fresh test account on Arcezia's live service, provided by the target owner. The key covers that account and nothing else. All testing runs from that account's surface only.

## In scope
- Getting an action that should be stopped to go through the action gate, full chains included: a cover first action, harm landing a later action
- Privilege launches: an agent launching a higher-privileged agent (the adk-python triage class)
- Method: external, behavioral testing only. The attack surface is everything an agent operating under the test account can say, see, reach, and do

## Out of scope
- Any other account or tenant, the hosting, the website, load or volume testing
- Whitebox: no access to, reading of, or reverse engineering of internal decision logic, source, or configuration. Findings come from observable behavior only
- Anything that touches data or resources outside the test account

## Process
1. Keys delivered after both sides mark up this scope; one-time delivery by email, deleted after receipt
2. Testing in the window; every finding kept with its minimal repro
3. Private report to the target owner first: findings, severity, repro, before anything is public
4. Target owner fixes; both sides confirm the fix. The tester does not implement the fix in code: finding, reporting, and verifying the fix are the tester's deliverables; building the fix is a separate, separately-priced deliverable
5. Joint write-up: target owner reads for accuracy and for anything not yet public. The findings and the repro stay the tester's

## Delivery model
The tester runs the test in the window using the provided key, at the tester's pace, and delivers the private report first. The two days of testing are not required to be done live on a shared screen. Two optional co-observed moments: (a) a short pre-commit method demo on the test account (one chain, live) so the target owner watches the process before committing; (b) live fix verification, the target owner fixes, the tester re-runs the chain in front of him and confirms it stops.

## Report
- Covers holds as well as hits: what was tried, what went through, what stopped it
- Severity ranked by impact: unauthorized action, data exposure, privilege escalation
- The test ends when the window closes or the gate holds against the agreed chains, whichever first
- Emergency stop: if testing surfaces access to data or accounts outside the test account, testing pauses and the target owner is notified immediately; no further action until both sides agree

## Publication
- The write-up ships only after the fix is confirmed, with both sides' sign-off
- Co-authored, bylines both; runs on both channels

## Key and data handling
Key used only for this engagement, not shared, returned or destroyed at close. No attempts on data or resources outside the test account.

## Terms
This engagement is unpaid, by agreement, for the stated
reason: the target owner is bootstrapped and will not
take on debt before the round. The fee is recorded here
as a one-time written waiver so it does not set a rate
default; the tester's rate is unchanged.

Agreed shape (both sides deliver inside the window):
- Test on the 27th and 29th; private report to the target
  owner first, on the 30th.
- The target owner fixes; the tester verifies the fix
  holds. The tester does not implement the fix in code;
  building the fix is a separate, separately-priced
  deliverable.
- Credit: the tester's name on every finding, bylined on
  the joint write-up in both channels; a written reference
  from the target owner for the tester's next client,
  delivered at report handoff.
- The joint write-up publishes only after the fix is
  confirmed, with both sides' sign-off; co-authored,
  bylines both, runs on both channels.

Superseded: the $100 commitment / $900 deferred structure
offered earlier on 10-24 was declined by the target owner
(declared pre-round debt) and is replaced by this
unpaid-with-credit agreement, accepted 10-24 8:30 PM.
