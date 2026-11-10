# SESSION CONTEXT: AI Safety / Eval Engineer, Brand + Applications

> Read top to bottom before acting. This is the handoff for the next session.

- **Updated:** 2026-11-06 (Lagos, UTC+1)
- **Session branch:** `arena/70379866-linkedin-emphire` (branched from `main`), pipeline work landed 2026-11-06
- **Repo:** private development copy; the public profile repo is `Teamthy/ai-redteam-five-tests`. Never name the
  development repo's organisation in anything outward (rule R03).

---

## 0. Read this first (added 2026-11-06)

This file is the handoff, not the rulebook. The rulebook is the pipeline:

1. `AGENTS.md` at the repository root, the contract for any session.
2. `linkedin_emphire/PIPELINE/00-START.md`, the read order.
3. `linkedin_emphire/PIPELINE/20-RULES.md`, 30 numbered rules, 23 of them blocking, generated from
   `PIPELINE/registry/rules.json`.
4. `linkedin_emphire/PIPELINE/50-CONTRACT.md`, the front matter every deliverable carries.
5. `linkedin_emphire/STATE/OPEN-LOOPS.md`, what is unfinished.

Then, before anything leaves the repo:

```
python3 linkedin_emphire/TOOLING/pipeline.py check <path>
```

Everything below is still true. It is the story; the pipeline is the enforcement.

---

## 1. The one-paragraph picture

The owner is a self-taught **software engineer who builds and tests AI for safety** (evaluations, red-teaming, reproducible harnesses). Two parallel tracks: (a) building a public brand to become known in the AI safety / evaluation space, and (b) using that brand to get hired into a research / evaluation role. The public brand is a LinkedIn comment engine plus the "Breaking AI" article series plus an open-source five-test red-team harness. The **Aithos Research Engineer application** was submitted 31 Oct 2026 (see section 6); the live priority is now the follow-up cadence and the in-lane comment set in section 10.

---

## 2. Who the owner is

- **Name:** Olusanya Timothy
- **Contact:** olusanyatimothy54@gmail.com · linkedin.com/in/olusanya-timothy · github.com/Teamthy · Lagos, Nigeria (UTC+1)
- **Role now:** Software Engineer, AI Integration & Red Teaming, Teamart.inc (Lagos, Jul 2025 - present). Previous: Senior Developer, YKAY ConsultingHub (Nov 2024 - Jun 2025).
- **Background:** Self-taught. BSc Computer Science, National Open University of Nigeria, expected Apr 2028 (studying while working). Prior academic background in Medical Laboratory Science.
- **Positioning:** the build-and-test side of AI safety. Designs and runs reproducible evaluations, and builds the harnesses so every result traces to a prompt, model, and commit. A practitioner who engineers the verification layer, NOT a formal ML researcher (no peer-reviewed papers). Own this honestly; it is an asset for a Research Engineer (engineering) role.
- **Certs:** NIST AI Bootcamp (AI Risk & Safety Frameworks); AI Engineering & Backend (Udemy); self-directed backend.

---

## 3. What exists (the body of work)

- **Five-test red-team harness:** `github.com/Teamthy/ai-redteam-five-tests` (public). Runs prompt injection, retrieval poisoning, tool-description poisoning, and multilingual refusal against any OpenAI-compatible model. Resolves tool calls, records raw responses, reports each failure with its sample size and rate. Reproducible (traces to prompt + model + commit).
- **Breaking AI series:** public, 21-part plan. Articles 1 and 2 published (Oct 6 and Oct 13, 2026). Article 2 is the honest "the tell" (no fabricated lab numbers; it ships the METHOD, a runnable harness, so the reader gets their own real results).
- **Aithos-tailored resume:** 1 page, well-designed. `RESUME/Timothy_Olusanya_Aithos_Research_Engineer.{pdf,docx}`. Generator: `linkedin_emphire/RESUME/build_resume_aithos.py` (FPDF + python-docx, DejaVu fonts). Title line: "Software Engineer, AI Evaluation & Safety Tooling".
- **Older resume (already public):** `linkedin_emphire/RESUME/Timothy_Olusanya_AI_ML_Engineer.{pdf,docx}` + `build_resume.py`.
- **Article 2 assets:** hero portrait (cinematic, navy/cyan data center, Base Neue), white in-article cards, 1200x628 cover + 1200x675 share. In `ARTICLES/2026-10-13_article-2_five-boring-failure-modes/`.

