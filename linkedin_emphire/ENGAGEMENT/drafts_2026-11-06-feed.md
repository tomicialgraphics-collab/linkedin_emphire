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
