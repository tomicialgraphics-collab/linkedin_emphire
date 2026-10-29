import { body as a01 } from "./articles/01-prompt-not-a-wall";
import { body as a02 } from "./articles/02-surface-drift";
import { body as a03 } from "./articles/03-matrix-executable";
import { body as a04 } from "./articles/04-verify-dont-trust";
import { body as a05 } from "./articles/05-negative-control";
import { body as a06 } from "./articles/06-auditing-the-judge";
import { body as a07 } from "./articles/07-exact-confidence-intervals";
import { body as a08 } from "./articles/08-the-empty-layer";
import { body as a09 } from "./articles/09-provenance-is-part-of-the-claim";
import { body as a10 } from "./articles/10-record-schema-for-verdicts";
import { body as a11 } from "./articles/11-exit-codes-a-ci-can-trust";
import { body as a12 } from "./articles/12-stateless-by-design";

export type Theme =
  | "ai-red-teaming"
  | "security"
  | "research-engineering"
  | "evaluation"
  | "software-engineering";

export interface Article {
  slug: string;
  title: string;
  theme: Theme;
  summary: string;
  /** every claim in the article traces to one of these */
  verified: string[];
  body: string;
}

export const THEMES: { id: Theme; label: string; line: string }[] = [
  {
    id: "ai-red-teaming",
    label: "ai red teaming",
    line: "what to probe an agent with, and how to keep the probe honest",
  },
  {
    id: "security",
    label: "security",
    line: "integrity of the record: chains, controls, stranger verification",
  },
  {
    id: "research-engineering",
    label: "research engineering",
    line: "measuring the measurer, and statistics that hold at small n",
  },
  {
    id: "evaluation",
    label: "evaluation",
    line: "the evidence layer, and provenance as part of the claim",
  },
  {
    id: "software-engineering",
    label: "software engineering",
    line: "schemas, cli contracts, and deploying stateless by design",
  },
];

