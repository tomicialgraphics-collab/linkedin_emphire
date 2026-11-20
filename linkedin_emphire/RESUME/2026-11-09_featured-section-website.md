---
deliverable: doc
id: 2026-11-09_featured-section-website
date: 2026-11-09
audience: owner
status: ready
approved: no
warm: no
thread: whether olusanyatimothy.vercel.app belongs in the LinkedIn Featured section, what the card should say, and what it exposes
verified: read on 9 November 2026 from the live site (home, contact) and the CV PDF served from it. The Open Graph tags could not be checked from here because this environment reaches only GitHub, npm and PyPI, and the page reader returns text without head metadata. The preview-card question is therefore left open rather than assumed.
---

# The website, as a Featured item

## Verdict

Yes. Add it, and add it first. It is the only thing you own that survives being clicked cold by somebody who has never heard of you: four open harnesses, twelve projects, three blog posts, a CV, and a contact route that answers. The launch post proves you can think. The site proves you can ship and that the artefacts exist.

Order matters, because Featured is a horizontal row and mobile shows roughly one and a half cards. Add in this order:

1. **The website.** Everything that follows is a detail inside it.
2. **The playbook launch post.** The proof of thinking, and it drives to the repository.
3. **Optional: your CV PDF.** `https://olusanyatimothy.vercel.app/olusanya-timothy-resume.pdf`. Recruiters like a CV card they can click without asking.

Skip a separate card for the repository. The post already carries it, and a GitHub card shows a star count of zero, which is a detail you do not need to put on your own profile.

## The card text

LinkedIn lets you edit the title and description in the add dialog before you confirm. Type these rather than accepting whatever the site's metadata says, because the scraped version is usually the page title and it buries the argument.

**Title** (59 characters, fits the card without truncating)

```
AI red teaming and evaluation, documented and re-derivable
```

**Description** (148 characters)

```
Four MIT-licensed harnesses, twelve shipped projects and the notes behind them. Every verdict can be re-derived from stored raw output, offline.
```

Alternates if you want the card to read as a person rather than a practice:

- Title: `Olusanya Timothy · AI red team and evaluation` (46)
- Title: `Portfolio: red teaming, evals and the tools behind them` (56)

Do not write "portfolio" in the description and again in the title. One of the two should carry the argument.

## How to add it

1. Profile, **Add profile section**, **Featured**, **Add**, then **Add a link**.
2. Paste `https://olusanyatimothy.vercel.app/`. Wait for the preview to appear before touching anything.
3. Overwrite the Title and Description with the two blocks above.
4. Check the preview image before you confirm. See the next section.
5. Add, then repeat for the launch post (choose **Posts**, not a link) and, if you want it, the CV.
6. Ten minutes later, open the post and use **Pin to top** from its menu, if you still want the post first. If the site should be first, do not pin the post.

## The one thing I could not check

The card thumbnail comes from the page's Open Graph image. If the site has one, the card renders as an image and a title. If it does not, the card renders as a grey placeholder with the domain, which looks broken next to your other items.

You will see which one it is in the dialog in step 2. If it is grey, tell me and I will draw a 1200 by 627 card in the same ink, paper and accent as the playbook banner, plus the four lines of Next.js metadata to paste into the layout. Do not settle for the grey box on the item that is meant to be the first thing a stranger sees.

## What the click exposes

This is the part worth acting on before you add it, because the site raises the standard the profile has to meet.

- **The CV and the profile disagree about who employs you.** The CV says `Independent AI security research, 2026 - present`, and it never names Teamart Inc. The profile leads with Teamart from May 2025. A recruiter holding both documents asks what Teamart is and gets no answer from the CV. One fix: change that CV heading to `Teamart Inc. · independent AI security research`, so the same name appears in both places.
- **The CV is the good document.** It carries `14/14 verdicts re-derived`, `0 FP / 0 FN`, `7 findings from 11 attacks`, `140+ routes, 70 models, 898 tests`, and Python is now supported by four projects instead of being a claim in a skills table. The profile's Experience entries carry none of this. That gap is what the rewrite of the other three entries fixes.
- **Dates still need your answer.** The site and CV say software since 2024. The profile has Corewell from February 2023. That is defensible, since Corewell is creative direction rather than engineering, but only if the entry says so.
- **The email is right.** `olusanyatimothy54@gmail.com` on the contact page and in the CV header. No other address appears anywhere on the site.

## What is good, and should not be changed

The hero line, `I build the system, then try to break it`, does in nine words what the whole LinkedIn headline is trying to do. The evidence bundle panel above the fold is the strongest single element on the page, because it shows a verdict and then shows that a stranger can re-derive it. The contact page explains the next three steps, which most portfolios skip. Nothing on the site overclaims, and nothing names an employer it cannot defend.

No trace of the retired brand appears anywhere in the text of the pages read, at the footer or elsewhere.
