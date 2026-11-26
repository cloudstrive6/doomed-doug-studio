"""Turns the approved pilot into a normal studio episode folder (episodes/<NNN-slug>/) in the live repo so
`python -m studio upload` handles it like every other episode: metadata.json, build/final.mp4, build/thumbnail.png,
build/captions.srt (exact, from the voiced line timings), build/chapters.txt, thumbnail A/B/C files for Test & Compare.
Usage: py make_episode.py <live studio root> <NNN-slug>"""
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
live = Path(sys.argv[1])
ep = live / "episodes" / sys.argv[2]
(ep / "build").mkdir(parents=True, exist_ok=True)
L = json.loads((HERE / "build" / "lines.json").read_text(encoding="utf-8"))


def ts(t, srt=False):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    if srt:
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"
    return f"{int(m)}:{int(s):02d}" if h < 1 else f"{int(h)}:{int(m):02d}:{int(s):02d}"


# captions: one cue per voiced line (long lines split in two at a comma or the middle)
cues = []
for l in L["lines"]:
    words = l["text"].split()
    parts = [l["text"]]
    if len(words) > 16:
        mid = len(words) // 2
        parts = [" ".join(words[:mid]), " ".join(words[mid:])]
    n = len(parts)
    for i, ptxt in enumerate(parts):
        a = l["start"] + l["dur"] * i / n
        b = l["start"] + l["dur"] * (i + 1) / n
        cues.append((a, b, ptxt))
(ep / "build" / "captions.srt").write_text(
    "\n".join(f"{i + 1}\n{ts(a, True)} --> {ts(b, True)}\n{t}\n" for i, (a, b, t) in enumerate(cues)), encoding="utf-8")

CHAPTERS = [("01", "The Storm"), ("03", "Day 1: Is That a Megalodon?"), ("06", "Day 2: Keep Swimming"),
            ("07", "Day 3: Tap Tap"), ("08", "Day 6: The Contract"), ("11", "Day 12: Too Big for the Pool"),
            ("13", "Day 15: Fisheries"), ("16", "Day 20: The Lagoon"), ("18", "Day 24: The Great White"),
            ("21", "Day 30: Midnight at the Reef"), ("26", "What Was Real")]
first = {}
for l in L["lines"]:
    first.setdefault(l["scene"], l["start"])
ch = [f"0:00 {CHAPTERS[0][1]}"] + [f"{ts(first[n] - 0.3)} {name}" for n, name in CHAPTERS[1:]]
(ep / "build" / "chapters.txt").write_text("\n".join(ch), encoding="utf-8")

desc = """A storm throws a two metre megalodon pup over your back fence and into your swimming pool. Now you have one fisheries officer, a neighbour who wants to sell it, and a shark that will not stop growing.

What is real: every science card. Megalodon died out about 3.6 million years ago, its name means big tooth, and scientists still argue about its size, its speed and how big its babies were. We show both sides.

What is invented: a living megalodon, the pool, the deadline and the rescue at sea.

Shark bites are rare, about 70 unprovoked bites a year worldwide. Never feed, touch or chase a wild shark, and swim with a buddy.

Cash or Meatball? Tell us in the comments.

CHAPTERS
{{CHAPTERS}}

KEY SOURCES
Natural History Museum, London, megalodon: https://www.nhm.ac.uk/discover/megalodon--the-truth-about-the-largest-shark-that-ever-lived.html
2019 extinction date study (ScienceDaily): https://www.sciencedaily.com/releases/2019/02/190213081637.htm
UCLA, megalodon was warm bodied (PNAS 2023): https://newsroom.ucla.edu/releases/megalodon-warm-blooded-extinct-shark
University of Zurich, energy needs model (Science Advances 2022): https://www.eurekalert.org/news-releases/961980
Florida Museum, megalodon nursery in Panama: https://www.floridamuseum.ufl.edu/science/megalodon-shark-nursery-discovered/
DePaul University, 2025 size and shape study: https://www.depaul.edu/news/megalodon-study-2025
Florida Museum, shark bite facts: https://www.floridamuseum.ufl.edu/discover-fish/sharks/shark-attack-faq/

DISCLAIMER
Educational entertainment. A living megalodon is fiction; the science on the cards is real and sourced. Cartoon only.

AI USE
The voices are AI text-to-speech. The script is researched and written with AI assistance and fact-checked against the sources above. All drawings are original.

#megalodon #whatif #sharks"""
meta = {
    "title": "What If a Baby MEGALODON Lived in Your Pool for 30 Days?",
    "alt_titles": ["What If a Baby MEGALODON Landed in Your Pool?",
                   "What If Your Pet MEGALODON Outgrew Your Pool in 12 Days?"],
    "format": "what-if-v1 (toon engine, branch whatif-pilot, pilot w01)",
    "description": desc,
    "tags": ["pet megalodon", "baby megalodon", "megalodon in pool", "megalodon pup", "megalodon facts",
             "what if megalodon was alive", "megalodon cartoon", "shark story animation", "what if", "doomed doug"],
    "playlist": "ocean",
    "paid_promotion": False,
    "review": {"independent_video_review": "3.5 of 5 (v4, 2026-11-27)", "file": "pilots/w01-pet-megalodon/video_review.md"},
    "thumbnail_tests": {"A": "build/thumbnail.png", "B": "build/thumbnail_B.png", "C": "build/thumbnail_C.png",
                        "note": "Bryce 2026-11-27: all three in YouTube Test & Compare"},
}
(ep / "metadata.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
for src, dst in (("build/final.mp4", "build/final.mp4"), ("thumbs/thumb_A.png", "build/thumbnail.png"),
                 ("thumbs/thumb_B.png", "build/thumbnail_B.png"), ("thumbs/thumb_C.png", "build/thumbnail_C.png"),
                 ("script.md", "script.md"), ("facts.md", "facts.md"), ("script_review.md", "script_review.md"),
                 ("video_review.md", "video_review.md")):
    shutil.copy2(HERE / src, ep / dst)
print("episode folder ready:", ep)
print("\n".join(ch))
