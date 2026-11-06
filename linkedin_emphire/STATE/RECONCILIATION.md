# Reconciliation, 6 November 2026

The restructure deleted 185 files and moved 27. This file answers the only question that matters after
a restructure: did anything unique go?

**Short answer: no.** Every one of the 185 deletions was byte-identical to a file still in the tree.
That is checked, not asserted:

```
python3 linkedin_emphire/TOOLING/pipeline.py verify-moves --since 4a56d93
```

```
4a56d93: 185 deletions
  byte-identical survivor in the live tree: 185
  no survivor, needs a human: 0
```

The check hashes the blob each deleted path had before the commit and looks for that exact blob
anywhere in the current tree. Same bytes means duplicate, by definition.

---

## Where the files went

| You were looking for | It is now |
|---|---|
| `banned_words.txt` at the root | `linkedin_emphire/DAILY CONTENT/banned_words.txt` |
| `visual_and_hook_spec.md` at the root | `linkedin_emphire/DAILY CONTENT/visual_and_hook_spec.md` |
| `post_templates.txt` at the root | `linkedin_emphire/DAILY CONTENT/post_templates.txt` |
| `master_prompt.txt`, `voice_dna.txt`, `content_bank.txt`, `content_strategy.txt` | `linkedin_emphire/DAILY CONTENT/` |
| `PIPELINE COMMAND VOCABULARY.txt`, `COMpletechaiinflow.md` | `linkedin_emphire/DAILY CONTENT/` |
| `RESUME/*.pdf` and `*.docx` | `linkedin_emphire/RESUME/` |
| `SESSION_LOG/SESSION_LOG_2026-10-3*.md` | `linkedin_emphire/SESSION_LOG/` |
| `PROJECTS/2026-11-01_*`, `2026-11-02_*` | `linkedin_emphire/PROJECTS/` |
| `STRATEGY/2026-10-31_icp-goals_push-plan.md` | `linkedin_emphire/STRATEGY/` |
| `CURRICULUM/` | `linkedin_emphire/CURRICULUM/` |
| `ai-redteam-five-tests-build-master.md` | `linkedin_emphire/BREAKLAB/` |
| `push_to_github.ps1`, `SYNC_FROM_BUNDLE.ps1` | `linkedin_emphire/TOOLING/` |
| `THE X/` persona folders at the root | `linkedin_emphire/THE X/` |

Nothing left the repository. `git show 4a56d93^:<path>` returns any old path exactly as it was, and
`ARCHIVE/RESTRUCTURE-2026-11-06.md` has the migration record.

---

## The three files that had two lineages

Fifteen files differed from their twin, so one of each pair had to become the canon and the other went
to `_variants/`. For twelve of them the answer is obvious and settled. For three it is an editorial
call that belongs to the owner, so it is written down here rather than decided quietly.

### 1. `THE ENGAGEMENT SPECIALIST` persona. Read this one first.

| | Size | What is in it |
|---|---|---|
| Canon now | 1,847 B, 66 lines | the shorter persona, matches the last snapshot in `.history` (`75449b2f7ff4`) |
| Parked | 3,855 B, 107 lines, `_variants/THE ENGAGEMENT SPECIALIST.root.md` | adds the working rules the canon lacks |

The parked copy carries the operational constraints:

```
VOICE RULES (10-24 human gate, full spec in ENGAGEMENT/voice_dna.txt PART 10 + COMMENT MODES):
- 90-120 words for a main comment, 15-60 for a reply. Never longer than the post.
```

Those numbers are worth having in the canon, because every comment draft in this repo is written to
them and the canon currently does not say so. **Recommendation: merge those four or five lines into
the canonical persona.** It is a two minute edit and it makes the comment pipeline traceable.

### 2. `DAILY CONTENT/master_prompt.txt`

| | Size | What is in it |
|---|---|---|
| Canon now | 14,810 B | the root lineage (`025d67fee9dc`) |
| Parked | 16,243 B, `_variants/master_prompt.root.txt` | marked `FINAL VERSION, All Updates Incorporated`, and it is the last snapshot in `.history` |

The parked copy has 37 lines the canon does not, including the wider scope line about multi-domain
development, computer vision and ethical adoption, and 16 canon lines are missing from it. Two
different edits of the same document, neither a superset.

**Recommendation: read both once and keep one.** If the "FINAL VERSION" header is real, the parked
one is the later document and should be promoted.

### 3. `DAILY CONTENT/content_strategy.txt`

| | Size | What is in it |
|---|---|---|
| Canon now | 22,224 B | the fuller document, 231 lines the parked copy does not have |
| Parked | 15,863 B, `_variants/content_strategy.superseded.txt` | marked `FINAL VERSION`, includes the pillar percentages |

**Recommendation: keep the canon as the canon, and read the parked copy for the pillar percentages
and the rules section.** If those percentages are still the plan, fold them into the canon by hand.
Do not promote a shorter file over a longer one to settle a header.

---

## How to promote a parked file

```bash
python3 linkedin_emphire/TOOLING/pipeline.py promote \
  "linkedin_emphire/DAILY CONTENT/_variants/master_prompt.root.txt" \
  --over "linkedin_emphire/DAILY CONTENT/master_prompt.txt"
```

The old canon is parked with a `.superseded` suffix, so promoting is reversible, and `render` picks up
the change on the next run. Nothing is ever deleted to settle a question.

## What is not in question

- `inspiration_library.txt`: the 253 KB file that could have been lost is byte-identical to
  `inspiration_library_RAW.txt` (`587bd3933ab8`), which is still in the tree. The curated 57 KB library
  is a different, shorter document, and it is the canon.
- `voice_dna.txt`: the 264 KB corpus is the canon. The 11 KB copy is in `_variants`.
- `banned_words.txt`: the 84-entry list is the canon. The 66-entry copies are in `_variants`, and this
  is the single most important correction in the whole restructure.
