---
deliverable: comment
id: 2026-11-16_reply_paolo-perrone_per-step-with-the-prefix-hash
date: 2026-11-16
audience: public
status: ready
approved: no
warm: yes
reply_to: >-
  Paolo Perrone, replying to the comment under his 16 November post about the 52.1% context re-read figure.
time_checked: >-
  checked: 2026-11-16 23:00 WAT, read from the system clock before this file was written.
profile_checked: >-
  Paolo Perrone, the author of the post the comment answered and a writer for engineers shipping production inference.
  He concedes the split is what decides the fix and asks one direct question: do you track it per run. The reply answers
  the question rather than expanding the argument, which is what a direct question asks for.
thread: >-
  the original comment argued that a token split is not a spend split because cache reads and cache writes sit on
  opposite sides of the base input price, so the useful split is cached against uncached, and that the context window is
  the second bill. His reply accepts the first and asks how the tracking is done in practice.
premise_checked: >-
  checked: the usage fields described are the ones a hosted API returns for a cached call, and the TTL behaviour is the
  documented five minute and one hour cache. No figure is quoted, nothing is claimed about his pipeline, and the limit
  stated at the end is a limit of the answer rather than a hedge about his data.
sources_read: >-
  read: his reply and the comment it answers. No page opened. The pricing multipliers behind the original comment were
  checked earlier the same evening against two current prompt-cache cost tables.
---

## Comment, paste as is

Per run and per step, and the per step is the one that pays. The usage block reports cache reads and cache writes as separate counts, so the split falls out of one log line per turn: step, prefix hash, read, write, input, output.

The prefix hash is what makes it readable. Without it a miss is ambiguous: either the prefix changed and nothing could hit, or it held and the entry expired between steps. With it you can point at the step where the hash moves and the writes start, which is your prompt structure telling on itself.

The number I'd log next to it is the gap between steps. A five minute cache and a step that waits seven pays a full write for nothing, and that arrives as a cost problem when it's a scheduling one.

Honest limit: past the usage block most hosted APIs won't attribute by tool, so per step is per model call. That's still enough to answer whether the prefix holds, which is the question the split is there to answer.

## Why the answer rather than the argument

He asked a closed question, so the reply is the log line and the two derived numbers. Anything longer turns a question into a lecture, and he writes for people who would notice.

The honest limit is in the reply because it is the part that stops somebody going looking for attribution that the API does not provide. A method that admits where it stops is usable; one that implies a finer resolution than exists gets abandoned at the first missing field.

## If he replies

The question worth having is whether he has ever seen a prefix hash move without a prompt change, which would mean a serde or ordering problem rather than a design one. That is the failure that makes every step a cache write while the prompt looks stable.
