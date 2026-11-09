"""Packaging gate (experiment D4, approved by the owner 2026-11-09).

Every episode gets 10 candidate titles, each paired with the 1-3 words its thumbnail would carry. They are
ranked with the title.py rules below, the top 3 are kept, and each is paired with one of the three thumbnail
variants (A = thumbnail.json, B = thumbnail_test_b.json, C = thumbnail_test_c.json) so YouTube Studio's
3-way "Test & compare" has three real variants. The ranking and scores are written into
`episodes/<id>/metadata.json` under `packaging`, so the weekly growth memo can read results at day 7.

    python -m studio package <ep> rank [--candidates FILE] [--dry-run]   # rank title_candidates.json
    python -m studio package <ep> check                                  # check the 3 thumbnail files

Title lint rules adapted from `title.py` in the yt-package skill:
  Source: https://github.com/Jakeschincariol/youtube-agent-skill (skills/yt-package/title.py,
  commit a2feb21, fetched 2026-11-09). Licence below. Changes for Doomed Doug: a name counts as concrete
  like a number (the episode's creature or subject names come from the candidates file), the mobile check
  passes when the subject or number survives the 40-character cut, at most 3 thumbnail words (was 4),
  and a thumbnail check against the primary title as well as its paired title (a thumbnail-only Studio
  test shows all three thumbnails next to the primary title).

  MIT License

  Copyright (c) 2026 Jake Schincariol

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

GATE = "D4 packaging gate v1 (2026-11-09)"
DESKTOP, MOBILE, HARD = 60, 40, 100
MAX_CAPS = 2            # all-caps words in a title before it reads as spam
MAX_THUMB_WORDS = 3     # words on a thumbnail before it is a grey smear at feed size
N_CANDIDATES = 10
VARIANTS = [("A", "thumbnail.json", "build/thumbnail.png", "hero close-up"),
            ("B", "thumbnail_test_b.json", "build/thumbnail_b.png", "Doug in peril"),
            ("C", "thumbnail_test_c.json", "build/thumbnail_c.png", "second shock")]
READOUT = {"metric": "long-form CTR at day 7", "min_impressions": 1000,
           "baseline_median": 0.022, "baseline_top": [0.025, 0.043], "target_median": 0.04,
           "baseline_source": "data/analytics/2026-11-08.json"}

VAGUE = {"amazing", "incredible", "insane", "crazy", "huge", "massive", "ultimate", "best", "powerful",
         "secret", "revolutionary", "mindblowing", "epic", "perfect", "complete", "everything"}
STOP = {"the", "a", "an", "of", "for", "to", "in", "on", "and", "or", "is", "are", "with", "your", "you", "my", "i",
        "this", "that", "it", "how", "what", "why"}


def words(t: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", t.lower())


def thumb_word_count(text: str) -> int:
    """Words as a viewer reads them: '46,000 YRS' is two words, 'NOT ME?' is two."""
    return len([w for w in text.split() if re.search(r"[A-Za-z0-9]", w)])


def _has_name(t: str, names) -> str | None:
    low = t.lower()
    for n in names or ():
        n = n.strip().lower()
        if n and re.search(r"\b" + re.escape(n) + r"s?\b", low):
            return n
    return None


def check(title: str, thumb: str | None = None, names=(), primary: str | None = None) -> dict:
    """Lint one title + thumbnail-text pairing. Same scoring as title.py: 100 - 14 per issue + 4 per good point."""
    t = title.strip()
    n = len(t)
    issues, good = [], []
    if n > HARD:
        issues.append(("length", f"{n} characters, YouTube's hard limit is {HARD}"))
    elif n > DESKTOP:
        issues.append(("length", f"{n} characters, desktop search cuts near {DESKTOP}"))
    else:
        good.append(f"{n} characters, inside the {DESKTOP}-character desktop cut")
    nums = re.findall(r"\d[\d,.]*%?", t)
    name = _has_name(t, names)
    if n > MOBILE:
        head = t[:MOBILE].rsplit(" ", 1)[0]
        if _has_name(head, names) or re.search(r"\d", head):
            good.append(f'subject survives the mobile cut ("{head}...")')
        else:
            issues.append(("mobile", f'a mobile feed shows about "{head}..." and loses the subject'))
    caps = [w for w in t.split() if len(w) > 2 and w.isupper()]
    if len(caps) > MAX_CAPS:
        issues.append(("shouting", f"{len(caps)} all-caps words, {MAX_CAPS} is the ceiling before it reads as spam"))
    elif caps:
        good.append(f"{len(caps)} all-caps word for emphasis")
    v = [w for w in words(t) if w in VAGUE]
    if v:
        issues.append(("vague", f"{', '.join(sorted(set(v)))}: swap for a number, a name or a date"))
    if nums:
        good.append(f"carries a concrete figure ({', '.join(nums[:3])})")
    if name:
        good.append(f"carries a name ({name})")
    if not nums and not name:
        issues.append(("no-number", "no number, date or name, the most reliable single fix"))
    front = [w for w in words(t)[:3] if w not in STOP]
    if not front:
        issues.append(("front-load", "the first three words are all filler, move the subject forward"))
    if thumb is not None:
        hw = set(words(thumb)) - STOP
        if not hw:
            issues.append(("thumb-empty", "no thumbnail words: give it 1 to 3 words that add to the title"))
        for label, other in (("duplicate", t), ("duplicate-primary", primary)):
            if not other or (label == "duplicate-primary" and other.strip() == t):
                continue
            shared = (set(words(other)) - STOP) & hw
            if shared:
                issues.append((label, f"thumbnail repeats the {'primary ' if label != 'duplicate' else ''}title on "
                                      f"{', '.join(sorted(shared))}; it should say what the title does not"))
        if hw and not any(k.startswith("duplicate") for k, _ in issues):
            good.append("thumbnail and title carry different words")
        tw = thumb_word_count(thumb)
        if tw > MAX_THUMB_WORDS:
            issues.append(("thumb-length", f"{tw} words on the thumbnail, {MAX_THUMB_WORDS} is the ceiling at feed size"))
    raw = 100 - 14 * len(issues) + 4 * len(good)  # unclipped: breaks ties between candidates at 100
    score = max(0, min(100, raw))
    return {"title": t, "thumb_text": thumb, "chars": n, "score": score, "raw": raw,
            "issues": [f"{k}: {m}" for k, m in issues], "issue_keys": [k for k, _ in issues], "good": good}


# Issues that may never ship on one of the three kept variants (the rest only lower the rank).
BLOCKING = {"length", "shouting", "duplicate", "duplicate-primary", "thumb-length", "thumb-empty"}


def rank(cands: list[dict], names=()) -> dict:
    """Score every candidate, keep the 3 best that pass the blocking rules and pair them with variants A, B, C.
    The titler's order breaks ties (it lists its own favourite first)."""
    scored = []
    for i, c in enumerate(cands):
        r = check(c["title"], c.get("thumb_text", ""), names)
        r.update(concept=c.get("concept", ""), formula=c.get("formula", ""), order=i)
        scored.append(r)
    scored.sort(key=lambda r: (-r["score"], -r["raw"], r["order"]))
    kept, seen = [], set()
    for r in scored:
        if len(kept) == 3:
            break
        if BLOCKING & set(r["issue_keys"]) or r["title"].lower() in seen:
            continue
        thumb_words = set(words(r["thumb_text"] or "")) - STOP
        if any(thumb_words == set(words(k["thumb_text"])) - STOP for k in kept):
            continue  # three thumbnails saying the same words is not a 3-way test
        if kept:  # in a thumbnail-only test every thumbnail sits next to the primary title
            again = check(r["title"], r["thumb_text"], names, primary=kept[0]["title"])
            if "duplicate-primary" in again["issue_keys"]:
                continue
        kept.append(r)
        seen.add(r["title"].lower())
    variants = []
    for (v, f, png, default_concept), r in zip(VARIANTS, kept):
        variants.append({"variant": v, "file": f, "png": png, "title": r["title"], "thumb_text": r["thumb_text"],
                         "concept": default_concept, "thumb_idea": r["concept"], "score": r["score"], "raw": r["raw"],
                         "issues": r["issues"]})
    return {"gate": GATE, "ranked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "names": list(names), "candidates": [{k: r[k] for k in ("title", "thumb_text", "concept", "formula",
                                                                     "chars", "score", "raw", "issues")} for r in scored],
            "variants": variants, "readout": READOUT}


