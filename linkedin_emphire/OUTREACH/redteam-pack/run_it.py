#!/usr/bin/env python3
"""One command that runs the evidence package end to end on a local machine.

Finds the endpoint, finds the model, checks the one dependency, runs the five tests, and fills the
package. Windows, macOS and Linux, same command.

    python run_it.py

Override anything it guesses:

    python run_it.py --base-url http://localhost:1234/v1 --model qwen2.5-7b

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
BUILDER = HERE / "build_package.py"
PACKAGE = HERE / "package.md"

# Ports that an OpenAI-compatible server commonly sits on, with how to start each one.
UA = "OpenAI/Python 3.x (redteam-pack)"

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
    """Return (model ids, note). Ids is None when nothing answered at all.

    A hosted endpoint rejects a placeholder key, so the real key has to travel with the probe.
    Sending "local" to api.groq.com gets a 401 and an empty model list, which used to look like an
    endpoint with no models loaded.
    """
    url = base_url.rstrip("/") + "/models"
    req = urllib.request.Request(url, headers={
        "Authorization": "Bearer " + (key or "local"),
        "User-Agent": UA,
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8", "replace"))
            ids = [m.get("id") for m in data.get("data", []) if m.get("id")]
            return ids, None
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode("utf-8", "replace").strip().replace("\n", " ")[:180]
        except Exception:
            pass
        if exc.code == 401:
            return [], "HTTP 401, key not accepted. %s" % detail
        if exc.code == 403:
            return [], "HTTP 403, key accepted but the request is forbidden. %s" % detail
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




def tidy_key(key, base_url=""):
    """Strip what a paste picks up, and undo a doubled paste. Return (key, notes)."""
    notes = []
    key = (key or "").strip()
    if key.lower().startswith("bearer "):
        key = key[7:].strip()
        notes.append("removed the word Bearer from the front")
    if len(key) >= 2 and key[0] == key[-1] and key[0] in "\"'":
        key = key[1:-1].strip()
        notes.append("removed the quote marks around it")
    if any(c in key for c in " \t\r\n"):
        notes.append("it still contains a space, which no key should")

    expect = None
    if "groq.com" in base_url:
        expect = 56
    elif "googleapis.com" in base_url:
        expect = 39
    if expect and len(key) == 2 * expect and key[:expect] == key[expect:]:
        key = key[:expect]
        notes.append("the same key arrived twice in a row, so only the first copy was kept")
    elif expect and len(key) != expect:
        notes.append(
            "a key for this endpoint is %d characters and this is %d, so something extra or "
            "something missing came with the paste" % (expect, len(key))
        )
    return key, notes


def check(base_url, model, key):
    """Make the two calls that matter and print exactly what came back. Changes nothing."""
    import getpass

    if not base_url:
        base_url = "https://api.groq.com/openai/v1"
    if not key:
        say("")
        say("Paste the key at the prompt. It will not be echoed and it is not written anywhere.")
        try:
            key = getpass.getpass("key: ")
        except Exception:
            key = input("key: ")
    key, notes = tidy_key(key, base_url)
    for n in notes:
        say("key note: %s" % n)
    base = base_url.rstrip("/")
    headers = {
        "Authorization": "Bearer " + key,
        "User-Agent": UA,
        "Accept": "application/json",
    }

    say("")
    say("=" * 62)
    say("checking one endpoint")
    say("=" * 62)
    say("endpoint  %s" % base)
    say("key       %d characters, starts with %s" % (len(key), (key[:4] or "(empty)")))
    if not key:
        say("")
        say("no key reached the script. Nothing below will work.")
        return 1

    def call(url, payload=None, timeout=45):
        """Return (status, body text). Status 0 means the connection itself failed."""
        data = None
        hdrs = dict(headers)
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
            hdrs["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, headers=hdrs, method="POST" if data else "GET")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            try:
                return exc.code, exc.read().decode("utf-8", "replace")
            except Exception:
                return exc.code, "(no body)"
        except Exception as exc:
            return 0, "%s: %s" % (exc.__class__.__name__, exc)

    say("")
    say("[1] GET %s/models" % base)
    status, body = call(base + "/models")
    say("    %s" % (("no connection, " + body) if status == 0 else "HTTP %d" % status))
    say("    %s" % (body.strip().replace("\n", " ")[:300] or "(empty body)"))

    ids = []
    if status == 200:
        try:
            ids = [m.get("id") for m in json.loads(body).get("data", []) if m.get("id")]
        except Exception:
            pass
    chat = [i for i in ids if not any(t in i.lower() for t in ("whisper", "tts", "guard", "embed"))]
    if ids:
        say("    %d models. chat models: %s" % (len(ids), ", ".join(chat[:6]) or "none obvious"))

    pick = model or (chat[0] if chat else "llama-3.3-70b-versatile")
    say("")
    say("[2] POST %s/chat/completions  model=%s  max_tokens=1" % (base, pick))
    status2, body2 = call(
        base + "/chat/completions",
        {"model": pick, "messages": [{"role": "user", "content": "hi"}], "max_tokens": 1},
    )
    say("    %s" % (("no connection, " + body2) if status2 == 0 else "HTTP %d" % status2))
    say("    %s" % (body2.strip().replace("\n", " ")[:300] or "(empty body)"))

    say("")
    say("-" * 62)
    if status2 == 200:
        say("READ: this key can generate with %s at this endpoint." % pick)
        say("")
        say("Next:")
        say("  python run_it.py --base-url %s --model %s" % (base, pick))
        say("It will ask for the key once, without echoing it.")
        return 0
    if status2 == 0:
        say("READ: nothing answered at this endpoint, so the key was never even seen.")
        say("      The base URL must end in /v1. If it does, the server, or the network, is down.")
        return 1
    if status2 == 401:
        say("READ: the key string is not accepted. Copy it again from the console,")
        say("      straight into the prompt, with no spaces before or after.")
        return 1
    if status2 == 403:
        say("READ: the key is real and the request is still refused. That is not a typo.")
        say("      Either the account is not entitled to %s, or this network is blocked." % pick)
        say("      A different model id is worth one try. If that also gives 403, change provider:")
        say("")
        say("  python run_it.py --base-url https://generativelanguage.googleapis.com/v1beta/openai/ --model gemini-2.5-flash")
        return 1
    if status2 == 404:
        say("READ: no model called %s at this endpoint. Use one of the chat models listed above." % pick)
        return 1
    if status2 == 429:
        say("READ: rate limited. The key works. Wait a minute and run it again.")
        return 1
    say("READ: unexpected answer. Send the two lines above to whoever asked you to run this.")
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", help="skip discovery and use this endpoint")
    ap.add_argument("--model", help="skip model selection")
    ap.add_argument("--api-key", help="key for a hosted endpoint")
    ap.add_argument("--package", default=str(PACKAGE))
    ap.add_argument("--yes", action="store_true", help="do not ask before spending the run")
    ap.add_argument(
        "--check",
        action="store_true",
        help="make two test calls and report what came back, then stop. Nothing is changed.",
    )
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

    if args.check:
        return check(args.base_url, args.model, args.api_key)

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
    remote = bool(args.base_url) and not any(
        h in args.base_url for h in ("localhost", "127.0.0.1", "0.0.0.0", "::1")
    )
    if remote and not args.api_key:
        import getpass

        say("")
        say("    This endpoint needs a key. It is not echoed and not written to the log.")
        try:
            args.api_key = getpass.getpass("    key: ")
        except Exception:
            args.api_key = input("    key: ")
        args.api_key, notes = tidy_key(args.api_key, args.base_url)
        for n in notes:
            say("    key note: %s" % n)
        if not args.api_key:
            say("    no key reached the script. Stopping before the run.")
            return 1

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
            say("    the endpoint listed no models. Pass --model with a chat model id.")
            say("    common ones: llama-3.3-70b-versatile (Groq), gemini-2.5-flash (Google)")
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
    shown = ["<key>" if args.api_key and c == args.api_key else c for c in cmd]
    log("    " + " ".join(shown))
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
    say("  3. Send it, with a line saying the run is attached (replies.md has both versions)")
    say("")
    say("Log: %s" % log_path.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
