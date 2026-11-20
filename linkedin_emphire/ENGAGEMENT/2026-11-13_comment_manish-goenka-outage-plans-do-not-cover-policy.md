---
deliverable: comment
id: 2026-11-13_comment_manish-goenka-outage-plans-do-not-cover-policy
date: 2026-11-13
audience: Manish Goenka, comment on his post about cloud concentration and the Microsoft outage
status: ready
approved: no
warm: no
thread: resilience plans written for failure, and the risk that arrives as policy
profile_checked: >-
  2026-11-13 from the post as pasted. Manish Goenka is a board member and strategy adviser writing for boards on emerging
  markets and technology. His post covers the Microsoft 365 outage, the October 2026 Google Cloud disruption at UK banks,
  the October 2025 AWS outage, the Synergy figure that three US providers hold about 61% of cloud infrastructure, and the
  June 2026 case where US export restrictions led Anthropic to disable model access worldwide before it was restored. He
  closes by asking boards whether their recovery plans have been tested. He is a generalist board audience, not an
  engineer, so the comment stays at the level of what a plan can and cannot restore.
premise_checked: >-
  opinion: on a fact he supplies, the June 2026 withdrawal is taken from his post and was not independently verified here,
  so the comment refers to it as the case he describes rather than asserting the details. The rest is structural: a
  recovery plan is triggered by a failure signal, and a policy withdrawal produces none, which is why it does not invoke
  the plan at all.
sources_read: >-
  none: the post was pasted in full with no article attached. The Synergy Research figure it quotes was not checked
  against the source and is not repeated in the comment.
---

## Comment, paste as is

The recovery plan most organisations hold answers an outage, and the June case you describe was not one. No status page went red, nothing timed out, no failover fired, and the capability was withdrawn while every dashboard stayed green. A plan that starts from a failure signal does not start at all when the provider is technically healthy and simply not permitted to serve you.

That is why the second cloud does not reach it. Another region restarts your servers. It does not recreate the behaviour of a model your workflows were adjusted around, and the runner up was almost certainly never run against your own cases, so nobody can say what it does differently on the inputs that decide something.

The question I would put to a board is narrower than readiness. Name one workflow whose output nobody in the company can produce without a vendor's model, and then say who owns the consequence when that model is withdrawn on a Thursday. If the answer is the platform team, the risk has been handed to people who cannot carry it.

## What not to say

No agreement paragraph about concentration, which is his argument and is well made. No repetition of the 61% figure or the outage dates back at him. No mention of vendors to switch to, since that is a purchase recommendation he did not ask for and could not verify from a comment. No link, no hashtag, no offer to review anyone's resilience plan.

## Why the slot is worth it

He is writing to boards, and the distinction between a plan that waits for a failure signal and a risk that arrives as a lawful instruction is the one that makes a resilience budget look inadequate. It is also the argument I can make from what I test, which is whether anything still works when a capability quietly changes shape.
