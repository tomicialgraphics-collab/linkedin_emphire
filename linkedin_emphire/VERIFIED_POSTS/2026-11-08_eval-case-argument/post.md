---
deliverable: post
id: 2026-11-08_eval-case-argument
date: 2026-11-08
audience: public
status: ready
approved: no
template: T6
headline: The score survived. The argument didn't.
subheadline: A suite that forgets why a case exists can't tell a worse product from a changed test.
headline_alt: Every eval case is a verdict with its argument deleted.
subheadline_alt: Keep the disagreement that produced the case, or the suite quietly changes meaning.
headline_alt2: The pass rate is the receipt, not the reason.
subheadline_alt2: Three fields per case, one minute of work, and the suite stops lying after a model upgrade.
box: WHY THIS CASE
box_alt: THE ARGUMENT
hashtags: [#AIEvaluation, #AgentEvaluation, #LLMEvaluation, #AIEngineering]
slot: 19:00 to 21:00 WAT, Sunday 8 November 2026, second post of the day
first_comment: none, the post stands alone
---

The score survived. The argument didn't.

Most eval suites can tell you their pass rate. Very few can tell you why a case exists.

Here's how a case usually gets written. Someone expects the system to do one thing. It does another. There's an argument, somebody decides which behaviour was correct, and a test lands in the suite carrying the verdict.

The verdict survives. The argument doesn't. Six weeks later the case is a line in a file that either passes or fails, and nothing in it remembers what it was defending.

That matters at the exact moment you need evals most. Swap the model, run the suite, and watch the number move. Now answer the only question anyone in the room actually cares about: did the product get worse, or did the test change meaning?

Without the history you can't tell, and the argument that follows is decided by whoever is most senior rather than by evidence.

Three fields fix it, and they take under a minute per case.

→ What was expected, in the words of the person who expected it. Not a restatement of the assertion.

→ Which version of the spec or the ticket they were reading. Those change more often than models do.

→ Who decided, and what the losing side argued. Ten words is enough.

That last one is the cheap one and the one people skip. It's also the only field that tells a new joiner that the case was ever contested, which is how a suite stops being folklore.

A pass rate tells you whether you're winning. The argument tells you what you're playing for.

#AIEvaluation #AgentEvaluation #LLMEvaluation #AIEngineering
