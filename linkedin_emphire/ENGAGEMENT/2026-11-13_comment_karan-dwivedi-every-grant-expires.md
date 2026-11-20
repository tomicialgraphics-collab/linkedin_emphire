---
deliverable: comment
id: 2026-11-13_comment_karan-dwivedi-every-grant-expires
date: 2026-11-13
audience: Karan Dwivedi, comment on his post about access management being the highest leverage work
status: ready
approved: no
warm: yes
profile_checked: >-
  2026-11-13 from the post as pasted. Karan Dwivedi is a security engineering leader at Google who trains cybersecurity
  professionals. This post argues that access reviews and offboarding are unglamorous and load bearing, lists the three
  familiar cases of stale access, and closes by asking which single access process a reader would fix with a magic wand.
  He has been commented under before, on 12 November, about agent accountability, so this answer has to be a different
  mechanism rather than a variation on intent records.
premise_checked: >-
  opinion: the argument for expiry over periodic review, and the claim that service identities are the part of the estate
  that never offboards, come from review work rather than a study. Nothing is asserted about his organisation, and no
  figure is given for how often stale access causes incidents, since the one in his post is not quantified either.
sources_read: >-
  none: the post was pasted in full with no link attached.
---

## Comment, paste as is

Every grant carries an owner and an expiry, and nothing survives the date unless somebody other than the requester renews
it. A quarterly review asks whether this still looks right, which nobody can answer for an account they did not create,
so the answer is usually yes and the review becomes a rubber stamp with a meeting attached. Expiry asks nothing and hands
you a list of grants that stopped being wanted, which is the list the review was supposed to produce.

I would spend the wand there rather than on offboarding, because offboarding only works on people. A service account made
for a migration outlives the team that made it, and so does the agent identity now holding its credentials. Nobody leaves,
so nothing triggers a review, and the account is still there three migrations later with permissions inherited from the
first one.

The test I would run first: pick ten service accounts, and try to name the person who would notice if each one were
switched off without warning. The ones with no name are the ones the wand is for.

## What not to say

No restatement of his three examples, no statistics about stale access, and no agreement that IAM is underrated, which is
his point and does not need a second voice. Nothing about the earlier comment on his accountability post, no link, no
hashtag, and nothing about his courses.

## Why the slot is worth it

He asked a direct question with a wand in it, which means the thread will fill with one-line wishes like MFA everywhere.
An answer that names a mechanism, says why it beats the process everyone already has, and ends with a test that fits in an
afternoon is the one that gets read by the people who own the estate.
