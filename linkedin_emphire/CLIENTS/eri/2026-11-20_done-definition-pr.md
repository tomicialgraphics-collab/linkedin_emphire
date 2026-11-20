---
deliverable: internal
id: 2026-11-20_done-definition-pr
date: 2026-11-20
audience: internal
status: ready
title: The docs pull request that defines what done means
time_checked: >-
  checked: 2026-11-20 16:54 WAT, read from the system clock before this file was written.
profile_checked: >-
  Marvin Percival, who answered the phone-gate question at 4:51 PM with his own wording, asked for it to go in on a docs
  branch, and said he would approve it tonight so it lands before the agent starts.
premise_checked: >-
  checked: the sentence being replaced is quoted from the instructions file read at 16:42 WAT. The replacement is his
  wording from 4:51 PM, unchanged, not a rewrite of it. The claim that the second sentence depends on the approval rule is
  read from the same file, which requires another person to review and merge every pull request.
sources_read: >-
  read: CLAUDE.md of DUNIN7/eri-test as pasted at 16:42 on 20 November. No page opened.
---

# The edit

In the instructions file, in **While working**, replace this sentence:

> A requirement is done only when its acceptance criterion has been observed on the Android phone and the iPhone. A pass
> on a laptop is not a pass.

with his wording, verbatim:

> A requirement whose acceptance criterion involves a screen or a device feature is done only when it has been observed on
> both the Android phone and the iPhone. Every other requirement is done when its automated tests pass.

That is the whole change. One sentence out, two sentences in, nothing else touched.

# The optional third sentence

Worth offering, and easy for him to strike: the second sentence is only safe because every pull request needs the other
person's approval. Without that rule, "done when its automated tests pass" lets one person write a test, watch it pass and
declare the requirement finished, which is the failure mode this product exists to argue against. If he takes it, it goes
directly underneath:

> The second sentence depends on the approval rule below: a test cannot be accepted by the person who wrote it.

# The branch and the pull request

```powershell
cd "$env:USERPROFILE\Desktop\PROJECTS\eri-test"
git switch main
git pull --ff-only
git switch -c docs/done-definition
```

Make the edit by hand or have Claude Code make it, then:

```powershell
git add CLAUDE.md
git commit -m "DOCS: define done for device requirements and for the rest"
git push -u origin docs/done-definition
```

Pull request title: `DOCS: what done means for device requirements and for everything else`

Pull request body:

```
Marvin's wording, from his message of 4:51 PM on 20 November, with no changes.

**What changed:** the single "done only when observed on both phones" sentence in While working is replaced by two
sentences. A requirement whose acceptance criterion involves a screen or a device feature is done when observed on both
phones. Every other requirement, including the event table, the revoke, the adapters and the sample path, is done when its
automated tests pass.

**Why:** cycle one is ten requirements and most of them have no screen. Under the old sentence they could not be finished,
and the build would stall on its first commit rather than on a real problem.

**How it was checked:** nothing to run. One sentence replaced, no other line touched.

**REQ numbers:** none yet. This is the rule that decides when REQ-001 to REQ-009 can be closed.
```

He merges it. The instructions file forbids merging your own pull request, and this one is his to approve.

# After it merges

The handoff note in `notes/` is the last thing to write before stopping, and it is three lines: what is done, what is next,
what is blocked. The blocked line has one entry worth naming honestly: whether there is an Android phone to test on.
