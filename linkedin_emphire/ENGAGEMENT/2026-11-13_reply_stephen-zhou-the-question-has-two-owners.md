---
deliverable: comment
id: 2026-11-13_reply_stephen-zhou-the-question-has-two-owners
date: 2026-11-13
audience: Stephen Z., founder and CEO at Tiybai, replying to his comment under the ORION Security post reposted by Daniel Miessler
status: ready
approved: no
warm: no
profile_checked: >-
  2026-11-13 from the comment as pasted. Stephen Z. is founder and CEO at Tiybai and wrote one day ago that DLP tools flag
  the file leaving the building without knowing why it is moving or who asked for it, so everything looks equally
  suspicious and teams start ignoring the alerts. His conclusion is that the question that matters is the boring one:
  what is this data, and does this movement make sense for this person right now. He has 11 reactions and ORION replied
  to him, so the thread is live. His profile page was not opened, so nothing in the reply refers to Tiybai, his customers
  or his history.
premise_checked: >-
  checked: the interview transcript in the post itself. The ORION speaker says anomaly detection failed because
  anomalies are how people work, that the baseline should be one data point rather than the only method, that they
  deliberately do not containerise data because copy and paste loses the container, and that the constant they track is
  the data rather than the file. The reply quotes no figure and makes no claim about ORION's customers.
sources_read: >-
  read: the ORION Security post and its full transcript, Stephen Z.'s comment, ORION's reply to him, and Rhett Glauser's
  comment. Not read: the interview on lnkd.in, which is a redirect and would need a session.
---

## Reply, paste as is

Agreed on the boring question, and I'd add that it's really two. "What is this data" is classification and lineage, and a
tool can settle it. "Does this movement make sense for this person right now" is a claim about somebody's job this week,
and the person who can settle that is whoever assigned the work, not an analyst three hops away. An alert that asks a
security team to adjudicate another department's job description doesn't get closed. It gets marked expected, and
eventually the queue is a record of what everyone agreed to stop looking at.

The baseline has the same problem from the other side. Learn normal from how people already work, and the account that
has been quietly doing this for a year becomes the most normal-looking one in the building. Which is why the line in the
interview worth underlining is the one about the baseline being a single data point, with the data itself as the
constant.

## What not to say

No "great point", no restating his sentence back at him, and no mention of anomaly detection as a technique because the
interview already disposes of it and reheating it would read as not having listened. Nothing about Tiybai, about his
customers, or about anything Timothy sells. No link, no playbook mention: this is a comment on somebody else's thread and
the first-comment rule does not apply here.

## Skips, and why

- **The ORION Security post itself.** The interview is the source, not the argument, and a top-level comment under a
  vendor post reads as an audition. The thread under Stephen's comment is where three practitioners are already
  disagreeing, which is where a reply lands as a reply.
- **ORION's own reply to Stephen** ("Exactly. But it's not a boring question"). Answering a vendor's agreement with his
  own reader adds nothing, and correcting the word "boring" would be pedantry dressed as insight.
- **Rhett Glauser, VP Marketing at ORION.** "Context is king as long as there are no shadows in the coverage" is the
  weakest claim in the thread and the easiest to press, because coverage of surfaces is a number nobody in the post
  gives. It is also the marketing line of the company whose post this is, and pressing it in their own thread reads as an
  attack on a colleague rather than a review. Held for a post of its own, where the coverage question can be asked
  without the audience reading it as a pile-on.
- **Daniel Miessler's repost.** He reposted without adding a sentence, so there is nothing of his to answer.

## Why the slot is worth it

Stephen has the audience Timothy wants: a founder selling into security teams, with 11 reactions and the post author
answering him. The reply agrees with him and then hands him the part his framing misses, which is that a verdict about a
person needs an owner who is not the analyst. That is the same argument as the review work, in the language of the
thread, and it leaves him with something to answer rather than something to like.
