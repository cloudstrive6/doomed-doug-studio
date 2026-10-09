# Visual review: 011-every-animal-fight

## Round 1: pre-render keyframes (2026-10-09)

Scope: `shotlist.json` (285 shots), `build/contact/sheet_01..24.png`. s001 shows "(thumbnail pending)", which is expected at this stage and not counted against the episode.

VERDICT: FAIL

Three required fixes, all small: one continuity break that undercuts a narrated payoff, one label collision, and two runs of near-identical frames. Everything else is clean. Drawings are recognisable, Doug is on-model throughout (red cap, white head, readable on every background including the night wolf set and the dark-red elephant set), the counter is correct (93 -> 94 kangaroo, 95 wolf, 96 cassowary, 97 chimp, 98 croc, 99 polar bear, 100 elephant; goose, cat and gorilla survived), all on-screen text is spelled correctly and inside frame, and the chapter labels and title cards are consistent.

### Policy checks
- **Gore / violence:** pass. Every death is shown as the dust cloud, then X-eyes Doug lying flat with his cap knocked off, plus ghost Doug (s072, s098-099, s124-125, s153, s213, s242-243, s279). There is no blood. The open mouths (gorilla s166/s171-175, polar bear s218/s221, croc s192-195) have plain red or tan interiors with no blood. The 2022 kangaroo death (s068) is a map dot, the Maasai spearing (s258) is shown as arrows meeting at a waterhole with no spear, the chimp killings (s145-149) are flat silhouettes, and the seal in s234 is whole.
- **Kids-show tone:** pass. The "hi friend?" bubbles are naive in a deadpan way, not nursery. There are no baby-style framings, mascots or sing-song text.
- **Gorilla walk-away (s177-s184):** pass. It does not read as survival advice. Doug's chest beat is framed as pathetic ("tap tap" on a cardboard box, s178). The verdict in the guide is MAYBE, not a tick (s181). The narrator's pre-drawn death page (s182) and the gorilla's own "~~~ = SMALL" judgement (s183) make it clear the gorilla chose to leave, and that Doug did nothing right. No frame shows a "DO THIS" style instruction.
- **Cat-bite bar (s043-s044):** pass. The 3-cell bar with 1 red cell plus "1 in 3 -> HOSPITAL" reads correctly in 1 s. "3 YEARS" sits above it, and "FIGHT" is crossed out in s044. There is no wound, blood or bite imagery, and Doug's bandage (s039) reads as a wrapped hand at full size.

### Required fixes
1. **s025, s026 (director): goose continuity.** In s021-s024 the goose walks off wearing Doug's cap (`canada_goose_cap`) and Doug sits with `cap_off`. In s025-s026 Doug is suddenly wearing the cap again and the goose is bare (`canada_goose`). That contradicts the narration "the goose kept the pond, the dignity and the last word ... a clean sweep". Change: in both shots set Doug `gear: ["cap_off"]` and swap the asset to `canada_goose_cap`. Keep it on the pond and keep the labels. The cap can come back at the s027 House Cat chapter card as it does now.
2. **s208 (director): label collision.** Doug's cap overlaps the bottom-right corner of the red "27 FATAL" box. Change: move Doug about 120 px right and down, or move the "87 ATTACKS" / "27 FATAL" stack up and left about 60 px, so they don't touch.
3. **s274-s278 and s230-s233 (director): variety.** These are two runs of 4 or more near-identical compositions.
   - **s274-s278 (elephant ending):** five shots in a row use the same layout: same frontal elephant at x1300, small Doug left, sunset left. Only the bubble or label changes. Change: make s275 ("listened very carefully") a close-up of the elephant's head and ear with sound arcs, with Doug small at the edge. Make s277 ("It was right.") a tighter two-shot or a low angle. Then keep s276 and s278 in the current wide layout, so the s278 -> s279 death cut still lands.
   - **s230-s233 (polar bear, "worst part" beat):** four shots in a row put Doug left and the side-view bear right on the same ice horizon. Change: make s232 ("the hungry one") a close-up of the bear's head, or show the bear with the empty FOOD meter from s231 enlarged, or just push in on the bear. Then s233 can keep the wide shot with the crossed-out "DEFENDING".

