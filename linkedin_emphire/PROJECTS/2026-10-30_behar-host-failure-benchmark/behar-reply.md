# Messages to send Behar

Three drafts: the reply to send now, the follow-up for when the patch is
delivered, and short answers for the questions he is likely to ask next.

Nothing here claims the patch is finished. It is not.

---

## 1. Send now

Behar, thank you. I read the audit twice and then reran the counterexamples myself rather than take them on trust.

You are right on the P0s. Six of the seven reproduce on my machine, including the two that matter most: a WAL verdict flipped from BLOCK to ALLOW with a stale signature still verifying clean, and deleting seven host journals still leaving a full pass. One is worse than reported. T14 does not just clear a named gap, it also clears it in the verifier's own recomputation, so the store and the checker agree that a forged unsigned record closed a gap.

Two claims of mine are wrong and I am withdrawing them rather than defending them. The note calls the store an independent issuer of identifiers when it accepts an id from the caller, and it says nine scenarios where the suite runs eight.

One correction on your side. T08 does not behave the way the report describes it: changing only the WAL timestamp makes B.wal fail and B hold, the reverse of the line in the report. The substance of F2 stands, but the regression test should be written against what actually happens.

I have a written response, finding by finding, and a reproduction script with one mode per finding that anyone can run against the repository. The P0 fixes are in progress. I will send the patch when the counterexamples come back failing.

Author order and venue stay where we left them until then.

---

## 2. Send when the patch lands

Behar, the P0 patch is ready.

Six changes, and each one is tested by the counterexample that beat the old code. A flipped WAL verdict now fails B instead of verifying clean. A deleted host journal now fails the completeness and scenario checks instead of passing. A rewritten actor, policy or timestamp now fails D. A torn host journal now produces a report with an explicit unreadable state instead of a traceback.

Two things are in the patch beyond the fixes. The verifier no longer imports the machinery it is checking, so a change in the encoder cannot pass itself. And the seven counterexamples ship as a regression script, so each fix keeps a test that can fail again.

Nothing here closes P1 yet: journal before memory, non-destructive repair, conflicts on duplicates, store-minted ids and the reply validation in the host are still to do.

Two requests, both about permanence. Put your 38-case package into the repository as audit/, so the counterexamples live next to the code rather than in a report about the code. And let me cite your review in the note once P1 lands.

---

## 3. If he asks

**"Can you demonstrate genuine host loss?"**
Not on one machine. C, C' and C'' exit with os._exit(9), so what the suite tests is a process that leaves deliberately, not a host that disappears. I will rename it everywhere, state the failure domain in the note, and list the two experiments that would cross it (an external kill at a barrier, destruction of the host-local filesystem). Both need a second failure domain: another machine, or a container with its own volume. I would rather declare that out of scope than simulate it and call it host loss.

**"Why should a substituted timestamp fail rather than be marked unverified?"**
Because a counter step is either in the host journal or it is not. If it is not, the record is claiming a decision the host has no evidence of, and unverified is too generous a word for it.

**"Is the suite still worth publishing?"**
As a demonstration of the named-gap result, yes, and your Appendix B is close to the sentence I would use. Not as authenticated recovery or host-loss survival. Those stay blocked until P0 and P1 are done and the claims matrix shows a test behind every guarantee sentence.

**"What about authorship?"**
Unchanged and settled the same way we agreed: at finalisation, against CONTRIBUTION.md, after the patch cycle.

---

## For you, not for him

- Do not say the patch is delivered until the zip is in his hands.
- If he pushes on severity, the line to hold is: the limitation was disclosed, the verdict line contradicted the disclosure. That is the defect, and it is fixable without a new external witness.
- The audit's own section 2 says 37/38 is not a reliability percentage. Do not restate it as one either way.
