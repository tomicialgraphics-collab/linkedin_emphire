---
deliverable: reference
id: 2026-11-09_infrastructure-principles-for-ai-red-teaming
date: 2026-11-09
audience: owner
status: ready
approved: no
warm: no
thread: answer to the question of which infrastructure and reliability principles matter most for AI red teaming on large projects, ranked by blast radius rather than by the order the list was given in
verified: no external statistic is used. The technical claims are about mechanism, and each is stated as something to check rather than as a claim about a named product or vendor.
---

# The infrastructure principles that actually matter for AI red teaming

**Written 2026-11-09. Read with `CURRICULUM/ai-redteam-and-research-master-curriculum.md`, which covers the model side. This covers the ground the model sits on.**

## The one-line answer

Twelve things, in order of blast radius, and the order is not the order of the list you were given:

1. Observability: logging, tracing, metrics, alerting
2. Identity: IAM, OAuth, JWT rotation, secrets management
3. API gateways and reverse proxies, with CORS and CSRF
4. The failure layer: timeouts, retries, exponential backoff, circuit breakers, idempotency, backpressure
5. Rate limiting, at the right place
6. Authorization depth: race conditions, locking, TOCTOU
7. Database access: SQL injection, parameterization, pooling
8. Caching and cache invalidation, including CDN and edge
9. CI/CD, IaC, Docker, Kubernetes
10. TLS, encryption at rest and in transit, and SSRF
11. SLOs, SLIs and error budgets
12. Deploys: feature flags, canary, blue-green, rollback, health checks

Everything else on that list is either tier two (know it, test it when it is present) or tier three (recognise the name, because it explains a finding you will otherwise misdiagnose).

## Why the list you were given is in the wrong order

That list is a backend engineering syllabus. It is ordered by how systems are built, not by how they break. For red teaming, three things decide the order: what an attacker can reach, what the action can do once it lands, and whether anyone can prove afterwards that it happened.

Almost every serious finding in a large LLM system in production is an ordinary web or infrastructure flaw with a natural-language front door. The model is rarely the weakest link. The gateway that forwards a header it should strip, the tool holding a credential it should not have, the retry that fires a payment twice, the log that cannot reconstruct which tool ran, the cache that returns one tenant's completion to another. None of those are model problems. All of them are on your list, and none of them are in the top ten of the list as given.

There is also a category the list omits entirely, covered at the end: nothing in it pins the model, the prompt, or the evaluation set, which is the thing that makes a finding reproducible or worthless.

---

## Tier one: must know deeply, must check on every engagement

### 1. Observability: logging, distributed tracing, metrics, alerting

The single most important item, and the one most teams under-invest in.

A red team report is only as good as the evidence behind it. If you cannot produce the trace, you have a story. For an agent, the trace is the finding: which prompt, which retrieved chunk, which tool call, which arguments, which response, which model version answered. Span per tool call, propagated correlation ID through the whole chain, and the raw input and output retained with redaction.

Three specific tests:

- Can you reconstruct, from logs alone, the full path of a single agent run that happened three days ago?
- Does the log record the model identifier and prompt version, or only the app version?
- Is the log itself a data leak? Prompt logs hold the personal data that was in the prompt, and the credentials a model was tricked into repeating.

Alerting belongs here because detection is half the control. A finding that no alert would ever fire on is a finding the client cannot operate.

### 2. Identity: IAM, OAuth, JWT rotation, secrets management

The core failure of an agent is the confused deputy: it acts with its own permissions rather than the user's, so a user who can read one document can make the agent read all of them. Everything you need to test lives here.

What to check: is the token on-behalf-of the user or a service account, what scopes does each tool hold, are credentials short-lived, does anything rotate, are secrets in environment variables where a model or a log can reach them. Then the JWT specifics, because they are a reliable source of findings: algorithm confusion, `kid` injection, missing audience or expiry validation, a `jku` header the server follows.

The red team question that finds the most: what can this credential do that the task does not require. Broad scope on a tool is the finding, even when nothing has been exploited yet.

