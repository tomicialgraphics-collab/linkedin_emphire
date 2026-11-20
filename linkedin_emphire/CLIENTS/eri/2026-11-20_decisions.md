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
| **Superseded, 16:41:** the repo of record is `DUNIN7/eri-test`, private, and the owner accepted the invite | Marvin created it, owner accepted | 14:12 |
| Claude subscription settled: 40 dollars for two months, sent via Marvin's wife in Washington | Marvin | 13:36 |
| There is no NIPOST key. Live keys need company verification, so cycle one runs on recorded sample responses | Marvin | 2:37 |
| The sample path gets its own requirement, REQ-052, so a sample address is labelled wherever it appears | Owner | 2:42 |
| The build is a test, not necessarily a product. The test settles three things, listed in the message of 02:57 | Marvin, then both | 2:47 |
| NIPOST expression of interest submitted by Marvin, reference 6affa72517651272a87e6b6c0 | Marvin | 2:49 |

# Open, and who owes an answer

- **Who pays at the moment of sale, and the number.** Owner asked at 12:18, still unanswered. It is the one thing that
  turns distribution from a story into a test.
- **Per-deal agency price.** Asked at 12:18, still unanswered. The subscription alone loses the small agencies.
- **How the Claude seat works.** Closed at 13:36: two months of Pro paid. The Team plan was priced and declined, because 25 a seat with a two-seat minimum is 50 a month against 40 for two subscriptions.
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

# The repository, and the one thing about it that is not settled

`DUNIN7/eri-test` is private, which was the first requirement, and it is under **Marvin's personal account**, not an
organisation. That is why it does not appear in the owner's own repository list: GitHub lists the repositories you own
there, and this one is his. The direct link is what to bookmark.

Three consequences worth naming while the repo is a day old and empty of consequences:

1. **The project's history sits under the 49 per cent partner's personal login.** Under the agreement the company is
   Nigerian, the owner holds 51, and the code, the issues and the commit history are the company's asset. Moving it to a
   free GitHub organisation, with both of them as owners, costs nothing today and is a transfer rather than a rewrite,
   because GitHub keeps history and redirects the old path.
2. **Admin is not the same as collaborator.** An invitation accepted as Write gives no Settings tab and no ability to
   change who else can reach the repo. Check for the Settings tab on the repo; if it is missing, ask for Admin.
3. **Branch protection on a private repository needs a paid plan.** If it is not available, the rule that binds the agent
   has to be agreed in writing instead, and written where the agent reads it, which is `CLAUDE.md`.

The agent branch `claude/adorning-babbage-jng35n` pushing to its own branch and offering a compare link is the right
shape. An agent that opens a branch is auditable; an agent that pushes to `main` is not.

