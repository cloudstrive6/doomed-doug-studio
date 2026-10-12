# Art review: 015 The Deeper Doug Digs (assets)

Reviewer: art director · 2026-10-12 · scope: the 48 new assets in `asset_requests.md` and the strata ramp.

## Verdict: PASS. All 48 assets APPROVED (`repenomamus_fight` passed on re-review, see below).

### Re-review 2026-10-12: `repenomamus_fight` v2 APPROVED
Checked `assets/previews/015-fight-v2.png` (side by side with `psittacosaurus` and `repenomamus`) and `015-fight-shot.png`
(s143 layout, x=1000 y=900 scale 1.3, plus small-size inset). Every point of fix 1 is met:
- The Repenomamus lies along the back with its jaws on the ribs at mid-flank (~(+34,-64)), well clear of the dinosaur head.
  The two heads no longer merge.
- The front paw rests on the lower jaw below the eye. The yellow eye stays fully visible.
- The dinosaur head stands apart at the right with the hooked dark beak, cheek horn, yellow eye and quilled tail of
  `psittacosaurus.json`, so it matches s135/s148. It reads as Psittacosaurus, not a seal or dog.
- No red anywhere in the asset (palette is browns, olives, black and white only). The mouths are dark with white teeth.
  The red circles in the shot preview are hold-point check markers, not part of the asset.
- Bbox is now ~610x195 instead of ~560x300. At scale 1.3 to 1.4 with the `bc` anchor at (1000,900) it spans roughly x 600-1400,
  so it stays inside the safe area and the shotlist layout holds. The silhouette also reads at inset size.
Minor note, no action needed: the reaching foreleg is long and straight. It still reads as a limb because the claws sit at its tip.

Checked every preview sheet (`assets/previews/015-*`), the worn-costume, dark-background and silhouette checks, plus my own
1920x1080 re-renders of the riskier assets. They match the detailed tier against crude Doug: 4-6 px outlines, flat fills with
spray shading. Palette is on, silhouettes are bold, the dark-scene assets read on `#0d1b2a` and near-black rock, and nothing is
gory (no wounds, blood, emergence or hatchling bodies). Creatures look like a dangerous documentary cartoon, not cute.
Note: the grid preview tool centres every asset, so tall `bc` assets (camel, giraffe, mud_wave, sue_skull_case) look cropped
on the sheets. That is a preview artefact. The assets are complete.

## Fixes

1. **`repenomamus_fight` (A, illustrator): REWORK. RESOLVED in v2 (see re-review above).** At hero size the pose doesn't read. The mammal's head sits on the
   dinosaur's neck and shoulder, and its paw crosses the Psittacosaurus face, so the two heads merge into one dog-like blob.
   The Psittacosaurus reads as a seal or dog. Redraw it so that:
   - the Repenomamus lies along the dinosaur's back with its **jaws clamped on the ribs at mid-flank**, well clear of the
     dinosaur's head;
   - one front paw reaches forward onto the **lower jaw** without covering the eye;
   - the dinosaur head stands clearly apart at the right with the same parrot beak, cheek horn and tail quills as
     `psittacosaurus.json` so it matches s135/s148;
   - there is no red inside either mouth (s142-s154 is a fight beat and red mouths read as blood at this size).

   Keep the `bc` anchor and the ~560x300 bbox so the shotlist layout holds.

## Fixed by me (no action needed)

2. `messel_snake_slab`: the lizard in the snake's belly read as a fish spine lost among the snake's rib fans. I added a slightly
   lighter stomach patch behind it, scaled the lizard group up to 1.4 and thickened its limbs. It still centres on (+40,+20),
   so existing ring and arrow targets hold.
3. `sue_skull_case`: removed the white eye glint in the orbit, which made the fossil skull look alive, and added a mounting post
   so the skull no longer floats above the plinth.

## Notes for the director

- `sue_jaw` is a true left-side view, so the **snout is at the LEFT** and the holes sit on the back half at the requested points.
  Don't flip it expecting a right-facing snout.