### 3. API gateways and reverse proxies, with CORS and CSRF

This is where trust boundaries are declared and where they are quietly broken.

- Header trust: `X-Forwarded-For` spoofing to defeat an IP allowlist, `X-User-Id` or `X-Tenant` set by the client and believed by the app.
- Path normalisation differences between proxy and application, which turn a blocked route into a reachable one.
- Gateway filters that do not run on streamed responses, so the injected payload arrives in the second chunk.
- CORS with credentials and a wildcard or reflected origin, on an app that authenticates by cookie. Combine with a permissive fetch in the browser and the completion leaves the tenant.

CSRF still matters in LLM apps for the boring reason: the expensive endpoint is a POST that spends tokens, and a third-party page can trigger it.

A WAF is not a control for prompt injection and should never be scored as one. It stops scripted volume, which is useful, and it stops semantic attack about as well as a spell checker stops a lie. Test it by encoding: the request that gets through to the model is usually not the request the rule was written for.

### 4. The failure layer: timeouts, retries, backoff, circuit breakers, idempotency, backpressure

This is the highest-severity group after identity, because this is where an agent's action stops being one action.

An agent that times out on a write and retries it has performed the write twice, and the second one is invisible unless the tool is idempotent and the request carries a key. Ask for the idempotency key on every mutating tool call. If there is not one, you have found a class of bug rather than an instance.

Retries also amplify: a client with three retries behind a proxy with three retries behind a load balancer with retry-on-5xx is twenty-seven requests from one. Exponential backoff without jitter synchronises the herd. A circuit breaker is a switch an attacker can flip deliberately by making the dependency fail for long enough, which converts a partial outage into a full one. Backpressure decides whether a flood is absorbed or queued until memory runs out.

For LLM systems specifically, add the cost channel: no per-user token budget, no maximum output length, an agent loop with a step ceiling that is missing or high, and a recursive plan-and-execute that bills per iteration. Denial of wallet is a real finding and it needs no exploit skill at all.

### 5. Rate limiting, applied at the right place

If limits exist only at the gateway and the app is reachable another way, there is no limit. If limits are per IP and the app trusts a client-supplied identity, the limit is a suggestion. Per-user, per-token and per-tenant are different controls and only one of them protects the bill.

Two red team uses beyond availability: the limit is your enumeration budget, so measure it, and the 429 pattern is a detection signal the client may already have.

### 6. Authorization depth: race conditions, locking, TOCTOU, distributed locks

The check-then-act gap is where agent bugs live, because an agent's plan takes seconds and permissions can change inside it. Revoke a user mid-run and watch whether the agent finishes the job it started with the authority it had when it began.

Same shape at the data layer: two agents writing the same record, a lock held with no expiry, an optimistic check on a version column that the update statement does not actually condition on. Read the update statement. The lock is only real in the SQL.

Eventual consistency belongs in this item rather than in the tier-three theory pile: a revoked permission that takes seconds to propagate, or a deleted document still served by a replica, is a live finding with a reproducible window.

### 7. Database access: SQL injection, parameterization, connection pooling

If a model writes SQL, you have a text-to-SQL injection surface with the database's full authority behind it, and it is the highest-severity defect commonly found in enterprise LLM systems. The fix is not a better prompt. It is a read-only role, parameterization where the query is assembled, row-level security, and a statement allowlist for anything an agent can trigger.

Pooling is here for two reasons: exhaustion is a cheap denial of service from inside an agent loop, and a pool shared across tenants can hand a connection with session state attached to the wrong request.

### 8. Caching and cache invalidation, including CDN and edge

A cache is a sharing mechanism and asking who shares what with whom is the whole test. Cross-tenant leakage happens through a key that does not include the tenant, a response cached before authorization ran, or a CDN in front of an endpoint that varies on a header nobody told it about.

For LLM apps specifically: a cached completion goes stale in a way ordinary data does not, because the correct answer depended on a prompt version that has since changed. And prompt or prefix caching, where the cached prefix includes one user's document, is a leak with no obvious symptom.

