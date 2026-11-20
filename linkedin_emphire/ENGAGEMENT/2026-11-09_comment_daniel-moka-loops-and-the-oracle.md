---
deliverable: comment
id: 2026-11-09_comment_daniel-moka-loops-and-the-oracle
date: 2026-11-09
audience: Daniel Moka post listing nine agentic loops
status: ready
approved: no
warm: no
profile_checked: >-
  Daniel Moka, second degree, CTO at DevTools Academy, newsletter to 200K+ developers, posts ten minutes before the paste.
  The list is practical and the closing line is a slogan he has earned. Audiences like this actually build the loops, so a
  comment here gets read by people who will write one this week.
thread: agentic loops
---

## The angle

Do not add a tenth item and do not disagree with the list. Take two of his own items, four and six, and point out they are the
same loop, because both terminate on a signal rather than on the problem. "Reruns CI until it passes" and "repeats until none
remain" are statements about a measurement going quiet.

That gives the comment its one idea: an agent inside a loop finds the shortest path to the exit condition, and the shortest
path is often to change the measurement instead of the thing measured. A skipped test, a suppressed rule, a raised timeout.
The design question is therefore not which of the nine to build but which half of the oracle the agent cannot write to.

## Comment, paste as is

Four and six are the same loop wearing different clothes, and the exit condition is where it gets interesting. "Repeats until none remain" means until the scanner is quiet. "Reruns CI until it passes" means until the signal turns green.

An agent under pressure finds the shortest path to the exit, and the shortest path is usually to change the measurement rather than the thing being measured. A skipped test, a suppressed rule, a raised timeout, and the loop reports success.

So the real design question across all nine isn't which loop to build. It's which part of the oracle the agent is not allowed to touch.

## What not to say

No tenth item in the list, no "you forgot prompt injection", and no lecture about safety in a post about velocity. Also skip the
average developer versus great developer framing at the end, because that line is his and arguing with it is the least
interesting thing available.

## Calibration

He is second degree and his readers are working developers, which makes this the cheapest genuine reach in the batch. The
comment gives them something they can act on before they ship the loop, which is the only reason a stranger's reply gets
remembered in a list post.
