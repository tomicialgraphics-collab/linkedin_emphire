# MAP

Generated 2026-11-09 by `TOOLING/pipeline.py map`. Do not edit by hand: the tree is the source
and this file is its index. If an area is undeclared, declare it in
`PIPELINE/registry/areas.json` with a purpose, an owner role and a stage.

| Area | Files | Size | Purpose | Role | Stage |
|---|---|---|---|---|---|
| `APPLICATIONS` | 16 | 149 KB | one folder per application, with the send package of record | opportunities | S3,S6 |
| `ARCHIVE` | 1 | 5 KB | superseded files and the record of every restructure | strategist | S8 |
| `ARTICLES` | 94 | 42773 KB | the Breaking AI series, one package per article | content | S3 |
| `ASSETS` | 10 | 2742 KB | photos, logos, fonts and anything a card is built from | visual | S3 |
| `BREAKLAB` | 5 | 44 KB | the public harness work | content | S3 |
| `CLIENTS` | 48 | 525 KB | one folder per client, per engagement, dated. Findings first, private to them | empire | S3,S5,S6 |
| `CONTENT` | 2 | 5 KB | content working files that are not yet a post | content | S3 |
| `CONTENT_CALENDARS` | 2 | 47 KB | the posting calendar | content | S1 |
| `CURRICULUM` | 1 | 27 KB | the red-team and research study plan | strategist | S2 |
| `DAILY CONTENT` | 32 | 1166 KB | the editorial canon: templates, hook and visual spec, banned words, voice DNA, drafts | content | S1,S3 |
| `DESIGN` | 5 | 88 KB | render scripts, fonts, locked geometry | visual | S3 |
| `EMAIL` | 10 | 142 KB | email drafts and send logs | opportunities | S3,S6 |
| `EMPIRE` | 12 | 643 KB | the operating layer: pipeline, prompts, money rows | empire | S8 |
| `ENGAGEMENT` | 85 | 1964 KB | comment and DM drafts, feed sweeps, replies | engagement | S1,S3 |
| `LEADS` | 1 | 1 KB | raw inbound leads | opportunities | S1 |
| `LINKEDIN` | 14 | 191 KB | profile copy, headline variants, about section | content | S3 |
| `NETWORKING` | 6 | 55 KB | contacts, connect notes, follow-ups | engagement | S2 |
| `OPPURTUNITIES` | 13 | 161 KB | job and gig leads, the tracker | opportunities | S1 |
| `OUTREACH` | 131 | 935 KB | client-facing outreach and confidential working files | empire | S3,S6 |
| `PIPELINE` | 11 | 57 KB | the rules registry, the stages and the contracts. Read first, change rarely | strategist | S0 |
| `PLANS` | 15 | 300 KB | dated plans with a target and a number | strategist | S1,S8 |
| `PROJECTS` | 277 | 3293 KB | named multi-session work with an owner and a due date | empire | S3,S5 |
| `PUBLISH` | 17 | 161 KB | publish-ready exports and the queue | content | S6 |
| `RESOURCES` | 1 | 2 KB | reference material that is not authored here | strategist | S2 |
| `RESUME` | 17 | 335 KB | resumes and generators. PII, never linked publicly | opportunities | S3 |
| `SESSION_LOG` | 3 | 35 KB | one log per working day, instructions and decisions | strategist | S7 |
| `STATE` | 4 | 36 KB | open loops, delivery log, gate report. The truth about what happened | strategist | S6,S7 |
| `STRATEGY` | 18 | 234 KB | ICP, positioning, weekly plans | strategist | S1,S8 |
| `THE CONTENT CREATOR` | 1 | 3 KB | role prompt for content | content | S0 |
| `THE EMPIRE BUILDER` | 1 | 3 KB | role prompt for the empire | empire | S0 |
| `THE ENGAGEMENT SPECIALIST` | 3 | 7 KB | role prompt for engagement | engagement | S0 |
| `THE OPPORTUNITIES MANAGER` | 1 | 2 KB | role prompt for opportunities | opportunities | S0 |
| `THE STRATEGIST` | 1 | 3 KB | role prompt for strategy | strategist | S0 |
| `THE VISUAL DESIGNER` | 149 | 57342 KB | role prompt for visuals | visual | S0 |
| `TOLU TEMPLATE` | 148 | 57339 KB | document templates inherited from a bundle | strategist | S3 |
| `TOOLING` | 6 | 101 KB | the gate, the linter, the renderer. Code only, no prose | strategist | S0,S4 |
| `UPWORK` | 51 | 30449 KB | catalog, proposals, gig delivery | opportunities | S1,S6 |
| `VERIFIED_POSTS` | 96 | 979 KB | every post that passed the gate, one folder each, plus the index | content | S3,S7 |
| `VISUAL` | 11 | 631 KB | brand guidelines and approved card references | visual | S3 |
| `analytics` | 2 | 6 KB | post performance, follower counts, weekly numbers | strategist | S8 |

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
| `books/` | reference library, inputs only, never a deliverable |
| `manual/` | the inherited operating manual bundle, including the PDF build pipeline |
| `host-failure-benchmark/` | the Behar benchmark suites as received, plus the zipped releases |
| `google_drive/` | local mirror of what was uploaded to Drive, hashes checked against it |
| `uploads/` | personal face assets, gitignored, never committed |
| `AGENTS.md` | the contract for any session |
| `README.md` | the map for a human in a hurry |
| `context.md` | the session handoff |
| `emphire`, `emphire.ps1` | the pipeline commands, bash and PowerShell 5.1 |