### Recommended (not blocking)
4. **s028 (director):** the cat's ear clips the "M" of "MOST CONFIDENT". Move the cat about 40 px down or move the text about 30 px right.
5. **s083 (director/illustrator):** the ELK, BISON and MOOSE labels float, but only the moose is drawn. Either point each label at an animal (add the existing library elk/bison if there are any) or keep only MOOSE plus a "+ ELK, BISON" line.
6. **s052 (director):** the red down-pointer lands right on the red figure's head and reads a little like a spike through it. Stop the arrow about 20 px above the head, or use a bracket or ring instead.
7. **s266 (director):** the red arrow points down from the low-frequency wave to the high-frequency wave under the heading "PITCH UP". At a glance it reads as "pitch down". Use a sideways arrow, or put the high-pitch wave above the original wave.
8. **s137 (director):** the 27 KG suitcase floats above the chimp, whose arms are down. Give the chimp a lifting pose if the asset has one, or place the suitcase in its hands or on its back. s136 works because Doug's arms are up.
9. **s217 (art director, optional):** the red-speckle threat aura behind the bear silhouette is denser than the cassowary's (s103). It is fine at full size, but at small size it could read as a red spray. Consider dropping its density or tinting it toward grey-red.

Routing: fixes 1-4 and 6-8 go to the director (shotlist edits, then re-key s025, s026, s028, s052, s137, s208, s230-s233, s266, s274-s278). Fix 5 goes to the director, plus the illustrator only if new assets are wanted. Fix 9 goes to the art director. Re-screen only the re-keyed shots in round 2.

## Round 2: re-keyed shots (2026-10-09)

Scope: the 20 re-rendered shots on `build/contact/sheet_01..02.png` (s025, s026, s028, s052, s055, s083, s123, s137, s146, s154, s189,
s207, s208, s209, s217, s232, s264, s266, s275, s277), with full-res checks of s025, s028, s052, s123, s137, s154, s189, s208, s232, s275 and s277.
I also checked continuity against `shotlist.json` (s024-s027 Doug gear and goose asset; s274-s279 narration).

VERDICT: FAIL

All of the round-1 fixes landed. Two small new defects in re-keyed shots block the pass: a text collision (s154) and a stray line on Doug in the new
s232 close-up. Each one is a one-element shotlist edit. Re-key s154 and s232 only.

### Round-1 fixes: verified
- **1. s025/s026 goose continuity: fixed.** Doug has `cap_off` and the goose is `canada_goose_cap` in s024, s025 and s026. The cap returns at the s027 chapter
  card. s025 is down to 2 labels (POND on the pond, DIGNITY + LAST WORD). The goose's cap is small at 1080p but it reads as red on the head, and it matches s021-s024.
- **2. s208 label collision: fixed.** The 27 FATAL box bottom is at about y 703 and Doug's cap top at about y 745, so they are clear.
- **3a. s274-s278 variety: fixed.** s275 is now a head-and-ears close-up that fills the frame, with small Doug bottom-left and white sound arcs going toward the elephant.
  "Listened very carefully" reads in 1 s. s277 is a tighter two-shot: large smiling Doug, a green tick over him, and the elephant at 1.1 scale. It reads as
  "Doug really is harmless: correct", which sets up "It did not matter" (s278) and the s279 death. The run is now wide / close / wide / two-shot / wide.
- **3b. s230-s233 variety: fixed.** s232 is a 2.6x push-in on the bear's head with tiny shocked Doug left, so it breaks the run. See fix 2 below for one new problem.
- **4. s028: fixed.** The cat sits at the bottom-left of the card, well clear of "MOST CONFIDENT".
- **5. s083: fixed.** There is one label, "MOOSE + ELK + BISON", over the moose.
- **6. s052: fixed.** The red arrow tip stops about 25 px above the red figure's head and reads as a pointer.
- **7. s266: fixed.** The high-pitch red wave is now above the black MEN wave, with an up arrow between them that agrees with "PITCH UP".
- **8. s137: fixed.** The 27 KG suitcase rides on the chimp's back.
- **9. s217: fixed.** The threat aura behind the silhouette is now a sparse grey speckle and no longer reads as red spray.
- **Art-director shots, also clean:** s055 (FEMALE / MALE 2x, 2 labels), s123 (bag tipped on the ground, seeds spilling, label upright), s146 (blue dots,
  10th chimp unmarked, nothing reads as blood), s189 (cream diagram, croc and car on separate baselines, 6 M line clear, about 150 px gap), s209 (about 100 px of
  sand between snout and Doug), s264 (BOYS clear of the sun), s207 (2 labels plus map, clean).
- **Policy:** no gore and no kids-show tone in any re-keyed shot. The s232 bear is a neutral side-on head with no open mouth.

