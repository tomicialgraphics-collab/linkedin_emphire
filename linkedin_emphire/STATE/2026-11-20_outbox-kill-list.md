---
deliverable: internal
id: 2026-11-20_outbox-kill-list
date: 2026-11-20
audience: internal
status: draft
approved: no
title: The outbox over seven days old, sorted into send, kill and ask, for the owner to approve
time_checked: >-
  checked: 2026-11-20 22:19 WAT, read from the system clock in the sandbox before this file was written.
sources_read: >-
  read: `pipeline.py outbox` at 22:19 WAT on 20 November, the activity feed the owner pasted the same day, open loops
  L11, L70 and L73, and STATE/REVENUE-LOG.md. No page opened.
---

# Outbox kill list, 20 November

What this is: the 132 files that are gated, unsent on paper and more than seven days old, each put in one group with
the evidence for it. Who it is for: the owner, to approve or correct by group. What to do next: answer the two questions
in group 6, say yes or no to each group, and nothing is changed until then.

A delivery log row does not prove a send in this repository: rows are often written when a draft is gated. So the
evidence used here is the live feed, the open loops and the replies that came back.

| Group | Files | Proposed action | Evidence |
| --- | --- | --- | --- |
| 1. Posts that went live | 5 | mark posted | the headline is on the feed you pasted on 20 Nov |
| 2. Posts that went live in other words | 2 | mark posted, once you confirm | a post on the same subject is on the feed with a different first line |
| 3. Posts that never went out | 3 | kill | overtaken, or never on the feed |
| 4. Messages that were answered | 11 | mark sent | the person replied to them, so they went |
| 5. Comments and thread replies, 8 to 14 days old | 110 | close as aged | a comment on a week-old post reaches nobody; whether each went is not recorded |
| 6. Not sure | 2 | your answer | below |


## 1. Posts that went live, mark posted

- `VERIFIED_POSTS/2026-11-12_whose-clock/post.md`
- `VERIFIED_POSTS/2026-11-12_nvidia-readable-record/post.md`
- `VERIFIED_POSTS/2026-11-09_span-boundary-scoring/post.md`
- `VERIFIED_POSTS/2026-11-08_eval-case-argument/post.md`
- `VERIFIED_POSTS/2026-11-06_absence-of-a-record/post.md`

## 2. Posts that went live in other words, mark posted once confirmed

- `VERIFIED_POSTS/2026-11-09_red-team-playbook-launch/post.md`: the playbook launch went out as 'I published the checklist I use for AI red teaming. 168 classes.'
- `VERIFIED_POSTS/2026-11-08_refusal-record/post.md`: two refusal posts went out as 'Ask your agent for something it is not allowed to do'

## 3. Posts that never went out, kill

- `VERIFIED_POSTS/2026-11-12_two-jobs-one-person/post.md`: overtaken by the Nvidia post that went out the same day, 2026-11-12_nvidia-readable-record
- `VERIFIED_POSTS/2026-11-09_foray-review-receipt/post.md`: overtaken by the case study launch post, 2026-11-13_seven-corrections
- `VERIFIED_POSTS/2026-11-07_twelve-swings/post.md`: never went out, and thirteen days old

## 4. Messages that were answered, mark sent

- `ENGAGEMENT/dm_2026-11-09_martina-brazelton.md`: Martina, round one
- `ENGAGEMENT/2026-11-10_reply_martina-brazelton-issuer-out-of-the-loop.md`: Martina, round two
- `ENGAGEMENT/2026-11-12_reply_martina-brazelton-observing-the-shift.md`: Martina, round three (delivery log)
- `ENGAGEMENT/2026-11-12_reply_martina-brazelton-what-im-working-on.md`: Martina, round four, sent per L73
- `ENGAGEMENT/2026-11-12_reply_sebastien-favre-evidence-a-second-reader-can-check.md`: Sébastien, answered before his 13 Nov decline
- `OUTREACH/evelyne-claudia-2026-11-06/ARTIFACT-MANIFEST-v3-v2.md`: Evelyne-Claudia, delivered before she closed the correspondence on 10 Nov (L70)
- `OUTREACH/evelyne-claudia-2026-11-06/HASH-RECOMPUTATION-2026-11-09.md`: Evelyne-Claudia, delivered before she closed the correspondence on 10 Nov (L70)
- `OUTREACH/evelyne-claudia-2026-11-06/F9b-CORRECTION-03.md`: Evelyne-Claudia, delivered before she closed the correspondence on 10 Nov (L70)
- `OUTREACH/evelyne-claudia-2026-11-06/F9b-CORRECTION-02.md`: Evelyne-Claudia, delivered before she closed the correspondence on 10 Nov (L70)
- `OUTREACH/evelyne-claudia-2026-11-06/F9b-CORRECTION-04.md`: Evelyne-Claudia, delivered before she closed the correspondence on 10 Nov (L70)
- `OUTREACH/evelyne-claudia-2026-11-06/F9b-refusal-pair-EXPECTATION.md`: Evelyne-Claudia, delivered before she closed the correspondence on 10 Nov (L70)

