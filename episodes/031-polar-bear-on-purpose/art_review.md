# 031-polar-bear-on-purpose: art review, assets (art director, 2026-10-29)

**Verdict: PASS.** All 35 new assets are APPROVED. I made one small fix myself (`thermal_bear_face` mouth). One composition fix
goes to the director (`tent_dented` placement in s173/s174). No asset needs to go back to the illustrator. This review covers the
asset gate only. Keyframes get their own review once the director's fix is in and the full `keyframes` run is done.

## How I reviewed
- Sheets: `assets/previews/031-polar-bear-on-purpose-assets-a.png`, `-b.png`, `-c.png`, `-paw.png`. Sheet cells crop the
  tall assets (`polar_bear_rearing`, `stick_sprinter`), so I re-rendered those at full size.
- Fit tests (scratch renders in `/tmp/ar031/`, not kept):
  - `arctic_map` with red dots at the four requested local points.
  - `polar_bear_thin` + `polar_bear_thin_collar` flipped at 0.9 (the s182 setup).
  - `polar_bear` beside `polar_bear_black_skin` at 0.85.
  - `polar_bear_paw` beside `ruler` at 1.4.
  - Readability rows: `polar_bear_running` and `polar_bear_thin` at 0.18, `paw_print_icon` at 0.3 beside a BEAR readout label,
    `ringed_seal` at 0.14, `polar_bear_sniffing` at 0.16.
  - `ringed_seal` inside `snow_lair_cutaway` at local (-40,+140) 0.45 on the shot bands (sea ice +140..+260, water `#3a9ad9`).
  - `holding_cell` / `cell_bars` with a bear and with Doug.
  - `snow_shelter` with Doug in `sit`; `doug_cap` on `snow_shelter_broken` and on `tent_collapsed`.
  - `thermal_screen` + `thermal_bear_face`; Doug with `thermal_camera`.
  - The town set on the dusk street `#3b4a6b`.
- Keyframes s092, s173, s174 (the shots where I had doubts about how an asset reads in place).

## House check (all 35)
- Two tiers are correct. Creatures, places and props are the detailed tier: dark outlines, flat fills, grey-blue interior shading
  and spray texture. `stick_sprinter` is the crude tier: 5 px lines, round head with grey crescent, `auto_ink`, no cap.
- Every bear pose is one design family: cream `#f4f1e4`, grey-blue `#c9d6e2` far legs and belly, small hard eye, long neck.
  None of them is cute (no big eyes, no smile, no blush).
- Brief 7 checks:
  - No cubs.
  - No claws in anything; `polar_bear_paw` shows claws on bare ice only.
  - No blood. The only red is the `#7a0d0d` mouth on `polar_bear_lunge`, which is the art bible's mouth colour and matches
    `polar_bear_standing`.
  - No seal kills.
  - No text on the map. The sign board, cell tag and race bib are all blank.
- Everything is readable at its smallest use. The 10-icon running and thin rows still read as polar bears at 0.18. The paw print
  reads as a paw at 0.3 next to the readout.

