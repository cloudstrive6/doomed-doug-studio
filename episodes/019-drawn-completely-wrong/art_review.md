# 019 art review: new assets (art director)

Date: 2026-10-15. Scope: all 68 new drawings in `asset_requests.md`. I judged them from the illustrators' previews
(`assets/previews/019-*`) and from my own renders: bbox at scale 1 for every asset against the requested extents, the worn
props on Doug (stand / thumbs_up, scale 1 and 0.4), silhouette + red rim on navy for `therizinosaurus`,
`spinosaurus_mystery` and `elasmosaurus_neck_rising`, and real keyframes s050, s056 and s224.

## Verdict: PASS (after two AD fixes below). Two arrow aims go back to the director. They don't block the asset gate.

All 68 assets are on file. Every bbox matches its request within a few units, and nothing overflows its anchor box.
- **Style:** the two tiers are consistent. Creatures and props are detailed (thick black outline, flat fills, interior shading,
  spray texture). Humans are crude (`victorian_woman` and the dinner guests in `iguanodon_mould_dinner`).
- **`old_*` plates:** the eleven plates form a coherent family: brown ink `#5a3a1e`, parchment fills, cross-hatching, stiff
  engraving posture, no text. Each "wrong part" is obvious: boxy head, `?` body, backwards neck, stilt spines and head blob,
  nose horn, elephant legs, roof tiles and wrist spikes, turtle shell and flipper claws, and the four Spinosaurus postures.
  The pale `#fff8e0` highlight on claws, teeth and spikes is shared by the whole set and reads well on `old_drawing_card`.
- **Gore and kid appeal:** no gore anywhere. The Elasmosaurus mouth, the `hallucigenia_head` throat and the Megalosaurus
  mouth are dark-red interiors, not blood. Nothing is cute or kids-show. The gift-shop toys are clearly toys in context, and
  the Doug family photo is our house crude style.

### Fixes made directly in the library
1. **`iguanodon`: the thumb spike was too small.** The spike was about 44 units long, roughly 25 px in a typical shot. That is
   too small for the shots whose whole beat is the thumb (s050-s056). I scaled the cream cone 1.5x about its tip, so the
   tip stays at (+94,-226) and the base now sits in the hand. The s050 "THUMB" arrow still lands on it (verified in the keyframe).
2. **`therizinosaurus`: the claws read as straws.** The six claw polygons were about 17 units thick, so the "huge scythe
   claws" looked like thin bristles, and the silhouette only gave you thin fingers. I widened every claw blade about 1.7x
   around its centre line. Length, tips and the requested claw position (about (+250,-330)) are unchanged. They now read as
   broad scythes in colour and in silhouette (s224 checked).

### For the director (composition, not blocking)
1. **s178 arrow:** it lands at about (-150,-108) in `hallucigenia_head` space, which is about 40 units below the eyes
   (-150,-150) and (-88,-164). If the line is about the eyes, aim it at about (-120,-160) (screen ≈ (676,408) at x820/y600/scale 1.2).
   If it is about the mouth or teeth, aim it at the right-hand mouth ring or the dashed throat window instead.
2. **s249 arrow:** it lands at about (-160,-60) in `homo_diluvii_slab_exposed` space, about 90 units below the left front leg
   (-150,-150). Re-aim it to about screen (610,430) so it touches the leg and toes.
3. **`hallucigenia` feet offset (illustrator flag):** the legs are not exactly under the spine pairs, and the head-end
   tentacles bunch up. That is fine at the scales used. If a shot puts a label or arrow on "legs", aim it at the middle leg
   pairs (x -120..+60, y +60..+100).

### Notes (approved as drawn, optional polish later)
- `elasmosaurus` / `elasmosaurus_underwater_body`: the tail tapers a little long, but the neck is still clearly the longest
  part, so the real animal reads correctly against `old_elasmosaurus_backwards`.
- `therizinosaurus`: the small triangle "feather tufts" read slightly as thorns. It still reads as shaggy at video scale.
- `big_shield`: oval rather than round, carried beside Doug's body per the requested bbox (x -10..150). Head, cap and
  face stay clear. Approved.
- `fencing_mask`: the mesh pushes slightly forward of the face, like a real mask in profile. Eyes and mouth read through,
  and the cap is untouched (checked on stand and thumbs_up). It is not mirrored for `facing: left`. Keep Doug facing right
  in s055-s058, which is how they are laid out.
- `old_drawing_card`: at 0.14 in Doug's hand, the header is not legible, but the card and drawing read as an "old card".
  This is as intended.

