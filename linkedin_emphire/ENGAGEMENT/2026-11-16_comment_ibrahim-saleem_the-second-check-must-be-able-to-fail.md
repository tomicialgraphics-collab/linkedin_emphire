---
deliverable: comment
id: 2026-11-16_comment_ibrahim-saleem_the-second-check-must-be-able-to-fail
date: 2026-11-16
audience: public
status: ready
approved: no
warm: no
time_checked: >-
  checked: 2026-11-16 09:45 WAT, read from the system clock before this file was written.
profile_checked: >-
  Mohammad Ibrahim Saleem, followed, AI security and governance engineer at AT&amp;T and a researcher at the University of
  Houston, working on agentic AI security, LLM red teaming and MCP and RAG security. The post is one minute old at the
  time of the paste and states his own position rather than relaying an article, so the comment engages the position.
thread: >-
  AI for security versus security of AI, framed as two jobs that get mixed up: the model as tool, where code should own
  the facts and a human the decision, and the model as target, where the risk sits in what surrounds the model rather
  than in the prompt. His rule: AI can speed up the work but should never be the last check on its own work.
premise_checked: >-
  checked: the one figure in the comment is the author's own audit, a verifier comparing 16 of 64 hash characters that
  passed fifty checks, published on the profile. Nothing is asserted about AT&amp;T, about his team, or about the contents
  of his article, which was not opened. No claim is made about his three questions, which are accepted as written.
sources_read: >-
  blocked: no page was opened for this comment. The blog link was not followed and nothing in the comment depends on what
  it says.
---

## Comment, paste as is

Your last rule is the one I'd underline, and it has a corollary that gets missed: the second check has to be able to say no.

I audited a verifier that compared 16 of 64 characters of a hash and passed fifty checks. Nothing about it was fragile. It was incapable. Every pass was true and none of them was evidence, and a team reading the green tick had one fewer check than it thought it had.

The other half is independence. A second model reading the summary the first model wrote is not a second check, it's the same check twice. Independence lives in the evidence: a different reader, the raw artifact instead of a description of it, and a run somebody else can repeat.

So the question I'd add to your three is the one nobody asks: if the last check had been run against work that was wrong, what would it have said? If there's no answer, you have a signature rather than a review.

## Why this and not agreement

The post is right and it is already well argued, so agreeing with it would be read as noise. The one place it can be pushed further is his own rule, which states the requirement for a second check without stating what makes a second check real.

Two properties do the work. It has to be capable of failing, and it has to be independent of the thing it is checking. Neither is about who is in the room.

That distinction matters for his audience specifically, because the natural reading of never the last check on its own work is that a human or a second model is enough. The verifier story is the counterexample: the second check existed, ran fifty times, and could not have caught anything.

## What this is not

Not a pitch and not a link. He writes about the same subject, so a comment that sounds like an advert would be worse here than anywhere else.

Not a claim about his article. It was not opened, and the comment stands on his post alone.

## If he replies

The interesting question is whether he has ever seen a check that passed for reasons unrelated to the work, because most engineers have and most organisations never find out. That is the conversation worth having, and it is his subject rather than the owner's.