| # | Asset | Verdict | Note |
|---|---|---|---|
| 1 | `paw_print_icon` | APPROVED | Bean palm pad, five toe pads, claw dots, flat `#1a1a1a`. Reads at 30 px beside the label. Nothing like 013's ruler. |
| 2 | `polar_bear_thin` | APPROVED | Lean, with a dip behind the shoulders and two short hip lines. Head low, not sick-looking, no ribs. Reads at 0.18. |
| 3 | `polar_bear_thin_collar` | APPROVED | Lines up exactly on the thin bear's neck when flipped at 0.9. Blue lens dot visible. |
| 4 | `polar_bear_running` | APPROVED | Long low gallop with snow puffs. Clear silhouette at 0.18. |
| 5 | `polar_bear_sniffing` | APPROVED | Nose to the sky at (+300,-405). Reads flipped at 0.16 on a horizon. |
| 6 | `polar_bear_rearing` | APPROVED | Heavy and predatory, paws turned down for the slam. Reads at 0.5 over the broken lair. |
| 7 | `polar_bear_lunge` | APPROVED | Good burst: drips, bluer submerged hindquarters, anchor at the ice corner (checked in s092). The mouth is the bible's `#7a0d0d`, no fangs. |
| 8 | `polar_bear_swimming` | APPROVED | Flat and long, with `#bcd3e3` shading. Head and back sit on the top edge as asked for s104. |
| 9 | `polar_bear_black_skin` | APPROVED | Same silhouette and bbox as `polar_bear` (verified side by side). Dashed fur line, eye highlight. Diagram look, no anatomy. |
| 10 | `polar_bear_paw` | APPROVED | Exactly the `ruler`'s 30 cm at 1.4. Thick dark curved claws pointing right. The pads are barely visible from above, which is fine for the beat. |
| 11 | `polar_bear_sling` | APPROVED | Calm, eyes closed, rope net, single hook at (0,0). |
| 12 | `tent_dented` | APPROVED (to spec), with director fix D1 | Matches `tent` exactly and the dent plus nose read. But the ragged muzzle end floats on white in s173 (see D1). |
| 13 | `ringed_seal` | APPROVED | Ring markings and an alert head. Adult, not a pup. Sits correctly on the cave floor at (-40,+140) 0.45. |
| 14 | `bearded_seal` | APPROVED | The bushy moustache is the read, with square flippers. Calm. Three at 0.35 stay distinct. |
| 15 | `berry_bowl` | APPROVED | Heap top at (0,-45). Reads at Doug's hand scale. |
| 16 | `berry_bush` | APPROVED | Red and orange leaves, blue-black berries, not green. Low contrast against the `#8a7a4a` tundra, but the black outline carries it. |
| 17 | `caribou_antler` | APPROVED | Main beam, tines and the palmate brow tine. No skull. |
| 18 | `whale_carcass` | APPROVED | Grey hump with a pale rib patch. No red, no flesh. Clean at 0.5. |
| 19 | `rubbish_bag` | APPROVED | Knot at (0,0), grey highlights. Reads on the dusk street. |
| 20 | `rubbish_bin` | APPROVED | Blue-grey `#4a5568` (not green), lid open, bags poking out. |
| 21 | `thermal_bear_face` | APPROVED (fixed by me) | The mouth line was a downturned arc, which read as a sad emoji face. I flattened it to a near-level line with a small centre dip (bear mouth). Now eerie, not cute or sad. |
| 22 | `thermal_camera` | APPROVED | Pistol grip, lens on the right, tiny glow on the screen. Fine at 0.6. |
| 23 | `thermal_screen` | APPROVED | `#1a0f2e` screen, crosshair, corner brackets, tiny IR mark. The face sits well on it. |
| 24 | `stick_sprinter` | APPROVED | Crude tier, generic, no cap, blank bib, no flag or logo. Mid-stride. Clearly not Doug (hair, no cap). |
| 25 | `holding_cell` | APPROVED | Back wall vent, perspective side walls, floor strip, empty. |
| 26 | `cell_bars` | APPROVED | Transparent between the bars. Blank tag plate at the top centre. Lines up with `holding_cell`. |
| 27 | `arctic_town_block` | APPROVED | Two storeys on piles, snowy roof, lit stairwell door at the left. The walls stay light, so Doug and the bear read in front on `#3b4a6b`. |
| 28 | `arctic_map` | APPROVED | Land is grey-tan, not green. All four dot points land correctly: Churchill on the west shore, Hudson Bay water, Svalbard island, Novaya Zemlya west coast. No text. |
| 29 | `holding_facility` | APPROVED | Quonset shape, roller door, drifts. The sign board is blank and centred for the overlay. |
| 30 | `snow_lair_cutaway` | APPROVED | Layers and breathing hole line up with the shot bands. Cave left empty. |
| 31 | `snow_lair_broken` | APPROVED | Same footprint, with the jagged roof hole, fallen chunks and snow puff. |
| 32 | `snow_shelter` | APPROVED | Cutaway with a light interior. Doug's black lines and cap read inside it. |
| 33 | `snow_shelter_broken` | APPROVED | Low block heap with a flat top. The cap sits cleanly on it. No body. |
| 34 | `stairwell` | APPROVED | Landings, flight, handrail, bulb and door all fall within the requested coordinates. |
| 35 | `tent_collapsed` | APPROVED | Flat heap with bent orange poles and a bump for the cap. No body, no blood. |

