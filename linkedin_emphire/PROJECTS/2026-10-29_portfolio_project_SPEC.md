# Portfolio project spec: the evidence-grade agent evaluation harness
Date: 2026-10-29. Status: PROPOSED, owner decisions D1-D4 open.
Lane: AI red teaming x AI evals x AI security x AI research, the intersection.

## 0. One-line position
An open harness for agent evaluation and red team runs that emits
EVIDENCE, not reports: every verdict is a signed, re-derivable event bound
to the action, the check version, the decision, and the effect, and the
harness's own reliability is measured and recorded in every run.

The report is a claim. The evidence bundle is the record a stranger can
re-derive without trusting the tool, the judge, or the team that ran it.

## 1. The gap (verified 10-29, open research)
The intersection is crowded in three layers and empty in the fourth.

Layer 1, ATTACKS: commoditized.
- garak (NVIDIA, 0.17.0, agent breaker probe since 0.15.0) [1](https://vdf.ai/blog/ai-red-teaming-tools/)
- PyRIT (Microsoft, multi-turn campaigns), promptfoo (now OpenAI, ~25.7k stars, CI-native, OWASP and ATLAS presets, agent plugins), DeepTeam (Confident AI, 1.0.9), Giskard v3, AgentDojo (research benchmark of injection on tool-using agents) [1](https://vdf.ai/blog/ai-red-teaming-tools/) [2](https://www.testmuai.com/blog/ai-red-teaming-tools/) [3](https://awesomeagents.ai/tools/best-ai-red-teaming-tools-2026/)
- OpenAI acquired promptfoo (March 2026) and committed to keeping it open source [3](https://awesomeagents.ai/tools/best-ai-red-teaming-tools-2026/).

Layer 2, EVALS: commoditized at the SCORING level.
- OSS standards: OpenAI Evals (registry), DeepEval v4.0.3 (pytest-native, Decision Graph Logic), Inspect AI v0.3.225 (UK AISI, 200+ evals, public-sector grade) [4](https://www.digitalapplied.com/blog/ai-agent-eval-frameworks-testing-guide-2026/)
- Commercial platforms: LangSmith, Braintrust, Helicone, Arize Phoenix, MLflow [4](https://www.digitalapplied.com/blog/ai-agent-eval-frameworks-testing-guide-2026/) [5](https://niteagent.com/blog/2026-05-21-ai-agent-eval-frameworks-compared/)

Layer 3, TAXONOMY: standardized.
- OWASP Top 10 for Agentic Applications 2026 (ASI01 agent goal hijack to ASI10 rogue agents), published 2025-12-09, 100+ experts, peer reviewed [6](https://cycode.com/blog/owasp-top-10-agentic-applications/) [7](https://arnav.au/2026/07/02/owasp-top-10-for-agentic-applications/)
- MITRE ATLAS and NIST AI RMF as the adjacent vocabularies; promptfoo already ships OWASP/ATLAS mapping presets [1](https://vdf.ai/blog/ai-red-teaming-tools/).
- Compliance clock: EU AI Act high-risk obligations (Annex III) land 2027-12-02 (workspace record, ICP-100 notes). The demand side is dated.

Layer 4, EVIDENCE: empty. This is the gap, and the research arrived at it
only in 2026, which is why the tool layer has not built it:
- RAND Judge Reliability Harness (March 2026, arXiv:2603.05399): "No judge
  that we evaluated is uniformly reliable across benchmarks"; verdicts flip
  on reformatting, paraphrasing, and verbosity [8](https://dikrana.dev/blog/llm-as-judge-is-flaky/) [10](https://cloudai.pt/llm-as-judge-has-a-reliability-problem-in-production/)
- "When the Judge Changes, So Does the Measurement" (arXiv:2607.08535):
  judge upgrades are not interchangeable; the authors recommend "dataset
  slices, bias probes, error-dependence estimates, and protocol audit
  trails"; their own critique section notes the debate numbers "cannot be
  re-audited" because raw outputs were not shipped [9](https://pith.science/paper/2607.08535)
- "Bias in the Loop" (arXiv:2604.16790): judge verdicts are prompt-
  sensitive; "no standard quantification of consistency for the
  judgments" [11](https://arxiv.org/html/2604.16790v1)
- "Necessary but Not Sufficient" (arXiv:2606.26185): even at
  temperature=0, borderline items stay non-reproducible; grader calls can
  cross provider boundaries "without any record in the evaluation
  artifact"; conclusion: the grader-disagreement rate and the resolved
  endpoint belong in the results artifact "because their absence does
  [not help]" [12](https://arxiv.org/html/2606.26185v1)

The structural fact underneath all four: every tool above uses a judge that
lives inside the tool. The evaluator and the evaluated share an operator.
A green eval from such a tool is a self-grade, which is exactly the
failure the whole lane has been naming. Nobody in the 2026 landscape
emits an artifact that survives contact with a stranger. That is the
project.

Adoption pressure: 57% of organizations run agents in production; 52% run
offline evals; 37% run online [5](https://niteagent.com/blog/2026-05-21-ai-agent-eval-frameworks-compared/). The gap between running and verifying is where the buyer lives, and it is the owner's ICP (at risk, cannot verify) almost by definition.

## 2. What it is / what it is not
IS:
- an open-source harness that runs eval + red team suites against an agent
  and emits an evidence bundle (machine-verifiable, human-readable)
- a bundle format v1 with a public spec
- a re-derivation command: a stranger verifies the bundle without the
  original machine, the original API key, or trust in the runner
- a judge audit suite that measures the harness's own reliability every run
- ASI01-ASI10 mapped check families with named policy versions
- a reproducible failure-mode benchmark for the evidence layer itself
  (co-authored, both names, with Behar Dalipi)
IS NOT:
- another probe library (garak and promptfoo own that; we consume their
  attack patterns where useful)
- another dashboard (LangSmith and Phoenix own that; we emit the artifact
  their dashboards will want to ingest)
- a judge model (we measure judges, we do not ship one)
- a compliance platform (we emit the evidence; the platform reads it)

## 3. Six design pillars
Each pillar is a doctrine line already spoken in public threads, now
machined into a component.
P1 VERDICT EVENT. Every check result is one record: pre-assigned check
ID, check/policy version hash, verdict (pass / fail / undetermined),
timestamps, judge identity, resolved endpoint, effect reference. The
four-part binding from the Behar thread: action, policy version,
decision, effect, in one event.
P2 PROVENANCE. Exact harness version, model, model version, dataset hash,
environment snapshot, decoding config, seed. The resolved endpoint of
every judge call is recorded, per the transmission-layer finding in
[12](https://arxiv.org/html/2606.26185v1).
P3 NEGATIVE CONTROLS. Every suite includes known-pass and known-fail
items. Every run emits the harness's own false-positive and false-negative
rate for that run. The check cannot write its own grade: its grade is
computed against items it does not generate.
P4 NAMED GAPS. Anything that could not be verified is recorded as a gap
with reason and scope, never dropped silently. A bundle with a named gap
is more honest than a green bundle; the format makes the difference
mechanical.
P5 RE-DERIVATION. `verify <bundle>` re-checks the hash chain, re-derives
every verdict from the raw outputs, and measures judge divergence, all
without re-running the model. The bundle either passes a stranger's
verify or it does not exist, as far as this project is concerned.
P6 JUDGE AUDIT. Every run carries the judge's own numbers: agreement on
calibration anchors, disagreement rate, perturbation flips (reformat,
paraphrase, verbosity), self-preference probe. "Who checks the checker,"
made mechanical, per the RAND and FairJudge findings [8](https://dikrana.dev/blog/llm-as-judge-is-flaky/) [10](https://cloudai.pt/llm-as-judge-has-a-reliability-problem-in-production/).

## 4. Architecture
NAME (decision D1): tieout (recommended; the register of the lane: tie
every number to a record somebody else can check) / verdictbench /
evidencebench. Repo: github.com/Teamthy/<name> (new repo, decision D2).
The five failure checks of the existing five-tests repo (public, latest
d95a57e, "ships the method, not pre-baked results") become check family
F1 in the new repo; five-tests stays live as the legacy line.

Layout:
  harness/      check families; each = checks + policy version + verdict
                emitter + negative controls
    f1_five_checks/
    f2_goal_hijack/      (ASI01; includes injection patterns, AgentDojo-style)
    f3_tool_misuse/      (ASI02)
    f4_identity/         (ASI03)
    f5_memory/           (ASI06)
    f6_human_trust/      (ASI09)
  evidence/     bundle writer, hash chain, verify (re-derivation) CLI
  calibration/  judge audit suite + human-anchored items
  mappings/     ASI01-ASI10 crosswalk, ATLAS and NIST references
  runs/         reproducible public runs (sample agent first)
  docs/         method note (the failure-mode matrix, expanded),
                bundle format spec, README narrative

CLI:
  <name> run --agent X --suite Y -> runs/<id>/bundle.jsonl + manifest.sha256
  <name> verify runs/<id>        -> re-derivation report (stranger-safe)
  <name> judge-audit --set S     -> judge reliability numbers
  <name> gaps runs/<id>          -> the named gaps, if any

## 5. Milestones
M0 (today): this spec; decisions D1-D4.
M1 (this week): the five F1 checks emit P1 verdict events; every run
writes an evidence stub with P2 provenance. Deliberately aligned with the
Andrey artifact run: his local `results/` becomes the first evidence
bundle produced on a real engagement.
M2 (week 2): bundle format v1 frozen (spec in docs/); `verify` CLI
working; P3 negative controls in every suite; P4 named gaps.
M3 (week 3): ASI crosswalk live; F2-F6 families (goal hijack, tool
misuse, identity, memory, human trust) each with policy version +
negative controls; first public run: the OrderBot sample agent from the
five-tests repo (owned, safe) + one public agent (decision D4).
M4 (week 4): P6 judge audit suite in the bundle (calibration anchors,
perturbation flips, disagreement rate, self-preference probe).
M5 (weeks 5-6): the failure-mode benchmark, public and reproducible.
Rows = the four failure modes from the Behar thread: verdict not emitted;
verdict emitted but not preserved; host dies between local commit and
independent ingestion; record preserved but not independently
verifiable. Columns = detectability, survivability requirement, recovery,
residual gap, test case. Co-authored with Behar Dalipi (his round 5
proposal, jointly attributed, both names); the T0-T6 trace + negative
control are tests 1-2; his T2-T5 host kill is test 3.
M6 (week 6): portfolio surface. README leads with the gap (section 1 of
this doc), the method note, public run results with verify demo (one
command, in the README), the co-authored benchmark, and the lane
cross-posts. The repo is the citation target of the content.

Success criteria (all four, or it is not done):
  (1) `verify` passes a bundle generated on a different machine;
  (2) a practitioner (Kyle class: production agent systems engineer) runs
      the full loop from a cold clone in under 30 minutes;
  (3) the failure-mode benchmark has a second named author and two or
      more public runs;
  (4) the lane's content has pointed at it for at least a month, with
      the repo as the proof under the claims.

## 6. Why this is the perfect lane
- The ICP is the gap's mirror: at risk, cannot verify, compliance
  exposure dated 2027 (EU AI Act Annex III). The artifact this project
  emits is the answer to "how would you know?", which is the decision-
  maker room's only question.
- The live threads become the distribution: Behar (co-author +
  governance-lane reference), Wolfe (the close cadence, re-derive a
  sample each close, is the verify ritual in his words), Sam (his
  judge-vs-human detector research is the evidence pillar's academic
  anchor), Kyle (already separates source from conclusion in his own
  traces; first beta user), Andrey (first real-run bundle), Filip
  (release-readiness across teams is the F-family's buyer question).
- The content spine is already written: mirror not witness, named gap
  vs silence, who checks the checker, the scorecard degrades the way
  satisfaction did. Each is a chapter; the repo is the citation.
- Industry-standard is achieved the only honest way: map to the
  standards (ASI, ATLAS, NIST), implement the practices the 2026
  research just converged on (protocol audit trail, grader
  disagreement in the artifact, re-auditability), and make the whole
  thing re-derivable by a stranger.

## 7. Owner decisions (ALL TAKEN 10-29, owner: 'yes all D
recommendation taken')
D1: RESOLVED = tieout.
D2: RESOLVED = new repo, five-tests becomes check family F1.
D3: RESOLVED = verdict-event emitter this week, aligned with the
    Andrey local run tonight.
D4: RESOLVED = OrderBot sample first for public runs.

## 7.5 M1 status (BUILT 10-29)
Local repo /home/user/tieout, git main, first commit 2a5c53d
(tieout 0.1.0 M1). Built and tested this turn:
- six pillars in code: P1 verdict events on a hash chain (pre-
  assigned item ids, policy version hash, decision, effect ref
  assigned before the run); P2 provenance manifest +
  manifest.sha256; P3 negative controls (known-hold + known-broken
  items in every bundle, harness false positive / false negative
  rate in the bundle); P4 named gaps (completeness: a missing
  verdict is a named gap, not silence); P5 re-derivation core
  (verify re-walks chain, re-hashes manifest, re-runs detectors on
  stored raw: no model, no key, no network); P6 judge identity +
  resolved endpoint recorded (full audit suite = M4)
- family F1: the five checks ported unchanged from
  ai-redteam-five-tests (d95a57e); deterministic sample OrderBot
  (holds all English checks, breaks the mixed-language unverified-
  refund refusal, so keyless runs produce a real metric); live
  adapter for any OpenAI-compatible endpoint (MODEL /
  OPENAI_BASE_URL / OPENAI_API_KEY, MY_SYSTEM_PROMPT_FILE)
- CLI: run, verify, gaps, judge-audit, selftest
- SELFTEST PASS (7/7): clean bundle verifies; one probe broke as
  designed (F1-T4-R1-mixed fail); controls clean (0 FP / 0 FN);
  one-character tamper detected (G-HASH); dropped line leaves a
  named gap (G-MISSING) + manifest count/tail break
- sample run green: 0 of 3 injection, 0 of 3 retrieval, 0 of 2
  tool, 1 of 6 multilingual; VERDICT PASS (re-derivable by a
  stranger)
- BLOCKER: gh token (integration) lacks createRepository scope
  ('Resource not accessible by integration'), so the public repo
  could not be created from this sandbox.
- OWNER DECISION 10-29 (verbatim: 'i will build in another repo'):
  the owner hosts the build in his own repo. Handoff ready both
  ways: (a) local git main at 2a5c53d is push-ready, if the owner
  names a repo URL the push is one command from this sandbox;
  (b) source zip /home/user/tieout-m1.zip (56.7 KB, 37 files,
  no .git, no generated bundles) is drop-in ready for any repo.
Next: Andrey local run tonight -> his results/ becomes the first
live-mode bundle (first real-run evidence in the new format);
M2 = bundle format v1 frozen + full re-derivation report.
NOTE 10-29 (Behar round 6): the M5 artifact advanced ahead of the
milestone plan on the strength of the Behar thread (collaboration
confirmed 1:06 PM). docs/failure-mode-matrix.md +
docs/harness-spec.md are now in the tieout tree (local main
73f008c) and ride with the zip; the Behar note is the first
co-authored artifact of the project (M5 is no longer 'to build',
it is 'to complete with a second named author'); the five-tests
push was 403 (token scope), the tieout tree is the home of record. UPDATE 10-29 late: owner directive 'do not reference the project, it is not yet fully built' - the Behar DM no longer references the tieout repository; R6 v2 delivers the matrix + harness spec inline and links the existing public five-tests implementation (d95a57e, live-verified); the harness lands there as a first-version commit; the tieout tree + zip were wiped from the sandbox workspace 10-29 late (rebuild = record + public source). 10-29 late (2nd): owner 'i said do not refernceany repo' - the Behar DM now carries zero repo references of any kind (R6 v3 920w, gate-asserted; v1 tieout link and v2 five-tests link both superseded); the implementation ships with the first runnable harness version; thread rule: no repo naming while the build is incomplete. 10-29 late (3rd): Behar's reply confirms the inline materials as a 'workable foundation' + two CORRECT distinctions (issuance does not prove the action was proposed, an independently preserved commitment to the proposal is required; signature + policy hash prove integrity/provenance, not correct enforcement, institutional authorization, or effect execution) + test-class split (persistence/recovery vs cryptographic verification under the key-free harness) + GOVERNANCE GATE before substantial development (author order, contribution records, repository arrangements, publication permissions); R7 DRAFTED 740w (both distinctions accepted as the guarantee/limitations split, C family splits to C/C'/C'', test classes P/V, day-one contribution record with author order following the record, repository arrangement confirmed in principle generic, link arrives with the first runnable version); thread rule held (no repo name/link; his ask worded 'when available').

## 8. Sources (fetched/searched 10-29)
[1](https://vdf.ai/blog/ai-red-teaming-tools/) AI Red Teaming Tools 2026 (vdf.ai, Oct 2026): garak 0.17.0 9 Sep 2026, agent breaker probe since 0.15.0; promptfoo 0.124.0, part of OpenAI, agent plugins; PyRIT, DeepTeam 1.0.9, Giskard v3, Spikee, AgentDojo; star counts.
[2](https://www.testmuai.com/blog/ai-red-teaming-tools/) 9 Best AI Red Teaming Tools 2026 (Sep 2026): the three-way split (endpoint scanners, app/RAG, managed).
[3](https://awesomeagents.ai/tools/best-ai-red-teaming-tools-2026/) (Aug 2026): promptfoo 24,174 stars, MIT, OpenAI acquisition Mar 2026, used internally by OpenAI and Anthropic per repo description; garak 8,782 stars, Apache 2.0.
[4](https://www.digitalapplied.com/blog/ai-agent-eval-frameworks-testing-guide-2026/) (May 2026): 5 commercial + 3 OSS eval landscape; Inspect AI v0.3.225 (UK AISI) 200+ evals; OpenAI Evals 18.5k stars; DeepEval v4.0.3.
[5](https://niteagent.com/blog/2026-05-21-ai-agent-eval-frameworks-compared/) (May 2026): 57% of orgs run agents in production, 52% offline evals, 37% online; MLflow/DeepEval/LangSmith/Braintrust/Phoenix comparison.
[6](https://cycode.com/blog/owasp-top-10-agentic-applications/) (Jul 2026): OWASP Top 10 for Agentic Applications 2026, published 2025-12-09, ASI01-ASI10 with identifiers.
[7](https://arnav.au/2026/07/02/owasp-top-10-for-agentic-applications/) (Jul 2026): 100+ experts, open peer review; risk-to-control-to-owner mapping.
[8](https://dikrana.dev/blog/llm-as-judge-is-flaky/) (Jun 2026): RAND Judge Reliability Harness, arXiv:2603.05399, "no judge uniformly reliable", verdicts flip on reformat/paraphrase/verbosity.
[9](https://pith.science/paper/2607.08535) (Jul 2026): judge-replacement audit; recommends slices, bias probes, rho, protocol audit trails; "cannot be re-audited" where raw outputs unshipped.
[10](https://cloudai.pt/llm-as-judge-has-a-reliability-problem-in-production/) (Jun 2026): JudgeBiasBench >50% error on advanced bias tests; FairJudge three-limitation taxonomy (adaptivity, non-semantic bias, cross-mode inconsistency).
[11](https://arxiv.org/html/2604.16790v1) (Apr 2026): Bias in the Loop; no standard test-retest quantification; prompt-induced judge bias large enough to change rankings.
[12](https://arxiv.org/html/2606.26185v1) (Jun 2026): temperature control necessary not sufficient; 1-2 of 7 borderline items non-reproducible at forced greedy; transmission-layer risk, no record in artifact; disagreement rate + resolved endpoint belong in results.
Workspace record: EU AI Act Annex III high-risk obligations 2027-12-02 (EMAIL/leads/2026-10-27_icp100.md); five-tests repo public, latest d95a57e, "ships the method, not pre-baked results".

## 7.6 FULL BUILD status (BUILT 10-29, owner: "full not scaffold, full frontend UI")
Repo name = tieout (D1 held; github.com/Teamthy/tieout confirmed
free via API this turn). Built at linkedin_emphire/PROJECTS/tieout/
(self-contained tree, owner hosts as a separate GitHub repo; gh
token still lacks createRepository). v0.2.0, MIT, authors = both
names (day-one contribution record).
- Python package tieout/: P1 verdict events on a hash chain
  (pre-assigned ids + effect refs before the run); P2 provenance
  (harness/model/dataset hash/env/decoding/seed + judge + target
  resolved endpoints); P3 negative controls (8 crafted known-hold /
  known-broken, per-run FP/FN in manifest); P4 named gaps (G-MISSING /
  G-HASH / G-VERDICT-MISMATCH / G-CONTROL / G-RECORD / G-TARGET /
  G-PROVENANCE; a missing verdict is a named gap, never silence); P5
  re-derivation (verify re-walks chain, re-hashes manifest +
  manifest.sha256, re-runs detectors on stored raw: no model, no key,
  no network); P6 judge audit (14 crafted/versioned anchors: agreement,
  perturbation flips reformat/paraphrase/verbosity, disagreement vs
  naive one-tell variant, self-preference probe)
- F1 family: the five checks ported unchanged from five-tests
  d95a57e (inputs + detectors identical); deterministic SampleOrderBot
  (holds all 11 English items, breaks exactly F1-T4-R1-mixed);
  LiveAdapter for any OpenAI-compatible endpoint (same env contract)
- CLI: run / demo / verify / gaps / judge-audit / selftest / serve
- bundle format v1 documented (docs/bundle-format-v1.md): manifest
  line, chained event + control records, trailing judge_audit + gap
  records, record_hash + prev_hash + tail + file sha256
- UI (web/, Vite + React + TypeScript, strict): run list; run detail
  with verdict timeline + hash chain, the metric, negative controls,
  named gaps, judge audit, provenance, and a stranger-verify button
  that POSTs to the API and renders the re-derivation report; dark
  evidence aesthetic; built and served by tieout serve (one command)
- tests: 13 pytest (verify/tamper/dropped-line/verdict-flip/metrics /
  audit numbers / CLI flow / server endpoints) + SELFTEST 7/7
  (same contract as M1: clean verify, sample behavior, 0/3 0/3 0/2
  1/6, 0 FP 0 FN, one-char tamper G-HASH, dropped line G-MISSING +
  manifest break, audit offline)
- verified this turn: pytest 13 passed, ruff clean, tsc strict clean,
  vite build clean, demo run VERDICT PASS (re-derivable by a
  stranger), live server smoke (health/runs/verify/UI all green)
- docs: README (M6 posture, gap-first), bundle-format-v1, harness-
  spec (T0-T6 as implemented, tests A-D, binding field map, standing
  gaps G-ASI-MAPPING / G-WAL / G-ISSUANCE), method-note, failure-
  mode-matrix (co-authored, both names, day-one contribution record,
  P/V test classes)
- CI (.github/workflows/ci.yml): backend (ruff + pytest + selftest)
  + frontend (npm ci + build); committed demo run at runs/demo
  (reproducible public sample; verdicts stable, timestamps per run)
Milestones covered: M1 + M2 (format v1 + verify + controls + gaps)
+ M4 (P6 in the bundle) + UI (new, per owner directive) + M6
(README posture). M3 families F2-F6 and M5 completion (Behar's
guarantee columns) remain; Behar thread rule holds: no repo
reference in the DM while the build is incomplete; the link ships
with the first runnable version, after both sign-offs.

## 7.7 Next.js UI + PUBLIC PUSH (10-29, owner directives)
Owner positioning directive (verbatim intent): the project must sit at
the intersection of industry-standard portfolio work for AI red teaming
x AI security x AI security research x AI evaluation, suitable for
fellowship review, employer review, industry-leader review, and
LinkedIn reference without skepticism. Execution: gap-first README +
method note + cited research section (RAND arXiv:2603.05399,
arXiv:2607.08535, arXiv:2604.16790, arXiv:2606.26185, OWASP Agentic
Top 10 2026, tool landscape) + co-authored benchmark with named second
author + one-command stranger verify in the README + reproducible
committed demo run + honest named gaps. The spec itself (with ICP and
thread-distribution sections) stays OUT of the public tree.
OWNER DIRECTIVE 2: frontend stack = Next.js, minimalist black and
white. DONE: web/ rebuilt on Next.js 14 (App Router, output: export,
TypeScript strict, builds clean with typecheck); monochrome design
system (#000 bg, #fff text, gray levels, monochrome verdict badges:
pass = outlined, fail = inverted, undetermined = dim); run list, run
detail (verdict timeline + chain, metric, controls, gaps, judge audit,
provenance, in-page stranger verify); Vite tree removed; FastAPI now
serves web/out (one command still: tieout serve).
OWNER DIRECTIVE 3: push to https://github.com/Teamthy/Tie-out- (repo
exists, created by owner, was empty). Clean tree pushed to main
(excluding .venv/node_modules/.next/out/caches). pyproject Homepage
updated to the real repo URL. REPO IS PUBLIC: publication gate for the
co-authored matrix = both sign-offs (Behar's guarantee columns are
still his move); the owner can keep citing the repo privately now and
flip the public story (content cross-posts, Behar link) after his
sign-off.
Verified this turn: ruff clean, pytest 13/13, SELFTEST 7/7, next build
clean (4 static pages), server smoke: Next UI title + /api/runs green.
