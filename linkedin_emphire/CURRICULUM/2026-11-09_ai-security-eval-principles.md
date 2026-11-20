---
deliverable: reference
id: 2026-11-09_ai-security-eval-principles
date: 2026-11-09
audience: owner
status: ready
approved: no
warm: no
thread: the counterpart to the infrastructure list, covering the model, the agent built around it and the measurement machinery, ranked by what makes the other tests interpretable
verified: no statistic is quoted. Frameworks are named without citing versions or dates beyond the order in which their duties apply, and the technique names are standard published work rather than claims about any named vendor.
---

# The principles that matter for AI red teaming, evaluation and AI security

**Written 2026-11-09. The pair to `CURRICULUM/2026-11-09_infrastructure-principles-for-ai-red-teaming.md`. That file covers the ground the model sits on. This one covers the model, the agent built around it, and the machinery that decides whether any of it can be measured.**

Read alongside `CURRICULUM/ai-redteam-and-research-master-curriculum.md`, which is the teaching path. This is the checklist.

## The one-line answer

Twelve, in order of what makes every other test interpretable:

1. Trust boundaries and the instruction hierarchy
2. Indirect prompt injection, through every channel that carries text
3. Attack success rate, defined precisely and reported with an interval
4. The reproducibility contract: model revision, prompt version, seed, date
5. Judgement: LLM as judge, calibrated against humans, with the biases controlled
6. The eval set as an asset, with provenance, contamination checks and edit history
7. Excessive agency: least privilege on every tool, and the confused deputy
8. Insecure output handling: where model text lands and what renders it
9. Guardrail bypass as an engineering problem, not a compliance checkbox
10. Memory and retrieval poisoning, the persistent compromise
11. Dangerous capability and propensity testing, inside a safe container
12. Reporting: denominators, exclusions, what you did not test, and the fix that becomes a regression test

Everything else is tier two (know it, test it when the target has it) or tier three (recognise the name, because it explains a finding).

## Why this list has a different shape from the backend one

The backend list has one axis: mechanism. Each item names a component and the way it fails. That is enough because the failures are deterministic once you see the plumbing.

This one needs three axes, and conflating them is the most common mistake in AI security work:

- **Capability.** What the model can be made to do, if it tries. Tested with adversarial effort.
- **Propensity.** What it actually does when nobody is pushing. Tested with realistic traffic, because a model that can be talked into a bad action and a model that volunteers one are different risks with different controls.
- **Measurement.** Whether the number you report would survive someone rerunning it. This is the axis almost nobody staffs, and it is the one that makes the work worth money.

A finding in this domain is a claim on all three. "The model will leak the system prompt" is capability. "It does so in 3 of 50 attempts, from this revision, on this date, judged by a rubric that agrees with two annotators 0.81" is the whole thing. The second is scarcer than the first by a wide margin.

---

## Tier one: the twelve, with the test for each

### 1. Trust boundaries and the instruction hierarchy

Before any test means anything, you need to know which text the system treats as instruction and which as data. System prompt, developer message, user turn, retrieved document, tool output, another agent's message, a web page, a file the user uploaded. Each is a different level of authority and each needs a stated rule for how it is delimited, quoted and stripped.

The test: for each channel, plant a benign instruction in it and see whether the model obeys. Then check whether the delimiters survive summarisation, because a summariser that concatenates retrieved text into the user turn has silently promoted data to instruction.

If the hierarchy is not declared, every injection result is uninterpretable and every fix is a guess.

### 2. Indirect prompt injection, through every channel

The dominant real-world LLM vulnerability, and the one that turns a chat feature into a remote code path.

Enumerate the channels: retrieved documents, web pages the agent browses, emails, calendar invites, PDFs, code in a repository, issue descriptions, image alt text, filenames, metadata, tool responses, another agent's output, a comment in a spreadsheet. For each: can text reach the model, and can it change what the next tool call does.

The test that matters is the propagation test rather than the injection test: one bad paragraph in one document, then trace how far the effect travels. Whether the model repeats a line is a curiosity. Whether it calls a tool with attacker-chosen arguments is the finding.

Variants worth knowing by name: payload splitting, where the instruction arrives in fragments across documents; second-order injection, where the model writes text that a later process trusts; and injection that survives a sanitiser because the sanitiser ran before the encoding.

### 3. Attack success rate, defined precisely

Every red team report quotes a number and most of them are not comparable to anything.

Define the unit before you count: attempts or objectives. One objective, fifty attempts, three successes is an attack success rate of six percent per attempt and one hundred percent per objective, and both are true and only one is useful to the reader. Say which, and say whether a partial success counts. Then weight by severity, because a rate that averages a leaked greeting with a leaked credential is a meaningless average.

