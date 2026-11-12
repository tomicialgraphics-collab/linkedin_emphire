---
deliverable: comment
id: 2026-11-10_comment_gadi-evron-milliseconds-are-a-telemetry-claim
date: 2026-11-10
audience: public, under Gadi Evron's post
status: ready
approved: no
warm: no
profile_checked: 2026-11-10 from public sources and the post itself. Gadi Evron is founder and CEO of Knostic, chairs the CSides cross-CISO community, founded the Israeli CERT, was CISO of the Israeli National Digital Authority, founded Cymmetria, and has written two books. He co-authored the 2025 warning on autonomous AI hacking with Heather Adkins, who is VP of security engineering at Google. His own line here is "Industry, please hear us", and the ask is to share the post or disclose your own incident, with an IoC as the entry ticket to the trust group he is forming.
thread: autonomous attacks at scale, and what a defender can prove afterwards
premise_checked: checked: the in-the-wild use of ARTEX and CAIRN in agentic attack frameworks, against Google Threat Intelligence Group and Mandiant reporting from 30 October 2026 plus vendor corroboration from Kaspersky, Microsoft, CrowdStrike, Wiz and AhnLab, 2026-11-10. The millisecond coordination claim is not independently checkable from outside, so the comment does not confirm or dispute it and instead names what would have to be true to verify it.
sources_read: read: the GTIG and Mandiant findings on ARTEX, PentAGI and CAIRN as summarised in two independent write-ups, and the GitGuardian
  survey of 45 agentic pentest frameworks, 2026-11-10. No paper behind the millisecond claim was found, and none is asserted.
---

## Comment, paste as is

Believed, and the part that makes it land is that it is no longer only your word for it. The reporting on ARTEX and CAIRN describes agents doing reconnaissance, movement and collection in real engagements, and thousands of forks later the capability did not leave the field when the repository did.

The thing I would add to the CISO list, because it decides whether any of this can be proved afterwards: coordination at millisecond scale is a claim about your telemetry before it is a claim about an attacker. Without synchronised clocks across sites and sub-second retention, a coordinated intrusion looks like three unrelated incidents, and you cannot refute the picture you are being shown either.

So the budget line that follows from this is correlation rather than AI security. One clock, one joined timeline, retention long enough to reach across sites.

On disclosing incidents, most of us cannot, and it is not cowardice. The substitute that carries the same information is a de-identified timeline with the site names removed, which is shareable without a legal review. An IoC proves you were touched. A timeline proves you can see, and it is the harder thing to fake.

Nobody in the room is disbelieving you. The gap has moved to instrumentation.

## Why it lands

He asks to be believed, and belief is the one thing a comment cannot add. What it can add is the next question after belief: whether a defender has the clock resolution to see what he describes, which is also the difference between an incident report that survives scrutiny and one that does not.

No links, no hashtags, no mention of red teaming work or the challenge coin he called an IoC. He is asking for disclosure and the comment answers that ask with something a security team can actually do this week.
