# 045 Visual review

## Round 1: keyframes (2026-11-12, visual screener)

Screened: shotlist.json (206 shots + endslate), build/contact/sheet_01..18.png, full-size keyframes for s001, s028, s029,
s091, s094, s137, s172.

VERDICT: FAIL

Overall the episode is in good shape. Doug is on-model in every shot (red cap, white head, readable on all backgrounds,
including the dark death cards). The counter runs 343 to 350 with seven deaths in the scripted places. WARNINGS LEFT
goes 3, 2, 1, 0 at the right chapters. Spelling is clean, the chapter tabs are consistent and there is no nursery tone.
Most drawings read well: mound, eagle, honey badger, jackal, monitor, mouse, umbrella hoods, Africa map, library.
Six shots must change before the render.

### Required fixes
1. **s091 (illustrator)**: the `black_mamba_gape` silhouette reads as a black desk lamp, not a snake. The head is a
   lampshade cone, there is no eye and no mouth interior. Redraw it as a recognisable mamba: green/grey body with a pale
   belly, a visible eye, and the mouth opened wide with the inky-black interior shown as a contrast area inside a light
   outline. The black interior is the fact being shown. If the silhouette treatment is kept, add a white eye and a
   light-outlined open jaw so the shape says "open mouth". Also check s125 and s137, which use the same black silhouette.
2. **s137 (director / art director)**: the red speckled spray-glow sits on the ground around the snake's coils and reads
   as a blood spray or pool next to a screaming Doug. Change the glow to yellow/white "impact" lines, or move it behind
   the raised head (sky area) in a non-red colour. Nothing red should spread on the ground.
3. **s172 (director)**: the red X is on a pill bottle labelled MORPHINE, under "NOT A MEDICINE". That says morphine is
   not a medicine. Move the X to a blank pharmacy bottle (or one labelled MAMBALGIN) and keep the morphine bottle out of
   the shot. Also use the same brown morphine bottle as s159/s160/s168/s171, not a new orange Rx bottle.
4. **s028 / s029 / s027 (director)**: text sits on top of the drawings. In s028, the "FRONT DOOR" wordart covers the mound
   peak. Move it to y ≈ 160 or to the left sky (x ≈ 400). In s029, the red "THE HOME" title covers the coiled snake on
   the mound top. Move the title to y ≈ 250, or the mound/snake right and down. In s027, the "NEITHER DID IT" label
   overlaps the mound peak. Lift it about 60 px or move it left of the mound.
5. **s100 (director)**: once the list is wiped, the orphaned card reads "6 STRIKE", which looks like a typo. Change it
   to "6. STRIKE", or just "STRIKE".
6. **s095 (director)**: the narration is "Doug has seen the inside of this mouth before" (the 010 callback), but the
   snake's mouth is closed (`black_mamba_hood`). Use `black_mamba_hood_gape` so the mouth interior is on screen. The
   "EPISODE 10" tag is fine.

### Advisory (fix if cheap)
7. **s143-s149 (director)**: seven shots in a row use the same nerve-to-muscle diagram. Only overlays change. The
   doorbell metaphor at s148/s149 is never drawn: the "doorbell" is a yellow blob on the synapse. Cut s148/s149 to an
   actual doorbell button (s148: glue tube, button pressed flat; s149: a ringer/bell with its plug pulled out) to break
   up the run and make the analogy land.
8. **s198 (illustrator)**: the banknotes are green and look like US dollars, but the line is "128 euros". Use
   euro-coloured notes (blue/orange) or add a € mark.
9. **s179 (director)**: Doug is drawn over the closed door while the open doorway sits empty beside him. Put him in the
   open doorway, walking out.
10. **s062 (director)**: Doug stands tiny on the horizon line, mid-frame, and looks like he is floating. Drop him to
    ground level (y ≈ 900) at normal scale, or remove him. He isn't needed for the predator queue.
11. **s085 (director)**: Doug is tiny and jammed into the bottom-left corner (feet about 10 px from the frame edge).
    Move him up and in (x ≈ 160, y ≈ 900) at the normal 0.4 scale.

### Checked, no change
- Death cards (s026, s048, s090, s112, s134, s157, s202): X eyes, ghost Doug, cap-off gag. Cartoon only, no gore.
- The tiny field-guide prop on death cards can't be read at that size. That's acceptable because s044 and s205 show
  it full size.
