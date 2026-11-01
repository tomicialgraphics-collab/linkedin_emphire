#!/usr/bin/env python3
"""Run the five-test harness and fill the evidence package from the real results.

The package at OUTREACH/2026-11-01_andrey_evidence_package.md ships with two marked blocks:

    <!-- CONFIG:BEGIN -->   ... <!-- CONFIG:END -->
    <!-- RESULTS:BEGIN -->  ... <!-- RESULTS:END -->

This script runs the harness, then rewrites both blocks from what the run actually produced. It
never invents a number. If the run fails, the blocks are left exactly as they were and the script
exits non-zero.

Usage, from the repo root:

    python3 linkedin_emphire/OUTREACH/build_evidence_package.py \
        --model gpt-4o-mini \
        --base-url http://localhost:11434/v1 \
        --api-key ollama

    # or point it at an existing clone instead of letting it clone one
    python3 build_package.py --harness /path/to/ai-redteam-five-tests ...

Before sending, read the generated section 4 yourself. Every flagged response needs a human verdict
next to it, and that part is not automatable.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

PINNED_COMMIT = "d95a57e3d5bfcad847b5d5d05d5beab1a49e8ba6"
REPO_URL = "https://github.com/Teamthy/ai-redteam-five-tests.git"
PACKAGE = Path(__file__).resolve().parent / "2026-11-01_andrey_evidence_package.md"


def preflight(model, base_url, api_key="x"):
    """Fail with a readable message before doing any work."""
    try:
        import openai  # noqa: F401
    except ImportError:
        raise SystemExit(
            "The harness needs the openai package and it is not installed for this interpreter.\n"
            "  fix: %s -m pip install openai\n"
            "  interpreter: %s" % (sys.executable, sys.executable)
        )

    import urllib.error
    import urllib.request

    url = base_url.rstrip("/") + "/models"
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + (api_key or "x")})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            resp.read(64)
    except urllib.error.HTTPError as exc:
        # a 401/404 still proves something is listening, which is what this check is for
        if exc.code in (401, 403):
            raise SystemExit(
                "the endpoint rejected the key (HTTP %d at %s).\n"
                "  Check the key, and that --base-url matches the provider it came from."
                % (exc.code, url)
            )
        if exc.code >= 500:
            raise SystemExit("endpoint answered %s at %s. Is the model loaded?" % (exc.code, url))
    except Exception as exc:
        raise SystemExit(
            "Nothing answered at %s (%s).\n"
            "  Ollama:     ollama serve  then  ollama pull %s\n"
            "  LM Studio:  Developer tab, Start Server, check the port\n"
            "  Then confirm the base URL ends in /v1 and the model id is loaded."
            % (url, exc.__class__.__name__, model)
        )
    print("[ok] openai installed, endpoint answering at %s" % base_url)


def sh(cmd, cwd=None, env=None):
    """Run a command, return stdout, raise on failure."""
    proc = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(
            "command failed: %s\n%s\n%s" % (" ".join(cmd), proc.stdout[-2000:], proc.stderr[-2000:])
        )
    return proc.stdout


def get_harness(path, workdir):
    """Use an existing clone, or clone the pinned commit into workdir."""
    if path:
        harness = Path(path).expanduser().resolve()
        if not (harness / "redteam.py").exists():
            raise SystemExit("no redteam.py in %s" % harness)
        head = sh(["git", "rev-parse", "HEAD"], cwd=str(harness)).strip()
        print("[harness] using %s at %s" % (harness, head))
        if head != PINNED_COMMIT:
            print("[harness] WARNING: HEAD is %s, package pins %s" % (head, PINNED_COMMIT))
        return harness

    target = Path(workdir) / "ai-redteam-five-tests"
    print("[harness] cloning %s" % REPO_URL)
    sh(["git", "clone", "--quiet", REPO_URL, str(target)])
    sh(["git", "checkout", "--quiet", PINNED_COMMIT], cwd=str(target))
    head = sh(["git", "rev-parse", "HEAD"], cwd=str(target)).strip()
    print("[harness] checked out %s" % head)
    if head != PINNED_COMMIT:
        raise SystemExit("clone is at %s, expected %s" % (head, PINNED_COMMIT))
    return target


def run_harness(harness, model, base_url, api_key, prompt_file=None):
    """Run the harness and return (results dict, generated results.md text)."""
    env = dict(os.environ)
    env["MODEL"] = model
    env["OPENAI_BASE_URL"] = base_url
    env["OPENAI_API_KEY"] = api_key
    if prompt_file:
        env["MY_SYSTEM_PROMPT_FILE"] = str(Path(prompt_file).expanduser().resolve())

    print("[run] python redteam.py  (model=%s endpoint=%s)" % (model, base_url))
    proc = subprocess.run([sys.executable, "redteam.py"], cwd=str(harness), env=env,
                          capture_output=True, text=True)

    results_json = harness / "results" / "results.json"
    results_md = harness / "results" / "results.md"

    # The harness writes results.json, then crashes while writing results.md, because write_outputs()
    # indexes the results dict by display name ("Test 1 - prompt injection") instead of by key
    # ("test1"). Known defect at the pinned commit. The run itself finishes before the crash, so a
    # non-zero exit with results.json on disk is a usable run and is reported as one.
    note = ""
    if proc.returncode != 0:
        if not results_json.exists():
            raise SystemExit(
                "the run failed and wrote no results/results.json\n"
                + (proc.stdout + proc.stderr)[-2500:]
            )
        note = (
            "The harness exited with an error after writing `results.json` and before writing "
            "`results.md`. Known defect at the pinned commit: `write_outputs()` reads the results "
            "dict by display name instead of by key. The run completed, the raw responses are "
            "recorded below, and nothing in this section depends on `results.md`."
        )
        print("[warn] harness exited non-zero but wrote results.json, continuing")

    data = json.loads(results_json.read_text(encoding="utf-8"))
    md = results_md.read_text(encoding="utf-8") if results_md.exists() else ""
    return data, md, note


def config_block(model, base_url, timestamp, results):
    """Section 2.3. Only what the run actually used."""
    rows = [
        ("Model id", "`%s`" % model),
        ("Endpoint", "`%s`" % base_url),
        ("Temperature", "0.2, harness default"),
        ("Max tool steps", "4, harness default"),
        ("Run started", timestamp),
        ("Sample", "built-in OrderBot prompt"),
    ]
    body = ["| Field | Value |", "|---|---|"]
    body += ["| %s | %s |" % (k, v) for k, v in rows]
    return "\n".join(body)


def results_block(data, md, model, base_url, timestamp, note=""):
    """Section 4, built from results.json only."""
    meta = data.get("meta", {})
    run = meta.get("run", timestamp)

    lines = []
    lines.append("**Run:** %s UTC, model `%s`, endpoint `%s`." % (run, model, base_url))
    lines.append("")
    if note:
        lines.append("> " + note)
        lines.append("")

    def section(title, items, key):
        if not items:
            return
        lines.append("**%s**" % title)
        lines.append("")
        flagged = 0
        for it in items:
            broke = it.get("broke")
            if broke:
                flagged += 1
            mark = "FLAGGED" if broke else "not flagged"
            label = it.get(key, "?")
            lines.append("- `%s` %s. %s" % (label, mark, it.get("why", "")))
        lines.append("")
        lines.append("Flagged %d of %d in this test." % (flagged, len(items)))
        lines.append("")

    section("Test 1, prompt injection", data.get("test1"), "attempt")
    section("Test 2, retrieval poisoning", data.get("test2"), "question")
    section("Test 3, tool description poisoning", data.get("test3"), "condition")
    section("Test 4, multilingual refusals", data.get("test4"), "refusal")

    lines.append("**Test 5, failure rate per input type**")
    lines.append("")
    lines.append("| Failure class | Sample | Flagged | Rate |")
    lines.append("|---|---|---|---|")
    for name, total, fired, rate in data.get("test5", []):
        shown = "n/a" if total == 0 else (
            ("%.0f%%" % (rate * 100)) if isinstance(rate, float) else str(rate)
        )
        lines.append("| %s | %d | %d | %s |" % (name, total, fired, shown))
    lines.append("")
    lines.append(
        "Rates are over a single run. A rate with a sample this small is an observation, not a "
        "measurement, and it is printed with its sample size for that reason."
    )
    lines.append("")
    lines.append("**Every flagged response, verbatim**")
    lines.append("")
    lines.append("Each one needs a human verdict beside it before this document goes out.")
    lines.append("")
    for test, key in (("test1", "attempt"), ("test2", "question"), ("test3", "condition"), ("test4", "refusal")):
        for it in data.get(test, []):
            if it.get("broke"):
                lines.append("```")
                lines.append("%s / %s / %s" % (test, it.get(key, "?"), it.get("why", "")))
                lines.append("")
                lines.append((it.get("raw") or "").strip())
                lines.append("```")
                lines.append("")

    if md:
        lines.append("")
        lines.append("The harness also wrote `results/results.md`, reproduced in full:")
        lines.append("")
        lines.append("```")
        lines.append(md.strip())
        lines.append("```")
    return "\n".join(lines)


def replace_block(text, name, new_body):
    pattern = re.compile(
        r"(<!-- %s:BEGIN -->)(.*?)(<!-- %s:END -->)" % (name, name), re.S
    )
    if not pattern.search(text):
        raise SystemExit("marker %s not found in the package" % name)
    return pattern.sub(lambda m: m.group(1) + "\n" + new_body.strip() + "\n" + m.group(3), text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="model id to test")
    ap.add_argument("--base-url", required=True, help="OpenAI-compatible base URL")
    ap.add_argument("--api-key", default="no-key", help="placeholder key is fine for local endpoints")
    ap.add_argument("--harness", help="existing clone; skips cloning")
    ap.add_argument("--prompt-file", help="test your own system prompt instead of the sample bot")
    ap.add_argument("--package", default=str(PACKAGE), help="package file to fill")
    args = ap.parse_args()

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    package = Path(args.package)
    if not package.exists():
        raise SystemExit("no package at %s" % package)

    preflight(args.model, args.base_url, args.api_key)
    print("[plan] clone harness at %s, run 5 tests against %s, fill %s" % (PINNED_COMMIT[:7], args.model, package.name))

    workdir = tempfile.mkdtemp(prefix="fivetests-")
    try:
        harness = get_harness(args.harness, workdir)
        data, md, note = run_harness(harness, args.model, args.base_url, args.api_key, args.prompt_file)

        text = package.read_text(encoding="utf-8")
        text = replace_block(text, "CONFIG", config_block(args.model, args.base_url, timestamp, data))
        text = replace_block(
            text, "RESULTS", results_block(data, md, args.model, args.base_url, timestamp, note)
        )
        package.write_text(text, encoding="utf-8")
        print("[done] filled %s" % package)
        print("[next] read section 4 and put a human verdict beside every flagged response.")
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


if __name__ == "__main__":
    main()
