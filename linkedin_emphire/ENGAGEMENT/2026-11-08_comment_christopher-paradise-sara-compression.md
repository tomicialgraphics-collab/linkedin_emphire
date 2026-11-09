---
deliverable: comment
id: 2026-11-08_christopher-paradise-sara-compression
date: 2026-11-08
audience: public
status: ready
approved: no
warm: yes
profile_checked: 2026-11-08 from his profile and public writing. Christopher Paradise is a first degree connection, founder and chief executive of Digital Dynamics Ai, building SARA as a backup and archive system with type-specific coders, and publishing on structural approaches to recovery and storage. He writes results posts with the limitations included, which is unusual and is what the comment leads on.
thread: his post reporting SARA Archive measurements against the ZIP tool in Windows, including 48.6 percent average across ten file types, 47.6 percent on a mixed folder, 98.3 percent smaller incremental saves, and an explicit paragraph admitting that MP3 and MP4 barely shrink and that the samples come from one machine rather than being a universal benchmark
verified: the numbers are his and are accepted as his measurements rather than independently checked. Two technical statements in the comment are standard and checkable: the ZIP tool in Windows uses deflate, and deflate dates from the early 1990s. Deduplicating backup tools do use content-defined chunking, so the comparison the comment proposes is a real one rather than a rhetorical one.
---

# Comment on Christopher Paradise's compression results post, 8 November 2026

## Why this angle

He is a first degree connection sharing measured results on his own product, with the limitations stated in the post. That
deserves engagement rather than applause, and the useful engagement is about the baseline, because a benchmark is only as
good as the thing it is compared against.

Comparing to the ZIP tool in Windows is either modest or misleading depending on how it is read, and it is almost certainly
modest. Deflate is over thirty years old. Against zstd or xz the single-pass margin narrows, and the incremental numbers are
competing with deduplicating backup tools rather than with ZIP at all. Saying that is a favour, since a buyer will say it
anyway, only later and less kindly.

## Comment

The paragraph admitting that MP3 and MP4 barely shrink is what makes the rest of these numbers worth reading. Most results
posts leave that out.

One suggestion on baselines. The ZIP tool in Windows means deflate, so the single-pass comparison mostly shows that deflate
is thirty years old. Against zstd or xz the margin will be thinner, and a sceptical buyer will run that first.

The comparison that actually matters is the incremental one, against deduplicating backup tools, because that is
content-defined chunking and it is the thing an infrastructure team already runs. A 43-file edit adding 0.45 MB is a claim
ZIP cannot answer at all. Lead with it.

## What not to say

No congratulations paragraph before the point. No doubt about the measurements, which are stated with their limits and
have the byte-exact restore check behind them. No mention of the wider KARIOS material, which is a different conversation
and not one to open in his comments. No request and no link.

## Held for a later turn

If he replies, the natural question is what the archive format does when a coder is removed or upgraded, since a
type-specific format that cannot restore an old archive after a version change is a worse trade than a weaker ratio. That
is a real engineering question and it is the one a backup product lives or dies on.
