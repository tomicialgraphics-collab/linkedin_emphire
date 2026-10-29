# Arcezia engagement - RESUME (10-29) + re-sequenced test plan
STATUS: RESUMED. The 10-27 hold (bereavement) is lifted.
Window of record: test Thu 2026-10-29 + Fri 2026-10-30, private
report to Praveen first Mon 2026-11-02.
Scope of record: arcezia_scope_2026-10-24.md + the six accepted
markups (10-26, accepted in the 10-29 acceptance email).
Prep of record: arcezia_test_prep_2026-10-27.md (still valid; the
dates below re-sequence it).

## THE CHANGE (his, accepted): the key protocol
Replaces the scope's one-time key email (process item 1).
1. Sign in at app.arcezia.com with an email used ONLY for this
   test (create a fresh address; nothing else on it).
2. Keys page: issue the key. Shown once, only to the owner.
   Store it in the password manager locally. It never travels by
   email, never to a third party, never into the report.
3. Reply to his email with ONLY the sign-in email (so he can tell
   the test calls apart). The key itself is never shared.
Close: delete the account from its Organization page; that also
ends the key (supersedes "returned or destroyed at close").
Security note: the fresh test-only email means the test surface
is fully isolated from the owner's other accounts.

## TODAY (Thu 10-29), in order
1. Send the acceptance email (draft of record: /tmp/arcezia_accept.txt,
   326 words; salutation per the Arcezia exception).
2. Key steps (1-3 above). Send the sign-in email as a follow-up
   (one line, no key in it).
3. Account check: reach the agent surface (api.arcezia.com + docs
   + SDK), confirm the gate is visible.
4. Recon (prep doc): tool/action list, the gate's input (a plan? a
   tool call? an output?), the privilege boundary (which agent/role
   is lower, which is higher, how one would launch the other).
   Write the map into the findings log (it is report data).
5. Optional live demo (a): ONE chain, live, 15-20 min, before the
   commit runs (the scope's pre-commit moment; he watches the
   process).
6. Matrix at owner's pace: Class A (should-be-stopped action
   through the gate, full chains: cover first, harm later), Class B
   (privilege launches, gated-call class per markup 2), Class C
   (say/see/reach/do). Synthetic data only (markup 4). Single-
   session chains (markup 1).
7. Record the consequential attempts (OBS). Log holds AND hits
   (a clean hold is report data). Repro format per markup 5: exact
   request, full response, time in UTC.
8. Stay under the key's limit (markup 3, DoS out of scope).
   Engagement counter of record: 500, currently 0/500 (owner to
   confirm what the 500 counts).
9. End of day: findings in the log. NO report yet (report is Mon).

## TOMORROW (Fri 10-30)
- Second test day against the SAME gate (the no-deploy line was
  proposed in the acceptance email; pending his acceptance).
- Continue/close the matrix; re-run anything inconclusive.
- Findings log final for the window.
- NOTE: the original plan put fixes + live verification (moment b)
  on the 29th and the report on the 30th. The new window moves
  the report to Monday, so fixes land after the report: Mon
  (report) -> his fixes (Mon or after) -> owner re-runs the
  failing chains (live verification b, when it suits him) ->
  fix confirmation -> joint write-up -> publication after both
  sign-offs.

## MONDAY (11-02)
- Private report to him FIRST: findings, severity ranked by impact
  (unauthorized action / data exposure / privilege escalation),
  minimal repros, holds as well as hits, the M1b exclusions cited
  in the scope note.
- Collect the WRITTEN REFERENCE for the next client (scope credit
  term, delivered at report handoff). In writing, with the report.
- Close sequence: his fixes -> verification -> write-up (unpaid
  disclosed, per markup 6) -> publication only after both
  sign-offs, co-authored, bylines both, both channels.
- Account + key: delete the account from the Organization page
  (ends the key) at close.

## STOP CONDITIONS (scope, unchanged)
- The test ends when the window closes OR the gate holds against
  the agreed chains, whichever first.
- EMERGENCY STOP: access to data or accounts OUTSIDE the test
  account surfaces -> stop immediately, tell him, no further
  action until both sides agree.

## OPEN ITEMS (owner)
- Confirm whether the 10-28 v3 email (six-markup acceptance +
  redacted report attached by the owner) was actually sent. The
  10-29 acceptance email accepts the markups in writing either
  way, so the written record closes regardless; the record stays
  flagged until the owner confirms.
- Name of record: LinkedIn shows "Praveen Babu" (the scope doc's
  name); his 10-29 email signs "Praveen Dante". Treated as the
  same target owner; owner to confirm.
- The 1:01 PM LinkedIn line "Olusanya shared you the mail for
  reference" suggests a third participant in the LinkedIn thread
  (or third-person self-reference); the 9:28 AM email is the
  working reference either way.
- The no-deploy line (gate identical on both days) is PROPOSED in
  the acceptance email; status = pending his acceptance.
- The redacted past report: NEVER claim it is in his inbox unless
  the owner confirms the 10-28 send. It stays the owner's to
  attach; the record never states otherwise (10-27 correction).