- `fly_pupa` silhouettes, `aspidorhynchus` silhouettes and `nothosaurus` silhouettes read well at the requested scales.
- Worn gear (`fly_pupa_costume`, `vet_coat`, `referee_shirt`, `cloudina_costume`) keeps Doug on-model: head, eyes and red cap
  stay clear, the stethoscope stays below the face and the whistle doesn't touch the eyes.

## Strata ramp: APPROVED with a correction (now in `channel/art_bible.md`)

The requested ramp got lighter partway down. Layer 5 `#8e4a2c` has luminance 91, but layer 6 `#7a6656` (106) and layer 7
`#6b7280` (114) were both brighter. That breaks the channel rule that each step is darker. Corrected values:

| Layer | Was | Now |
|---|---|---|
| 6 | `#7a6656` | `#665244` (86) |
| 7 | `#6b7280` | `#4a505c` (80) |
| 8 | `#4f5560` | `#3f444d` (68) |

Layers 1-5 and 9-11, the boundary clay stripe `#efe6d0`, the grey bands `#5f5f5f`, the green glow `#2f5a3a`, the shaft
interior `#f1e4c6` and the DEPTH meter placement are approved as requested. I swapped the three hexes in `shotlist.json`
directly (they appear only in the strata rects). `validate shotlist` passes, apart from the expected missing thumbnail on s001.

---

# Keyframes round 1

Reviewer: art director · 2026-10-12 · scope: `build/contact/sheet_01-25.png` (s002-s289) plus full-res checks of
`build/keyframes/` for anything that looked borderline. s001 skipped (thumbnail pending).

## Verdict: FAIL

The episode holds together well. Doug is on-model in every shot, including the costume, vet, referee, swim, close-up
and ghost shots, and the red cap shows every time. The strata ramp in the title-card shafts darkens correctly with
depth, the x-ray/scan language (s043-s048, s066-s069, s079) stays consistent, and layouts change often (maps,
slabs, timelines, cutaways, close-ups, callback circle s281, strata finale s289). There are no runs of identical
compositions. It still fails on hard rules: silhouettes reveal without the red glow (style bible 7.7), there are
too many labels on screen in three shots (7.4), scale analogies are drawn wrong, and art covers the HUD in about a
dozen shots. All fixes below go to the **director** unless they are marked (illustrator).

## Required fixes

### A. Silhouette reveals need the red glow (rule 7.7)
1. **s043, s054, s166, s180, s186, s199, s204**: each black silhouette needs a red glow behind it (a red spray at
   the same density as s225). s098/s103 already have one, and it can be pushed a little stronger.

### B. Label count (rule 7.4, max 2 on screen)
2. **s067, s068**: SNAKE, LIZARD and INSECT are 3 labels. Keep LIZARD and INSECT on s067. Drop SNAKE, because the
   snake reads on its own. On s068, keep only the "?". INSECT also crowds the depth meter.
3. **s211**: COPROLITE, 5 CM and SPIRAL are 3. Drop COPROLITE, which the narration covers, or bring SPIRAL in on s212.

### C. Art covering the HUD (death counter / depth meter must stay clean)
4. **s034**: the "WASPS INSIDE FOSSIL FLIES" title card runs under the DEPTH box and shovel icon. Shrink it to about
   80% or move it down about 60 px.
5. **s206**: "THE SHARK'S" overlaps the shovel icon and the DEPTH box. Shrink it or shift it left and down. Also check
   s057, s109, s131, s232 and s256. They clear, but only by a few px, so give every title card the same max width
   (the shaft width plus about 100 px) and a top limit below y=300.
6. **s082**: Sue's skull sits behind the depth meter. Move the skeleton about 150 px left or down.
7. **s152**: the "005" slab touches the DEPTH box. Move it down about 80 px.
8. **s155**: the mudflow's ash puffs run behind DOUG DEATHS. Lower the wave or cut the top puffs. The counter
   increments on this shot and must be readable.
9. **s169, s170, s171**: the wing bone runs through the shovel icon and DEPTH box. Move the jaw group down about
   90 px or shorten the bone.
