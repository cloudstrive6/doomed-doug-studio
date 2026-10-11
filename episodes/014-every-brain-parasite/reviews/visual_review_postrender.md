# 014-every-brain-parasite: post-render visual review (2026-10-11)

What I checked: the 29 samples in `build/samples/`, plus my own grabs from `build/final.mp4` (opening at 0.1, 1 and
3 s; every zoom-in shot at 75% and at the end of its move; s243-s254). I ran ffmpeg blackdetect (d 0.1) and
freezedetect (8 s) over the whole video, viewed `build/thumbnail.png` and `build/thumbnail_small.png`, read
`metadata.json`, and looked at the three Shorts: each preview, 12 frames per Short, a 2 fps sheet of short01's first
20 s, and full-res crops wherever something looked tight. Nothing was rendered. QC: no problems, 871.4 s.

VERDICT (main): FAIL
VERDICT (shorts): FAIL

## Blocking
1. **The zoom-ins on s014 and s024 crop the death counter (director).** It's the same fault as 013. `s014`
   (`zoom_in` x 700, zoom 1.08) and `s024` (`zoom_in` x 520, zoom 1.08) push the camera window left. By the end of
   each move the right edge of the frame sits around x 1777, but the "DOUG DEATHS: 114" label at x 1590 runs out to
   about x 1815. So the label loses its last digit ("DOUG DEATHS: 11"). The same crop plays in **short01** at about
   15.0-15.4 s, because camera-move shots use the full-width window there. **Fix:** set `camera.x` to 960 in both
   shots and leave `y` and `zoom` alone. The window then spans x 71-1849, so the labels fit and Doug (x 600 / x 420)
   stays in frame. Once both shots are re-rendered, short01 needs a re-render too.

## Advisory (do not block)
2. **s250 (director):** the red arrow (`to [1008,768]`, head 40) ends right on Doug's raised hand and the two red
   scratch strokes. At the end of the zoom, the arrowhead, scratch and thumb merge into one red blob at the hand.
   It's cartoonish, not gory, but it reads more cleanly if you change the arrow's `to` to `[1040,740]`, so the head
   stops short of the hand and the scratch stays visible as its own mark.
3. **s249, short03 only (director):** "WONDERFUL AFTERNOON" (wordart x 900, y 300, appears at 0.617) isn't counted
   in the Short's auto-fit window, because that window is measured at t 0. It lands about 18 px from the left crop
   edge and its right end almost touches "BRAIN: EATEN". Moving it to `x 1000, y 400` clears both. The main video
   is fine as it is.
4. **s244 / s245, short03 only (director):** "WORM: 7 OF 7" (s244, appears late) and `worm_icon` (s245, x 400) both
   sit about 20-40 px from the left edge of the Short. Nothing is cut, but it's tight. If the director is touching
   the shotlist anyway: move the s244 label to x 760 and the s245 `worm_icon` to x 560.
5. The short03 title renders without the black outline that short01 and short02 have (plain red on near-black). It
   reads fine at phone size. This is an engine/style detail for the art director, not a fix needed for this
   episode.

## Checked and OK
- **Black/frozen:** blackdetect and freezedetect find nothing. The Balamuthia act is near-black by design, and the
  HUD and drawings stay on screen throughout.
- **Opening:** the 0.1 s and 1 s frames are the thumbnail grid (s001), so the click lands on what the thumbnail
  promised. At 3 s it cuts to the head outline and Doug.
- **Other zooms:** s003, s010, s040, s044, s069 (counter right edge about x 1906, tight but whole), s071, s081, s099,
  s120, s130, s136, s181, s208, s235, s239, s250 and s254 keep the whole HUD in frame.
- **Doug:** on-model in every frame I checked (red cap, white head; white body on the dark Balamuthia and
  Halicephalobus grounds). The costumes (killifish, ant, sheep) keep the cap and face readable. The costume pile at
  the rat lungworm transition reads clearly.
- **Gore/tone:** nothing graphic. Parasites are pink cartoon worms and cysts are pale circles. The heads are plain
  grey outlines with no anatomy. The deaths are a gravestone ("RIP DOUG", s253) and the cap on an empty flowerpot
  (s254). No nursery tone.
- **Text:** all chapter tags, HUD labels and wordart are spelled correctly and legible (Halicephalobus, Gnathostoma,
  Spirometra, Balamuthia mandrillaris, "2.5 TO 8 MILLION", "5-6 cm"). Nothing overlaps a drawing.
