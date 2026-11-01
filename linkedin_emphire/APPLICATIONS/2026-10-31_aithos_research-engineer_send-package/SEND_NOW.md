# Aithos application: send package

**Due: today, 31 Oct 2026.** Deadline item #1 in `context.md` section 10.
Everything in this folder is built and verified. The only thing left is pressing send.

- `Aithos_application_Olusanya_Timothy.eml`: complete email, resume already attached. Verified by round-trip parse: subject, from, to, 527-word body, one 29 KB PDF attachment.
- `letter.txt`: the body on its own, in case you would rather paste it.
- `original_appendixA_letter.txt`: the untouched text from `context.md`, kept for diffing or rollback.
- `build_eml.py`: rebuilds the `.eml` from `letter.txt`. Run it if you edit the letter. It never sends anything.

---

## Send it, three ways

**1. The `.eml` (fastest, keeps the attachment)**

Open `Aithos_application_Olusanya_Timothy.eml` in Gmail, Apple Mail, Outlook or Thunderbird. It loads as a draft with the recipient, subject, body and resume in place. Read it once, press send.

```bash
# from a Linux box, if you want the draft sitting in Gmail
xdg-open Aithos_application_Olusanya_Timothy.eml
```

**2. Gmail compose (cleanest if you are on the web)**

Copy `letter.txt`, paste into a new message. To `hiring@aithos.org`. Subject below. Attach `RESUME/Timothy_Olusanya_Aithos_Research_Engineer.pdf`.

```
Subject: Application, Research Engineer, Olusanya Timothy
```

**3. Terminal (no GUI in the way)**

```bash
cd /home/user/linkedin_emphire
mutt -s "Application, Research Engineer, Olusanya Timothy" \
     -a RESUME/Timothy_Olusanya_Aithos_Research_Engineer.pdf -- \
     hiring@aithos.org < "linkedin_emphire/APPLICATIONS/2026-10-31_aithos_research-engineer_send-package/letter.txt"
```

---

## Before you press send

- [ ] The recipient is **hiring@aithos.org** and not a `lnkd.in` form. `context.md` section 11 is explicit: email route, not the form.
- [ ] The PDF opens and is **one page**. It is one page; I checked the page count in the file.
- [ ] You are sending from `olusanyatimothy54@gmail.com`, the address on the resume.
- [ ] If you have picked up **Inspect** since 13 Oct, change "I have not used Inspect yet" to "I have started with Inspect". Section 10 step 7 of `context.md` says to update this line. It is the one line in the letter that can go stale.
- [ ] Nothing in the letter is now untrue. See the resume flag below.

---

## What changed, and why

Four edits. The letter was already strong; these are copy-level, no new claims.

| Edit | Before | After | Why |
|---|---|---|---|
| 1 | "is the same **standard** I hold my own work to" | "is the **bar** I already hold my own work to" | "standard" appeared three times in four sentences, reading as an unedited draft |
| 2 | "That is why I publish the harness and make every run **rerunnable**, so a finding can be questioned" | "So I publish the tests and not just the findings, which is the difference between a claim someone has to trust and one they can rerun" | Near-verbatim repeat of paragraph 2 ("rerunnable by anyone who wants to question them"). A reviewer tracking your argument sees a loop, not a build |
| 3 | Breaking AI buried mid-paragraph | Its own paragraph | It is your second piece of evidence. It was sharing a paragraph with the "why Aithos" argument |
| 4 | no mention of the attachment | "My resume is attached, and the harness repository is public if you want to read the code before we speak" | The original never acknowledged the attached file, and gives them a reason to look at the repo before the screen |

Voice lint: **0 errors, 0 warnings** on the `email` profile. Zero em dashes. 527 words.

```bash
python3 linkedin_emphire/TOOLING/voice_lint.py --profile email \
  "linkedin_emphire/APPLICATIONS/2026-10-31_aithos_research-engineer_send-package/letter.txt"
```

---

## Two flags before you send

**1. The resume has a number that does not add up.** `RESUME/Timothy_Olusanya_Aithos_Research_Engineer.docx`, AI Safety section, second bullet:

> "ran six structured prompt-injection tests before launch; **four** succeeded (system prompt leakage, an unauthorized refund commitment, a policy bypass)"

Four named outcomes, three listed. To a research org whose whole filter is reproducibility, this is the exact kind of inconsistency they are trained to notice. Either name the fourth or write "four succeeded, including". Takes ten seconds and it is worth doing before the letter goes.

**2. LARA is not mentioned anywhere in the letter.** Aithos ships LARA (`lara.aithos.org`), an open alignment tool. Their own stated mission is open tooling, and you are applying as the person who ships open tooling. If you have actually looked at LARA, one sentence near the top of paragraph 3 pays for itself:

```
Your LARA tool is the version of that argument I can point at: an alignment
question turned into something people can run.
```

Only use it if you have opened LARA. If you have not, skip it. Do not claim it.

---

## Not touched, flagged for later

Two repo problems I found while reading, both left alone because they are not today's job:

- **108 tracked files match your own `.gitignore`** (`uploads/` with 20 photos of your face, `.history/` with 88 snapshot files). `.gitignore` says "personal face assets, never commit (repo was public)". They were committed before the rule and are still in history on a public repo.
- **124.7 MB of duplicate files across 181 groups**, mostly `THE VISUAL DESIGNER/` and `linkedin_emphire/TOLU TEMPLATE/` holding byte-identical PDFs, plus a root-level copy of `linkedin_emphire/`. That is why the checkout is 271 MB.

Say the word and I will clean both up on a branch. Not before the email goes.
