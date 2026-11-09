# 08 References

Short, and chosen for what each one is actually useful for. A long reading list is easy and usually unread.

## Frameworks

| Source | Use it for |
|---|---|
| OWASP Top 10 for LLM Applications | The filing language. Map findings here so the security team can triage them. |
| OWASP Agentic Security work | Agent and tool specific categories, identity and autonomy. |
| MITRE ATLAS | Technique naming, and joining a finding to the wider threat picture. |
| NIST AI Risk Management Framework | Risk vocabulary for US-facing clients. |
| NIST Generative AI Profile | Concrete suggested actions, useful as a list of controls to test for. |
| ISO/IEC 42001 and ISO/IEC 27001 | Where AI management sits relative to an existing management system. |
| EU AI Act | Duties by role and classification. Facts to establish, not a legal opinion to give. |

## Papers that change how you work

- **Indirect prompt injection** (Greshake and others, 2023). The framing that made injection a systems problem rather than a prompting problem. Read for the taxonomy of channels.
- **Universal and transferable adversarial suffixes** (Zou and others, 2023). Read for the mechanism and for the honest limitation: transfer to a production system is not guaranteed.
- **Many-shot jailbreaking** (Anthropic, 2024). Read for why long context changes the risk, not just the cost.
- **Judging the judges**: the position, verbosity and self-preference bias literature. Read before you trust any model-graded number, including your own.
- **The reliability papers behind pass^k** (tau-bench and successors). Read for why a per-step rate is not a per-task rate.
- **Model extraction and membership inference** literature. Read for what is measurable about a model you can only query.

## Reading the vendor documentation properly

Three questions, every time: what data leaves the environment, what is retained and for how long, and whether the model can be pinned to a revision. The answers are in the data processing terms and the API reference, and rarely in the marketing page.

## What to skip

Named jailbreak catalogues. Learn the mechanisms (surface form, language, length, encoding, output shape) and the catalogue becomes optional. Half the named attacks in circulation are the same three mechanisms wearing new names, and an adaptive attacker will invent a fourth.
