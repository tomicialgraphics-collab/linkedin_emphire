---
deliverable: comment
id: 2026-11-08_mitko-vasilev-forward-deployed-handover
date: 2026-11-08
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-08 from his profile and public activity. Mitko Vasilev, chief technology officer, an advocate of local and on-device models running open source without cloud dependency, with a consistent line that organisations should own their AI rather than rent alignment from whoever owns the model. He has also built local gating tooling for package supply chains. Second degree.
thread: his post arguing that AI has eaten the outsourcing layer and that the harder problem is teaching ten thousand employees to use it, naming forward deployment engineers as the role being reborn, giving the window twelve to twenty four months, and closing on owning your AI rather than renting it
verified: nothing external is claimed. The twelve to twenty four month window and the role categories are his and are not restated as mine. The comment's argument is about handover and measurement rather than about the market forecast, which is his to make.
---

# Comment on Mitko Vasilev's forward deployment post, 8 November 2026

## Why this angle

He has made the market argument and does not need another version of it. The part his framing leaves out is the one that
decides whether the model works at all: embedded engineers create dependency by design, so the deliverable has to be what
remains when they leave.

That ties to his closing line about ownership, which is the strongest thing in the post. Owning weights is not the same as
owning the ability to tell whether they are working, and the second one is the part a forward deployed engineer can hand
over or keep hostage. This is also short enough not to read as a lecture at a CTO.

## Comment

The twelve to twenty four month window is the right read, and it hides the thing that decides whether the model works: what
is left when the engineer leaves.

Embedded work creates dependency by design, so the handover is the deliverable, not the pipeline they built. That means the
internal team has to be able to run the thing and, more to the point, tell whether it is working. If only the deployed
engineer can judge output quality, the capability was rented, whatever the contract says.

Which is why I would put one line in the engagement: an eval suite the client owns and can run without you. Weights you
cannot measure are rented capability with extra steps.

## What not to say

No argument about the window, which is his forecast and a reasonable one. No defence of outsourcing, which is not the point
of his post. No mention of my own work and no link, since he has a newsletter and a following and does not need traffic
advice from a comment thread.

## Held for a later turn

If he replies, the interesting question is what he thinks a forward deployed engineer should leave behind besides code:
the eval suite, the runbook, or the decision log of what they tried and rejected. He builds tools rather than advisory
engagements, so his answer would be more concrete than most.
