---
deliverable: comment
id: 2026-11-14_reply_ron-brazil-harmless-mutation
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 21:46 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: public
status: ready
approved: no
warm: yes
profile_checked: "Ron Brazil replied 13 minutes ago on the live post, sharpened the rule about a mutation failing alone, added the case of a check that could not look at all, and asked one direct question: what happens to a mutation that survives because it is genuinely harmless. He is asking for a practice, not agreement."
premise_checked: >-
  checked: the answer describes mutations used in the work behind the post and the examination thread, including
  the comment-only change appended to the store module that the hash guard refused. Nothing is attributed to
  Ron beyond what he wrote, and no claim is made about his system.
sources_read: >-
  read: his reply and the post it sits under. No page was opened and no link is in the reply.
---

## Reply, paste this

<!-- gate:body:start -->
Red alone isn't enough. The red has to land on the assertion you meant: a mutation that fails with a traceback rather than a failed comparison tells you something is broken, not that your check works.

On the survivor, I've stopped using two buckets because there are three.

Equivalent is the rare one. The mutant changes nothing observable, you say in a sentence why, and it retires with that sentence attached. Keeping it matters, because a list holding only kills is a sales document.

Blind spot is the common one. Behaviour changed, nothing went red. Naming it, with the input that didn't notice, is the most useful line in the file.

The third one answers your question. Some mutations are harmless to behaviour and fatal to something else, and those aren't survivors, they're aimed at a different check. I appended one comment line to the store module. No test could see it, and it proved the hash guard refuses anything it wasn't built to expect.

Holding it together: harmless is a claim by whoever wrote the mutant, which makes it self-assessment. It needs a reason somebody else can check, and until then it counts as a blind spot.

Which gives the number worth reporting. Not how many died, but how many are unclassified.
<!-- gate:body:end -->
