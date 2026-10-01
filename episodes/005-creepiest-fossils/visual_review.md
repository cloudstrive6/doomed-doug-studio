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
