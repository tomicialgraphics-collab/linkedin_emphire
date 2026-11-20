---
deliverable: post
id: 2026-11-18_vibe-coding-balance
date: 2026-11-17
audience: public
status: ready
approved: no
template: T1
visual_link: https://drive.google.com/file/d/1pYL2ifcoArqNHzHfhFHsATVUDBoSEQSU/view
headline: People argue about vibe coding and AI security as if one of them has to give.
subheadline: What decides how much speed you can take isn't how much code the model wrote. It's where the failure lands.
headline_alt: >-
  Vibe coding is fine until the mistake stops announcing itself.
headline_alt2: >-
  You don't choose between speed and security. You choose where the failure lands.
box: LOUD OR SILENT
box_alt: REVERSIBLE
hashtags: ["#AISecurity", "#AIEngineering", "#SoftwareEngineering", "#AIGovernance"]
time_checked: >-
  checked: 2026-11-17 23:59 WAT, read from the system clock before this file was written. Written on the 17th for the morning slot on
  18 November, because the feed is thin at midnight.
premise_checked: >-
  checked: the twenty-two figure is the count of failure modes in the host-failure benchmark that ships in this
  workspace, and every mode has a reproducer attached, which is what the last sentence claims. No statistic is
  invented, no survey is cited, and the two questions are tests a reader can apply in a minute without buying
  anything.
sources_read: >-
  read: the benchmark's own register and the runs from 16 and 17 November. No external page opened, so the argument
  rests on the reader's own experience rather than on a citation.
---

## Post, paste as this

<!-- gate:body:start -->
People argue about vibe coding and AI security as if one of them has to give.

I don't think that's the argument. What decides how much speed you can take isn't how much of the code a model wrote. It's where the failure lands.

A model can rebuild a layout in ninety seconds, and you'll know in ninety seconds whether it's wrong. That loop is why vibe coding feels like cheating, and it's also why it works: the mistake is loud, and it's cheap to reverse.

Security failures don't do that. They sit quietly in an endpoint that authenticates nobody, a key in a log line, a permission granted to a service account because it made the test pass. You find them months later, or somebody else finds them for you.

So the balance isn't a dial. It's two questions, asked before you start anything.

If this is wrong, who notices inside an hour?

Can I undo it without asking anybody's permission?

Where both answers are good, go fast and skip the ceremony. Where the failure is silent and the undo needs a meeting, the check comes first, and then the fast part happens against a check that already exists.

That's the whole balance, and it isn't really a compromise. A check you can run in a minute is what buys the right to keep the speed. I have 22 of them for one class of failure, and every one exists because that particular lie was silent until it was expensive.

#AISecurity #AIEngineering #SoftwareEngineering #AIGovernance
<!-- gate:body:end -->

## First comment, within twenty minutes

The 22 are here, each with a reproducer attached: github.com/Teamthy/Ai-Red-Team-Playbook

The class they cover is a host layer that lies about its own state. If you run any of them against something you own and it passes when it shouldn't, that's more useful to me than a star.

## Why this framing

The usual version of this post is a both-sides essay, which nobody finishes. The framing that earns attention says the trade-off is not between fast and safe, and then gives the reader a test they can run on their own next ticket in under a minute.

Both questions are answerable by one person in a room, which is the point. A framework would have lost them.

## Why the last line carries the number

Twenty-two with reproducers is a claim the reader can check by opening the repository, which is the only kind of number worth putting in a post. It also avoids the survey-statistic opening that makes this genre of post indistinguishable from the rest.

## What not to do

No claim that vibe coding is safe or unsafe in general, no criticism of any named tool, and no story about a client. The post argues about failure visibility, which is a property of a system rather than of a person's habits.
