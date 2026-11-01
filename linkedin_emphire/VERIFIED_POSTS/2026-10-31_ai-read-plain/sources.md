# Sources and build notes: "The AI read plain and drew a plane"

Second option for 2026-10-31. The primary post for today is
`../2026-10-31_prompt-is-0-10-percent/`. Do not publish both on the same day.

## What is verified, and where

Primary source: BBC News, "Just Eat apologises for AI food mistakes after social media ridicule",
21 October 2026, `bbc.co.uk/news/articles/crz981p0klvgo`. Read in full.
Corroborated by NDTV's write-up, 24 October 2026.

| Claim in the post | Source |
|---|---|
| Trialling AI images for dishes with no photo | BBC: "testing out the tech to showcase food which didn't have images yet" |
| Chip muffin rendered as muffins with potato chips baked in | BBC image caption: "brown cakes with potato chips in them" |
| Cheese roll rendered as cheese rolled into sushi | BBC: "a 'cheese roll' - bread and cheese - instead became slabs of cheese rolled into a sushi roll" |
| Soda bread rendered as cola with egg and bacon floating in it | BBC: a Belfast cafe's bacon and egg soda bread "represented as a glass of fizzy drink with a cooked egg and bacon floating in it", a confusion between "soda" and "soda bread" |
| Garlic bread shaped like a plane, ticket said plain | BBC: "garlic bread in the shape of a plane - presumably because of a misspelling of the word 'plain'" |
| Manchester calls it a chip muffin | BBC: "What some parts of Manchester call a 'chip muffin' - also known as a chip butty" |

## What is NOT verified, and must be checked before you lean on it

**"Every image had been manually checked before it appeared on the platform."**

That sentence is in the BBC News social post, quoted by an archive capture, and echoed in a
secondary summary. It is **not in the article body I fetched**, and I could not open the original
post to confirm the wording.

This matters because it is the load-bearing fact in the `al neitsch` comment in
`ENGAGEMENT/comment_round_2026-10-31.md`, which states it as something Just Eat told the BBC.
Verify it before sending that comment, and if it cannot be verified, cut it to "the report says the
images were checked" or drop the claim and argue from the vocabulary pattern alone, which is fully
sourced.

The post above deliberately does not use that sentence. It rests only on what the article body
states.

## Why this is a good fit for you and not just a news reaction

The four failures share one cause, and it is your positioning rather than a general AI-quality
story. The vocabulary that broke the model is regional, and it broke in Manchester. Which means the
same class of failure arrives first wherever the menu language sits furthest from the training data.
That is the Global South argument arriving as a UK consumer incident, which is a better vehicle for
it than any amount of writing about Lagos.

It also does not require you to have run anything. The rule in this repo is real numbers only, and
every number here belongs to someone else and is attributed.

## Checks

- 343 words, 1,881 characters, inside the 3,000 limit.
- Headline and subheadline take 165 characters including the break, so both sit above the fold.
- `voice_lint.py --profile linkedin --human`: 0 errors, 0 warnings, gate 100/100.
- Template 1 slots all present: problem, "what most teams get wrong", "the reality is different",
  "what actually works" with three arrows, "the part nobody tells you", takeaway, closing question,
  hashtags.

## Conflict to avoid

If you publish this, do **not** also send the `al neitsch` comment today. Same finding, same day,
two surfaces, and the comment would read as a repost of your own post in someone else's thread.
Publish one, comment with the other angle tomorrow.