### Required fixes
1. **s154 (director): cap over the citation.** The `doug_cap` asset at (800, 745) sits on the white "PNAS 2017" card and covers the "NA" of "PNAS". This was
   present in round 1 and I missed it. It is text overlapped by a drawing. Change: move the cap onto the log next to the card, at about x 960, y 790
   (scale 0.35, sitting on the log top), or move the card to x 520 and keep the cap where it is. Check that no part of the cap touches the card.
2. **s232 (director): stray line on Doug.** The ice-crack line `[[200, 820], [420, 812]]` starts exactly at Doug's cap brim (Doug is at x 170, scale 0.4).
   It reads as a long pole sticking out of his cap or face. Change: delete that line, or move it to `[[330, 960], [560, 952]]`, clear of Doug.

### Recommended (not blocking)
3. **s232 (illustrator/director):** at 2.6x the `polar_bear` asset shows two artefacts: the near foreleg's black outline pokes above the chest line as a
   small spike (about x 1355, y 810), and the grey far-leg stroke crosses the body diagonally (about x 1565,670 to 1460,960) like a crease. At this
   scale it reads as a stray line. Moving the bear will not hide it, because the spike sits mid-frame. The fix is in the asset: the illustrator
   ends the foreleg outline at the chest line. The grey stroke can stay. It is invisible at the asset's normal 0.85 scale, so this does not block s232.
4. **s277 (director, optional):** the green tick at (494-626, 400-520) floats in the sky band. It would tie to Doug more clearly about 60 px lower, nearer his head.

Routing: fixes 1-2 go to the director (re-key s154 and s232). Fix 3 is optional and goes to the illustrator (`polar_bear` asset). Fix 4 is optional and goes to the director. In round 3 I will re-screen only s154 and s232.

## Round 3: re-keyed shots (2026-10-09)

Scope: full-res `build/keyframes/s154.png`, `s232.png` and `s277.png` (rendered 09:36, same time as commit 051581f), with a zoomed crop of the s232
foreleg. I also checked the shared `polar_bear` asset edit by re-keying ep 008 s195, s198, s208, s214 and s220 (scales 0.3 to 1.0), with a zoomed crop
of the s198 chest/foreleg joint.

VERDICT: PASS

### Round-2 fixes: verified
- **1. s154 cap over citation: fixed.** `doug_cap` now sits on the log top at about x 925-995, y 778-802. That leaves about 35 px of clear log between the
  cap and the right edge of the "PNAS 2017" card, and "PNAS 2017" reads in full.
- **2. s232 stray line: fixed.** The ice-crack line at Doug's cap brim is gone. Doug (shocked, cap on, on-model) stands alone at the left with clean space
  around him. The close-up still breaks the s230-s233 run, and "THE HUNGRY ONE" reads in 1 s.
- **3. s232 foreleg spike (optional): fixed.** The new chest fill patch hides the foreleg outline, so it now starts at the chest line. Only a ~5 px
  square end-cap is visible at about x 1352, y 855, and it is not noticeable at 1080p. The grey far-leg stroke is unchanged, as allowed in round 2. The one
  short pale ice-crack line left of the leg (about x 1250-1345, y 900) reads as ice, not as a stray stroke.
- **4. s277 tick (optional): fixed.** The green tick moved down 60 px (bottom at about y 585). It now sits just above and right of Doug's cap (top at about
  y 655), so it clearly belongs to him. It overlaps the edge of the sun a little, which is fine.

### Shared asset check (ep 008)
- The `polar_bear` edit does not break anything in ep 008. In s195, s198, s208, s214 (two bears, 0.9 and 0.7) and s220 (0.3), the chest/foreleg joint is
  clean, with no gaps, holes, or fill showing past the outline. The silhouette, radio collar (s208) and -22% comparison (s214) are unchanged. Re-keying ep 008
  is not needed. If it has already rendered, the new asset only removes a hidden spike.

### Policy
- No gore and no kids-show tone in the three shots.

Routing: none. Keyframes for 011 are cleared for render from the visual side. The post-render screen (samples, qc.json, thumbnail, shorts) follows the build.

## Round 4: thumbnail (2026-10-09)

Scope: `build/thumbnail.png` (1280x720), `build/thumbnail_small.png` (320x180) and `build/thumb_168.png` (168x94, upscaled
view), plus zoomed crops of Doug, the goose, the wolf, the kangaroo and the bottom-right corner (duration-badge zone). Checked
against the title in `metadata.json`, the `thumbnail_brief`, and style bible section 2.B.

