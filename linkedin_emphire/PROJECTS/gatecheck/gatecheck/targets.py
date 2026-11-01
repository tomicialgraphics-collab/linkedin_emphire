"""Targets: anything with an endpoint that takes a message and answers.

Two adapters cover the useful cases:
  HttpTarget     a URL, JSON in and JSON out (the demo agent, and any app)
  LocalTarget    a Python callable, for tests and for people who do not
                 want to run a server to try a gate

Both return a Reply, so an engine never needs to know which it is.
"""
from __future__ import annotations

import json
import threading
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


@dataclass
class Reply:
    text: str
    actions: list[str] = field(default_factory=list)
    status: int = 200

    @property
    def ok(self) -> bool:
        return self.status < 400


class TargetError(RuntimeError):
    pass


class HttpTarget:
    """POST {"message": ...} to a URL, read {"reply": ...} back."""

    name = "http"

    def __init__(self, url: str, timeout: float = 20.0, message_key: str = "message",
                 reply_key: str = "reply", actions_key: str = "actions") -> None:
        self.url = url.rstrip("/")
        self.timeout = timeout
        self.message_key = message_key
        self.reply_key = reply_key
        self.actions_key = actions_key
        self.session = ""

    @property
    def endpoint(self) -> str:
        return self.url

    def send(self, message: str) -> Reply:
        body = json.dumps({self.message_key: message}).encode("utf-8")
        headers = {"content-type": "application/json"}
        if self.session:
            headers["x-session"] = self.session
        req = urllib.request.Request(self.url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8") or "{}")
                return Reply(
                    text=payload.get(self.reply_key, ""),
                    actions=payload.get(self.actions_key) or [],
                    status=resp.status,
                )
        except urllib.error.HTTPError as e:
            return Reply(text=e.read().decode("utf-8", "replace"), status=e.code)
        except Exception as e:
            raise TargetError(f"{self.url}: {type(e).__name__}: {e}") from e


class LocalTarget:
    """Wrap a callable(text) -> (reply, actions)."""

    name = "local"

    def __init__(self, fn, label: str = "local") -> None:
        self._fn = fn
        self.label = label
        self.session = ""

    @property
    def endpoint(self) -> str:
        return f"local:{self.label}"

    def send(self, message: str) -> Reply:
        try:
            text, actions = self._fn(message, self.session)
        except TypeError:
            text, actions = self._fn(message)
        return Reply(text=text, actions=list(actions))


class ServedTarget:
    """Serve a callable over HTTP on a free port, for the length of a run.

    The demo needs a real URL so that promptfoo can be pointed at it with
    the same config a customer would write. A gate that only works
    in-process is not a gate anybody can use.
    """

    def __init__(self, fn) -> None:
        self._fn = fn
        self._server: ThreadingHTTPServer | None = None
        self._thread: threading.Thread | None = None

    def __enter__(self) -> HttpTarget:
        fn = self._fn

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):  # noqa: N802
                length = int(self.headers.get("content-length") or 0)
                raw = self.rfile.read(length) if length else b"{}"
                try:
                    message = json.loads(raw.decode("utf-8")).get("message", "")
                except Exception:
                    message = ""
                session = self.headers.get("x-session", "")
                try:
                    reply, actions = fn(message, session)
                except TypeError:
                    reply, actions = fn(message)
                body = json.dumps({"reply": reply, "actions": actions}).encode("utf-8")
                self.send_response(200)
                self.send_header("content-type", "application/json")
                self.send_header("content-length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):  # silence the access log
                return

        self._server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        port = self._server.server_address[1]
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()
        return HttpTarget(f"http://127.0.0.1:{port}/chat")

    def __exit__(self, *exc) -> None:
        if self._server:
            self._server.shutdown()
            self._server.server_close()
