---
deliverable: doc
id: 2026-11-13_upwork-four-archetype-proposals
date: 2026-11-13
audience: internal
status: ready
approved: no
---

# Four proposals, one per archetype

Copy the block, replace the bracketed parts, delete nothing else. Each is under 120 words because the first screen of a
proposal is all most clients read, and a long one gets skimmed rather than answered.

Rules that apply to all four: no external links, no contact details, no price without a scope attached, one attachment
maximum, and the first sentence mirrors the client's own words so they know it is not a template.

## A. Pre-launch test, quote $600 Standard

```
You are shipping [the feature] in [their date] and want it broken before a user finds it.

That is the work I do: prompt injection, RAG poisoning, tool-call abuse and policy bypass, run against your system in a
workspace, with nothing shared or published without your written permission.

Standard is $600: the full four-layer test in 7 days, and every finding in four parts, exact repro, which layer failed,
the fix, and how I verified the fix holds. I can attach a sample findings report from my own production chatbot so you can
see the format before you buy.

One question: is the feature live to any users today, or is there a staging copy I can test without touching production?
```

## B. Something already went wrong, quote $600 scan plus findings

```
[Their exact sentence about what happened]. That is a reportable finding, not a bug ticket, and it is worth knowing how
many other paths reach the same place.

I run a scan in 3 days for $450, then the full four-layer test at $600 if the scan shows breadth. Every attempt is logged
exactly as run, including the ones that fail, and you get the repro so your engineer can confirm it without me.

I can send a sample findings report from my own chatbot, where four of six attempts worked, including a fabricated refund
from a single trigger word.

Question: is [the behaviour] reachable by a logged-in user only, or by anyone who can type into the chat?
```

## C. Build with testing inside, quote $900 or $2,500

```
You want [the build] and you want it to survive real users. I build it and then I break it, which is why the test plan is
not a separate purchase.

Standard at $900 is the build with RAG over your data, the tool calls it needs, and a regression suite that keeps a closed
hole closed on the next deploy. Advanced at $2,500 adds the full red team pass before launch and a written hardening
report you can hand to a client.

Question: what does the agent need to read, and what is it allowed to do on its own without a human confirming?
```

## D. Compliance or governance review, quote $1,500 Advanced

```
You need a document that says what was tested, what failed, how the defect was closed and how the closure was verified. That is the
format I already write in, and it maps onto [SOC 2 / GDPR / their framework] evidence requests without translation.

Advanced is $1,500: the four-layer test across prompt injection, retrieval integrity, tool-call abuse and policy bypass,
plus code-level fixes scoped, plus the regression suite, delivered in 14 days. The case study I can attach is a named
review of another team's tool with seven corrections in it, including the ones that were mine.

Question: which control is the audit actually asking you to evidence first?
```

## When a client replies and goes quiet

One follow-up, five days later, one sentence, no re-pitch:

```
Still happy to run this. If the timing moved, tell me when it lands and I will keep the scope where it is.
```

After that, the row goes to `lost` in the register and the connects are gone. Chasing a third time is how an account gets
remembered badly.

## What never goes in a proposal

- "I am the best fit for this role", because every proposal says it.
- A list of technologies with no job attached to each one.
- A discount offered before they ask.
- Any mention of Upwork's fees, other clients' names, or a comparison to another platform.
- A number with no method behind it. The case study exists precisely because every figure in it can be re-run.
