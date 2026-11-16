---
deliverable: comment
id: 2026-11-16_comment_daniel-miessler_the-probe-points-outside
date: 2026-11-16
audience: public
status: ready
approved: no
warm: no
time_checked: >-
  checked: 2026-11-16 22:11 WAT, read from the system clock before this file was written.
profile_checked: >-
  Daniel Miessler, followed, writes to a large security and AI audience and sells an operating system for companies
  (LifeOS, Vector). The post is seven minutes old and carries no comments yet, so there is no thread to avoid
  repeating and no other commenter to answer. The account already commented on a different post of his earlier today,
  on organisational friction, and this says nothing that one said.
thread: >-
  he has replaced CLAUDE.md and AGENTS.md with a doctrine: a constitution, preferences, TELOS, and an Ideal State
  Artifact whose criteria each name the probe that would prove them false. Assay maps every criterion to an eval,
  nothing is handed over on a self-review, and a rejection means the missing check gets named and added rather than
  the prompt getting another paragraph.
premise_checked: >-
  checked: the comment asserts one thing about his system, that a receipt lists the checks that passed, and quotes it
  from his own text. It makes no claim about his customers, his results or his numbers. The instance is from the
  owner's own audit work and is stated as such, with the count that was measured. Nothing about the client is named.
sources_read: >-
  blocked: no page opened. The post text is the whole of the material. No link, article or prior comment of his is
  relied on, and the account's own figures come from the benchmark work this repo already records.
---

## Comment, paste as is

Naming the probe that would prove a criterion false is the strongest line here, because it forces the criterion to point at something outside the system's own account of itself. That's where receipts go soft.

A check that a failed write returns the right reply passes. It reads the reply. In a suite I work with, the reply said the disk was unchanged, which was true of the write, and recovery had already cut forty-four bytes off the journal two steps before it. Everything passed and the file had shrunk.

The repair wasn't a better reply. It was moving the probe off the reply and onto the bytes.

That makes the ERRATA line worth counting rather than admiring. Every miss you reject that passed adds a check that exists because you found the bug, not because the system did. That share tells you whether Assay is reviewing the work or keeping a record of your reviews. Mine is embarrassing, which is why I want it on a chart rather than in a sentence.

## Why the probe and not the doctrine

The post is a description of a system, and describing it back to him adds nothing. The one place the description has an edge is the sentence about criteria naming their own falsifier, because that is the part most people will copy without noticing what it demands: the probe has to read something the system does not author.

A receipt is testimony. It says what was checked, in the checked system's own vocabulary. It cannot say what nobody wrote a check for, and the defects that survive a good suite are almost always of that kind. So the strongest reading of his own line is also a critique of it, which is the only useful thing to send to somebody who has just published his architecture.

## The instance

The benchmark work this repo carries, in `CLIENTS/hfb`, is the source. A store refuses a write it cannot make durable and answers that the disk is unchanged. The suite asserted the reply, and the reply was correct. Recovery, running before the append, had quarantined a torn record and the journal had gone from 341 bytes to 297. Both facts were true at once: the write did not change the file, and the file had changed.

Recording that as a documented limit, and pinning both halves as mode f25, is what the probe moved to. The number forty-four is in the comment because it was measured, not because it reads well.

## What this is not

No link, no offer, no mention of engagements or of the client by name. He is selling a framework to companies and a comment that advertises closes the door he opened.

Not a claim that his doctrine is wrong. It is the clearest statement of this idea the account has read, and the comment says so by taking the hardest sentence in it seriously rather than by praising the rest.

## If he replies

The question worth having is what his suite would look like if he counted checks by origin: found by the system, or found by him after the system passed it. If the second number dominates, ERRATA is not an improvement loop, it is his attention doing the reviewing with extra steps, and the fix is generative rather than additive. A criterion that names its own falsifier is cheap to write and hard to write well, and the ones that read best usually point at the reply rather than at the world.
