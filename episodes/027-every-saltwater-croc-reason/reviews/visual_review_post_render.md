# Visual review: post-render (2026-10-26)

Scope: `build/final.mp4` (955.6 s) via 32 samples in `build/samples/` (one frame every 30 s), `build/qc.json`, all three thumbnails plus their `_small` versions, `metadata.json` title, and the 4 Shorts (`build/shorts/*_preview.png`, plus 11 frames per mp4 including the last 8 s). Nothing was re-rendered.

## Main video: PASS

- `qc.json` reports `problems: []`. None of the 32 samples is black, blank, glitched or frozen. The topbar chapter labels and the death counter (218 to 225) move forward in the right order.
- I checked the labels that looked odd against the narration, and all of them are correct:
  - f_004 "ALLIGATOR" goes with s041/s042, "a 2012 study counted ~4,000 of them on an alligator".
  - f_009 "ITS RIVER" goes with s092, "ran from its river"; this is the possessive, so the spelling is correct.
  - f_024 "COMBAT / DISEASE / HUNGER" goes with s254, the Ramree account.
  - f_025 "EVERY YEAR" goes with s261.
- In every sample, Doug is on-model (red cap, white head) and readable against the background. There is no gore. The one death beat I saw, f_022 (an empty splash), is cartoon-safe, and nothing has a kids-show tone.
- f_032 is the end screen. The empty dark panel is the end-screen video slot, which is expected.
- Minor, not blocking: on f_013 the "CAIRNS" label box sits on the coastline. It is still legible.

## Thumbnails: PASS (as in Round 5)

The title is "Every Reason the Saltwater Crocodile Is the Scariest Reptile". At 168x94:
- **A ("IT WAS THERE")**: Doug in the canoe and the big croc head with its yellow eye both read clearly.
- **B ("11.5 HOURS")**: Doug in the canoe with the whole croc underneath him. Still the strongest of the three.
- **C (4-tile grid)**: Skin, Size, Home and Dive are all legible.

Each has one clear focal point, none is misleading, and none shows gore. The Round 5 optional notes (A's snout running off the top-right edge, the C Dive nostril touching the border) are still optional.

## Shorts: FAIL (short01 only)

The checks below passed on all four:
- Titles are fully legible.
- Subtitles are legible.
- The drawings fit the frame.
- Doug is present and on-model.
- The end card arrow points down to the link.
- Each outro opens a question about a later beat with "Full video below."

Minor, not blocking: the `*_preview.png` stills catch subtitles mid-word ("cl", "oxyg"). The mp4 frames show whole words, so this only affects the preview capture.

| Short | Payoff | Cliffhanger | Silhouette | Result |
|---|---|---|---|---|
| short01 (face sensitivity) | yes | **answered in clip** | **not recognisable** | **FAIL** |
| short02 (411 km home) | yes | "What was in Doug's bathtub?" is not answered | clawfoot tub with a croc hump, readable | PASS |
| short03 (Cassius 110+) | yes | "Did the crocodile wake up?" is not answered (s148 is cut) | croc shape, snout and tail visible | PASS |
| short04 (11.5 h dive) | yes | "Was Doug's river really empty?" is not answered | croc shape, snout and tail visible | PASS |

### Required fixes

1. **short01 end-card question (director).** The clip itself (s050 to s052, preview frame "ONE DROP") shows a single drop of water making the alligators turn to the ripples. So "WHAT DID ONE DROP DO?" is answered before the end card. Change `end_card` in `shorts.json` so it asks about Doug's own drop, for example `"WHAT HAPPENED WHEN DOUG'S DROP FELL?"`. Keep `tease_from: s060`.
2. **short01 silhouette (director; illustrator if no existing asset works).** `tease_asset: croc_eyes_water` renders as a flat, bumpy red strip about 40 px tall, and "???" covers most of it. It reads as a log or a cloud, not a crocodile. Switch `tease_asset` to an asset with a recognisable croc outline. Either `croc_eyeshine` (if its eyes-and-head outline reads as a croc in silhouette) or a croc head/snout asset seen side-on. Then check the end-card frame again. Re-render short01 only.

VERDICT (main): PASS
VERDICT (shorts): FAIL

---

# Round 2 (2026-10-26): Shorts re-render after the short01 fixes

Scope: all 4 re-rendered Shorts in `build/shorts/*.mp4`. For each I pulled frames at 0.5 s and 1.5 s and at 8, 6, 4, 2.5, 1 and 0.3 s before the end, plus a full-resolution last frame of short01. I also re-checked the 32 `build/samples/*.png` and `qc.json`. `final.mp4` and the thumbnails have the same timestamps as in Round 1 (19:34), so the main video has not changed. Nothing was rendered.

## Main video: PASS (unchanged from Round 1)

- `qc.json` still reports `problems: []`.
- The 32 samples match Round 1: no black, blank or frozen frames, the death counter goes up in order from 218 to 225, Doug is on-model, and there is no gore.
- The thumbnails are unchanged and still pass.

## Shorts: PASS

| Short | Payoff | Cliffhanger | Silhouette | Result |
|---|---|---|---|---|
| short01 (face sensitivity) | yes | "WHAT HAPPENED WHEN DOUG'S DROP FELL?" is not answered | open croc jaws, readable | PASS (fixed) |
| short02 (411 km home) | yes | unchanged, not answered | tub with croc hump | PASS |
| short03 (Cassius 110+) | yes | unchanged, not answered | croc profile | PASS |
| short04 (11.5 h dive) | yes | unchanged, not answered | croc profile | PASS |

**short01 fix 1 (question): verified.**
- The clip runs s045 to s057 and ends on "It can feel him."
- The new end card asks about Doug's own drop. The outro sets it up: "sat perfectly still in a canoe... One drop fell."
- The answer (s061 to s062, "One drop falls from his paddle. Doug has died. Again.") is outside the clip.
- The earlier alligator-tank drop (s050 to s052) no longer gives the answer away, because the question is now about Doug.

**short01 fix 2 (silhouette): verified.**
- `croc_jaws_open` renders as a large black silhouette with a red outline. It shows a long upper snout with a jagged tooth line, an open lower jaw and a nostril bump, so it reads as crocodile jaws in under a second.
- "???" sits inside the gape and the upper jaw, but the snout tip, teeth and lower jaw are all still visible around it.
- The red glow below and the arrow pointing down sit correctly.
- The question text, the title and "Full video below." are all legible.

**Minor, not blocking:**
- (a) On short01's silhouette, the back of the head is cut off flat on the left, which makes that end look a little boxy. Optional for the illustrator: round off the back of the skull.
- (b) The short03 and short04 silhouettes are thin profiles, and "???" covers their middle. They still read as crocs because the snout and tail are visible, the same as in Round 1.
- (c) The `*_preview.png` stills still catch subtitles mid-phrase. This only affects the preview capture.

VERDICT (main): PASS
VERDICT (shorts): PASS
