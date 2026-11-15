# Brand card template

Set from a reference card the owner supplied on 2026-11-15. Every visual from now on carries his photo and his name, in this layout.

**The name is Olusanya Timothy.** The reference card belonged to somebody else, whose name was printed on the first two renders by mistake. The renderer now defaults to the owner's name and takes it as an argument, so a design can never supply a name again.

## The rule

A visual without the photo and the name does not ship. The card is 1080x1350, the LinkedIn portrait size that takes the most screen in the feed.

## Palette, sampled from the reference rather than chosen

| Role | Hex |
|---|---|
| Background | `#FBFBF9` |
| Ink | `#0B0B0B` |
| Secondary text | `#5A5A5A` |
| Rules and empty bars | `#E7E4DB` |
| Accent | `#F9D811` |

Fonts are DejaVu Sans Bold for headline and name, DejaVu Sans for everything else, both already on the machine.

| Field | Value |
|---|---|
| Name | Olusanya Timothy |
| Strapline under the header name | Lagos, Nigeria · AI red teaming, in public |
| Second line on the yellow tag | SOFTWARE ENGINEER, AI RED TEAMING |

## Render

```
ASSETS/brand/make_card.sh out.png \
  "168 WAYS" "AN AI AGENT" "CAN FAIL" \
  "51 are core. The rest are named." \
  "51 core, answered" "117 named, not run" 51 168
```

The last four arguments drive the proportion bar, so a card built on a count shows the count rather than describing it.

## The assets

- `headshot_400.jpg` is the master photo, 400x400, copied from the owner's upload on 2026-11-15. Never regenerate it, never restyle it, and never take a portrait from a reference design.
- `make_card.sh` is the renderer. It takes the copy, not a design decision.

## Fixed elements

Photo circle and name top left, a yellow "AI RED TEAMING" tab, three headline lines, a proportion bar with the core label left and the remainder right, a yellow follow pill above the yellow name tag bottom left, and a 372px portrait circle bottom right.

Arguments 10 and 11 are the name on the card and the second line of the tag. They default to Olusanya Timothy and SOFTWARE ENGINEER, AI RED TEAMING.
