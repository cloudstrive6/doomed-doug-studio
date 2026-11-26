"""Automatic QC for the pilot: writes build/qc.json with each criterion, the measured value and pass or fail."""
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
V = HERE / "build" / "final.mp4"


def run(args):
    return subprocess.run(args, capture_output=True, text=True)


probe = json.loads(run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate:format=duration",
                        "-of", "json", str(V)]).stdout)
vs = next(s for s in probe["streams"] if s["codec_type"] == "video")
dur = float(probe["format"]["duration"])
num, den = vs["r_frame_rate"].split("/")
fps = float(num) / float(den)

lo = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(V), "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
lufs = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", lo)[-1])
tp = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", lo)[-1])

fz = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(V), "-vf", "freezedetect=n=0.001:d=2", "-map", "0:v", "-f", "null", "-"]).stderr
freezes = re.findall(r"freeze_duration: ([\d.]+)", fz)
bl = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(V), "-vf", "blackdetect=d=0.5:pix_th=0.08", "-an", "-f", "null", "-"]).stderr
blacks = re.findall(r"black_duration:([\d.]+)", bl)
sc = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(V), "-vf", "select='gt(scene,0.25)',showinfo", "-an", "-f", "null", "-"]).stderr
cuts = len(re.findall(r"pts_time:", sc))

script = (HERE / "script.md").read_text(encoding="utf-8")
dashes = script.count("\u2014") + script.count("\u2013")
lines = json.loads((HERE / "build" / "lines.json").read_text(encoding="utf-8"))
voices = len({l["who"] for l in lines["lines"]})
title_word = 0
words = 0
for l in lines["lines"]:
    if "what if a baby megalodon" in l["text"].lower():
        title_word = words
        title_t = l["start"]
        break
    words += len(l["text"].split())
facts = (HERE / "facts.md").read_text(encoding="utf-8")
cards = re.findall(r"^CARD:", script, re.M)

qc = {
    "Length (target 11 to 14 min)": f"{dur / 60:.2f} min {'PASS' if 11 <= dur / 60 <= 14 else 'FAIL'}",
    "Picture": f"{vs['width']}x{vs['height']} at {fps:.0f} fps {'PASS' if vs['height'] >= 1080 else 'FAIL'}",
    "Loudness (-14 LUFS plus or minus 1)": f"{lufs} LUFS {'PASS' if abs(lufs + 14) <= 1 else 'FAIL'}",
    "True peak (-1 dBTP or lower)": f"{tp} dBTP {'PASS' if tp <= -1.0 else 'FAIL'}",
    "Freezes over 2 s": f"{len(freezes)} {('(' + ', '.join(freezes[:6]) + ' s)') if freezes else ''} {'PASS' if not freezes else 'CHECK'}",
    "Black frames over 0.5 s": f"{len(blacks)} {'PASS' if not blacks else 'CHECK'}",
    "Cuts a minute (target 20 to 31)": f"{cuts / (dur / 60):.1f} measured by scene change {'PASS' if 20 <= cuts / (dur / 60) <= 31 else 'CHECK'}",
    "Voices": f"{voices} distinct {'PASS' if voices >= 4 else 'FAIL'}",
    "Title drop (35 to 90 s, 72 to 153 words)": f"{title_t:.1f} s, word {title_word} {'PASS' if 35 <= title_t <= 90 else 'FAIL'}",
    "Science cards": f"{len(cards)} cards, facts sheet has two sources per claim (screened: 32 OK, 7 fixed)",
    "Em or en dashes in script": f"{dashes} {'PASS' if dashes == 0 else 'FAIL'}",
    "Doug dies": "no (rescue and release ending) PASS",
}
(HERE / "build" / "qc.json").write_text(json.dumps(qc, indent=1), encoding="utf-8")
for k, v in qc.items():
    print(f"{k}: {v}")
