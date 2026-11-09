# Contributing

Corrections, new items and better tests are welcome.

## The bar for a new item

1. **A test somebody can run.** Not a topic, not a concept, not a direction of travel. `tools/validate.py` rejects a test line shorter than five words for a reason.
2. **One sentence.** If it needs three, it is probably two items.
3. **A tier.** `core` means you should be able to run it from memory. Most new items are `standard`.
4. **A category that already exists.** Adding a category means adding a section to the docs and an argument for why the six in place are not enough.

## How to add an item

Edit `checklist/checklist.json` only. Then:

```bash
python3 tools/validate.py
python3 tools/render.py
```

Commit the JSON and the regenerated `CHECKLIST.md` and `checklist.csv` together. CI fails if they disagree, which is deliberate: a rendered file that drifts from its source is worse than no rendered file.

## Where items come from

A test earns a place when it has produced a real finding, or when it closes a class that a real engagement was blind to. Items that exist to fill a category get rejected, and so do items that restate a neighbour with different words.

## Style

- British spelling, plain words, no marketing.
- No em dashes, no exclamation marks in headings.
- Say what to do, not why the idea is interesting.
- A test should name the evidence it produces. "Check access control" is not a test. "Query the vector store with a low-privilege identity" is.

## Pull requests

One change per pull request. Say what you tested it against, even if the answer is "a staging clone of my own system". If a finding came from a real engagement, say the class and not the client.