VERDICT: PASS

### Readability
- **1280:** All ten labels are spelled right, in Title Case, uncropped, and do not overlap the drawings: Elephant, Gorilla,
  Crocodile, Polar Bear, Grey Wolf, Cassowary, Chimpanzee, Goose, House Cat, Kangaroo. Each animal is recognisable at once.
- **320 (feed/sidebar):** The stepped pyramid reads in 1 s as a size/danger ladder from bottom to top. The elephant, crocodile,
  polar bear, gorilla, goose and cat silhouettes are clear. Of the labels, "Elephant", "Gorilla", "Crocodile", "Polar Bear",
  "Goose", "House Cat" and "Kangaroo" are readable. "Cassowary" and "Chimpanzee" are only just readable, which is acceptable
  for a table-of-contents grid.
- **168 (mobile suggested):** The labels are not readable, as is normal for this archetype. The colour-band ladder and the
  elephant/croc/bear shapes still carry it.
- **Duration badge:** "Kangaroo" ends at about x 1165, so the bottom-right badge zone (about x 1185+, y 690+) covers only
  empty yellow. Nothing important is hidden.

### Errors / drawing check
- Doug is on-model: red cap, white head, red boxing gloves, guard up with the lower glove joined by its arm, smug closed-eye
  grin. He is a red speck at 168 px, which matches the brief ("tiny Doug") and bible 2 ("the stick man is never the hero").
- No stray lines, gaps or broken fills. The wolf's legs are a bit stiff and post-like, but it clearly reads as a wolf.
- No hippo, and all ten chapter animals are present, matching the brief.

### Policy
- **Gore:** none. The croc's open jaws and the goose's serrated hiss are threat cues with no blood or wounds.
- **Kid appeal:** low risk. The colours are bright, but every animal is posed aggressively (hissing goose, ears-back cat,
  open-jawed croc, ears-out elephant) on a band that darkens to near-black at the top. The boxing Doug and the "Until He Dies"
  title make it adult-coded. There are no baby faces, pastels or nursery framing.
- **Not misleading:** every pictured animal is a chapter. The thumbnail does not repeat the title's words, so the title gives
  the frame and the thumbnail gives the items.

### Optional polish (not blocking)
1. Graphic designer: the bottom-row labels (Goose / House Cat / Kangaroo) sit about 4 px above the bottom border. They read
   fine, but raising them about 8 px would give the same breathing room as the upper tiers.
2. Graphic designer: the kangaroo is the smallest and most passive figure. If the art is touched again, a boxing/rearing pose
   or a slightly larger scale (about 0.24) would make it read as a threat at 320 px.

Routing: none required. The thumbnail is cleared from the visual side.

## Round 5: revised thumbnail (2026-10-09)

Scope: the re-render made after the creative director's round 1 changes (`canada_goose_attack`, `red_kangaroo_kick`,
`polar_bear_standing`, resized subjects, Doug `point` with rig-anchored gloves). Checked `build/thumbnail.png` (1280),
`build/thumbnail_small.png` (320) and `build/thumb_168.png` (viewed at 4x), with pixel zooms of Doug, every label/drawing gap,
and every place a subject meets a band outline. Round 4 above screened the previous render (09:42); this render is from 09:44.

VERDICT: FAIL (one small required fix; everything else passes)

### Required fix
1. **Graphic designer, bottom tier is clipped by the orange band's outline.** `gen_tiers.py` draws the orange rect *after* the
   yellow-tier assets, so its 6 px outline (y about 553-559) paints over the tops of the three bottom subjects:
   - Goose (`canada_goose_attack`): the raised far wing is cut flat at y 559 (about x 420-470). At 1280 and in s001 at 1080p
     it looks like the wing was cropped.
   - House Cat: the tail tip is sliced flat against the outline (about x 675-690).
   - Kangaroo: the ear tips are cut by the outline (about x 1050-1065).
   Fix: lower or shrink these three so each top clears the yellow band's top outline by at least 6 px (top at y 565 or lower).
   For example, goose scale 0.30 to about 0.28, cat y +6, kangaroo scale 0.207 to about 0.20. **Do not** fix this by changing
   the draw order: the goose wing would then rise into the orange band and come close to the "Grey Wolf" label (bottom at
   about y 545). After the change, keep the kangaroo's tail tip clear of the "Kangaroo" label (it is about 6 px clear now) and
   re-check that no label touches a drawing. This is also s001, so the editor re-renders s001 as already routed.

