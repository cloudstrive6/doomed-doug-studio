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
**one shot per beat**: a new drawing roughly every 1.5–4 seconds of speech (follow the style bible's pacing numbers).

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
| `doug` | `x`,`y` (hips), `scale` (1 = 400 px tall), `pose` (or list to loop), `expression` (or list), `gear` [`scuba`,`mask`,`tank`,`helmet`,`sweat`], `facing` `right`/`left`, `rotate` (deg; lying dead = `pose: lie, rotate: -90`), `ink` (auto-white on dark backgrounds) |
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

Doug poses: stand, wave, point, arms_up, panic1, panic2, shrug, think, hands_hips, walk1, walk2, run1, run2,
swim1, swim2, float, sit, fall, cower, lie, dive. Loop pairs for GIF-like motion: `["walk1","walk2"]`,
`["run1","run2"]`, `["swim1","swim2"]`, `["panic1","panic2"]`.
Expressions: neutral, happy, scared, shocked, worried, dead, smug, crying, confused, angry, sleepy, determined,
screaming, nervous_smile.

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
