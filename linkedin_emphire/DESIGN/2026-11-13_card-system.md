---
deliverable: doc
id: 2026-11-13_card-system
date: 2026-11-13
audience: internal
status: ready
approved: no
---

# The card system, read off the template folder

What the templates in the Drive folder actually do, what I copied, what I refused to copy, and the
command that turns a post into a card. The generator is `VISUAL/post_visual.py`; the rule that keeps it
attached to the work is R46.

## What was studied

Four files from folder `19lEVdu0nOsvaSOw5gEF68we6hcN-sNVS`, downloaded to `google_drive/` on 13 November:

| File | What it is |
|---|---|
| `1759067440266.jpg` | single card, black ground, 800×1000 |
| `1764597940860.jpg` | single card, white ground, 800×1000 |
| `1764770651964.jpg` | single card, white ground, 800×1000 |
| `1764340246990.pdf` | six-page carousel, page size 1080×1350, "what exactly does a GRC analyst do every day" |

The PDF has no text layer, so the pages were rasterised and read as images.

## What they have in common

Every one of the four is **4:5, portrait**, and every element is either type, a rule, or a flat block of
colour. There is no illustration, no icon set, no stock photograph, no gradient, no drop shadow.

1. **Identity chip at the top**, the same on every card: a round avatar, the name in heavy type, a small
   blue tick immediately after the name, and the role in grey underneath. It is a signature, not a header:
   it never changes, and it is the only element that appears on every page.
2. **The headline carries the card.** Heavy, near-black, tightly set, uppercase, filling roughly the top
   half of the frame in two to five lines. On the black-ground card the whole frame is ink and the type is
   white; on the white-ground cards the frame is paper and the type is ink. There is no third scheme.
3. **One accent, used once.** A flat yellow block `(245,198,75)` holding a short uppercase label, usually
   with a dotted leader line running to a numbered list. Yellow never appears as body text, never as a
   border, never twice on the same card.
4. **A quiet footer**: a hairline rule, the handle on the left, the page counter on the right. Small,
   grey, and the same size on the cover as on the last page.
5. **The carousel is one idea per page.** The cover asks the question; each following page states one
   answer in a headline and, at most, one sentence underneath. Nothing on any page of the document is
   longer than a sentence a person would say out loud.

The design's trick is that the constraint is total: one face, one accent, one measure of grey, no imagery.
A card that needs a picture to work is a card with a weak headline.

## What the cards are made of, in numbers

| Item | Value | Note |
|---|---|---|
| Canvas | 1080 × 1350 | 4:5, the largest ratio LinkedIn renders in the feed and in a document post |
| Margin | 96 px | measured off the carousel: the type block never crosses it |
| Chip | centred, avatar 92 px round, name ~34 px bold, role ~21 px grey | chip baseline sits about 92 px from the top |
| Headline face | one heavy grotesque, uppercase | 54 to 116 px, whichever size keeps the block at five lines or fewer |
| Headline colour | ink `#111111` on paper, paper on ink | no grey headlines |
| Accent | `#F5C64B`, as a solid block behind an uppercase label | one per card |
| Body | regular weight, ~34 px, one sentence | only on carousel pages, never on the cover |
| Footer | hairline rule, handle left, `n/N` right | no page counter on a single card |

The type is set **condensed**. The templates are noticeably narrower than a default grotesque; the
generator reproduces that by drawing each headline line into its own layer and scaling it to 0.74
horizontally. Nothing else on the card is squeezed.

## What I would not copy, and why

**The trial font.** `DESIGN/fonts/BasisNeueExpanded-*.ttf` is a Power Type Foundry trial: every digit in it
is stamped with a tiny "POWER TYPE FOUNDRY" mark. It is invisible at headline size on letters and obvious
the moment a card has a number or a handle in it, which every card here does, and shipping a trial face on
public posts is a licence problem rather than a taste problem. The cards therefore use DejaVu Sans, which
is free, clean and already on every machine that runs the pipeline, squeezed to the same proportion. When a
licensed grotesque is available, swap `FONT_BOLD` and `FONT_REGULAR` and re-render; nothing else changes.

**The illustration.** The GRC carousel fills its right-hand side with pale 3D question marks. It works
because the subject is generic. These posts carry a number and a claim, so a decorative object would be the
one element on the card saying nothing true. Type only.

**The black ground.** Kept in the system, not used by default. It is the right ground for a card that has to
land as a statement rather than as a page, and it will be used for those, not as a rotation.

## How a post becomes a card

```
./emphire visual linkedin_emphire/VERIFIED_POSTS/<slug>/post.md --pages 5
```

It reads the post's own front matter (`headline:`, `box:`) and its body paragraphs, and writes beside the
post:

- `visual/cover.png`, `visual/cover.jpg`: the card a text post goes out with.
- `visual/page2.png` onward, `visual/carousel.pdf`: the document post, when a PDF is the better format.
- A re-render deletes the previous pages first, so a shorter carousel cannot leave an earlier render's cards behind.

Then the card is uploaded, and the Drive link comes back **in the same message as the post**. The link goes
into the post's front matter as `visual_link:`, and R46 fails any post dated 14 November 2026 or later that
has no `visual/cover.png` beside it. A card that exists on this machine and not in his hands is not a card.

## Do and do not

- Do write the headline before the card. If the headline needs more than five lines at 54 px, the post is
  carrying two ideas and the card is telling you so.
- Do keep the box label to three words or fewer. It is a label, not a subtitle.
- Do put a number in the headline when the post has one; the card is the only place the number is seen by
  someone who does not read the post.
- Do not set a headline in mixed case, in grey, or centred.
- Do not put a second yellow anywhere, including in a chart or a highlight.
- Do not let the footer collide with the last line of the block: the generator reserves 200 px above it.
- Do not ship a card whose text is a paraphrase of the headline. Two lines saying the same thing is a card
  with one line and a lot of space.

## Still open

The chip currently falls back to an "OT" monogram disc. It should be his face. Drop a square photo at
`VISUAL/assets/avatar.jpg` and every future card picks it up without another change.
