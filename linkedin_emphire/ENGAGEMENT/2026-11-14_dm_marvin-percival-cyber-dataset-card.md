---
deliverable: dm
id: 2026-11-14_dm_marvin-percival-cyber-dataset-card
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 20:33 WAT, read from the system clock in the sandbox (19:33 UTC) before this
  file was sent for gate. The clock helper used earlier is not present in this checkout.
audience: peer
status: ready
approved: no
profile_checked: "Marvin Percival sent the link at 20:04 with the words saw this, FYI, and nothing else. He is not asking a question and he is not proposing work, so the useful reply is a read he can use rather than an acknowledgement or a request of my own. He reviewed version 5 and has asked for a call, so a message that costs him nothing to read and gives him something to argue with is the right currency here."
premise_checked: >-
  checked: the dataset card was read in full, both sections, and every figure in the reply is quoted from
  it rather than recalled. The files themselves are behind an accept-the-conditions gate and were not
  opened, which the reply says plainly. Nothing in it characterises the content, only the card.
sources_read: >-
  read: huggingface.co/datasets/Vyber07/cyber-security, the card text only, including the overview, the
  statistics table, the sources list, the licence line and the download and fine-tune counts.
---

## DM, paste this

<!-- gate:body:start -->
Read the card. Two things it says about itself don't agree, and the licence line is the reason I would not put this near a client.

Size: the overview says 16 GB. The statistics table and the file metadata both say 95 GB. Same page, six times apart.

Files: 507 total, 394 valid JSON. So 113 files, about a fifth, are not valid JSON and the card does not say which ones or why. Anyone writing a loader against 507 gets 394 and an exception.

Licence: Apache 2.0, over content described as pulled from HackTheBox, TryHackMe, PortSwigger Academy, SANS and VulnHub. None of those licence redistribution of their material, so the uploader is granting something they do not hold. Nine models are already fine-tuned on it and it pulled 20,702 downloads last month, which means the wrong licence is travelling in a lot of pipelines.

The other tell is smaller. PhD-level appears as a string inside the metadata of the records. That is a label the file gives itself, and five seconds of reading turns it from a standard into a word.

I only read the card. The files sit behind an accept-the-conditions screen, so I am making no claim about whether the content is any good. The claim is narrower and enough: the card fails its own arithmetic, and the licence cannot be relied on.

Provenance and licence are the two gates everyone skips, and they are the two that cannot be repaired after the model is trained.

Worth thirty seconds of your time to see the pattern. When you send me the windows for next week, I will bring this as one of the open items if you want it on the agenda.
<!-- gate:body:end -->
