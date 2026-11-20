---
deliverable: comment
id: 2026-11-16_comment_daniel-miessler_friction-needs-an-instrument
date: 2026-11-16
audience: public
status: ready
approved: no
warm: no
time_checked: >-
  checked: 2026-11-16 21:43 WAT, read from the system clock before this file was written.
profile_checked: >-
  Daniel Miessler, followed, building an operating system for companies and writing for a large security audience. The
  post is twenty hours old and already carries a thread with substance in it: patching assumes an inventory, the
  inventory problem is twenty years old, the anti-patch line is contested, and one commenter has already extended the
  friction idea to stopping rather than fixing. The comment adds the missing instrument and does not repeat any of that.
thread: >-
  why just patch is bad advice for a large company: the limit is organisational friction rather than technology, the
  asset and code-to-owner maps have never been built because the company is not set up to maintain them, and the fix is
  an AI-native organisation with a lower friction coefficient.
premise_checked: >-
  checked: no figure is quoted and nothing is asserted about his company, his audience or the organisations he
  describes. The instrument proposed is a method, not a result, so there is nothing in it to verify beyond its own
  arithmetic. The claim that most large organisations lose this at permission rather than skill is stated as what the
  measurement tends to show, and is the author's judgement from audit work rather than a statistic.
sources_read: >-
  blocked: no page was opened. The post and the visible comments are the whole of the material, and the comment is
  written so that it does not depend on the article or on anything the other commenters linked.
---

## Comment, paste as is

The friction coefficient is the right name, and it has one problem: nothing measures it, so every conversation about lowering it turns into an argument about the org chart.

There's a cheap instrument. Take what the team already knows it should have done, the host to map, the patch to apply, the credential to rotate, and put three fields under each: what would prove it's done, who owns the window in which it can be done, and how many days it's been known and undone.

That gives you a number, a name and a test. The number is days known-and-undone. The name is the person who owns the window rather than the person who wants it. The test is the artifact that would close it. Friction stops being a property of a company and becomes a queue with a top.

It also settles the just-patch argument without either side winning. Patching is the basics. What the record shows is whether the basics fail on skill or on permission, and in the large organisations I've seen it's the second.

Which is his point, with an instrument attached. A friction coefficient you can't measure is an org theory. Three fields and a date make it a finding.

## Why this and not the friction argument

Four commenters have already made the strong points: the inventory assumption, the twenty-year age of the map problem, the owner who disappears at the team boundary, and the fact that friction slows stopping as much as fixing. Restating any of them adds a line to a thread that has enough.

What none of them has is the thing that makes the framing usable inside a company: the coefficient cannot be argued down because nobody can put a figure on it. Give it three fields and a median and it becomes a number a chief information security officer can be held to, which is the only form in which an org argument gets settled.

## Where the three fields come from

They are the smallest version of the method this account uses on systems: what would count as proof, who is allowed to act, and how long the gap has stood. Applied to a queue rather than to a control, it produces the one number that separates a skills problem from a permission problem.

That distinction is the whole disagreement in the thread. Patching is a basic skill and it is also, in most large organisations, a permission the security team does not hold. Both can be true, and only a record can say which one is binding.

## What this is not

No link, no offer, no mention of engagements. He writes to a very large audience and sells an operating philosophy, not a service, so a comment that advertises is read as noise by everyone including him.

Not a claim that measurement replaces the reorg. The instrument tells you where the friction is; it does not remove it. If anything it makes the reorg harder to avoid, because it names the owners.

## If he replies

The question worth having is what he would count as the unit of friction, because days is his unit only if the queue is short. A queue with a thousand items and one owner reads as low friction and infinite delay, and the ratio between them is the number that actually moves.
