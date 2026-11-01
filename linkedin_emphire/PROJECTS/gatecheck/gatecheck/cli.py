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
        baseline = Baseline.load(config.baseline_path)
        baseline.save(result["all_findings"])
        print(f"baseline updated: {config.baseline_path} ({len(result['all_findings'])} findings)")

    print(markdown(result))
    print()
    print(f"artifacts: {out_dir}")
    return 0 if result["verdict"]["ok"] else 2


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
        results.append(engine.run(target, engine.plan(), config.severity_for))

    all_findings = dedupe([f for r in results if hasattr(r, "findings") for f in r.findings])
    baseline = Baseline.load(config.baseline_path)
    delta = baseline.compare(all_findings)

    accepted = baseline.accepted_ids()
    blocking = [f for f in delta["new"] if config.fails_gate(f.severity) and f.id not in accepted]
    blocking += [w["finding"] for w in delta["worse"]
                 if config.fails_gate(w["finding"].severity) and w["finding"].id not in accepted]

    if blocking:
        worst = max(blocking, key=lambda f: f.severity.rank)
        reason = (
            f"{len(blocking)} new finding(s) at or above the gate threshold, "
            f"highest severity {worst.severity.value}"
        )
    else:
        reason = (
            f"no new finding at or above {', '.join(s.value for s in config.fail_on)}"
            if config.fail_on else "gate threshold empty"
        )

    errors = [f"{r.tool}: {e}" for r in results if hasattr(r, "errors") for e in r.errors]
    tools_run = [r.tool for r in results if hasattr(r, "findings")]
    tools_skipped = {r["tool"]: r["skipped"] for r in results if isinstance(r, dict) and "skipped" in r}

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
        "verdict": {"ok": not blocking, "reason": reason},
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
    r.add_argument("--out", default=None)
    r.add_argument("--update-baseline", action="store_true")
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
