---
deliverable: comment
id: 2026-11-16_comment_eduardo-vedes_the-column-that-is-missing
date: 2026-11-16
audience: public
status: ready
approved: no
warm: yes
time_checked: >-
  checked: 2026-11-16 10:09 WAT, read from the system clock before this file was written.
profile_checked: >-
  Eduardo Vedes, first degree, a software engineer and AI consultant working on architecture, AI integration and team
  training. The post is six minutes old at the time of the paste and is a practical method rather than an argument, so
  the comment adds one field to the record instead of debating the method.
thread: >-
  a lightweight record for judging whether AI improves a workflow: task and acceptance checks, complexity and
  familiarity, tool and model, active implementation, review and correction time, elapsed time to merge, tool cost and
  defects found. His own caveats are that active work and elapsed time must stay separate, that tasks must be compared
  at similar scope, and that a handful of tasks guides a local decision without establishing a general claim.
premise_checked: >-
  checked: the comment adds one field and argues for it. No figure is quoted, nothing is claimed about his results, and
  the method is not corrected. The claim that a defect count is uninterpretable without knowing what the review could
  catch is an argument, stated as one, and does not dispute any of his nine fields.
sources_read: >-
  blocked: no page was opened. The post carries no link that matters here and nothing in the comment depends on the
  earlier entries in his series that he refers to in his closing paragraph.
---

## Comment, paste as is

The record is good, and there's one column missing that changes what the rest of it means.

Defects found only means something next to what the review could have caught. Two tasks can both report one defect: in the first, somebody read the whole diff and the code was clean. In the second, somebody skimmed nine hundred lines and got lucky. The count reads the same and the workflow decision that follows it points the opposite way.

So I'd add a line for the check that was actually standing, and whether it could fail. On my own work the signal that changed behaviour wasn't defects per hour. It was how often the review found something a machine could have found first, which says more about the setup than about the person.

What I'd keep exactly as you wrote it is the caveat: a handful of tasks guides a local decision and doesn't establish a general claim. Most posts of this kind leave that sentence out and publish the ratio anyway.

One task tracked through correction is enough to change one thing. That's the method, and it doesn't need a sample size.

## Why this field and not another

His nine fields already separate activity from elapsed time, which is the distinction most productivity posts miss, and they ask for defects found after merge, which is rarer still. The gap is that a defect count is a numerator with no denominator.

Adding the check that was standing turns the record from a diary into a measurement. It also does something useful to the reader: a team that writes down what its review can catch, and gets an honest answer, discovers that most of its review is a read-through by somebody who is also doing three other things.

## What this is not

No pitch, no link, and no offer. He is a consultant who teaches this material, so the comment competes only by being more specific than the post, and it does that with one field.

Not an argument that the method is wrong. His caveats are better than the post's headline, and the comment says so.

## If he replies

The follow-up worth having is what he would count as a check that can fail, because most teams answer with tests, then discover the tests pass on code that does the wrong thing. That is his subject and the answer would be useful to him.
