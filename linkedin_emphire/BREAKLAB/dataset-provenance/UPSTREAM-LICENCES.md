# Upstream licences: what each source actually permits

Checked 14 November 2026 against the operators' own published terms, not against a summary of them. Every entry carries the clause that decides it. Where no clause was read, the entry says so and is treated as blocked.

This file exists because a dataset card's `License:` line describes the uploader's claim, not the rights of the people whose work is inside the file. A scraper cannot license what it does not own, and Apache 2.0 stamped on top of someone else's lab write-ups grants nothing.

## Blocked: redistribution is prohibited as it stands

### PortSwigger Web Security Academy

**Clause 7.4.** "Users may print off one copy, and may download extracts, of any page(s) from the Websites for personal use only."

**Clause 7.7.** "Users must not use any part of the content on the Websites or share any materials, tools or products obtained from PortSwigger, whether directly or indirectly, for any commercial purposes without obtaining a license to do so from PortSwigger."

**Clause 7.8.** Reproducing content in breach of the terms ends the user's right to use the site, and the user must return or destroy the copies.

Source: `portswigger.net/web-security/certification/terms-and-conditions/website-terms-of-use`, read 14 November 2026.

What this means for a dataset: the Academy material is licensed for one person's personal study. Republishing it in a corpus, under any licence, is the act 7.7 prohibits. The commercial-purpose line matters twice over, because a training corpus is normally built towards a product.

### Hack The Box

**User Agreement 11.2.** "Hack The Box grants you a limited, personal, non-exclusive, non-transferable, and revocable right to access and use HTB Content solely for the purpose of your own cybersecurity education, training, and upskilling within the Services."

**Clause 11.4(a).** The user "must not copy, reproduce, modify, create derivative works from, frame, mirror, republish, download, display, transmit, or distribute all or any portion of the Services or HTB Content in any form or by any means".

**Clause 11.4(e).** Nor "license, sell, rent, lease, transfer, assign, distribute, disclose, or otherwise commercially exploit, or make the Services or HTB Content available to any third party".

**HTB Academy terms 4.** "Is expressly prohibited any copying, reproduction, republication, transfer, storage, processing, transmission, distribution ... of the content of the HTB ACADEMY in any manner or means, for commercial or other purposes whatsoever, in part or in summary form, without the prior written consent of the HTB."

Sources: `resources.hackthebox.com/hubfs/Legal/UA.pdf` (effective 1 April 2026), `academy.hackthebox.com/tos`, read 14 November 2026.

### TryHackMe

**Terms of Use 3.1.** Content is "provided on the Website 'AS IS' for your information and personal use only", and "no part of the Website and no Content or Marks may be copied, reproduced, aggregated, republished ... for any commercial purpose whatsoever, without our express prior written permission".

**Business terms 8(b).** The customer "shall not reproduce or adapt any Content, or any material derived from or reproducing the structure or substance of any Content, in order to develop or deliver any training, course or assessment outside the Services".

Sources: `tryhackme.com/terms`, `tryhackme.com/legal/business-terms-of-use`, read 14 November 2026.

## Conditional: allowed only if a stated condition travels with the copy

### MITRE ATT&CK

MITRE grants a non-exclusive, royalty-free licence for ATT&CK, and it extends to commercial use. Copies are authorised on one condition, quoted here in full:

> "Any copy you make for such purposes is authorized provided that you reproduce MITRE's copyright designation and this license in any such copy."

The designation, verbatim: "© 2026 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation."

Source: `attack.mitre.org/resources/terms-of-use`, read 14 November 2026.

This is the one upstream source in the Vyber07 card that is genuinely redistributable, and it comes with a condition that is easy to test: does the required sentence appear anywhere in the repository or the card. In the case at hand, it does not.

### OWASP

Generally CC BY-SA for written material, which requires attribution and share-alike. **Not verified for any specific document here.** Treat as conditional and check the document before citing.

## Open, in principle

- **NVD**: a US government work, redistributable. Not verified for this dataset.
- **CISA Known Exploited Vulnerabilities**: US government work. Not verified for this dataset.

## Unknown, and therefore blocked until read

- **SANS Institute** white papers: copyrighted to SANS and the authors. No redistribution terms were read, so nothing may be assumed.
- **VulnHub**: each virtual machine carries its own author's terms, which vary.
- **pwn.guide**, **PwnTillDawn**: not read.
- **Bugcrowd**, **HackerOne**: platform content, terms not read.

## How to use this table

A dataset that lists twelve upstream sources, of which three are blocked outright and one is conditional with an unmet condition, cannot be redistributed as a whole under Apache 2.0. That does not make it worthless. It makes it a corpus that may be read by the person who assembled it and may not be passed on, which is the opposite of what a published dataset is for.

The distinction that matters in a client conversation is between the rights you hold and the rights you were told about. This table is only ever about the second.
