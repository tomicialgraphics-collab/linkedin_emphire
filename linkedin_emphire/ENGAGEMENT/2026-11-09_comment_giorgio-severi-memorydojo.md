---
deliverable: comment
id: 2026-11-09_comment_giorgio-severi-memorydojo
date: 2026-11-09
audience: public comment on Giorgio Severi's MemoryDojo post
status: ready
approved: no
warm: no
profile_checked: >-
  Giorgio Severi, AI safety and security researcher at Microsoft, second-degree connection, posting the arXiv release of
  MemoryDojo with his co-authors named. Read from the post and the paper summary inside it; nothing about his role is
  asserted beyond the headline he publishes under.
thread: memory poisoning, and the three rates a single attack-success number hides
---

## What the post is

A benchmark paper: 155 multi-session trajectories, four domains, five memory systems, following a poisoned instruction from storage through retrieval into later behaviour. Their own summary of the findings is unusually precise, including the two that matter for an evaluator: storing does not mean retrieving, retrieving does not mean following, and the original malicious text can be gone from the context while its effect persists.

## Why comment now, after skipping it in the batch

The skip reason was that the available comment deserved a post. That is half right. There are two comments here and only one of them is a comment.

The narrow one is about the metric, it is useful to the authors today, and it reaches their audience while the paper is news. The wide one, about what is left to review after the poison propagates into entries the agent wrote itself, is a post, and spending it here would burn it on a reply. So the comment takes the metric and the post keeps the audit trail.

## Comment, paste as is

The three-step chain in your findings is where the metric should sit. Stored, retrieved and followed are three different failures, and one attack success rate collapses them into a number that hides which stage did the work.

Split three ways, the numbers also locate the cheapest control. Poison that rarely survives retrieval is an index problem. Poison that is retrieved but rarely changes behaviour is a problem in whatever turns retrieved text into instructions, which is a different fix in a different place.

Your last bullet is the one I would protect from being read as reassurance. A long benign history reduces the effect, so it looks like hygiene works, and a control that reduces rather than eliminates is the one people stop running.

## What not to say

No summary of the paper back to its authors, no congratulation as the opening, and no claim about which of the five memory systems was worst without the per-system denominators. Do not spend the audit-trail argument here.

## Held for the post

Once the poison propagates into entries the agent wrote itself, nothing in the transcript distinguishes something it learned from something it was told. That makes post-incident review a question about whether the memory store is versioned, not about what the model said. It also means deletion of the source entry is not remediation, because the effect has already been copied into records that look like the agent's own work.
