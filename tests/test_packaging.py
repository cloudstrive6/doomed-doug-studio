"""Tests for the D4 packaging gate and topic lanes (2026-11-09).

    python tests/test_packaging.py        # or: python -m pytest tests/test_packaging.py
"""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from studio import packaging as pk  # noqa: E402
from studio import topics  # noqa: E402

NAMES = ["walrus", "walruses"]
CANDS = [
    {"title": "How the Walrus Kills Doug Without a Single Bite", "thumb_text": "NO TEETH NEEDED", "concept": "hero"},
    {"title": "Why a 1.5-Tonne Walrus Can Sink Doug's Boat", "thumb_text": "TOO CLOSE", "concept": "peril"},
    {"title": "Every Reason 40,000 Walruses Are a Death Trap for Doug", "thumb_text": "STAMPEDE", "concept": "herd"},
    {"title": "The Most TERRIFYING HUGE ANIMAL That KILLS Doug Without Biting", "thumb_text": "BIG", "concept": ""},
    {"title": "Why This Arctic Giant Is the Scariest Thing Doug Has Ever Met in the Sea Ice",
     "thumb_text": "RUN", "concept": ""},
    {"title": "Why the Walrus Is Scarier Than It Looks", "thumb_text": "WALRUS ATTACK", "concept": ""},
    {"title": "How Walruses Drown Doug Under the Ice", "thumb_text": "HE CANNOT SWIM AT ALL", "concept": ""},
    {"title": "The Arctic Animal That Kills Doug by Sitting on Him", "thumb_text": "SQUASHED", "concept": ""},
    {"title": "What the Walrus Does to Kayaks Near Point Lay", "thumb_text": "TOO CLOSE", "concept": ""},
    {"title": "Why the Walrus Hunts Seals, and Then Doug", "thumb_text": "DOUG NEXT", "concept": ""},
]


def test_check_rules():
    r = pk.check("Why a 1.5-Tonne Walrus Can Sink Doug's Boat", "TOO CLOSE", NAMES)
    assert r["issues"] == [], r
    assert any("concrete figure" in g for g in r["good"]) and any("name" in g for g in r["good"])
    long = pk.check("Why This Arctic Giant Is the Scariest Thing Doug Has Ever Met in the Sea Ice", "RUN", NAMES)
    assert "length" in long["issue_keys"] and "mobile" in long["issue_keys"] and "no-number" in long["issue_keys"]
    shout = pk.check("The Most TERRIFYING HUGE ANIMAL That KILLS Doug", "BIG")
    assert "shouting" in shout["issue_keys"] and "vague" in shout["issue_keys"]
    dup = pk.check("Why the Walrus Is Scarier Than It Looks", "WALRUS ATTACK", NAMES)
    assert "duplicate" in dup["issue_keys"]
    four = pk.check("How Walruses Drown Doug Under the Ice", "HE CANNOT SWIM AT ALL", NAMES)
    assert "thumb-length" in four["issue_keys"]
    assert pk.thumb_word_count("46,000 YRS") == 2 and pk.thumb_word_count("NOT ME?") == 2
    # a name in the first 40 characters keeps the mobile cut from losing the subject
    ok = pk.check("How the Walrus Kills Doug Without a Single Bite", "NO TEETH", NAMES)
    assert "mobile" not in ok["issue_keys"]


def test_rank_keeps_three_distinct_safe_variants():
    res = pk.rank(CANDS, NAMES)
    assert len(res["candidates"]) == 10
    scores = [(c["score"], c["raw"]) for c in res["candidates"]]
    assert scores == sorted(scores, reverse=True)
    v = res["variants"]
    assert [x["variant"] for x in v] == ["A", "B", "C"]
    assert [x["file"] for x in v] == ["thumbnail.json", "thumbnail_test_b.json", "thumbnail_test_c.json"]
    titles = [x["title"] for x in v]
    assert len(set(titles)) == 3
    for x in v:
        assert not pk.BLOCKING & {i.split(":")[0] for i in x["issues"]}, x
        assert pk.thumb_word_count(x["thumb_text"]) <= 3
        # no thumbnail repeats the primary title (thumbnail-only tests show every variant next to it)
        assert not (set(pk.words(x["thumb_text"])) - pk.STOP) & (set(pk.words(titles[0])) - pk.STOP)
    # duplicate thumb words ("TOO CLOSE" twice) never fill two variant slots
    assert len({x["thumb_text"] for x in v}) == 3
    # the blocked candidates are ranked but never kept
    assert not any(x["title"].startswith("The Most TERRIFYING") for x in v)


