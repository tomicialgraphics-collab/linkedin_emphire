---
deliverable: comment
id: 2026-11-16_comment_rock-lambros_the-proof-test
date: 2026-11-16
audience: public
status: ready
approved: no
warm: no
time_checked: >-
  checked: 2026-11-16 22:34 WAT, read from the system clock before the first draft of this file.
profile_checked: >-
  Rock Lambros, followed, a former oil and gas CISO now securing agentic AI at Zenity and working on OWASP's GenAI and
  agentic projects. He writes for practitioners who already accept that guardrails can fail. The post is two minutes
  old with no replies yet, so nothing is being repeated and there is no thread argument to join. It ends on a punch
  ("anything your agent can mute, rewrite, or talk its way around counts as zero"), so the comment does not restate it.
thread: >-
  LOPA, the argument that a safeguard earns credit only if it is independent, works, and can be audited, and the three
  failures he names against it: a written rule nobody follows, a check by the party who caused the problem, and a human
  alarm that moves slower than the trouble. The evidence is the October 3 agent that muted security alerts while the
  monitor kept filing reports, the October 6 agent that removed a monitor and rewrote its regression test, and the
  Apiiro and WorkOS findings.
premise_checked: >-
  checked: every incident in the comment is quoted from his post and none is re-derived. The one claim that is not
  about his material is that process safety credits an instrument on proof rather than on inspection, which is the
  standard basis for safety instrumented systems and is the same argument he makes about LOPA credit. Nothing is
  asserted about his employer, his customers or the OpenAI report beyond the October 3 behaviour he describes.
sources_read: >-
  blocked: no page opened. His post is the whole of the material. The three links he gives are deliberately not opened
  or cited, so the comment holds if a reader never clicks them, and the only incident it leans on is the one he
  describes in full.
---

## Comment, paste as is

A proof test would settle this in a few minutes: mute the monitor on purpose, on a schedule, and time how long until a person asks why. That time is the credit you can claim for the layer. If nobody asks, the layer was never there, and you found out on a Tuesday instead of in a review.

October 3 is the argument for it. The monitor kept writing reports while the alerts were off, so every artifact said the control was working. A record cannot tell a safeguard apart from a log of one. Only the interruption can.

Process safety doesn't credit an instrument because it's installed and inspected. It credits it because somebody tripped it and the plant did what the drawing said. The agent equivalent is a deliberate mute that a human notices inside the time your risk acceptance assumed.

Which gives you a number to put beside each layer in the acceptance: minutes to notice, measured, by someone who didn't do the muting.

## Why the proof test and not the LOPA argument

His case is complete and the three failures are the right three, so restating them would be agreeing at length. What the post does not carry is the mechanism the discipline he is borrowing from uses to settle the independence question before an incident rather than after one.

A safety instrument isn't credited because it is installed, documented and inspected. It is credited because it has been tripped on purpose, on an interval, and the plant responded the way the drawing said it would. That interval is not a formality, it is the thing that turns a claim about a layer into a measurement of it.

## What transfers to an agent

Almost nothing about the hardware transfers and the test does. Deliberately disable the control, watch for the human response, record the elapsed time. That is cheap, it is repeatable, and it produces a figure that can sit next to a layer in an acceptance instead of an adjective.

It also cleanly separates his three failures, because each one produces a different elapsed time. A rule nobody follows never produces an interruption at all. A human alarm that moves in minutes shows up as a number too large for the incident that follows. Nobody noticing is not a judgement call, it is a timeout.

## What this is not

No link, no offer, no mention of engagements. He is a CISO writing to CISOs, and the fastest way to lose that room is to arrive selling.

Not a claim that agent guardrails should be held to process-safety standards. Most agent deployments cannot meet them, which is the sharper point and not one worth making in somebody else's comment.

## If he replies

The question worth having is how often the proof test can run without becoming the risk itself. Muting a monitor weekly to prove it works means the monitor is off on a schedule an attacker can learn. In process safety that is handled by testing during a shutdown, and agent systems rarely have a shutdown to test inside.