---

## 4. Git status of the resume PDF (important for the PR)

- As of this session, the top-level `RESUME/` folder (the Aithos PDF + DOCX) is **UNTRACKED** in git. So the Aithos resume is **NOT** in `main` and will **NOT** be in a PR unless it is explicitly `git add` + committed to the branch.
- The **older** AI/ML resume IS already committed and public in `linkedin_emphire/RESUME/`.
- **Open decision for the owner:** whether to commit the Aithos resume to this **public** repo. Doing so makes it publicly viewable (consistent with the older resume already being public). Confirm before committing.

---

## 5. Deadlines

- ~~**31 Oct 2026:** send the Aithos application email (resume PDF + motivation letter) to **hiring@aithos.org**.~~ **DONE 31 Oct 2026.**
- **Follow-up clock:** if there is no reply by **14 Nov 2026** (two weeks), send one short, warm follow-up to hiring@aithos.org referencing the original subject line. One bump only. Do not chase Lauren on LinkedIn (Premium still off below 1k followers).
- **[un]prompted registration:** Oct 27-29, SF (owner to decide whether to register).
- **Article 2 launch posts** (relative to the Oct 13 publish): a 10:00 WAT link post, a quote-card post, save / checklist posts.

---

## 6. State of things

### Done
- **Aithos application SUBMITTED 31 Oct 2026** to hiring@aithos.org, before the deadline. Four copy edits applied to the letter first (repetition cut, attachment line added, Breaking AI given its own paragraph). Lint: 0 errors, 0 warnings, 0 em dashes.
- Aithos resume (1-page PDF + DOCX, verified one page).
- Aithos motivation letter (paste-ready; full text in Appendix A).
- Article 2 published (Oct 13).
- Harness repo published; first comment with the repo link posted.
- Many LinkedIn comments LIVE: Rock [un]prompted; Musk/Cursor; Zuckerberg; Cheeky Pint x2; 1900 template letters; models-as-insider-risks; service-credentials; REA; Aithos/Lauren x2.
- Paolo Perrone engaged the owner's post (affirmed "a manipulated agent looks healthy on every dashboard"); a punchy reply is ready (Appendix B).

### Pending (owner to send or do)
- ~~Send the Aithos email~~ **DONE 31 Oct 2026.** Package of record: `linkedin_emphire/APPLICATIONS/2026-10-31_aithos_research-engineer_send-package/` (final letter, `.eml` with resume attached, send log in `SENT.md`).
- Post the Paolo reply (Appendix B).
- Post the in-lane comment drafts (Appendix C): Catasta (strongest of the batch), Replit "AI native = code", Hamel, Zenity/SSRF, Lenny, Clint. Space them out.
- Send Sudhir follow-up (Upwork $65 milestone + LinkedIn ping) after the consultation call (Appendix D).
- Send the AEC application (Upwork, $4,000 fixed) (not sent).
- Raymond (Orcrux) DM close. Other pending DMs (Nanna first DM, Suphi, etc.).
- Article 2 launch posts.

### Intentionally skipped this session (do not force)
- Google Cloud / Deloitte "Agentic blueprint" (vendor promo).
- AI News World Zuckerberg/Wang (hype; redundant with the live Zuckerberg comment).
- Amjad Masad partner-program post (commercial; a third Replit touch; weaker than the in-lane Replit ones).

---

## 7. Standing rules (do NOT break)

