---
deliverable: doc
id: 2026-11-20_session-log
date: 2026-11-20
audience: internal
status: ready
approved: no
time_checked: >-
  checked: 2026-11-20 18:48 WAT, read from the system clock in the sandbox before this file was written.
---

# Session log, 2026-11-20

What this is: the record of the cloud session on branch `claude/festive-goldberg-nrko22`, from the boot read to the
filing of the Marvin thread. Who it is for: the next session, so nothing here is re-derived from chat. What to do next:
the open loops L74 to L76, and the order of work at the end.

Other sessions worked today too, and their drafts are the many `ENGAGEMENT/2026-11-20_*` files. This log covers only
this one.

## Instructions from the owner, in order

1. "Read through all lines of each files and we will discuss." The repository holds about 1,700 text files and 335,000
   lines, so the boot set was read in full instead (AGENTS, README, context.md, every PIPELINE document, the open loops,
   the reply queue, the revenue log, the borrowed-audience board, the case-study index), and the owner was told so.
2. "Do you understand my objectives and goal", and read the LinkedIn profile. The public URL refused with HTTP 999. The
   goals were read from `STRATEGY/2026-11-12_revenue-5000-by-25-dec.md` and the follower plan.
3. Three screenshot sets of the live profile and the full activity list. Read and filed as
   `LINKEDIN/2026-11-20_profile-read_about-services-and-the-feed.md`.
4. Marvin's 16:20 message about `DUNIN7/eri-test`. The repository was attached after three failed tries (permission
   check, then GitHub access, then it worked once the Claude app and the account were settled on the owner's side) and
   cloned into the session.
5. Fork or clone. Answered: neither into an account; a local clone is the collaborator's way, and nothing from it ever
   goes into this public repository.
6. "Read the Standards, decision 0001 and the feat/event-table migration, and report what matters before Monday."
   Read only. Filed as `CLIENTS/eri/2026-11-20_review_repo-standards-0001-event-table.md`.
7. The full LinkedIn thread with Marvin, 02:22 to 18:27. Filed as `CLIENTS/eri/2026-11-20_thread_linkedin-marvin.md`.
8. "Save all chat thread, deliverables, reply in the emphire folder, check where they belong." This filing.

## What was found at boot, and is not yet fixed

- Rule counts disagree: AGENTS, README and 00-START say 30 rules with 20 or 23 blocking; the registry holds 49 with 29
  blocking.
- `context.md` was last updated on 6 November and still says Aithos was sent on 31 October, which the open loops
  corrected to 14 October.
- Open-loop IDs L11 to L15 are each used twice for different subjects.
- No session log from 16 to 19 November, though the open loops record work on those days.
- `context.md` Appendix A carries the owner's phone number in a public repository (R24).
- Two copies of the NIST paper, in `books/` and `ARTICLES/`, against the no-two-copies rule.
- The follower log had no row from 14 to 19 November, which R41 needs before a post ships. Today's row is now in.

## Decisions and reasoning

- **The impression fall was misread first, then corrected.** The first reading said posting had stopped, because every
  post folder from 16 November says `status: ready`. The activity list showed posts at 11 hours, 16 hours and 2 to 4
  days. Reach fell per post, not by count, and the repository is what fell behind.
- **"A decade" in the live About is an R06 problem**, not a style one. The owner's first post says three years.
- **Decision 0001: accept.** The owner had already accepted it at 16:51 with two conditions. Two more were added for
  the note: one shared hash function, and Stele sessions verified on the server. The note is 0003 because 0002 is taken.
- **The purge door is good engineering and still breaks F6 as written.** Marvin rules on it before PR 6 merges.
- **What goes into this repository from eri-test is a summary only.** DUNIN7's repository is private and this one is
  public, so no standards text, requirement text or code is copied here.
- **The thread is filed with three things withheld**: the credential Marvin posted at 04:12, his family's travel, and a
  deleted message. A password in a public repository would turn a slip into a breach.

## Files from this session

| File | What it is |
| --- | --- |
| `CLIENTS/eri/2026-11-20_thread_linkedin-marvin.md` | the thread of record, 02:22 to 18:27 |
| `CLIENTS/eri/2026-11-20_review_repo-standards-0001-event-table.md` | the repository read before Monday |
| `ENGAGEMENT/2026-11-20_dm_marvin-the-password-in-the-chat.md` | change the shared password; ready, not sent |
| `ENGAGEMENT/2026-11-20_dm_marvin-decision-0001-in-and-reading.md` | superseded draft; the owner sent his own at 16:51 |
| `LINKEDIN/2026-11-20_profile-read_about-services-and-the-feed.md` | the profile and feed, read from screenshots |
| `analytics/follower-log.md` | the 20 November row, 1,374 |
| `STATE/OPEN-LOOPS.md` | L74 Ẹ̀rí before Monday, L75 credentials, L76 profile |

Nothing was sent, posted or pushed to Marvin's repository. No live LinkedIn or Upwork page was touched.

## Where things stand on the three goals

- **Money:** 90 dollars paid against 5,000 by 25 December. The 29 November checkpoint (first 1,000 agreed) has nothing
  agreed yet. Kuldeep's 1,500 is proposed; Marvin's 1,500 W-04 scope is drafted and unsent.
- **Fellows:** due Saturday 28 November, 08:59 WAT. The coding test invitation is unconfirmed, the take-home not
  started, two references outstanding. It collides with Ẹ̀rí cycle one in the same week.
- **Followers:** 1,374. At about 25 a day the plan reaches roughly 2,250 by 25 December.

## Next, in order

1. The owner changes "a decade" and trims Services, today, because Fellows reviewers read the page this week.
2. The credential message to Marvin, in his morning.
3. In eri-test, each as a pull request the owner sees before it is pushed: REQ v0.4, decision 0003, the F6 note, the
   hash chain migration.
4. Bring post folders from 16 November up to date with their live status.

## Later, 19:04 WAT: Marvin's answer

He replied at 19:01, appended to `CLIENTS/eri/2026-11-20_thread_linkedin-marvin.md`. PR 5 closed with no purge, PR 4
merged, PR 6 praised. His design replaces the purge door: each event splits into a record that never goes (kind, seq,
fingerprint, seal) and a content table that alone can be purged, written as decision 0003 before PR 6 merges. That takes
number 0003, so the stack-conditions note becomes 0004. He takes the connecting-role question into DEPLOYMENT.md.

Reply drafted as `ENGAGEMENT/2026-11-20_dm_marvin-the-split-and-0003.md`, PASS at human 92, not sent. It accepts the
split, adds the address to the content side and the hash chain over the record half, and says the commit label is corrected
forward because the instructions forbid amending a pushed commit. Its last line assumes `claude/adoring-babbage-jng35n`
is the owner's: the commit is signed plain "Claude" at 16:03 WAT, not "Claude (for Marvin Percival)". The owner confirms
before it goes. L74 and L75 updated to match.

Also said to the owner this evening, at his request, and not repeated in any file outward: what the emphire is not
doing well. In short, free work, drafts that are never sent, a rule set that grew from 30 to 49 while the basics slipped,
too many threads at once, a public story that disagrees with the record, and security habits that do not match the brand.
