# Scene & shotlist format (MS Paint engine)

Everything visual in Doomed Doug is drawn by `studio/paint.py` from JSON. No image generators: this keeps Doug
identical in every video, costs $0, runs on any cloud machine, and looks like MS Paint on purpose
(aliased edges, flat fills, bucket fills, spray-can glow, hand-drawn wobble).

## shotlist.json

```json
{
  "episode": "001-ocean-layers",
  "shots": [
    {
      "id": "s001",                         // unique, zero-padded, in order
      "chapter": "Sunlight Zone",           // first shot of each item: chapter + caption bar text
      "topbar": true,                       // false hides the caption bar; a string overrides it
      "scene_ref": "thumbnail",             // instead of "scene": reuse episodes/<id>/thumbnail.json (opening shot)
      "narration": "This is Doug.",         // the exact words spoken during this shot (<= 45 words)
      "scene": { "background": "#8fd3ff", "size": [1920, 1080], "elements": [ ... ] },
      "camera": {"move": "zoom_in", "x": 960, "y": 540, "zoom": 1.2},   // optional
      "boil": true,                         // default true: 3 wobble drawings looping at 8 fps
      "hold": 0.0,                          // extra seconds after the line (let a joke land)
      "pause_after": 0.12,                  // silence after the line (default from config)
      "min_duration": 0.8
    }
  ]
}
```

Shot duration = TTS length of `narration` + `pause_after` + `hold`. The picture changes when the shot changes, so
**one shot per beat**, and within a shot use `appear` so something new arrives **at least every 5 s** (target ~3 s).
QC fails any static stretch over 6 s.

### Camera (`camera`)
| move | effect |
|---|---|
| (none) / `static` | fixed. If `scene.size` is bigger than 1920x1080 the whole canvas is fitted |
| `zoom_in` / `zoom_out` | toward/away from `x`,`y` to `zoom` (1.1–1.4 is plenty) |
| `pan_down` / `pan_up` / `pan_right` | scroll a tall/wide canvas (e.g. `size: [1920, 4320]` for ocean depth) |
| `shake` | panic / impact |
| `{"from": [cx, cy, zoom], "to": [cx, cy, zoom], "ease": "smooth"}` | custom |

Keep text and key action inside the central 80% when zooming, or it gets cropped.

## Elements

Coordinates are canvas pixels (origin top-left, y down). Draw order = list order (later is on top).
Common keys: `color` (outline, default `#000000`), `fill`, `width` (line px, default 4),
`appear` (fraction 0–1 of the shot when the element pops in, for reveals timed to the narration),
`boil`/`wobble` multipliers (0 = rock steady, e.g. text).

| type | keys |
|---|---|
| `doug` | `x`,`y` (hips), `scale` (1 ≈ 450 px tall), `pose` (or list to loop), `expression` (or list), `gear` [`scuba`,`mask`,`tank`,`helmet`,`sweat`,`sunburn`], `facing` `right`/`left`, `rotate` (deg; lying dead = `pose: lie, rotate: -90`), `ink` (auto-white on dark backgrounds) |
| `asset` | `name` (file in `assets/library/`), `x`,`y`, `scale`, `flip`, `rotate` |
| `line` / `curve` | `points` [[x,y],...]; curve is smoothed |
| `arrow` | `from`, `to`, `head` |
| `poly` | `points`, `fill`, `smooth` |
| `circle` / `ellipse` | `x`,`y`,`r` or `rx`,`ry`, `fill`; `start`/`end` degrees for an arc |
| `rect` | `x`,`y`,`w`,`h`, `fill` |
| `fill` | `x`,`y`, `color`: MS Paint bucket fill at a point (after outlines exist) |
| `spray` | `x`,`y`,`r`,`color`,`density`: airbrush dots (glow, blood mist, bubbles, dust) |
| `text` | `text`,`x`,`y` (center), `size`, `color`, `outline`,`outline_width`, `max_width`, `align` |
| `label` | text in a white box (depth markers, names, numbers) |
| `speech` | speech bubble: `x`,`y`,`w`,`h`,`text`,`tail` [x,y] |
| `bands` | horizontal colour bands: `bands` [{`y0`,`y1`,`color`}] (sky/sea/depth layers) |
| `group` | `elements` with its own `x`,`y`,`scale`,`rotate`,`flip` |
| `wordart` | keyword label: `text`,`x`,`y`,`size`, yellow→green gradient + dark outline (`top`,`bottom`,`outline` colours) |
| `tile` | thumbnail/intro grid tile: `x`,`y`,`w`,`h`, `fill`, `asset` + `asset_scale` (or `elements`), `label` (comic font, under the tile); contents are clipped to the rounded frame |
| `image` | real photo inset: `file` in `assets/photos/` (must be listed with source + licence in `assets/photos/SOURCES.md`; public domain / CC0 / CC-BY only), `x`,`y`,`w`; 4 px black frame |

Extra keys: `line`/`curve` take `dash: [on, off]` (dotted distance lines); `arrow` takes `bend` (px, curved red
arrows) and draws a filled head; `asset` takes `"silhouette": true` (+ `glow` colour, `glow_r`) for the black
silhouette-with-red-glow reveal. `asset` also takes `ink` (outline colour override for black lines); assets whose JSON has
`"auto_ink": true` (crude-tier humans) switch black outlines to white on dark backgrounds automatically, except
elements marked `"keep_ink": true`.

Annotation assets in the library: `question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`, `thermometer`,
`gravestone`.

**Caption bar:** the renderer automatically draws the current item name (ALL CAPS, comic font, thin white strip,
top centre) on every frame from the shot with that `chapter` until the next one.

Doug poses: stand, wave, point, arms_up, panic1, panic2, shrug, think, hands_hips, walk1, walk2, run1, run2,
swim1, swim2, float, sit, fall, cower, lie, dive. Loop pairs for GIF-like motion: `["walk1","walk2"]`,
`["run1","run2"]`, `["swim1","swim2"]`, `["panic1","panic2"]`.
Expressions (style bible set first): shock (open mouth + pink tongue), gritted (teeth grid), flat (unimpressed),
hopeful, dead (X eyes), smirk, sad, angry, confused, sleepy, neutral. Old names still work as aliases.
`"ghost": true` draws ghost Doug (grey, wavy tail) for death beats.

## Asset library (`assets/library/<name>.json`)

Reusable drawings (creatures, props, places). Draw each once, reuse forever:

```json
{"name": "anglerfish", "description": "...", "anchor": [0, 0], "tags": ["deep sea"],
 "elements": [ ...same element types, local coords centred on (0,0), ~300-500 units wide, facing right... ]}
```
Preview: `python -m studio asset-preview anglerfish giant_squid`. See `assets/library/anglerfish.json` for the
house style: thick black outlines (5–6), flat fills, white eyes with black pupils, simple silhouettes that read
at thumbnail size. For creatures that live in dark scenes, use a mid-tone fill (not near-black) so the silhouette
reads against deep-sea backgrounds.

## Thumbnails & channel art
Same scene format, rendered by `python -m studio thumbnail <ep>` from `episodes/<ep>/thumbnail.json`
(`size: [1280, 720]`) or `python -m studio art scene.json out.png` (banner 2560x1440, avatar 800x800).
