# 017 Most Disturbing Fungi: post-render visual review (2026-10-13)

Inputs checked:
- `build/samples/f_001..f_031.png`: one frame every 30 s, starting at 15 s. I matched each frame to its shot using `timing.json`.
- Full-resolution re-grabs from `final.mp4` at 1.5 s, 8.5 s, 108.0 s (s036), 165.9 s (s053) and 798.3 s (s232). I used these to check whether elements that appear late in a shot (`appear`) actually show up.
- `build/qc.json`
- `build/thumbnail.png` and `build/thumbnail_small.png`
- `metadata.json`
- `build/chapters.txt`
- `build/shorts/short01-03_preview.png`, plus 7 frames from each short (taken at 3%, 15%, 35%, 55%, 75%, 90% and 98.5% of its length).

## Main video

- **QC and specs:** `qc.json` reports 917.5 s with no problems. The video is 1920x1080 at 60 fps. There are no black, blank or frozen frames.
- **Opening:** at 1.5 s the cold open (s001) shows the same 3x3 grid as the thumbnail, so the opening image matches the package.
- **Chapters:** 11 chapters, starting at 0:00, all in increasing order. The on-screen topic labels match the chapter names: MASSOSPORA, DEATH-POSE FLY FUNGUS, THE CAVE SPIDER FUNGUS, CHYTRID, WHITE-NOSE SYNDROME, VALLEY FEVER, ERGOT, THE TOMB FUNGUS, CRYPTOCOCCUS GATTII, CANDIDA AURIS.
- **Death counter:** it climbs correctly from 139 to 146 across the segments and never goes backwards.
- **Doug:** on-model in every sample. The red cap is readable on every background, including the cicada, fly, spider, frog and bat costumes and the hard hat at s155.
- **Pictures vs narration:** every sampled picture matches its narration. Examples:
  - s007: map with 13 OR 17 YEARS
  - s044: 5 HOURS AFTER SUNSET with the fly
  - s094: 2019 STUDY with 501 SPECIES
  - s147: bar chart with TEN TIMES
  - s155: ABOUT 60%
  - s188: ASPERGILLUS FLAVUS
  - s222: B.C. circled with LARGEST REPORTED
  - s232: JAPAN pin, once it appears
- **Gore and tone:** no gore and nothing that reads as kids' TV.
- **Variety:** no stale runs among the samples.
- **Late elements:** frames that look sparse (s036 at 1.1 s, s232 at 0.7 s) are just early in the shot. The re-grabs confirm that BEFORE SUNSET, 5 HOURS, the JAPAN pin, the JAPAN label and the microscope all appear as planned.

### Defect found (blocking)

The "setting sun" half-circles render as **hollow black outlines with no fill**.

- **Cause:** `studio/paint.py` draws a circle that has `start`/`end` set as a stroke only (`cv.stroke`) and ignores `fill`.
- **Where:** 14 shots use this element (s031–s034, s036–s040, s043, s051–s054). That is the whole sunset setup of the Death-Pose Fly segment, about 30 s of screen time.
- **s051–s054 (orange sunset window):** the arc floats about 30 px above the sill with no horizon. At a glance it reads as a stray line or a doorway, not a sun, so the "sunset pose" beat loses its key prop (sample f_006, re-grab at 165.9 s).
- **s036:** the arc sits on a line, so it reads as a white dome rather than an orange sun.

## Thumbnail

- `thumbnail.png` has not changed since the round-3 PASS.
- At feed size (`thumbnail_small.png`) all 9 tiles read clearly. The White Nose bat is fully inside its tile, and every label is legible.
- The grid fits the title "The Most Disturbing Fungi Scientists Have Ever Found" and is not misleading.
- No label reuses a word from the title or the alternate titles.

No changes needed.

## Shorts (01 chytrid, 02 Northridge, 03 C. auris)

- All three are 1080x1920, running 38.8 s, 46.0 s and 37.6 s.
- **Titles:** the red title with a black outline is readable at the top of every frame. Short 02's title wraps to three lines and still clears the drawing area.
- **Framing:** no drawing is cut off at the sides. The 16:9 scenes are reframed with Doug, the counter and the key subject inside the frame (frog rows, ID cards, quake dust clouds, epidemic curve, 37°C wall, thermometer).
- **Subtitles:** white text with a black outline, legible on cream, sand, olive and blue backgrounds.
- **End cards:** all three show "WHAT HAPPENS NEXT? TAP BELOW" with a red arrow pointing straight down. The arrow sits beside Doug and does not cover anything.
- **Previews:** each `_preview.png` catches the caption in the middle of typing (for example "all the d" and "as the c"). This is an artefact of when the frame was grabbed. In the videos themselves the caption chunks are whole phrases. Advisory only.

## Required fixes (main video)

1. **s031, s032, s033, s034, s037, s038, s039, s040, s043, s051, s052, s053, s054** (director, composition)
   - Replace the element `{"type":"circle","x":1300,"y":760,"r":90,"fill":"#ffe24a",...,"start":180,"end":360}` with a filled half-disc polygon: `{"type":"poly","points":[[1210,780],[1216,746],[1234,716],[1260,694],[1300,690],[1340,694],[1366,716],[1384,746],[1390,780]],"smooth":false,"fill":"#ffe24a","color":"#000000","width":4}`. Any equivalent arc-shaped point list is fine, as long as the result is a filled half-disc.
   - Add a horizon line just in front of it: `{"type":"line","points":[[370,780],[1550,780]],"color":"#1a1a1a","width":4}`. With the line, the sun sits on the horizon instead of floating above the sill.
   - Keep each shot's existing `appear` value, if it has one.
2. **s036** (director, composition)
   - Make the same swap at x=1300, base y=660, r=110, fill `#f2a24a`, width 5, and keep `appear: 0.3`.
   - Points: `[[1190,660],[1197,619],[1218,583],[1252,557],[1300,550],[1348,557],[1382,583],[1403,619],[1410,660]]`.
   - The existing 600 px black bar stays as the horizon.

Alternative: the art director could fix the engine so that a circle with `start`/`end` and a `fill` is drawn as a filled sector. That is outside the scope of shotlist-only fixes, but it would fix all 14 shots at once.

## Advisory (not blocking)
- A8. **s232:** the microscope (x=300, scale 0.7) overlaps the left edge of the world map by about 80 px. Move it to x=170, or scale it to 0.55.
- A9. **Shorts previews:** grab the preview frame at the end of a caption chunk, so the preview text isn't cut off in the middle of a word.
- Earlier advisories A1–A7 carry forward unchanged.

VERDICT (main): FAIL
VERDICT (shorts): PASS
