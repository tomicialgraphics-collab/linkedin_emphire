# Portfolio Item 3 — Sample Findings Report

**Project title:**
```
Sample Findings Report: Prompt Injection Test (Personal Project)
```
**Your role:** AI Red Teamer
**URL:** (none needed)
**Skills/tags:** AI Security, Prompt Injection, Risk Assessment, Technical Writing

**Description:**
```
A real findings report from testing my own chatbot, shown in the exact four-part format every client gets: exact repro, which layer failed, the fix, how it was verified. Covers a system prompt leak, a fabricated refund triggered by a trigger word, and a content-policy bypass via fictional framing. This is the format behind every tier of my project catalog, shown here on my own project so you can see it before you buy it.
```
**Full text to use as the project's long description or an attached PDF:** `../sample_findings_report.md`
**Image (landscape, 1584x990):** `../gallery/03_photoreal_findings.png`
**Image (square, 1080x1080):** `../gallery/03_photoreal_findings_square.png`

## The Full Story — What, Why, How

**What was done:** Re-packaged the same three findings from Article 1 into the exact four-part reporting format used for paid client engagements: exact repro, which layer failed, the fix, how it was verified.

**Why it was done:** Client findings reports are confidential by nature, so there was no way to show a prospective buyer a real deliverable without breaking trust with past clients. Reformatting an already-public, self-owned test into the real client template solves that problem directly: a buyer sees exactly the format and depth they'd be paying for before they commit, with zero confidentiality risk because the underlying project is personal, not a client's.

**How it was done:**
1. Took each of the three findings and forced them into the fixed four-field template instead of the looser narrative style used in the article.
2. Wrote the "which layer failed" field as a root-cause statement rather than a restated symptom, for example "no instruction-boundary check" or "conversation text was being treated as an authorization event" instead of just repeating what the bot said. This is the part of a findings report that actually earns the fee, because it tells a client what structurally has to change, not just which input broke things.
3. Added an explicit verification step to each finding: re-ran the original input plus several reworded variants to prove the fix holds against minor rephrasing, not just the exact original attack string.

**Route line (append to the description, last sentence):**
```
The four-layer test this report comes from is the Standard tier of my project catalog, $600, delivered in seven days.
```
