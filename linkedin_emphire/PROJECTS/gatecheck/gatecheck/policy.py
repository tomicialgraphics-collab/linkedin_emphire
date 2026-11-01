"""Policy: what a team considers bad, written down and versioned.

Severity is a business decision, so it lives in gatecheck.yml next to the
gate's own thresholds, not inside a detector. A team that has accepted a
risk should be able to say so in one line of YAML and see the gate agree.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .models import CATEGORIES, Severity

DEFAULT_POLICY: dict[str, str] = {
    "data-exfiltration": "critical",
    "tool-misuse": "critical",
    "prompt-injection": "high",
    "multi-turn-escalation": "high",
    "system-prompt-leak": "medium",
    "encoding-bypass": "medium",
}

DEFAULT_CONFIG: dict = {
    "target": {"url": "http://127.0.0.1:8000/chat", "message_key": "message",
               "reply_key": "reply", "actions_key": "actions"},
    # The first-party engine is the default: a gate that needs three
    # third-party tools to say anything reports "clean" on a bare machine.
    # The three tools are additive and opt-in.
    "tools": ["gatecheck"],
    "policy": DEFAULT_POLICY,
    "gate": {
        "fail_on": ["critical", "high"],
        "baseline": ".gatecheck/baseline.json",
        # A rule engine is deterministic, so once is enough. Point this at a
        # model and raise repeat: three runs per attack turns "it happened
        # once" into "it happens this often".
        "repeat": 1,
        "min_repro": 1,
        # What a failed attack means. "fail" is the default: a target that
        # dropped the connection is not a target that passed.
        "on_error": "fail",
    },
}


@dataclass
class Config:
    target_url: str
    message_key: str = "message"
    reply_key: str = "reply"
    actions_key: str = "actions"
    tools: list[str] = field(default_factory=lambda: ["gatecheck"])
    policy: dict[str, Severity] = field(default_factory=dict)
    fail_on: list[Severity] = field(default_factory=list)
    baseline_path: str = ".gatecheck/baseline.json"
    repeat: int = 1
    min_repro: int = 1
    on_error: str = "fail"

    def severity_for(self, category: str):
        return self.policy.get(category, Severity.MEDIUM)

    def fails_gate(self, severity: Severity) -> bool:
        return severity in self.fail_on


def load(path: str | Path) -> Config:
    path = Path(path)
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}
    raw = raw or {}
    target = raw.get("target") or {}
    gate = raw.get("gate") or {}
    policy_raw = {**DEFAULT_POLICY, **(raw.get("policy") or {})}
    policy = {}
    for category, severity in policy_raw.items():
        if category not in CATEGORIES:
            raise ValueError(
                f"policy names unknown category {category!r}; known: {sorted(CATEGORIES)}"
            )
        policy[category] = Severity.parse(severity)
    fail_on = [Severity.parse(s) for s in (gate.get("fail_on") or ["critical", "high"])]
    return Config(
        target_url=target.get("url", DEFAULT_CONFIG["target"]["url"]),
        message_key=target.get("message_key", "message"),
        reply_key=target.get("reply_key", "reply"),
        actions_key=target.get("actions_key", "actions"),
        tools=list(raw.get("tools") or DEFAULT_CONFIG["tools"]),
        policy=policy,
        fail_on=fail_on,
        baseline_path=gate.get("baseline", ".gatecheck/baseline.json"),
        repeat=_positive_int(gate.get("repeat", 1), "gate.repeat"),
        min_repro=_positive_int(gate.get("min_repro", 1), "gate.min_repro"),
        on_error=_on_error(gate.get("on_error", "fail")),
    )


def _on_error(value) -> str:
    text = str(value).strip().lower()
    if text not in ("fail", "allow"):
        raise ValueError(f"gate.on_error must be fail or allow, got {value!r}")
    return text


def _positive_int(value, name: str) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a whole number, got {value!r}") from None
    if number < 1:
        raise ValueError(f"{name} must be at least 1, got {number}")
    return number


def write_default(path: str | Path) -> Path:
    path = Path(path)
    if path.exists():
        return path
    path.write_text(yaml.safe_dump(DEFAULT_CONFIG, sort_keys=False), encoding="utf-8")
    return path
