# 010-every-venom: visual screen, post-render (round 1)

Inputs checked: `build/samples/f_001-f_032.png` (one frame every 30 s starting at 15 s, mapped to shots via
`build/timing.json`), `build/qc.json` (961.6 s, `problems: []`), extra frames pulled from `build/final.mp4` for the
outro (s279-s286) and s040, `build/thumbnail.png`, `build/thumbnail_small.png`, `metadata.json`, and
`build/shorts/short01-03_preview.png` plus 9 frames from each Short mp4 (1080x1920, 60 fps).

## Main video

No black or blank frames, no frozen shots, no render glitches in the 32 samples. Every sample matches its narration
(for example f_001 s006 "spare parts" labels, f_015 s130 one bed in ten, f_020 s176 the mamba's black mouth, f_030
s265 the 3 m tentacle next to a basketball hoop). Doug is on-model everywhere. The red cap reads on all backgrounds.
Ghost Doug (s286) and the sunburn gear (s226-s231) are intended variants. The death counter climbs correctly,
84 to 93. Nothing gory: the deaths are an X-eyed Doug, a floating cap and an empty field guide. The tone is adult
and deadpan, not a kids' show. Lots of variety: no run of 4 or more near-identical compositions. There are no
burned-in subtitles on the main video, and `captions.srt` carries "Sateré-Mawé" correctly as UTF-8, which closes
the carried-over item.

### Required fix

1. **s286, the final CTA shot, 957.3-961.6 s (director; optional engine fix by the art director).** The "friend?"
   speech bubble's tail is broken. The engine always anchors the tail on the bubble's lower-left. With
   `tail: [1300, 400]` the tip sits to the right and only 14 px below that anchor, so the tail renders as a
   hairline black sliver along the bubble's bottom edge. It stops about 150 px short of ghost Doug and looks like
   a stray line. Every other bubble in the episode points down-left and renders fine.
   Change: move the bubble to Doug's right so the tail points down-left at his head:
   `{"type": "speech", "text": "friend?", "x": 1650, "y": 290, "w": 260, "h": 120, "tail": [1495, 370], ...}`.
   This keeps it clear of the DOUG DEATHS label, which ends about y 195. Alternatively, move Doug to the right
   of the bubble's tail anchor. Engine option (art director): in `studio/paint.py` (speech, about line 499),
   mirror the tail base to the right side when `tail.x > x`, so right-pointing tails stop collapsing.
   Re-render s286 and the final.

### Minor (do not block)

A. **s284 (director):** the platypus "bandage" (3 beige squares) overlaps the bottom of the "MAYBE" text on the
   platypus card. It is still readable, but moving it down about 15 px to the card's bottom edge, or onto the
   PLATYPUS label, would look cleaner.
B. **s250 (director):** the lowercase "not fear" bubble is a slightly odd fragment. It works once CERTAIN
   appears. Optional.

## Thumbnail

`thumbnail.png` (1280x720) and `thumbnail_small.png` match the brief. Platypus is the joke tile at top-left and
the box jellyfish sits alone on the darkest tile at bottom-right. Doug's face gets worse tile by tile. The labels
are animal names only, and "Blue-Ringed Octopus" now fits. At feed size the red caps, the octopus, the hornet, the
mamba and the jellyfish all read. It complements "How Every Deadly Venom Would Kill Doug" and is not misleading.
No wounds or blood. **PASS.**

## Shorts

- **short01** (48.75 s): the title is readable and outlined. The octopus, Doug and the labels sit inside the 9:16
  frame. The subtitles are large and legible. The end card "WHAT DID DOUG DO? TAP BELOW" has a red arrow pointing
  straight down. Minor: on the opening frame, the shoreline line runs just under the red BLUE-RINGED OCTOPUS
  wordart. It is still legible.
- **short02** (54.36 s): the title is readable. The snake, terrarium and field guide are not cut off. The subtitles
  are legible. The end card "ALL 12 VENOMS: TAP BELOW" has a down arrow.
- **short03** (54.80 s): the title is readable on the dark background. The jellyfish, Australia map and labels are
  all inside the frame. The subtitles are legible. The end card "WHAT HAPPENS NEXT? TAP BELOW" has a down arrow.
  Minor: in the opening shots (s257-s258), swimming Doug's trailing arm touches the left edge, about x 10 of
  1080. It is not a readability problem.
- s286, the bug above, is not part of any Short.

## Verdicts

VERDICT (main): FAIL. 1 fix: s286, bubble tail (director, or engine fix by the art director).
VERDICT (shorts): PASS

# Post-render, round 2

Inputs checked: re-rendered `build/final.mp4` (03:10 UTC), with s286 frames pulled at 958.0, 959.5 and 961.0 s (the shot starts at 957.26 s in `build/timing.json`), plus `build/samples/f_001-f_032.png`, `build/qc.json` (961.6 s, `problems: []`), `build/thumbnail.png`, `metadata.json`, `build/shorts/short01-03_preview.png`, and 5 frames from each Short mp4.

## s286 re-render

- **Tail: fixed.** The bubble now sits up and to the right of ghost Doug. The tail is a clear wedge pointing down-left at his cap. It reads as a tail. There is a tiny stray notch or dot where the tail's right base meets the bubble outline (about x 1560, y 298). It is only visible when zoomed in, so it does not block.
- **Clearance: not fixed.** The bubble is `y 250, h 110`, so its top edge is at y 195. The DOUG DEATHS: 93 box has its bottom border at y 193-195. In the frame, the bubble outline starts at y 196, directly under the label border across x 1540-1600. There is 0 px of gap, so the two outlines merge into one line and the bubble looks like it hangs from the counter box.

### Required fix (main)

1. **s286 (director):** in the speech element, change `"y": 250, "h": 110, "tail": [1510, 316]` to `"y": 262, "h": 100, "tail": [1505, 326]`. The bubble then runs from y 212 to y 312, which leaves about 16 px of sky under the label, and the tail tip lands just right of the cap dome without touching it. Keep x, w and the text as they are. Re-render s286 and the final. The Shorts are not affected.

## Rest of the main video

The 32 samples match round 1: no black, frozen or glitched frames. Doug is on-model, the counter steps correctly from 84 to 93, nothing is gory, and nothing reads as a kids' show. No regressions.

## Thumbnail

Unchanged since the round 1 pass. It works with "How Every Deadly Venom Would Kill Doug". PASS.

## Shorts

These are the same files as round 1. All three titles are readable, nothing is cut off at the sides, the subtitles are legible, and every end card ("WHAT DID DOUG DO? / ALL 12 VENOMS / WHAT HAPPENS NEXT? TAP BELOW") has a red arrow pointing down. s286 is not in any Short. PASS.

VERDICT (main): FAIL
VERDICT (shorts): PASS
