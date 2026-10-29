const body = `
## A verdict without an environment is a rumor

"Pass rate 92 percent" is not a claim until you can say where it was made. Model version, decoding parameters, package versions, harness version, dataset hash, seed, machine: every one of those is a variable that can move the number, and a record that omits them cannot be reproduced, compared, or even repeated. Provenance is therefore not metadata around the eval. It is part of the claim, and it lives in the first line of the bundle, the manifest.

## What the manifest actually stores

Each committed manifest in this repository records, among other fields:

- the harness version and git identity of the code that ran,
- the suite id and the family policy versions in force,
- the agent and, for live runs, the model name, model version, and the resolved endpoint of every judge call,
- the dataset hash, so "same inputs" is a sha256, not a feeling,
- the environment: machine, platform, python version,
- the decoding parameters and the seed.

The F2 manifest is a concrete example. Its provenance pins python 3.11.2 on an x86_64 Linux platform, a deterministic sample agent (no model, no endpoint), a dataset hash of sha256:f92f1905823cc6fd5, the harness version, the family policy hash, and the seed. Two runs with identical provenance except the seed are comparable by construction. The committed stability pair is built on exactly that: the same F1 suite and the same dataset hash, re-run at seed 0 and seed 7, with only the seed differing in the record.

## Format v1.1: the environment includes the packages

Format v1.0 recorded the runtime but not the software. v1.1 closes that gap: the manifest now carries the exact package versions of the harness's dependencies plus a hash over that set. The F2 bundle records fastapi 0.162.0, httpx 0.28.1, pydantic 2.14.2, tieout 0.3.0, uvicorn 0.54.0, under packages_hash sha256:ad5b76bc56823f57. A reviewer checking your work in six months does not have to hope your lockfile survived. The record says what was loaded.

Old bundles keep verifying: the v1 demo run in this repository predates the field and verifies against the same procedure, which is the difference between a format that evolves and one that breaks its past.

## The discipline it enforces

Every provenance field answers a question a reviewer would otherwise have to ask. The questions a reviewer does not have to ask are the ones your record answered on its own. That is the whole practice.
`;

export { body };