## Fixes
**Done by me (art director)**
1. `assets/library/thermal_bear_face.json`: mouth curves (elements 24-25) flattened from a frown arc to a level line with a centre
   dip. I re-rendered and checked it on `thermal_screen`. I also regenerated sheet `-b.png`.

**For the director (composition)**
- D1. s173 / s174: `tent_dented` sits at x 1350, scale 0.7, so the muzzle's ragged back end (local x +264, so frame x ~1535) is in
  open white snow. It reads as a floating severed snout (the illustrator flagged this risk). Either:
  - push the muzzle off-frame, for example `tent` + `tent_dented` at x 1720, scale 0.8 (muzzle end past x 1920), and re-aim the
    speech-bubble tail; or
  - draw a flipped `polar_bear` body behind the tent at the right, with its head hidden by the dent.

  Re-render s173/s174 before keyframe review.

**For the illustrator**
- None required.
- Optional, not blocking: `berry_bush` could take a lighter `#a04a2a` rim on its upper leaves so it separates more from the
  `#8a7a4a` tundra at 0.5 and below.

## Overall
**PASS: 35/35 assets approved.** The asset side is ready for `art_approved` once D1 is applied and the keyframes pass their review.

---

# Keyframe review, round 1 (art director, 2026-10-29)

**Verdict: FAIL (minor, 10 fixes).** The style is consistent across all 233 shots (s001 is waiting for the thumbnail and was not reviewed). Doug is on-model
everywhere. The bear family, the zone colours and the death grammar are all correct. Every fix below is a composition or
readability fix, plus one small asset variant. Nothing structural needs to change. Re-run `keyframes` on the listed shots, and
I'll re-check only those.

## How I reviewed
- I went through all 20 contact sheets (`build/contact/sheet_01..20.png`), shot by shot, against style bible section 7 (Art Director rules 1-9) and the art bible.
- I re-rendered 16 doubtful shots at 1080p and cropped them (s044, s047, s065, s067, s104, s120, s123, s132, s135, s138, s139,
  s145, s162, s178, s213, s223). Scratch files are in `/tmp/ak031/` and were not kept.
- I checked the element coordinates in `shotlist.json` for every shot flagged below.

## What passes
- **Doug:** on-model in every shot. He has the round head with the crescent, oval eyes, thin lines and the cap.
  - He auto-inks white on the dark thermal and night shots (s044, s047, s053, s139, s232), as he should.
  - All the expressions come from the allowed set.
  - The seal costume callback (s099-s104, s221) leaves his head, face and cap fully visible.
  - Every death beat keeps the cap in frame and ticks the counter: s026 shelter, s052 thermal, s079 binoculars, s129 cap with speed lines, s174 tent, s200 bowl, s227/s228 detained cap.
  - The ghosts keep the cap. The counter stays flat at 250 through The Town (s152-s155) and at 253 to the end, which matches the series bible.
- **Two-tier rendering:** every bear is in the approved family. The scientist, sprinter and officer are crude-tier humans. There are no cubs and nothing gory. The s151 bear's red mouth reads as a snarl, not blood. The s178 berry pile reads as berries, not a carcass.
- **Zone colours:** the bands step correctly from `#cfe9ff` (1 km) to `#c4dcee` (100 m) to `#b8c8d8` (10 m), and the boss is on slate `#4a5670`. The Town is a night street (logged). Sub-ice water stays at `#3a9ad9`. The olive Thin Bear ground uses the white-to-yellow WordArt override every time (s177-s203).
  The montage (s218-s222) brings back each stop's original colours.
- **Reveals:** the silhouette with red glow comes first, every time: s003, s025, s082, s177, s190, s203, s204.
- **Text:** every caption bar matches its item name. Labels are short, and the second meter sits correctly under the counter.
  The flat-looking wordart on dark shots is the known effect of the dark outline vanishing on a dark background (art bible, boss row). It is acceptable.
- **Variety:** layouts rotate well between field, cutaway, diagram, map, card, thermal screen and cell. The build-up runs stay within the rule:
  lair s006-s013, paw s116-s120, cell s228-s231, and the sober data cards s205-s212.

## Fixes