def _scene(text, cap=True, words_key="text"):
    doug = {"type": "doug", "x": 300, "y": 600, "scale": 0.5, "pose": "arms_up", "expression": "shock"}
    if not cap:
        doug["gear"] = ["cap_off"]
    el = {"type": "tile", "label": text} if words_key == "label" else {"type": "wordart", "text": text}
    return {"size": [1280, 720], "elements": [{"type": "asset", "name": "walrus"}, {"type": "group", "elements": [doug]}, el]}


def test_apply_and_thumbnail_check():
    with tempfile.TemporaryDirectory() as d:
        ep = Path(d) / "999-test"
        ep.mkdir()
        (ep / "metadata.json").write_text(json.dumps({"title": "x", "playlist": "animals", "description": "d" * 300}))
        res = pk.rank(CANDS, NAMES)
        m = pk.apply(ep, res)
        assert m["title"] == res["variants"][0]["title"]
        assert len(m["alt_titles"]) == 4 and m["alt_titles"][:2] == [v["title"] for v in res["variants"][1:]]
        saved = json.loads((ep / "metadata.json").read_text(encoding="utf-8"))
        assert saved["packaging"]["readout"]["target_median"] == 0.04
        assert len(saved["packaging"]["candidates"]) == 10
        # no thumbnail files yet: every variant is reported missing
        assert sum("missing" in p for p in pk.thumbnail_problems(ep)) == 3
        for v in res["variants"]:
            (ep / v["file"]).write_text(json.dumps(_scene(v["thumb_text"])))
        assert pk.thumbnail_problems(ep) == [], pk.thumbnail_problems(ep)
        # a grid with four labels, a cap knocked off, and words that do not match the ranking all fail
        grid = {"size": [1280, 720], "elements": [{"type": "tile", "label": w} for w in ("46,000 YRS", "101M YRS")]
                + [_scene("x")["elements"][1]]}
        (ep / "thumbnail_test_c.json").write_text(json.dumps(grid))
        (ep / "thumbnail_test_b.json").write_text(json.dumps(_scene(res["variants"][1]["thumb_text"], cap=False)))
        probs = pk.thumbnail_problems(ep)
        assert any("thumbnail_test_c.json shows 4 words" in p for p in probs), probs
        assert any("cap is off" in p for p in probs), probs
        # an uploaded episode is never re-ranked
        saved["youtube_id"] = "abc"
        (ep / "metadata.json").write_text(json.dumps(saved))
        try:
            pk.apply(ep, res)
            raise AssertionError("apply should refuse an uploaded episode")
        except SystemExit:
            pass


def test_candidate_problems():
    assert pk.candidate_problems(CANDS) == []
    assert pk.candidate_problems(CANDS[:5])
    assert pk.candidate_problems(CANDS + [CANDS[0]])


def test_lanes():
    weak = ["Could Megalodon Survive Every Era Before and After It Died?",
            "When Earth Had So Much Oxygen That Bugs Could Kill Doug",
            "Would a Hippo Survive Every Prehistoric Era? Doug Died Trying",
            "How Fast Doug Would Die in Every Prehistoric Era",
            "The Deadliest Predator From Every Period of Earth's History",
            "When the Sahara Was Green and Full of Things That Wanted Doug Dead"]
    for t in weak:
        assert topics.lane(t, "prehistoric") == "weak-era", t
    single = ["Every Reason the Saltwater Crocodile Is the Scariest Reptile",
              "Why Orcas Kill Everything in the Ocean Except Doug",
              "How the Komodo Dragon Kills Doug Without Chasing Him",
              "Why Hyenas Are Deadlier to Doug Than Lions",
              "Nothing About the Oarfish Is Normal"]
    for t in single:
        assert topics.lane(t, "animals") == "single-animal", t
    assert topics.lane("What Dying From Every Parasite Would Feel Like", "parasites") == "body-horror"
    assert topics.lane("The Parasites That Turn Insects Into Zombies", "animals") == "body-horror"
    for t in ["Why the Mariana Trench Gets Deadlier the Deeper Doug Goes",
              "Every Animal in the Amazon River That Wants Doug Dead",
              "The Most Disturbing Things Nature Kept Trapped the Longest"]:
        assert topics.lane(t, "ocean") == "other", t
    assert topics.episode_lane_problem("Could Megalodon Survive Every Era Before and After It Died?", "prehistoric")
    assert topics.episode_lane_problem("How the Walrus Kills Doug Without a Single Bite", "animals") is None


def test_shortlist_on_real_backlog():
    ideas = topics.parse_ideas(Path(__file__).resolve().parents[1] / "data" / "ideas.md")
    ok, blocked = topics.shortlist(ideas)
    assert ok and blocked, "the gate must neither block everything nor nothing"
    assert all(r["lane"] != "weak-era" for r in ok)
    assert [r["adjusted"] for r in ok] == sorted((r["adjusted"] for r in ok), reverse=True)
    assert all(r["status"].startswith("backlog") for r in ok + blocked)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
    print("ALL OK")
