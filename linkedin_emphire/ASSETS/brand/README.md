# Brand card

Rebuilt on 2026-11-15 to the reference layout the owner supplied. Every visual from here on follows this card: photo, name, headline, cut-out portrait, desk, yellow pill, yellow tag.

**The name is Olusanya Timothy**, and it is an argument to the renderer rather than part of a design. The reference card belonged to somebody else and its name was printed onto two renders by mistake before this was fixed.

## The card

1080x1350, the LinkedIn portrait size that takes the most of a phone screen.

| Role | Value |
|---|---|
| Ground | `#FCFCFA` |
| Ink | `#0B0B0B` |
| Accent | `#F9D811` |
| Desk | gradient `#7A4E2A` to `#2E1A0C`, lit edge `#8A5B33` |
| Name on card | Olusanya Timothy |
| Second line on the tag | AI RED TEAMING |

## Render

```
ASSETS/brand/make_card.sh out.png "168 WAYS" "AN AI AGENT" "CAN FAIL"
```

Three headline lines, centred, 104pt bold. Arguments five and six are the name and the tag's second line.

## Assets

- `headshot_400.jpg`, the master photograph, 400x400, from the owner's upload on 2026-11-15. Never regenerated, never restyled, never taken from a reference design.
- `portrait_cutout.png`, 1024x1024, his own photograph with the background removed and replaced by flat white so the desk and the pill can sit behind him. The face is his; the removal only touches what surrounds him. It is a derived file, so if the master photo ever changes, this is regenerated and not edited.
- `make_card.sh`, the renderer. It takes copy, never a design decision.

## Fixed elements, top to bottom

Header: 66px circular photo with the name beside it. Headline: three centred lines, 104pt. Portrait: the cut-out standing behind the desk, 600px tall, bottom aligned to the desk. Desk: 110px band across the bottom with a lit top edge. Yellow pill: person icon, "Follow", then two lines of small type. Yellow tag: name in caps, second line beneath. I would not add a verification badge to the header unless the account has one, because that decorates an asset with a claim.
