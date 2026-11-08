---
deliverable: comment
id: 2026-11-07_vallikat-peethamber-vector-state
date: 2026-11-07
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-07 from his own headline and a search for the product. Vallikat Peethamber, managing director of VectorPeak Technology and Business Advisory Services, describes himself as an independent researcher with published work across mathematics, physics, nuclear physics, quantum theory, graph theory, string theory and neural networks. First degree connection. He argues from first principles and publishes claims, so a precise counterexample is the register he will respect; agreement would be worthless. Searches for StructuralDB and the vector benchmark returned no public repository, only generic vector-database benchmarking projects, so the reproduction he offers cannot be checked from here.
thread: his post on a vector store returning APPROVED and REJECTED for the same transaction, and the signed state tree that refuses the second write
---

# Comment on Vallikat Peethamber's vector-state post, 7 November 2026

## What the post argues

A vector store asked for the authoritative state of one transaction returns APPROVED at 0.95 similarity and
REJECTED at 0.97, because it retrieves neighbours and has no notion of authority. The agent then receives both and
synthesises a third answer that satisfies them both. That part is correct and it is the clearest short account of
retrieval-grounded hallucination I have seen.

The proposed fix is a signed state tree in which a negative state cannot be written where a positive already lives:
APPROVED is committed, REJECTED is attempted, blocked in microseconds, the LLM never sees the contradiction.

Two problems sit behind that fix, and both are in lane.

## Draft, paste as a comment

The diagnosis is right, and it is the best short account of retrieval-grounded hallucination I have read. The fix
worries me.

Refusing the negative write does not remove the contradiction, it hides one side of it, and the side it hides is
usually the correction. Approvals get reversed. A payment is authorised and voided twenty minutes later. If the
store rejects the second write, the reversal has nowhere to live except a side system, and the next reader
retrieves the approval again, with no trace that anyone tried to undo it.

A signed state tree also proves the tree was not edited. It does not prove the person who wrote APPROVED was
allowed to write it. Those are different guarantees, and only the second one survives an audit.

Recording the reversal beats refusing it.

## Why this shape

- Concedes the diagnosis in one clause, because it is genuinely good and arguing with it would waste the comment.
- The reversal case is a counterexample rather than an opinion. It is the ordinary life of a transaction, not an
  edge case, and it defeats the rule as stated without needing to see the code.
- The signature point is the second, quieter failure: integrity is not authority. That is the distinction the whole
  post is missing and it is the one an auditor would raise.
- Short closing line, so the disagreement reads as a constraint on a good idea rather than a rebuttal of it.
- No link, no numbers of mine, no mention of any test I have run.

## Posting notes, and one reservation

- He is selling this. The post is a product launch wearing an essay, and the comment engages the launch. That is
  acceptable here only because the challenge is technical and a technical audience will judge it on its merits.
- Do not raise in public that the benchmark could not be found. It is a fair private question and a cheap public
  one, and it would read as an attack rather than a critique of the design.
- If he replies that reversals are supported, the follow-up question is what a reader sees for the interval
  between the two writes, because that interval is where the contradiction does its work.
- Nothing about clients, the benchmark or the review work here.
