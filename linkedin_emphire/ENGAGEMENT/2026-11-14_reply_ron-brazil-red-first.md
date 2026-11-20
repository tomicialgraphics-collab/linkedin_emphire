---
deliverable: comment
id: 2026-11-14_reply_ron-brazil-red-first
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 20:59 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: public
status: ready
approved: no
warm: yes
profile_checked: "Ron Brazil is first degree and commented 35 minutes ago on the live post with the strongest question in the thread: when did a check last break on purpose, before the work started. He is not asking for agreement, he is asking for a date, so the reply gives one and admits the answer is bad."
premise_checked: >-
  checked: every fact in the reply is from the post being replied to or from the work behind it: the 16-of-64
  character comparison, the forged manifest, the interrupted pair and the simulated crash between two renames,
  the six cases and thirteen checks. Nothing is claimed about Ron's work beyond what he wrote.
sources_read: >-
  read: the live post, Ron's comment, and the author's own earlier comment on it. No page was opened; the
  playbook link is in the author's comment and is not repeated here.
---

## Reply, paste this

<!-- gate:body:start -->
Ron, the honest answer is this week, and not before. That is the failure, not the fix.

I had the cheap version of your rule: a test that goes red on a bad input. It went red, so I stopped being curious. What I had never done is break the thing the check depends on, which was the comparison itself. It looked at 16 of the 64 characters, and no input I owned would ever have caught that, because every input I owned was correct.

The version I use now is one mutation per assumption rather than one per test. Truncate the digest to the length the code actually compares. Swap the file underneath the manifest. Kill the process between the two renames. Each one is aimed at a specific sentence the check makes about itself.

Where I would add to your version: a mutation has to fail for the reason you are afraid of. A fixture with a typo in it goes red and proves nothing about whether a wrong digest would. Red is not the goal, the right red is.

Which is the part of your last line I keep coming back to. You validate the method before the work. Mine got validated by a reviewer instead, and that is a much more expensive way to learn it.
<!-- gate:body:end -->
