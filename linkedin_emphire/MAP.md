# MAP

Generated 2026-11-06 by `TOOLING/pipeline.py map`. Do not edit by hand: the tree is the source
and this file is its index. If an area is undeclared, declare it in
`PIPELINE/registry/areas.json` with a purpose, an owner role and a stage.

| Area | Files | Size | Newest | Purpose | Role | Stage |
|---|---|---|---|---|---|---|
| `APPLICATIONS` | 16 | 149 KB | 2026-11-06 | one folder per application, with the send package of record | opportunities | S3,S6 |
| `ARCHIVE` | 1 | 5 KB | 2026-11-06 | superseded files and the record of every restructure | strategist | S8 |
| `ARTICLES` | 94 | 42773 KB | 2026-11-06 | the Breaking AI series, one package per article | content | S3 |
| `ASSETS` | 10 | 2742 KB | 2026-11-06 | photos, logos, fonts and anything a card is built from | visual | S3 |
| `BREAKLAB` | 5 | 44 KB | 2026-11-06 | the public harness work | content | S3 |
| `CLIENTS` | 35 | 355 KB | 2026-11-06 | one folder per client, per engagement, dated. Findings first, private to them | empire | S3,S5,S6 |
| `CONTENT` | 2 | 5 KB | 2026-11-06 | content working files that are not yet a post | content | S3 |
| `CONTENT_CALENDARS` | 2 | 47 KB | 2026-11-06 | the posting calendar | content | S1 |
| `CURRICULUM` | 1 | 27 KB | 2026-11-06 | the red-team and research study plan | strategist | S2 |
| `DAILY CONTENT` | 31 | 1165 KB | 2026-11-06 | the editorial canon: templates, hook and visual spec, banned words, voice DNA, drafts | content | S1,S3 |
| `DESIGN` | 5 | 88 KB | 2026-11-06 | render scripts, fonts, locked geometry | visual | S3 |
| `EMAIL` | 10 | 142 KB | 2026-11-06 | email drafts and send logs | opportunities | S3,S6 |
| `EMPIRE` | 11 | 642 KB | 2026-11-06 | the operating layer: pipeline, prompts, money rows | empire | S8 |
| `ENGAGEMENT` | 65 | 1847 KB | 2026-11-06 | comment and DM drafts, feed sweeps, replies | engagement | S1,S3 |
| `LEADS` | 1 | 1 KB | 2026-11-06 | raw inbound leads | opportunities | S1 |
| `LINKEDIN` | 14 | 191 KB | 2026-11-06 | profile copy, headline variants, about section | content | S3 |
| `NETWORKING` | 6 | 55 KB | 2026-11-06 | contacts, connect notes, follow-ups | engagement | S2 |
| `OPPURTUNITIES` | 13 | 161 KB | 2026-11-06 | job and gig leads, the tracker | opportunities | S1 |
| `OUTREACH` | 103 | 713 KB | 2026-11-06 | client-facing outreach and confidential working files | empire | S3,S6 |
| `PIPELINE` | 11 | 56 KB | 2026-11-06 | the rules registry, the stages and the contracts. Read first, change rarely | strategist | S0 |
| `PLANS` | 15 | 300 KB | 2026-11-06 | dated plans with a target and a number | strategist | S1,S8 |
| `PROJECTS` | 276 | 3291 KB | 2026-11-06 | named multi-session work with an owner and a due date | empire | S3,S5 |
| `PUBLISH` | 17 | 161 KB | 2026-11-06 | publish-ready exports and the queue | content | S6 |
| `RESOURCES` | 1 | 2 KB | 2026-11-06 | reference material that is not authored here | strategist | S2 |
| `RESUME` | 16 | 327 KB | 2026-11-06 | resumes and generators. PII, never linked publicly | opportunities | S3 |
| `SESSION_LOG` | 3 | 35 KB | 2026-11-06 | one log per working day, instructions and decisions | strategist | S7 |
| `STATE` | 3 | 7 KB | 2026-11-06 | open loops, delivery log, gate report. The truth about what happened | strategist | S6,S7 |
| `STRATEGY` | 17 | 225 KB | 2026-11-06 | ICP, positioning, weekly plans | strategist | S1,S8 |
| `THE CONTENT CREATOR` | 1 | 3 KB | 2026-11-06 | role prompt for content | content | S0 |
| `THE EMPIRE BUILDER` | 1 | 3 KB | 2026-11-06 | role prompt for the empire | empire | S0 |
| `THE ENGAGEMENT SPECIALIST` | 2 | 6 KB | 2026-11-06 | role prompt for engagement | engagement | S0 |
| `THE OPPORTUNITIES MANAGER` | 1 | 2 KB | 2026-11-06 | role prompt for opportunities | opportunities | S0 |
| `THE STRATEGIST` | 1 | 3 KB | 2026-11-06 | role prompt for strategy | strategist | S0 |
| `THE VISUAL DESIGNER` | 149 | 57342 KB | 2026-11-06 | role prompt for visuals | visual | S0 |
| `TOLU TEMPLATE` | 148 | 57339 KB | 2026-11-06 | document templates inherited from a bundle | strategist | S3 |
| `TOOLING` | 6 | 93 KB | 2026-11-06 | the gate, the linter, the renderer. Code only, no prose | strategist | S0,S4 |
| `UPWORK` | 51 | 30449 KB | 2026-11-06 | catalog, proposals, gig delivery | opportunities | S1,S6 |
| `VERIFIED_POSTS` | 95 | 976 KB | 2026-11-06 | every post that passed the gate, one folder each, plus the index | content | S3,S7 |
| `VISUAL` | 11 | 631 KB | 2026-11-06 | brand guidelines and approved card references | visual | S3 |
| `analytics` | 1 | 3 KB | 2026-11-06 | post performance, follower counts, weekly numbers | strategist | S8 |

## Root files

| File | Purpose |
|---|---|
| `MAP.md` | **UNDECLARED** |
| `PIPELINE.md` | money and relationship rows, the weekly truth |

## Rules, templates, tags

- rules: 30 in `PIPELINE/registry/rules.json`
- templates: 14 in `PIPELINE/registry/templates.json`
- verified hashtags: 11 in `PIPELINE/registry/hashtags.json`


## Repository root, outside the working tree

| Path | Purpose |
|---|---|
| `books/` | reference library, inputs only, never a deliverable (5 files) |
| `manual/` | the inherited operating manual bundle, including the PDF build pipeline (50 files) |
| `host-failure-benchmark/` | the Behar benchmark suites as received, plus the zipped releases (38 files) |
| `google_drive/` | local mirror of what was uploaded to Drive, hashes checked against it (10 files) |
| `uploads/` | personal face assets, gitignored, never committed (20 files) |
| `AGENTS.md` | the contract for any session |
| `README.md` | the map for a human in a hurry |
| `context.md` | the session handoff |
| `emphire`, `emphire.ps1` | the pipeline commands, bash and PowerShell 5.1 |
