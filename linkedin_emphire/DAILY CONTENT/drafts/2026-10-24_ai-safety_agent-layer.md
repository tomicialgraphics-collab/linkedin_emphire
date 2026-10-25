# DRAFT POST 2026-10-24 — AI safety (agent layer)
Status: DRAFT, pending owner approval. NOT posted.
Pillar: AI Red Teaming / AI Safety (secondary). Mode: STANDALONE.
Supersedes: nothing (vulnzero standalone is 10-25, untouched).

POST TEXT (copy from the line below to the hashtags):

Most AI safety testing stops where the model ends.

I keep seeing teams ask the wrong question before launch. Is the model safe? Yes, it passed, here's the report. Nobody asks what the agent does with what it's handed.

The record from the last two years is a list of wrappers, not weights. EchoLeak in Microsoft 365 Copilot. ForcedLeak in Salesforce Agentforce. A prompt-injection chain that leaked secrets through Claude Code, Gemini CLI, and GitHub Copilot at once, rated 9.4. CVE-2026-21520, Copilot Studio, Microsoft's first indirect prompt injection CVE. 492 MCP servers public with no auth. 1,184 malicious skills on a registry people were told to trust.

The weights were fine.

The model in each one was probably doing its job. A model that does what it is asked is a good model, and that is exactly the problem, because the safety question was never what it would say. It was what the meeting invite, the ticket, the webhook, or the other agent was allowed to put in front of it, and whether anything would notice.

IBM put a number on it: about fifty agent incidents per company a year, a fifth of them high severity, counted across two thousand tech leaders. Two thirds of IT execs expect a public one inside eighteen months.

The model has no keys. The agent has all of them.

#AISafety #AIAgents #AIRedTeam #BreakingAI

=== GATE RECORD (10-24 fine-tune, PART 10 + 10.5) ===
MECHANICAL: 0 em dashes; 2 contractions (here's, it's; none first line,
none twice in one clause); straight quotes only; one idea per breath
(P3 is dense but seven short sentences); paragraph lengths 9/30/68/4/65/
38/11 = wildly uneven; first line 9 words, starts from a specific claim,
no compliment, not category 7; ends flat on a concrete image, no
question mark; 225 words + 4 hashtags (10-23 published without hashtags,
drop the last line to match the newest post).
STRUCTURE (standalone S1-S8): S1 7 paragraphs, 4-word beat "The weights
were fine.", dense P3 (7 sentences), no three equal blocks; S2 habitual
bridge "I keep seeing teams ask the wrong question before launch."
(relationship to topic, not thesis restated); S3 two period fragments
("The weights were fine.", "The agent has all of them."); S4 plain words
("doing its job", "here's the report"); S5 one dense exact pile (P3:
incident names, CVE, 9.4, 492, 1,184), everything else hedged (about
fifty, a fifth, two thirds, probably); S6 pivot "The weights were
fine." (checked against 10-21/10-22/10-23 pivots, none reused); S7
unlanded detail "a registry people were told to trust" (stated, left);
S8 one 26-word comma chain, point at the end; S9 none; D1 absent, D2
absent, D3 absent.
ARGUMENT TEST: arguable claim ("Most AI safety testing stops where the
model ends."), specific concession ("A model that does what it is asked
is a good model."), "The weights were fine." is the line a hostile
reader argues with.
MOTIF/CLOSER CHECK vs last 7 days: no pivot reuse; no "Not: X. This:
Y."; closer couplet is the approved echo shape (10-21 "All of those
look exactly the same... All of them are green."), not the 10-21 or
10-22 sardonic-fragment close; "the layer you do not own" (10-22 close,
used in Tanya 119w) deliberately NOT reused.
FACTS (all from ENGAGEMENT/potential_clients_2026-10-24.md, verified
10-24, no new claims): EchoLeak (M365 Copilot); ForcedLeak/PipeLeak
(Salesforce Agentforce); Claude Code + Gemini CLI + GitHub Copilot
prompt-injection chain, Anthropic rated CVSS 9.4; CVE-2026-21520
Copilot Studio, Microsoft's first IPI CVE; 492 unauthenticated MCP
servers; 1,184 malicious ClawHub skills (unnamed = hedge); IBM 2026
study of 2,000 tech leaders, avg 54 agent incidents/company/year, 17%
high severity (hedged to about fifty / a fifth); Workato/Censuswide Oct
2026, ~two-thirds of IT execs expect a public AI-agent incident in 18
months (hedged to two thirds / eighteen months).
SELF-REFERENCE: S2 bridge traces to the owner's red team work habit;
no invented incidents; no repo pitch, no funnel, no affiliation claim.