### Per-asset status
| asset | status |
|---|---|
| old_drawing_card | APPROVED |
| gift_shop_shelf | APPROVED |
| old_brontosaurus_boxy | APPROVED |
| old_deinocheirus_arms | APPROVED |
| old_elasmosaurus_backwards | APPROVED |
| old_hallucigenia_1977 | APPROVED |
| old_iguanodon_nosehorn | APPROVED |
| old_megalosaurus_quadruped | APPROVED |
| old_spinosaurus_1915 | APPROVED |
| old_spinosaurus_2014 | APPROVED |
| old_spinosaurus_2020 | APPROVED |
| old_spinosaurus_2022 | APPROVED |
| old_stegosaurus_roof | APPROVED |
| old_therizinosaurus_turtle | APPROVED |
| allosaurus_vertebra | APPROVED |
| apatosaurus_skull | APPROVED (clearly distinct from camarasaurus_skull) |
| camarasaurus_skull | APPROVED |
| big_shield | APPROVED |
| brontosaurus | APPROVED |
| brontosaurus_foot | APPROVED |
| chalkboard | APPROVED |
| classic_museum | APPROVED |
| crystal_palace_iguanodons | APPROVED |
| crystal_palace_megalosaurus | APPROVED |
| deinocheirus | APPROVED |
| deinocheirus_arm_bone | APPROVED |
| deinocheirus_eating | APPROVED |
| dimetrodon | APPROVED |
| dimetrodon_tooth | APPROVED |
| dollar_bill | APPROVED |
| elasmosaurus | APPROVED (note) |
| elasmosaurus_neck_rising | APPROVED (silhouette checked) |
| elasmosaurus_underwater_body | APPROVED (note) |
| family_photo_frame | APPROVED |
| fencing_mask | APPROVED (checked on Doug) |
| fossil_crate | APPROVED |
| giant_salamander | APPROVED |
| gizzard_stones | APPROVED |
| glass_display_case | APPROVED |
| hallucigenia | APPROVED (feet offset: director note 3) |
| hallucigenia_head | APPROVED (s178 arrow: director note 1) |
| homo_diluvii_slab | APPROVED |
| homo_diluvii_slab_exposed | APPROVED (s249 arrow: director note 2) |
| iguanodon | APPROVED (AD fix 1) |
| iguanodon_mould_dinner | APPROVED |
| iguanodon_skeleton | APPROVED |
| iguanodon_teeth | APPROVED |
| iguanodon_thumb_spike | APPROVED |
| iguanodon_thumbs_up | APPROVED |
| journal_paper | APPROVED |
| megalosaurus | APPROVED |
| megalosaurus_bones | APPROVED |
| ping_pong_table | APPROVED (side/length view) |
| ping_pong_table_end | APPROVED (end/width view, clearly different) |
| salamander_outline | APPROVED |
| sauropod_skeleton_headless | APPROVED |
| spinosaurus_mystery | APPROVED (silhouette + rim checked) |
| stegosaurus | APPROVED |
| stegosaurus_fossil_slab | APPROVED |
| stegosaurus_tail_spike | APPROVED |
| synapsid_skull | APPROVED |
| tall_ladder | APPROVED |
| tennis_court_side | APPROVED |
| therizinosaurus | APPROVED (AD fix 2) |
| therizinosaurus_claw | APPROVED |
| us_quarter | APPROVED |
| victorian_woman | APPROVED |
| water_plants_bunch | APPROVED |

68 / 68 APPROVED, 0 REVISE.

---

# 019 keyframe review (art director)

Date: 2026-10-15. Scope: all 293 keyframes (`build/contact/sheet_01-25.png`). I opened s083, s215, s286 and s288 at full 1080p
and checked the element coordinates in `shotlist.json` for every shot listed below. Thumbnail pick is at the end.

## Verdict: FAIL. 1 blocking policy fix (asset), 22 composition fixes (director). The rest of the episode passes.

What passes: Doug is on-model in every shot (red cap, head about 1/3 of his height, oval eyes, ghost/death poses correct).
Chapter colours hold within each chapter. The counter runs 154 to 161 in the right places. Title cards read clearly, and the
OLD DRAWING cards stay a recognisably detailed tier next to crude Doug. Nothing is cropped by the frame edge.