### Checks that pass
- **Doug's boxing stance:** now correct. The jab glove sits exactly on the extended hand and the rear glove sits on the
  lowered hand's endpoint, attached to its arm with no floating glove. Facing right, he squares up to the goose about 130 px
  away. He is on-model (red cap, white head, black stick body) with the closed-eye smirk, at scale 0.26. He reads as a tiny
  red-capped speck with red gloves at 320 px and as a red dot at 168 px, which is acceptable for "tiny Doug".
- **Threat poses:** the attack goose (wings up, serrated beak open), kicking kangaroo (both feet out, motion lines) and
  reared polar bear are big improvements. The bottom tier no longer reads as a petting zoo at 320 px. At 168 px the goose
  reads as a goose with wings up, and the kangaroo as a brown rearing figure.
- **Subject size:** all subjects now fill their tiers. The cassowary reads as a dark bird with a blue head at 320 px (no
  longer a dot).
- **Label/drawing contact:** none. Wolf paws, cassowary feet and chimp knuckles each clear their labels by about 5-8 px, and
  the gorilla feet, croc jaw and polar bear paws clear theirs by about 3-6 px. The bottom labels have been raised and clear
  the bottom outline. All ten labels are spelled right and uncropped, and the duration-badge zone (bottom-right) covers only
  empty yellow.
- **Gorilla and polar bear heads** overlap the red band's top outline into the white, drawn on top. This reads as a
  deliberate frame break, not a crop, so it is fine. The gorilla does not touch the elephant panel.
- **Readability:** at 320 the pyramid, the colour ramp and 8 of 10 labels read in 1 s (Cassowary and Chimpanzee only just).
  At 168 the labels are illegible, as expected for archetype B, and the elephant, croc, gorilla and goose carry it.
- **Gore:** none. The polar bear's open mouth is a dark-red interior with teeth. It reads as a snarl, not blood, at every
  size. The croc's open jaws show no wounds.
- **Kid appeal:** low. Every animal is aggressive except the stiff wolf and the cassowary. The ramp darkens to near-black,
  and nothing has baby proportions, pastels or nursery framing. The cat (crouched, hissing) is the softest figure, but it is
  acceptable next to the attack goose and kicking kangaroo.
- **Title fit:** it complements "Every Animal Doug Could Beat in a Fight, Until He Dies" without repeating any title words.
  Every animal shown is a chapter and there is no hippo, so it is not misleading.

Routing: graphic designer (fix 1), then visual screener re-check of the bottom tier only, then creative director.

## Round 6: thumbnail bottom-tier re-check (2026-10-09)

VERDICT: FAIL (one small fix; everything else passes)

### Round 5 fix verified
- **Bottom-row clipping is fixed.** The yellow band's top outline runs y 553-559. The highest drawn pixels are now: goose wing
  tip y 566, cat tail tip y 565, kangaroo ear tips y 565 and Doug's cap y 565. All are at or below the y 565 target and none
  is cut flat. At 3x zoom the goose's raised far wing is whole with a ragged primary edge, the cat's tail ends in a rounded
  tip and both kangaroo ears are complete.
- **Goose to "Goose":** 6 px clear (feet at y 670, label from y 677). **Kangaroo tail to "Kangaroo":** 5 px clear (tail at
  y 671, label from y 677). **Doug:** no label, and the gloves and feet are clear.
- **Feed size (320 / 168):** the bottom row reads the same as in Round 5. The goose (wings up), the orange cat and the brown
  kicking kangaroo are recognisable at 320 px. At 168 px the tier still carries the pyramid and colour ramp. Nothing
  regressed in the upper three tiers, and their labels, clearances and frame-breaking heads are unchanged.

### Required fix
1. **Graphic designer: "House Cat" now almost touches the cat.** Moving the cat down 6 px (y 673, scale 0.362) closed the gap
   to its label. The front paw's claw/scratch pixels end at y 675 (x about 802) and the top of the "C" starts at y 677
   (x 802-812). That leaves 1 empty row (2 px), and the haunch at about x 712-720 ends at y 676, right above the "H"
   stem. At 1280, and after s001 is compressed at 1080p, this looks like contact. Fix: in `thumbnail.json`
   (via `gen_tiers.py`), move all three bottom labels "Goose", "House Cat" and "Kangaroo" from y 688 to y 692, so
   their baseline stays shared. Label bottoms move to about y 705-708, still 5 px or more above the bottom outline at y 713. Then the
   cat has about 6 px of clearance, the goose about 11 px and the kangaroo about 10 px. Do not move the cat back up,
   because its tail would hit the outline again. Re-render s001 with the thumbnail as already routed.