**For the illustrator (asset)**
1. **`paw_print_icon` disappears on dark backgrounds.** It is a flat `#1a1a1a` fill, so on `#000`/`#2a2a2e` it is invisible, and on `#1b2f5a`/`#3b4a6b`/`#4a5670` it is only a smudge.
   - Add a variant `paw_print_icon_light`: the same shapes, `#f4f1e4` pads with a thin `#1a1a1a` outline.
   - Render a preview at 0.3 next to the BEAR label on `#000000` and on `#4a5670`.

**For the director (composition)**
2. **Swap the BEAR readout icon** (the one at y 238) to `paw_print_icon_light` once fix 1 lands. Same x/y/scale. The shots are s044, s046, s047, s048, s052, s053, s130-s141 (all), s149, s204, s213-s217, s219, s223-s227. Leave s129 as it is: its frame is light at the keyframe.
3. **s065, s067: the scientist's feet are cut off at the bottom edge.** The asset's feet sit at local +149, so at scale 0.5 they land at y 1074.
   Set the `scientist` y from 1000 to **920**, which puts the feet at y 994, level with Doug. In s065, move the telescope down with it if
   it no longer lines up with his eye.
4. **Camp backdrop, s156-s176: the titles and wordart cross the mountain ridges.** The peaks reach y 280-300, and the text sits at y 320-420 (art bible "find clear sky").
   - **Fix:** lower the range in every shot of the set. Keep the base at y 600 and recompute each peak and snowcap point as
     `y' = 600 - (600 - y) * 0.45`. That puts the highest peak at about y 456.
   - **Then check:**
     - s157 "ZERO." and s158 "THE TENT" (y 380, sizes 160/150): glyph bottoms must stay above about y 450. If they touch, drop the size to 140.
     - s156 CAMPING, s159 THE RULES, s164 GREAT DISTANCES, s166 MOST INTERESTING, s170 MADE OF FABRIC, s172 FIRM and s176 NOT READING: keep the wordart y ≤ 400.
     - The s173 bubble tail and the s169 warning triangle move with nothing.
   - Changing the backdrop the same way in all 17 shots keeps the build-up seamless.
5. **Town street, wordart and labels sitting on the buildings.** The roofs of `arctic_town_block` (x 520, y 650, scale 1.0) are at about y 410 (left) and y 470 (right).
   - s132: "STATE OF EMERGENCY" (y 260) touches the left roof snow. Move it to **y 225** and move "FEB 2019" to **y 140**. Both still clear the counter, since x stays under 1300.
   - s135: "6 TO 10" (960, 330) sits on the left building's roof corner. Move it to **(960, 250)**, the clear sky between the buildings.
   - s138: "MASS INVASION" (1300, 450) runs across the right building's windows. Move it to **(900, 300)** at size 76.
   - s140: "CAUGHT" (960, 420) straddles both roof edges. Move it to **(960, 330)**.
   - s149: "COMES BACK" (960, 420), the same problem. Move it to **(960, 330)**.
6. **s162: "RECOMMENDS" (1450, 600) overlaps the sign's right post and board corner.** Move it to **(1560, 760)**, below the board and right of the
   post, or set size 64 at (1600, 640). Keep it clear of Doug at x 1780.
7. **s105-s107: the same composition three times in a row.** All three are Doug on the left, a dashed "10 M" and the bear on the right. The s106/s107 band and title pair is
   house format, so change **s105**. Show the swim being cut: the bear standing at the floe edge (`polar_bear`, x 1450) with a small water ripple
   under a red X, in place of the X over the bear's back. An X on the bear reads as "no bear", and the line says "doesn't need to *swim*".
   Keep s105 on the `#b8c8d8` sky.
8. **s145: Doug stands on the right cell's outline** (x 1400, art bible: never put Doug's x on a prop edge), and the bars run through his head.
   Move him to **x 1520**, the open middle of the right cell, or bring him forward at scale 0.5 so the cap and head stand clear of the bars.
9. **s180: a grass tuft touches Doug's feet** at the right edge (Doug x 1700 at 0.4, tuft at about x 1760). Move the tuft to x 1880 or remove it (art bible: keep
   Doug off busy props).
10. **s123: "OVERHEAT" touches the running bear's front paw.** Move the wordart **60 px right** (or about 40 px up) so there's
   a clear gap between the "O" and the paw.

