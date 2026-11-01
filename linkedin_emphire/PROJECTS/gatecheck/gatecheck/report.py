"""Three outputs, three readers.

markdown   the reviewer, in the pull request, deciding in thirty seconds
sarif      the code scanning tab, where findings get assigned and closed
json       the next run, which reads this one as its baseline

The markdown leads with what changed, because a comment that opens with
48 findings every time gets muted after the second pull request.
"""
from __future__ import annotations

import json

from .models import Finding, Severity

BADGE = {"critical": "CRITICAL", "high": "HIGH", "medium": "MEDIUM", "low": "LOW"}
RULE_ID = {
    "prompt-injection": "GC001",
    "system-prompt-leak": "GC002",
    "tool-misuse": "GC003",
    "data-exfiltration": "GC004",
    "multi-turn-escalation": "GC005",
    "encoding-bypass": "GC006",
}


def markdown(result: dict, *, max_rows: int = 12) -> str:
    """A PR comment: verdict, then the delta, then the detail."""
    verdict = result["verdict"]
    if verdict.get("status") == "error":
        # A run that reached no engine says nothing about the target. It
        # must not borrow the language of a pass or a fix.
        lines = ["## gatecheck: ERROR", "", f"**{verdict['reason']}**", ""]
        lines.append(
            f"`{result['target']}` | tools: {', '.join(result['tools_run']) or 'none'}"
            f" | {result['attacks_run']} attacks ran"
        )
        lines.append("")
        lines.append(
            "No attack was executed, so this run cannot say whether the agent is "
            "better, worse or unchanged. It is not a pass."
        )
        lines.append("")
        if result.get("tools_skipped"):
            lines.append("Skipped:")
            lines.append("")
            for tool, why in result["tools_skipped"].items():
                lines.append(f"- `{tool}`: {why}")
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    head = "## gatecheck: PASS" if verdict["ok"] else "## gatecheck: BLOCKED"
    lines = [head, ""]
    if not verdict["ok"]:
        lines.append(f"**{verdict['reason']}**")
        lines.append("")
    lines.append(
        f"`{result['target']}` | tools: {', '.join(result['tools_run']) or 'none'}"
        f" | {result['summary']['total']} findings"
        f" | {result['summary']['new']} new"
        f" | {result['summary']['fixed']} fixed"
    )
    lines.append("")

    if result["new"] or result["worse"]:
        lines.append("### New or worse in this change")
        lines.append("")
        lines.append("| severity | category | finding | attack | found by |")
        lines.append("| --- | --- | --- | --- | --- |")
        rows = [(f, "new") for f in result["new"]] + [(w["finding"], "worse") for w in result["worse"]]
        rows.sort(key=lambda r: -r[0].severity.rank)
        for finding, kind in rows[:max_rows]:
            label = BADGE[finding.severity.value]
            if kind == "worse":
                label += " (was lower)"
            found_by = ", ".join(finding.found_by)
            if finding.runs > 1:
                found_by += f" ({finding.hits}/{finding.runs} runs)"
            lines.append(
                f"| {label} | `{finding.category}` | {finding.title} | "
                f"`{finding.attack_id}` | {found_by} |"
            )
        if len(rows) > max_rows:
            lines.append(f"| ... | | {len(rows) - max_rows} more | | |")
        lines.append("")
        top = next((f for f, _ in sorted(rows, key=lambda r: -r[0].severity.rank)), None)
        if top is not None:
            lines.append("<details><summary>Evidence for the highest-severity finding</summary>")
            lines.append("")
            lines.append(f"**Attack** `{top.attack_id}` ({top.turns} turn(s))")
            lines.append("")
            lines.append("```text")
            lines.append(top.evidence.prompt[:400])
            lines.append("```")
            lines.append("")
            lines.append("**Response**")
            lines.append("")
            lines.append("```text")
            lines.append(top.evidence.excerpt(400))
            lines.append("```")
            lines.append("")
            lines.append("</details>")
            lines.append("")

    if result["fixed"]:
        lines.append(f"### Fixed since the baseline ({len(result['fixed'])})")
        lines.append("")
        for entry in result["fixed"][:10]:
            lines.append(f"- `{entry['category']}` {entry.get('title', '')}")
        lines.append("")

    # What is left, not only what changed. "1 finding, 5 fixed" tells a
    # reader nothing about which one survived, and that is the question a
    # security review asks first.
    if result.get("unchanged"):
        lines.append(f"### Still present ({len(result['unchanged'])})")
        lines.append("")
        for finding in sorted(result["unchanged"], key=lambda f: -f.severity.rank)[:10]:
            rate = f" ({finding.hits}/{finding.runs} runs)" if finding.runs > 1 else ""
            lines.append(
                f"- {BADGE[finding.severity.value]} `{finding.category}` "
                f"{finding.title} `{finding.attack_id}`{rate}"
            )
        lines.append("")

    if result["errors"]:
        lines.append("### Tool errors, recorded not hidden")
        lines.append("")
        for e in result["errors"][:10]:
            lines.append(f"- {e}")
        lines.append("")

    lines.append(f"<sub>baseline: {result['baseline_used'] or 'none (first run)'} | "
                 f"run: {result['run_id']}</sub>")
    return "\n".join(lines)