export const ARTICLES: Article[] = [
  {
    slug: "prompt-not-a-wall",
    title: "prompt is not a wall: the five failure checks against an agent",
    theme: "ai-red-teaming",
    summary:
      "what family F1 actually probes, why each check exists, and what the committed run measured",
    verified: [
      "runs/demo: 14 events (13 pass / 1 fail), 8 controls, 0 FP / 0 FN",
      "docs/harness-spec.md: the F1 items and detectors",
      "ai-redteam-five-tests @ d95a57e: the public method F1 was ported from",
    ],
    body: a01,
  },
  {
    slug: "surface-drift",
    title: "the same suite, twice: measuring surface drift without moving a verdict",
    theme: "ai-red-teaming",
    summary:
      "two seeds, one suite, fourteen aligned ids: zero verdict flips, ten drifted transcripts, and why the difference is the point",
    verified: [
      "runs/demo-stability/a (seed 0) and runs/demo-stability/b (seed 7)",
      "tieout diff output: aligned 14, flips 0, drift 10, stability 1.000",
      "the diff report and the CI stored in both manifests",
    ],
    body: a02,
  },
  {
    slug: "matrix-executable",
    title: "the failure-mode matrix, made executable: E, P, R, V as checks",
    theme: "ai-red-teaming",
    summary:
      "four failure modes of decision-time evidence become eight runnable items with their own controls and judge audit",
    verified: [
      "runs/demo-f2: 8 events (4 fail / 4 pass), 8 controls, 0 FP / 0 FN",
      "docs/failure-mode-matrix.md: the matrix the family executes",
      "the judge audit record: 12 anchors, agreement 1.0, disagreement 0.4167",
    ],
    body: a03,
  },
  {
    slug: "verify-dont-trust",
    title: "verify, don't trust: a hash chain a stranger can walk",
    theme: "security",
    summary:
      "how re-derivation works, what it refuses to do, and the two selftest points that prove it catches tampering",
    verified: [
      "selftest points 5 and 6: one-character tamper and dropped-line detection",
      "tieout verify output on all four committed runs",
      "docs/bundle-format-v1.md: the chain, the tail, the file hash",
    ],
    body: a04,
  },
  {
    slug: "negative-control",
    title: "the negative control: a check that cannot grade itself",
    theme: "security",
    summary:
      "every suite ships items it does not generate; the detector's false positives and false negatives are part of the run",
    verified: [
      "the control records in all four committed bundles: 8 each, 0 FP / 0 FN",
      "selftest point 4: negative controls clean",
      "docs/bundle-format-v1.md: control event schema",
    ],
    body: a05,
  },
  {
    slug: "auditing-the-judge",
    title: "auditing the judge: anchor agreement, perturbation flips, self-preference",
    theme: "research-engineering",
    summary:
      "the judge's own numbers, measured every run: anchors, perturbations, disagreement against a naive variant, and a self-preference probe",
    verified: [
      "the judge_audit records in runs/demo and runs/demo-f2",
      "tieout/calibration/audit.py: the four measured quantities",
      "selftest point 7: the audit runs offline with honest numbers",
    ],
    body: a06,
  },
  {
    slug: "exact-confidence-intervals",
    title: "exact confidence intervals for small evals: why 13 of 14 is not 93%",
    theme: "research-engineering",
    summary:
      "Clopper-Pearson at n=14, computed in the code before the bundle closes, and stored where a stranger can read it",
    verified: [
      "manifest.statistics in the committed bundles: CI 0.661316..0.998193 at 13/14",
      "tieout/stats.py: bisection on the binomial CDF, math.comb only",
      "the test vectors: 0/10 -> [0, 0.3085], 13/14 -> [0.6613, 0.9982]",
      "runs/demo-f2/bundle.jsonl: the F2 bundle, 4 of 8 pass, CI 0.157013..0.842987 in its statistics block",
    ],
    body: a07,
  },
  {
    slug: "the-empty-layer",
    title: "the empty layer: attacks are commoditized, evidence is not",
    theme: "evaluation",
    summary:
      "the 2026 tooling landscape is crowded in three layers and empty in the fourth; a self-grade is a verdict from a shared operator",
    verified: [
      "docs/method-note.md: the four-layer argument and the tool landscape it cites",
      "the committed bundles: the artifact the argument demands",
      "the RAND 2026 finding as cited in the method note",
    ],
    body: a08,
  },
  {
    slug: "provenance-is-part-of-the-claim",
    title: "provenance is part of the claim: pin the environment, hash the packages",
    theme: "evaluation",
    summary:
      "a verdict without an environment is a rumor; what the manifest records, and what the package hash adds in format v1.1",
    verified: [
      "the four manifests: harness, agent, model, dataset hash, environment, seed",
      "runs/demo-f2 manifest: packages and packages_hash sha256:ad5b76bc56823f57",
      "docs/bundle-format-v1.md: the provenance section",
    ],
    body: a09,
  },
  {
    slug: "record-schema-for-verdicts",
    title: "a record schema for verdicts: one event per decision, chained",
    theme: "software-engineering",
    summary:
      "the design decisions behind the bundle format: pre-assigned ids, canonicalization, one record per line, and a versioned schema",
    verified: [
      "docs/bundle-format-v1.md: the schema and the verify procedure",
      "tieout/hashing.py: canonicalization, including U+2028 / U+2029",
      "the bundles themselves: v1 and v1.1 records that verify today",
    ],
    body: a10,
  },
  {
    slug: "exit-codes-a-ci-can-trust",
    title: "exit codes a CI can trust",
    theme: "software-engineering",
    summary:
      "the cli contract: what 0, 1 and 2 mean on verify, diff and selftest, and how one definition of pass is shared by site and pipeline",
    verified: [
      "tieout/cli.py: the argparse tree and every return code",
      ".github/workflows/ci.yml: verify-committed-runs and the stability gate",
      "this site: the same commands, surfaced as pages",
    ],
    body: a11,
  },
  {
    slug: "stateless-by-design",
    title: "stateless by design: deploying an evidence site to serverless",
    theme: "software-engineering",
    summary:
      "how this site deploys: a static export plus one function, an ephemeral filesystem handled explicitly, and why the evidence never lived there anyway",
    verified: [
      "vercel.json, main.py and tieout/server.py in this repository",
      "tests/test_deployment.py: the read-only-filesystem contract",
      "the live deployment this article ships on",
    ],
    body: a12,
  },
];
