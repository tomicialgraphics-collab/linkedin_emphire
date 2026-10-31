# Sources and build notes: "prompt is 0.10 percent"

## Every number, traced

All figures come from one page, fetched and read in full on 2026-10-31:
**https://cxbom.org** (the CxBOM reference session ledger), plus **https://cxbom.org/spec/**
(specification 0.3.1) for the trust-ring definitions and the caveat quoted in the post.

| Post claim | Source |
|---|---|
| 46,205 tokens of context | `contextWindowTokensUsed`, reference session (46,192 component + 13 template overhead) |
| Operator system prompt 45 tokens, 0.10% | Ledger row 1, `cc-001`, Ring 0 operator |
| Three retrieved documents 45,774 tokens, 99.1% | Ledger rows 3-5: 15,710 + 15,283 + 14,781 = 45,774, and 34.01 + 33.09 + 32.00 = 99.10% |
| Tool definition 357 tokens, 0.77% | Ledger row 2, `cc-002`, external MCP tool definition (fetch) |
| The one flagged component | Row 2 is the only row whose status is not `NOT ASSESSED`. Its status is `TRUST INVERSION` |
| "authored outside the boundary, assembled where operator content sits" | Spec 0.3.1: the Tool Definition Trust Inversion structural finding is "an externally authored ring 1 tool definition assembled with ring 0 positional authority" |
| The caveat quoted in the post | Spec 0.3.1, verbatim: "CxBOM is a design contribution. It has not been evaluated in production, and its value in incident response has not been measured against a baseline" |

## What I did NOT use

- **MCPTox** (1,348 cases, 45 servers, 72.8% o1-mini ASR). Rock's post cites it, I did not read
  the study, so no MCPTox number appears in the post. Do not add one from memory.
- The `lnkd.in` redirects in Rock's post do not resolve from this sandbox. `cxbom.org` does.

## Why "one session, not a study" is in the post

The site says it plainly: the film is a recording and "is not a rate." Publishing a single
session's proportions as if they were a measured distribution would be the exact failure this
post is about. The caveat is in the copy because it is true, and because it is the thing that
makes the number usable by someone who disagrees with you.

## Voice checks

- 262 words, inside the 250-270 band of the recent best performers (`aithos-answer-key` 269w,
  `check-never-failed` 259w).
- `voice_lint.py --profile linkedin`: 0 errors, 0 warnings. No banned phrases, no em dashes.
- One contraction, not in the first line. Ends on a statement, not a question. No hashtags,
  no arrows, no CTA question. Note that `post_templates.txt` still contains closing questions,
  arrow bullets and hashtags, all of which the 2026-10-13 standing rules disallow. Written to
  the `aithos-answer-key` shape instead.

## Build 2: TEMPLATE 1 (TECHNICAL DEEP-DIVE), owner instruction 2026-10-31

Owner asked for the post to follow `DAILY CONTENT/post_templates.txt`. Template 1 is the
only one of the 14 that fits sourced technical material, so `post.md` is now the template
build (303 words, 1,783 chars). Slot mapping, so a later session can audit it:

| Template slot | What fills it |
|---|---|
| [SPECIFIC TECHNICAL PROBLEM] | 46,205 tokens, operator prompt 45 tokens, 0.10 percent |
| "Here's what most engineers get wrong" | Treating the system prompt as the control |
| "The reality is different" | Three retrieved documents, 45,774 tokens, 99.1 percent, plus CxBOM attribution |
| [YOUR ACTUAL EXPERIENCE] | Red teaming: failures start with a pulled document or a summarised tool definition |
| "Here's what actually works" | 3 arrows: untrusted input at the boundary, hash and diff definitions, log the assembled window |
| "The part nobody tells you" | The flagged component is the tool definition at 0.77 percent. Small components carry the authority. Plus their "one session, not a study" caveat |
| [PRACTICAL TAKEAWAY] | "You can't audit a prompt that is one line in a context you didn't assemble." |
| Closing question | Whether a bad answer was traced to the window or the instruction |
| Hashtags | #AISecurity #AIEvaluation #RedTeaming |

### Where this build now diverges from the 2026-10-13 standing rules

Noted here so it is a decision and not an accident. Template 1 requires two things the
standing rules forbid:

1. **A closing question** ("What's your experience with [TOPIC]?"). The rules say end on a
   statement, and a question only in INTERACTIVE replies.
2. **Hashtags.** No post after 2026-10-13 uses them.

Both are in `post.md` because the owner asked for the library. The flat-ending version is
preserved as `post_alt_thesis-shape.md` (262 words, statement ending, no hashtags) if the
call gets reversed. Everything else still holds in both builds: no em dashes, no banned
phrases, no fabricated numbers, sourced claims only.

## Headline and subheadline (standing rule from 2026-10-31)

Owner instruction, now recorded in `context.md` §7: every daily post ships with a headline
and a subheadline, always, not on request.

**Shipped pair**

- Headline (43 chars): `You are auditing 0.10 percent of the input.`
- Subheadline (113 chars): `In a published agent context window, the operator's instruction is 45 tokens. The retrieved documents are 45,774.`

Together they take 158 characters including the break, so both lines sit above the "see
more" fold, which truncates around 200. The headline is the memorable line and carries the
thesis. The subheadline adds the evidence pair and deliberately does not restate the
headline. The body then starts at Template 1's misconception slot and no longer repeats the
45,774 figure, since the subheadline holds it.

**Alternatives considered**

1. Headline `The prompt is not the control. The arithmetic says so.` Subheadline `45 tokens
   of operator instruction against 45,774 of retrieved documents, in a vendor's own
   published ledger.` Stronger claim, softer evidence framing.
2. Headline `Nobody signs the 99 percent.` Subheadline `A published agent window, split by
   trust ring. The smallest component carries the most authority.` Best for a card or
   carousel cover, where the line has to survive being read with no body under it.

Total post: 311 words, 1,833 chars, inside the 3,000 char limit. Voice lint strict: clean.
