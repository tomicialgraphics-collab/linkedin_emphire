---
deliverable: comment
id: 2026-11-07_paolo-caressa-devfest-judge
date: 2026-11-07
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-07 via Google Scholar, the jsday speaker page and a Codemotion DevCast listing; LinkedIn itself returns 403 to any fetch. Paolo Caressa, IT Expert at GSE, the Italian energy services operator, external researcher at M&Mocs with work in software lifecycle and data science, adjunct professor and deep learning instructor, past speaker at jsday and Codemotion. He writes conference recaps that credit every speaker by name, so a comment that engages with one talk rather than the whole day is the right shape, and a mechanism he can check is the right register.
thread: his recap of DevFest Pescara, and the four talks he attended in full, one of which was on LLM-as-a-judge and observability
---

# Comment on Paolo Caressa's DevFest Pescara recap, 7 November 2026

## What the post is

A conference recap that credits four speakers in full and a dozen by name. The one in lane is Fabio Carusi's talk on
LLM-as-a-judge and data quality, with faithfulness and observability frameworks. The rest is compression, local
generative AI in the browser, and the cyber kill chain.

A recap post is a gift to a commenter, because the author has already put four hooks in it and named the people who
will read the replies. One hook is worth taking seriously and three are worth leaving alone.

## Draft, paste as a comment

The LLM-as-a-judge talk is the one I would spend the afternoon on. The frameworks give you a score, and the score
hides two things worth printing beside it: how often the judge agrees with a human on your own items, and which
judge version produced the number.

Without the first, a pass rate is a measure of agreement between two models, one of which was never tested. Without
the second, a judge upgrade quietly rewrites last quarter's history, and the dashboard still reads the same.

Observability usually ends at the trace. The judge is the part of the pipeline nobody watches.

## Why this shape

- Picks one of his four talks rather than summarising the day back at him. He attended the talks; he does not need
  them returned.
- The two additions are the ones that are missing from almost every judge implementation: an agreement figure and a
  version string. Both are checkable in a minute on his own data, which suits a reader who teaches.
- Names no tools and no vendor, because the talk was about frameworks and a comment that lists frameworks is a
  catalogue rather than an argument.
- No link to my own writing on the subject, although the post scheduled for 11 November is on exactly this. A
  comment that points at a future post is an advertisement, and this thread does not need one.

## Posting notes

- Post while the recap is fresh. Conference posts collect replies from the speakers tagged in them, and Carusi is
  the one most likely to respond here.
- If he comes back asking for the agreement figure method, the useful answer is to pull fifty items, label them
  yourself, and report agreement next to the headline result, because one number is a claim and two hold each
  other up.
- Nothing about clients, the benchmark or the refusal work in this thread.
