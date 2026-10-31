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
