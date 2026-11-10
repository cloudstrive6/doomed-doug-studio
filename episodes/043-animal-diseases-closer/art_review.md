# 043 art review: new assets (art director, 2026-11-10)

**Verdict: PASS** (32/32 approved; two trivial fixes applied by the art director, listed below).

Checked: the 9 previews in `assets/previews/043-*`, plus my own test renders. These covered the hanging and flying bats, the colony,
the stalagmite and the virus on cave #3b2a17 and IR green #2a3a2e, next to Doug for scale. I also rendered silhouette-with-glow tests
for fruit_bat_flying, chicken_coop, wooden_shed and brown_dog_sitting, Doug seated in diner_booth with burger_plain on the table, flea
beside sesame_seed at the same scale, broom rotated, the farm animals at 1.3-2x, and the hanging bat downscaled to 168x94.
Both tiers hold: the creatures and props have interior shading, layered fills and bold 4-5 px outlines against crude Doug. All are on
the requested hexes. There is no gore and no symptom imagery, and the germ is faceless.
Per the brief, the carriers look ordinary and calm, not cute: small dark eyes with no shine, no blush, no tongues.

## Fixes applied by the art director
1. **pig**: the mouth curve dipped in the middle and read as a smile, which breaks the "never cute, no smiles" rule. I flattened it to
   a straight, slightly downturned line (element 26). The anchor and footprint are unchanged.
2. **goat**: the horn floated just above the skull at scale (a visible gap). I moved the horn by (+10,+14) so its base tucks under the
   head outline. The anchor and footprint are unchanged.

## Per asset
| # | Asset | Result | Notes |
|---|---|---|---|
| 1 | fruit_bat_hanging | APPROVE | Reads as a bat on both cave and IR. The face is the right way up for an inverted head. The preview sheet crops its head because the cell assumes bottom-centre anchors, but the asset is fine. See thumbnail note T1. |
| 2 | fruit_bat_flying | APPROVE | The silhouette reads clearly as a bat with the red glow. |
| 3 | bat_ceiling_colony | APPROVE | |
| 4 | bat_ceiling_colony_stir | APPROVE | Clearly different from #3: wings flicked. |
| 5 | stalagmite | APPROVE | Flat tip suits the cap. |
| 6 | europe_map | APPROVE | Pin coordinates match the projection. Germany and Serbia are highlighted. |
| 7 | malaysia_map | APPROVE | Frame is off-centre as the request specified. See director note D1. |
| 8 | netherlands_map | APPROVE | Oss at (39,90) checks out. |
| 9 | date_palm_tapped | APPROVE | |
| 10 | clay_sap_pot | APPROVE | The spout rises above the rim. Hang the cap on the rim, not the spout. |
| 11 | sap_cup | APPROVE | |
| 12 | flour_bag | APPROVE | |
| 13 | pig | APPROVE (fixed) | Fix 1. |
| 14 | virus_blob | APPROVE | Still reads at 0.25. |
| 15 | temple_stairs | APPROVE | No symbols and no text. |
| 16 | goat | APPROVE (fixed) | Fix 2. |
| 17 | chicken_coop | APPROVE | The props sheet crops its roof, but the full render is correct and the silhouette reads. |
| 18 | straw_nest_eggs | APPROVE | |
| 19 | burger_plain | APPROVE | |
| 20 | diner_booth | APPROVE | Seat and table heights verified with a seated Doug. |
| 21 | wooden_shed | APPROVE | The silhouette reads. |
| 22 | wooden_shed_open | APPROVE | |
| 23 | deer_mouse | APPROVE | |
| 24 | mouse_nest | APPROVE | |
| 25 | broom | APPROVE | |
| 26 | medieval_town_skyline | APPROVE | The tower has a clock face, with no cross or flags. |
| 27 | ground_squirrel | APPROVE | Upright and intact, fine as the doormat "present". |
| 28 | flea | APPROVE | Matches sesame_seed at the same scale. |
| 29 | brown_dog_sitting | APPROVE | Non-blocking: the forelegs are two stiff rectangles. Illustrator may soften them in a later pass. |
| 30 | brown_dog_sleeping | APPROVE | Consistent with the other two dog poses. |
| 31 | brown_dog_walking | APPROVE | |
| 32 | cardboard_box_open | APPROVE | |

## Notes for the director (composition, not blocking)
- D1. **malaysia_map**: to centre the map in frame, offset placement by (-40,-30). The pin is at (-260,20) relative to the anchor.
- D2. Several animals run up to 20% over their requested boxes (pig, goat, deer_mouse, brown_dog_walking, brown_dog_sitting). Keep
  them clear of the caption bar and the safe area when the keyframes come in.
