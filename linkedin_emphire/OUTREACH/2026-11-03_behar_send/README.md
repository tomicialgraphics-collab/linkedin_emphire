# What to send Behar tonight

Two attachments, one message. Nothing else.

## Attach

1. **`01_MANIFEST-delivered.sha256.html`**, or the `.txt` beside it. The hashes of the 42 files at the names
   they arrived with. The message asks him to run this against his extracted copy, so he cannot close the
   content half without it. Use the `.txt` if his mail client refuses `.html`, and save the `.html` page as
   plain text from a browser if that is easier to copy.
2. **`02_S1-S5-REPRODUCTION-RESULTS.html`**, self-contained, opens in any browser, no network needed. The
   full results with command, environment, expected, observed, exit code and status per finding.

## Do not attach

- **The zip.** He already has the archive. Sending it back proves nothing and muddies which copy is
  authoritative.
- **The 42 files.** Same reason. They are in his repository at `ec6e46f`.
- **The six logs.** The message already carries every observed value, and the results file cites them. Add
  them only if he asks, and then as plain text.
- **`RESTRUCTURE.md` and the kit manifest at repo paths.** They describe a layout that does not exist in his
  repository yet.

## Before sending, one action

The message says the manifest is in the repository. Commit `01_MANIFEST-delivered.sha256.txt` to
`Teamthy/host-failure-benchmark` at the repo root, named `MANIFEST-delivered.sha256`. GitHub web upload,
Add file, Upload files, is enough for one file.

## The message

`00_MESSAGE.txt`, 459 words, lint clean. It is plain text on purpose, because it gets pasted into LinkedIn
rather than opened.

## Printing without a path or page number

Both HTML files carry a print rule that sets the page margin to zero and puts the white space back as body
padding. Chrome and Edge render their own header and footer inside the page margin box, which is where the
`file:///C:/Users/...` line and the page counter come from, so a zero margin leaves them nowhere to draw.

If a path still appears, the browser is adding it from the print dialog, not from the file. Untick
**Headers and footers** in the print dialog, under More settings. Nothing in either file contains a local
path: `grep -c 'file:///' *.html` returns zero on both.