### A. Illustrator (asset). BLOCKING
1. **`spinosaurus_mystery` (s286, s288)**: the drips that hang from the jaw tip are part of the silhouette, so they get the
   red rim. On black they read as **blood dripping from the mouth** (clearest at s288, x 1740-1780, y 420-530). This breaks
   "never gory". Remove the drips from the silhouette polygon. If you want water, redraw them as separate light-blue droplets
   (`#bfe6ff`, no red rim) a little away from the jaw. Re-preview it on navy and on the orange s288 background. I approved
   the asset on navy, where the drips didn't show. My mistake.

### B. Director (composition). Fix before art_approved
Text/wordart sitting on the floor line and the bottom edge of the card (all are wordart/labels at y 980-1000 on top of the
`y 1000` floor line):
2. **s092** `LIKE A SHELL`, 3. **s145** `CLAWED HUNTER`, 4. **s216** `WATER PLANTS`, 5. **s218** `TURTLE-SHAPED`,
6. **s270** `UPRIGHT HUNTER`, 7. **s274** `SWAM`: move the wordart to the free right margin, about (1600, 440),
   size 56-64. That's the slot s063/s089/s170 already use, so the card shots stay consistent.
8. **s251** `SALAMANDER` (860, 990) runs into the bottom of the slab: move it to about (1450, 420).
9. **s217** `CHELONIFORMIS` label (820, 990) straddles the floor line: move it to (1600, 430).

Labels/wordart overlapping a drawing or another label:
10. **s215**: the `4.5 m` dimension line (y 330) and label (820, 300) run straight through the card header, so
    "OLD DRAWING" and "1954" become unreadable. Move the line and label below the turtle, inside the card (y about 870), or
    above the card (y about 225).
11. **s018** `OLDER NAME WON` (1120, 360) overlaps the right edge of the card: x 1300.
12. **s026** `THE NAME IS BACK` (1120, 360) has the same overlap: x 1320.
13. **s172**: the `1991` label (330, 330) sits on the card's top-left corner and header: move it to (1600, 430).
14. **s259** `STILL A SALAMANDER` (1300, 330) overlaps the right edge of the glass case: x 1450 (or size 48).
15. **s178**: `EYES` (400, 290) sits on the top-left corner of the head panel and `TEETH` (1180, 330) sits on its top-right
    corner. Move EYES to about (250, 380), outside the panel (re-aim the arrow from there), and TEETH to about (1450, 470).
16. **s275**: the `ABOUT 15 m` label (850, 730) sits on the middle giraffe's head and hides the "1" of 15. Move the
    dimension line and label to y 690 and the label to x 1015, between two giraffes.
17. **s017**: the `APATOSAURUS` label (1260, 900) covers the scientist's legs (1180, 860). Move the scientist to x 1440.
18. **s066**: the scientist (620, 860) stands with his head inside the vertebra row (y 620). Move him to x 1420.
19. **s071**: `journal_paper` (1090, 700) covers Marsh's face (scientist at 1200). Put it at his hand, about (1110, 800).
20. **s268**: the `MUNICH` label (820, 380) is half-hidden behind the dust cloud and reads "MUNICH" clipped. Move it to y 315
    or drop it (s265-s267 already establish Munich).
21. **s063, s170**: the red arrow starts on top of the "OLD DRAWING" header text. Start it outside the card on the right
    (by the wordart) and curve it in.

Map edges (the world_map border shows as a black bar and an empty strip):
22. **s008, s064, s191**: the left edge of the map is visible at x of about 30-40. Scale `world_map` 2.6 to 2.8 and re-centre
    so the red circle stays put, or shift x so the border is off-frame.
23. **s148, s149**: the top edge of the map (black line at y of about 135) is visible: scale 2.2 to 2.4 or move y down to about 1120.

Doug standing on water:
24. **s080, s084**: Doug uses `point` / `panic1` at the sea line (y 560), so he stands on the water up to his ankles, while
    s082/s083 have him swimming. Use `swim1/swim2` (holding the card for s080), or put him on the island next to the
    time machine.

### C. Notes (not blocking; director's call)
- **s083**: the narration line is "The long end has a mouth", but the neck is a black silhouette, so you can't see a mouth.
  A small `TEETH`/`MOUTH` arrow, or the coloured neck with teeth as in s079, would land the line.
- Repeated compositions: s019-s022 (the same headless-skeleton frame 4 times, only the label changes), s013-s015 and
  s169-s171 (the same card + Doug 3 times, only an arrow or wordart changes). These are under the 5-in-a-row limit, but a
  push-in or a Doug pose/position change on the middle shot of each run would help pacing.
- s205: the red X over the `RELATIVES` plaque makes the word hard to read. Fine as a gag, or move the X to the toy set.