**Not blocking (optional)**
- s104: at 1080p, `dinner_plate` at (1500, 380) reads as a plate, but at phone size it is a floating white ellipse. Option: add the `fork`/knife pair
  if the library has one, or drop the plate and let "HAS TO EAT" carry the beat.
- s147: the "NO FOOD" tag on the cell is small at phone size. Optionally add a `label` "NO FOOD" (size 40) beside the cell, as in s231.

## Overall
**FAIL, round 1.** Fix 1 goes to the illustrator. Fixes 2-10 go to the director. After that, re-run
`python -m studio keyframes 031-polar-bear-on-purpose --shots` on the affected shots: s044-s053, s065, s067, s105, s123, s129-s141,
s145, s149, s156-s176, s180, s204, s213-s227. Round 2 only checks those. Everything else is approved as it stands.

---

# Keyframe review, round 2 + thumbnails (art director, 2026-10-29)

**Verdict: keyframes PASS. Thumbnails A and B PASS; thumbnail C FAIL (2 fixes, both for the graphic designer).** C is the
grid variant, which is a Test & Compare challenger and not the opening frame, so it does not block `art_approved` for the
episode video. It must be fixed before it is uploaded as a test variant.

## How I reviewed
- I went through all 11 round-2 contact sheets (`build/contact/sheet_01..11.png`), shot by shot, against the round 1 fix list.
- I cropped the 1080p keyframes for the BEAR readout on four dark grounds (s044 `#2a2a2e`, s053 `#000`, s139 `#1b2f5a`,
  s213 `#4a5670`), for s145 (Doug against the bars), and for s157/s158 (the title against the lowered ridges).
- Thumbnails: `build/thumbnail.png`, `thumbnail_b.png` and `thumbnail_c.png` at 1280x720, plus all three `*_small.png` at
  168x94 (viewed at 2x). I also cropped Doug in A and B and the Stalk and Tent tiles in C, and I rendered `polar_bear_lying`
  at 1.3 to check its rear end. Scratch files are in `/tmp/ar031r2/` and were not kept.

## Round 1 fixes: re-check
| # | Fix | Result |
|---|---|---|
| 1 | `paw_print_icon_light` | PASS. Cream pads with a thin dark outline. It reads clearly at 0.3 on `#000`, `#2a2a2e`, `#1b2f5a` and `#4a5670`. Same anchor as the dark icon, no shift. |
| 2 | Readout icon swap | PASS. The light icon is on every dark shot I listed (s044-s053, s130-s141, s149, s204, s213-s227). The light shots keep the dark icon, and s129 is unchanged. |
| 3 | s065 / s067 scientist | PASS. Feet are level with Doug and inside the frame. In s065 the telescope still lines up with his eye. |
| 4 | Camp ridges s156-s176 | PASS. The range is lowered in all 17 shots, with the same profile each time, so the build-up is seamless. "ZERO." and "THE TENT" clear the highest peak (about 15 px at THE TENT; legible). All the wordart sits in clear sky. |
| 5 | Town text | PASS. s132 STATE OF EMERGENCY / FEB 2019, s135 "6 TO 10", s138 MASS INVASION, s140 CAUGHT and s149 COMES BACK are all in clear sky now. None of them touches a roof, a window or the counter. |
| 6 | s162 RECOMMENDS | PASS. Uses the size-64 option at about (1600, 640). It is clear of the post, the board and Doug. |
| 7 | s105 | PASS. Bear at the floe edge with open water behind it, and the red X sits on a water ripple. It reads as "no swim needed", and it is now clearly different from s106/s107. |
| 8 | s145 | PASS. Doug is at x 1520, in the open middle of the right cell. His head and cap draw over the bars and stand clear. |
| 9 | s180 tuft | PASS. The tuft is at about x 1875, well clear of Doug's feet. |
| 10 | s123 OVERHEAT | PASS. There is a clear gap between the "O" and the front paw. |
| D1 | s173 / s174 tent muzzle | PASS. A flipped `polar_bear` body behind the tent joins the muzzle, so there is no floating snout. |

Also checked in passing (from the visual review round):
- `seal_costume_prone` in s099-s104 and s221: Doug's head, face and cap stay clear, and it lines up on the floe.
- The s100 LAST TIME inset still uses the upright costume, as it should.
- The redrawn `berry_bush` / `berry_bowl` read as berries on the olive tundra at every scale (s178-s202).
- s147: the NO FOOD label is in.

