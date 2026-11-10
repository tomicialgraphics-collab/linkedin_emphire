---
deliverable: post
id: 2026-11-09_span-boundary-scoring
date: 2026-11-09
audience: public
status: ready
approved: no
template: T1
headline: Exact match scores the truncated answer as right and the complete one as wrong.
subheadline: Span scoring rewards stopping early, and every copy-based extractor inherits it.
headline_alt: Two extra words score zero. The first clause scores full marks.
subheadline_alt: A metric that cannot tell generosity from error teaches the model to be less useful.
headline_alt2: The right answer in the wrong place scores nothing.
subheadline_alt2: Three numbers to report together, so a long span is not filed as a miss.
box: TWO EXTRA WORDS
box_alt: BOUNDARY, NOT FACT
hashtags: [#AIEvaluation, #LLMEvaluation, #AIEngineering, #AISecurity]
slot: 13:30 WAT, Monday 9 November 2026, ahead of the 19:00 launch post
first_comment: none, the post stands alone
---

Exact match scores the truncated answer as right and the complete one as wrong.

If your extractor returns the words from the document that answer the question, most span metrics will punish it for quoting generously and reward it for stopping early.

Exact match compares what came back to a single gold span after normalisation. Add two words, even the clause that makes the answer true, and the score is zero. Cut a three sentence answer down to its first clause and the score is full marks. So the metric is not measuring whether the answer is correct. It is measuring whether the span ends where an annotator decided it ends, and that ending is a convention, not a fact.

Hand the same clause to two annotators and ask them to underline the part that answers the question. You will get two defensible spans and a rule that accepts one.

Three numbers worth reporting together, because each is blind where the other sees:

→ Character overlap, so a span that contains the whole answer but runs long is not filed beside the ones that missed it entirely.

→ Boundary agreement on its own, because that is what breaks in production: the extractor knows the answer and does not know where to stop reading.

→ A rate for the absence cases, since a clause that is not in the document has no gold span and exact match has nothing to say about it.

That last one is the branch your pipeline actually reads, because a null is what triggers the downstream code. A metric that cannot score it leaves the most consequential output untested.

Punishing the honest quote and rewarding the truncated one is a training signal. Models learn it faster than they learn the task.

#AIEvaluation #LLMEvaluation #AIEngineering #AISecurity
