"""gatecheck command line.

  gatecheck init                       write gatecheck.yml
  gatecheck run                        run the gate against the target
  gatecheck run --demo vulnerable      run it against the bundled broken agent
  gatecheck run --demo fixed           run it against the hardened agent
  gatecheck accept <finding-id> -r "why"
  gatecheck report <run-dir> --format md|sarif|json
"""
from __future__ import annotations

import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

from . import __version__
from .baseline import Baseline
from .engines import ENGINES
from .models import Severity, dedupe
from .policy import Config, load, write_default
from .report import as_json, markdown, sarif
from .targets import HttpTarget, ServedTarget


def _now_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:6]


def cmd_init(args) -> int:
    path = write_default(args.config)
    baseline_dir = Path(args.baseline).parent
    baseline_dir.mkdir(parents=True, exist_ok=True)
    print(f"wrote {path}")
    print(f"baseline will live at {args.baseline}")
    print()
    print("next: point target.url at your agent, then run `gatecheck run`")
    return 0


def _resolve_target(args, config: Config):
    """Return (target, context manager or None)."""
    if args.demo:
        from demo.agent import hardened, vulnerable

        fn = vulnerable if args.demo == "vulnerable" else hardened
        ctx = ServedTarget(fn)
        return ctx.__enter__(), ctx
    return HttpTarget(
        args.url or config.target_url,
        message_key=config.message_key,
        reply_key=config.reply_key,
        actions_key=config.actions_key,
    ), None


