---
deliverable: comment
id: 2026-11-09_comment_amjad-masad-error-text-is-input
date: 2026-11-09
audience: Amjad Masad post on Replit's monitoring agent
status: ready
approved: no
warm: no
profile_checked: >-
  Amjad Masad, founder of Replit, already following him. Original post, not a repost: "But who maintains vibe coded
  apps?" answering the maintenance objection with Replit's Monitoring Agent, which detects production issues, validates
  fixes and deploys them, 24/7. This is a founder defending a product he built, written to win an argument.
thread: automated production remediation
---

## The angle

Not whether the maintenance objection is fair. It is, and it is also already answered well enough by the product. The
gap is upstream of the fix: what the agent is reading. Production errors are strings written by whoever caused them, so an
agent that diagnoses from error text and then drafts a patch is consuming attacker-influenced input and shipping the
result to production. The failure does not look like a breach. It looks like a maintenance commit.

Second half, kept short: validation comes from the same loop as diagnosis, so the fix is judged against the reproduction
whoever caused the error chose to create.

## Comment, paste as is

The paragraph I'd want next is about the input. Production errors are strings written by whoever caused them: a stack trace, a malformed payload, a request naming a file that should not exist. An agent reading those and drafting a patch is taking instructions from an attacker one error at a time, and what lands looks like a maintenance commit, not an incident.

That isn't an argument against building it. It's an argument for the patch arriving as a diff a person reads before it deploys, and for the diagnosis and the validation not coming out of the same loop.

The signal that says something is broken shouldn't also be the one that says the fix is good.

## What not to say

No "vibe coding" sneer, no July database-deletion story, and no pretending the maintenance question is unanswered. He will
have heard all three and the first two turn a technical point into a pile-on. Do not ask him to disclose internals in public
either. The comment makes a claim and leaves him room to agree without conceding anything.

## Why this one is not a vendor repost

The Mamidala repost was a reseller forwarding someone else's announcement. This is the founder making his own argument,
which is the one place the point belongs. Different decision.