## 5. Comments and thread replies, close as aged

The reason written on each: 'aged out at 8 days or more; whether it was posted is not recorded here.' That is true either way, so the group can be closed without checking each one on LinkedIn.

- `ENGAGEMENT/2026-11-06_comment-round_feed-sweep-2.md`
- `ENGAGEMENT/2026-11-06_comment_ai-news-world-altman.md`
- `ENGAGEMENT/2026-11-06_comment_hitesh-choudhary.md`
- `ENGAGEMENT/2026-11-06_comment_soubhik-ghosh.md`
- `ENGAGEMENT/2026-11-06_comment_stephen-klein.md`
- `ENGAGEMENT/2026-11-06_comment_taha-hussain.md`
- `ENGAGEMENT/2026-11-06_reply_brad-wolfe.md`
- `ENGAGEMENT/2026-11-07_comment_christopher-story.md`
- `ENGAGEMENT/2026-11-07_comment_eduardo-ordax-airbnb-agent-workflows.md`
- `ENGAGEMENT/2026-11-07_comment_guillermo-flor.md`
- `ENGAGEMENT/2026-11-07_comment_luis-roquette-multi-agent.md`
- `ENGAGEMENT/2026-11-07_comment_marin-ivezic-quantum-finance-pqc.md`
- `ENGAGEMENT/2026-11-07_comment_paolo-caressa-devfest-judge.md`
- `ENGAGEMENT/2026-11-07_comment_paolo-perrone-agent-budget.md`
- `ENGAGEMENT/2026-11-07_comment_ricky-jones-round-table.md`
- `ENGAGEMENT/2026-11-07_comment_rock-lambros-agent-blinded-security.md`
- `ENGAGEMENT/2026-11-07_comment_shawn-bullock.md`
- `ENGAGEMENT/2026-11-07_comment_vallikat-peethamber-vector-state.md`
- `ENGAGEMENT/2026-11-07_reply_brad-wolfe_own-post.md`
- `ENGAGEMENT/2026-11-08_comment-shalini-goyal-bola-gap.md`
- `ENGAGEMENT/2026-11-08_comment_adi-rashkes-queen-of-hearts-vishing-ctf.md`
- `ENGAGEMENT/2026-11-08_comment_aiswarya-venkitesh-diwali.md`
- `ENGAGEMENT/2026-11-08_comment_ananya-ghosh-chowdhury-diwali.md`
- `ENGAGEMENT/2026-11-08_comment_andreas-horn-access-lives-in-people.md`
- `ENGAGEMENT/2026-11-08_comment_artur-walisko-self-verification.md`
- `ENGAGEMENT/2026-11-08_comment_ben-li-agent-eval-ownership.md`
- `ENGAGEMENT/2026-11-08_comment_brandon-crimmins-refusal-seam.md`
- `ENGAGEMENT/2026-11-08_comment_christopher-paradise-sara-compression.md`
- `ENGAGEMENT/2026-11-08_comment_dietrick-hardwick-history-eraser.md`
- `ENGAGEMENT/2026-11-08_comment_eaton-zveare-god-mode-border.md`
- `ENGAGEMENT/2026-11-08_comment_eva-benn-sans-dma-vote.md`
- `ENGAGEMENT/2026-11-08_comment_guillermo-flor-bubble-cables.md`
- `ENGAGEMENT/2026-11-08_comment_ilir-aliu-robot-arm-repeatability.md`
- `ENGAGEMENT/2026-11-08_comment_love-babbar-who-holds-the-switch.md`
- `ENGAGEMENT/2026-11-08_comment_marcus-chan-hand-typed-numbers.md`
- `ENGAGEMENT/2026-11-08_comment_mitko-vasilev-forward-deployed-handover.md`
- `ENGAGEMENT/2026-11-08_comment_mourad-elmaalaoui-sovereign-evaluation.md`
- `ENGAGEMENT/2026-11-08_comment_neil-mcloughlin-legacy-policy-inventory.md`
- `ENGAGEMENT/2026-11-08_comment_salman-lakhani-fallback-attribution.md`
- `ENGAGEMENT/2026-11-08_comment_shane-butler-self-serve-analytics.md`
- `ENGAGEMENT/2026-11-08_comment_soribel-feliz-nvidia-board-investigation.md`
- `ENGAGEMENT/2026-11-08_comment_thomas-roccia-volta-refusal-router.md`
- `ENGAGEMENT/2026-11-08_reply_christopher-paradise-codec-noise.md`
- `ENGAGEMENT/2026-11-08_reply_christopher-paradise-entropy-bounds.md`
- `ENGAGEMENT/2026-11-08_reply_eva-benn-vote-cast.md`
- `ENGAGEMENT/2026-11-08_reply_paolo-perrone-exit-codes.md`
- `ENGAGEMENT/2026-11-08_reply_paolo-perrone-pipe-attribution.md`
- `ENGAGEMENT/2026-11-08_reply_paul-sheals-attribution-split.md`
- `ENGAGEMENT/2026-11-08_reply_ricky-jones-round-table.md`
- `ENGAGEMENT/2026-11-09_comment_adrian-lee-sanchez-fiduciary-process.md`
- `ENGAGEMENT/2026-11-09_comment_alejandro-saucedo-pando-force-with-lease.md`
- `ENGAGEMENT/2026-11-09_comment_amjad-masad-error-text-is-input.md`
- `ENGAGEMENT/2026-11-09_comment_anthony-alcaraz-cost-per-task.md`
- `ENGAGEMENT/2026-11-09_comment_chinasa-okolo-sovereignty-over-evaluation.md`
- `ENGAGEMENT/2026-11-09_comment_damien-filiatrault-commit-and-push.md`
- `ENGAGEMENT/2026-11-09_comment_daniel-moka-loops-and-the-oracle.md`
- `ENGAGEMENT/2026-11-09_comment_divyanshi-sharma-bank-native-agent.md`
- `ENGAGEMENT/2026-11-09_comment_efi-pylarinou-read-only-and-egress.md`
- `ENGAGEMENT/2026-11-09_comment_elizabeth-rotimi-first-class.md`
- `ENGAGEMENT/2026-11-09_comment_emily-j-ai-evals-launch.md`
- `ENGAGEMENT/2026-11-09_comment_giorgio-severi-memorydojo.md`
- `ENGAGEMENT/2026-11-09_comment_hitesh-choudhary-cleanup-prompt.md`
- `ENGAGEMENT/2026-11-09_comment_juliet-ugbor-preparedness-gap.md`
- `ENGAGEMENT/2026-11-09_comment_launch-playbook-link.md`
- `ENGAGEMENT/2026-11-09_comment_martha-boeckenfeld-forestry-standard.md`
- `ENGAGEMENT/2026-11-09_comment_mostafa-dehghanpour-ratify-or-review.md`
- `ENGAGEMENT/2026-11-09_comment_olushola-olaleye-purpose-and-the-no.md`
- `ENGAGEMENT/2026-11-09_comment_sairam-sundaresan-conformal-coverage.md`
- `ENGAGEMENT/2026-11-09_comment_sam-illingworth-the-model-stays.md`
- `ENGAGEMENT/2026-11-09_comment_shreya-shankar-quail-extract.md`
- `ENGAGEMENT/2026-11-09_comment_span-scoring-playbook-link.md`
- `ENGAGEMENT/2026-11-09_comment_tanya-janca-instruction-vs-capability.md`
- `ENGAGEMENT/2026-11-09_comment_tina-austin-purple-flower.md`
- `ENGAGEMENT/2026-11-09_held_anthropic-sales-tools-repost.md`
- `ENGAGEMENT/2026-11-09_held_denis-panjuta-viktor-ad.md`
- `ENGAGEMENT/2026-11-09_reply_christian-macdonald-prompt-injection.md`
- `ENGAGEMENT/2026-11-09_reply_christian-macdonald-take-the-note.md`
- `ENGAGEMENT/2026-11-09_reply_efi-pylarinou-the-side-door.md`
- `ENGAGEMENT/2026-11-09_reply_juliet-ugbor-human-problem.md`
- `ENGAGEMENT/2026-11-09_reply_martha-boeckenfeld-long-term.md`
- `ENGAGEMENT/2026-11-09_reply_mostafa-dehghanpour-cannot-check-vs-right.md`
- `ENGAGEMENT/2026-11-09_reply_sairam-sundaresan-the-grain.md`
- `ENGAGEMENT/2026-11-09_reply_sam-illingworth-what-i-can-run.md`
- `ENGAGEMENT/2026-11-10_comment_gadi-evron-milliseconds-are-a-telemetry-claim.md`
- `ENGAGEMENT/2026-11-12_comment_allie-miller-the-answer-you-cannot-grade-later.md`
- `ENGAGEMENT/2026-11-12_comment_elena-bobkova-the-credentials-nobody-owns.md`
- `ENGAGEMENT/2026-11-12_comment_eva-benn-outcome-with-no-cause.md`
- `ENGAGEMENT/2026-11-12_comment_hayete-gallot-what-you-can-answer-before-the-advisory.md`
- `ENGAGEMENT/2026-11-12_comment_jerry-liu-absent-field-and-citation-gap.md`
- `ENGAGEMENT/2026-11-12_comment_jerry-liu-one-change-at-a-time.md`
- `ENGAGEMENT/2026-11-12_comment_jess-ramos-what-his-access-touched.md`
- `ENGAGEMENT/2026-11-12_comment_karan-dwivedi-who-gets-paged.md`
- `ENGAGEMENT/2026-11-12_comment_kunwoo-kim-ai-workflow-award.md`
- `ENGAGEMENT/2026-11-12_comment_love-babbar-authority-to-refuse.md`
- `ENGAGEMENT/2026-11-12_comment_marin-ivezic-the-tail-is-the-untimestamped-check.md`
- `ENGAGEMENT/2026-11-12_comment_ricky-jones-the-run-beside-it.md`
- `ENGAGEMENT/2026-11-12_comment_rock-lambros-the-version-string-lied.md`
- `ENGAGEMENT/2026-11-12_comment_rock-lambros-verdict-and-effect.md`
- `ENGAGEMENT/2026-11-12_comment_sam-illingworth-the-missing-sentence.md`
- `ENGAGEMENT/2026-11-12_comment_sara-hooker-holdout-outside-the-expansion.md`
- `ENGAGEMENT/2026-11-12_comment_stephen-klein-no-mechanism-for-it.md`
- `ENGAGEMENT/2026-11-12_comment_stephen-platten-the-next-hour.md`
- `ENGAGEMENT/2026-11-12_comment_tolulope-michael-test-one-control.md`
- `ENGAGEMENT/2026-11-12_reply_elena-bobkova-who-holds-the-list.md`
- `ENGAGEMENT/2026-11-12_reply_rock-lambros-rotate-wider-than-the-evidence.md`
- `ENGAGEMENT/2026-11-12_reply_tim-zlomke-age-rather-than-change.md`
- `ENGAGEMENT/2026-11-12_reply_tim-zlomke-margin-against-skew.md`
- `ENGAGEMENT/2026-11-12_reply_tim-zlomke-score-the-refusal-not-the-outcome.md`
- `ENGAGEMENT/dm_2026-11-09_martina-brazelton.md`
- `VERIFIED_POSTS/2026-11-08_refusal-record/FIRST-COMMENT.md`

## 6. Not sure, your answer

- `ENGAGEMENT/2026-11-12_reply_martina-brazelton-who-can-act-on-it.md`: a fifth Martina reply written the same day as round four; sent, or overtaken by it?
- `CLIENTS/foray-dunin7/FINDINGS-02-register-addendum-v8.md`: register addendum v8 for Marvin; the FORAY review closed on 10 Nov and C1 cleared on 12 Nov. Sent, or overtaken?

## What runs once approved

Each group uses the outbox commands, so every file keeps its history and gets a dated reason:

    pipeline.py outbox sent <file> --to "<name>" --how "confirmed from the feed or the reply, 20 Nov"
    pipeline.py outbox kill <file> --why "<the reason above>"

Posts in groups 1 and 2 are marked posted rather than sent. Nothing is deleted.

