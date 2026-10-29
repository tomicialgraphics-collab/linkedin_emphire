const body = `
## Four layers, three of them crowded

The 2026 tooling landscape for agent security is crowded in three layers and empty in the fourth. The full argument, with the tool list, sits in the [method note](/method). The short version:

- **Attacks are commoditized.** garak, PyRIT, promptfoo, DeepTeam, Giskard, AgentDojo. Running an attack suite is a solved logistics problem.
- **Scoring is commoditized.** OpenAI Evals, DeepEval, Inspect AI, LangSmith, Braintrust, Phoenix. Producing a number from a run is a solved plumbing problem.
- **Taxonomy is standardized.** OWASP Top 10 for Agentic Applications, MITRE ATLAS, NIST AI RMF. Naming the threat is a solved vocabulary problem.
- **Evidence is empty.** Nobody in the landscape emits an artifact that survives contact with a stranger.

## The self-grade

The reason the fourth layer is empty is structural. Every tool uses a judge that lives inside the tool. The evaluator and the evaluated share an operator, the same credentials, the same process, often the same model family. A green eval from such a tool is a self-grade: the exam was set, administered, marked, and archived by the same person who took it.

The research the method note cites names the failure modes precisely. No judge is uniformly reliable (RAND, 2026). Verdicts flip on reformatting and verbosity. Judge upgrades are not interchangeable. And where raw outputs were not shipped, the numbers cannot be re-audited, which means the debate about them is settled by whoever owns the tool, because only they can look under the hood.

## What the missing layer looks like

Not a bigger judge. Not a second opinion by another model from the same vendor. A record with three properties:

- every verdict is bound to the raw that produced it, with the policy version and the judge identity in the same event,
- the record is chained and hashed so that a stranger can detect any tampering without trusting the tool that wrote it,
- the judge's own error rates are measured in the same run, on inputs the judge did not generate.

The committed bundles in this repository are the artifact for exactly that spec, and they are the reason this site links to run pages instead of screenshots. A screenshot is a claim. A bundle is a record. The difference is the entire fourth layer.
`;

export { body };