10. **s204**: the Nothosaurus silhouette's snout touches the DEPTH box. Scale it to about 0.9 or move it down 60 px.
11. **s240**: the OUTSIDE label is jammed under the DEPTH box. Move it next to the worm, at about (1500, 600).
12. **s281**: the callback T. rex sits behind the counter and depth meter, and Doug at x≈1865 is outside the 5%
    safe area. Pull the circle in or drop the rex to the empty slot at the right, and move Doug to x≤1780.

### D. Scale analogies drawn wrong
13. **s018**: the 30 cm ruler is as tall as Doug, which makes Doug about 30 cm. Scale the ruler to about 1/6 of
    Doug's height, or zoom in on his shins, and make the grey ash band match the ruler.
14. **s039**: the rice grain is only slightly longer than the pupa. The script says the pupa is less than half the
    rice. Make the rice ellipse at least 2.2x the pupa's length.
15. **s239**: the ostracod (max 4 mm) is drawn about 2.5x the rice grain. Flip it: the ostracod should be about
    0.6x the rice. Shrink the ostracod or enlarge the rice.
16. **s064**: the lizard's body spans about 25 cm on the 30 cm ruler, but the line says 8 cm. Scale the ruler up so
    the body (without the tail) covers 0-8.
17. **s088, s089**: Doug (scale 0.5) stands about 0.7 m against a 1.5 m skull. Doug should be a little taller than
    the skull is long, so use scale about 1.2, or shrink the case.
18. **s191**: the Tanystropheus head runs into the giraffe's chest and GIRAFFE sits on the giraffe's head. Put them
    side by side or stacked, neck to neck, with the label beside the giraffe.

### E. Readability and staging
19. **s031**: dead Doug lies on the red gingham. His body lines vanish, and the red cap beside his head reads as a
    red pool at small size (gore risk). Move the body off the blanket onto the sand.
20. **s141**: the "2023" label is hidden behind the slab, so only "20" shows. Move it to the left of the slab.
21. **s178, s179, s180, s181**: the fishing line ends in mid-air about 85 px above the water, and the rod runs up
    through the caption bar. End the line at the waterline with the bobber on the surface, and shorten or lower
    the rod so it clears the caption bar.
22. **s202**: the `snorkel` asset is placed at a fixed point and floats detached above Doug's head while he swims.
    Remove it (`gear: ["mask"]` already reads) or attach it at his mask.
23. **s223, s224**: the pink flesh window with red zigzags inside the black shark reads as guts. Restyle it in the
    episode's pale-blue x-ray look (as in s045 and s066): a light-blue window and a white spiral.
24. **s247**: the camera is a spray-noise grey blob about 60 px wide and doesn't read. Scale it to about 3x and drop
    the noisy fill (use the plain camera asset).
25. **s134**: the Asia map's black frame shows along the top and right inside the shot. Scale the map to bleed off
    the frame or crop the frame lines.
26. **s070**: RUSSIAN DOLLS sits on the biggest doll's face. Move it above the dolls.

## Minor (fix if touching the shot anyway)
- s015: YELLOWSTONE sits at the bottom, far from the hotspot. Move it next to the volcano or circle.
- s016: the ash plume spray is very faint on blue. Raise its density so "drifted east" reads.
- s020: the hoop sits on the ash surface like a sign. A cutaway showing the buried pole would sell "3 m deep".
- s099: the "2022" label clips the jaw outline. Nudge it up.
- s159, s160: Doug's black ink on the dark slate bottom band (about `#3d5868`) is low contrast. Lift that band a
  step or force white ink there.
- s287: TWO CAPS runs into the hole edge. Shift it left about 60 px.
- s086: the cap is `doug_cap_fossil` (stone grey), but the line says "a red cap". A faded red tint in the stone
  (illustrator) would make it read as *his* cap. Not blocking.
- s072, s073, s160, s213: the generic orange goldfish stands in for an ancient "spiny fish". That's fine as
  shorthand, but s072 says "spiny fish" on screen. An acanthodian asset (illustrator) would match better. Not blocking.

## Checked and OK
- Doug on-model everywhere. Ghost Doug keeps his cap (s031, s056, s107, s130, s156, s182, s205, s230, s286). The
  death counter steps 121 to 130 exactly on the death beats.
