# linkedin_emphire

The operating system for one practitioner's public work: LinkedIn posts, comments, articles, client
reviews and applications, run as a pipeline rather than a pile of drafts.

Owner: **Olusanya Timothy**, software engineer working on AI evaluation and red teaming, Lagos.

---

## Start here

| If you are | Read | Then |
|---|---|---|
| An agent or a new session | `AGENTS.md` | `python3 linkedin_emphire/TOOLING/pipeline.py start` |
| The owner, checking today | `linkedin_emphire/STATE/OPEN-LOOPS.md` | `./emphire status` |
| Reviewing one deliverable | that file's front matter | `python3 linkedin_emphire/TOOLING/gate.py <file>` |
| Trying to understand the tree | `linkedin_emphire/MAP.md` | `linkedin_emphire/PIPELINE/10-STAGES.md` |

## What makes it a pipeline

Three things, and they are the whole design:

1. **One rule registry.** `linkedin_emphire/PIPELINE/registry/rules.json` holds 30 rules, each with an
   ID, a source, a severity and the check that enforces it. The readable doc is generated from it. A
   rule that is not in the registry is not a rule.
2. **One gate.** `TOOLING/gate.py` enforces every rule with a check and says so in one screen. It exits
   non-zero when a deliverable would fail one. It reads front matter, so a post declares its headline,
   its box, its hashtags and its template, and the gate checks the declarations against the rules.
3. **One record.** `STATE/DELIVERY-LOG.md` holds a row for every file that left, with size, SHA-256,
   gate verdict, recipient and method. If it is not there, it was not delivered.

```
intake -> read -> draft -> gate -> verify -> deliver -> log
   S1       S2      S3      S4       S5        S6      S7
```

## The gate in one line

```bash
python3 linkedin_emphire/TOOLING/pipeline.py check linkedin_emphire/VERIFIED_POSTS/<folder>/post.md
```

## What it will not do

It will not make the argument good, and it will not read the room. Those five rules are marked
`manual` in the registry on purpose, and a person still has to be honest about them.

## Layout

The working tree is `linkedin_emphire/`. The repository root holds this file, `AGENTS.md`, `context.md`
and two launchers, so a session lands on the contract before it lands on the content. See
`linkedin_emphire/MAP.md` for every folder, its purpose and its owner role.
