# Portfolio Item 2 — redteam-lab repo

**Project title:**
```
redteam-lab: 6 Attempts, 4 Breaks (Personal AI Red Team Lab)
```
**Your role:** AI Red Teamer / Developer
**URL:** [paste your GitHub repo link here if public, otherwise leave blank]
**Skills/tags:** AI Security, Prompt Injection, Python, Red Team, Chatbot Development

**Description:**
```
A personal lab documenting real prompt injection testing against my own chatbot: six attempts, four succeeded. System prompt leakage, a fabricated refund triggered by a single word, and a content-policy bypass. The repo holds the exact test inputs, what broke, the fixes shipped, and the regression tests that keep each fix from quietly reopening. Built by me, broken by me, fixed by me.
```
**Image (landscape, 1584x990):** `../gallery/02_photoreal_testlog.png`
**Image (square, 1080x1080):** `../gallery/02_photoreal_testlog_square.png`

## The Full Story — What, Why, How

**What was done:** Built a GitHub repository, redteam-lab, that turns the testing work from Article 1 into reviewable artifacts rather than a narrative: the exact test inputs used, the broken behavior each one triggered, the fix shipped for it, and a regression test that re-runs the original input (plus phrased variants) to confirm each hole stays closed.

**Why it was done:** An article is a claim. A repo is evidence. "I tested my chatbot and found four holes" is a sentence anyone can write. A public repo with the actual test harness and regression suite lets a technical buyer or hiring manager open the code and verify the work line by line, which is a materially stronger credibility signal than prose alone, especially for an audience (engineers, CTOs) that trusts code over copy.

**How it was done:**
1. Took the three concrete findings already documented in the article and the sample findings report (system-prompt leak, fake-refund trigger word, content-policy bypass).
2. Structured the repo so each finding maps to four things: the exact input that triggered it, the observed broken behavior, the fix that was shipped, and a regression test that reruns the original input plus several reworded variants.
3. Scoped everything to self-owned systems only, no client data and no third-party systems, so the entire repo can be fully public with zero confidentiality conflict.

**Route line (append to the description, last sentence):**
```
The four-layer test behind this lab is the Standard tier of my project catalog, $600, delivered in seven days.
```
