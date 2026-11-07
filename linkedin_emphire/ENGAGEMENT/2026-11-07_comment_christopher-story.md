---
deliverable: comment
id: 2026-11-07_christopher-story-agent-pr
date: 2026-11-07
audience: public
status: ready
approved: no
warm: no
profile_checked: 2026-11-07 via the LinkedIn profile metadata and a ZoomInfo record, both naming linkedin.com/in/christory. Christopher Story, displays as Christopher S., Staff Software Engineer, Applied AI at Certify (CertifyOS), first degree. His own bio line reads "In another life, I might've been a monk or a bard. In this one, I build systems, refactor things." He writes literary long-form with a punchline structure, so a comment that ignores the conceit reads as a robot at a funeral.
thread: his eulogy for the software engineer, built around an agent opening a four-hundred-line pull request with a migration that would have dropped the users table
---

# Comment on Christopher Story's eulogy post, 7 November 2026

## What the record says

The post is a set piece, and the anecdote inside it is the argument: an agent opens a pull request, four
hundred lines, green checkmarks, and one migration near the bottom that would have dropped the users table
in production. A human catches it at the wake. The post's thesis is that the typing is what got measured
and the judgment is what survives.

The post does not say the thing worth adding, which is that the green check was never a verdict about
permission. That is the whole comment, and it agrees with him rather than correcting him.

## Draft, paste as a comment

The wake story is the whole problem in one scene. Four hundred lines got a green verdict, and green says
the tests passed, not that the change was allowed. The line that could drop the users table got no verdict
at all.

A reviewer's attention caught it. Attention does not scale to a thousand agents opening a thousand pull
requests. A boundary that refuses the destructive migration without an explicit grant does, provided the
refusal leaves a record you can tell apart from a pass.

The job that died was measured in keystrokes. The one replacing it gets measured in decisions that still
hold up a week later.

## Why this shape

- Four paragraphs would be one too many. Three keeps it under the length of the post's own anecdote, which
  is the polite ceiling under a piece this well written.
- The turn is "green says the tests passed, not that the change was allowed". That is the sentence the
  post is missing and it is short enough to be quoted.
- The last line answers his thesis on his own terms. He says the identity built on the keyboard is dead and
  the person staring at the system survives; the comment agrees and changes the unit of measurement.
- No hashtags in a comment, no link, no pitch, and no reference to my own work. The post is a
  performance and a comment that mentions clients under it would be a mistake.

## Posting notes

- Under a post this popular, reply to the first two responses rather than posting twice.
- If someone argues that review is the control, agree and add the throughput number: one reviewer per
  thousand automated diffs is not a control, it is a queue.
