---
deliverable: comment
id: 2026-11-08_ben-li-agent-eval-ownership
date: 2026-11-08
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-08. LinkedIn returns 403 to fetch, so read from cached profile and activity. Ben (Xiaojun) Li, principal software engineering manager at Microsoft building generative AI and Copilot for Teams messaging, twenty or more years in software and twelve or more in management, previously Apple and Intel, around 35 thousand followers. He writes about the A2E engineer idea, meaning the person who sits across eval design, behaviour shaping, orchestration, workflow redesign, change management and governance, and he posts about eval design specifically rather than in passing.
thread: his post arguing that agent eval is a product quality system rather than a benchmarking function, describing the Anthropic model of a dedicated evals team owning the infrastructure while product managers and domain experts contribute the tasks and run them, and promoting the launch of the evals book by Hamel Husain and Shreya Shankar
verified: the book and its authors are real and the launch event is linked in his post. Nothing in the comment depends on those facts, because a resource-list thread is the wrong place to argue about other people's book.
---

# Comment on Ben Li's agent eval post, 8 November 2026

## Why this one

This is the closest post to the actual work of anyone in the feed today: enterprise agents, eval as a quality system,
domain experts writing the cases. He is a manager at Microsoft who has to make that model work inside a large
organisation, so the useful contribution is the specific point at which the distributed model quietly fails.

He is also assembling a resource list in the comments, which means a comment that adds a mechanism rather than a link is
the thing his thread needs. Two of the people he tagged are the best known names in evals, so the comment is written for
that audience too, without addressing them.

## Comment

The distributed model works until you read what actually gets written down. When product managers and domain experts own
the tasks, they write the cases the product already handles, and the cases nobody thought of never appear at all. The
infrastructure team then reports a healthy suite that was never at risk.

The fix is small and mostly social: keep the disagreement that produced each case. Who expected what, which version of the
spec they were reading, and who decided the other behaviour was right. A pass rate is a number. The argument behind the
case is what stops the same argument coming back six weeks later.

That is also the part that survives a reorg, when the person who wrote the case has moved on.

## What not to say

No link to my own material under a post that is already a list of other people's material. No opinion on the book. No
claim about what Anthropic does internally, since he has described it and I have not seen it.

The word for the eval tooling in his post is his, and it is on the banned list in mine, so the comment uses suite and
tasks instead. Nothing is lost by that and the constraint is not worth explaining to him.

## Held for a later exchange

If he replies, the natural next question is how that disagreement record survives a model upgrade, when the evidence that
a case was ever contested is the only thing that tells you the suite changed meaning rather than the product changing
behaviour.
