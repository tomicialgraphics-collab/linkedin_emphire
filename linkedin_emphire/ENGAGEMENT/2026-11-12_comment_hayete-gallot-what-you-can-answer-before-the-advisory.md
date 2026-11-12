---
deliverable: comment
id: 2026-11-12_comment_hayete-gallot-what-you-can-answer-before-the-advisory
date: 2026-11-12
audience: public, under Hayete Gallot's post
status: ready
approved: no
warm: no
profile_checked: 2026-11-12 from the post and the show page the post links to. Hayete Gallot is Executive Vice President of Microsoft Security and is launching Safety in Numbers, a podcast produced by Larj Media, in which each episode starts from one number. Her number here is negative ten hours, the collapsed window between discovering a vulnerability and the attack. The comment says nothing about her beyond the post and the page, and nothing about Microsoft's products.
thread: the negative exploitation window, and what a defender should measure if the advisory now arrives after the attack
premise_checked: stable: the negative ten hours figure is her own framing of the discovery-to-exploitation window, repeated in the show description, and the comment takes it as given rather than asserting or disputing it. The figure itself was not independently verified and the comment does not depend on whether it is exactly right, only on the window being negative. The show's own stated thesis, that the answer is not fixing everything but a different operating model, is the thing the comment builds beside rather than repeats.
sources_read: read: the link in the post, 2026-11-12, which resolves through a Linkfire landing page to Apple Podcasts, Spotify and Amazon Music, and carries the show description and a summary of the first episode. The individual platform pages were not opened, because the landing page carried the description and the episode summary and no audio was available to listen to. No article or report is attached.
---

## Comment, paste as is

Negative ten hours moves the job earlier, and it moves what a defender should measure too. If exploitation lands before the advisory, the first signal can't be a severity score or a patch, because neither exists yet. What's left is an attempt in your own telemetry against a host you already knew was exposed.

So the useful number is dull and uncomfortable: for how much of the internet-facing estate would you have a log that would show that attempt, and how far back does it go? Time to patch is measured from a date that hasn't arrived yet. This one you can answer today and fix before the next advisory rather than after it.

There's an episode in that, and I would listen to a defender being asked to prove the share rather than state it.

## Why this angle

The show's premise is that every number has a story, and its stated conclusion is that the answer is not fixing everything. That leaves a gap a comment can fill: if the window is negative, patch time stops being a leading indicator, and something has to replace it. Its replacement is not a better prioritisation score, because the score is derived from the advisory the attacker has already beaten.

The one thing a defender has before the advisory is their own logs. So the number that predicts how the next window goes is coverage: the share of the exposed estate where an attempt would produce a record, and the retention that decides whether the record still exists when somebody thinks to look. It is the kind of number a board can be given, and unlike patch time it can be improved before the event rather than explained after it.

That last line is aimed at the format. Each episode starts from one number and asks what leaders should do, and a defender being asked to prove a coverage share rather than state one would be the most useful episode in the series.

## What this is not

It is not a fact-check of the ten hours. She is quoting a figure that carries her argument, the comment does not need it to be exact, and a stranger challenging an executive's opening number under a launch post is the wrong first move with a person whose programme is worth reaching.

It is also not a summary of the episode, which was not listened to, only read about on the landing page. The file says so rather than implying otherwise.

No link, no pitch, no mention of Microsoft tooling, and no self-promotion under a Microsoft executive's launch post, which is the one place a pitch would travel furthest in the wrong direction.

## If she replies

Under R38 a reply is owed the same day. The likely pushback is that Microsoft already ships this coverage view, which would be fair and does not change the question, because the number is about the customer's estate rather than the vendor's dashboard. Then the follow-up is retention, since a share without a retention period is a claim about today only.
