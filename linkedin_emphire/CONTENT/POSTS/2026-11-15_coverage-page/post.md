---
deliverable: post
id: 2026-11-15_coverage-page
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 08:41 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: public
status: ready
approved: no
warm: no
template: T1
first_comment: FIRST_COMMENT.md
headline: 168 ways an AI agent can fail. My reports name the ones I did not test.
headline_alt: "A coverage claim without a count is a sales document."
headline_alt2: Ask what was not tested, then ask why.
subheadline: "51 core classes, and a reason written next to every skip."
box: named, not hidden
box_alt: coverage, counted
hashtags: "#AIRedTeam #AIEngineering #AISecurity #LLMEvaluation"
visual_link: https://drive.google.com/file/d/1x2v1M5tUXee0frysKgs7rA5Knt18du_z/view?usp=drivesdk ASSETS/brand/make_card.sh
visual_note: 1080x1350 branded card, his photo and his name on the image, rendered from ASSETS/brand/make_card.sh
premise_checked: >-
  checked: the counts were computed from the repository's own checklist file on 15 November 2026, not remembered. It
  holds 168 classes across six categories, split 51 core, 93 standard and 24 extended, and the core split by category
  is 14 measurement, 13 agents, 10 governance, 6 model, 5 output and 3 retrieval. The coverage rule quoted in the post
  is the one written in the playbook README: no skipped class without a reason. The other two failure modes named in
  the post are the README's own two, in its own order.
sources_read: >-
  read: the checklist JSON and CSV in the playbook repository, the README overview and coverage sections. No page was
  opened for this post and no link sits in the body; the playbook link belongs in the first comment, as it does on
  every post until the repository reaches a thousand stars.
profile_checked: >-
  Nobody is named and nothing is quoted from a private thread. The post is about the tool's own stated limits, which is
  the one authority a buyer can check without trusting the author.
---

## Post, paste this

<!-- gate:body:start -->
168 ways an AI agent can fail. My reports name the ones I did not test.

A report that lists what it tested and stays quiet about the rest reads as though the rest was checked. That is the failure the whole checklist is built against.

The list I work from holds 168 classes across six areas. 51 of them are core, the ones I want an answer on before anything ships. The other 117 are standard and extended, and they get named in the scope even when nobody is paying for them this month.

So coverage reads as a count, not an adjective: this many core classes, this many run, this many skipped, and a reason written next to every skip. The rule in the repository is that no class can be skipped without one. A skip with a reason is a decision the buyer made in the room. A skip with no reason is what they find out at the incident review.

Two other ways these engagements fail, and I have been on the wrong side of both. A finding nobody can reproduce, because the model revision moved and nobody wrote the date. A rate with no denominator, three successes quoted as a percentage from a single run.

So the question to ask anyone selling you a red team is short. What did you not test, and why.

If the answer takes longer than the findings, you bought a document.

#AIRedTeam #AIEngineering #AISecurity #LLMEvaluation
<!-- gate:body:end -->
