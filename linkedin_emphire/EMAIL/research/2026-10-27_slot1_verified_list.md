# VERIFIED LIST - research slot 1 (week of 10-27 to 11-02)
# Role: agent ran the research. Owner scans this list, picks one
# item (or adjusts, or passes to the honest week). Nothing sends
# before the owner's pick. Then the agent produces the
# personalized send per contact (protocol, weekly pipeline).
Date: 2026-10-27
Items: 2 (item 1 re-run executed by the agent; item 2 verified to
source with the live re-scan flagged as an owner job)

============================================================
ITEM 1 (recommended): the S-1 number the filing does not contain
============================================================

CLAIM: the most-quoted efficiency number in the Anthropic S-1
(filed 10-26, the document everyone in this feed is quoting):
"TTM revenue per employee over $6.6 million as of September 30,
2026, up from $1.4 million a year earlier" (MD&A, page 136).
Paired with it in the same filing: "Claude wrote more than 90%
of contributions to Anthropic's codebase in September 2026."

RESULT: the filing's financial statements end June 30, 2026. The
maximum TTM revenue computable from the document itself:
FY2025 ($4,585M) minus H1 2025 ($1,163M) plus H1 2026 ($16,286M)
equals $19,708M, about $19.7 billion. Divided by the roughly
5,300 employees the filing names: $3.7 million per employee, not
$6.6 million. The $6.6 million figure implies a TTM of about
$35 billion, which requires Q3 2026 revenue of about $15.3
billion, a quarter that appears nowhere in the filing (it would
be 94% of the entire first half). The 90 percent of code figure
carries no disclosed definition and no independent re-run.

METHOD: EDGAR accession 0001628280-26-067168, CIK 2130357, file
333-299633. The per-employee passage is MD&A page 136; the
components are in the H1 2026, FY2025, and FY2024 financial
statements (H1 link in circulation: sec.gov/Archives/edgar/data/
2130357/000162828026067168/anthropicpbc-sx1.htm). The arithmetic
is three subtractions and one division, above. Re-computed
2026-10-27 by the agent; any analyst re-runs it in under five
minutes.

HONEST LINE: not proof of misstatement. Q3 2026 revenue is not in
the document (the financials end June 30), and growth is
accelerating (H1 2026 was fourteen times H1 2025), so a fifteen
billion dollar quarter is possible and the $6.6 million could be
exactly right. The finding is narrower and stranger: the single
most-quoted number in the most-watched document of the month is a
management number about a quarter the document does not contain.
Even the filing-supported number, $3.7 million, is up from $1.4
million, and Yahoo's cross-check says only Nvidia does better per
employee ($7.2 million).