- s178 narrator hand enters from the side edge and stays clear of the counter and the tab. It follows the art bible.
- s182-s185 sober text cards without Doug or counter are appropriate.
- s001 (the thumbnail as the opening image): the wordart touches the mound top by design. Readable, one focal arrow.
- Variety outside s143-s149 is fine. No other run of 4 or more near-identical compositions.

## Round 2: keyframe fixes + thumbnails (2026-11-12, visual screener)

Screened at full size: s027, s028, s029, s091, s095, s100, s137, s172; grid view: s062, s085, s143-s149, s179, s198.
Thumbnails: build/thumbnail.png, thumbnail_b.png, thumbnail_c.png and their 168x94 `_small` versions.

VERDICT: PASS

### Round 1 fixes, verified
1. s091: fixed. The mamba now has a white eye, fangs and a wide-open jaw with a light outline around the black interior. It reads as an open snake mouth, not a lamp.
2. s137: fixed. Yellow impact lines sit around the raised head in the sky. There is no red on the ground.
3. s172: fixed. The red X is on a MAMBALGIN vial under "NOT A MEDICINE". The morphine bottle is gone.
4. s027 / s028 / s029: fixed. "NEITHER DID IT" sits above the mound, "FRONT DOOR" is in the left sky, and "THE HOME" is clear of the snake on the mound top.
5. s100: fixed. The card now reads "6. STRIKE".
6. s095: fixed. The snake's mouth is open and the EPISODE 10 arrow points to it.
7. s143-s149: fixed. s148 cuts to a glued doorbell panel with a glue tube, and s149 shows a bell with a STOP box and an UNPLUGGED plug. This breaks up the diagram run.
8. s198: fixed. The notes are euro notes (50 and 20 with the € mark) under "~128 EUROS".
9. s179: fixed. Doug walks out through the open doorway.
10. s062: fixed. Doug stands on the ground at the end of the predator queue.
11. s085: fixed. Doug is in from the corner, at ground level and at normal scale.