- **Thumbnail:** a 3x3 item grid shading from pond green to near-black, matching `thumbnail_brief`. Labels are item
  names only, and there are no title words, brains or scans. At 320x180, Doug's red caps and the progression read
  clearly and the labels are still mostly legible. It suits "What Dying From Every Brain Parasite Would Feel Like"
  and isn't misleading (all nine items appear in the video, in this order). The lancet-fluke ant is clipped by the
  top of its tile, which is acceptable.
- **Shorts:** titles are readable on all three. The end cards ("WHAT HAPPENS NEXT? TAP BELOW" and "SEE ALL 9
  PARASITES. TAP BELOW") have a red arrow pointing straight down, with Doug beside it. Subtitles are large,
  outlined and legible. Apart from items 1, 3 and 4 above, no drawing is cut off at the sides. Brief two-Doug
  frames at shot boundaries in short03 are crossfades, not duplicates.

## Required fixes (shotlist only)
| # | Shot | Change | Owner |
|---|---|---|---|
| 1 | s014 | `camera.x` 700 -> 960 | director |
| 1 | s024 | `camera.x` 520 -> 960 | director |

After re-rendering, re-run final, qc and short01. Items 2-4 are optional polish.

---

# Round 2: post-render re-check (2026-10-11)

What I checked: the re-render from 21:41 (`final.mp4`, the samples, the thumbnails and all three Shorts are newer
than commit 5c144b5). The shotlist now has `camera.x` 960 on s014 and s024. I pulled frames from `final.mp4` at
39.3, 39.7, 40.05 and 40.13 s (the end of s014's zoom) and at 73.4, 74.6, 75.8 and 75.93 s (the end of s024's zoom).
I also viewed all 29 samples, `build/qc.json` (no problems, 871.4 s), `thumbnail.png` and `thumbnail_small.png` and
`metadata.json`. For the Shorts I viewed each preview, 12 frames from each Short, and short01 at 14.6-15.8 s, where
s014 plays. I re-ran blackdetect and freezedetect over the whole video. Nothing was rendered.

VERDICT (main): PASS
VERDICT (shorts): PASS

## Round 1 blocker: fixed
1. **s014 / s024 death counter:** fixed. At the end of both zooms the full label "DOUG DEATHS: 114" sits inside
   the frame, with its box ending around x 1880 of 1920. "BRAIN: STEERED" under it is also whole. Doug (stick at
   x ~575 in s014, killifish costume at x ~400 in s024) and the chapter tag stay in frame, and the cap and face read
   clearly.
2. **short01:** fixed. From 14.6 to 15.8 s the counter shows "DOUG DEATHS: 114" with nothing cut off. s024 is not in
   short01 (its range is s012-s020), so only s014 needed checking there.

## Re-checked and OK
- **Samples (29):** the HUD is whole in every frame. The counter climbs 114 to 120 in chapter order, and the
  BRAIN meter reads STEERED, then OCCUPIED, then EATEN. There are no black, blank or glitched frames. Doug is on-model
  throughout, and the parasites are cartoon drawings with no gore.
- **Black/frozen:** see the line at the end.
- **Thumbnail:** unchanged from round 1 and still a pass. At 320x180 the 3x3 grid, Doug's red caps and the dark
  progression read clearly, and the tile labels are still mostly legible. It suits the title and isn't misleading.
- **Shorts:** the titles are readable. The end cards have the red arrow pointing straight down, next to Doug.
  Subtitles are large and outlined. No drawing is cut off at the sides; short03 has the same tight but whole left
  margin noted in round 1.

## Still open (advisory, does not block)
- Round 1 items 2-5 (the s250 arrow on the hand; short03's "WONDERFUL AFTERNOON" position, s244/s245 margins and
  missing title outline) are unchanged. They are optional polish (director / art director).
- New, minor (editor/engine): the short01 preview frame shows the subtitle mid-word ("...near the surf"). This is
  just the word-by-word subtitle reveal caught partway through a word, and playback is fine. If a cleaner preview is
  wanted, take it at the end of a caption line.

No required fixes.
- **Black/frozen (round 2 run):** blackdetect (d 0.1, pix_th 0.05) and freezedetect (8 s) over the whole of `final.mp4` found nothing.
