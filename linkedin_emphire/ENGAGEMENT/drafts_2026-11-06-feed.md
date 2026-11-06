# Feed drafts, 6 November 2026

## 1. Bryan Khoo, Section 833 and the BCBS tax deduction (3h)

Post: the 1986 Section 833 deduction, the JCT estimate, and the Michigan comparison against a national
prior-authorization average. Kevin S. has already corrected the comparison in the thread, and Adam K.
has endorsed the correction and added the point that the original Blues qualify by existing in 1986
rather than by meeting the tests.

My comment, to be posted as a reply on Bryan's post, not on the Mark Cuban line, which has nothing
to add to.

---

Kevin and Adam have the substance: the Michigan figure compares a Medicaid plan's prior authorization rate with marketplace claim denials, and it does not survive being put side by side.

The stronger version is already inside the statute. Section 833 has two doors. Plans that qualify by having existed in 1986 without material change, and nonprofit plans that have to earn it through open enrollment, pre-existing conditions, community rating and an 85% MLR. Same deduction, two populations.

That is a natural experiment nobody has run in public. Grandfathered plans against test-qualifying plans, same state, same measure. If they behave differently, the grandfather clause is doing the work and the argument holds. If they behave the same, the deduction is not the lever, and the case has to be made on the formula itself, which is the more interesting argument anyway.

The anger is justified. A two-door comparison is what makes it stick.

---

150 words. No numbers invented. Credits the two commenters before adding, which is what keeps a
mid-thread correction from reading as a pile-on.

## 2. Paolo Perrone, RAG bugs that start at parsing (9m)

Post: most RAG failures blamed on retrieval begin in parsing, a flattened table is gone before the
reranker sees it, and at $1 per 1,000 pages you can re-parse the whole corpus whenever you catch one.
Adit Abraham's Reducto launch post below it carries the same $1/1,000 pages figure, so the two read as
one message from the vendor side and one from the newsletter side.

My comment goes on Paolo's post only. The vendor launch post is a congratulations thread and there is
nothing technical to add to it that the launch itself has not already said.

---

Right about where it starts, and the cheap re-parse is what makes it actionable.

The part worth adding is that a flattening parse does not fail. It produces prose that looks like the document. Downstream, at retrieval and at generation, "the figure is not in this document" and "the figure was destroyed on the way in" are the same observation, and only one of them is fixable.

At a dollar a thousand pages the fix is affordable, but cost was never the whole obstacle. To re-parse the right pages you have to know which ones, which means keeping the parse artifact and diffing it against the next one. Otherwise a better parser just changes the answers, and nobody can say which changes were improvements.

Do you keep the intermediate parse as an artifact, or only the extracted text?

---

131 words.

## 3. Shubham Vora, make the AI grade itself before it writes (20m)

Post: three prompts run in one chat, a rubric first, an assumption check, then a self-grade that quotes
the failing line and rewrites only that line. 1st degree connection, GTM and growth audience.

---

The three steps are the right shape, and the third is the one that will quietly stop working.

The rubric in step 1 is written by the same model that then has to pass it, so five out of five is evidence of consistency between two outputs from one source, not evidence the reader would reply. If the model does not know that a VP checks whether you read their last earnings call, that check will not be in the rubric, and the email passes a test that was never the real one.

Two things fix it. Build the rubric from evidence the model did not produce, actual replies and actual deletes, or the buyer's own words. Then keep the score next to the outcome for every send, so after fifty you can see which of the five checks tracks replies and drop the others.

Otherwise the grade is a receipt for work the grader defined.

---

136 words.

## 4. Mohit Rathod, zero initialization and the loss that never moves (1h)

Post: zero and constant init as the silent bug, symmetry in the forward pass, gradient collapse in the
backward pass, Xavier against He, and a closing question asking which first signal people saw in
production. He asks a question, so the comment answers it and then adds the part the slides cannot
cover.

---

Both, and they turned out to be different bugs.

Zero gradient variance across hidden units at the first backward pass is the signal I trust. If per-unit gradient norms come back identical at step one, the network is one unit wide, and you know that before the epoch ends. A loss plateau is the same fact arriving later and blurrier.

The production warning is that an exactly constant loss has three causes and they look identical on the metric. Weights moving with a flat loss is usually a logging or cached-metric bug. Weights still and gradients identical is symmetry. Weights not moving at all is a frozen parameter or a detached graph.

So before changing the initializer, print the weight delta between two steps. One line tells you which of the three you have, and only one of them is an initialization problem.

---

138 words.
