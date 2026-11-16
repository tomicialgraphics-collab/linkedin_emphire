---
deliverable: dm
id: 2026-11-16_dm_behar-the-rerun-checklist
date: 2026-11-16
audience: direct
status: ready
approved: no
warm: yes
time_checked: >-
  checked: 2026-11-16 22:38 WAT, read from the system clock before this file was written.
profile_checked: >-
  Behar Dalipi, whose message of 10:12 PM confirms that the documentation point is addressed, that the wording now
  limits unchanged to the append attempt after recovery, that f25 captures both steps, that a separate recovery status
  can be considered in a future revision, and that he has received M1f with the independent rerun still to go before
  final confirmation.
premise: >-
  Nothing is waiting on this side, so the reply does one useful thing: it puts every value the rerun needs in the
  message so he does not have to open the readme or the pack to find them, and it takes his future-revision point
  without expanding it.
sources_read: >-
  read: his 10:12 PM message, CLIENTS/hfb/2026-11-16_m1f-pack/03-this-change/revision.txt, regressions.log (22 modes),
  f25.log and suite-verify.log. Every figure in the reply is copied from those files, which were produced on this tree
  on 16 November.
premise_checked: >-
  checked: the file hashes are read from the pack's revision file, the mode count from the count of mode lines in
  regressions.log, and the verdict line verbatim from suite-verify.log. The forty-four bytes, 341 to 297 and the
  unchanged reply are from f25.log as printed. Nothing is quoted from memory where a file could be read.
---

## DM, paste this

Good. The rerun is the only thing left, so here's everything it needs in one place.

Zip sha256 52f2d5bf8d5ba46060e25581971cb518033e5bc5d525fe0143df6104bbea0e63, md5 746c78d865a8735d4d9e93d0d9d65af2, seventeen files.

After unpacking, three commands from the root: python3 audit/regressions.py, then the runner and then the verifier, the two scripts sitting beside the audit folder.

What you should see from the first is 22 modes, 22 caught, 0 missed, and from the last a verdict line reading every check holds. f25 prints as a genuinely torn line quarantined by recovery, then a retry that fails at open, and its case line carries forty-four bytes, 341 to 297, gap None, and the retry refused with disk_state unchanged.

Three files to hash: bench/store.py should come out at 0989c8db, audit/regressions.py at 490de706 and audit/README.md at ae147a28. The patch is 27b0c47b, 337 lines.

On the separate recovery status, agreed, it belongs in a future revision. It's a change to a reply you've just certified, so it should arrive as its own change rather than inside a documentation pass, and f25 would then assert the new field instead of the silence it pins now.

If a figure differs at your end, send me the value and the line it came from and I'll chase it rather than explain it.

## Why the values and not a restatement

He has already agreed the substance, so a reply that re-argues the scope spends his attention on a point he settled twenty-six minutes ago. What stands between this and a merge is a rerun, and a rerun fails for boring reasons: the wrong zip, a stale tree, a mode count read from an older log.

So the reply is a checklist. It carries the artefact hashes, the three commands in order, the four expected values and the file hashes to compare. If he runs it and everything matches, he merges without another exchange. If something differs, the difference is named rather than negotiated.

## Why the future revision is agreed with briefly

He raised it as a possibility, not a request, so the reply treats it as one and says the only thing that matters about it: it changes a reply shape he has just certified, which makes it a change with its own review rather than a paragraph added to a documentation pass.

It also names what that revision would do to f25. The mode currently pins the silence around recovery. If a separate status appears in the reply, f25 has to pin the new field instead, which is a rewrite of the assertion rather than an addition to it. Saying that now stops the revision being scoped as a wording change later.

## What this is not

No deadline, no pressure and no second offer. He has said the rerun is the remaining step, which is a statement about his process, and the reply leaves the timing with him.

No thanks. He confirmed a document, and gratitude for a confirmed document reads as anxiety about the merge.

## If he reruns and it passes

Then the next message is about what comes after the merge, not about this. The pilot conversation is the one to have, and it should open with what he wants tested rather than with what the packages cost.
