"""Render watermark.json and key out the magenta background -> transparent watermark.png."""
import subprocess, sys
from pathlib import Path
from PIL import Image
here = Path(__file__).parent
subprocess.run([sys.executable, "-m", "studio", "art", str(here / "watermark.json"), str(here / "watermark_raw.png")],
               check=True, cwd=here.parent)
im = Image.open(here / "watermark_raw.png").convert("RGBA")
px = im.load()
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = px[x, y]
        if r > 240 and g < 20 and b > 240:
            px[x, y] = (0, 0, 0, 0)
im.save(here / "watermark.png")
(here / "watermark_raw.png").unlink()