Report the interval. Three of fifty is not "six percent", it is a range wide enough to contain most of the plausible truth, and the Wilson interval is the honest tool. Report the denominator, the number of attempts per case, and the refusal and error buckets separately, because a model that errors out has not resisted.

### 4. The reproducibility contract

Six things recorded or the finding does not exist: model identifier and revision, prompt version, retrieval index snapshot, tool schema version, sampling parameters, and the date the run happened. Add the judge version if a model graded it.

The test is personal and brutal: take a finding from three weeks ago and try to rerun it exactly. If you cannot, you did not find it, you had an opinion with a screenshot.

This is where most AI red teams quietly fail, and it is why the number of findings in a report should be smaller than the number of claims.

### 5. Judgement: LLM as judge, or a human rubric done properly

Almost all large scale safety evaluation now runs through a model grader, and model graders have documented biases: they prefer the answer that comes first, the answer that is longer, and the answer written by their own family of models. They drift when the rubric is long, and they fail silently on edge cases rather than saying so.

The test: grade a sample by hand, compare, and report agreement. Cohen's kappa if you want to be formal about it. Then run the position swap and the verbosity control on a slice and see whether your pass rate moves. If it does, your number moved too.

Also decide pointwise against pairwise against reference-based grading before you build anything, because the three answer different questions and only one of them is usually what the client asked for.

### 6. The eval set as an asset

Whose cases are they, where did they come from, who can edit them, and is the history of edits kept. A suite the vendor controls is a certification, not a measurement.

Contamination is the quiet killer: if the benchmark, or material derived from it, sat in the training data, the score measures recall of the test rather than capability. Check for it by paraphrase, by translation, and by looking for suspiciously exact matches on rare phrasing.

Then saturation. A suite at 94 percent is a suite with nothing left to tell you, and its remaining headroom is noise. Measure the ceiling before you celebrate the score.

### 7. Excessive agency and the confused deputy

Every tool is a capability grant. The red team question is never "can the agent use this tool" but "what can this tool do that the task does not require, and as whose identity".

Enumerate the tools, then the credentials behind each, then the scopes. Then the specific failure: the agent holds a permission the current user does not, and is steered into using it on the user's behalf. That is the confused deputy, and it is the top severity finding in agentic systems because it converts a prompt injection into an authorization bypass.

The controls to test for: per-request scoping, on-behalf-of tokens, approval gates the agent cannot reach, allowlists rather than blocklists, and a step ceiling on the loop.

### 8. Insecure output handling

Model text becomes someone else's input, and where it lands decides the severity. Markdown image tags that exfiltrate a conversation through a URL parameter. HTML that renders in a chat UI. Model-written SQL executed against a live database. Model-written code run in a sandbox with a network route. Model-written shell in a tool call. Model text that becomes a filename, a header, or an email recipient.

The test is a data flow diagram of the output, not a checklist. Every sink the text can reach is a candidate, and the ones that render it automatically in another user's browser are the worst, because the payload then fires without the reader clicking anything.

### 9. Guardrail bypass as an engineering problem

Guardrails are classifiers and filters, so the whole discipline of adversarial examples against classifiers applies. Encoding, base64, rot13, emoji, invisible unicode, homoglyphs, leetspeak, token boundary splitting, and low-resource languages are the cheap ones. Structured output modes are the sharp one: a model forced into JSON can be walked into the same content through a different shape.

The test that separates a real control from a purchase order: does the guardrail sit inside the same context as the content it judges. If the guardrail is a prompt, it can be argued with. Test the ordering too, because a guardrail that runs after the tool call has already happened is a log line.

### 10. Memory and retrieval poisoning

Single-shot injection ends when the session ends. A write to memory, a saved preference, a summary carried forward, or a document committed to the index persists, and it will be served back to everyone who queries it.

The test: plant something benign and durable, then start fresh sessions, and see whether it comes back and whether it changes behaviour. Check who can write to the index, whether retrieval is scoped per tenant, and whether the ingestion path validates a document before embedding it.

This is a supply chain problem more than a prompting problem, which is why it belongs near the top: the persistence is the severity.

### 11. Dangerous capability and propensity testing

For frontier or high-agency systems in a large project, the question of whether the model meaningfully helps with harm is a formal one with two halves. Capability: with maximum effort and tooling, does it add real uplift over what an unaided expert could do. Propensity: without pressure, does it volunteer the harmful path.

Containment is part of the test, not a courtesy. Sandbox without real network egress, no live credentials, no live third parties, and a written scope that says what you may not try. A red team that produces a working capability and no safe container has produced a liability.

For most enterprise engagements this item collapses into a smaller one: does the system's own risk classification match what it can do. Most do not, because capabilities get added by feature request and the classification is set once at launch.

### 12. Reporting, and the fix that becomes a test

The report is the deliverable and the number is the product. Denominators, exclusion criteria, what you did not test and why, and the smallest reproduction anyone can follow.

