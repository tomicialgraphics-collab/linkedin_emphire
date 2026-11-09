# 03 Retrieval and agents

Covers `RK-01` to `RK-09` and `AG-01` to `AG-25`.

## The corpus is untrusted input

Every retrieval system is a trust boundary that people forget to draw, because the corpus feels like it belongs to the company. It usually does. It also usually accepts documents from a shared drive, a scrape, an email import or a support queue, and each of those is a write path an outsider can sometimes reach.

Three questions, in this order:

1. **Who can write to the index.** Nothing else matters until this is answered. Poisoning is a write access problem before it is a prompt problem.
2. **Whether retrieval filters on the asking user's permissions.** Filtering after ranking leaks existence: a user without access still learns that a document exists and roughly what it is about.
3. **Whether retrieved text is delimited and ranked below the user turn.** Chunk boundary attacks depend on the answer, because a document that looks harmless in each piece can carry a complete instruction across two.

The persistence is the severity. A single-shot injection ends when the session ends; a poisoned document is served to everyone who queries it, indefinitely, and looks like normal content to every reviewer who reads it later.

## Agency is a permission question

A tool is a capability grant. The interesting question is never "can the agent call this tool" but "what can this tool do that the task does not require, and as whose identity".

Work three columns:

| Tool | Credential behind it | What that credential can reach |
|---|---|---|
| Support lookup | Service account, read across all tenants | Every customer record |
| Ticket update | Same account, write scope | Any ticket, any customer |
| Document fetch | Outbound network, no allowlist | Internal networks, cloud metadata |

Three of those answers are findings before a single exploit is attempted. Excess scope is a finding even when nothing has been exploited yet, because it is the thing that turns every other bug into an incident.

## The confused deputy, in one paragraph

The agent holds a permission the current user does not. If the agent acts on the user's behalf with its own authority, then any input that can steer the agent can borrow that authority. This is why prompt injection in an agentic system is an authorization bypass rather than a content problem, and why the fix is per-request scoping and on-behalf-of tokens rather than a better prompt.

## The four controls that decide severity

1. **Scoping.** Per request, per user, least privilege, short lived. Ask what the token can do, not what the agent needs.
2. **The approval gate.** What it gates, whether the agent can reach it, whether a retry can skip it, whether a timeout starves it into auto-approval, and whether the person reviewing can understand the decision. `AG-09`, `GV-25`.
3. **The step ceiling.** A missing ceiling is a denial of wallet finding with no exploit skill required. `AG-20`.
4. **The kill switch.** Exercised, not documented. If it does not reach subagents spawned after the stop, it is not a kill switch. `AG-14`.

## Agent-specific surfaces worth naming

- **Tool descriptions.** They are trusted unread, they go into the context, and they can carry instructions. Read every one.
- **Tool rug pulls.** The definition approved on Monday is not always the definition running on Friday.
- **MCP servers.** A third party with read, write and call access to your agent. Ask who reviewed it and what it can reach.
- **Memory.** A write to persistent memory returns in fresh sessions and quietly changes behaviour for later users.
- **Files and PDFs.** Body text is the obvious channel. Comments, metadata, alt text and filenames are the ones nobody checks.
- **Fetch and browse tools.** The LLM version of SSRF has a natural front door: a URL the model chooses, a metadata endpoint that answers, and a role attached to the instance.

## What to write down

- The map: channels, tools, credentials, sinks. One page.
- For each tool, the scope that would be sufficient and the scope that exists.
- The propagation test: one bad input, how far it travelled, where it stopped, and what stopped it.
- The controls above, present or absent, with the evidence.