- D3. On cave #3b2a17 at small scales the bat's dark wings (#4a3c34) merge with the background, though the body and face still read.
  For the colony and other small-bat shots, use the lighter IR green or a light rim if they look muddy in keyframes.

## Note for the graphic designer
- T1. Thumbnail hero (fruit_bat_hanging): at 168x94 on #3b2a17 the wings sink into the background. Use a flatter, lighter background
  (Archetype C), or add `"rim": {"color": "#ffffff", "px": 4}`, so the silhouette pops in the feed.

---

# 043 art review: keyframes (art director, 2026-11-10)

**Verdict: FAIL** (7 required fixes, all director/composition; no asset redraws needed).

Checked: all 15 contact sheets (s001-s178 + endslate). Most of the episode is on-model and on-bible. Doug is crude, 3-4 px, with his cap
in every live frame. Death grammar is correct at all 7 deaths (329 to 336; X eyes, ghost with cap, cap on a prop). The caption bar matches
the script item names. Band headers ("THE WILD." / "THE FARM." / "THE HOUSE.") are white with an outline and have no top bar. Sober cards are
#15181a with no Doug, no counter and no names. The HOW CLOSE fingerpost only moves toward the house and the last plank is stamped red.
The zone ramp reads as intended: cave brown, night palm, temple sky, farm sky and grass, diner cream, shed, then the house interior.
Carriers are calm and ordinary everywhere (bats, pig, macaque, goat, cow, chickens, mouse, cat, dog); none look sick or cute. Asset note D3
is resolved: the colony reads on #3b2a17. The failures are the 043 disease rules (series bible: no symptom imagery, germs are faceless blobs
under a magnifying glass) plus two series-continuity misses.

## Required fixes (director)
1. **s160 (symptom imagery).** Doug cowers in shock from the water bottle, which acts out hydrophobia, a rabies symptom. Remove the Doug
   element, or make him `stand` with a `flat` expression at least 400 px from the bottle. Keep the bottle, the "!" and FEAR OF WATER.
2. **s158 (germs on a body).** Three `virus_blob`s travel down the stick person's face and neck from a bite point. That shows infection on
   a human body. Keep the person and the dashed purple path, which is enough for "moves inside the nerves". Delete the three blobs, then put
   one `virus_blob` inside a magnifying glass beside the NERVES label.
3. **s080, s081, s082 (reads as fever).** The `sunburn` gear turns Doug's face and arms red during the Q fever item. That reads as a flushed,
   feverish Doug, and it contradicts s081's "no symptoms". Drop `sunburn` from all three. Doug's thumbs-up and the cap on the path carry the gag.
4. **Loose germs (magnifier rule).** These shots show germ icons floating free, with no magnifying glass. In each, remove the icons or
   enclose one in a magnifying glass:
   - s006: the blob on the Africa inset. The red arrow and the AFRICAN CAVES label already carry the beat.
   - s013: the free blob next to UGANDA.
   - s038: the blob trail leaving the pig. Run the dashed line out of frame and put a single magnifier on it.
   - s054: the blob on the dashed line. Use a magnifier at the line's start; the red X stays.
   - s087: the two loose purple blobs over the chickens. The magnifier is already there.
   - s127: both blobs in the dust. The spray cloud alone reads as "droplets in the air".
   - s061, s066, s067, s068: the free green bacteria specks over the animals, barn and dust. Keep the plain dust/spray clouds; s064's magnifier
     has already shown what the specks are.
   s101 (crossed-out blob, "NOT A GERM") may stay as it is. It is a negation and reads as one.
5. **s058, s059, s060 (bandage continuity).** Doug is bitten at s057 and survives. Series bible (022 gear) says the white ankle bandage is the
   survival marker for a bite he walks away from, so add `"bandage"` to `gear` on s058-s060 alongside `cap_off` (s058, s059). Doug's
   gear list on s060 currently has no entries.
6. **s176 (one cap per frame).** The RIP DOUG gravestone wears a red cap while the real cap sits in the UNDER OBSERVATION box. The ghost's cap
   is allowed; the gravestone cap is a second real cap. Remove the cap from the gravestone and keep the stone plain.
