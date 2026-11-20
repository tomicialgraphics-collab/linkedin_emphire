---
deliverable: comment
id: 2026-11-08_thomas-roccia-volta-refusal-router
date: 2026-11-08
audience: public
status: ready
approved: no
warm: yes
profile_checked: 2026-11-08. LinkedIn profile fetch returns 403, so read from his GitHub, X and conference bios instead. Thomas Roccia, threat researcher and founder of SecurityBreak, creator of the Unprotect Project (malware evasion database, open since 2015), creator of NOVA (prompt pattern hunting for LLM abuse, SANS Difference Makers Award), creator of PromptIntel with the Indicators of Prompt Compromise taxonomy, author of Visual Threat Intelligence, ex-Microsoft and ex-McAfee, trains at Black Hat and DEF CON, now publishing as founder, author, speaker in AI threat intelligence.
thread: his post on the Talos analysis of VOLTA, which sends a stolen-data bundle to a model through OpenRouter and asks for a dossier ranking the victim's assets by monetisation value and grading their opsec
verified: Talos blog 2026-10-31 and two independent write-ups agree on the mechanics used below. The refusal check looks for phrases like "I can't" or "I'm not able" before moving down a chain of up to three models, default anthropic/claude-opus-4.6, then moonshotai/kimi-k2, then google/gemini-2.5-flash, temperature 0.2. The inference round trip runs on the victim's machine over the victim's own connection, only the result is exfiltrated. Talos does not establish whether any model complied or refused.
---

# Comment on Thomas Roccia's VOLTA post, 8 November 2026

## Why this one

Roccia is the person in this feed whose work is closest to the argument the account has been making all week: prompts as
indicators, adversarial use of models, the evidence that survives an operation. His post is a short pointer to his own
Talos reading plus the PromptIntel entry, so there is room to add a distinction rather than agree.

The comment takes the one mechanism in the report that is easy to skim past, the refusal check, and shows that it is
doing routing rather than control. That is a threat intel point and it is also the same point in a different costume as
the refusal-record post from earlier today, without saying so.

## Comment

The part worth sitting with is the refusal handling. The code string-matches "I can't" or "I'm not able" and walks down
the chain, which turns a refusal into a routing decision rather than a control.

Two consequences. The operator only ever learns that the appraisal failed, never why, so a refusal and an empty response
look the same from inside the operation. And the fallback order is a live measurement of which guardrails held against
one very specific request, recorded by someone with no reason to flatter any vendor.

Talos doesn't say whether any model in the chain complied. The only party who could answer is the reseller in the middle.

## Two beats held for a reply

If he engages, the second observation is that the prompt asks for an auditable trail of citations, so the operator wants
to check the model's work before pricing a person. Attacker-side evidence discipline is not the story anyone is telling
about this sample.

The third is the local debug log, which records whether the model call succeeded. The operator built a fault-trace into
the tool because the model was a component that could fail. That is the same lesson defenders keep failing to learn
about their own agents, arriving from the other side.

## Facts held back

No claim about whether any provider blocked the requests, because Talos does not establish it and the write-ups that
imply it are inferring. No speculation about the operator, the builder sales, or the victim count. Nothing about the
sample hash or the archive names, which are his material, not mine to restate.
