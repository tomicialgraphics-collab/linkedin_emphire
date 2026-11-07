# _variants

Superseded copies kept for the record. Nothing here is the canon and nothing here is loaded by the
tools. `voice_lint.py` and `gate.py` both read `DAILY CONTENT/banned_words.txt`, never this folder.

| File | Why it is here |
|---|---|
| `banned_words.root.txt`, `banned_words.superseded.txt` | the 66-entry list. The canon has 84 entries. This is the copy that would have been read by anyone opening the folder first, and demoting it is the main point of the 6 November restructure |
| `voice_dna.root.txt`, `voice_dna.superseded.txt` | the 11 KB corpus. The canon is the 264 KB corpus |
| `master_prompt.root.txt` | a different lineage, marked `FINAL VERSION`, 37 lines the canon lacks. See `STATE/RECONCILIATION.md` |
| `content_bank.root.txt`, `content_bank.superseded.txt` | shorter copies of the canon |
| `content_strategy.superseded.txt` | shorter copy, marked `FINAL VERSION`, holds the pillar percentages. See `STATE/RECONCILIATION.md` |
| `content_strategy.root.txt` | same document, earlier edit |
| `inspiration_library.root.txt` | byte-identical to `DAILY CONTENT/inspiration_library_RAW.txt`. Not lost, duplicated |

To make one of these the canon without deleting anything:

```bash
python3 linkedin_emphire/TOOLING/pipeline.py promote "_variants/<file>" --over "<the canon>"
```

The old canon is parked with a `.superseded` suffix, so the move is reversible.
