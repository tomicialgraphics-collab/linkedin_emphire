# Restructure, 6 November 2026

The repository had two copies of almost everything. Two `DAILY CONTENT/` folders, two `ENGAGEMENT/`,
two `STRATEGY/`, two `RESUME/`, two of each persona file, three `banned_words.txt` and no way to tell
which one the tools read. A session that guessed wrong quoted the wrong banned list, which is exactly
the failure the owner kept having to catch by hand.

This is the record of what moved, what was deleted, what was kept, and why. Nothing was lost: every
file that was not a byte-identical duplicate is either at its new canonical path or parked in a
`_variants/` folder next to it.

## The shape now

- **Root:** boot files and launchers only. `AGENTS.md`, `README.md`, `context.md`, `emphire`,
  `emphire.ps1`, and the input folders that are not deliverables (`books/`, `manual/`,
  `host-failure-benchmark/`, `google_drive/`, `uploads/`).
- **`linkedin_emphire/`:** the whole working tree, with `PIPELINE/` holding the rules, `TOOLING/` the
  gate, `STATE/` the truth about what is open and what was delivered.

## Counts

| Action | Count | Meaning |
|---|---|---|
| dedupe | 185 | byte-identical copy, deleted because the canon already had it |
| move | 27 | only copy, moved to its canonical path |
| replace | 5 | root copy won, the shorter `DAILY CONTENT` copy was parked |
| park | 15 | differs from the canon, kept in `_variants/` rather than merged |

## The canonical editorial files

| File | Canonical path | What happened |
|---|---|---|
| `banned_words.txt` | `DAILY CONTENT/` | the 84-entry list, the one `voice_lint.py` documents, won over two shorter copies |
| `voice_dna.txt` | `DAILY CONTENT/` | the root copy won; the longer `DAILY CONTENT` copy is in `_variants/voice_dna.superseded.txt` |
| `master_prompt.txt` | `DAILY CONTENT/` | root copy won, older copy parked |
| `content_bank.txt` | `DAILY CONTENT/` | root copy won, older copy parked |
| `content_strategy.txt` | `DAILY CONTENT/` | root copy won, older copy parked |
| `post_templates.txt` | `DAILY CONTENT/` | identical in both places, one copy kept |
| `visual_and_hook_spec.md` | `DAILY CONTENT/` | moved from the root, only copy, referenced by every post rule |
| `inspiration_library.txt` | `DAILY CONTENT/` | root copy won, `EMPIRE/` and `DAILY CONTENT/` variants parked |
| `PIPELINE COMMAND VOCABULARY.txt` | `DAILY CONTENT/` | moved, only copy |
| `COMpletechaiinflow.md` | `DAILY CONTENT/` | moved, only copy |

Three copies of `banned_words.txt` existed: 84 entries, 84 entries and 66 entries. The 66-entry copy is
the one that would have been read by anyone who opened `DAILY CONTENT/` first, which is the whole
argument for one canonical path and a gate that resolves it in code.

## Areas merged into the emphire

`EMPIRE/`, `ENGAGEMENT/`, `OPPURTUNITIES/`, `STRATEGY/`, `VISUAL/`, `RESUME/`, `SESSION_LOG/`,
`CURRICULUM/`, `THE CONTENT CREATOR/`, `THE EMPIRE BUILDER/`, `THE ENGAGEMENT SPECIALIST/`,
`THE OPPORTUNITIES MANAGER/`, `THE STRATEGIST/`, `THE VISUAL DESIGNER/`, `PROJECTS/`, `DAILY CONTENT/`.

The root shells are gone. The nested copies were already larger in every case (65 engagement files
against 5, 13 strategy files against 6, 10 resume files against 6), so the nested tree was the survivor
and the root copies that were not identical were parked rather than overwritten.

## Notable moves

- Three resume pairs (PDF and DOCX for AITHOS MTS, Aithos Research Engineer, Anthropic Fellows) moved
  into `linkedin_emphire/RESUME/`. They were already tracked and therefore already public. Nothing new
  was exposed, and the PII rule (R24) is unchanged: confirm before committing a new one.
- The two older session logs moved into `linkedin_emphire/SESSION_LOG/`, next to the current ones.
- The Aithos interview prep and the Aithos aligned post run moved into `linkedin_emphire/PROJECTS/`.
- `ai-redteam-five-tests-build-master.md` moved to `BREAKLAB/`, where the harness work lives.
- `push_to_github.ps1` moved to `TOOLING/`, next to `SYNC_FROM_BUNDLE.ps1`.

## Tooling changes that came with the move

- `voice_lint.py` no longer hard-codes the root `banned_words.txt`. It resolves the canon first, then
  falls back to the two older locations, so an out-of-date checkout still lints.
- `voice_lint.py` strips front matter before linting, because otherwise a gated file reports a false
  "paragraph one has no terminal punctuation" on its own metadata.
- `gate.py` and `pipeline.py` are new, and read every rule from `PIPELINE/registry/`.

## What to do if something looks missing

Look in `_variants/` next to where it used to live, then in git history. Nothing was deleted that was
not byte-identical to a file still in the tree, and every deletion is a `dedupe` row in the migration
log that produced this file.
