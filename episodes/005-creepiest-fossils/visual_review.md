# Visual review: 005-creepiest-fossils

## Round 1: pre-render keyframes + thumbnail (2026-10-01)

Scope: all 18 contact sheets (s001-s211), zoomed keyframes s006, s021, s060, s081, s134, s145, s151, s181, s205,
plus build/thumbnail.png and build/thumbnail_small.png.

What works: Doug is on-model (red cap, white head) and readable in every shot. Chapter tags and big words are legible
and spelled right, including ZHÙR and TR'ONDËK HWËCH'IN. The death counter runs 36 to 46 with the right survivals
(Blue Babe, Zhùr) and continues from 004 (total 36). Deaths are cartoon only (ghost Doug, lone cap, RIP stone,
flat squid costume). There is no gore. The lab blood tubes (s065-s066) and the organ blobs (s176) are clinical and
fine. Nothing looks like a kids' show. The art-review fixes are in: the wolf pup has a muzzle, and the fighting
dinosaurs block reads as a fight.

VERDICT: FAIL

### Required fixes
1. **s030 (director)**: the label says "PAUL BUNYAN'S BLUE OX", but the second animal is the brown `steppe_bison`.
   The picture contradicts the joke. Recolour it blue (a blue ox, or the bison asset tinted blue), or swap it for a
   blue ox prop.
2. **s145 (director)**: a red X is drawn over the label "NO PREDATOR". That reads as a double negative ("not no
   predator"), and the X hides "PRED". Either keep the label "NO PREDATOR" with no X, or cross out a predator
   drawing/label ("PREDATOR") placed clear of the text.
3. **s134 (director / art director)**: next to Doug sits a giant realistic thumbs-up hand prop with a blue cuff.
   It is bigger than Doug's head and clearly not Doug's arm, so it looks off-model and pasted in. Remove the prop and
   give Doug a thumbs-up arm pose. If the rig has no such pose, the art director adds a stick-arm thumbs-up to
   `studio/doug.py`.
4. **s181, s182 (art director)**: in the swim pose, the snorkel floats about 60 px above and away from Doug's head,
   and the fins hang under his body instead of on his feet. Attach the snorkel to the head/mask and the fins to the
   feet in the swim pose. Same issue in **s151** (walking pose): Doug holds the snorkel in his hand and the fins lie
   on the lagoon floor. Put the fins on his feet, or remove both items for this shot.
5. **s207 (director)**: the frame is a flat brown fill with only the counter. It looks like a blank/broken frame and
   is likely to trip the blank-frame QC. Show the mudflow arriving: a dark wave edge rolling in from the left over the
   seafloor, with Doug's cap and one of the Stanleycaris eye stalks still poking out (or the lone cap on top of the
   mud).
6. **s081 (illustrator)**: the den reads as a frying pan (an oval dish with a straight handle), and the pup inside is
   only a few pixels. Redraw it as a burrow: a tunnel from the surface into a chamber, with the chamber roof visibly
   caving in (falling clods). Put `wolf_pup_mummy` clearly visible curled in the chamber, at least about 250 px wide.
7. **s011-s014 (director)**: there are 4 near-identical shots in a row (two cubs lying in the brown frozen-ground
   cross-section, Doug on the surface). With s009-s010, that makes 6 shots in the same layout. Change at least two
   of them. For example, s013 "Here's the twist." could be a close-up of Doug's shocked face with a big "!", and
   s014 could put the two ages on a horizontal timeline (Boris at 43,000+, Sparta at 28,000) instead of the
   cross-section.

### Recommended (not blocking, fix if cheap)
8. **s021 (illustrator)**: the mother's silhouette has a rounded blob head with no ears or muzzle, so it reads as a
   bear or a hippo. Silhouette the actual `cave_lion` asset used in s023 so the shape matches the reveal.
9. **s060 (illustrator/director)**: the pale bone fragment sticking out of the cliff reads as a stray white chevron
   mark. Either make it a recognisable bone (with knobbed ends) or remove it.
10. **s205, s120, s101 (director)**: the time-machine sign text fills or overflows the green plate. In s205,
    "506,000,000 YEARS AGO" runs past both edges. Widen the plate or write "506 MILLION YEARS AGO".
11. **s006, s007 (director)**: Doug stands exactly on the mummy/fossil seam, half on each background. Move him
    about 150 px onto the light side so he isn't split.
12. **s149 (director)**: the "ERRATIC" word sits on top of a footprint circle. Move the word up or right.
13. **s139, s156 (director)**: the creature icon sits over North Africa, below the location circle (Bavaria,
    Holzmaden). Move it next to the circle or onto the ocean beside Europe.
