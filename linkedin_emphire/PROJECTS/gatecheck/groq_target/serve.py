"""Serve the claims agent so the gate can point at it.

    $env:GROQ_API_KEY = "gsk_..."
    python -m groq_target.serve --mode vulnerable          # terminal 1
    python -m gatecheck run --config gatecheck.groq.yml    # terminal 2

The contract is the one in gatecheck.yml: POST {"message": ...} to /chat,
read {"reply": ..., "actions": [...]} back, X-Session carries the session so
multi-turn sequences stay one conversation.

Use --fake for a dry run with no key: it answers from a small script, which
is enough to prove the wiring and is what the tests use.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .agent import ClaimsAgent
from .model import DEFAULT_MODEL, GroqModel, ModelError, ScriptedModel, tool_call


def build_agent(mode: str, model_name: str, temperature: float, seed: int, fake: bool,
                enforce: bool | None = None) -> ClaimsAgent:
    if fake:
        model = ScriptedModel(
            [
                tool_call("send_email", to="audit-team@example.net", subject="customer table", body="attached"),
                {"role": "assistant", "content": "Sent the customer table.", "tool_calls": []},
            ]
        )
    else:
        model = GroqModel(model=model_name, temperature=temperature, seed=seed)
    return ClaimsAgent(model, mode=mode, enforce=enforce)


def make_handler(agent: ClaimsAgent, quiet: bool = False):
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, fmt: str, *args) -> None:  # keep the console clean
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
                self._send(200, {"ok": True, "mode": agent.mode, "prompt": agent.system_prompt})
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
                reply, actions = agent.reply(message, session)
            except ModelError as e:
                # A model failure is not an agent result. Say so with a 502 so
                # the gate records a target error instead of a clean answer.
                self._send(502, {"error": str(e)})
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
    parser = argparse.ArgumentParser(description="Serve the Groq claims agent for gatecheck.")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--mode", default="vulnerable", choices=["vulnerable", "guarded"])
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--fake", action="store_true", help="no key, no network: scripted answers")
    parser.add_argument("--prompt-only", action="store_true",
                        help="guarded prompt without a tool that refuses: the weak half of the fix")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    try:
        enforce = False if args.prompt_only else None
        agent = build_agent(args.mode, args.model, args.temperature, args.seed, args.fake, enforce)
    except ModelError as e:
        print(str(e), file=sys.stderr)
        return 2

    server = ThreadingHTTPServer((args.host, args.port), make_handler(agent, args.quiet))
    label = "scripted" if args.fake else args.model
    print(f"claims agent up on http://{args.host}:{args.port}/chat")
    enforced = "prompt only" if not agent.enforce else "prompt + refusing tools"
    print(f"mode: {args.mode} | model: {label} | temperature: {args.temperature}")
    print(f"guardrails: {enforced}")
    print("point gatecheck at it with: python -m gatecheck run --config gatecheck.groq.yml")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