7. **Composition variety.**
   - s022-s024: three near-identical frames in a row (Doug lower-left, colony ceiling, wordart right). Make s023 a wide, low shot looking up at
     `bat_ceiling_colony_stir` with Doug small at the bottom. Keep s024 as the flying-bats beat.
   - s043-s045: the same temple wide three times in a row. Make s045 (DEADLIEST) a push-in on one macaque, about the s046 framing,
     or the triangle alone on cream.
   - The **torch** in s022-s024 has no beam. Rotated -50, it reads as a microphone. Aim it up at the ceiling (rotate about -20) and add the
     pale-yellow beam poly (`#fff7a0`) used in s001, so "walked in with a torch" reads.

## Minor fixes (director, do in the same pass)
- m1. **s069**: the dust puffs are pale blue on the #8fd3ff sky and almost invisible. Tint them tan #c9a87a, as in s068.
- m2. **s127**: the brown wedge poly on the left, (0,200)-(700,900), doesn't read as anything. Delete it, or make it a clear open-door light
  shaft in #5a4a38.
- m3. **s130**: the red "!" sits on the map's bottom frame line. Move it up about 60 px, inside the map, next to the pin.
- m4. **s081**: the capped icon in the grid is Doug, so the full Doug at the right is a second cap. Drop the full Doug, or drop the cap
  from the icon.

## Notes (non-blocking)
- N1. The red silhouette glow on the light-grey fingerpost background renders as a pink speckle disc (s026, s042, s083, s115, s134, s152).
  It is consistent across every fingerpost shot, so it is accepted as this episode's look. It would read better with the s015 treatment
  (darker `#8a1a1a` glow), so do that on the next reuse.
- N2. s171 shows a living Doug on "Doug has died."; the death image lands on s172 ("Again."). That is accepted: it suits the rabies "nothing
  seemed wrong" beat, and s172 follows within about a second.
- N3. In s036 and s138 three data labels share the screen (BATS/PIGS/PEOPLE, PLAGUE/GROUND SQUIRREL/PRAIRIE DOG). These are diagram callouts,
  not keyword labels, so they are fine, but don't add more.
- N4. The HOW CLOSE HUD text is about 18 px at 1080p. It is legible full-screen and illegible on mobile, which is fine because it is staging
  and never read aloud.

Re-render only the shots listed (`python -m studio keyframes 043-animal-diseases-closer --shots ...`). I will re-check those shots only.

---

# 043 art review: keyframes, Round 2 (art director, 2026-11-10)

**Verdict: PASS.** All 7 required fixes and all 4 minor fixes from Round 1 are in. No new rule breaks.

Re-checked at full size: s003, s006, s013, s018, s022-s024, s038, s042, s043-s045, s054, s056-s061, s066-s069, s079-s082, s087, s098,
s102, s127, s130, s145, s158, s160, s170-s172, s176.

## Round 1 fixes verified
1. s160: Doug now `stand`/`flat`, about 580 px from the bottle; the bottle, "!" and FEAR OF WATER are kept. No hydrophobia acting.
2. s158: no blobs on the body. The dashed purple path stays, and one `virus_blob` sits in a magnifier beside NERVES.
3. s080-s082: `sunburn` is gone. Doug's skin is white and the thumbs-up and cap-on-path gag carry the beat.
4. Loose germs: s006, s013, s127 have none. s038, s054, s087 have a single magnifier each (s038's dashed line runs out of frame).
   s061, s066, s067, s069 have plain clouds only. s068 now encloses the bacterium in a magnifier, which is an allowed alternative.
5. Bandage: white ankle bandage on s058, s059, s060 (and already on s057, at the bite).
6. s176: the gravestone is plain. The only caps are the ghost's (allowed) and the real one in the UNDER OBSERVATION box.
7. Variety: s022 (close, torch), s023 (wide and low, colony stir, Doug small), s024 (flying bats) now read as three different frames.
   s045 is the triangle on cream with one macaque, which breaks up the temple run. The torch now aims up with the #fff7a0 beam.
- m1 s069: the dust is tan and visible. m2 s127: the wedge is gone. m3 s130: the "!" is inside the map. m4 s081: the icon has no cap
  and the cap is on the floor beside Doug.

## Notes (non-blocking)
- R2-1. s171/s172 are now the same death frame, with AGAIN added on s172. That is fine for a sub-second "Again." beat. It also
  supersedes N2: the death now lands on "Doug has died."
- R2-2. s170: the speech-bubble tail is a thin stray line ending in empty space between Doug and the dog. A short wedge tail pointing
  at Doug would read better. Fix it if the director touches the shot again.
- R2-3. s042: the pink speckle glow is still there (N1, accepted for this episode).
