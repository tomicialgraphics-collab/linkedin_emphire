---
deliverable: dm
id: 2026-11-20_dm_marvin-the-repo-is-up
date: 2026-11-20
audience: outbound
status: superseded
approved: no
recipient: Marvin Percival
premise: >-
  The build repository exists at github.com/Teamthy/Eri-OS, empty, created 01:08 WAT. Marvin needs to know it exists,
  needs to be given access, and the two of them need one rule about what never goes inside it. This message gives him
  the link, asks for his GitHub username, states the access level and the reason for it, and carries the rule that the
  code works the same way as the product: nothing is rewritten quietly.
time_checked: >-
  checked: 2026-11-20 02:11 WAT, read from the system clock before this file was written. That is 20:11 on Thursday in
  New York.
profile_checked: >-
  Marvin Percival, who builds software for a living and who argued all night that a record must never be able to hide
  a change. The repository rules here are the product's rules applied to the code, because he will notice if they
  aren't and he will be right to name it.
premise_checked: >-
  checked: the repository was read through the GitHub API before this message was written. It is empty, it was created
  at 01:08 on 20 November, and it is currently public, which is why the first line of the message is a change of
  visibility rather than an invitation. The visibility must be changed before this is sent, or the message is untrue.
sources_read: >-
  read: github.com/Teamthy/Eri-OS through the GitHub API on 20 November. No page opened.
---

## Superseded by 2026-11-20_dm_marvin-both-of-us-admin.md. Do not send this one.

If it is sent while the repository is public, the second paragraph is a false statement to a co-builder on day one.

## Message, paste as is

<!-- gate:body:start -->
Repo is up. github.com/Teamthy/Eri-OS. It's empty on purpose, because I'd rather push the skeleton than a pile of files I haven't decided about. The name is as temporary as the working name.

I'm making it private now, before you open it, so if the link gives you a 404 that's why and not a typo.

Send me your GitHub username and I'll add you with write access. Write, not admin, and it's not me being precious. Admin can change the visibility and delete the repository, and at two in the morning neither of us should be able to do that alone.

Main is protected and we merge by pull request, with the reason in the message. Same rule as the product. If we can't work that way on the code, we shouldn't be asking families to work that way on their land.

Two rules inside it. No real names, no real numbers, no documents belonging to anyone real, and the demo household stays invented. And keys live in the environment, never in the repository, which is what REQ-006 is about and is how small teams get breached.

I'll push the skeleton Monday after the anchor test, so what you see on your first visit is what day one actually looked like.
<!-- gate:body:end -->