WHY THIS WEEK: filed yesterday (10-26). The number is already
circulating in every S-1 thread, including this owner's feed
conversations. The IPO window is 11-17 to 02-28 (Allie's note),
so this number has weeks of air left. The list seed is full of
S-1 engagers.

SUBJECT OPTIONS (1 to 20 chars, lowercase): "the s-1 number"
FRAMINGS:
PRACTITIONER (method-first):
"Let me show you a number I re-ran this week, because it is the
one number in that filing that the filing does not contain. The
arithmetic takes two minutes, and it is below."
DECISION-MAKER (consequence-first):
"There is a number in that document that nobody can re-run, and
your next board pack will quote it. When the room asks how you
verified it, the answer you can give is: it is not in the
document. Here is what is."
TEASER: none this week (no verified candidate yet for next week,
R8, no fake countdown)

OWNER SCAN (2 minutes): check the four inputs yourself, FY2025
equals 4,585, H1 2025 equals 1,163, H1 2026 equals 16,286,
headcount about 5,300, and the passage on MD&A page 136. If the
inputs hold, the finding holds. The one thing to watch: if the
company puts Q3 2026 revenue in a future filing at about $15
billion or more, the $6.6 million was right, and the honest line
already says so.

============================================================
ITEM 2: the screen that was sold as the fix (ClawHub state)
============================================================

CLAIM: the story in circulation after the ClawHavoc cleanup:
ClawHub, the OpenClaw skill marketplace, is now screened. The
marketplace integrated VirusTotal and ClawScan screening, so the
1,184 malicious skills are a closed chapter.

RESULT: the verified state, four independent sources:
Koi Security (Jan 27 to Feb 1, 2026): 341 of 2,857 skills
malicious, about 12%, 335 of them one coordinated campaign
delivering Atomic macOS Stealer.
Antiy CERT (as of Feb 5, 2026): 1,184 malicious skills in the
registry's history, 12 author IDs, one account (hightower6eu)
published 677 of them; after the mass removals the registry held
3,498 skills, and 60 packages tied to one account (14,285
downloads) were still accessible at publication.
Snyk ToxicSkills (Feb 2026, 3,984 skills audited across ClawHub
and skills.sh): 36.8 percent with at least one security flaw,
13.4 percent critical, 76 confirmed working payloads, 8 still
public at publication; average time to detection 47 days, the
longest-lived skill ran 112 days with over 9,000 installs.
Unit42 (Feb to May 2026, after screening went live): five
malicious skills still unblocked.
tobira.ai (Sept 10, 2026, 67,453 skill versions): the three main
scanner families agree on 0.69 percent of what they flag.

METHOD: all sources are public reports, linked in the log below.
Cross-verified by the agent on 2026-10-27 (four independent
reports agree on the 1,184 count and the 12-account attribution).
The live re-run is a registry re-scan with public tooling
(ClawScan, or the Snyk audit method), a 30-minute job, and the 60
packages Antiy named are a ready-made re-check list. Flagged
honestly: the agent could not execute the live registry scan from
this environment, so the live number is an owner job with the
method attached, not a number the agent ran.

HONEST LINE: the registry size and contamination rate move
(12 percent, then 7.7 percent, then cleanup), so the counts are a
state, not a verdict, and the 1,184 is a February number. The
fresh finding is not the 1,184. It is the 0.69 percent agreement
between the screeners that were sold as the fix, and the five
skills that stayed live after the screening was deployed. The
class, not this campaign, is the finding.

WHY THIS WEEK: the agent-ecosystem list (the agent room, the MCP
thread) installs skills the way the web installs extensions, and
the EchoLeak line (Forbes, June 2026: "both vulnerabilities were
patched, but the underlying class was not") is the pattern. The
marketplace is the first supply chain an agent touches, and the
cleanup story is what buyers will quote.

SUBJECT OPTIONS: "0.69 percent"
FRAMINGS:
PRACTITIONER (method-first):
"The cleanup sold a story: the registry is now screened. I checked
what the screeners actually agree on. The number is 0.69 percent,
and here is the re-check list if you want to run it yourself."
DECISION-MAKER (consequence-first):
"Your agent's first supply chain is the marketplace it installs
from. The screening sold as the fix has a measured agreement
rate. Here is the number, and the question your next
questionnaire will ask about it."
TEASER: none this week (R8)

============================================================
SOURCE LOG (item 2 cross-verification, 2026-10-27)
============================================================
- termdock.com/en/blog/clawhub-malicious-skills-incident (timeline:
  341 to 824 to 1,184)
- bulwarkai.io/blog/clawhavoc-analysis (Antiy CERT 1,184, 12
  accounts, 677 from one)
- antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign
  (original Antiy CERT report, upload policy, 60 still accessible)
- sparkagents.com/research/the-brain-problem (numbers table, all
  counts)
- cyberdesserts.com OpenClaw security post (Snyk ToxicSkills:
  3,984 audited, 36%, 1,467 with flaws, 91% injection plus
  malware)
- unit42.paloaltonetworks.com OpenClaw supply chain post (screening
  deployed, 5 unblocked, Feb to May 2026)
- blog.tobira.ai skill marketplace post (0.69% scanner agreement,
  67,453 versions, Sept 10 2026)
- venturebeat.com agent backdoor post (May 2026, no detection
  category for the pattern)
Item 1 sources:
- saastr.com S-1 learnings (FY2025 4,585, H1 2026 16,286, H1 2025
  1,163, $6.6M per employee)
- finance.yahoo.com IPO live updates + per-employee article
  (5,300 employees as of Sept 30, Nvidia $7.2M cross-check)
- kepler.ai S-1 breakdown (MD&A page 136 citation of the
  per-employee passage, 900% NRR, customer counts)
- hackernoon.com S-1 post (back-of-envelope: 5,300 x $6.6M about
  $35B TTM)
- sec.gov EDGAR accession 0001628280-26-067168 (the filing itself)
- agenticbytes.substack.com (900% NRR definition: three-month
  windows, excludes Pro and Max)
- animaapp.com blog (90% of code contributions, Sept 2026)

## RESEARCH SLOT 1 STATE

ITEM 1: VERIFIED (re-run executed by the agent, 2026-10-27,
fingerprint above), AWAITING OWNER SCAN
ITEM 2: VERIFIED TO SOURCE (live registry re-scan flagged as an
owner job), AWAITING OWNER SCAN
PICK: (owner fills in: item 1 / item 2 / adjust / pass to honest
week)
PERSONALIZED SENDS: not generated (after the pick)

Last updated: 2026-10-27 (slot 1 research complete, owner scan
pending)
