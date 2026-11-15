---
deliverable: doc
id: 2026-11-15_upwork-portfolio-hfb
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 11:29 WAT, read from the system clock before this file was opened for gate.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: the owner is in the Add a new portfolio project modal and asked to publish the HFB pack as the fifth item. The
  modal's own limits are 600 characters of description, five skills, and a project title under 70 characters. Before the copy, one thing has to be said: the
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

**Project title**, 58 of the 70 allowed. The 77-character version was rejected by the form at 11:22 WAT.

```
Reproducible AI agent failure benchmark, hashed and pinned
```

Two alternates if that reads wrong, both inside the limit: `Agent failure benchmark: pinned, hashed, rerunnable` at 51
characters, and `Hashed failure benchmark for AI agents, rerunnable` at 50.

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

## The content block, built and ready

Four files sit in `UPWORK/PORTFOLIO/hfb-item/`. All are 1600px wide except the cover, and all carry his name and a
small portrait.

| file | size | what it shows |
|---|---|---|
| `01_manifest.png` | 1600x955 | `05-SHA256SUMS.txt` in full, with the "prove the file tested is the file delivered" line, 24 files, 36,215 bytes, rebuilt twice |
| `02_structure.png` | 1600x550 | the numbered pack layout, read as a process rather than a claim |
| `03_classification-log.png` | 1600x1036 | the log's opening, the aligned table of checks, and "every check holds" at both revisions |
| `04_cover.png` | 1080x1350 | the brand card for the portfolio grid, name and portrait on the template |

Upload order is 01, 02, 03, then the cover last, because a buyer who clicks reads the evidence first and the poster last.

The cover carries a follow pill from the brand template reading `Follow @Olusanya Timothy`. On an Upwork portfolio that
reads as a social card, so it can be rebuilt without the pill in one command if he wants it.

## Leave blank

`Related Upwork job` stays empty. Pointing a portfolio item at a job he did not win gives a client a reason to check.

## After saving

The item renders as the fifth. Reload the profile logged out and confirm it appears above or below the sample findings
report, since order on the portfolio strip is the order clients read. If it lands fifth of five, that is fine: the
checklist and the sample report are the two that carry a stranger to the third.

Then the last structural item is the video, and after that the profile stops being the bottleneck.