The deeper point in the same item is that most of the interesting reduction and most of the interesting leakage are library-level rather than file-level properties. Cache keys are the same argument: the question is what the unit of sharing is.

### 9. CI/CD, IaC, Docker, Kubernetes

Three separate reasons this is tier one.

Reproducibility: you cannot test production and you cannot rebuild production by hand. Terraform and the container definition are how you get a faithful copy of the target, which is the difference between a finding and an anecdote.

Scanning the pipeline: secrets committed in IaC, a security group open to the world, an IAM policy with a wildcard action, a privileged pod, a service account token mounted into every workload, an image built from a base nobody pinned, a model artefact pulled by tag rather than digest. Any of those is a finding in a week of review.

The eval suite in the pipeline: this is the part most red teams skip and the part that makes the work durable. Every confirmed finding becomes a test case that runs on every deploy. Without that, the fix is a patch and the bug returns in three months under a new prompt.

### 10. TLS, encryption at rest and in transit, and SSRF

TLS is table stakes and the finding is never "TLS is off", it is "TLS is not verified": a client with verification disabled, a certificate pinned to nothing, service-to-service traffic in the clear inside the cluster on the assumption that the network is trusted.

The high-value item in this group is SSRF, because the LLM version has a natural front door. A model with a fetch or browse tool, plus a cloud metadata endpoint, plus an over-broad instance role, is a credential theft chain that needs no jailbreak worth the name. Test it as infrastructure, not as prompting: what can the fetch tool reach, and with which identity.

Encryption at rest matters for the new stores: vector databases hold the same personal data as the source documents and are frequently built without the access control the source had.

### 11. SLOs, SLIs and error budgets

This looks like an operations topic and is really an evidence topic. A finding without an SLI is an opinion about risk. Saying that the missing step ceiling moves P99 completion cost from 0.4 cents to 11 dollars, or that the retry storm takes the write path past its error budget, is how a finding gets fixed.

It also tells you where the client already has eyes, which is where your work compounds, and where nobody is watching, which is where you start.

### 12. Deploys: feature flags, canary, blue-green, rollback, health checks and probes

The prompt and the model are deploys. A team that ships prompt changes by editing a string in a dashboard with no version, no canary and no rollback cannot answer the first question any finding raises, which is whether the bug is still there.

Health checks have a specific AI failure: a probe that returns 200 because the process is up, while the model is degraded, rate limited, or silently answering from a fallback. Test whether readiness reflects the ability to answer, not the ability to accept a connection.

Rollback has a matching one: rolling back the app while leaving the index, the cache and the fine-tune in place is not a rollback.

---

## Tier two: know well, test when present

