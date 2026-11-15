---
deliverable: comment
id: 2026-11-15_matt-pocock_home-repo-pattern
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 09:04 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: public
status: ready
approved: no
target: Matt Pocock, author of AI Hero, post announcing the Home Repo pattern article
profile_checked: >-
  The post says what it says: a published article on the Home Repo pattern, a prompt to set one up, four minutes old
  when it was pasted. Nothing about his audience size or history is claimed in the comment, because none of that was
  checked.
premise_checked: >-
  checked: the article was opened and read in full on 15 November 2026, both halves, including the setup prompt and the
  FAQ on scale. The comment adds two things the article does not cover, the pointer list as a privilege list and the
  stale pointer, and does not repeat its own contents back at it. The claim about what the prompt already does is
  accurate to its text: read-only until the plan is approved, and secrets left unread.
sources_read: >-
  read: https://www.aihero.dev/the-home-repo-pattern in full, reached through the shortened link in the post, which
  turned out to resolve to that address rather than to a landing page. Read on 2026-11-15.
---

# Comment on Matt Pocock's Home Repo post

<!-- gate:body:start -->
The part I would add is what happens when one of those skill files is wrong on purpose.

I red-team agents, and a Home Repo ends up being the most powerful file in the setup. One steering file now names every repo you own, so anything that can write a line into it, or into a skill it points at, hands an agent a map of your whole estate and a reason to trust it. The pointer list is a privilege list.

Two additions to the prompt. Treat every skill and doc as untrusted input rather than instructions from you. And after the inventory step, ask the agent to name the files it read before it proposed the plan, which catches the case where a repo's own steering file quietly redirected it.

The failure that bites quietly is the stale pointer. A missing repo is easy, the agent clones it. A stale one means it works in an old fork, everything passes, and nobody notices for a month.
<!-- gate:body:end -->
