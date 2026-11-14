# Dataset provenance audit

Five checks you can run on a training corpus before anyone trains on it, using only the file listing. No download, no imports, no code execution, no model calls.

It exists because the usual diligence on a dataset is reading its card, and the card is written by whoever assembled the corpus. A page that grades its own homework is not evidence. A file listing is.

## The five checks

1. **Size reconciliation.** Every size the card states, compared against each other and against the sum of the files.
2. **Usability.** How many files are there, how many parse, what the rest are.
3. **Licence standing.** Each named upstream source mapped to its actual published terms, and the condition each one attaches.
4. **Executable artefacts.** Files that run or unpack on load, plus anything the platform has flagged.
5. **Evaluation overlap.** Paths that look like benchmark or lab material, because a corpus that also serves as a leaderboard makes the leaderboard meaningless.

## Files here

| File | What it is |
| --- | --- |
| `audit.py` | The tool. Reads a Hugging Face tree JSON or a directory listing, writes markdown and JSON. |
| `RUNBOOK.md` | How to get the tree without cloning, in PowerShell 5.1, and what not to do. |
| `UPSTREAM-LICENCES.md` | Per-source licence standing with the deciding clause quoted and dated. |
| `FINDINGS-2026-11-14-vyber07-cyber-security.md` | The case that started this, written up. |

## Run it

```powershell
python audit.py --tree tree.json --dataset "org/name" --claim "16 GB" --claim "95 GB" --out report.md --json report.json
```

Exit code 1 means something blocks: the sizes disagree with the repository, or the licence is blocked, or the platform flagged a file.

## What it is for

Two uses, and the second is the interesting one.

**Before training.** Run it on any corpus you are about to fine-tune on. Ten minutes, no download, and it either clears the dataset or tells you which of the five questions to take to a lawyer or to the uploader.

**Before trusting a model.** If a model was trained on a corpus that fails these checks, the fact is worth knowing and is almost never published. The count of published models trained on a failing corpus is a number nobody is tracking, and it is a legitimate thing to ask a vendor.

## The limit, stated once

This checks claims, not content. A dataset can pass all five and be useless, biased or wrong. A dataset can fail one and be excellent. What none of the five can be answered after the fact is what makes them worth the ten minutes: once the weights exist, the corpus is unobservable.

## Provenance of this tool

Built 14 November 2026 while reading a 20,702-download cyber security corpus whose card contradicted itself five times. The clause texts in `UPSTREAM-LICENCES.md` were read from the operators' own published terms on that date and will drift, so re-read before quoting them in front of a client.
