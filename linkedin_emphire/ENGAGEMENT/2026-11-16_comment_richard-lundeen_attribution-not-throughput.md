---
deliverable: comment
id: 2026-11-16_comment_richard-lundeen_attribution-not-throughput
date: 2026-11-16
audience: public
status: ready
approved: no
warm: no
time_checked: >-
  checked: 2026-11-16 08:24 WAT, read from the system clock before this file was written.
profile_checked: >-
  Richard Lundeen, second degree, describes himself as a software security geek and posts about AI red teaming at
  Microsoft. The post is a hiring notice for a Senior Security Software Engineer on AIRT, framed around GPU
  infrastructure for running and evaluating models at scale, with a careers link and the line open anywhere in US.
  Nothing about him is claimed beyond the post, and the comment does not ask about the role.
thread: >-
  AI red teaming automation needs GPU capacity to run and evaluate models at scale, and they are hiring a senior
  engineer for that infrastructure. No argument in the post, so there is nothing to agree with and nothing to correct.
premise_checked: >-
  checked: the post states no facts to verify beyond the role itself. The one figure in the comment, a verifier that
  compared 16 of 64 hash characters and passed fifty checks, is the author's own audit and was published on the
  profile. The claim that the role is US-only is the post's own line, quoted as open anywhere in US, and is not used
  in the comment.
sources_read: >-
  blocked: no page was opened. The careers link was not followed and nothing is asserted about the role's
  requirements, its team or its process. The comment is written so that it does not depend on any of them.
---

## Comment, paste as is

The constraint that gets harder as this scales is attribution, not throughput.

Once you can run thousands of evaluations a day, the cost moves to knowing which of them count as evidence: the revision of the model that was actually hit, the check that produced the verdict, and whether that check can fail at all. I audited a verifier that compared 16 of 64 hash characters and passed fifty checks. At one run a day that's a wasted afternoon. At a thousand a day it's a factory producing confident answers to questions nobody asked.

GPU capacity is what makes the volume possible. What makes the volume worth having is a verdict per run that a second person can re-derive without your cluster.

That part doesn't parallelise with more cards, which is why the hire matters more than the hardware.

## Why comment at all on a job post

Because the role is not something the owner can take. The post says open anywhere in US, the owner is in Lagos, and no comment changes that. Pretending otherwise in public would be the worst possible reply under a Microsoft hiring notice.

What the comment does is put one technically specific idea in front of the group that runs this function at Microsoft. A hiring post from that team gets read by the people on it. The comment gives them something to recognise: the observation that red teaming at scale is an evidence problem before it is a compute problem, stated with a defect that proves it.

It also does not read as an application, because it never mentions the role, the owner's location or availability. That is deliberate. A comment that says I would love to apply under a US-only advert costs credibility with everyone who reads it.

## What it does not do

No link, no offer, no mention of prices or packages. This is not a buyer.

No congratulations. Congratulating a hiring post adds a line to a queue of them.

No claim about Microsoft's process or about what AIRT does internally, because neither is in the post and the careers page was not opened.

## If he replies

The useful reply is about rerunability, not about the role. If he asks what the verdict per run looks like, that is the one page from the 15 November pack and it can be sent as a specimen. If he asks whether the owner is applying, the answer is no, and the reason is the requirement in his own post.

## The other path, if the owner wants it

A direct message to him is the only route worth anything here, and only if it is a question about how AIRT records findings rather than a request for a job. Do not send both. The comment has to land first, or the message reads as a follow-up to nothing.
