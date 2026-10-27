# Redacted Engagement Sample, draft template (Arcezia trust
# artifact)
Purpose: the artifact for Praveen's 10-26 ask ("one past
write-up or repo of yours"). Goal: prove shape and rigor,
strip all identity. Send: 10-28 morning, attached to the
markup-acceptance email (v3). This is a working file, not
the sent artifact. Keep the ORIGINAL report out of this
repo; fill this template on your own machine.

## THE RULE (one line)
Strip every identifier, keep every technical substance.
Recognition test: could the client, or a competitor of the
client, identify this engagement from the document? If
yes, scrub harder. If one finding cannot be made safe,
swap it for a different finding; if findings end up coming
from more than one engagement, the cover note says
"sample findings from real engagements" (plural), and the
email stays accurate.

## PAGE 1: COVER BLOCK (fill in)
- Title: Redacted Engagement Sample, AI Agent Action-Gate
  Red Team (or the closest class of the original)
- Engagement: [Month Year], external behavioral test,
  single test account, [N]-day window
- Target class: [generic class, e.g. "production LLM
  support agent with tool calling and an action gate"].
  NOT a product name, company, or domain
- Method: black-box, external, synthetic data only,
  nothing outside the test account touched
- Status: private, client confidentiality terms, NDA
- Honesty line (keep it, it is the frame): "All
  identifiers removed: company, product, people,
  endpoints, real data, real dates. What remains is the
  full technical substance: exact repro, root cause, fix,
  verification. This is the shape and rigor of the report
  for the Arcezia engagement."

## EXECUTIVE SUMMARY (five lines max)
- Scope in one line
- Attempts vs results: [N] chains tried, [X] went
  through, [Y] held, [Z] fixed and verified in the window
- Severity mix: [n] unauthorized action / [n] data
  exposure / [n] privilege escalation
- The one-line theme: what the gate actually relied on
- Close: the report covers holds as well as hits

## FINDINGS (5 to 7, strongest first)
Per finding, the same four-part format the Arcezia report
uses:
### Finding [k]: [title] ([severity class], [status])
- Exact repro: [the actual request or prompt as sent,
  UTC timestamps, all data values synthetic]
- Which layer failed: [root-cause class, one or two
  sentences]
- Fix: [what the target owner changed]
- Verified: [re-run: same prompt plus [N] variants,
  result, UTC]
Selection guidance: the set must include at least (a) one
indirect or multi-step chain, (b) one unauthorized-action
or privilege-escalation class, (c) one held finding with
the reason it held.

## HOLDS (first-class section, not an afterthought)
For each hold: the chain tried, what stopped it, and why.
This is the section an action-gate owner reads first, and
it mirrors the Arcezia scope ("covers holds as well as
hits").

## FIX AND VERIFY LOOP (at least one, shown in full)
Finding, target owner fix, tester re-run inside the
window, confirmed hold. This demonstrates the "you fix, I
verify" contract from a past engagement, which is the
exact contract the Arcezia scope runs on.

## SCOPE NOTE (one short paragraph)
Each engagement runs on its own written scope, agreed in
writing before keys. This sample reflects the scope that
was agreed for that engagement. (Keeps the sample from
reading as a promise about what the Arcezia window
covers, his six markups define that.)

## REDACTION PASS (run line by line, then again after
## any edit)
STRIP (search the draft for each):
[ ] company, product, brand names, logos
[ ] domains, URLs, endpoints, API paths, hostnames
[ ] person names, job titles, team or org labels
[ ] internal tool names unique to the client
[ ] real customer data, PII, real IDs (orders, tickets,
    accounts, transactions)
[ ] real dates (use Month Year, or Day 1 / Day 2)
[ ] infra fingerprints: exact version combos, regions,
    unusual naming, anything that alone or in combination
    identifies the client
[ ] re-identifying combinations (niche product plus a
    unique bug plus a timeframe)
[ ] filename, PDF metadata (title, author, subject),
    watermarks, footers
KEEP (never redact the substance):
[ ] the four-part structure on every finding
[ ] severity ranked by impact class
[ ] exact repros (with synthetic values)
[ ] root-cause class, fix pattern, verification
[ ] holds, including why they held

## FILE HYGIENE
- Filename: redacted_engagement_sample_findings.pdf, no
  client name anywhere in the path
- PDF metadata: clear title, author, subject; author is
  your name only
- Final check: open the finished PDF, read it cold, and
  ask: could I identify the client from this? If yes,
  back to the pass.

## REVIEW LOOP (optional but recommended)
Paste the REDACTED draft (never the original) into this
conversation; a line-by-line identifier scrub and a
cold-read recognition check run on it before the 10-28
send. The original client report stays on your machine
the whole time.