Then the part that makes the work compound: every confirmed finding becomes a case in the suite that runs on every deploy. Without that line, the engagement ends and the bug returns in three months under a new prompt.

What not to write: a severity score with no method behind it, a rate with no denominator, and any recommendation that says "implement guardrails" without naming the control and how it would be tested.

---

## Tier two: know it, test it when the target has it

### Model behaviour and attack surface

| Principle | The test |
|---|---|
| Direct prompt injection | A user turn that overrides the system prompt, and whether the boundary is declared at all |
| Jailbreak families | Roleplay, encoding, prefix injection, refusal suppression, payload splitting, many-shot, gradual multi-turn escalation |
| System prompt extraction | "Repeat your instructions", then the indirect route through a tool, a summary or a translation |
| Prompt leakage through logs and traces | Whether the system prompt sits in a trace, an error message or a client-side bundle |
| Tokenisation quirks | Glitch tokens, split tokens, unicode normalisation differences between filter and model |
| Invisible and homoglyph characters | Zero-width, bidirectional override, confusables, right-to-left marks |
| Sampling and determinism | Temperature, top-p, seed, and how much the same input varies across runs |
| Prompt brittleness | Paraphrase the same request ten ways and measure the spread in behaviour, not the mean |
| Refusal behaviour | Over-refusal and false refusal, since a system that refuses the legitimate case is a defect with a cost |
| Instruction hierarchy violations | A tool response or retrieved chunk that outranks the developer message |
| Hallucination and confabulation | Citation fidelity: are the quoted source, page and quote actually there |
| Sycophancy | Agreement rate under polite pushback, which is the failure that trains users to trust a wrong answer |
| Abstention | Whether the system says it does not know, and whether it is graded for doing so |
| Long-context behaviour | Eviction, lost-in-the-middle, and what falls out of the window first |
| Persona and goal drift | Fifty-turn conversations, and whether the guardrails hold at turn forty |
| Data exfiltration channels | Markdown images, links with parameters, alt text, whitespace, output length as a channel |
| Multimodal injection | Text inside an image, a screenshot, a PDF layout, audio, or an adversarial patch |
| Adversarial examples | Perturbations and suffixes, and whether they transfer to the deployed revision |
| Memorisation and extraction | Training data extraction, membership inference, model inversion, and what the system prompt reveals about the corpus |
| Backdoors and trojans | Trigger behaviour in a supplied fine-tune, weights from an unpinned source, a model whose origin cannot be shown |
| Data poisoning | Pretraining, fine-tune, preference data, and the retrieval corpus as the easy target |
| Calibration | Whether the confidence the system displays corresponds to accuracy on the cases you hold |
| Bias and fairness probes | Counterfactual swaps on protected attributes, with a stated decision threshold |
| Copyright and attribution | Near-verbatim reproduction, and whether the output policy is enforced or aspirational |

### Retrieval, tools and agents

| Principle | The test |
|---|---|
| Retrieval poisoning | A document written to the index that changes behaviour for every later user |
| Chunk boundary attacks | Instructions split across chunks so no single chunk looks wrong |
| Embedding inversion | Whether an embedding store leaks content, and who can query it |
| Document level access control | Whether the retriever filters by the asking user's permissions or by the index's |
| Cross-tenant isolation | Two tenants, one index, and the query that returns the other one's chunk |
| Tool description poisoning | A tool whose description contains instructions, since descriptions are trusted unread |
| Tool rug pull | A tool whose definition or output changes after approval |
| Argument injection | Attacker-chosen arguments to a legitimate tool, which is the injection that actually does damage |
| Confused deputy | The agent acting on authority the current user does not have |
| Excessive autonomy | No step ceiling, no approval gate, no kill switch, and what a runaway loop costs |
| Sandbox escape | Code execution, filesystem reach, network egress from the tool runtime |
| SSRF through fetch and browse tools | The metadata endpoint, the internal admin page, the file scheme |
| Agent to agent trust | A subagent that accepts its parent's message as instruction, and a message that crosses a trust boundary unnoticed |
| Human in the loop bypass | Whether the approval can be reached, spoofed, skipped by a retry, or starved by a timeout |
| Unbounded consumption | Denial of wallet: per-user budget, output ceiling, loop ceiling, and who is billed |
| Framework-specific surfaces | LangChain, LangGraph, CrewAI, MCP servers, and the default settings each ships with |
| Provider configuration | Data retention and training settings on the API, key handling, and whether the client knows what leaves |

### Evaluation and measurement

