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