Routing: graphic designer (fix 1), then visual screener (cat/label gap only), then creative director.

## Round 7: thumbnail bottom-label re-check (2026-10-09)

VERDICT: PASS

### Round 6 fix verified (labels at y 690)
- **"House Cat" vs cat:** the cat's lowest pixels (haunch, x 716-720) end at y 676, and the label tops start at y 679. That
  leaves 2 empty rows. The closest label pixels are the "H" stem at x 692-700, which does not sit directly under the
  haunch. The claw pixels end at y 675 (x ≤ 803). At 1280 and at 2x zoom there is a visible yellow gap with no contact.
- **"Goose":** the feet end at y 670 and the label starts at y 679, so 8 rows are clear.
- **"Kangaroo":** the tail ends at y 671 and the label starts at y 679, so 7 rows are clear. The "g" descender ends at y 709 and
  the band's bottom outline starts at y 713, so 3 rows are clear. Every other label bottom is at y 703.
- **Overall:** the shared baseline holds across all three labels and Doug has no label. The upper three tiers are unchanged from
  Round 6 (all PASS). Nothing touches or is cropped at 1280 px.

No fixes. Routing: creative director (package approval).

## Round 8: post-render check, final.mp4, thumbnail and Shorts (2026-10-09)

### Main video (final.mp4, 910.5 s; qc.json reports no problems)
- **Samples f_001-f_030 and the final frame:** no black, blank, frozen or glitched frames. Each chapter has its own
  background (meadow, brick wall, desert, night forest, rainforest, misty highland, estuary, ice, sunset savanna), so no
  run of near-identical compositions. The chapter tag at top centre and the DOUG DEATHS counter (93 to 100, rising once per
  chapter) are legible and never overlap the drawings.
- **Doug:** on-model in every sample (red cap, white head, black stick body). He is readable on every background, including
  the night forest, the ice and the dark red savanna. On the dark end card his outline is white and still reads clearly.
- **Drawings:** all ten animals are recognisable (goose, cat, kangaroo, wolves plus moose, cassowary and its foot,
  chimp, silverback, crocodile vs car scale, polar bear, elephant). The comparison graphics (1.00 vs 1.35 bars, 6 M croc
  vs car, poll box, Australia map, timeline) are clean and spelled correctly.
- **Policy:** deaths are cartoon only (X-eyes Doug with dropped cap and gloves, Doug's ghost floating up, a dust-cloud
  brawl, an empty cap on the birdseed bag). There is no blood. I zoomed in on the dark red in the gorilla and polar-bear
  mouths: it is mouth interior with white teeth, not gore. The tone is adult and not nursery-like.
- **Advisory, no fix needed:** f_001's poll box is mostly empty white. This is a build-up frame and it fills in later.
  f_024 shows a "POLAR BEAR" label that repeats the chapter tag. It is redundant but harmless.

### Thumbnail (build/thumbnail.png, thumb_168.png)
- Unchanged from the Round 7 PASS. The labels are clear of the drawings, nothing is cropped, and there is no blood or
  hippo. At 168 px the coloured pyramid, the elephant at the top and the crocodile jaws still read clearly.
  It complements the title "Every Animal Doug Could Beat in a Fight, Until He Dies" and is not misleading.

### Shorts (short01-03, 1080x1920; frames at 1/10/20/30/40 s, the end, and the previews)
- **Titles:** the red-on-outline titles wrap to 3 lines, are fully on-canvas and readable, and are spelled correctly.
- **Subtitles:** white with black outline, centred and legible on every background. In the previews and some frames the
  caption is cut mid-word ("tapping a ca", "toge"). This is the word-by-word reveal caught mid-way, not cropping.
- **Framing:** no drawing is cut off at the sides. Two elements are tight to the edge: the left cassowary in short01 at
  about x 30, and Doug in the short02 Rwanda frame at about x 1040. Both are inside the frame. This is advisory only.
- **End cards** (WHO'S NEXT? / WHAT HAPPENS NEXT? / ALL 10 FIGHTS: TAP BELOW): the text is legible, Doug is on-model,
  and the red arrow points straight down to the link area.
- **Death count:** short03's death frame shows DOUG DEATHS: 100, which matches the outro.

No required fixes. Routing: creative director (final approval).

VERDICT (main): PASS
VERDICT (shorts): PASS