None of these changes introduces a new layout repeat. Doug is on-model in every re-rendered shot.
Not blocking, still open: the s104 `dinner_plate` (optional in round 1). It is fine to leave.

## Thumbnails
**A, `thumbnail.png` (lead, also s001): PASS.**
- Doug is on-model: round head with the crescent, oval eyes, thin lines, red cap. He is neutral and unaware, and he reads
  as Doug at 168x94 (the red cap carries it).
- `polar_bear_standing` at 3.5 is clearly the episode's bear: hard eye, heavy brow, long head, dark-red `#7a0d0d` mouth with white
  fangs. It is predatory, not plush, and has no blood.
- The window glow and the navy field are on-palette. DINNER TIME is the house white-with-black-outline Arimo, in the safe area,
  and it is the biggest thing that reads at feed size. The bottom-right timestamp corner holds only bear body, no text.
- Optional: the field guide stands beside Doug rather than in his hands (the brief says "reading"). It is fine as it is.

**B, `thumbnail_b.png`: PASS.**
- Doug is on-model, with the hopeful smile and arms up, facing away from the bear.
- The bear is the approved `polar_bear_standing`. It towers behind him with its forelegs over his cap. There is no contact and the
  claws stay clear of him (brief: no claws *in* Doug). It reads as a predator at 168x94.
- BEHIND YOU is in the safe area and legible small. The composition is clearly not 029's floe-and-shadow.
- Note for the creative director: the brief asked for the flat stalking bear here. The towering bear is a stronger silhouette
  at feed size, so I accept it on style grounds.
- Optional: drop the binoculars about 10 px (y 346 to 356) so the whole cap brim shows above them. At 168x94 the brim
  partly merges into the binoculars and the cap reads a little like a dome. Not blocking.

**C, `thumbnail_c.png` (grid): FAIL, 2 fixes (graphic designer, `thumbnail_test_c.json`).**
- Pass: Nose, Fur, Charge and Town. Doug is on-model in Nose and Charge. The tile colours are the house grid brights, the
  labels are ComicNeue, and there are no cubs and no title words.

1. **Tent tile: the floating severed muzzle is back.** This is the round 1 D1 problem: `tent_dented` alone, so the ragged back end of
   the muzzle sits in open sky. At 168x94 it reads as a white blob or a cut-off snout. Use the s173 fix, scaled to the tile:
   - Set `tent` + `tent_dented` to **(960, 575), scale 0.5**.
   - Add a flipped **`polar_bear` at (1196, 618), scale 0.54, `flip: true`**, placed in the element list *before* the tent, as s173
     does (same offset +330/+60 and ratio 1.07 to the tent scale as s173).
   - Check that the bear's feet land on the snow strip (y 562-598) and that the muzzle joins the head behind the dent. The tile
     clips the bear's hindquarters at the right edge, which is fine.
2. **Stalk tile: the bear faces away from Doug, and its rear end reads as a cut stump.** `polar_bear_lying` faces left while Doug
   faces right, so there is no "closer than he thinks". The bear just looks like it is resting. Its hind-paw sole at the right end
   (a dark oval in a cream square) reads as a severed log end at feed size.
   - Set `polar_bear_lying` to **`flip: true`** (same x 993, y 217, scale 0.36). Its nose then points at Doug's back, about 60 px
     behind his feet.
   - Cover the hind paw, now at the tile's left edge (about x 875, y 210), with a low snow drift, as s063 does: an
     `ellipse` at (885, 212), rx 48, ry 22, fill `#f4fbff`, with no outline, or a `#94adc2` 3 px top edge to match the drift lines.
   - Re-check at 168x94: the bear must read as lying low and *aimed at* Doug, with no stump end.

Re-render with `python -m studio thumbnail 031-polar-bear-on-purpose` (variant C) and send me `thumbnail_c.png` and
`thumbnail_c_small.png`. I will check only those two tiles.

## Overall
**Keyframes: PASS. Every round 1 fix landed, and art is approved for the episode video.**
Thumbnail A (lead/opening frame) and B: PASS. Thumbnail C: FAIL until fixes C1 and C2 go in. Route them to the graphic designer. No
asset or director work is outstanding.
