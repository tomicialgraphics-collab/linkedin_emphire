---
deliverable: doc
id: 2026-11-14_about-rewrite
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 22:34 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: internal
status: ready
approved: no
---

# About: the rewrite

The live About opens with a biography, spends its second paragraph on an abstraction, and buries the offer under the fold. Only the first two lines are read by most visitors, and those two lines currently say where he came from rather than what he does.

## What is wrong with the live version

**It opens with the wrong door.** "I trained as a Medical Laboratory Scientist" is a good story and a bad first sentence, because a buyer gives the About four seconds and stops at the first line they cannot use.

**The second paragraph argues with nobody.** "Nothing goes wrong until someone trusts it" is true of almost every system and therefore says nothing about AI.

**The proof is in the third paragraph and the link goes to the weaker artifact.** The five-test repository has zero stars; the Playbook carries 168 testable classes and the tooling. The public link should point at the stronger one.

**There is a comma splice in the sentence that matters most,** and a stray comma list in the paragraph about range.

## Paste this, 1,184 characters

<!-- gate:body:start -->
I find the failure in AI systems that a passing test suite says can't happen.

Most AI products pass their own evaluations because nothing inside them can fail. A check that can't return a different answer is decoration, and a green dashboard isn't evidence that anybody looked.

In November I found my own verifier comparing 16 of 64 hash characters and passing every run. I rebuilt it so it fails when it should, then published the failure-path tests that keep the hole closed.

Before this I spent a decade building across the stack, web apps, computer vision, e-commerce and automation, and before that I trained as a medical laboratory scientist, where a result nobody can reproduce gets thrown away rather than filed.

Today that's AI red teaming plus the evals behind it: I attack agents before they're given keys, and I build the check that tells you the eval was real. The public version is 168 testable classes with the tooling to turn a run into a coverage argument someone else can audit, and it lives at github.com/Teamthy/Ai-Red-Team-Playbook.

If you're shipping AI and want a second pair of eyes on the checks, message me. I read them.
<!-- gate:body:end -->

## Why the order

Line one is a claim a buyer can disagree with, which is what makes them read line two. Line two names the defect they half suspect in their own evals. Paragraph three is evidence with a number, because the number is what separates this from every other profile claiming rigour. Paragraph four buys range and the laboratory, in that order, because the decade is the credential and the lab is the character. Paragraph five is the offer with the link attached to the artifact that carries weight.

The email address is gone from this draft. It duplicates Contact info, it is a scraping target, and Open Profile already lets anyone message him for free.

## Two things to change in the same sitting

**Top skills.** Still Software Systems Engineering, Artificial Intelligence, Go, Next.js, Red Teaming. Pin AI Evaluation, AI red teaming, LLM security, Threat modeling, Go, in that order. Next.js is holding a search slot in a market that does not hire for it.

**The link in the old About** points at the five-test repository. If that repository stays linked anywhere, link the Playbook instead, because a reader who clicks through is looking for the body of work and not the evidence of one week.

## The five-second test

Read only the first sentence aloud. If a security lead cannot tell what is being sold from it, the fold is still wrong, whatever follows.
