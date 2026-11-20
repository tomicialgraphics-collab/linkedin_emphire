---
deliverable: internal
id: 2026-11-20_reading-the-repo-rules
date: 2026-11-20
audience: internal
status: ready
title: What eri-test already decides, and the two places it collides with our plan
time_checked: >-
  checked: 2026-11-20 16:45 WAT, read from the system clock before this file was written.
profile_checked: >-
  Not a per-person deliverable. Written for the owner, from files he pasted after cloning DUNIN7/eri-test at 16:42.
premise_checked: >-
  checked: every quotation is from the pasted text of CLAUDE.md and DATA-RULES.md as read at 16:42 WAT, not paraphrased
  from memory. The version gap was confirmed against this workspace, which holds the v0.4 amendments and no v0.4 file in
  the repository. The mojibake in the pasted output is a Windows console decoding artefact, not a defect in the files,
  and is reported as such rather than as a repo problem.
sources_read: >-
  read: CLAUDE.md and DATA-RULES.md of DUNIN7/eri-test as pasted by the owner on 20 November, and the file listing of
  the same clone. Nothing opened through the browser.
---

# The rules are already better than the ones I asked for

`CLAUDE.md` v0.2 already carries, in the agent's own reading list: never commit to `main`, never force-push, rebase or
amend a pushed commit, never rewrite history, never merge your own pull request, never commit anything in `DATA-RULES.md`,
never invent a postcode or a transaction ID and present it as real, one branch per task, tests written from the
acceptance criteria before the code, and a handoff note at the end of every session.

My suggestion of putting three lines in `CLAUDE.md` is withdrawn. It is done, and done better than the version I had in
mind, because it also tells the agent where to look and what to write down.

`DATA-RULES.md` goes further than the version we discussed: postcodes of real homes are barred except NIPOST's own test
values, demo content is deleted thirty days after the review, and fingerprints and anchor references stay so a copy can
still be shown to have existed on a date. That last clause is the product's own logic applied to its own test data, and
it is the right call.

# Collision one: the phone gate cannot be met by the first requirements

`CLAUDE.md` says: "A requirement is done only when its acceptance criterion has been observed on the Android phone and
the iPhone. A pass on a laptop is not a pass."

That is a good rule for a screen and an impossible rule for a schema. Cycle one is REQ-001 to REQ-009 plus REQ-050: the
event table, the revoke, the adapters, the sample path and the postcode format check. Several of them have no phone face
at all. Either the gate means "every requirement whose criterion names a device", or cycle one has no definition of done
and stalls on the first commit.

**Ask Marvin which he means.** Two sentences, and it decides whether Monday's work can close a requirement or only
hand one to the next person.

# Collision two: the repository is one version behind on requirements

The repository carries `docs/ERI-REQ-v0_3.md`. This workspace holds the v0.4 amendments: REQ-046 to REQ-053, the
sample-labelling rule, the fourth answer, the timing changes, and the revised arithmetic of 7.65 build days. None of that
is in the repository, and `CLAUDE.md` tells every session to read the REQ before planning work.

So the first pull request is not code. It is the v0.4 amendments as `docs/ERI-REQ-v0_4.md`, on a `docs/` branch, with the
eight new requirements and their acceptance criteria, so the agent that reads the repo tomorrow reads the same document we
are building from.

# What the stack confirms, and what it leaves open

The stack matches the plan: Next.js 15 with TypeScript strict, Postgres with Drizzle and raw SQL migrations, Vitest, and
`next-intl` with `en` and `yo` message files. Three things to note rather than fix:

- **Stele appears as a fact** in the stack, as a Python service beside the app, while we still have no answer on whether
  it can mount this week. It stays the one assumption in week one.
- **Next.js 15 means a Node application**, which makes the anchor probe more useful, not less: it is the one part that
  runs anywhere with no dependencies.
- **`spike/` branches are never merged**, by rule, and their result is a decision note. That is exactly the shape the
  anchor probe should take: a branch called `spike/anchor-probe`, the script, its dry-run output, and a decision note in
  `docs/decisions/` saying whether FORAY returns something a stranger can open.

# The console artefact

The pasted output shows `Â·` and `áº¸Ì€rÃ` where the files contain `·` and `Ẹ̀rí`. The files are UTF-8, which is correct;
Windows PowerShell 5.1 decodes them as ANSI when printing. Read them with `Get-Content -Encoding UTF8`, and edit them with
an editor that writes UTF-8 without a BOM, or the tone marks will break.