def load_candidates(path: Path) -> tuple[list[dict], list[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    cands = data["candidates"] if isinstance(data, dict) else data
    names = data.get("names", []) if isinstance(data, dict) else []
    return cands, names


def candidate_problems(cands: list[dict]) -> list[str]:
    probs = []
    if len(cands) < N_CANDIDATES:
        probs.append(f"title_candidates.json has {len(cands)} candidates; the packaging gate needs {N_CANDIDATES}")
    for c in cands:
        if not c.get("title") or not c.get("thumb_text"):
            probs.append(f"candidate without title or thumb_text: {c}")
    if len({c.get('title', '').lower() for c in cands}) < len(cands):
        probs.append("duplicate titles among the candidates")
    return probs


def apply(ep: Path, result: dict) -> dict:
    """Write the ranking into metadata.json: title = variant A's title, alt_titles = the rest in rank order."""
    p = ep / "metadata.json"
    m = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    if m.get("youtube_id"):
        raise SystemExit(f"{ep.name} is already uploaded; packaging is not re-ranked after upload")
    titles = [v["title"] for v in result["variants"]]
    m["title"] = titles[0]
    m["alt_titles"] = titles[1:] + [c["title"] for c in result["candidates"] if c["title"] not in titles][:2]
    m["packaging"] = result
    p.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return m


# ---- thumbnail files ---------------------------------------------------------------------------------------

def thumbnail_texts(scene: dict) -> list[str]:
    """Every piece of text a viewer sees on a thumbnail scene (text, wordart, label, speech, tile labels)."""
    out = []

    def walk(els):
        for e in els or []:
            if e.get("type") in ("text", "wordart", "label", "speech") and e.get("text"):
                out.append(str(e["text"]))
            if e.get("type") == "tile" and e.get("label"):
                out.append(str(e["label"]))
            walk(e.get("elements"))
    walk(scene.get("elements"))
    return out


def _dougs(els):
    for e in els or []:
        if e.get("type") == "doug":
            yield e
        yield from _dougs(e.get("elements"))


def thumbnail_problems(ep: Path) -> list[str]:
    """Check the three variant files against the kept pairings and the channel's thumbnail rules
    (Doug with his red cap in every variant, at most 3 words, words that add to the title)."""
    m = json.loads((ep / "metadata.json").read_text(encoding="utf-8"))
    pk = m.get("packaging")
    if not pk:
        return ["metadata.json has no packaging block: run `python -m studio package <id> rank` (D4 packaging gate)"]
    probs = []
    if len(pk.get("variants", [])) < 3:
        probs.append(f"packaging kept {len(pk.get('variants', []))} variants; the 3-way test needs 3 "
                     "(write better candidates and re-rank)")
    primary = m.get("title", "")
    if pk.get("variants") and primary != pk["variants"][0]["title"]:
        probs.append("metadata title differs from packaging variant A; re-rank instead of editing the title by hand")
    for v in pk.get("variants", []):
        f = ep / v["file"]
        if not f.exists():
            probs.append(f"{v['file']} missing (variant {v['variant']}: \"{v['thumb_text']}\")")
            continue
        scene = json.loads(f.read_text(encoding="utf-8"))
        text = " ".join(thumbnail_texts(scene))
        n = thumb_word_count(text)
        if n > MAX_THUMB_WORDS:
            probs.append(f"{v['file']} shows {n} words ({text!r}); at most {MAX_THUMB_WORDS}")
        if n == 0:
            probs.append(f"{v['file']} has no words; it should carry \"{v['thumb_text']}\"")
        for t in {primary, v["title"]}:
            shared = (set(words(text)) - STOP) & (set(words(t)) - STOP)
            if shared:
                probs.append(f"{v['file']} repeats title words {sorted(shared)} from \"{t}\"")
        if text and set(words(text)) != set(words(v["thumb_text"])):
            probs.append(f"{v['file']} says {text!r} but packaging variant {v['variant']} is \"{v['thumb_text']}\" "
                         "(build the thumbnail with the ranked words, or re-rank with the new words)")
        dougs = list(_dougs(scene.get("elements")))
        if not dougs:
            probs.append(f"{v['file']} has no Doug (red cap in every variant is the channel rule)")
        elif all({"cap_off", "cap_taken"} & set(d.get("gear", [])) for d in dougs):
            probs.append(f"{v['file']}: Doug's red cap is off; it must be visible in every variant")
    return probs


def report(result: dict) -> str:
    lines = [f"{result['gate']}: {len(result['candidates'])} candidates ranked"]
    for i, c in enumerate(result["candidates"], 1):
        lines.append(f"{i:2}. {c['score']:3} ({c['raw']:3})  {c['title']}  [{c['thumb_text']}]")
        for s in c["issues"]:
            lines.append(f"          x {s}")
    lines.append("Kept for the 3-way Test & compare:")
    for v in result["variants"]:
        lines.append(f"  {v['variant']} {v['file']:24} {v['score']:3}  {v['title']}  [{v['thumb_text']}]  "
                     f"({v['concept']}: {v['thumb_idea'] or 'designer picks'})")
    return "\n".join(lines)
