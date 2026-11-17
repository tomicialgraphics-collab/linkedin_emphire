---
deliverable: post
id: 2026-11-17_limit-line
date: 2026-11-17
audience: public
status: ready
approved: no
template: T1
visual_link: https://drive.google.com/file/d/1nTX5Rw5E851g0MWLOTKL5r6qRcmV9kSf/view
headline: A check that passes on every version of a system has stopped identifying anything.
subheadline: Twenty-two modes caught, none missed, and the line that mattered named what the run could not tell apart.
headline_alt: >-
  A verification report with no limit section is a sales document.
headline_alt2: >-
  The defect in my last delivery was not code. It was a sentence claiming more than the run showed.
box: LIMITS FIRST
box_alt: THE LIMIT LINE
hashtags: ["#AIEvaluation", "#AIEvals", "#AIGovernance", "#SoftwareEngineering"]
time_checked: >-
  checked: 2026-11-17 19:08 WAT, read from the system clock before this file was written.
profile_checked: >-
  Own post. Written for the technical reviewer who will open the artefacts rather than the reader who will take the
  summary, because that reviewer is the one who decides whether a review is worth paying for.
premise_checked: >-
  checked: every figure comes from the runs recorded in this workspace today. Twenty-two modes, twenty-two caught, none
  missed on the rebuilt tree, and the verdict line from the verification pass. The invariance claim is measured, not
  inferred: the one check returns byte-identical output on three consecutive trees, 44 bytes quarantined, 341 cut to
  297, no gap, and the three logs hash to the same value. No client is named and no claim is made about their systems.
sources_read: >-
  read: the correction note, the three f25 run logs and the verification output in the current pack. No page opened, no
  external source used, so nothing here depends on a link a reader cannot check.
---

## Post, paste as this

<!-- gate:body:start -->
A check that passes on every version of a system has stopped identifying anything.

The engineer reviewing my last delivery found the same class of defect twice. Neither one was code. Both were sentences claiming more than the run had shown.

A note said a test could identify which revision produced a log. It can't. Run against three consecutive trees, that check returns byte-identical output every time: the same 44 bytes quarantined, the same 341 bytes cut to 297, the same absent gap, all three logs hashing to the same value. What that shows is stable behaviour. What it separates is nothing.

That isn't a flaw in the test. It's the limit of the instrument, and a limit belongs beside the number it qualifies, not in an appendix and not in a reply after somebody asks.

Twenty-two modes ran on the rebuilt tree, twenty-two caught, none missed, and the verdict says every check holds. All true, and none of it is the useful part. What's useful is the line naming which of those twenty-two can't tell two versions apart.

A report with no limit section is a sales document. The technical reviewer on the other side will find those limits anyway, and they'll find them faster than I did. What separates a report from a claim is who names them first.

So the register closes an item when the fix is verified rather than when it's promised, and a report holds its own claims to the same standard. That's the whole method, and it's dull on purpose.

#AIEvaluation #AIEvals #AIGovernance #SoftwareEngineering
<!-- gate:body:end -->

## First comment, post it yourself within twenty minutes

The register and the code are public, and the open count is in the readme rather than in the sales line: github.com/Teamthy/Ai-Red-Team-Playbook

Start with the class list if you only open one file. It is the part people argue with, and the arguments are the useful ones.

## Why this one now

Two corrections went out on this pack in eighteen hours, both found by the person receiving it, and both about the same thing: a document claiming more than the run behind it supports. That is a post about method with the evidence still warm, which is the only kind worth writing.

## The line being tested

The claim under the headline is that invariance and coverage are different properties. Twenty-two modes catching twenty-two failures is coverage. One of those twenty-two returning identical output across three revisions is invariance, and it means the mode documents behaviour without separating any of the versions it ran against. Confusing the two is how a suite ends up described as identifying a build.

## What not to say

No mention of the client, the merge, the rerun or the pack hashes. No claim that any of this was endorsed. The post stands on the domain, and the artefacts are public enough for a sceptical reader to open.