def sarif(result: dict, *, tool_version: str = "0.1.0") -> dict:
    """SARIF 2.1.0, so the findings land in the code scanning tab."""
    rules = {}
    results = []
    for finding in result["all_findings"]:
        rule_id = RULE_ID.get(finding.category, "GC999")
        rules.setdefault(
            rule_id,
            {
                "id": rule_id,
                "name": finding.category,
                "shortDescription": {"text": finding.title},
                "properties": {"category": finding.category},
            },
        )
        results.append(
            {
                "ruleId": rule_id,
                "level": _sarif_level(finding.severity),
                "message": {"text": f"{finding.title} (found by {', '.join(finding.found_by)})"},
                "locations": [
                    {
                        "physicalLocation": {
                            "artifactLocation": {"uri": result.get("target_file", "gatecheck.yml")}
                        }
                    }
                ],
                "partialFingerprints": {"gatecheckFingerprint": finding.fingerprint},
                "properties": {
                    "severity": finding.severity.value,
                    "attack": finding.attack_id,
                    "turns": finding.turns,
                    "prompt": finding.evidence.prompt[:1000],
                    "response": finding.evidence.excerpt(1000),
                },
            }
        )
    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "gatecheck",
                        "informationUri": "https://github.com/",
                        "version": tool_version,
                        "rules": list(rules.values()),
                    }
                },
                "results": results,
            }
        ],
    }


def _sarif_level(severity: Severity) -> str:
    return {
        Severity.CRITICAL: "error",
        Severity.HIGH: "error",
        Severity.MEDIUM: "warning",
        Severity.LOW: "note",
    }[severity]


def as_json(result: dict) -> str:
    return json.dumps(result, indent=2, default=_default) + "\n"


def _default(obj):
    if isinstance(obj, Finding):
        return finding_dict(obj)
    if isinstance(obj, Severity):
        return obj.value
    raise TypeError(f"not serialisable: {type(obj)}")


def finding_dict(f: Finding) -> dict:
    return {
        "id": f.id,
        "fingerprint": f.fingerprint,
        "category": f.category,
        "severity": f.severity.value,
        "title": f.title,
        "found_by": f.found_by,
        "attack_id": f.attack_id,
        "turns": f.turns,
        "hits": f.hits,
        "runs": f.runs,
        "evidence": {"prompt": f.evidence.prompt, "response": f.evidence.response,
                     "actions": f.evidence.actions},
        "first_seen": f.first_seen,
        "last_seen": f.last_seen,
    }
