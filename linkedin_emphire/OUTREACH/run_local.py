#!/usr/bin/env python3
"""One command that runs the evidence package end to end on a local machine.

Finds the endpoint, finds the model, checks the one dependency, runs the five tests, and fills the
package. Windows, macOS and Linux, same command.

    python linkedin_emphire/OUTREACH/run_local.py

Override anything it guesses:

    python linkedin_emphire/OUTREACH/run_local.py --base-url http://localhost:1234/v1 --model qwen2.5-7b

If nothing answers, it says exactly what to start and stops without touching the package.
"""

import argparse
import json
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILDER = HERE / "build_evidence_package.py"
PACKAGE = HERE / "2026-11-01_andrey_evidence_package.md"

# Ports that an OpenAI-compatible server commonly sits on, with how to start each one.
CANDIDATES = [
    ("http://localhost:11434/v1", "Ollama", "ollama serve"),
    ("http://localhost:1234/v1", "LM Studio", "Developer tab, then Start Server"),
    ("http://localhost:8080/v1", "llama.cpp or vLLM", "start the server"),
    ("http://localhost:8000/v1", "vLLM", "start the server"),
]


def say(msg=""):
    print(msg, flush=True)


def step(n, total, text):
    say("")
    say("[%d/%d] %s" % (n, total, text))


def probe(base_url, key=None, timeout=6):
    """Return (model ids, note). Ids is None when nothing answered at all."""
    url = base_url.rstrip("/") + "/models"
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + (key or "local")})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8", "replace"))
            ids = [m.get("id") for m in data.get("data", []) if m.get("id")]
            return ids, None
    except urllib.error.HTTPError as exc:
        if exc.code in (401, 403):
            return [], "HTTP %d, key rejected. Check the key, or that it is the right provider." % exc.code
        if exc.code < 500:
            return [], "HTTP %d from %s" % (exc.code, url)
        return None, "HTTP %d from %s" % (exc.code, url)
    except Exception as exc:
        return None, exc.__class__.__name__


def have_package():
    try:
        import openai  # noqa: F401
        return True
    except ImportError:
        return False


def install_package():
    say("    installing openai for %s" % sys.executable)
    proc = subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "openai>=1.0"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        say("    pip failed. Run this yourself and try again:")
        say("      %s -m pip install openai" % sys.executable)
        say(proc.stderr.strip()[-800:])
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", help="skip discovery and use this endpoint")
    ap.add_argument("--model", help="skip model selection")
    ap.add_argument("--api-key", help="key for a hosted endpoint")
    ap.add_argument("--package", default=str(PACKAGE))
    ap.add_argument("--yes", action="store_true", help="do not ask before spending the run")
    args = ap.parse_args()

    log_path = HERE / ("run_%s.log" % datetime.now().strftime("%Y%m%d_%H%M%S"))
    log_lines = []

    def log(msg):
        log_lines.append(msg)
        say(msg)

    say("=" * 62)
    say("evidence package, end to end")
    say("=" * 62)
    log("python      %s" % sys.version.split()[0])
    log("interpreter %s" % sys.executable)
    log("package     %s" % args.package)

    if not Path(args.package).exists():
        say("no package at %s" % args.package)
        return 1

    # 1. dependency
    step(1, 4, "checking the openai package")
    if have_package():
        import openai
        log("    openai %s present" % getattr(openai, "__version__", "?"))
    else:
        if not install_package():
            return 1
        if not have_package():
            say("    still not importable after install. Different interpreter?")
            return 1
        log("    openai installed")

    # 2. endpoint
    step(2, 4, "looking for an endpoint")
    found = None
    tried = []
    if args.base_url:
        ids, note = probe(args.base_url, args.api_key)
        if note:
            say("    %s" % note)
        if ids is None:
            say("    nothing answered at %s" % (args.base_url.rstrip("/") + "/models"))
            return 1
        found = (args.base_url, ids)
    else:
        for url, name, how in CANDIDATES:
            tried.append("%s (%s)" % (url, name))
            ids, note = probe(url, args.api_key)
            if ids is not None:
                say("    found %s at %s" % (name, url))
                found = (url, ids)
                break
            say("    nothing at %s" % url)

    if not found:
        say("")
        say("No endpoint answered. Start one, then run this again:")
        say("")
        say("  Ollama      ollama serve")
        say("              ollama pull llama3.1:8b")
        say("")
        say("  LM Studio   load a model, Developer tab, Start Server (port 1234)")
        say("")
        say("  Hosted      --base-url https://api.groq.com/openai/v1 --api-key <key>")
        say("")
        say("Tried: " + ", ".join(tried))
        return 1

    base_url, model_ids = found
    log("    endpoint %s" % base_url)
    log("    models   %s" % (", ".join(model_ids) if model_ids else "(endpoint returned none)"))

    # 3. model
    step(3, 4, "choosing the model")
    model = args.model
    if not model:
        if not model_ids:
            say("    the endpoint listed no models. Load one, or pass --model")
            return 1
        model = model_ids[0]
        if len(model_ids) > 1 and sys.stdin.isatty():
            say("    available: " + ", ".join(model_ids))
            pick = input("    model to test [%s]: " % model).strip()
            if pick:
                model = pick
    if model not in model_ids and model_ids:
        say("    warning: %r is not in the endpoint's model list. Continuing anyway." % model)
    log("    model    %s" % model)

    # 4. run
    step(4, 4, "running the five tests")
    if not args.yes and sys.stdin.isatty():
        go = input("    run 14+ model calls against %s now? [Y/n]: " % model).strip().lower()
        if go in ("n", "no"):
            say("    stopped before the run. Nothing changed.")
            return 1

    cmd = [sys.executable, str(BUILDER), "--model", model, "--base-url", base_url,
           "--package", args.package]
    if args.api_key:
        cmd += ["--api-key", args.api_key]
    log("    " + " ".join(cmd))
    proc = subprocess.run(cmd, text=True)
    log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    say("")
    if proc.returncode != 0:
        say("The run did not complete. The package is unchanged.")
        say("Send %s if you need a second pair of eyes." % log_path.name)
        return proc.returncode

    say("=" * 62)
    say("done. The package now holds this run.")
    say("=" * 62)
    say("")
    say("Next, and this cannot be skipped:")
    say("  1. Open the package, section 4")
    say("  2. Beside every FLAGGED response, write confirmed or false positive, in your words")
    say("  3. Send it with reply A from the applications file")
    say("")
    say("Log: %s" % log_path.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
