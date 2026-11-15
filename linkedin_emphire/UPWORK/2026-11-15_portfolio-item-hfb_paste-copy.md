---
deliverable: doc
id: 2026-11-15_upwork-portfolio-hfb
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 11:20 WAT, read from the system clock before this file was opened for gate.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: the owner is in the Add a new portfolio project modal and asked to publish the HFB pack as the fifth item. The
  modal's own limits are 600 characters of description and five skills. Before the copy, one thing has to be said: the
  pack was built for Behar and delivered to him, so the filed version of it is his until he says otherwise.
sources_read: >-
  read: the modal screenshot at 11:20 WAT, CLIENTS/hfb/2026-11-14_m1-pack/ contents, and the 15 November delivery
  message to Behar carrying the zip hash and file count.
---

# Before you paste: whose pack is it

The M1 pack was built for Behar Dalipi and delivered to him on 15 November with its hash. Upwork portfolio files are
public to anyone who visits the profile. Publishing his benchmark, his environment and his baseline failure as a public
download is a decision he has not been asked about, and one message to him settles it.

So there are two versions below. **Variant A publishes now** and describes the work without shipping his files.
**Variant B publishes the pack itself** and needs one reply from Behar first.

## Variant A, publish now. 547 of 600 characters

**Project title**

```
Host-failure benchmark: reproducible AI agent failures, hashed and rerunnable
```

**Your role**

```
Design, build and verification
```

**Project description**, 547 characters.

```
An AI agent failed in production and nobody could say whether it was the model, the prompt or the storage layer.

I built a benchmark pack that isolates it: one pinned revision, a baseline that reproduces in one command, a recorded change, and a classification log naming which layer broke.

Failures are quarantined to a byte range, so a rerun reproduces them exactly or reports something different, and that difference is the finding. A SHA-256 manifest proves the file tested is the file delivered.

Rerun scripts included. Full pack under NDA.
```

## Variant B, only after Behar says yes. 523 of 600 characters

**Project description**, 523 characters.

```
An AI agent failed in production and nobody could say whether it was the model, the prompt or the storage layer.

I built a benchmark pack that isolates it: one pinned revision, a baseline that reproduces in one command, a recorded change, and a classification log naming which layer broke.

Failures are quarantined to a byte range, so a rerun reproduces them exactly or reports a difference, and that difference is the finding.

Built twice, hashed twice, both e997029d. 24 files, 36 KB. Rebuild and rerun scripts inside.
```

Then attach the zip as content, and put the full `sha256` in the description only if the 600 limit allows, otherwise in
the first line of the attached README, which already carries it.

## Skills and deliverables, five slots

```
AI Security
AI Agent Development
Evaluation Harness Design
Python
Test Automation
```

If `Test Automation` is not offered, use `Automated Testing`, then `Technical Writing`.

## The content block, in this order

**1. The manifest, as a screenshot.** `05-SHA256SUMS.txt` open in an editor, showing the commit hash and both file
hashes for `bench/store.py`. This is the single most persuasive image available, because almost nobody else on the
platform can show a verifiable artifact at all.

**2. The folder tree, as a screenshot.** The numbered files from `00-README.md` through `05-SHA256SUMS.txt`. It reads as
a process rather than a claim.

**3. The classification log, as a screenshot.** `04-classification-log.md`, one page. This is the four-part findings
format that the overview promises, shown rather than described.

For all three: remove the client's name, any repository URL, and any path containing his organisation if one appears.
Variant A promises the pack under NDA, so nothing sensitive needs to be in the images.

**Optional fourth: a cover card.** The repo has the card script at `CONTENT/POSTS/2026-11-15_coverage-page/`, 1080x1350,
his palette, his name and photo. A cover helps the grid and adds nothing a client cannot get from the screenshots, so
treat it as last.

## Leave blank

`Related Upwork job` stays empty. Pointing a portfolio item at a job he did not win gives a client a reason to check.

## After saving

The item renders as the fifth. Reload the profile logged out and confirm it appears above or below the sample findings
report, since order on the portfolio strip is the order clients read. If it lands fifth of five, that is fine: the
checklist and the sample report are the two that carry a stranger to the third.

Then the last structural item is the video, and after that the profile stops being the bottleneck.
