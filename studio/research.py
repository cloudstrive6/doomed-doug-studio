"""Topic signals for the growth analyst: search demand, saturation, and current interest (views per hour).

    python -m studio signals "every parasite" "mariana trench" ...

Per query:
  demand      YouTube autocomplete (what people type): how many suggestions the phrase produces and how many
              keep the core words. 0-10.
  saturation  YouTube search, last 90 days: how many DIFFERENT channels already have a long video on it with
              100K+ views (format copies). Few = open lane; many = we'd arrive late.
  interest    views per hour of those recent videos (median and best): is the topic hot right now?
Results are cached 7 days (search costs 100 YouTube API units per query; keep runs to ~8 queries) and written to
data/signals/<date>.json.
"""
from __future__ import annotations

import datetime as dt
import json
import statistics
import urllib.parse
import urllib.request

from .config import ROOT

CACHE = ROOT / "data" / "signals" / "cache.json"


def autocomplete(q: str) -> list[str]:
    url = "https://suggestqueries.google.com/complete/search?" + urllib.parse.urlencode(
        {"client": "firefox", "ds": "yt", "hl": "en", "gl": "us", "q": q})
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.loads(r.read().decode("utf-8", "replace"))
    return data[1] if len(data) > 1 else []


def demand(q: str) -> dict:
    core = [w for w in q.lower().split() if len(w) > 3] or q.lower().split()
    seen = []
    for variant in (q, q + " ", "every " + q if not q.lower().startswith("every") else q + " explained"):
        for s in autocomplete(variant):
            if s not in seen:
                seen.append(s)
    relevant = [s for s in seen if all(w in s.lower() for w in core)]
    score = min(10, round(len(relevant) * 10 / 15))
    return {"score": score, "suggestions": relevant[:12]}


def saturation_and_interest(q: str, api=None) -> dict:
    from .youtube import _iso_dur, _parse_utc, yt
    api = api or yt()
    now = dt.datetime.now(dt.timezone.utc)
    since = (now - dt.timedelta(days=90)).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    items = api.search().list(part="snippet", q=q, type="video", order="viewCount", publishedAfter=since,
                              maxResults=25, relevanceLanguage="en").execute().get("items", [])
    ids = [i["id"]["videoId"] for i in items]
    if not ids:
        return {"copies_100k": 0, "channels": [], "vph_median": 0, "vph_best": 0, "top": []}
    vids = api.videos().list(part="snippet,statistics,contentDetails", id=",".join(ids)).execute()["items"]
    rows = []
    for v in vids:
        secs = _iso_dur(v["contentDetails"]["duration"])
        if secs <= 180:  # Shorts don't count as format copies
            continue
        views = int(v["statistics"].get("viewCount", 0))
        age_h = max(1.0, (now - _parse_utc(v["snippet"]["publishedAt"])).total_seconds() / 3600)
        rows.append({"title": v["snippet"]["title"], "channel": v["snippet"]["channelTitle"], "views": views,
                     "age_days": round(age_h / 24, 1), "vph": round(views / age_h, 1), "id": v["id"]})
    big = [r for r in rows if r["views"] >= 100_000]
    chans = sorted({r["channel"] for r in big})
    vphs = [r["vph"] for r in rows] or [0]
    return {"copies_100k": len(chans), "channels": chans[:10], "vph_median": round(statistics.median(vphs), 1),
            "vph_best": max(vphs), "top": sorted(rows, key=lambda r: -r["vph"])[:5]}


def signals(queries: list[str]) -> dict:
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    now = dt.datetime.now(dt.timezone.utc)
    out, api = {}, None
    for q in queries:
        c = cache.get(q.lower())
        if c and (now - dt.datetime.fromisoformat(c["at"])).days < 7:
            out[q] = c["data"]
            continue
        try:
            d = demand(q)
        except Exception as e:
            d = {"score": None, "error": str(e)[:200]}
        try:
            if api is None:
                from .youtube import yt
                api = yt()
            s = saturation_and_interest(q, api)
        except Exception as e:
            s = {"error": str(e)[:200]}
        out[q] = {"demand": d, "saturation": s}
        cache[q.lower()] = {"at": now.isoformat(), "data": out[q]}
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, indent=1, ensure_ascii=False), encoding="utf-8")
    day = ROOT / "data" / "signals" / f"{now.date().isoformat()}.json"
    prev = json.loads(day.read_text(encoding="utf-8")) if day.exists() else {}
    prev.update(out)
    day.write_text(json.dumps(prev, indent=1, ensure_ascii=False), encoding="utf-8")
    return out


def summary_line(q: str, d: dict) -> str:
    dm, sa = d.get("demand", {}), d.get("saturation", {})
    return (f"{q[:44]:44} demand {dm.get('score', '?'):>2}/10 | recent 100K+ copies: {sa.get('copies_100k', '?'):>2} "
            f"channels | views/hr median {sa.get('vph_median', '?'):>7} best {sa.get('vph_best', '?'):>8}")
