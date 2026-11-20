---
deliverable: dm
id: 2026-11-20_dm_marvin-both-of-us-admin
date: 2026-11-20
audience: outbound
status: ready
approved: no
supersedes: 2026-11-20_dm_marvin-the-repo-is-up
recipient: Marvin Percival
premise: >-
  The owner pushed back on the previous message, correctly, on the grounds that a permission he keeps and Marvin does
  not is a hierarchy rather than a partnership. This message agrees, makes both of them administrators, and then does
  the thing that actually protects the repository: branch rules that bind the owner too, with administration included
  in the rule and no bypass for anyone.
time_checked: >-
  checked: 2026-11-20 02:14 WAT, read from the system clock before this file was written. That is 20:14 on Thursday in
  New York.
profile_checked: >-
  Marvin Percival, an engineer who will read a permission model the way he reads a schema, and who spent the night
  arguing that a record must not be able to hide a change. He will notice immediately if the repository rule exempts
  the person who wrote it.
premise_checked: >-
  checked: the plan restriction was verified by web search before it was put in the message. Protected branches and
  rulesets are not available on private repositories under GitHub Free, and are available on GitHub Pro for a personal
  account or GitHub Team for an organisation, which is four dollars a user a month at the time of writing. The
  repository is owned by a personal account, so Pro is the cheaper route of the two.
sources_read: >-
  read: four write-ups of GitHub plan features and two GitHub community discussions on rulesets for private repos, by
  web search on 20 November. The GitHub pricing page itself was not opened.
---

## Supersedes the earlier repo message. Send this instead, not both.

## Message, paste as is

<!-- gate:body:start -->
You're right, and better to say it before you do. If we're building this together, a permission I keep and you don't is a hierarchy with a nicer name.

So both of us admin. But admin on GitHub isn't a building permission, it's a destroying one. It can turn the repo public, transfer it to another account, or delete it entirely. None of that helps write a line of code, and all of it is hard to undo at two in the morning.

So the rule has to cover both of us instead. I'm paying for Pro on my account this week, because a private repo can't have protected branches without it, and it's four dollars a month. Then main gets this: a pull request to merge into it, one approval from the other person, no force pushing, no deleting, and administrators included in the rule so it binds me too. No bypass list.

That's the version of together I can defend. Same rule as the product. Nothing is rewritten quietly, including by the person who wrote the rule.

Send your username and I'll add you as admin. Turn on two-factor if it isn't already, because a stolen account with admin on this repo is the whole thing gone.
<!-- gate:body:end -->
