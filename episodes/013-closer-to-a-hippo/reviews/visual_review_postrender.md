# 013-closer-to-a-hippo: post-render visual review (2026-10-09)

What I checked: the 29 samples in `build/samples/`, plus my own grabs from `build/final.mp4` at 0.5 s, the last
frame of every zoom-in shot, and every frame from s242 to s253. I also ran ffmpeg blackdetect and freezedetect on the
whole video, viewed `build/thumbnail.png` and `build/thumbnail_small.png`, read `metadata.json`, and looked at the three
Shorts (each preview plus 9 frames, and 4 frames from the end of short03). Nothing was rendered. QC: no problems,
869.4 s.

VERDICT (main): FAIL
VERDICT (shorts): FAIL

## Blocking
1. **Zoom-in shots crop the death counter: s194, s221, s248, s249 (director).** Each `zoom_in` points right of
   centre (x 880-900, zoom 1.08-1.1). By the end of the move the camera window ends at about x 1753-1789, but the
   counter labels at x 1590 reach about x 1815. You end up seeing "DOUG DEATHS: 112" lose its last digit (s194),
   "11" (s221, s248), and "DOUG DEATHS: 1" plus "DISTANCE TO HIPPO: 0 r" (s249). s249 is the beat right before the
   114 payoff, so the counter matters most there. The fix, for all four shots, is to set `camera.x` to 960 and leave
   `y` and `zoom` alone. That keeps x 87-1833 in frame, so the labels fit. (The other option is to move the two labels
   to x 1540 in those four shots.) This also fixes short03 (see Shorts).
2. **s251: broken red arrow in the water (director).** The arrow `from [640,880] to [300,880]` (red #e0201b) is drawn
   before `field_guide_open`, so the book covers the arrowhead. What's left is a headless red streak on the river next
   to the floating cap, just after Doug dies. It reads as a stray line, and could read as a blood trail. Either
   delete the arrow, or start it at the cap (`from [600,790] to [490,840]`), put it after the field guide in
   `elements`, and make it black (#000000) or white.

## Checked and OK
- **s250 black:** blackdetect finds pure black from 858.52 to 858.78 s (0.27 s). The cap and "DOUG DEATHS: 114" fade
  in at 0.85, so it doesn't play as a dropout. Fine. The "THE MOUTH" chapter tag stays visible over the black, which
  is acceptable. No other black stretches, and no freezes of 8 s or longer.
- **Opening frame:** the 0.5 s frame is the thumbnail image (s001), so the click lands where the thumbnail promised.
- **Teeth vs Doug:** in s243 Doug stands outside the mouth, left of it. In s248, s249 and s221 he stands on the lower
  lip with clear gaps to the incisors on both sides (about 30 px at 1080p). No tooth touches him, and the death
  happens off-screen under the black.
- **Red sweat:** orange-red streaks (s114 and short01). It doesn't read as blood, and the "SUNSCREEN" label and the
  short's title make that explicit. s117 Doug is pink with the `sunburn` gear and his red cap still separates
  clearly. He's on-model.
- **Deaths:** all cartoon. Dust cloud with an X-eyed Doug (s092), a ghost Doug over the campsite and the canoe, cap
  left behind, a gravestone. No gore and no kids-show tone.
- **Doug:** on-model in every frame I looked at (red cap, white head). HUD and chapter tags are legible everywhere
  except item 1. Text is spelled correctly. No garbled drawings.
- **Variety:** good spread across scenes (charts, doors, Africa map, underwater, silhouettes, sunset). There are no
  runs of near-identical compositions in the samples.

## Thumbnail (graphic designer): passes, same as the last round
Reads at feed size: the open mouth, the tusks, Doug, the lettuce and "VEGETARIAN". It complements "Why Hippos Get
Deadlier the Closer Doug Gets" and isn't misleading. The two non-blocking nits from last round are still there:
"VEGETARIAN" sits about 10 px from the left edge (nudge it to a 24 px margin), and the horizontal incisor at about
(930-985, 570-595) reads as a stray rectangle. Fix both if the thumbnail gets touched again; neither blocks.

## Shorts
- **short03 (blocking, fixed by item 1):** s194 has a camera move, so the Short keeps the full 1920 frame. The end of
  the zoom therefore crops "DOUG DEATHS: 112" on the right at about 38-40 s. After the s194 fix, run
  `shorts render` again.
- **short01 and short02:** pass. The hook title is legible, the 16:9 drawing isn't cut off at the sides, subtitles
  are legible, and the end-card arrow points down to "TAP BELOW". The red sweat in short01 is orange-red.
- Nit (not blocking): the titles of short02 and short03 wrap to three lines, leaving a single orphan word ("Fly",
  "Doesn't"). A slightly smaller title size or a manual break would tidy it.

## Not checked
The "hipposudoric" pronunciation is an audio issue and can't be judged from frames. The editor or a listener needs to
check it at the red-sweat chapter.

## Route
Director: items 1-2 (shotlist only, no new assets). Then the editor does a final render, runs `qc` and
`shorts render` again, and the screener checks the four shot ends, s251 and short03 at 38-40 s.