### Thumbnails (feed size, 168x94)
- A, "IT'S GOING HOME" (main title): readable. The large snake and the arrow to the mound hole give one clear focal path. Doug in the doorway is tiny at feed size (a red dot with a face), but the brief asks for that and the arrow carries it. It matches the title's twist without spoiling it.
- B, "DOUG IGNORED THEM" (Warns You Three Times): readable. The crossed-out tally of 3 plus the open-mouthed mamba next to Doug make the threat obvious. Doug's sweat-drop smile reads as ironic, not cutesy. The bottom text touches the snake's tail. That's minor and needs no change.
- C, "FLAT TYRE" (A Day's Ride From Help): readable. The bike and Doug are the focal point and the snake is on the left. The hospital is too small to read at 168 px, but the dashed route still implies distance. Advisory only: the black-with-red-outline mamba is styled differently from the green mamba in A and B.
- Policy: no blood, bite wounds or gore. Not kid-coded. None of the three is misleading against its paired title.

## Round 3: revised thumbnails A and C (2026-11-12, visual screener)

Checked build/thumbnail.png, thumbnail_c.png and their 168x94 `_small` versions against the creative director's package notes (decisions.md, 2026-11-12).

VERDICT: PASS

### A, "IT'S GOING HOME" / "Every Reason the Black Mamba Is Africa's Scariest Snake"
- CD fix 1 (Doug about 0.65 in the doorway): done. Doug stands in front of the mound hole with his shock face. At 168x94 the red cap and white face with the open mouth are clearly visible. Text clears Doug's cap.
- CD fix 2 (threat): done. The `black_mamba_hood_gape` head is now the largest element, with an inky open mouth, white eye and small fangs, and it aims at Doug/the mound rather than at empty sky. At feed size it reads as a snake about to strike, which carries "scariest". There is no drip, blood or wound.
- CD fix 3: the arrow (snake -> hole), the text and the sun are all kept. The focal path is head -> arrow -> Doug in the doorway.
- Advisory (youtube-titler, internal only): `metadata.json` `thumbnail_brief` still says "mouth closed, narrow hood". Update it to match the approved gape version.

### C, "FLAT TIRE" / "Why Black Mamba Bites Are Deadliest a Day's Ride From Help"
- CD fix 1: the text reads "FLAT TIRE" (en-US). It's readable at 168x94.
- CD fix 2: the mamba is the green unsilhouetted reared drawing, so it now matches A and B.
- CD fix 3: the hospital block is replaced by a thatched hut with a large red-cross sign at the far end of the dashed route. The red cross reads at feed size, and so does the idea of distance.
- CD fix 4: no bite is shown. The bike, the flat front tyre and shocked Doug are the focal point, with the snake rearing beside them as the threat.
- Policy: no gore and no kid-coding. Not misleading against the paired title.

## Round 4: post-render (2026-11-12, visual screener)

I checked build/samples f_001-f_023 (final.mp4, 684.2 s), build/qc.json (no problems), the three thumbnails with their 168x94 `_small` versions, metadata.json, the three Shorts previews, and 8 frames from each Short (spread through the clip plus the last 3 s). I also pulled extra full-resolution frames around s003, s014, s028, s057, s083-s089, s174 and s200-endslate.

VERDICT (main): PASS
VERDICT (shorts): PASS

### Main video
- No black or blank frames, no frozen shots and no garbled drawings. The chapter cards match the description timestamps (THE SPEED through THE LONG RIDE). The DOUG DEATHS counter steps 343 -> 350 in order, and WARNINGS LEFT goes 3 -> 2 -> 1 -> 0, green to red.
- Round 1 fixes I saw in the final render: the s085 HEAD UP / MOUTH / HOOD row and the s173 hospital with a red X. I did not pull frames for s091, s172 or s179 in this round.
- Doug is on-model (red cap, white head) and readable in every sampled frame. The only deaths are cartoon ones (X-eyes, floating), with no blood or wounds. Nothing reads as a kids' show.
- The ending is clean. s200-s206 recap the warnings (boot, umbrella, stick), and the notebook payoff reads "LET IT LEAVE." with DOUG DEATHS: 350. The endslate is the standard "DOUG'S NEXT DEATH" end-screen with video and subscribe slots. There is no withheld payoff and no "???" card.
- Non-blocking, so only apply it if anything else forces a re-render:
  1. (director) s083 "Here's the twist.": the `zoom_in` camera (x 900, y 680, zoom 1.08) pushes the scene-drawn HUD past the right edge in the last ~0.5 s. "DOUG DEATHS: 345" gets clipped to "DOUG DEATHS: 34" (visible in sample f_009). Fix: set camera x to 1020, or zoom to 1.04.
  2. (art director, engine) The HUD labels are scene elements, so every zoom shot (s003, s014, s028, s057, s083, s089) makes the counter drift and grow. Consider drawing the HUD as a screen-fixed overlay after the camera transform.

### Thumbnails
- The files are unchanged since the round 3 PASS (A "IT'S GOING HOME", B "DOUG IGNORED THEM", C "FLAT TIRE"). All three are readable at 168x94, each has one focal path, Doug and the mamba are obvious, and none is misleading against its paired title in `packaging.variants`. There is no gore.
- Advisory, still open from round 3 (youtube-titler): `metadata.json` `thumbnail_brief` and `packaging.candidates[0].concept` / `variants[0].thumb_idea` still say "mouth closed, narrow hood". The approved A shows an open gape with small fangs, so update the text to match.

### Shorts
- short01 (s051-s059, 30.9 s), "This Bird Hunts Black Mambas Longer Than a Bed": the title is readable and the eagle, snake, Doug and bed all stay inside the 1080 crop. The payoff (eagle carrying the snake past the bed) is shown before the end card.
- short02 (s160-s175, 58.7 s), "Black Mamba Venom Hides a Painkiller as Strong as Morphine": the MAMBALGIN = MORPHINE vial/bottle, the mice, NOT TOXIC and MICE ONLY are all legible. The s174 nerve diagram, "+" and the PAIN DOWN meter fit inside the crop. The payoff and the "mice only" caveat are both delivered.
- short03 (s072-s078, 24.5 s), "A Black Mamba Can Strike Up to a Meter High": the reared mamba next to the 1 M kitchen counter pays off the title.
- On all three, subtitles are large, white with an outline, and legible. The HUD is small but secondary. The end card reads "FULL VIDEO: TAP BELOW", and Doug points to a red arrow that points straight down. There is no teaser card.
