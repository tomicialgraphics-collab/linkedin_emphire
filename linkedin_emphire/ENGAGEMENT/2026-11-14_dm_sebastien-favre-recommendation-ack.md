---
deliverable: dm
id: 2026-11-14_dm_sebastien-favre-recommendation-ack
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:47 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: vendor
status: ready
approved: no
warm: yes
profile_checked: >-
  Sébastien Favre published a recommendation on 14 November describing the review, the disagreement and
  the release work, and it is visible on his profile rather than sent privately. He wrote it before
  hearing whether the pull request wording is approved, which makes the reply a statement about accuracy
  rather than a thank you note. He is precise in public: the recommendation names the exit codes, the
  strict-mode propagation and the unmeasured expectations, so a reply that only says thank you would
  leave the one attribution error standing in front of his network.
premise_checked: >-
  checked: the recommendation's account of the review matches the thread. The disagreement was about
  exit codes, and the distinction Timothy argued for was between an incomplete verification and a failed
  one. The recheck was at 1.3.0, with 172 digests conforming, 121 fixtures reproduced byte for byte and
  eleven checks green, all of which Timothy reported at 06:43 on 14 November. One sentence needs a
  correction and it is not a small one: the strict-mode value that no run had measured came out of
  Sébastien's own release notes, so crediting Timothy with uncovering it gives him work that was not his,
  and the reply says so plainly.
sources_read: >-
  read: the recommendation text as pasted on 14 November, and Timothy's message of 06:43 the same day,
  which is the only primary account of the recheck. Nothing else is relied on. No repository was opened.
---

## DM, paste this

<!-- gate:body:start -->
That's a generous recommendation, and it's mostly accurate, which is rarer. Two things before it settles.

The correction first, because I'd rather say it now than have it sit on your profile. The strict-mode value that no run had ever measured came out of your own release notes. I read them, noticed the gap and propagated the flag, which is ordinary reviewing. Uncovering it was your work, done in public, before I got there. If you ever revise the recommendation, that sentence should say I found it in your notes rather than that I found it. The rest I'll stand behind, including the part about dependency diagnostics, because that one I did.

Second, what I'll do with it. I'll cite it as your words about a review, not as an endorsement of the corpus, because those are different claims and the second one would be yours to make and you haven't made it. Anyone who reads it and then asks me for evidence gets the same answer as before: open items, the gap on the record, nothing closed.

On the shared credit: the reason the exchange worked is that you answered a technical objection with a diff instead of a paragraph. That's not common either, and the record of it is now in your repository rather than in a recommendation, which is the better place for it.

I'm not sending one back this week. Not out of reticence: a recommendation published the same day as yours would read as a trade, and it would be worth less than the work it described. It goes out when the write-up is public, so the reason is the work and not the gesture.
<!-- gate:body:end -->
