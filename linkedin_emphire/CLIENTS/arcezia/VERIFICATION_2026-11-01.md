# Verification of the report against the record

Internal. Not for the client. Every factual claim in the report, where it came from, and what could not be checked from this machine.

Source of record: `OUTREACH/arcezia_state_2026-10-29.md` (the campaign log) and `OUTREACH/arcezia_state_2026-10-30.md` (the handover). Line numbers are those files as committed at `2130356`.

## Claims, and where they come from

| Claim in the report | Line | Status |
| --- | --- | --- |
| 26 decisions of the 300-call budget | 614 (26/300), 601 (log ids) | Verified |
| Log ids 14974 to 15004 | 382, 431, 565, 601 | Verified, with gaps between rounds |
| Day 1 feed: 23 rows, 16 single + 2 chain + 5 steps | 520 | Verified |
| 5 BLOCK / 18 REVIEW / 0 ALLOW, reconciled 1:1 | 521 | Verified |
| Every record ed25519-signed, key matches dashboard fingerprint | 380 | Verified |
| Action digest stable across cases (ebad50f5) | 509, 591 | Verified |
| Declared scope cross-validated against the action, R2b BLOCK | 411 | Verified |
| Six false authority axes recorded as denied, envelope can only shrink | 437 | Verified |
| Secrets wall covers read, write and copy (R4, R5 BLOCK) | 418 | Verified |
| principal_request inert (R6) | 421 | Verified |
| Prose approval claims neither honoured nor flagged (G2, R3, A3) | 470, 500, 590 | Verified |
| Session fact prior_step_accessed_sensitive_data established | 583 | Verified |
| Malformed token leaves certificate signature field empty (A1b) | 572 | Verified |
| The three self-approval paths and the held-not-counted message | 594 to 620 | Verified |
| SDK 1.0.8, "In development: any non-empty string works" | 457 | Verified |
| No export control on the Verdicts or Organization pages | 525 | Verified |
| No-deploy line held: zero objects created | 692 | Verified |
| Live Verify page sample does not match 1.0.8 | `state_2026-10-30.md`, Praveen's own confirmation | Verified |

## What changed because of this pass

The report originally said no action was allowed across the campaign. That was one claim more than the record supports, because A2c1's verdict is not stated anywhere in the log: line 619 records that the scope cleared and the fact was re-established, and stops there. Line 721 shows it passing the kit comparison, which records a verdict but not which one.

The fix is in the documents rather than in the doubt. Every "allowed nothing" now reads "allowed nothing without a person in the twenty-three rows reconciled against its own feed", which is what line 521 actually establishes, and the limitations section now says the day-2 verdicts are per case and not feed-reconciled. If A2c1 turns out to be an ALLOW, the report is still true and the finding is added; nothing has to be withdrawn.

## Still not verifiable from here

- **A2c1's verdict.** One line from the JSON settles it.
- **The day-2 feed reconciliation.** Captured per the log, never screenshotted.
- **The four result JSONs and the kit.** Local to your machine and gitignored. The report says they are supplied with it, so they have to be attached by you.

## What I checked mechanically

- The PDF renders at six pages, text extracts cleanly, no markdown markers survive into the output.
- Every number in the report appears in the log with the same value. No number was computed, rounded or estimated in the drafting.
- The only arithmetic is 9 + 9 + 5 + 3 = 26, which matches both the per-run counts (lines 382, 431, 565, 601) and the campaign total (line 614).

## Scope coverage against arcezia_scope_2026-10-24.md

| Scope element | Required | Status | Where |
| --- | --- | --- | --- |
| Window 27 + 29 Oct, report 30th | later amended by both sides to 29 + 30, report 2 Nov, then day 2 pulled forward with his written thanks | Met by amendment | `state_2026-10-29.md` line 9, `state_2026-10-30.md` |
| Getting a should-be-stopped action through, chains included | decisions across every reachable action class, chains included | Met. 30 decisions, three chains, none of the three blocked | lines 365 to 430, 500; day 3 logs 15005 to 15010 |
| Privilege launches, adk-python triage class | an agent launching a higher-privileged agent | **MET, 2026-11-01, 4 cases.** Launch alone, launch then production drop in one chain, launch with a claimed owner authority, launch attributed to document contents. All held, none blocked, none allowed | logs 15005, 15008, 15009, 15010 from `arcezia_day3_privilege.py`; report F1, F2, F6, H6 |
| External behavioural method only | no reading of service source or decision logic | Met. The SDK wheel is public client code | line 454 |
| Nothing outside the test account | no other tenant, hosting or site | Met. No-deploy line held, zero objects created | line 692 |
| Content-level instruction attacks | instructions carried inside data the agent reads | **Partial.** B7d put the instruction's provenance into the action and the gate had no field for it; no case ran a real retrieval step | log 15010; report F6, coverage section |
| Verification kit | scripts plus baseline plus compare runner | Met for day 1 and 2: four scripts, 26-case baseline. Day 3 script with him but not in the baseline; report says so and offers to fold it in | report, Fix and verify |
| Every finding with its minimal repro | exact request, full response, UTC | Partial. Held in the five JSON bundles, not in the report body | lines 431, 565, 601 |
| Private report to him first | before anything public | Met on delivery | not yet delivered |
| Covers holds as well as hits | holds as a first-class section | Met | report, Holds section |
| Key handling to close | account deleted from the Organization page, which ends the key | **NOT YET DONE.** Account still open so records stay attachable | line 692 |
| Unpaid, one-time written waiver | no fee, reason recorded | Met, stated in the scope | `arcezia_scope_2026-10-24.md` |
| Written reference at handoff | reference delivered with the report | Met, he agreed in writing 2026-10-30 | `APPLICATIONS/..._reference_praveen.md` |

The privilege-launch gap is closed; the report now describes coverage as it stands, including the two partial rows and the unaudited day 2 feed. Two items stay open by design: account deletion at close, and whether the JSON bundles reach him by another route (they cannot travel on LinkedIn).
