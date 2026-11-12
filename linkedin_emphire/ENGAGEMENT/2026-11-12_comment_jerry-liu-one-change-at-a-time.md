---
deliverable: comment
id: 2026-11-12_comment_jerry-liu-one-change-at-a-time
date: 2026-11-12
audience: public, under Jerry Liu's ParseBench-2 launch post
status: ready
approved: no
warm: no
profile_checked: 2026-11-12 from the post and the paper. Jerry Liu is co-founder and chief executive of LlamaIndex and the post announces ParseBench-2, OCRia-1.5 and a leaderboard. Third degree, not a connection. The post ends by inviting exactly this kind of feedback: if there is an error they should test, or a severity choice to disagree with, say so. The comment takes that invitation and nothing else, which is why it neither congratulates nor challenges any figure.
thread: the launch of a severity-weighted parsing benchmark, and what its scenario catalog does not measure
premise_checked: checked: the method, read in the paper's introduction on 2026-11-12. Their own sentence is that "each test scenario applies one change to a correct output on a particular page", and the severity policy fixes how much the score should drop for each. The score is the lower of a content score and a severity cap. So the observation in the comment is about the catalog as they describe it, not about a defect I infer. No figure from the launch is disputed and none is repeated.
sources_read: read: the launch blog, the first two chunks covering severity metrics, the expanded dimensions, results and the invitation; the ParseBench-2 paper, introduction and abstract, which is where the single-change sentence comes from; and parsebench.ai, the leaderboard and method notes. The technical report link in the post resolves to the same paper. The LlamaParse signup link is a registration form and was not opened.
---

## Comment, paste as is

Read the paper before answering the invitation at the end, so here's the one thing I'd add. Your scenarios apply a single change to a correct output on one page, and that measures how sensitive the metric is. Parsers don't fail one change at a time. A table comes back as a plausible list with every cell shifted by a column, or the whole page is transcribed confidently into the wrong reading order, and no single injected change looks like that. A metric can meet the severity policy across all 330 scenarios and still order two real outputs the wrong way round.

What would cover it is a pairwise test rather than an injected one. A few dozen real parser outputs over the same pages, ordered by someone who reads them for a living, and then the question is whether the scores produce the same order. Where the two disagree, the disagreement is usually correlated error, which is the shape the catalog can't represent.

## Why this and not a compliment

The post asks for an error to test or a severity choice to disagree with, and a reply that says the release is impressive answers neither. The single-change point is the one I would want them to hear, because it is the difference between calibrating an instrument against known perturbations and validating it against real failures, and they have the data to close it.

It is also deliberately aimed at the method rather than at the ranking. Challenging a launch number under the launch is the one move that would guarantee the comment is read as rivalry, and the number is not where their work is weakest.

## The careful part

No claim that their benchmark is wrong, and no claim that anyone has already done this. The paper says plainly what its scenarios are, so the comment takes them at their word and describes the gap in coverage that follows. If they have a pairwise study in a section I did not read, the right response is that they should point at it, and the comment still stands as the question a buyer would ask.

## If he replies

The follow-up worth having is which real outputs they would use, because the hard part is not the ordering but finding a set where two systems disagree in ways an expert would call meaningful rather than noisy.
