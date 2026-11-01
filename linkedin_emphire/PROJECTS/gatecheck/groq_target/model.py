"""Groq chat completions, with no SDK and no dependency.

The gate is deliberately dependency-light, so the one place that talks to a
model does it with urllib. Groq is OpenAI-compatible at
https://api.groq.com/openai/v1, so the same file would work against any
OpenAI-shaped endpoint by changing base_url.

A model here is a callable:

    model(messages, tools) -> {"role": "assistant", "content": str|None,
                               "tool_calls": [...]}

That is the only surface the agent uses, which is what lets the tests run
the whole loop against a scripted model with no key and no network.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

DEFAULT_BASE_URL = "https://api.groq.com/openai/v1"
DEFAULT_MODEL = "openai/gpt-oss-120b"


class ModelError(RuntimeError):
    """The model refused, rate limited us, or answered with nonsense."""


class GroqModel:
    def __init__(
        self,
        api_key: str | None = None,
        model: str = DEFAULT_MODEL,
        base_url: str = DEFAULT_BASE_URL,
        temperature: float = 0.0,
        seed: int = 7,
        timeout: float = 60.0,
        max_tokens: int = 900,
    ) -> None:
        self.api_key = api_key or os.environ.get("GROQ_API_KEY", "")
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.temperature = temperature
        self.seed = seed
        self.timeout = timeout
        self.max_tokens = max_tokens
        if not self.api_key:
            raise ModelError(
                "GROQ_API_KEY is not set. Create a key at console.groq.com and, "
                "in PowerShell: $env:GROQ_API_KEY = 'gsk_...'"
            )

    def __call__(self, messages: list[dict], tools: list[dict] | None = None) -> dict:
        body = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "seed": self.seed,
            "max_completion_tokens": self.max_tokens,
        }
        if tools:
            body["tools"] = tools
            body["tool_choice"] = "auto"

        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "content-type": "application/json",
                "authorization": f"Bearer {self.api_key}",
                "user-agent": "gatecheck-target/0.2",
            },
            method="POST",
        )

        for attempt in (1, 2):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    payload = json.loads(response.read().decode("utf-8"))
                break
            except urllib.error.HTTPError as e:
                detail = e.read().decode("utf-8", "replace")[:400]
                if e.code == 429 and attempt == 1:
                    # free tier is 30 requests a minute; wait a beat and retry
                    time.sleep(6)
                    continue
                if e.code == 401:
                    raise ModelError(f"401 from Groq: the key was rejected. {detail}") from e
                raise ModelError(f"{e.code} from Groq: {detail}") from e
            except urllib.error.URLError as e:
                raise ModelError(f"cannot reach Groq: {e.reason}") from e

        try:
            message = payload["choices"][0]["message"]
        except (KeyError, IndexError) as e:
            raise ModelError(f"unexpected response shape: {str(payload)[:300]}") from e

        return {
            "role": "assistant",
            "content": message.get("content") or "",
            "tool_calls": message.get("tool_calls") or [],
        }


class ScriptedModel:
    """A model that says exactly what you tell it, for tests and dry runs.

    Pass a list of assistant messages; each call pops the next one. The last
    one repeats, so a loop that calls one time too many still terminates.
    """

    def __init__(self, script: list[dict]) -> None:
        if not script:
            raise ValueError("script cannot be empty")
        self.script = list(script)
        self.calls: list[list[dict]] = []

    def __call__(self, messages: list[dict], tools: list[dict] | None = None) -> dict:
        self.calls.append(list(messages))
        index = min(len(self.calls) - 1, len(self.script) - 1)
        return dict(self.script[index])


def tool_call(name: str, **arguments) -> dict:
    """Build the assistant message a model sends when it wants a tool run."""
    return {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {
                "id": f"call_{name}",
                "type": "function",
                "function": {"name": name, "arguments": json.dumps(arguments)},
            }
        ],
    }
