# AGENTS.md

Read this before you touch a single file in this repository. It is the contract between the owner and
every session, agent or tool that works here, including the one reading this now.

---

## 1. What this repo is

The operating system of one LinkedIn brand and one consulting practice, run by **Olusanya Timothy**
(software engineer, AI evaluation and red teaming, Lagos, UTC+1).

It is not a notes folder. It is a **pipeline**: seven stages, a rule registry, one gate, and a written
record of every file that left it. The working tree is `linkedin_emphire/`. The boot file inside it is
`linkedin_emphire/PIPELINE/00-START.md`.

```
AGENTS.md                       you are here: the contract
README.md                       the map, for a human in a hurry
context.md                      the session handoff: who the owner is, standing rules, state
emphire / emphire.ps1           the pipeline commands, for bash and for PowerShell 5.1

linkedin_emphire/
  PIPELINE/                     the machine: rules, stages, contract, roles, registries
    00-START.md                 the read order
    10-STAGES.md                S0 to S8, entry and exit conditions
    20-RULES.md                 generated from the registry, 30 rules
    30-TEMPLATES.md             generated, the fourteen post templates
    40-HASHTAGS.md              generated, the verified tags only
    50-CONTRACT.md              the front matter and the file shape
    60-ROLES.md                 six roles, six folders
    registry/*.json             the only place a rule is defined
  TOOLING/
    gate.py                     enforces every automatable rule
    pipeline.py                 start, status, check, log, audit, render, map, loops
    voice_lint.py               vocabulary and rhythm
    md2html.py                  markdown to a self-contained page
  STATE/
    OPEN-LOOPS.md               what is unfinished
    DELIVERY-LOG.md             what actually left the building
    GATE-REPORT.md              generated scoreboard
  VERIFIED_POSTS/               every post, one folder each, plus INDEX.md
  DAILY CONTENT/                templates, hook spec, banned words, voice DNA, drafts
  ENGAGEMENT/                   comment and DM drafts
  CLIENTS/ PROJECTS/            client work and named projects
  SESSION_LOG/                  one log per working day
```

`linkedin_emphire/MAP.md` is the generated index of every folder, with a declared purpose for each.

## 2. The commands

Bash, in this sandbox:

```bash
python3 linkedin_emphire/TOOLING/pipeline.py start
python3 linkedin_emphire/TOOLING/pipeline.py check <file>
python3 linkedin_emphire/TOOLING/pipeline.py log <file> --to "Name" --how "Drive link"
python3 linkedin_emphire/TOOLING/pipeline.py status
python3 linkedin_emphire/TOOLING/pipeline.py audit
./emphire start
```

Windows PowerShell 5.1, for the owner, one command per line, no `&&`:

```powershell
python linkedin_emphire/TOOLING/pipeline.py start
python linkedin_emphire/TOOLING/pipeline.py check linkedin_emphire\VERIFIED_POSTS\2026-11-06_absence-of-a-record\post.md
.\emphire.ps1 start
```

## 3. The rules that block

The full set is `linkedin_emphire/PIPELINE/20-RULES.md`. These are the ones that have cost the owner
work already:

1. **No em dashes.** Anywhere. R01.
2. **No banned word.** `DAILY CONTENT/banned_words.txt` is literal on LinkedIn. R02.
3. **No `tomicial` identity outward.** No repo URL, handle or email variant in anything a client,
   reviewer, hiring team or vendor receives. Files plus SHA-256 only. R03, R04.
4. **No local paths** in a deliverable. R05.
5. **No fabricated number.** No run, no number; ship the method. R06.
6. **Every post ships a headline and subheadline pair**, two alternatives, one boxed phrase, three to
   five verified hashtags, and the name of the template it was built on. R07 to R13.
7. **Human gate 90 or above**, zero errors, before anything is called done. R14.
8. **The owner sends.** The agent drafts, gates and hands over. R28.
9. **Nothing delivered is missing from `STATE/DELIVERY-LOG.md`.** R22.
10. **Every session writes its log.** R21.

## 4. How to begin, exactly

```bash
python3 linkedin_emphire/TOOLING/pipeline.py start
```

It prints the read order, the rule counts and the open loops. Then read, in order: `00-START.md`,
`20-RULES.md`, `50-CONTRACT.md`, `10-STAGES.md`, and `context.md` sections 7 and 8. If the work is a
post, add `DAILY CONTENT/visual_and_hook_spec.md`, `30-TEMPLATES.md` and `40-HASHTAGS.md`.

Then draft. Then gate. Then log. Then hand over.

## 5. How not to work here

- Do not write a deliverable before reading the rules. The owner has corrected this twice, in writing:
  "always read rules end to end before any deliverables".
- Do not add a rule in a document. Add it to `PIPELINE/registry/rules.json` and render.
- Do not add a hashtag without evidence and a date in `hashtags.json`.
- Do not leave two copies of a file. Superseded files go to `ARCHIVE/`.
- Do not create a new top-level folder without declaring it in `registry/areas.json`.
- Do not commit a new resume, phone number or address: the repository is public. R24.
- Do not claim a fix is fixed, a file is sent, or a number is measured, unless the artefact proving it
  exists in this repo.

## 6. State of play

Live truth is in `STATE/OPEN-LOOPS.md`, `STATE/DELIVERY-LOG.md` and `context.md`. Where those disagree
with a chat message, the repo wins, and the chat message gets added to the repo before work continues.