## Thumbnail pick: `thumbnail.json` (A, labelled 4x3 grid). Winner confirmed
- The grid is the designer's recommendation, it's the opening image (s001 = the grid, per decisions.md item 8 and style bible
  "open with the thumbnail grid"), and it pairs with the list-style title. At feed size (`thumbnail_small.png`, 320 px)
  all 11 silhouettes and red X's read and the labels are still legible. It's on-palette, subject-first, not gory.
- `thumbnail_b.json` (FAKE HEAD hero card) is clean and readable, but it sells only item 1 and doesn't match the opening frame.
  Keep it as the A/B backup.
- `thumbnail.json` already holds the grid spec, so nothing needed copying. `thumbnail_b.json` is left unchanged as the alternate.
- Optional polish for the designer: the Dimetrodon tile shows the *real* Dimetrodon under an X, while every other tile shows
  the old wrong drawing. The toy-set plate from s189 (`gift_shop_shelf` with its "DINOSAURS" sign) would match the tile grammar.
  Not blocking.

Re-review needed: the shots in B after the director's patch, plus s286/s288 after the illustrator's asset fix.

---

# 019 keyframe review, round 2 (art director)

Date: 2026-10-15. Scope: all 25 re-rendered sheets (`build/contact/sheet_01-25.png`). I compared the shotlist against `d93e529`
(42 shots changed: s008 s017 s018 s026 s054 s063 s064 s066 s071 s080 s083 s084 s092 s099 s145 s148 s149 s157-s160 s170 s172 s178
s190 s191 s205 s215-s218 s251 s259 s268 s270 s274 s275 s287-s291). I checked every one on the sheets, and opened s071, s083,
s178, s215, s218, s286 and s288 at full 1080p.

## Verdict: PASS. All blocking items from round 1 are fixed. One leftover is optional polish (s071) and does not block art_approved.

### A. Blocking asset fix: verified
1. **`spinosaurus_mystery` (s286, s288): FIXED.** The jaw drips are gone from the silhouette polygon. At full size on the teal
   water (s286) and the orange river (s288), the red rim follows only the snout, back spines, body and tail. Nothing hangs
   from the mouth, and nothing reads as blood. The silhouette is still a clear "unknown shape" for the Shorts end card.

### B. Composition fixes 2-24: verified
- **Wordart/labels off the floor line:** s092, s145, s216, s218 (now a new frame with the turtle costume, and Doug is on-model:
  cap, head, oval eyes), s270 and s274 all sit in the right-hand margin, matching s063/s089/s170. s251 SALAMANDER and s217
  CHELONIFORMIS are clear of the slab and the floor.
- **Overlaps:** s215 `4.5 m` now sits above the card, and "OLD DRAWING 1954" is fully readable. s018 and s026 wordart clear the card.
  s172 `1991` is off the header. s259 clears the glass case. In s178, EYES sits outside the panel and its arrow lands on the eye,
  and TEETH sits in the right margin. s275 `ABOUT 15 m` is between the giraffes with the "1" visible. In s017 the label is clear
  of the scientist. In s066 the scientist is out of the vertebra row. s268 drops the MUNICH label, and the dust cloud no longer
  has gag stars (this also covers the visual screener's tone note). s063 and s170 arrows start outside the card.
- **Map edges:** in s008, s064 and s191 the left border is off-frame. In s148 and s149 the top border is off-frame.
- **Water:** in s080, Doug stands on the island with the card. In s084 he swims. The s157-s160 and s287-s291 river is now water
  blue `#3a9ad9` with wave ticks, so the s289 splash reads as Doug going in.
- **Notes that were also taken:** s083 has a MOUTH arrow on the head. s099 has an original chalk spike-tail doodle (not
  Larson's panel). s205 no longer has the X over RELATIVES. In s190 the X sits on the DINOSAURS plaque, which is the point
  of the line "It is not a dinosaur", so it is approved.

General: Doug is on-model in every changed shot. Chapter colours are unchanged. The counter runs 154 to 161 correctly. No new
crops or overlaps.

### Optional polish (director, non-blocking)
1. **s071:** `journal_paper` at (1110, 800) still covers Marsh's left eye. The asset is anchored at its centre and is about
   190 px tall, so my round-1 coordinate was too high. That was my mistake. Move it to about **(1090, 880)** so its top edge
   sits below his chin (head bottom at about y 760). Marsh still reads as holding the paper as it is, so this does not block.

Re-review needed: none. The keyframes are approved for `art_approved`.
