---
deliverable: post
id: 2026-11-21_post_the-door-built-in-a-week
date: 2026-11-21
audience: outbound
status: ready
approved: no
channel: LinkedIn, own feed
template: T6
headline: Remove the reset email and your recovery path becomes your login.
subheadline: Attackers skip the door you hardened for a year and try the one you built in a week.
headline_alt: >-
  Passkeys stop phishing. They don't help the person who just lost every device.
subheadline_alt: >-
  Whatever you build for that day is a second way in, and it gets the least testing.
headline_alt2: >-
  The cheapest login to break is the one built for someone who lost everything.
subheadline_alt2: >-
  An account recovery path with no email behind it has to carry its own safety checks.
box: THE OTHER DOOR
box_alt: LOST EVERYTHING
hashtags: ["#AISecurity", "#AIRedTeam", "#AIEvaluation", "#AIEngineering"]
premise: >-
  Observational post for Saturday 21 Nov 2026. Systems that drop email for passkeys lose the reset link that quietly did
  the recovery work, so recovery has to be rebuilt by hand, and that rebuilt path is the one attackers try first. It
  speaks to the buyer in the ICP note (founders of agent identity and access companies) and ends on three questions the
  reader can check against their own system. It names no person, company or product.
time_checked: >-
  checked: 2026-11-21 05:05 WAT, read from the system clock in the sandbox before this file was written.
profile_checked: >-
  Olusanya Timothy, AI red teaming and evaluation, Lagos. The post is written to the selling point in
  STRATEGY/2026-11-20_icp-and-selling-point_verified.md: specific attacks, said plainly, no service announced.
premise_checked: >-
  opinion: a design argument about account recovery. It quotes no figure, statute or product, and the post says why it
  carries no number.
sources_read: >-
  none: nothing attached.
---

## Post, paste as is

<!-- gate:body:start -->
Remove the reset email and your recovery path becomes your login.

Passkeys are a real step up. They stop phishing cold. What they don't cover is the day someone loses every device they own.

Most systems quietly lean on email for that day. "Forgot password" sends a link, and the inbox does security work nobody ever wrote down.

Take email away, which is often the right call, and you have to build that safety net yourself. A recovery code. A delay before it works. A record that it was used. Every one of those is a door.

And attackers don't try the door you hardened for a year. They try the one you built in a week for the rare case.

The same goes for AI agents. The path that revokes and reissues an agent's credentials gets far less testing than the path that grants them.

So when I test a sign-in system, I start where the team spent the least time: the person who has lost everything.

Three questions to ask of your own system:

1. Can a stolen recovery code be used before the owner notices?
2. Does cancelling a recovery end the sessions it already opened?
3. Do your guessing limits survive a restart?

There's no statistic here because nobody counts these paths. If any answer is "I'd have to check", that's your next test.

#AISecurity #AIRedTeam #AIEvaluation #AIEngineering
<!-- gate:body:end -->
