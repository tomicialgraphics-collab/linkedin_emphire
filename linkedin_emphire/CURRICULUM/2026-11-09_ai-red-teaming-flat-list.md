---
deliverable: internal
id: 2026-11-09_ai-red-teaming-flat-list
date: 2026-11-09
audience: internal
status: ready
approved: no
warm: no
thread: a flat scanning list in the same shape as the backend engineering list, so the coverage question can be asked item by item rather than read as prose
verified: no external statistic is quoted. Every item is a standard named technique, control or evaluation concept in published AI security work, and the list makes no claim about any named vendor or product.
---

# AI red teaming, the flat list

**Written 2026-11-09. A working checklist rather than a document, so the voice gate does not apply to it: every line is a fragment by design.** Same shape as the backend list: one term per line, meant for scanning and for arguing coverage. The ranking and the tests live in `CURRICULUM/2026-11-09_ai-security-eval-principles.md`, and the ground underneath lives in `CURRICULUM/2026-11-09_infrastructure-principles-for-ai-red-teaming.md`.

How to use it: print it, mark each line as tested, not present, or skipped on purpose. The last of those three is the one that belongs in the report, because a skipped class that is named honestly is a finding about the engagement, and an untested class that is not named is a claim the reader will assume.

## Model behaviour

Prompt Injection (Direct)
Prompt Injection (Indirect)
Jailbreaking
System Prompt Extraction
Instruction Hierarchy
Refusal Behaviour
Over-Refusal
Hallucination
Confabulation
Sycophancy
Abstention
Context Window Limits
Lost in the Middle
Temperature and Sampling
Determinism and Seeds
Prompt Brittleness
Persona Drift
Multi-Turn Escalation
Many-Shot Jailbreaking
Encoding Attacks (Base64, ROT13)
Payload Splitting
Token Smuggling
Unicode Normalization
Homoglyphs and Confusables
Invisible Characters
Glitch Tokens
Low-Resource Language Attacks
Multilingual Refusals
Adversarial Examples
Adversarial Suffixes
Data Poisoning
Backdoors and Trojans
Fine-Tune Safety Regression
Quantization Effects
Calibration and Confidence
Memorization
Training Data Extraction
Membership Inference
Model Inversion
Model Extraction
Model Theft and Distillation
Watermarking
Fingerprinting
Canary Tokens
Copyright Reproduction
Bias and Fairness
Toxicity
Harm Taxonomy
Content Policy Mapping

## Retrieval and knowledge

Retrieval Poisoning
Chunk Boundary Attacks
Embedding Inversion
Vector Store Access Control
Document-Level ACLs
Cross-Tenant Leakage
Metadata Injection
Ingestion Validation
Retrieval Provenance

## Agents and tooling

Tool Calling Abuse
Tool Description Poisoning
Tool Rug Pull
Argument Injection
Excessive Agency
Confused Deputy
Permission Scoping
On-Behalf-Of Tokens
Human-in-the-Loop Bypass
Approval Fatigue
Agent Memory Poisoning
Agent-to-Agent Trust
MCP Server Trust
Subagent Spawning
Kill Switch Escape
Sandbox Escape
Code Execution via Tools
SSRF via Fetch and Browse
Autonomous Goal Hijacking
Loop and Step Ceiling
Unbounded Consumption
Denial of Wallet
Prompt Injection via Files and PDFs
Multimodal Injection
Steganographic Exfiltration

## Output handling and containment

Insecure Output Handling
SQL Injection via LLM
XSS via LLM Output
Markdown Image Exfiltration
Link Parameter Exfiltration
Output Length Side Channel
Schema Validation
Structured Output Abuse
Guardrail Bypass
Guardrail Ordering
Prompt Firewall
Input Sanitization
Spotlighting and Delimiters
Dual-LLM Pattern
Allowlisting vs Blocklisting

## Measurement and evaluation

Eval Set Design
Golden Sets
Held-Out Sets
Private Slices
Benchmark Contamination
Benchmark Saturation
Attack Success Rate
Per-Objective vs Per-Attempt
Confidence Intervals (Wilson)
Pass@k
pass^k (Reliability)
Paired Comparison (McNemar)
Sample Size and Power
Run-to-Run Variance
LLM-as-Judge
Judge Calibration
Position Bias
Verbosity Bias
Self-Preference Bias
Inter-Rater Reliability
Cohen's Kappa
Rubric Design
Failure Taxonomy
Severity Scoring
Regression Suites
CI Eval Gates
Drift Canaries
Trace-Based Evaluation
Automated Red Teaming
Fuzzing and Mutation
Adversarial Test Generation
Coverage Argument
Cost per Case
Latency per Case
Reproducibility Contract

## Governance and practice

Threat Modelling for AI
Trust Boundaries
Data Flow Mapping
Attack Surface Map
Propagation Testing
OWASP LLM Top 10
OWASP Agentic Security
MITRE ATLAS
NIST AI RMF
NIST Generative AI Profile
ISO/IEC 42001
EU AI Act Duties
Model and System Cards
AI Bill of Materials
Model Provenance and Signing
Risk Register
Dangerous Capability Evaluation
Uplift Studies
Propensity vs Capability
Red Team Rules of Engagement
Safe Harbour
Coordinated Disclosure
Bug Bounty for AI
AI Incident Response
Human Oversight Design
Auditable Logging
Privacy Impact Assessment
Data Residency of Prompts
Prompt Versioning
Model Version Pinning
Rollback of Prompts and Models
Purple Teaming
Continuous Red Teaming
Adversarial Training as Patching
Safety Cases

## The lines that are not on the list and should be

Canary string in the system prompt, because it is the cheapest leak detector that exists and almost nobody plants one.
The prompt and model version, in the report, because without them the finding expires the moment it is written.
The test case that came out of the last finding, because a fix that becomes a regression test is the only fix that lasts.
