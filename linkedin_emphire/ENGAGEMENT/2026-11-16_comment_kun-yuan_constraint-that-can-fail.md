---
deliverable: comment
id: 2026-11-16_comment_kun-yuan_constraint-that-can-fail
date: 2026-11-16
audience: public
status: ready
approved: no
warm: yes
time_checked: >-
  checked: 2026-11-16 07:47 WAT, read from the system clock before this file was written.
profile_checked: >-
  Kun Yuan, first degree, founder and principal researcher at TRANTOR LABS, posting his own research rather than
  relaying someone else's. The post is one minute old at the time of the paste. He states his four questions in his own
  words and links a Pulse article; three of the four preprints are co-authored with two named professors, which is why
  the comment treats the questions as his and does not paraphrase the papers, none of which was read.
thread: >-
  four Zenodo preprints on auditable AGI claims, persistent AI identity, structural safety and governance accountability,
  introduced through four questions: who is acting, what governs the formation of an action, how do we know a safety
  constraint is effective, and can responsibility stay traceable over time.
premise_checked: >-
  checked: the comment answers his third and fourth questions and claims nothing about the contents of the four papers.
  No title is summarised, no finding is attributed to him or to his co-authors, and the article is not described because
  it was not opened. The two defects named are the author's own, reproduced on two revisions and recorded in the
  host-failure benchmark work of 15 November.
sources_read: >-
  blocked: nothing was opened for this comment beyond the post. The Pulse article, the Zenodo records and all four
  preprints are unread, and the comment is written so that it does not depend on any of them.
---

## Comment, paste as is

Your third question decides the other three, and it has a harder answer than it looks.

A safety constraint can only be shown effective by something that fails when the constraint is absent. Most audits never run that case, so the constraint reports satisfied on the strength of a check that couldn't fail. One verifier I audited compared 16 of 64 hash characters and passed fifty checks. Every pass was true and none of them was evidence.

Question four has the same shape. Traceability isn't the journal existing, it's the journal still naming the right record after a restart. Specimen I keep: a retry stored the verdict at 4, and the conflict raised against it pointed at 3, a number replay had withheld. Both records were intact. The link between them wasn't.

Who is acting is a read of the log. Whether the log can be wrong after a failed recovery read is the question underneath it, and it's the one that decides whether the other three survive contact.

So the thing I'd ask of all four preprints: which of them carries a test that fails when the property is absent?

## Why this angle

Four questions where the second, third and fourth all resolve into the same engineering problem: a claim about a system is only worth what the instrument behind it is worth, and an instrument nobody has tried to break is a formality with a pass rate.

His four questions are also unusually close to the work in this repository, and that is the reason to answer carefully rather than enthusiastically. Agreeing with a researcher about the importance of auditability adds nothing. Naming two defects that his own questions predict, with the numbers attached, is the only kind of reply that gets a founder to look at the profile.

This comment deliberately does not say which preprint to start with, because none of them has been read. Suggesting a reading order would be a claim about his work dressed as interest.

## What this is not

This is not a pitch. No link, no offer, no mention of packages or prices. He is a researcher publishing preprints, not a company with a security questionnaire.

Nor a summary of his work. Every sentence about traceability is grounded in a defect that was reproduced twice, not in a paper.

## If he replies

The opening is the one real question: does any of the four carry a negative test, or do they describe properties that are asserted rather than exercised. If he says the papers specify tests, ask for one concrete failing case and offer to run it. That is a conversation about his work rather than about selling, and it is the only version of this that ends anywhere useful.
