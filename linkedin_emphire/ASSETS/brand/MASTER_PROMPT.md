---
deliverable: doc
id: 2026-11-15_master-prompt_reference-card
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 08:56 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: every proportion below was measured from the reference card itself on 15 November 2026, by
  downsampling it to a hundred by a hundred and twenty five cells and reading the yellow regions, the dark
  headline band and the desk edge off the pixels, rather than estimated by eye. The colours were sampled the
  same way. The claim about text inside generated images garbling is the reason the prompt is split in two,
  and it is a statement about how these models behave, not a measured result, so it is marked as judgement.
sources_read: >-
  read: the reference card supplied on 2026-11-15, its pixels for colour and proportion, the owner's master
  photograph, and the renderer that already produces this layout. No page was opened.
---

# Master prompt for this template

## Read this before the prompt

**The card is two jobs, and a single prompt does both badly.** A text-to-image model cannot be trusted with a name, a headline and a small line of type: it will letter them beautifully and spell them wrong, and a misspelt name is worse than no name. What models are good at is the part a renderer cannot do, which is a person cut out of a background with believable edges.

So the master prompt is two prompts and one spec:

1. **Prompt A**, the portrait plate. Run this in an image model, with the photograph attached.
2. **Prompt B**, the full card. Only for a one-shot draft to show a client, never for the asset that ships.
3. **The spec**, measured off the reference, which the renderer already follows and which any designer can follow by hand.

## Prompt A, the portrait plate

This is the one that earns its keep.

```
Cut out the man in the attached photograph and set him on a plain flat white background.

Keep his face, skin tone, haircut, beard, light blue dress shirt, dark green waistcoat, patterned tie and watch exactly as photographed. Do not retouch the face, do not smooth the skin, do not change his expression or his age.

Pose: standing, arms folded, framed from mid-thigh to just above the head so the desk can sit in front of his waist. Slight three-quarter turn, shoulders relaxed, head level, looking at the camera.

Light: even studio light, soft key from the front left, no coloured cast, no strong shadow under the chin.

Background: pure white #FFFFFF, no gradient, no vignette, no shadow on the ground.

Square output, sharp edge definition at the hair and shoulders, suitable for compositing.
```

Then key the white out and trim, which is three lines of ImageMagick and already written in the renderer.

## Prompt B, the full card, if you must do it in one shot

```
Design a 4:5 portrait social card, 1080 by 1350, in this exact layout. Flat off-white ground #FCFCFA with the faintest paper texture, no gradient.

Top left: a circular headshot 66 pixels across, with the name "OLUSANYA TIMOTHY" beside it in heavy black sans-serif, about 30 pixels, left aligned on the photo's centre line.

Headline: three centred lines in very heavy black condensed sans-serif, uppercase, about 104 pixels, tight leading, spanning 17 percent to 79 percent of the width and sitting between 18 and 46 percent of the height. The lines read exactly:
"168 WAYS"
"AN AI AGENT"
"CAN FAIL"

Lower left: a yellow #F9D811 rounded rectangle, about 119 to 400 pixels across and 724 to 789 down, holding a small black person-with-plus icon at its left edge, then "Follow @Olusanya Timothy" in bold black 14 pixels, then "for more insight on" and "agent security" in regular black 14 pixels.

Lower right: a yellow #F9D811 rectangle from 713 to 1015 across and 851 to 924 down, holding "OLUSANYA TIMOTHY" in bold black and "AI RED TEAMING" beneath it in regular black.

Bottom: the same man from the attached photograph, cut out, standing behind a dark walnut desk that fills the bottom 3 percent of the frame and runs the full width, with a thin lit edge along the desk's top. His waist disappears behind the desk, his forearms rest forward. He is centred, occupying roughly the middle 55 percent of the width.

Photographic, not illustrated. Flat colour, high contrast, generous white space, no drop shadows, no glows, no gradients except the desk.
```

**Attach the photograph and the reference card to that prompt.** Without both, a model invents a different person in a different layout.

**Then correct the type by hand or in the renderer.** Every word on the card is set by the renderer. Models change it.

## The spec, measured off the reference

Percentages of the 1080 by 1350 frame, so it survives any resize.

| Element | Left | Right | Top | Bottom |
|---|---|---|---|---|
| Pill | 11 | 37 | 53.6 | 58.4 |
| Tag | 66 | 94 | 63 | 68 |
| Headline band | 17 | 79 | 18.4 | 46.4 |
| Desk | 0 | 100 | 96.8 | 100 |

| Role | Value |
|---|---|---|
| Ground | `#FCFCFA` |
| Ink | `#0B0B0B` |
| Accent | `#F9D811` |
| Desk | `#7A4E2A` to `#2E1A0C`, lit edge `#8A5B33` |

Type is heavy geometric sans throughout, one weight for the headline and the name, one regular weight for the small type. Nothing is italic, nothing is outlined, nothing is letter-spaced except the tag.

## Variables to change per post

Only these four move. The rest is the template.

- the three headline lines, kept under about fourteen characters each so they hold the 104 pixel measure
- the tag's second line, default `AI RED TEAMING`
- the two small lines under "Follow"
- nothing else, and never the name

## Negative prompt, which matters as much

```
no second person, no stock-photo stranger, no different face, no beauty filter, no smoothed skin,
no extra fingers, no warped hands on the desk, no invented logos, no verification badge, no watermark,
no signature, no URL, no misspelled text, no duplicated text, no drop shadow on the type,
no gradient background, no border, no rounded frame, no dark mode, no neon, no lens flare
```

The verification badge earns its own line because the reference has one and it is the only element on that card that states a fact rather than decorating. Do not copy it unless the account is verified.

## Why the split is the professional answer

The renderer prints the name, the headline and the small type as vectors, which means they are correct at every size, they can be changed in a second, and they never depend on a model's spelling. The model contributes the one thing code cannot: a person who looks alive against a plain ground.

Two hours spent building the renderer is why this card takes one command today. A prompt that re-rolls the whole card takes as long each time and returns a different person at the end of it.
