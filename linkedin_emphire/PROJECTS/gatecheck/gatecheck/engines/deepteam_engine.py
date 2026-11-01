"""DeepTeam engine: breadth.

DeepTeam's value in a gate is the breadth of its generated variants and
the fact that its attack classes are deterministic string transforms, so
a gate can run them on every pull request without a model call, a key or
a bill. The generative half needs a simulator model and is reported as
skipped rather than pretended.
"""
from __future__ import annotations

from ..corpus import SINGLE_TURN, Case
from .base import Engine


def _base64(text: str) -> str:
    import base64

    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def _rot13(text: str) -> str:
    import codecs

    return codecs.encode(text, "rot13")


class DeepTeamEngine(Engine):
    name = "deepteam"
    label = "DeepTeam"

    def available(self) -> tuple[bool, str]:
        try:
            import deepteam  # noqa: F401
        except ModuleNotFoundError as e:
            if "sentry_sdk" in str(e):
                return False, "deepteam needs sentry-sdk installed: pip install sentry-sdk"
            return False, f"deepteam not installed: {e}"
        except Exception as e:  # pragma: no cover
            return False, f"deepteam not importable: {e}"
        return True, ""

    def version(self) -> str:
        try:
            from importlib import metadata

            return metadata.version("deepteam")
        except Exception:
            return "unknown"

    def plan(self) -> list[Case]:
        cases: list[Case] = []
        for case in SINGLE_TURN:
            for variant, transform in (
                ("raw", None),
                ("base64", _base64),
                ("leetspeak", self._leet),
                ("rot13", _rot13),
            ):
                prompt = case.prompts[0] if transform is None else transform(case.prompts[0])
                cases.append(
                    Case(
                        attack_id=f"{case.attack_id}-{variant}",
                        hint=case.hint,
                        prompts=(prompt,),
                        note=f"{case.note} [{variant}]",
                    )
                )
        return cases

    @staticmethod
    def _leet(text: str) -> str:
        """DeepTeam's Leetspeak.enhance when available, else a local table."""
        try:
            from deepteam.attacks.single_turn import Leetspeak

            return Leetspeak(weight=1).enhance(attack=text)
        except Exception:
            return text.translate(str.maketrans({"e": "3", "a": "4", "o": "0", "i": "1", "s": "5"}))
