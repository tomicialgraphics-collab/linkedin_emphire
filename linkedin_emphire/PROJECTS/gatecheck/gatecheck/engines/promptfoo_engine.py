"""promptfoo engine: the assertion layer, and the CI-native one.

promptfoo is in this gate for two reasons. It already speaks HTTP
targets and assertions, so a team that uses it can keep its config. And
it returns a machine-readable result with an exit code, which is what a
gate needs to be checkable rather than advisory.

The gate reads promptfoo's own pass/fail per case and also keeps the raw
response, so a promptfoo failure and a gate finding can be compared
rather than trusted.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from ..corpus import SINGLE_TURN, Case
from .base import Engine


class PromptfooEngine(Engine):
    name = "promptfoo"
    label = "promptfoo"

    def available(self) -> tuple[bool, str]:
        if shutil.which("promptfoo") is None:
            return False, "promptfoo not on PATH (npm install -g promptfoo)"
        return True, ""

    def version(self) -> str:
        try:
            out = subprocess.run(["promptfoo", "--version"], capture_output=True, text=True, timeout=60)
            return (out.stdout or out.stderr or "unknown").strip().splitlines()[-1]
        except Exception:
            return "unknown"

    def plan(self) -> list[Case]:
        return list(SINGLE_TURN)

    def run(self, target, cases, severity_for):
        started = time.perf_counter()
        workdir = Path(tempfile.mkdtemp(prefix="gatecheck-pf-"))
        try:
            result = self._run_in(workdir, target, cases, severity_for)
        finally:
            shutil.rmtree(workdir, ignore_errors=True)
        result.duration_ms = int((time.perf_counter() - started) * 1000)
        return result

    def _run_in(self, workdir: Path, target, cases, severity_for):
        from ..detectors import detect
        from ..models import Evidence, Finding
        from .base import EngineResult, _title, now

        root = str(Path(__file__).resolve().parents[2])
        (workdir / "assert_gatecheck.py").write_text(
            "import sys\n"
            f"sys.path.insert(0, {root!r})\n"
            "from gatecheck.detectors import detect\n\n\n"
            "def get_assert(output, context):\n"
            "    category = detect(output)\n"
            "    return {\"pass\": category is None, \"score\": 0 if category else 1,\n"
            "            \"reason\": category or 'held'}\n",
            encoding="utf-8",
        )

        lines = [
            "description: gatecheck (generated)",
            "prompts:",
            '  - "{{prompt}}"',
            "providers:",
            "  - id: http",
            "    config:",
            f"      url: {target.endpoint}",
            "      method: POST",
            "      headers:",
            '        content-type: "application/json"',
            '      body: \'{"message": "{{prompt}}"}\'',
            '      transformResponse: "json.reply"',
            "tests:",
        ]
        for case in cases:
            lines += [
                "  - vars:",
                f"      case_id: {json.dumps(case.attack_id)}",
                f"      prompt: {json.dumps(case.prompts[0])}",
                "    assert:",
                "      - type: python",
                "        value: file://assert_gatecheck.py",
            ]
        (workdir / "promptfooconfig.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")

        env = dict(os.environ)
        env.update({"PROMPTFOO_DISABLE_TELEMETRY": "1", "PROMPTFOO_DISABLE_UPDATE": "1", "NO_COLOR": "1"})
        proc = subprocess.run(
            ["promptfoo", "eval", "-c", "promptfooconfig.yaml", "-o", "out.json",
             "--no-cache", "--max-concurrency", "1", "--no-progress-bar"],
            cwd=str(workdir), capture_output=True, text=True, timeout=1200, env=env,
        )
        result = EngineResult(tool=self.name, version=self.version())
        out_json = workdir / "out.json"
        if not out_json.exists():
            result.errors.append(
                "promptfoo produced no result file: "
                + " / ".join((proc.stderr or "").strip().splitlines()[-2:])
            )
            return result

        rows = json.loads(out_json.read_text(encoding="utf-8")).get("results", {}).get("results", [])
        by_case = {(r.get("vars") or {}).get("case_id"): r for r in rows}
        for case in cases:
            row = by_case.get(case.attack_id)
            if row is None:
                result.errors.append(f"{case.attack_id}: promptfoo returned no row")
                continue
            result.attacks_run += 1
            output = (row.get("response") or {}).get("output") or ""
            category = detect(output)
            if category is None:
                continue
            result.findings.append(
                Finding(
                    category=category,
                    severity=severity_for(category),
                    title=_title(category, case),
                    evidence=Evidence(prompt=case.prompts[0], response=output),
                    found_by=[self.name],
                    attack_id=case.attack_id,
                    turns=1,
                    first_seen=now(),
                    last_seen=now(),
                )
            )
        return result
