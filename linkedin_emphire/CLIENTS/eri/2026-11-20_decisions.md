---
deliverable: internal
id: 2026-11-20_decisions
date: 2026-11-20
audience: internal
status: ready
title: Decisions on Eri, as they stand at 02:30 on 20 November 2026
sources_read: >-
  read: the LinkedIn thread of 20 November and the GitHub API for Teamthy/Eri-OS.
---

# Settled

| Decision | Who said it | When |
| --- | --- | --- |
| Ẹ̀rí is the product to build, not the other idea with a ready market | Marvin, one word | 2:24 |
| Nigerian company, owner 51, Marvin 49 | Agreed on the call | before 2:00 |
| The test is hosted on Marvin's Mac Mini | Marvin | 2:22 |
| Real data has to be hosted in Nigeria | Marvin | 2:22 |
| No deadline: cycles end when their criteria pass | Both | by 2:00 |
| Claude subscription is Marvin's cost | Agreed on the call | before 2:00 |
| Repo is `Teamthy/Eri-OS`, Marvin invited as `DUNIN7` | Marvin | 2:21 |
| There is no NIPOST key. Live keys need company verification, so cycle one runs on recorded sample responses | Marvin | 2:37 |
| The sample path gets its own requirement, REQ-052, so a sample address is labelled wherever it appears | Owner | 2:42 |
| The build is a test, not necessarily a product. The test settles three things, listed in the message of 02:57 | Marvin, then both | 2:47 |
| NIPOST expression of interest submitted by Marvin, reference 6affa72517651272a87e6b6c0 | Marvin | 2:49 |

# Open, and who owes an answer

- **Who pays at the moment of sale, and the number.** Owner asked at 12:18, still unanswered. It is the one thing that
  turns distribution from a story into a test.
- **Per-deal agency price.** Asked at 12:18, still unanswered. The subscription alone loses the small agencies.
- **How the Claude seat works.** Owner has withdrawn the shared-login idea; either a seat on a team plan or the money.
- **Whether the Mac Mini can be reached from outside Marvin's network.** Needs a tunnel or a stable address before the
  first Friday review, or the review cannot see the build.
- **NIPOST's reply.** What they need to verify a Nigerian company, and whether a sandbox or test postcodes exist. Reference 6affa72517651272a87e6b6c0.
- **Stele.** The only remaining week-one assumption. Whether it can mount, or whether a development-only session is agreed in writing. Asked three times.

# Housekeeping that is the owner's to do, not Marvin's

- Make `Teamthy/Eri-OS` private. It was still public at 02:30, and files are due in it in the morning.
- Pay for GitHub Pro or move to an organisation on Team, otherwise a private repository cannot have protected branches.
- Accept the invitation check: the invite went to `DUNIN7` and unconfirmed until he accepts.

# The thing to watch

Marvin now owns hosting, repository setup, the subscription and the file loading, and has said he will review the plan
tomorrow. That is a lot of the critical path in one person's evening. The counterweight is that the owner has the one
date nobody else has: Monday morning's anchor test, which produces a fact regardless of whether anything is agreed.
