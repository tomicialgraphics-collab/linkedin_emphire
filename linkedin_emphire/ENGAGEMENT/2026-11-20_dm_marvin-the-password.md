---
deliverable: dm
id: 2026-11-20_dm_marvin-the-password
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Marvin Percival
premise: >-
  A local Postgres password was written into a file through the GitHub web editor at 5:35 PM and lives in a commit on an
  open pull request, PR #5, in the private repository. DATA-RULES.md step 2 says tell him the same day. He is at the
  airport, so the message has to work read once, later, with no question left hanging.
time_checked: >-
  checked: 2026-11-20 17:39 WAT, read from the system clock before this file was written. The commit and pull request
  numbers are from the session output of 5:37 PM.
profile_checked: >-
  Marvin Percival, architect and co-founder, who wrote the data rules himself and asked for decisions and evidence rather
  than build steps. He values a flag over a tidy silence, and the rules he wrote only work if the first breach is
  reported plainly and early.
premise_checked: >-
  checked: the exposure is a password for a Postgres instance on the owner's own laptop, in a private repository, so the
  message says that plainly rather than either minimising or dramatising it. The remediation listed as done is what is
  being done in the same session: the password is rotated, the pull request is closed unmerged, and the file is never
  merged. The one open question, whether to ask GitHub to purge, is left to him because it is his call as owner.
sources_read: >-
  read: DATA-RULES.md as pasted on 20 November. No page opened.
---

<!-- gate:body:start -->
One thing to flag now rather than after the weekend. I put the local database password into a file through the GitHub web editor instead of on my laptop, so it went into a commit on a pull request rather than staying in a file that git ignores. Nothing merged, and the database is a Postgres on this machine, not anywhere near real data. The repo is private, so the exposure is small.

Still, the rules say tell you today, and I would rather you read it from me than find it in the history later.

Already done: the PR is closed without merging, the password is changed, and nothing else used it. The file is not coming back.

One question for when you land. Do we ask GitHub to purge that pull request, or leave it closed with the password rotated? I have no strong view and it is your call.
<!-- gate:body:end -->
