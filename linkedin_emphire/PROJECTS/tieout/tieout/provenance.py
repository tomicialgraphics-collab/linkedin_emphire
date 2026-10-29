"""P2 provenance snapshot."""
from __future__ import annotations

import platform

from .models import Provenance


def snapshot(
    *,
    suite: str,
    family_policy_versions: dict[str, str],
    agent: str,
    dataset_hash: str,
    started_at: str,
    finished_at: str,
    model: str | None = None,
    model_version: str | None = None,
    decoding: dict | None = None,
    seed: int = 0,
    harness_git: str = "",
) -> Provenance:
    from . import __version__

    return Provenance(
        harness_version=__version__,
        harness_git=harness_git,
        suite=suite,
        family_policy_versions=family_policy_versions,
        agent=agent,
        model=model,
        model_version=model_version,
        dataset_hash=dataset_hash,
        env={
            "python": platform.python_version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
        },
        decoding=decoding or {},
        seed=seed,
        started_at=started_at,
        finished_at=finished_at,
    )