- `repenomamus_fight` v2 reads correctly in context (s142, s143, s149, s151-s154). The heads stay separate and there
  is no red in the mouths.
- Zone and strata colours match the art bible ramp (s005-s256 title cards, s278, s289). Night (s132, s147, s148),
  ash grey (s017-s033) and sea teal (s186-s205, s257-s286) stay consistent inside each item.
- Caption bars are present and match the item names on every segment frame. Intro and outro frames (s002-s005,
  s287-s289) correctly have none.

## Director fixes after keyframes round 1 (2026-10-12)

All 26 required items above, plus visual_review.md Round 1 (13 required + recommended 14-18), applied in `shotlist.json`;
validate OK, shorts validate OK, affected keyframes re-rendered and checked.

- **A. Red glow on silhouettes:** s043 (glow switched from blue to red), s054 (wasp also moved off the HUD), s166, s180 (fish +
  pterosaur), s186, s199, s204: red spray behind each silhouette, timed with its `appear`. s098, s103, s107: density raised to 0.42.
- **B. Labels:** s067 has LIZARD + INSECT only (INSECT moved bottom right, away from the depth meter, with the new `insect`
  icon beside it). s068 keeps only the "?", now placed by the lizard's belly. s211 COPROLITE dropped.
- **C. HUD:** every chapter title card (s006 s034 s057 s081 s109 s131 s157 s184 s206 s232 s256) now has size 110 and
  max_width 1000, with its top edge at y≈315, so all titles sit below the HUD. s082 skeleton x760 s1.3 (SUE label moved left).
  s152 slab and "005" moved down 80 px. s155 mudflow s1.75 lowered (top puffs at y≈330). s169-s171 jaw/wing group and its
  arrows/labels moved down 90 px (s170 BONE label + red X now sit on the bone). s176 slab grid down 50 px. s204 Nothosaurus s2.16, y+70.
  s240 OUTSIDE label at (1560,640) beside the worm. s281 ring pulled in 15% (T. rex moved to the free slot clear of the HUD),
  Doug x1760.
- **D. Scale:** s018 rebuilt: big Doug (s1.5) buried to the shins in a 105 px ash band, a ruler of the same height, and an arrow to "30 CM".
  s039 pupa s0.9 (rice is about 2.4x). s064 lizard s1.6 + ruler s2.3: body (without tail) spans 0-8 cm. s088 Doug s1.4 (a bit taller
  than the 1.5 m skull). s089 case shrunk to s0.38 against Doug s0.45. s191 Tanystropheus (s1.0) and giraffe (s0.7) side by side
  with a gap, GIRAFFE label above the giraffe. s239 now compares the tongue worm itself to the rice grain (worm about 0.6x rice).
- **E. Staging:** s031 dead Doug + ghost moved off the blanket onto the sand. s141 "2023" moved left of the slab (drawn on top).
  s178-s181 rod redrawn inline as a flatter group: the tip is at y≈120, below the caption bar, and the line ends at the waterline with the float on
  the surface. s202 snorkel removed. s223/s224 window now pale blue (#6fb7d6) with a white coiled spiral. s247 camera
  s2.4, spray removed. s134 map scaled to 3.75 around China, so the frame lines bleed off. s070 dolls lowered and RUSSIAN DOLLS moved above them.
- **Visual review:** s071/s078 brown oval replaced by the new `insect` icon. s072/s073/s213 use the new `spiny_fish`
  (s160 keeps small_fish, because acanthodians are gone by the Jurassic). s197 is now a close-up: the slab bleeds off the right edge and a
  dashed outline of the missing body has a "?". s238 shows the tongue worm alone on a 0-5 mm ruler (4 mm and 1 mm worms).
  s242 is now a timeline: ostracod → 425 MILLION YEARS → worm today. s107 adds Sue's silhouette with a red glow beside the
  hole. s086 tag "003" changed to "HIS" (appears on the word), using the red-tinted `doug_cap_fossil`. s287 shovel s1.8 with
  caps s0.9, TWO CAPS moved left.
- Minor notes not addressed: s015, s016, s020, s099, s159/s160.