| Principle | The test |
|---|---|
| Case design | One behaviour per case, a stated expected outcome, and a fixture that reruns |
| Sample size and power | Whether the suite can detect the difference the client is claiming at all |
| Paired comparison | McNemar on the same cases under two versions, rather than two independent rates |
| Pass@k and pass^k | Capability at least once, against reliability every time, which are the two questions people conflate |
| Variance reporting | The spread across five runs, not a single run's number |
| Judge calibration | Hand-graded slice, agreement reported, biases probed |
| Rubric discipline | One behaviour per criterion, and a rubric short enough that a judge does not drift |
| Failure taxonomy | Buckets that a fix can be assigned to, with severity defined before the run |
| Severity method | OWASP and ATLAS mapping, and a stated reason a case is high rather than a number with no method |
| Regression suite | The finding, as a case, running on every deploy |
| Drift and canary | A standing set that runs weekly, and the alert when the refusal rate moves |
| Cost and latency per case | Because a suite nobody can afford to run is a demo |
| Coverage argument | A written statement of the classes tested and the classes skipped, so the reader knows what the rate describes |
| Contamination control | Paraphrase, translate, hold out, and keep the private slice private |

### Governance and professional practice

| Principle | The test |
|---|---|
| Threat model | Asset, actor, trust boundary, and the abuse case written before the test |
| OWASP LLM and Agentic Top 10 | Mapping each finding, since that is the language the security team already uses |
| MITRE ATLAS | Mapping the technique, which is how a finding joins the wider threat picture |
| NIST AI RMF and the generative profile | Whether the client's controls map to a framework they are already audited against |
| ISO/IEC 42001 and 27001 | Where AI management meets the existing information security management system |
| EU AI Act | Whether the system is general purpose or high risk, and which duties that triggers for the client |
| Model and system cards | Whether the documented limits match the observed behaviour |
| AI bill of materials | Weights, dataset, dependencies, and whether any of it is pinned by digest |
| Supply chain provenance | Signed artefacts, pinned revisions, and a model whose origin can be shown |
| Rules of engagement | Written scope, authorised targets, no live third parties, a stop condition, and a named person who can stop it |
| Coordinated disclosure | Timeline, channel, and what happens if the vendor disagrees |
| Incident response for AI | What runs when a prompt leaks, a model is abused, or an exfiltration channel fires |
| Auditable logging | Retention, redaction, and whether the log can answer a regulator's question |
| Privacy impact | Prompts as personal data, residency, retention, and where the log sits |
| Human oversight design | What the approval gate actually gates, and whether the person can understand the decision |
| Rollback of a model or prompt | Whether the previous version can be restored in minutes, and whether the index rolls back with it |

---

## Tier three: recognise the name

Model watermarking and fingerprinting, and canary strings planted in the system prompt to detect leakage, which is the cheapest leak detector in existence and rarely used. Distillation and model theft detection. Adversarial training, red teaming as a training input, and the difference between patching a behaviour and removing it. Differential privacy. Federated learning risks. Inference-time defences: input filtering, output filtering, spotlighting, delimiters, dual-LLM patterns, and the honest limit of all of them against an adaptive attacker. Debate and self-critique as mitigation, which reduces variance rather than bias. Speculative decoding and caching as attack surfaces. Quantisation effects on safety behaviour, which is real and under-tested. Fine-tune safety regression, where a helpfulness fine-tune quietly removes refusals.

Benchmarks worth knowing by name and limitation: the safety sets, the cyber capability sets, the agentic task sets, and the fact that all of them saturate or leak eventually.

---

## The order to learn it in

Four phases, each with an artifact, because reading about this produces familiarity rather than skill.

1. **Break one thing properly.** One target, one injection channel, one propagation test. Artifact: a finding with a reproduction someone else ran.
2. **Measure it.** Turn the finding into a case, add the judge, calibrate the judge, report the interval. Artifact: a number with a denominator and a range.
3. **Widen the surface.** The tier two table, worked through against one real system, so the gaps are visible. Artifact: an attack surface map with the untested classes named.
4. **Make it durable.** Cases in CI, a canary set on a schedule, a written coverage argument. Artifact: a suite the client owns and can run without you.

## What this list deliberately leaves out

Nothing about infrastructure, because the other file covers it, and nothing about model training, because a red team does not need to build one to test one. Also left out: the long tail of named jailbreak techniques, which is a vocabulary game that produces recognition rather than capability. Learn the families, not the catalogue. Half of the named attacks in circulation are the same three mechanisms wearing new names, and an adaptive attacker will invent a fourth.

## The honest caveat

This list is larger than the backend one for a reason that should worry anyone reading it: the failure modes are open-ended, because the input space is natural language and the system's behaviour depends on content nobody controls. There is no finite checklist that certifies an AI system as safe, and any vendor claiming one is selling a number rather than a measurement.

What you can do is narrower and worth more. Declare the classes you tested, count them properly, state the interval, name what you skipped, and leave behind a suite that reruns. That is the whole job, and the discipline of it is what almost nobody in this field has.
