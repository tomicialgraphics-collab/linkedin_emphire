"""Serve the PydanticAI claims agent on the gate's contract.

    $env:GROQ_API_KEY = "gsk_..."
    pip install "pydantic-ai-slim[openai]"
    python -m pydantic_target.serve --mode vulnerable      # terminal 1
    python -m gatecheck run --config gatecheck.pydantic.yml  # terminal 2

--fake answers from a script, so the wiring can be checked with no key and
no network.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # the runtime import stays inside main(), so --help works without it
    from .agent import ClaimsRunner

MISSING = (
    'PydanticAI is not installed. Run:\n'
    '    pip install "pydantic-ai-slim[openai]"\n'
    "or pip install -e \".[pydantic]\" from a checkout."
)


def scripted_model():
    """A model that sends one email and then stops, for the wiring test."""
    from pydantic_ai.messages import ModelResponse, TextPart, ToolCallPart
    from pydantic_ai.models.function import FunctionModel

    calls = {"n": 0}

    def handler(messages, info):
        calls["n"] += 1
        if calls["n"] % 2 == 1:
            return ModelResponse(
                [
                    ToolCallPart(
                        "send_email",
                        {"to": "audit-team@example.net", "subject": "customer table", "body": "attached"},
                    )
                ]
            )
        return ModelResponse([TextPart("Sent the customer table.")])

    return FunctionModel(handler)


def make_handler(runner: ClaimsRunner, quiet: bool = False):
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, fmt: str, *args) -> None:
            return

        def _send(self, status: int, payload: dict) -> None:
            body = json.dumps(payload).encode("utf-8")
            self.send_response(status)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):  # noqa: N802
            if self.path.rstrip("/") in ("/health", ""):
                self._send(200, {"ok": True, "mode": runner.mode, "runtime": "pydantic-ai"})
                return
            self._send(404, {"error": "unknown path"})

        def do_POST(self):  # noqa: N802
            length = int(self.headers.get("content-length") or 0)
            raw = self.rfile.read(length) if length else b"{}"
            try:
                message = json.loads(raw.decode("utf-8")).get("message", "")
            except ValueError:
                self._send(400, {"error": "body must be JSON with a message field"})
                return

            session = self.headers.get("x-session", "")
            started = time.perf_counter()
            try:
                reply, actions = runner.reply(message, session)
            except Exception as e:  # a model or runtime failure is not an answer
                self._send(502, {"error": f"{type(e).__name__}: {e}"})
                return

            elapsed = (time.perf_counter() - started) * 1000
            if not quiet:
                preview = message.replace("\n", " ")[:58]
                print(
                    f"[{session or '-'}] {elapsed:6.0f}ms  {len(actions)} action(s)  {preview}",
                    file=sys.stderr,
                    flush=True,
                )
            self._send(200, {"reply": reply, "actions": actions})

    return Handler


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Serve the PydanticAI claims agent for gatecheck.")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8100)
    parser.add_argument("--mode", default="vulnerable", choices=["vulnerable", "guarded"])
    parser.add_argument("--model", default=os.environ.get("GATECHECK_PYDANTIC_MODEL", "openai/gpt-oss-120b"))
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--fake", action="store_true", help="no key, no network: scripted answers")
    parser.add_argument("--prompt-only", action="store_true",
                        help="guarded prompt without the refusing tools")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    try:
        from .agent import ClaimsRunner, groq_model

        model = scripted_model() if args.fake else groq_model(args.model, temperature=args.temperature)
    except ImportError:
        print(MISSING, file=sys.stderr)
        return 2
    except RuntimeError as e:  # no key, or a model name the provider does not serve
        print(str(e), file=sys.stderr)
        return 2

    enforce = False if args.prompt_only else None
    runner = ClaimsRunner(model, mode=args.mode, enforce=enforce)
    server = ThreadingHTTPServer((args.host, args.port), make_handler(runner, args.quiet))
    label = "scripted" if args.fake else args.model
    enforced = "prompt only" if not runner.enforce else "prompt + refusing tools"
    print(f"claims agent (pydantic-ai) up on http://{args.host}:{args.port}/chat")
    print(f"mode: {args.mode} | model: {label} | temperature: {args.temperature}")
    print(f"guardrails: {enforced}")
    print("point gatecheck at it with: python -m gatecheck run --config gatecheck.pydantic.yml")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