14. **s133 (director)**: the belly-up carcass sits on the grass beside the river, not on it. Put it on the river line.
15. **s176-s177 (illustrator/director)**: the "inside the nodule" body is a plain ellipse. A faint arthrodire
    outline (armoured head and body) would show the organs are inside a fish.
16. **s019 (director)**: the narration says Doug "kneels down to pet her", but he stands upright. Use a crouch/kneel
    pose if the rig has one.
17. **s039 (director)**: the "THE PLAN" picture overlaps the shelf props. Move it up or right.

### Thumbnail (graphic designer)
- PASS with one note. The 3x3 Archetype A grid reads at feed size (320x180). Every label is legible, no label uses a
  title word, and the background runs from ice blue to near-black with Stanleycaris (red glow) as the bottom-right
  boss, as briefed. It complements "The Creepiest Fossils That Still Look Alive" and does not mislead (every tile
  appears in the video).
- Note: at 320x180, Doug in the Fighting Dinosaurs tile is about 6 px, just a red dot. The brief asks for "tiny",
  so this is not blocking. Scaling him up about 1.5x (cap and face clearly readable at small size) would make the
  "Doug visits" hook land in the feed. "Fighting Dinosaurs" is also auto-shrunk smaller than the other labels.
  Optional fix: "Raptor Fight" fits the standard size.

Re-check after fixes: s030, s081, s134, s145, s151, s181, s182, s207, s011-s014 (plus any recommended items
changed).

## Round 2: keyframe re-check + full contact-sheet pass (2026-10-01)

Scope: zoomed keyframes s011-s015, s019, s020, s030, s039, s060, s064, s081, s101, s120, s134, s139, s145, s149,
s151, s156, s181, s182, s205, s207, and all 18 contact sheets again. Thumbnail not re-checked (unchanged; it passed
in round 1).

### Round 1 fixes: status
- **s030**: fixed. The ox is now blue. One small leftover is listed in fix 7 below.
- **s145**: fixed. "NO PREDATOR" now stands alone, with no X.
- **s081**: fixed. It reads as a burrow: a tunnel, a chamber, a caving roof with falling clods, and the pup curled
  up, clearly visible, about 370 px wide.
- **s151, s181, s182**: fixed. The snorkel and fins are gone, Doug wears a mask only, and the swim pose is clean.
- **s207**: fixed. The mudflow wave curls in, the lone cap and one eye stalk poke out, and the counter shows 46. It
  no longer reads as a blank frame.
- **s011-s014**: fixed. s013 is now a big shocked close-up of Doug on yellow, and s014 is a clear radiocarbon
  timeline (dots at about 43k and 28k). The run of identical cross-sections is now s009-s012. Those shots differ
  in labels and props, so this is acceptable.
- **s205, s120, s101**: fixed. The plates fit.
- **s019, s039, s060, s139, s149, s156**: fixed (crouch pose, moved picture, stray chevron removed, icons moved
  next to the circles, ERRATIC clear of the prints).
- **s134**: **not fixed.** See fix 1.
- Still open from the recommended list: s133 (the carcass sits beside the river, not on it) and s176-s177 (a plain
  ellipse). Both are still optional.

VERDICT: FAIL

### Required fixes
1. **s134 (director + art director)**: Doug is drawn in a sitting pose but floats in mid-air, about 90 px above the
   carcass. The "THUMBS UP" arrow points at empty sky, and his arm has no thumb (just a bent stick). Put him
   sitting on the belly between the two upturned legs, at the same spot he occupies in s135, so his seat line
   touches the belly. Art director: give the raised fist a visible thumb (a short vertical stroke on the hand).
   Point the arrow at that hand.
2. **s027 (director)**: an empty white rectangle (rect at x820, y500, 160x60) floats over Blue Babe's back. It
   reads as a broken or missing label. Delete it, or make it a museum plaque on a post with text (for example
   "BLUE BABE"). Optional: flip Doug to face left, toward the bison.
3. **s019, s038, s069, s166 (director; art director if it is the engine)**: the speech-bubble tails render as thin
   double-line slivers instead of a solid wedge. The tails are long and shallow (for example, s019 runs from the
   bubble at 720,420 to 980,560; s166 is nearly horizontal). In s038 the tail also stops about 100 px above Doug's
   head. Move each bubble close to Doug, directly above or beside his head, so the tail is short (under about
   150 px), steep, and ends about 15 px from the head, like the good tails in s053, s151 and s182. If the engine
   draws the tail's base too narrow at shallow angles, the art director should widen the tail base in `paint.py`.
