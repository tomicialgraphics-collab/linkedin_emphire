---
deliverable: comment
id: 2026-11-09_comment_hitesh-choudhary-cleanup-prompt
date: 2026-11-09
audience: Hitesh Choudhary post on the codebase cleanup prompt
status: ready
approved: no
warm: no
profile_checked: >-
  Hitesh Choudhary, developer educator, two YouTube channels at 1M and 700k, ex founder and CTO, posts five minutes before the
  paste. He shares a prompt attributed to Alex Albert at Anthropic, gives three steps to try it, adds a caveat about "no longer
  needed" removing things that matter, and ends by asking whether readers would run it on a work repo. He has already found the
  weak spot, so the comment sharpens it rather than announcing it.
thread: agentic codebase cleanup
---

## The angle

He named the right risk and stopped one step short of the reason. The prompt's safety valve is "fix what you're sure
about", and confidence is not calibration. An agent's certainty is a property of its output, not evidence about the edit.

The second half: "no longer needed" is the only item on that list which no test can defend. A green suite covers the
behaviour somebody thought to exercise. It is silent on the contract, the migration, the dark flag, the rare branch.

He asked a direct question at the end, so answer it. Yes on a work repo, with deletion separated and never auto-merged, and say
what that looks like.

## Comment, paste as is

"Fix what you're sure about" is the hinge, and it's the one clause I'd change. Confidence isn't calibration. The edits that cost you are the ones the agent was sure about and wrong, and the prompt gives you no way to tell those from the safe ones.

The second risk is "no longer needed", the only item on that list no test can defend. A green suite covers the behaviour somebody thought to exercise. It says nothing about the endpoint a customer contract depends on, the migration nobody has run, or the flag that's been off for a year and is about to be switched on.

So yes on the work repo, with one change. Deletions go on their own branch and never auto-merge. Renaming and dead imports, sure. Deleting is a judgement about the future, not a cleanup.

## What not to say

No Hindi, no riffs on the safai joke, and no disagreement with the prompt being useful, because it is. No model or vendor
comparison either. He is a teacher with a very large audience and his caveat was correct, so the comment extends him rather
than correcting him.

## Why the slot is worth it

Millions of developers see this post, many of them will run the prompt tonight, and the comment answers the question he asked
with a policy instead of an opinion. That is the kind of reply that gets pinned by the author or quoted in a follow up.
