# Final banner, 3 November

Set A applied by the owner in the existing design. Words changed, layout untouched.

## What was wrong with the export

The file delivered was 2170 by 725 with the artwork occupying only the middle band, 2170 by 555 starting
92 pixels down. That left a white strip about 92 pixels deep at the top and 78 at the bottom. Uploaded as
it was, LinkedIn fits the image into a 4 to 1 container, so those strips either show as white bands or get
cropped unevenly depending on where the crop box lands.

## The corrected file

`banner_final_1584x396.png`. Cropped to the artwork (2170x555+0+92), resized to 1584 wide, then centre
cropped to exactly 1584 by 396. Full bleed, no white, and every text element intact.

Edge check after the fix: rows 0, 1 and 2 read as the blue artwork, rows 393, 394 and 395 likewise. No
white band anywhere.

## Mobile crop

LinkedIn crops the sides of the banner on mobile. Measured against the 1584 width:

- Speech bubble, roughly x 85 to 430: cut on mobile. Decorative, so it costs nothing.
- "Defenses", roughly x 510 to 1345: survives.
- White pill and the footer line, roughly x 500 to 1350: survive.
- The portrait, roughly x 1290 to 1584: partly cut, which is normal.

If the bubble matters, move it right by about 120 pixels so it clears the mobile crop. That is the only
element that does not survive, and it is the only one that needs to move.

## File to upload

`banner_final_1584x396.png`, 1584 by 396, PNG, 772 KB.
