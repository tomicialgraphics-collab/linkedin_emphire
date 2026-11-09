---
deliverable: reply
id: 2026-11-08_reply_christopher-paradise-entropy-bounds
date: 2026-11-08
audience: public
status: ready
approved: no
warm: yes
profile_checked: Christopher Paradise, profiled on 2026-11-08. Founder and chief executive of Digital Dynamics Ai, building SARA as a backup and archive system. First degree connection. He replied to the comment within the hour, in technical terms rather than social ones, which is the right register to answer in.
thread: his reply agreeing that MP3 and MP4 are already compressed near the entropy bound, then saying that if the noise can be handled properly there is room for large gains, and that compressed files are the problem everyone has had for a while
verified: the Shannon bound argument is standard information theory and is stated as a bound rather than a calculation. The claim that a container or library level pass finds redundancy a per-file pass cannot is a statement about where redundancy sits, not a measurement of his product.
---

# Reply to Christopher Paradise, 8 November 2026

## What he said

He agreed on the entropy point and then made a claim that deserves an honest answer rather than a polite one: that if the noise
is handled properly there are large gains available in already-compressed files. He is working on it and he may be right in
places. The bound still applies to the entropy coder, and the useful reply is to say where the real gains are instead of
arguing about whether noise modelling can beat Shannon, which it cannot.

The distinction that helps him is per-file against per-library. His incremental numbers already prove he understands this. He
may be looking for the win in the wrong layer for the single-file case.

## Reply

Shannon bounds the entropy coder, and on a single file that is the wall. The gains available on already-compressed media are
not usually in modelling the noise, though. They are in everything the encoder never bounded: near-duplicate frames across a
photo library, silence in audio, the same album art repeated in every track, re-encoded copies, and container overhead.

That is the difference between compressing a file and compressing a library. Per-file ratios on MP4 stay in single digits, and
a library pass can still look dramatic, because the redundancy was never inside the file.

Worth reporting those two numbers separately. They compete in different categories.

## What not to say

No claim that his idea cannot work, because re-encoders do find real redundancy in Huffman tables, padding and shared
reservoirs, and he knows his own field. No maths dump, which would be showing off rather than helping. No mention of the
other product material, and no pitch.

## Held for later

If he keeps going, the interesting question is whether the type-specific coders keep their own version history, since the
archive has to restore a file compressed with a coder that has since changed. That is the question I would ask any backup
inventor and it is more valuable than another opinion about ratio.
