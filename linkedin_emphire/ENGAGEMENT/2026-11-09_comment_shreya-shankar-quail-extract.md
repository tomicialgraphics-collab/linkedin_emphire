---
deliverable: comment
id: 2026-11-09_comment_shreya-shankar-quail-extract
date: 2026-11-09
audience: public comment on Shreya Shankar's Quail AI.EXTRACT post
status: ready
approved: no
warm: no
profile_checked: >-
  Shreya Shankar, databases and HCI researcher, incoming assistant professor of computer science at Carnegie Mellon,
  co-author of Evals for AI Engineers. The post announces AI.EXTRACT in Quail and a paper, Copy That? Faster AI-Powered
  Extraction by Drafting from the Document. The mechanism described in the comment is read from the project's own pull
  requests on GitHub: the operator copies words that answer a question and returns a character span, and text not found in
  the document comes back with a null span. The claim about 33 clause types is from the CUAD workload as described there,
  not from the post.
thread: a copy constraint removes invention and leaves a harder error
---

## Why this one

A researcher posting a real system with a measurable claim, in his exact field, and the failure mode she has created is more interesting than the speed win she is advertising. The comment does not dispute the 2x. It names the error class that survives the copy constraint and asks for the one number that decides whether the operator is safe in a pipeline.

## Comment, paste as is

The copy constraint changes what a failure looks like, and the number I would want next is the one about nulls.

If an answer that is not in the document comes back with a null span, the model cannot invent a clause. It can still copy the wrong one, and a wrong span is harder to catch than an invented value, because it is verbatim and it looks checked. The dangerous output here is not a hallucination. It is a confident quote that does not answer the question.

CUAD gives you the clean negative set for measuring that: the clause types a given contract does not contain. The false-answer rate on those is what decides whether AI.EXTRACT can sit in a pipeline, because that is the branch downstream code reads as "not present".

Curious whether that is reported separately from span-F1.

## What not to say

No congratulations and no summary of the paper back to its author. Do not quibble with the speed numbers, which are hers and measured. Do not raise span-boundary scoring here; it is a second point and this thread only has room for one.

## Held

Span-boundary scoring. SQuAD-style exact match counts a span that includes two extra words as fully wrong, so a system can look worse than a human reviewer would judge it, and the reverse error, a span that is exact but semantically incomplete, scores as right. That is worth a post rather than a comment under a launch.

## Follow-on

She is one of the two authors of the evals book he will cite in public eventually. A comment that names a real gap and asks one question is the right introduction; a connection request with a pitch in it is not.
