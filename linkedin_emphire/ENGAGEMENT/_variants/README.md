# _variants

Copies that differed from the canon after the 6 November restructure. Kept, never deleted, never read
by the tools.

- `inspiration_library.root.txt` (EMPIRE): byte-identical to `DAILY CONTENT/inspiration_library_RAW.txt`.
- `empire_pipeline.root.txt` (ENGAGEMENT): an earlier edit, 18 lines the canon lacks, 147 the canon has.
- `voice_dna.root.txt` (ENGAGEMENT): the 11 KB corpus. The canon is the 264 KB corpus in `DAILY CONTENT`.
- `THE ENGAGEMENT SPECIALIST.root.md`: 107 lines against the canon's 66, and it carries the comment
  length rules the canon is missing. See `STATE/RECONCILIATION.md` before deciding either way.

Promote rather than merge by hand:

```bash
python3 linkedin_emphire/TOOLING/pipeline.py promote "<this folder>/<file>" --over "<the canon>"
```
