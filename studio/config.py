from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


@lru_cache(maxsize=1)
def load_config() -> dict:
    return yaml.safe_load((ROOT / "config" / "channel.yaml").read_text(encoding="utf-8"))


def episode_dir(ref: str) -> Path:
    """Accept '001', '001-ocean-layers' or a path."""
    p = Path(ref)
    if p.exists():
        return p.resolve()
    eps = ROOT / "episodes"
    matches = sorted(d for d in eps.iterdir() if d.is_dir() and d.name.startswith(ref))
    if not matches:
        raise FileNotFoundError(f"no episode matching {ref!r} in {eps}")
    return matches[0]
