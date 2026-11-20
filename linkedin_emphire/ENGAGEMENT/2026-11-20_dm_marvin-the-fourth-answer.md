---
deliverable: dm
id: 2026-11-20_dm_marvin-the-fourth-answer
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Marvin Percival
premise: >-
  Marvin answered the three things the test settles by saying the requirements document already covers them, and that
  the NIPOST request is in. He is right about two of the three. The third has no requirement, and it is the one he
  argued for himself, so this reply concedes the two, points at the single missing screen, and keeps the third item out
  of the requirements list where it never belonged.
time_checked: >-
  checked: 2026-11-20 03:04 WAT, read from the system clock before this file was written. That is 22:04 on Thursday in
  New York.
profile_checked: >-
  Marvin Percival, who wrote the requirements document himself and will know within seconds whether a claimed gap is
  real. The reply concedes the two items before naming the third, quotes his own argument back to him, and costs the
  build ten minutes rather than a day, which is what makes it worth raising at three in the morning.
premise_checked: >-
  checked: REQ-035 was read again before this was written, and it is scoped to matching a file against sealed items
  inside one evidence file. No requirement in v0.3 describes a checker whose file matches nothing in the register, which
  is the claim the reply makes. The three things the test settles were put to him at 02:57 and are not restated as
  agreed.
sources_read: >-
  read: ERI-REQ-v0_3.pdf as extracted in this repository, and his messages of 02:47 to 03:02. No page opened.
---

## Message, paste as is

<!-- gate:body:start -->
Fair, and mostly right. The file does cover the mechanics, which is why it was worth writing as requirements instead of a plan.

Two places it doesn't, and one of them is yours.

The fourth answer. REQ-035 tells a checker whether their file matches a sealed item inside one evidence file. Nothing in the document says what a person sees when their paper matches nothing anywhere. That's your own argument from the call, that it has to read as an ordinary answer and not as bad news, and it's the first screen of the demo rather than the last, because on day one the register is empty and every check returns it.

Second, the pace thing isn't a requirement and I put it in the wrong list. It's an operating condition, not a criterion, so it belongs in how we work and not in your numbering. My mistake.

NIPOST, fine. Waiting costs us nothing now that the sample is the path, so Monday doesn't depend on their reply.

I'll put the fourth answer into the redline as REQ-053, which is about ten minutes of work and one sentence of copy, and send it with the rest over the weekend.
<!-- gate:body:end -->
