# Session log, 2026-11-09

## Owner instruction: read the links, always

Asked directly whether attached links and read-more material are always read before a comment goes out.
The honest answer was no, and the answer was checked against the files rather than asserted: of 35
engagement artefacts dated 9 November, 4 named a source that was opened and 2 carried a `verified:`
line. The remainder were silent, which is worse than an answer, because silence reads as "nothing to
read" when it usually meant "nothing the comment depended on".

The rule I had been applying privately was "read it when the comment would otherwise be a reaction".
That is not a rule. Only I can check it, and the owner finds out afterwards.

First pass, same evening: `sources_read:` added to the R26 contract for comments and DMs dated
2026-11-10 onward, with four values including `not-needed:` for a comment that deliberately rests on
the post alone. The owner struck that out within the hour. "please always read it."

Second pass, now standing:

- Every link a post attaches is opened before anything is written about it. The read-more, the paper,
  the SSRN copy, the film, the waitlist, the publisher page, the repository, the other post it quotes.
- Reading the post is not reading the link. Summarising a source is not reading it either.
- A landing page, a waitlist or a listing counts as read. Open it, say what it turned out to be, and
  the line still reads `read:`.
- `blocked:` is only for material that will not open, and it carries the reason plus what the comment
  claims without it.
- `not-needed:` is retired and now fails the gate.
- Nothing before 2026-11-10 is retro-fitted. The values would be reconstruction.

Written to `context.md` section 7 as a standing rule, to `PIPELINE/50-CONTRACT.md` as the contract, and
to `PIPELINE/registry/rules.json` as R26, which blocks from 2026-11-10.

## Owner question: what other rules should be added

Answered with the six gaps that have an actual failure behind them, two of them now machine-checked
and four left as reading rules. The test applied to each: name the artefact it would have caught.
A rule that cannot name one is bureaucracy, and this repo has 31 rules already.

Added as checks:

- **R32, no filename with an extension in pasted text.** `wilson.py` was sitting inside the launch
  first comment, `status: ready`, for a 19:00 WAT paste. A dot in pasted text is an autolink to an
  address that does not exist, learned the first time with a zip and the second time with a md. The
  comment now says "the Wilson interval script". WARN before 2026-11-10, block after.
- **R33, `premise_checked:`.** The Nvidia repricing was checked before the Sanchez comment and the
  check lived only in that file's prose. A post resting on a price, a count or a benchmark now names
  the fact, where it was checked and the day, or declares `opinion:`.

Added as reading rules:

- **R34, two exchanges per thread.** Already the habit; now written.
- **R35, version and surface.** The FORAY lesson: a proof on an internal path is not a capability.
- **R36, recompute the hash in the same command that writes the letter.** The Evelyne recomputation.
- **R37, a question answered twice is not asked a third time.** He chose Drive links twice.

Rejected on purpose, with reasons: a rule that every comment must be answered within a day, because
the feed is not a service desk. A rule against commenting on reposts, because the existing held-file
pattern already handles it and a blanket ban would lose the one repost worth answering. A rule
requiring a figure in every post, because it would manufacture the thing R06 exists to prevent.

