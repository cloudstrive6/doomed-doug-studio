"""Builds review/index.html for Bryce: the pilot video, the three thumbnails, the packaging options, the reviews and the
script. Served on 127.0.0.1:8777 (launch.json entry doug-whatif-review)."""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
out = HERE / "review"
out.mkdir(exist_ok=True)


def md(text):
    """Tiny markdown to HTML: headings, tables, lists, bold, paragraphs."""
    lines, res, table = text.splitlines(), [], []
    def flush():
        if table:
            rows = [r for r in table if not re.match(r"^\|\s*-", r)]
            res.append("<table>" + "".join(
                "<tr>" + "".join(f"<{'th' if i == 0 else 'td'}>{inline(c.strip())}</{'th' if i == 0 else 'td'}>"
                                 for c in r.strip().strip("|").split("|")) + "</tr>" for i, r in enumerate(rows)) + "</table>")
            table.clear()
    def inline(s):
        s = html.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
        return re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    for ln in lines:
        if ln.startswith("|"):
            table.append(ln)
            continue
        flush()
        if ln.startswith("#"):
            n = len(ln) - len(ln.lstrip("#"))
            res.append(f"<h{min(6, n + 2)}>{inline(ln.lstrip('# '))}</h{min(6, n + 2)}>")
        elif ln.strip().startswith(("- ", "* ")):
            res.append(f"<li>{inline(ln.strip()[2:])}</li>")
        elif re.match(r"^\d+\.\s", ln.strip()):
            res.append(f"<li>{inline(re.sub(r'^\d+\.\s', '', ln.strip()))}</li>")
        elif ln.strip():
            res.append(f"<p>{inline(ln)}</p>")
    flush()
    return "\n".join(res)


def read(name):
    p = HERE / name
    return p.read_text(encoding="utf-8") if p.exists() else f"({name} not written yet)"


qc = read("build/qc.json")
try:
    qc = json.loads(qc)
except Exception:
    qc = {}
qc_rows = "".join(f"<tr><td>{html.escape(k)}</td><td>{html.escape(str(v))}</td></tr>" for k, v in qc.items())

page = f"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Doug What If Pilot</title>
<style>
:root{{--bg:#0f1626;--card:#18233a;--ink:#eef2f8;--mute:#9fb0c8;--acc:#f6b73c;--red:#e0201b}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 system-ui,Segoe UI,sans-serif}}
main{{max-width:1100px;margin:0 auto;padding:16px}}
h1{{font-size:28px;margin:8px 0}} h2{{color:var(--acc);margin-top:32px}}
.card{{background:var(--card);border-radius:14px;padding:16px;margin:12px 0}}
video{{width:100%;border-radius:12px;background:#000}}
.thumbs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px}}
.thumbs figure{{margin:0}} .thumbs img{{width:100%;border-radius:10px}} figcaption{{color:var(--mute);font-size:14px}}
table{{border-collapse:collapse;width:100%;font-size:14px}} td,th{{border-bottom:1px solid #2a3858;padding:6px;text-align:left;vertical-align:top}}
details summary{{cursor:pointer;color:var(--acc);font-weight:600}} code{{color:#ffd28a}}
.ask{{border-left:5px solid var(--red)}}
</style></head><body><main>
<h1>Doomed Doug: What If pilot w01, Pet Megalodon</h1>
<p style="color:var(--mute)">New format test, 2026-11-26. Nothing uploaded. Branch <code>whatif-pilot</code> of the studio repo.</p>
<div class="card"><video controls preload="metadata" src="../build/final.mp4" poster="../thumbs/thumb_A.png"></video></div>
<div class="card ask"><h2 style="margin-top:0">What I need from you</h2>
<ol><li>Watch the pilot: approve it, or tell me what to change.</li><li>Pick a title and a thumbnail (options below).</li>
<li>After approval: upload it as a normal episode, then switch the daily pipeline to this format (gate 3).</li></ol></div>
<h2>Thumbnails</h2><div class="thumbs">
<figure><img src="../thumbs/thumb_A.png"><figcaption>A: smug Doug, giant shark rising</figcaption></figure>
<figure><img src="../thumbs/thumb_B.png"><figcaption>B: DAY 1 vs DAY 12 growth split</figcaption></figure>
<figure><img src="../thumbs/thumb_C.png"><figcaption>C: the baby, with Tanner filming</figcaption></figure></div>
<div class="card"><figure style="margin:0"><img src="../thumbs/sheet.jpg" style="width:100%;border-radius:10px">
<figcaption>Bottom row: how they look at phone size</figcaption></figure></div>
<h2>Titles, description and tags</h2><div class="card">{md(read("packaging.md"))}</div>
<h2>Checks</h2><div class="card"><table>{qc_rows}</table></div>
<details class="card"><summary>Independent review of the video</summary>{md(read("video_review.md"))}</details>
<details class="card"><summary>Fact and policy screen of the script</summary>{md(read("script_review.md"))}</details>
<details class="card"><summary>Full script</summary>{md(read("script.md"))}</details>
<details class="card"><summary>Facts and sources</summary>{md(read("facts.md"))}</details>
</main></body></html>"""
(out / "index.html").write_text(page, encoding="utf-8")
print("review/index.html written")
