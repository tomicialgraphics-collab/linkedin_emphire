---
deliverable: internal
id: 2026-11-20_decision-note-done-definition
date: 2026-11-20
audience: internal
status: ready
title: Draft decision note for what done means, in case the standards file makes it a default
time_checked: >-
  checked: 2026-11-20 17:00 WAT, read from the system clock before this file was written.
profile_checked: >-
  Marvin Percival, whose instructions file says a change to a default needs a decision note in docs/decisions rather than a
  quiet edit. The note is written to that rule, and it may turn out to be unnecessary, which is why it is drafted rather
  than committed first.
premise_checked: >-
  checked: the requirement to write a decision note is quoted from the instructions file read at 16:42 WAT, and the
  observation that the standards file might carry the phone rule is the agent's own catch, printed in the session output
  at 16:58. This file does not assert what the standards file says, because it has not been read. The heading skeleton is
  deliberately generic and should be replaced by the shape of decision 0001 if that file has headings.
sources_read: >-
  read: the Claude Code session output of 16:58 as pasted, and CLAUDE.md as pasted at 16:42. No page opened.
---

# First, the check that decides whether this note is needed

```powershell
Get-Content docs\ERI-Standards-v0_1.md | Select-String -Pattern "phone|device|iPhone|Android" -Context 2,2
```

If the phone rule is in the fixed rules of §1, the change needs Marvin's agreement and probably a note anyway, because
fixed rules do not move without a decision. If it is a default in §2, the note is required by his own process. If it is in
neither place, the change to the instructions file stands on its own and the note is unnecessary.

# The note, if it is needed

File: `docs/decisions/0002-what-done-means.md`. Use the next free number; if 0002 is taken, take the next one.

```markdown
# 0002: What done means, for device requirements and for the rest

**Status:** proposed, for review
**Date:** 20 November 2026
**Decided by:** Marvin Percival, wording his own, proposed in the message of 4:51 PM

## What it said before

A requirement was done only when its acceptance criterion had been observed on the Android phone and the iPhone, and a
pass on a laptop was not a pass.

## What it says now

A requirement whose acceptance criterion involves a screen or a device feature is done only when it has been observed on
both the Android phone and the iPhone. Every other requirement is done when its automated tests pass.

## Why

Cycle one is ten requirements: the event table, the revoke grant, three adapters, the sample path and the postcode format
check. Most of them have no screen and no device feature. Under the old sentence none of them could ever be finished, so
the build would have stalled on its first commit for a reason that had nothing to do with whether the work was correct.

## What this trades away

A requirement is now closed on evidence nobody looked at on a phone. That is acceptable only because every pull request
needs the other person's approval, so a test cannot be accepted by the person who wrote it. If that approval rule ever
lapses, this decision should lapse with it.

## What it does not change

Nothing about the device requirements. Anything a person sees or touches, screens, camera, microphone, location, install
and the QR scan, is still proven on both handsets before it counts. A laptop pass still counts for nothing there.

## Evidence

The wording is Marvin's own, from his message of 4:51 PM on 20 November, and it was accepted without amendment.
```

# Where it goes

Same branch, `docs/done-definition`, so it arrives with the change it explains rather than as a second pull request
arguing with the first.
