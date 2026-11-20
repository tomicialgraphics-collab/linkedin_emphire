---
deliverable: comment
id: 2026-11-13_comment_rowan-cheung-three-runs-teach-judgement
date: 2026-11-13
audience: Rowan Cheung, comment on his post about doing a task manually three times before automating it
status: ready
approved: no
warm: no
thread: what manual repetition teaches, and what it cannot
profile_checked: >-
  2026-11-13 from the post as pasted. Rowan Cheung runs a very large AI newsletter and writes workflow posts for people
  building with AI rather than for engineers. His rule is that he does a task by hand at least three times before he
  automates it, because that is how he learns what good looks like, which steps matter and where it goes wrong. The post
  is aimed at beginners who go looking for tools before they have a problem, and his closing instruction is to run the
  task on Monday, Wednesday and Friday. That framing is what the comment has to answer.
premise_checked: >-
  opinion: the point about frequency is structural rather than measured. Three manual passes rarely hit the same
  exception twice, which is why the failure rate that shows up in production cannot be learned from them. Nothing here
  asserts a number, and nothing disputes his rule.
sources_read: >-
  none: the post was pasted in full. The newsletter link in it is a LinkedIn safety redirect and was not followed.
---

## Comment, paste as is

Three runs teach judgement, and they cannot teach frequency. Doing the work by hand shows you what good looks like and
leaves you with no idea how often an agent gets it wrong, because three passes rarely hit the same exception twice.
That one in two hundred case is what automation runs into, and it arrives after you have stopped watching.

So I would take one more thing out of those runs than the habit. Every time something odd happens on the Monday, the
Wednesday or the Friday, save the input and the output you decided was right. Three runs will not give you many, but
the first ten of those become a test set, and a test set is what turns I know good work when I see it into something an
agent can be held to on a Tuesday when nobody is looking.

Steps are the cheap half of what manual work gives you. The exceptions are the part that survives automation.

## What not to say

No restating the rule back to him, no argument with it, and no mention of the factory inspection story as if it needed
improving. No link, no newsletter, no hashtag, and nothing that turns a workflow post into a pitch. The test set idea
has to arrive as the next step from what he already does, not as a correction of it.

## Why the slot is worth it

His posts reach people who are about to automate something for the first time, which is exactly the moment when a
missing test set costs the most. A short comment that adds the one artifact worth keeping is more useful under this post
than agreement, and it is the kind of thing readers save.
