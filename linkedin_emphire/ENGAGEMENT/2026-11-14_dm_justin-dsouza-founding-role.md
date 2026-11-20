---
deliverable: dm
id: 2026-11-14_dm_justin-dsouza-founding-role
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 21:12 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: peer
status: ready
approved: no
warm: false
profile_checked: "Justin D'Souza is co-founder and CEO of Asymptote Labs, three people, $5.5M seed led by Tower Research Ventures, hiring founding engineers and security researchers. His article is addressed to people also considering OpenAI, Anthropic or their own company, which is exactly the position this message comes from, and he ends it with an open invitation to write."
premise_checked: >-
  checked: the repository was read before the first message and the article before this one. Every claim in
  the message is about work already done and shipped: the truncated comparison in the verifier, the
  failure-path tests, the four-version examination with an external examiner. No claim is made about
  Asymptote's memory layer beyond the question asked in the comment, and no number is quoted from their
  materials that was not published by them.
sources_read: >-
  read: the article in full, the repository metadata and README, and the hiring post and its replies. The
  Doppel blog post and the Trail of Bits write-up were not opened and nothing in the message depends on them.
---

## DM, paste this

<!-- gate:body:start -->
Justin,

I left a comment on the post, but this is the actual message.

I am one of the people your article is addressed to: also in process with a frontier lab. So rather than say I am excited, here is what I would bring.

Two artifacts. A five-test AI red team suite where I found that my own verifier compared 16 of 64 hex characters and passed everything, then rebuilt it so it fails when it should, including the ordering cases where a record and a package are written in two steps. And a four-version examination of a benchmark artifact with an external examiner, which is where I learned that self-reproduction by the author is not reproduction and should never be described as though it were.

The pattern in both is the one your Beacon release chain already gets right: nothing counts until something has been shown to reject. What I would want to work on is the memory layer's version of that, provenance for what an agent remembers rather than what it installs.

Two questions, and the second one decides it for me. Who should I be talking to, and is the team distributed? I am in Lagos, so remote is not a preference, it is the shape of the job.

Timothy
<!-- gate:body:end -->