| Principle | The only way it shows up in a finding |
|---|---|
| Message queues, pub/sub, event-driven | Unauthenticated broker, replay of a consumed message, a poison message that stalls the consumer, and a dead letter queue holding raw prompts and personal data that nobody classified |
| Dead letter queues | Usually the most valuable store to read and the least protected, because it exists to hold failures and failures contain input |
| Webhooks | Signature not verified, no replay window, or the receiver fetches a URL the caller supplied |
| WebSockets, SSE, long polling | Authorization checked when the stream opens and never again, or a token in the query string and therefore in the access log |
| API versioning, semantic versioning | The old version is still up and does not have the fix; a model alias that moves under you between test and report |
| DNS | Subdomain takeover on a decommissioned model endpoint, and DNS rebinding to defeat an SSRF allowlist |
| Clock skew | JWT expiry and replay windows; also makes audit logs order differently on two hosts, which matters when you are reconstructing a run |
| Multi-region, DR, backups, failover | Prompts and their contents crossing a residency boundary; whether the eval set and system prompts are actually backed up |
| Sharding, partitioning, replicas, leader election, CAP | Replica lag as an invisibility window for a deleted document or a revoked permission |
| Distributed transactions, saga | Partial states an attacker can drive, where the compensation step is missing and the agent has already acted |
| Cron jobs | Scheduled agent jobs run with elevated credentials, unwatched, and overlapping runs double an action |
| Dependency hell, build caching, Helm, build integrity | Supply chain: unpinned model artefacts, a poisoned package, a chart values file that disables auth in a non-production profile that reaches production |
| Memory leaks, garbage collection, thread safety | Long-running model servers with request state in a global: the context bleed where one user's conversation appears in another's |
| Autoscaling, horizontal and vertical scaling, load balancing, service discovery | Autoscaling as cost amplification, and traffic that discovers the pod directly and never passes the gateway |
| Cost optimisation | The budget anomaly is often the first and only detection signal for a slow extraction or a denial of wallet |
| Cold starts, serverless limits | Timing side channel on caching, and the execution cap that silently truncates a long agent run mid-action |
| Latency, throughput, P99, tail latency | Where timeouts and retries interact to produce duplicates, and where a step ceiling shows up as a budget number |
| gRPC, HTTP/2, HTTP/3, TCP vs UDP | Stream multiplexing abuse, reflection left on in a service the agent can reach |
| Chaos engineering | Not a principle to implement before red teaming, but the same method and the same instrumentation, so it is the closest adjacent discipline and a natural ally inside the client |
| On-call, production incidents, postmortems | Not controls. This is the process that consumes your findings, and knowing how it works is how a finding becomes a ticket instead of a PDF |

## Tier three: recognise the name

Load balancing, vertical and horizontal scaling, service discovery, CDN, event-driven architecture, optimistic and pessimistic locking as concepts, distributed locks as products, garbage collection internals, TCP versus UDP internals, static sharding schemes. You need the vocabulary because it appears in architecture diagrams and because someone in the room will use it to explain away your finding. You do not need depth to write a test.

## What the list leaves out, and it is the most important part

Nothing in those hundred-plus items is about the model, the prompt, or the evaluation set. For AI red teaming that is the whole game, because everything above tells you how a system fails and none of it tells you whether the failure is still there next Tuesday.

Four additions:

1. **Version pinning.** Model identifier and revision, prompt version, retrieval index snapshot, tool schema version, temperature and seed. Without all six recorded, a finding has no denominator and cannot be reproduced.
2. **The evaluation set as an asset.** Whose test cases they are, who can edit them, and whether the history of edits is kept. An eval suite the vendor controls is a certification, not a measurement.
3. **Data provenance.** Where the retrieval corpus came from, who can write to it, and when it was last checked. Poisoning is a supply chain problem before it is a prompting problem.
4. **The kill switch and the human approval gate.** Not on the list at all, and it is the control every governance review will ask about: what stops an agent mid-run, and which decisions require a person who is not the agent.

## How to use this on a large project

Ask these twelve questions in the kickoff, in this order. Each maps to one tier-one item, and each answer tells you where the week goes.

1. Show me the trace of the last agent run you can reconstruct end to end.
2. What scopes does each tool credential hold, and which of them is on behalf of a user?
3. Which headers does the gateway trust from the client, and which routes bypass it?
4. Which mutating tool calls carry an idempotency key, and what is the step ceiling on the loop?
5. Where is rate limiting enforced, and per what unit?
6. What happens if I revoke a permission while an agent is mid-run?
7. Can the model write SQL, and with which database role?
8. What is in the cache key, and does it include the tenant?
9. Which finding from the last review became a test in CI?
10. What can the fetch tool reach, and as which identity?
11. Which SLI moves if this system is abused, and who is paged?
12. How is a prompt change shipped, versioned and rolled back?

If the answers to one, four, six and nine are weak, the engagement is about measurement before it is about exploitation, and saying so early is worth more than a long list of low findings.

## The honest caveat

This is a menu of failure modes, not a curriculum. Depth on the twelve above is roughly a year of deliberate work, and nobody holds all of it well. What is genuinely scarce is not the infrastructure knowledge, which is documented and learnable, but the discipline of turning a break into a number someone else can rerun. Use the list to know where to look. Use the test suite to make what you find count.