- **No em dashes** in any owner-facing content (comments, articles, resume, emails). Use commas, periods, colons.
- **No fabricated numbers or results.** Real runs only. If there is no model access, use the honest "the tell": ship the method, no invented counts or rates.
- **Never reference `tomicialgraphics` in any deliverable (owner instruction, 2026-11-04).** No repository URL, no account name, no handle, no email variant, in anything a client, reviewer, hiring team or vendor receives. That includes the public repository `tomicialgraphics-collab/linkedin_emphire` and every GitHub link built from it. Pinned revisions are identified to outsiders by commit SHA and file SHA-256 only, never by URL. Deliver review artefacts as files (Drive link or attachment) with a hash in the message. Internal repo paths inside the owner's own files are fine; anything outward-facing is not.
- **Contact address (owner instruction, 2026-11-04):** `olusanyatimothy54@gmail.com` is the only address used for applications, outreach, vendor files and anything a hiring team or protocol author receives. **Never use `tomicialgraphics@gmail.com`** for outbound contact, never put it in a deliverable, and never name it as the owner's address. It is already public twice over: it sits in the Contact info on the LinkedIn profile, and it appears as the author of one commit in the public repository `tomicialgraphics-collab/linkedin_emphire`. Treat it as burned for outreach. Commits made from now on use the GitHub noreply identity, so the leak is historical, not ongoing.
- **Every link a post attaches is read before anything is written about it (owner instruction, 2026-11-09: "please always read it").** The read-more, the paper, the SSRN copy, the film, the waitlist, the publisher page, the repository, the other post it quotes. Reading the post is not reading the link, and summarising a source is not reading it. If a link will not open, say so in the deliverable and in the `sources_read:` line rather than writing beside it in silence. Applies to comments, replies, DMs and anything quoted back at a client. Enforced by R26 from 2026-11-10 on comments and DMs.
- **Two exchanges per thread, then stop (owner instruction, 2026-11-09, recorded as R34).** The other person keeps the last substantive word. A third reply is an argument, and an argument under somebody else's post reads as a fight.
- **A claim about somebody else's system names the version and the surface (R35).** A proof on an internal path is not a capability. Say which was tested, every time, because that difference was the whole FORAY finding on 9 November.
- **Every hash, byte count and word count is recomputed in the same command that writes the letter (R36).** A hash copied from an earlier message is a claim about a file that may have changed since.
- **A question the owner has answered twice is not asked a third time (R37).** Record the choice and the date, and work from it. He has chosen Drive links twice; the caveat is closed.
- **No filename with an extension in text a human pastes (R32).** It autolinks to a dead address. Name the file without the extension and let the URL carry the path. Caught in the launch first comment, which named a script as `wilson.py`.
- **A fact that moves is checked the day the comment is written (R33).** `premise_checked:` in the file says which fact, where it was checked, and when. Prices and counts are dated or they are wrong later.
- **A direct question is answered within a day, or acknowledged with the day it will be (R38).** The queue is `linkedin_emphire/STATE/REPLY-QUEUE.md`, with date received, date due and state. Checking it is the first thing a session does.
- **No comments on reposts (R39).** A repost carries no author argument, so a substantive comment under one is a broadcast. The one exception is a repost that carries the author's own writing around it, and the file says so.
- **Every post carries a real number, or says in the text why it has none (R40).** R06 still owns the figures: the number is from a run that happened, or the post states the method and says there is no run. A post with no number and no reason is unfinished.
- **Every session opens with the pace reading and the reply queue (R41).** `python3 linkedin_emphire/TOOLING/pace.py`, then `STATE/REPLY-QUEUE.md`. No post ships on a day whose `analytics/follower-log.md` row is missing. The weekly review template is `PIPELINE/70-WEEKLY-REVIEW.md`, output to `STATE/REVIEWS/`, and one of its three decisions is always what to kill.
- **Borrowed audiences are a board, not a hope (R42).** `STATE/BORROWED-AUDIENCE.md`: two asks a week to a named host via a named route, a follow-up date seven days out, and nothing sent by the agent. An ask that is not a row did not happen. This is the only lever with a lead time in weeks, and it is the one that fails silently.
- **Client work becomes a case study only with permission in writing (R43).** `PIPELINE/80-CASE-STUDIES.md`, indexed in `STATE/CASE-STUDY-INDEX.md`. Draft first, then ask at the first milestone, never at the end. The gate blocks a case study at `status: ready` until the front matter says `permission: granted`.
- **A session starts with `./emphire start`, which now prints what is late and what is due (R41).** Four lines: pace, late replies, borrowed asks sent in seven days, case studies awaiting permission.
- **PII:** never hand the owner's resume / contact a public link to a hiring manager (owner declined that). The repo itself is public and already holds an older resume, so anything committed here is public. Confirm with the owner before committing new PII to the public repo.
- **Every daily post ships with a HEADLINE and a SUBHEADLINE** (owner instruction, 2026-10-31). Not optional, not only when asked. The headline is the memorable line and goes first. The subheadline carries the number or the stakes and must add something the headline does not say. Together they have to land inside the first ~200 characters, because that is what shows before "see more". They are the post's first two lines, and the same pair is reused as the card or article title and deck. Give one recommended pair plus two alternatives. No em dashes in either, no banned words, no clickbait, and no question in the headline.
- **The first line must force the "see more"** (owner instruction, 2026-11-01). Under 120 characters, no question, no greeting, and incomplete without the next line. Use one of three mechanisms: a number that fights its own unit, a contradiction in two clauses, or a cost stated flatly. If the headline already hooks, it IS the first line and you do not add another. Full rules and the three approved cards are in `linkedin_emphire/DAILY CONTENT/visual_and_hook_spec.md`.
- **Every post names the words to box in its visual** (owner instruction, 2026-11-01). One boxed phrase per card, one to three words, never opening line one. Box the quantity or the failure verb, never the topic. It must pass the portability test: if the phrase could headline a different post by a different writer, it is wrong. Give a primary box and one alternative, and say which is stronger and why.
- **Everything ships through the human gate** (owner instruction, 2026-10-31). Before any deliverable is called done, run `python3 linkedin_emphire/TOOLING/voice_lint.py --human <file>`. Target 90 or above with zero errors. The gate scores rhythm, not vocabulary: triads, repetitive sentence openings, sentence-length variance, hedges, missing contractions, and paragraphs with no terminal punctuation. Vocabulary and the em-dash rule are already covered by the base lint. Proper punctuation means every paragraph ends in a full stop, comma, colon or question mark, no doubled words, and a space after every comma.
- **Every session writes its own log** (owner instruction, 2026-10-31). Append to or create `SESSION_LOG/SESSION_LOG_<date>.md` capturing each user instruction, each decision, each artifact with its path, the open loops, and anything a future session would otherwise have to re-derive from chat. Record the reasoning, not just the output. If an instruction in the chat is not in the repo, it will be lost, and losing it costs the owner work he has already paid for once.
- **Comment style (current, as of 2026-10-13):** punchy, multi-paragraph, one idea per breath, short lines. Concede first (acknowledge the post's point). One memorable line. Plain connectives. End on a statement, not a question (a light offer is fine in a warm reply). Confident peer tone, never sycophantic. No links in cold comments (links are OK in a warm reply, or where one was already posted).
- **No edits to live Upwork or LinkedIn** without owner approval.
- **Sudhir $65** via a fixed-price milestone; no public Sudhir post.
- **Article hero templates:** geometry and colors are LOCKED (per the approved references). Per-article changes are copy plus a generated background photo only. Do not redesign.
- **No AI face generation** of the owner. Use real photos.
- **Fonts:** Base Neue / Basis Neue (licensed) for article cards; use the Expanded members for the hero.
- **Upwork strategy:** 2 listings x 3 tiers (from research); 3 changes already applied by the owner on 2026-10-11.

---

## 8. Voice and signature lines

Plain, direct, human. Concede before pushing back. One memorable line per piece. End on a statement. No hype, no invented metrics. The owner is a practitioner building reproducible evidence, not a slogan-shouting safety advocate.

Signature moves to reuse:
- "can I run this" -> "can I verify this"
- attention is not trust
- treat retrieved context and tool output as untrusted input
- the control lives at the boundary, not in the prompt
- the boring failures are the ones that ship
- you can't find it by monitoring; you find it by adversarially testing it before the person doing it on purpose does
- it's code that's been checked

---

## 9. Key people and relationships

- **Aithos (the target):** a Dutch ANBI non-profit, Amsterdam; AI alignment research (systemic alignment, procedural legitimacy, human autonomy and pluralism). Hiring contact: **Lauren Toulson** (AI Researcher, ex-UK AI Security Institute). Others: Nadia Kadhim (Exec Dir), Daan Henselmans (Research Dir). Open tool: **LARA** (lara.aithos.org). Published alignment-eval work (e.g., low-temperature evals can mask behavior; a European model "can't follow European law"). Role flow: 30-min screen -> ~3-hr take-home on a real eval -> 60-min technical.
- **Paolo Perrone:** author of "Shipping Production AI" (agents, inference, GPU), 1M+ readers. In-lane. Engaged the owner's post; reply ready.
- **Rock Lambros (Zenity):** top-tier in-domain (OWASP agentic security). Liked the owner's [un]prompted comment.
- **In-domain voices the owner engages:** Hamel Husain (evals / debugging), Zenity / Michael Bargury (agent security, SSRF), Clint Gibler (data / RAG), Lenny Rachitsky (founders, moats), Ruben Hassid (practical AI), Amjad Masad + Michele Catasta (Replit).
- **Sudhir:** consulting client; $65 milestone pending on Upwork; consultation call (confirm done + follow up).
- **Raymond (Orcrux):** DM close pending.
- New follower: Victor Cardenas (Global Payment Partnerships).

---

## 10. Immediate next steps, in order

1. ~~**Send the Aithos email**~~ Sent 31 Oct 2026. Next: log the reply (or the silence) in `2026-10-31_aithos_research-engineer_send-package/SENT.md` as it lands, and set the two-week follow-up for 14 Nov.
2. Post the **Paolo reply** (Appendix B).
3. Post the in-lane comment drafts (Appendix C), spaced out: Catasta first (strongest), then Replit "AI native = code", Hamel, Zenity/SSRF, Lenny, Clint. Watch for author replies.
4. Send **Sudhir** the Upwork message + LinkedIn ping (Appendix D).
5. Send the **AEC** application (Upwork, $4,000).
6. Raymond close + other pending DMs.
7. (Optional, high-leverage) build ONE "eval study" artifact to bridge practitioner to researcher: a clean, reproducible evaluation (a real question, a defined sample, results with sample size and rate, limitations, a runnable script). Real numbers only. This is the highest-leverage new piece for a research org. The letter currently says "I have not used Inspect yet"; if the owner picks up Inspect before sending, update that line.

---

## 11. Dead ends (do NOT retry)

- **GitHub PRIVATE resume hosting** from the sandbox: not possible (the GitHub App token is scoped to `linkedin_emphire` only; gists cannot hold binary files).
- **Google Drive upload** from the sandbox: connector action tools are not invocable.
- **Typed e2b download links:** dead (sandbox recycle invalidates the sandbox id and kills background servers; the public e2b host 502s).
- **tmp_dl download-page route:** abandoned, do not re-stage.
- **Aithos application method:** EMAIL (hiring@aithos.org), not the lnkd.in form. A direct LinkedIn DM to Lauren is blocked (LinkedIn Premium is off until 1k followers; currently ~485).
- **Pushing to `Teamthy/ai-redteam-five-tests`** from the sandbox: not possible (token scoped to `linkedin_emphire` only); the owner built and pushed it externally.

---

## 12. Repo and file map

Restructured 2026-11-06. The root is now thin on purpose: boot files, launchers, and nothing that
could be mistaken for a second copy of the work. Everything else is inside `linkedin_emphire/`.

**Root**

- `AGENTS.md` = the contract for any session or agent. Read before acting.
- `README.md` = the map for a human in a hurry.
- `context.md` = this file, the handoff.
- `emphire` and `emphire.ps1` = the pipeline commands, for bash and for Windows PowerShell 5.1.
- `books/`, `manual/`, `host-failure-benchmark/`, `google_drive/`, `uploads/` = inputs and mirrors,
  not part of the pipeline, never a deliverable.

**Inside `linkedin_emphire/`**

- `PIPELINE/` = the rules, stages, contract and roles. `registry/*.json` is the only place a rule,
  template or hashtag is defined. `20-RULES.md`, `30-TEMPLATES.md` and `40-HASHTAGS.md` are generated
  from it, so they cannot drift.
- `TOOLING/gate.py` = enforces every automatable rule, reads front matter, exits non-zero when a file
  would fail one. `TOOLING/pipeline.py` = start, status, check, log, audit, render, map, loops.
- `TOOLING/voice_lint.py` = vocabulary and rhythm. `TOOLING/md2html.py` = markdown to a page.
- `STATE/OPEN-LOOPS.md` = the only list of unfinished work. `STATE/DELIVERY-LOG.md` = every file that
  left, with size and SHA-256. `STATE/GATE-REPORT.md` = the generated scoreboard.
- `MAP.md` = generated index of every folder, its purpose, its role and its stage.
- `DAILY CONTENT/` = the editorial canon: `post_templates.txt`, `visual_and_hook_spec.md`,
  `banned_words.txt` (the 84-entry list), `voice_dna.txt`, `master_prompt.txt`, `content_bank.txt`,
  `content_strategy.txt`, `inspiration_library.txt`, `drafts/`. `_variants/` holds superseded copies
  kept for the record, never the canon.
- `VERIFIED_POSTS/` = one folder per post, `INDEX.md`, and 25 legacy posts that predate the contract.
- `RESUME/` = PDFs and DOCX for three roles (AITHOS MTS, Aithos Research Engineer, Anthropic Fellows).
  PII. Never linked publicly.
- `CLIENTS/`, `PROJECTS/`, `OUTREACH/` = client work, named projects, confidential working files.
- `ARTICLES/`, `CONTENT/`, `CONTENT_CALENDARS/`, `LINKEDIN/`, `PUBLISH/` = content pipeline.
- `ENGAGEMENT/`, `NETWORKING/` = comments, DMs, contacts.
- `OPPURTUNITIES/`, `UPWORK/`, `APPLICATIONS/`, `EMAIL/`, `LEADS/` = opportunities and applications.
- `DESIGN/`, `VISUAL/`, `ASSETS/` = card geometry, brand rules, photographs.
- `EMPIRE/`, `STRATEGY/`, `PLANS/`, `analytics/` = the operating layer.
- `SESSION_LOG/` = one log per working day, 2026-10-31 onward.
- `ARCHIVE/` = superseded files and `RESTRUCTURE-2026-11-06.md`, the record of the restructure.

---
---

# APPENDIX (paste-ready drafts)

## Appendix A: Aithos motivation letter (FINAL, send-ready)

Subject: Application, Research Engineer, Olusanya Timothy

To the Aithos team, I am applying for the Research Engineer role because it is the closest match to what I actually build. I work on AI safety from the build-and-test side: I design and run evaluations that check whether an AI system does what it should under the conditions a real user or a regulator would test, and I build the code so those checks are reproducible, public, and rerunnable by anyone who wants to question them.

The most direct proof is a five-test red-team harness I published (github.com/Teamthy/ai-redteam-five-tests). It runs prompt injection, retrieval poisoning, tool description poisoning, and multilingual refusal tests against any OpenAI-compatible model, resolves tool calls, records the raw responses, and reports each failure with its sample size and rate. It is written to the standard the role asks for: clean, tested, documented Python that others can build on, not a one-off script. Every result traces back to a specific prompt, model, and commit, which is the part I care about most. I would not report a number I could not reproduce.

That reproducibility mindset is why Aithos stands out to me. Turning every piece of research into a benchmark, open tooling, or reproducible methodology, and making work that regulators and other teams can actually use, is the same standard I hold my own work to. It is also the standard your principles describe: the values a model encodes should stay open and contestable rather than converge on one ideal, and a result is only as strong as the method that produced it. That is why I publish the harness and make every run rerunnable, so a finding can be questioned, not just trusted. My public series, Breaking AI, applies it to the question I started from: shipping AI that survives real users. The failures I write about are the boring ones (the prompt is not a wall, retrieved documents are untrusted input, tool descriptions are trusted unread, test sets that only cover one language), and the controls I recommend are engineering controls, not slogans.

A few things I want to be straight about. I am a self-taught practitioner, not a formal ML researcher, so I have no peer-reviewed papers. I have published a public, reproducible body of work instead, and I build with the discipline the role describes: safe sandboxes for code-running agents, careful handling of credentials, and a habit of checking AI coding output rather than trusting it. I have done tool-calling and agentic scaffolding but less formal multi-agent simulation, and I have not used Inspect yet; both are quick for me to pick up given the evaluation work I already do. I am based in Lagos (UTC+1), so my hours line up with Amsterdam, and I can work remotely; I am open to discussing the in-person days.

I would welcome the screening call, and honestly the three-hour take-home on a real Aithos evaluation is the part I would most like to do.

Olusanya Timothy
olusanyatimothy54@gmail.com · +234 812 786 8211 · linkedin.com/in/olusanya-timothy · github.com/Teamthy

---

## Appendix B: Paolo Perrone reply (punchy)

Thanks Paolo. Genuinely appreciate you saying that.

"Second list" is exactly the right frame.

The first list shows up. Timeout, retry, latency spike. You can watch it, so you can fix it.

The second list is built not to show up. A manipulated agent runs clean. Calls logged, latency normal, cost normal. Healthy on every dashboard.

You can't find it by monitoring.

You find it by adversarially testing it before the person doing it on purpose does.

That's the whole reason I've been writing it down.

The five-test harness I just published (github.com/Teamthy/ai-redteam-five-tests) is the second list, made runnable. Prompt injection, retrieval poisoning, tool description poisoning, multilingual refusal. Against any OpenAI-compatible model, and every failure traces to a prompt, a model, and a commit.

Happy to send you the full list and the method, or walk through it on a call.

---

## Appendix C: In-lane comment drafts (this session)

### C1. Michele Catasta (Replit President & Head of AI), safety vs cybersecurity

The safety-versus-cybersecurity split is a fair way to frame it, and "move part of the team onto security until we're out of this phase" is the line I'd repeat. But I'd push on where the split actually holds, because in a live coding agent the two stop being separable. A prompt injection that makes the agent fetch an internal URL or fire a tool call with too much scope is, in the same minute, an AI-safety failure and a cybersecurity breach. That's not a long-tail risk; it's a today incident. So "cybersecurity is the today problem" is doing double duty: it already contains the AI-safety surface, and you can't staff for one and defer the other. The control that matters lives at the boundary, egress policy, scoped credentials, least privilege, treating every tool call and retrieved document as untrusted input, and that's the part that's chronically underfunded. And once the security team is "managing security agents," the daily discipline is the one I'd push: run the adversarial evals against your own agent before it ships, not after. The org that treats its agent as an adversary internally is the one that ships the safe one externally.

### C2. "AI native = code" (Daniel Bulteel / Replit, reposted by Amjad Masad)

The "AI native means code, not a pile of apps" point is the right one. The Paul Graham line is the one I'd put on the wall: the deepest change takes the form of code. But there's a missing piece, and it shows up fast once the marketer, the ops manager, and the account manager all start shipping AI-generated code. The bottleneck stops being "can I build this?" and becomes "can I trust what I just built?" When code comes out of a model at the speed of a prompt, nobody is reading every line before it ships. So the check has to move up a layer: tests and evals that catch the failure before the user does, not a review of a file no one can trace. The AI-native org that isn't instrumenting its AI output isn't moving faster, it's just scaling unverified code. The deepest change isn't just code. It's code that's been checked.

### C3. Hamel Husain (debug multi-turn LLM traces)

First upstream failure is the whole game, because LLM traces compound. A small mistake three turns back, a mis-extracted field or a tool called with the wrong argument, silently poisons every turn after it. So the user-visible break almost always points at the symptom, not the cause. I debug by slicing the trace to the smallest step that fails and reproducing just that step in isolation: one input, no conversation history, so the failure is deterministic. That is why I keep my tests small and isolated instead of one big end-to-end run. A minimal repro is the difference between "the chat got weird" and a specific, fixable, re-testable bug.

### C4. Michael Bargury / Zenity (Bedrock AgentCore SSRF)

"Threat model with the agent itself as the adversary" is the frame I keep. The model has no idea that the internal metadata endpoint is off limits, or that the role it runs under shouldn't be readable by the thing running under it. It is a text predictor that does what it is told, and "fetch this URL" is a perfectly normal instruction. So the control can't live in the prompt or in the tool's intent. It has to live at the boundary: an egress policy, a scoped role, an allow-list the model never has to remember. That is the same reason I treat every tool call and outbound request as an untrusted action to check, not a thing to trust because the prompt seemed to want it. A safe default is a boundary decision, not a model decision, and the provider is the one who can actually set it.

### C5. Lenny Rachitsky (moats, data effects)

Data effects is the one I'd push on, because in AI it's not the user-clicks flywheel most people mean. The durable data effect is the eval set: the running record of which behaviors actually break in production and the tests that pin each one down. It compounds, because every incident you catch and codify makes the next launch safer, and it's hard to copy, because you can't buy a competitor's failure history. The part I'd stress is the third step of the framework: measure whether it's working. Most teams can name the advantage; few can point to the metric proving it's still turning. A flywheel you're not instrumenting is a story, not an advantage. And the running record of everything that ever broke, plus the test that stopped it, is the moat that shows up nowhere on the four-list.

### C6. Clint Gibler (data lifecycle / degrading AI usage)

Most of the "degrading AI usage" problem is a correctness problem wearing a governance costume. Stale or duplicated documents don't make the model misbehave the way a prompt injection does, but they make it answer from the wrong source with full confidence, which is retrieval poisoning with staleness standing in for an attacker. The control is the same either way: treat the retrieved context as untrusted input and check it before it becomes an answer. You can't be fined for data you don't have, and you also can't ship a confident wrong answer that came from a file nobody remembered to retire.

---

## Appendix D: Sudhir follow-up (consultation call, Upwork $65 + LinkedIn)

### D1. Upwork message

Hi Sudhir, hope you've been well. I wanted to check in on the consultation call. Could you confirm it's all done on your end? I'd love to hear how it went for you, and if there's anything from the notes you'd like me to clarify or go deeper on. On next steps, what does your side look like going forward? Happy to line things up so we can move forward cleanly. Also, on the $65 milestone on Upwork, could you let me know the status when you get a chance? I just want to make sure it's not stuck on either end so I can wrap up my side. Thanks, Sudhir. Let me know if a quick call is easier.

### D2. LinkedIn ping (money deferred to Upwork)

Hey Sudhir, hope you're doing well. Just following up on the consultation call, how did it land for you? Would love your thoughts and what's next on your side. I'll sort the milestone on Upwork, so keeping that over there.

### D3. Firmer line (only if the milestone is overdue)

The milestone for the consultation call is complete on my end; could you go ahead and approve/release it so it can close out?