def cmd_run(args) -> int:
    config = load(args.config)
    if args.tools:
        config.tools = [t.strip() for t in args.tools.split(",") if t.strip()]
    if args.fail_on:
        config.fail_on = [Severity.parse(s) for s in args.fail_on.split(",")]
    if args.repeat:
        config.repeat = max(1, args.repeat)
    if args.min_repro:
        config.min_repro = max(1, args.min_repro)
    if config.min_repro > config.repeat:
        config.min_repro = config.repeat

    target, ctx = _resolve_target(args, config)
    try:
        result = _run_gate(config, target, args, commands_used=config.tools)
    finally:
        if ctx is not None:
            ctx.__exit__(None, None, None)

    out_dir = Path(args.out or Path(config.baseline_path).parent / "runs" / result["run_id"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "findings.json").write_text(as_json(result), encoding="utf-8")
    (out_dir / "comment.md").write_text(markdown(result) + "\n", encoding="utf-8")
    (out_dir / "results.sarif").write_text(json.dumps(sarif(result, tool_version=__version__), indent=2) + "\n", encoding="utf-8")

    if args.update_baseline:
        if not result["verdict"]["baseline_safe"] and not args.force_baseline:
            print("baseline NOT updated:")
            if result["verdict"]["status"] == "error":
                print("  no engine ran, so there is nothing to record.")
            if result["tools_skipped"]:
                print(
                    "  these configured tools did not run: "
                    + ", ".join(result["tools_skipped"])
                )
                print("  a missing engine looks exactly like a fixed finding.")
            if result["attacks_run"] == 0:
                print("  no attack ran, so there is nothing to record.")
            print("  fix the environment, narrow `tools:` in gatecheck.yml to what is")
            print("  installed, or pass --force-baseline if you mean it.")
            if result["verdict"]["status"] == "blocked":
                print("  (a blocked run is fine to record: known findings are accepted,")
                print("   that is how you adopt the gate on a codebase that already fails)")
        else:
            baseline = Baseline.load(config.baseline_path)
            baseline.save(result["all_findings"])
            print(
                f"baseline updated: {config.baseline_path} "
                f"({len(result['all_findings'])} findings, {result['attacks_run']} attacks)"
            )
            if result["verdict"]["status"] == "blocked":
                print("  note: this run is BLOCKED. Those findings are now the accepted")
                print("  state and will not fail the gate again unless they get worse.")

    if config.repeat > 1:
        print(
            f"each attack ran {config.repeat} times; "
            f"findings block at {config.min_repro} reproduction(s)",
            file=sys.stderr,
        )
    print(markdown(result))
    print()
    print(f"artifacts: {out_dir}")
    return {"pass": 0, "blocked": 2}.get(result["verdict"]["status"], 3)


def _run_gate(config: Config, target, args, *, commands_used: list[str]) -> dict:
    run_id = _now_id()
    results = []
    for name in config.tools:
        cls = ENGINES.get(name)
        if cls is None:
            results.append({"tool": name, "skipped": f"unknown tool {name!r}"})
            continue
        engine = cls()
        ok, reason = engine.available()
        if not ok:
            results.append({"tool": name, "skipped": reason})
            continue
        results.append(engine.run(target, engine.plan(), config.severity_for, repeat=config.repeat))

    all_findings = dedupe([f for r in results if hasattr(r, "findings") for f in r.findings])
    baseline = Baseline.load(config.baseline_path)
    delta = baseline.compare(all_findings)

    accepted = baseline.accepted_ids()
    def _blocks(finding) -> bool:
        return (
            config.fails_gate(finding.severity)
            and finding.id not in accepted
            and finding.hits >= config.min_repro
        )

    blocking = [f for f in delta["new"] if _blocks(f)]
    blocking += [w["finding"] for w in delta["worse"] if _blocks(w["finding"])]

    tools_skipped = {r["tool"]: r["skipped"] for r in results if isinstance(r, dict) and "skipped" in r}
    tools_run = [r.tool for r in results if hasattr(r, "findings")]

    if not tools_run:
        # No engine ran. Reporting PASS here would be the exact failure
        # this project exists to name: a green tick for a test that never
        # happened. The run is an error, not a pass.
        status = "error"
        ok = False
        reason = "no engine ran, so there is no result: " + "; ".join(
            f"{tool}: {why}" for tool, why in tools_skipped.items()
        )
    elif blocking:
        status = "blocked"
        ok = False
        worst = max(blocking, key=lambda f: f.severity.rank)
        reason = (
            f"{len(blocking)} new finding(s) at or above the gate threshold, "
            f"highest severity {worst.severity.value}"
        )
    else:
        status = "pass"
        ok = True
        reason = (
            f"no new finding at or above {', '.join(s.value for s in config.fail_on)}"
            if config.fail_on else "gate threshold empty"
        )

    errors = [f"{r.tool}: {e}" for r in results if hasattr(r, "errors") for e in r.errors]

    # A partial run cannot rewrite the baseline: a missing engine looks
    # exactly like a fixed finding, and accepting it would launder
    # unexercised coverage into a clean record. Recording known findings
    # is allowed even when the gate blocks, because adopting the gate on
    # a codebase that already has problems is the normal first day.
    attacks = sum(getattr(r, "attacks_run", 0) for r in results if hasattr(r, "attacks_run"))
    baseline_safe = not tools_skipped and status != "error" and attacks > 0

    return {
        "run_id": run_id,
        "gatecheck_version": __version__,
        "target": getattr(target, "endpoint", str(target)),
        "started_at": run_id,
        "tools_run": tools_run,
        "tools_skipped": tools_skipped,
        "tool_detail": [
            {
                "tool": r.tool,
                "version": r.version,
                "attacks": r.attacks_run,
                "findings": len(r.findings),
                "duration_ms": r.duration_ms,
                "errors": r.errors,
            }
            for r in results
            if hasattr(r, "findings")
        ],
        "all_findings": all_findings,
        "new": delta["new"],
        "worse": delta["worse"],
        "unchanged": delta["unchanged"],
        "fixed": delta["fixed"],
        "errors": errors,
        "baseline_used": str(config.baseline_path) if baseline.findings else "",
        "verdict": {"ok": ok, "status": status, "reason": reason, "baseline_safe": baseline_safe},
        "attacks_run": attacks,
        "repeat": config.repeat,
        "min_repro": config.min_repro,
        "summary": {
            "total": len(all_findings),
            "new": len(delta["new"]),
            "fixed": len(delta["fixed"]),
            "unchanged": len(delta["unchanged"]),
            "worse": len(delta["worse"]),
            "blocking": len(blocking),
        },
    }


def cmd_accept(args) -> int:
    config = load(args.config)
    baseline = Baseline.load(config.baseline_path)
    if not baseline.accept(args.finding_id, args.reason or ""):
        print(f"no finding with id {args.finding_id!r} in {config.baseline_path}")
        return 1
    print(f"accepted {args.finding_id}")
    return 0


def cmd_report(args) -> int:
    run_dir = Path(args.run_dir)
    data = json.loads((run_dir / "findings.json").read_text(encoding="utf-8"))
    if args.format == "markdown":
        print(markdown(_rehydrate(data)))
    elif args.format == "sarif":
        print(json.dumps(sarif(_rehydrate(data)), indent=2))
    else:
        print((run_dir / "findings.json").read_text(encoding="utf-8"))
    return 0


def _rehydrate(data: dict) -> dict:
    """Reload a stored run for rendering (findings come back as dicts)."""
    from .models import Evidence, Finding

    def to_finding(d: dict) -> Finding:
        return Finding(
            category=d["category"],
            severity=Severity.parse(d["severity"]),
            title=d["title"],
            evidence=Evidence(**d["evidence"]),
            found_by=d.get("found_by", []),
            attack_id=d.get("attack_id", ""),
            turns=d.get("turns", 1),
            first_seen=d.get("first_seen", ""),
            last_seen=d.get("last_seen", ""),
        )

    data["all_findings"] = [to_finding(d) for d in data["all_findings"]]
    data["new"] = [to_finding(d) for d in data["new"]]
    data["worse"] = [{"finding": to_finding(d["finding"]), "was": Severity.parse(d["was"])} for d in data["worse"]]
    return data


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="gatecheck", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version", version=f"gatecheck {__version__}")
    sub = p.add_subparsers(dest="cmd", required=True)

    i = sub.add_parser("init", help="write gatecheck.yml")
    i.add_argument("--config", default="gatecheck.yml")
    i.add_argument("--baseline", default=".gatecheck/baseline.json")
    i.set_defaults(fn=cmd_init)

    r = sub.add_parser("run", help="run the gate")
    r.add_argument("--config", default="gatecheck.yml")
    r.add_argument("--url", default=None)
    r.add_argument("--demo", choices=["vulnerable", "fixed"], default=None)
    r.add_argument("--tools", default=None, help="comma list: deepteam,pyrit,promptfoo")
    r.add_argument("--fail-on", default=None, help="comma list of severities")
    r.add_argument("--repeat", type=int, default=None,
                   help="run each attack N times and record how often it reproduced")
    r.add_argument("--min-repro", type=int, default=None,
                   help="only block when a finding reproduced at least this many times")
    r.add_argument("--out", default=None)
    r.add_argument("--update-baseline", action="store_true")
    r.add_argument("--force-baseline", action="store_true",
                   help="update the baseline even if the run is incomplete")
    r.set_defaults(fn=cmd_run)

    a = sub.add_parser("accept", help="accept a finding, with a reason")
    a.add_argument("finding_id")
    a.add_argument("--reason", "-r", default="")
    a.add_argument("--config", default="gatecheck.yml")
    a.set_defaults(fn=cmd_accept)

    rp = sub.add_parser("report", help="re-render a stored run")
    rp.add_argument("run_dir")
    rp.add_argument("--format", choices=["markdown", "sarif", "json"], default="markdown")
    rp.set_defaults(fn=cmd_report)

    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