4. **s100 (director)**: "very reasonable guess" wraps to two lines, and "guess" collides with the bubble outline
   and the tail. The bubble also touches the chapter tag. Widen the bubble to about 640 px so the text fits on one
   line (or drop the size to about 40), and move it down so it sits clear of the tag.
5. **s045 (director)**: "1 MONTH" is wider than the calendar page and spills past both edges. Use a smaller size
   (about 30) or a larger calendar.
6. **s136 (director)**: the ghost Doug's body overlaps the "N" of "UPSIDE DOWN". Move the ghost right, about
   120 px or more (still under the counter), or shift the word left.
7. **s030 (illustrator)**: the blue ox still has two dark-brown legs (the far-side legs kept the original bison
   colour). It looks like a recolour miss. Tint them dark blue.

### Recommended (not blocking)
8. **s151 (director)**: the narration says Doug follows the trail "across the lagoon floor", but his feet are
   about 95 px above the sand. Drop him onto the floor line.
9. **s013 (director)**: Doug's right arm runs into the "T" of "THE TWIST", and the top half of the frame is empty.
   Move the word up, next to the "!".
10. **s142 (director)**: the red X clips the end of the "ALMOST NO OXYGEN" plate, and crossing out a "no" label is
    the same double-negative problem as s145. Remove the X.
11. **s026 (director)**: the Blue Babe icon sits over Scandinavia while the circle is on Alaska. Move the icon next
    to the Alaska circle (or onto the Pacific beside it).
12. **s210 (director)**: the big "DOUG DEATHS: 46" plate covers the top of the time machine. Nudge it up or left.
13. **s133, s176-s177**: same as round 1 items 14 and 15.

Re-check after fixes: s134, s027, s019, s038, s069, s166, s100, s045, s136, s030 (plus any recommended items
changed).

## Round 3 (final): keyframe re-check + general pass (2026-10-01)

I viewed every keyframe in `build/keyframes/` (s001-s211, rendered at 23:07, plus s026, s100 and s136 re-rendered at
23:08). Sheets 01-08 were full contact sheets when I read them. Partway through, a `--shots` run overwrote
`build/contact/` with a single 3-tile sheet, so I reviewed s097-s211 from my own grids of the current keyframes.

### Round 2 fixes: status
- **s134**: fixed. Doug stands on the belly between the upturned legs, the thumb stroke is visible, and the arrow
  points at the hand.
- **s027**: fixed. The empty rectangle is gone.
- **s019, s038, s069, s166**: fixed. The tails are short, solid wedges that end just above Doug's head.
- **s100**: fixed. "very reasonable guess" fits on one line, and the bubble is clear of the tag. The scientist now
  stands behind the lectern.
- **s045**: fixed. "1 MONTH" fits inside the calendar page.
- **s136**: fixed. The ghost sits right of "UPSIDE DOWN" with a clear gap, under the counter.
- **s030**: fixed. All four legs of the ox are blue.
- **s013**: fixed. "THE TWIST" sits next to the "!", clear of Doug's arms.
- **s142**: fixed. The X is gone.
- **s151**: fixed. Doug walks on the floor line next to the trail.
- **s210**: fixed. The counter plate sits above the time machine.
- **s133**: fixed. The carcass floats in the river channel.
- **s020**: OK. It is the clean "HER MOTHER?" beat.
- **s026**: not changed. The Blue Babe icon still sits east of the Alaska circle, over northern Canada. It is now
  next to the circle, so this is acceptable (see note 1).

### General pass
No blank or broken frames. Doug is on-model everywhere (red cap, white head). No gore: the deaths are ghost-and-cap
gags, and s047's "ORGANS: INTACT" is text only. Nothing reads as a kids' show. All text I checked is legible and
spelled correctly. The "Zh?r" boxes appear only in the contact-sheet captions (the caption font lacks the glyph).
The rendered title cards show "ZHÙR" correctly.

VERDICT: PASS

### Non-blocking notes (optional polish; do not hold the render)
1. **s026, s043 (director)**: the map icons sit beside their circles, not on them. s043's mammoth sits over
   Scandinavia while the circle is on Yamal. Move each icon onto or right next to its circle.
2. **s036 (director)**: the "well aged" bubble tail ends in the air between the two scientists. Aim it at the
   speaker's head.
3. **s197-s201 (director)**: five near-identical Stanleycaris close-ups in a row. The labels and the brain overlay
   change, but the framing doesn't. Consider cutting to Doug, or widening the shot, on s198 or s200.
