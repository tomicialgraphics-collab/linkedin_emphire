---
deliverable: dm
id: 2026-11-13_dm_sebastien-favre-second-reader
date: 2026-11-13
audience: vendor
status: ready
approved: yes
warm: yes
profile_checked: >-
  Sébastien Favre, NeoMundi. He replied on 13 November at 14:01 to the message about his evidence chain. He has taken the
  report-versus-evidence distinction seriously and says he is building NeoMundi Evidence as a verification layer separate
  from the measurement API, with independent Python and Rust verifiers, attestations and timestamping. He concedes the
  limitation rather than arguing with it, and asks directly how I would design the second-reader experience. He also asks
  for the case study. This is a peer conversation with a vendor, not a sale.
premise_checked: >-
  checked: the claims the reply relies on are his own, from the message, about the separate verification layer and the
  independent Python and Rust implementations. The case study detail is from this repository: version 5 of 13 November,
  the title corrected from five weeks to ten days at the client's instruction. Nothing is asserted about NeoMundi's
  implementation beyond what he wrote.
sources_read: >-
  read: his message in full. The neomundi.io link was read earlier on 12 November; it was not re-opened for this reply,
  and nothing here depends on a fresh reading of it.
---

## Message, paste as is

<!-- gate:body:start -->
Hi Sébastien,

Thanks for naming the limitation rather than smoothing it over. Since you asked how I'd design the second reader,
here is what I'd build and the order I'd build it in.

Split the verdict before you split the tooling. A package should come back with three separate results rather than
one stamp: integrity, which is the bytes being the bytes; provenance, which is who signed them, when, and by what
authority; and meaning, which is what the numbers are supposed to show. That third one is what nobody can verify
remotely, and printing it as its own row stops a reader treating a green integrity check as a true claim. Your site
already separates authenticity this way, and your package should do the same per claim.

Then make the verifier portable and testable. One static binary or a single file with no network, published with
its own hash, with the vectors that test the verifier shipped inside the package. It runs the self-test first, so
a failure is attributable to the tool or to the data instead of to both at once.

Include a negative control: one deliberately corrupted copy that must fail, with the exact output it produces. An
auditor who has only seen your tool succeed has never seen it fail, and cannot tell verified from printed OK.

And write the no-tool path. Three checks that need a browser and a text editor: the digest recomputed on the
auditor's own machine, the anchor looked up on a public explorer, the timestamp checked against the timestamping
authority. Say plainly what a person can still establish when they can run nothing, because that is the version
that survives a procurement review.

The case study is at
https://drive.google.com/file/d/1bMrMGCwFvI6q7z00n7YaCkwk2rYhI_FY/view and version 5 is the one to read, three pages.
Start at the section headed What changed in version 5. Its title said five weeks and the review ran ten days. My
client caught that after publication and asked for a new version rather than an edit in place, so the correction
sits in the page where a reader can see it. That is the closest thing I have to the property you're designing for.

Timothy
<!-- gate:body:end -->

## What not to say

No assessment of his product beyond the one distinction he already accepted, and no offer to consult. No second link and
no pitch for the playbook. Nothing that points out the correction as a way of saying the page is unusual: it is in there
because a reader should be able to see it, which is his argument, not mine.

## Why this is worth the slot

He is building the exact thing the last three messages have been about, in public, and he asked a design question rather
than for a favour. The answer is specific enough to be checked against his own build, and the case study goes out with it
because a document that carries its own correction is a better argument than a paragraph claiming the property.
