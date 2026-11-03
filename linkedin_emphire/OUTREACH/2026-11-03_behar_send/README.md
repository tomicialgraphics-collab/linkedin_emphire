# What to send Behar tonight

Two attachments, one message. Total 12.4 KB. Nothing else.

## Attach

1. `01_MANIFEST-delivered.sha256.txt`, 3.4 KB, 42 lines. The hashes of the 42 files at the names they
   arrived with. The message asks him to run this against his extracted copy, so he cannot close the
   content half without it. The `.txt` extension is deliberate: LinkedIn and mail clients are more
   reliable with it than with `.sha256`.
2. `02_S1-S5-REPRODUCTION-RESULTS.md`, 9.1 KB. The full results with commands, environment, expected,
   observed, exit codes and statuses per finding.

## Do not attach

- **The zip.** He already has the archive. Sending it back proves nothing and doubles the confusion about
  which copy is authoritative.
- **The 42 files.** Same reason. They are in his repository at `ec6e46f`.
- **The six log files.** 6.5 KB total, and the message already carries every observed value. Add them only
  if he asks for the raw output, and then as `.txt`.
- **`RESTRUCTURE.md`, the kit `README.md`, the manifest at repo paths.** Internal to the tidy-up. They name
  the layout he will see once the restructure lands, and sending them ahead of that creates a second
  description of a state that does not exist yet.

## Before sending, one action

The message says the manifest is in the repository. Commit
`01_MANIFEST-delivered.sha256.txt` to `Teamthy/host-failure-benchmark` at the repo root, named
`MANIFEST-delivered.sha256`, before or immediately after sending. GitHub web upload, Add file, Upload
files, is enough for one file. Then the `sha256sum -c` line works for both sides without an attachment
being the only copy.

## The message

`00_MESSAGE.txt`, 459 words, lint clean.