4. **s176-s177**: still a plain ellipse body outline (carried over from rounds 1 and 2).
5. **Pipeline (editor)**: a `--shots` keyframe run overwrites `build/contact/` with a partial sheet. Re-run full
   `keyframes` before any later contact-sheet review.

## Post-render review (final.mp4, thumbnail, Shorts)

Checked: 34 sample frames (`build/samples`), `build/qc.json` (problems: none, 1007 s), the end frames of every
camera-move shot pulled from `final.mp4`, `build/thumbnail.png` and `build/thumbnail_small.png`, `metadata.json`,
the three Shorts previews, and 9+ frames from each Short.

### What passes
- No black, blank, frozen or glitched frames. Every sample matches its narration (once you allow for the 15 s
  sample offset). Doug is on-model everywhere. No gore: the deaths are ghost-and-cap gags. Nothing reads as a
  kids' show.
- Thumbnail: the 3x3 labelled grid reads at feed size. Doug's red cap shows in the Fighting Dinosaurs tile. The
  grid fits the title "The Creepiest Fossils That Still Look Alive" and isn't misleading.
- Shorts end cards: "WHAT HAPPENS NEXT? TAP BELOW" is readable, the red arrow points down, and Doug points at
  the arrow. Titles and subtitles are legible in all three Shorts.

### Blocking problems
1. **Map zoom crops the date label and Doug (director)**: s008, s043, s074, s106, s139 and s156 all have
   `camera: zoom_in, zoom 1.08, y 400-450`. By the end of each shot the visible frame stops at y ~1000. The date
   label at y 1010 shrinks to an unreadable sliver ("2017 + 2018", "2007", "JULY 2016", "AUGUST 3, 1971",
   "150 MILLION YEARS AGO", "180 MILLION YEARS AGO"), and Doug's legs (y 979) are cut off. The keyframes are
   static frames, so this only shows in the render. Fix: set `camera.y` to 580 in these six shots. That keeps
   y 80-1080 in frame, with the map top still visible. Or move the date label to y 900 and Doug to y 900.
   s096 has the same zoom; its Doug at y 979 is also cut, so apply the same `camera.y` change there.
2. **Short03 shows a wrong number (director)**: in s199 (the hook scene and again in the body), the label
   "84 FOSSILS" at x 300 falls outside the Shorts crop-safe zone (x 260-1660 minus half the text width). On
   screen it reads "4 FOSSILS". Move the label to x 480 or more.
3. **Short03, Doug cut in half (director)**: in s197, s199, s200 and s201, Doug sits at x 200, so only half of
   him shows at the left edge of the Short. Move him to x 380 or more. Also move the s197 "STALK EYES" label
   (x 360) to x 420 or more, and check "506 MILLION YEARS" in s199 (x 1500), which sits on the right edge.
4. **Short03 time-machine sign cut off (director)**: in s205, the sign rect starts at x 60 and the text is
   centred at x 358, so the Short shows "MILLION YEARS AGO" without the "506". Move the time machine and its sign
   so the sign spans x 300-900 or so.

### Non-blocking notes
5. s113 (director): the BEAK arrow tip (1260, 600) ends in the air about 70 px in front of the beak. Move `to`
   to about (1190, 630).
6. Short01 s035-s039 and Short02 s071: the "DOUG DEATHS" plate and the time-machine sign sit at the right edge
   and are partly trimmed in the Short. They are still readable, so this is optional polish.
7. Engine (editor): the keyframe contact sheet can't catch camera-move crops. Consider rendering the final
   camera frame of each zoom shot to the contact sheet.

After the fixes: re-render shots s008, s043, s074, s096, s106, s139, s156 and Short03, then re-screen.

VERDICT: FAIL

## Post-render review, round 2 (final.mp4 re-render, Shorts re-render)

Checked: the end frame of each fixed zoom shot taken from `build/final.mp4` (s008 28.7 s, s043 180.75 s, s074 333.75 s,
s096 444.15 s, s106 497.7 s, s139 667.75 s, s156 740.55 s), plus s113. `build/qc.json` reports no problems
(1007.27 s, matching timing.json). I also checked `build/shorts/short0{1,2,3}_preview.png`, a frame every 3 s from
all three Shorts, and full-resolution crops of the edge regions.

