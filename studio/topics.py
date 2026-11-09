"""Topic picker lanes (experiment D4, approved by the owner 2026-11-09).

The growth analyst ranks `data/ideas.md`; this module turns that ranking into the creative director's shortlist
with the lane rule applied:
- **blocked:** the prehistoric "every era" / deep-time lane (023 hippo every era 1.70% CTR, 025 oxygen 21 views
  at day 7, 028 megalodon every era 1.26% CTR on 1,673 impressions; `data/analytics/2026-11-08.json`).
- **favoured (+LANE_BONUS):** single famous animals (027 saltwater croc 10.5K impressions, 021 orcas 4.31% CTR on
  9.1K) and parasites / body horror (002 parasites 6.5% CTR, 014 brain parasites 5.1%).

    python -m studio topics [--top N] [--json]
"""
from __future__ import annotations

import re
from pathlib import Path

LANE_BONUS = 0.5

# Era or deep-time axis: "every era / period / prehistoric era", "when Earth had...", "before and after it died".
WEAK_ERA = re.compile(
    r"\bevery\s+(?:prehistoric\s+|geologic(?:al)?\s+)?(?:era|period|age|epoch|ice age|mass extinction)s?\b"
    r"|\bfrom every (?:era|period)\b|\bevery period of earth\b|\bbefore and after it died\b"
    r"|\bwhen (?:the )?(?:earth|antarctica|sahara|the sahara|the oceans?|the planet)\b[^|]*\b(?:was|had|grew|were)\b"
    r"|\bmillion[- ]year (?:rain|storm|winter|summer)",
    re.I)
BODY_HORROR = re.compile(r"\b(?:parasit\w*|worms?|larva\w*|fung\w*|zombie\w*|rabies|virus\w*|viral|infect\w*|"
                         r"disease\w*|botfl\w*|tapeworm\w*|leech\w*|lamprey\w*|brain[- ]eat\w*|flesh[- ]eat\w*|"
                         r"inside (?:your|doug's) body)\b", re.I)
# One named animal as the subject: "Why the Walrus...", "Every Reason the Bison...", "How the Komodo Dragon...",
# "Why Hyenas Are...", "Nothing About the Oarfish...". Group lists ("Every Animal in...", "Animals That...") are not.
SINGLE_ANIMAL = re.compile(
    r"^(?:why|how|every reason|nothing about|what)\s+(?:even\s+)?(?:(?:a|an|the)\s+)?"
    r"(?!(?:a|an|the|no|one|most|deadliest|scariest|creepiest|animals?|creatures?|nature|ocean|sea|deep|predators?|earth|things|doug|nothing|ground|mariana|trench|southern|arctic|antarctic\w*|amazon|sahara|desert|forest|jungle|cave|volcano\w*|swamp|mangrove|river|lake|island)\b)"
    r"[A-Za-z][\w'-]*(?:\s+[A-Z][\w'-]*){0,2}\s+(?:is|are|has|can|kills?|hunts?|gets?|lures?|doesn't|won't|leaves?|"
    r"comes?|snatches|sees?|run|runs|was)\b", re.I)


def lane(title: str, playlist: str) -> str:
    """'weak-era', 'single-animal', 'body-horror' or 'other'."""
    t = re.sub(r"\*\*NEW [^*]*\*\*\s*", "", title).strip()
    if WEAK_ERA.search(t):
        return "weak-era"
    if playlist == "parasites" or BODY_HORROR.search(t):
        return "body-horror"
    if playlist in ("animals", "ocean", "prehistoric") and SINGLE_ANIMAL.search(t) and not re.search(
            r"\b(?:every animal|animals that|creatures that|these animals|every apex|every prehistoric|"
            r"every terrifying animal)\b",
            t, re.I):
        return "single-animal"
    return "other"


def parse_ideas(path: Path) -> list[dict]:
    """Rows of the ranked backlog table in data/ideas.md."""
    rows, in_backlog = [], False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_backlog = line.strip().lower().startswith("## ranked backlog")
            continue
        if not in_backlog or not line.startswith("| ") or line.startswith("| #") or line.startswith("|---"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 11:
            continue
        m = re.search(r"\d+(?:\.\d+)?", c[9])
        status = c[-1]
        rows.append({"id": c[0], "title": re.sub(r"\*\*NEW [^*]*\*\*\s*", "", c[1]).strip(), "playlist": c[2],
                     "score": float(m.group()) if m else 0.0,
                     "status": re.sub(r"[*(].*$", "", status).strip().lower() or status[:20].lower(),
                     "note": status})
    return rows


def shortlist(ideas: list[dict]) -> tuple[list[dict], list[dict]]:
    """(ranked backlog with the lane rule applied, blocked weak-lane rows). Duplicate ids keep the first row."""
    seen, ok, blocked = set(), [], []
    for r in ideas:
        if not r["status"].startswith("backlog") or r["id"] in seen:
            continue
        seen.add(r["id"])
        r = dict(r, lane=lane(r["title"], r["playlist"]))
        if r["lane"] == "weak-era":
            blocked.append(r)
            continue
        r["adjusted"] = round(r["score"] + (LANE_BONUS if r["lane"] in ("single-animal", "body-horror") else 0), 2)
        ok.append(r)
    ok.sort(key=lambda r: -r["adjusted"])
    return ok, blocked


def episode_lane_problem(title: str, playlist: str) -> str | None:
    if lane(title, playlist) == "weak-era":
        return (f'"{title}" is in the blocked prehistoric "every era" lane (028 megalodon 1.26% CTR, 025 oxygen 21 '
                "views at day 7); pick a single famous animal or a parasites / body horror topic instead")
    return None
