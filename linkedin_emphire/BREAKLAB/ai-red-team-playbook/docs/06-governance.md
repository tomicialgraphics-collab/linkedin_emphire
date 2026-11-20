# 06 Governance and practice

Covers `GV-01` to `GV-35`.

This section is not paperwork. It is the language in which the rest of the work is either funded, filed, or ignored.

## Map to the frameworks the client already reports on

You do not need to adopt a framework. You need to be able to say where a finding lands in the one the client already uses.

| Framework | What it is for in an engagement |
|---|---|
| OWASP LLM Top 10 | The vocabulary the security team files tickets in. Map every finding. |
| OWASP Agentic Security | The agent-specific categories, for tool and identity findings. |
| MITRE ATLAS | Techniques, so a finding joins the wider threat picture rather than standing alone. |
| NIST AI RMF | The risk language a US-facing client is likely already publishing against. |
| NIST Generative AI Profile | Concrete actions, useful as a checklist of controls to test for. |
| ISO/IEC 42001 | Where AI management meets the information security management system that already exists. |
| EU AI Act | Which duties apply, and from when, for a client selling into the EU. |

Two cautions. First, a mapping is not an analysis: putting a finding under a framework row does not tell anyone what to do. Second, framework coverage is not security. A system can be mapped to every row and still leak its system prompt on request.

## Legal posture, honestly

Whether the EU AI Act applies to a given client depends on their role and the system's classification, and getting that wrong in either direction is expensive. Establish two facts early: is the system a general purpose model or a high risk system, and in which jurisdiction is it placed on the market. Then name the duties that follow, and say plainly that the classification is the client's to confirm with counsel. Do not offer a legal opinion; offer the technical evidence a lawyer will need.

## Rules of engagement

Written before testing, not after. `templates/engagement-scope.md`.

- Authorised targets, named individually, with the environment (production, staging, a clone).
- What you may not do: no live third parties, no real customer data, no destructive writes, no denial of service against shared infrastructure.
- The stop condition, and the named person who can invoke it, with a number that works at 2am.
- Data handling: what you will copy, where it lives, when it is deleted, and who can see the findings before the client does.
- Disclosure terms: channel, timeline, and what happens if the vendor disagrees.

## When something goes wrong

An AI incident usually looks like one of four things: a prompt leak, model abuse by a user, an exfiltration channel firing, or a tool action that should not have happened. Walk one of those as a tabletop exercise before the engagement, because the answer to "who do we call when the agent transfers money twice" is never in the runbook.

The controls that matter in that moment are the ones this playbook asks about earlier: a kill switch that reaches subagents, a step ceiling, an audit log with the tool arguments, and a rollback that includes the index and the cache.

## Human oversight, defined rather than declared

"This system has human oversight" is a claim with no content until three questions are answered:

1. What decision does the person actually make.
2. Can the person understand the basis of it, in the time available.
3. What happens when the person says no, and who can override them.

Approval fatigue is the quiet failure of all three. An approval that arrives forty times an hour is a rubber stamp, and the log will show a person who agreed, which is worse than no gate at all.

## What to write down

- The mapping table, one row per finding, in the client's framework.
- The classification facts, stated as facts, with the legal conclusion left to counsel.
- The rules of engagement, signed.
- The oversight answer to the three questions above, in the client's own words.