### Fixed (verified)
- **Map zooms, s008, s043, s074, s096, s106, s139, s156**: with camera.y at 580, every end frame shows the whole
  date plate ("2017 + 2018", "2007", "JULY 2016", "AUGUST 3, 1971", "150 MILLION YEARS AGO", "180 MILLION YEARS
  AGO") and Doug from cap to feet. The title plates and map tops are intact.
- **Short03**: "84 FOSSILS" reads in full in the hook and the body. Doug is whole in s197 and s199-s201.
  "STALK EYES", "THIRD EYE" and "506 MILLION YEARS" are all inside the frame. The s205 sign reads "506 MILLION YEARS
  AGO" in full. The title, subtitles and end card (arrow pointing down) are fine.

### Blocking problems (Short01 / Short02, crop-safe zone x 260-1660 of the 1920 frame)
Round 1 called these edge trims optional (note 6). Full-resolution frames show the text is cut, not just trimmed,
so they now block:
1. **s067 (director), Short02**: the "SOUTH KOREA" label (x 1600, size 46) reads "SOUTH KORE". Move the label
   to x 1420 and the second scientist from x 1600 to x 1450.
2. **s071 (director), Short02**: the "42,000 YEARS" label reads "42,000 YEAR", and the foal (the subject of
   "give back one foal") is cut at the right edge. Move `batagaika_foal_mummy` and the "42,000 YEARS" label from
   x 1600 to x 1400, and `doug_cap` from x 1250 to x 1150.
3. **s037 and s038 (director), Short01**: the time-machine sign reads "36,000 YEARS A" (s037), and the "1984" sign
   is also trimmed (s038). Move `time_machine` from x 1650 to x 1400, along with its sign rect and text
   ("36,000 YEARS AGO" from x 1625 to 1375, "1984" from 1650 to 1400). Shift Doug left if he overlaps.
4. **s040 (director), Short01**: Doug at x 1750 shows only as a red sliver at the right edge, which looks like a
   glitch. Move him to x 1600 (scale 0.45), clear of the stew bowl at 1500, or remove him from the shot.
5. **s063 (director), Short02 hook frame**: Doug at x 1700 touches the right edge. Move him to x 1580.

### Non-blocking (carried over)
- s113: the BEAK arrow tip still ends in the air in front of the beak. Set `to` to about (1190, 630).
- s008 and s043: the map icons still sit off their circles (cave lion cubs over China, mammoth over Europe).

After the fixes, re-render s037, s038, s040, s063, s067 and s071 in final.mp4, and re-render Short01 and Short02.
Then re-screen.

VERDICT: FAIL

## Post-render review, round 3 (final re-screen: final.mp4, Short01-03, thumbnail)

Checked: full-resolution frames from `build/shorts/short0{1,2,3}.mp4` (a frame every 2 s, plus targeted grabs of
the fixed shots and every DOUG DEATHS plate), the end frames of s037, s038, s040, s063, s067, s071, s113 and s200
from `build/final.mp4`, all 34 `build/samples/*.png`, `build/qc.json` (no problems, 1007.27 s), and
`build/thumbnail.png` / `thumbnail_small.png`.

### Fixed (verified)
- **s037 / s038 (Short01)**: the time-machine sign reads "36,000 YEARS AGO" in full, and the "1984" sign is whole.
  The booth is fully inside the frame.
- **s040 (Short01)**: Doug is whole beside the bowl, with no red sliver at the edge.
- **s063 (Short02 hook)**: Doug stands clear of the right edge.
- **s067 (Short02)**: "SOUTH KOREA" reads in full, and both scientists are whole.
- **s071 (Short02)**: "42,000 YEARS" reads in full, and the foal and the cap are whole.
- **s113**: the BEAK arrow now ends on the beak.
- **DOUG DEATHS counter**: shows the full number everywhere. "DOUG DEATHS: 37" (Short01), "DOUG DEATHS: 39" (Short02) and
  "DOUG DEATHS: 46" (Short03) are inside the frame with a margin. They also read correctly in final.mp4.
- Short03 regressions from round 2: none. "84 FOSSILS", "STALK EYES", "THIRD EYE", "506 MILLION YEARS AGO", "2 EYES / 3
  EYES" and Doug are all inside the frame.
- Titles, subtitles and end cards (arrow pointing down) are fine on all three Shorts.
- final.mp4 samples: no black or frozen frames and no glitches. Text is readable, and there's no gore or kids-show tone.
- Thumbnail: unchanged since approval. The 3x3 fossil grid with Doug in the Fighting Dinosaurs panel is still
  readable at feed size.

### Non-blocking (carried over, optional)
- s008 / s043: the map icons still sit slightly off their circles.
- Short03 "DOUG DEATHS: 46" plate sits about 40 px from the right edge. It reads, but it's tight.

VERDICT: PASS
