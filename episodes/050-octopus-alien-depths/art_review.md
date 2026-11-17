# 050 art review

## Round 2 (art director, 2026-11-17)

### Asset re-check: PASS (`seven_arm_octopus_male`, s121/s122)
The redrawn sac reads as a closed, bulging pouch. It has a lilac fill, a white highlight arc and a black outline, and holds a wine-red
coiled tube with a darker edge, pale sucker dots and a rounded tip. It no longer reads as a cut cross-section or a sore. The s121 arrow
lands on the coil, not the eye. All 54 assets are now approved.

Round-1 composition notes 2-5 are closed: the reef water is clean in s019-s025, Doug sits on the floor line in s187/s188, the s157
beard sits on the floor, and the s121 arrow is on target.

### Keyframes (`build/contact/sheet_01-18.png`, 214 shots + endslate): FAIL (11 fixes, all for the director)
Style, Doug and palette are consistent. The zone ramp holds from 5 m to 6,957 m, Doug auto-inks correctly on dark grounds, and there
is no gore. These are the fixes:

1. **s037: the umbrella crosses the reserved counter zone.** The canopy runs under "DOUG DEATHS" and over the depth icon. Move the
   umbrella so its rendered right edge is ≤ x 1280, or drop it below y 330.
2. **s211, s212: the TV frame sits under the depth meter.** The TV is an inset frame, so its rendered right edge must be ≤ x 1280
   (bible "Death counter" rule). Shrink it or shift it left.
3. **Headline text collides with the creature.** Move each word clear of the drawing, with about 30 px of space:
   - s018 "TWO THIRDS" on the octopus head
   - s075 "THE BLANKET" on the cape
   - s098 "SEE-THROUGH", s104 "ALONE" and s105 "THE EYES" on the glass octopus mantle
   - s118 "THE SEVEN ARMS" on the mantle
   - s124 "75 KG" on the mantle
4. **s144: replace the Olympic rings.** They are a protected IOC mark, which is a policy and ad-suitability risk. Use two generic
   torches or two plain calendar pages marked "GAMES" with the 4-year bar between them. Ask the illustrator if you need a torch.
5. **s122: the number labels 1-7 don't line up with the arm tips.** The labels run from x 520 to 1270, but the tips sit at about
   625-1155. Put one label under each tip, at a pitch of about 88 px.
6. **s125: Doug hangs under the right pan.** Stand him in the pan with his feet on the pan line, and tilt the beam slightly down on
   his side (80 kg > 75 kg).
7. **s124: the "grown man" reads as a snowman** (two white discs). Use a plain stick man without a cap at the same height as the
   octopus, or Doug himself.
8. **s067-s071: the same wide shot five times in a row.** Each one shows Doug sitting at the centre of the shell bed between two
   octopuses. Vary them: punch s068 in on Doug inside the silt puff, make s070 a close-up of Doug's "fine" face, and keep s067/s069
   wide.
9. **s136 → s137: the two shots are nearly identical** (only "!" is added). Make s137 a push-in on Doug in the "bowl", with the
   octopus head looming and an alarmed expression. Show no beak contact.
10. **s174: the depth bar's lower half is white**, which reads as ice or surface. Band it with the zone ramp instead (`#3a9ad9`
    0-200, `#1b4f86` to 1,000, `#0b2447` below). Keep the whale at 2,000 m and Doug at 3,200 m.
11. **s095, s096: the HUD says "ABOUT 20 M"** but the ground is twilight `#1b4f86`. Switch the depth label to "ABOUT 500 M" from
    s095, matching s097.

After fixing, re-render only the affected shots
(`keyframes 050-octopus-alien-depths --shots s018,s037,s067,s068,s070,s075,s095,s096,s098,s104,s105,s118,s122,s124,s125,s137,s144,s174,s211,s212`)
and send them back to me.

## Asset review (art director, 2026-11-17): FAIL (1 asset fix; 53 of 54 approved)

I checked the five sheets in `assets/previews/050-*.png` and the illustrator's notes in `asset_requests.md`. I also rendered 44 keyframes in
context (`python -m studio keyframes`): every costume shot (s019-s025, s044-s047, s089-s094, s135-s138, s155-s157, s185-s189), every
sober and near-black card (s159, s160, s162), the silhouettes (s073, s193), and the scale and diagram shots (s018, s034, s035, s084, s121,
s129, s168, s175, s203, s209). I zoomed into the costume fits, the beard props, and the male's arm sac. Only one asset needs work before keyframes.

### Renames applied (art director)
The illustrator's two re-placements are applied in `shotlist.json`. I made the same change in `build/gen_shotlist.py` so a regeneration keeps it.
- s019: `goatfish_costume` → `goatfish_costume_swim` (same x/y/scale as Doug). The swim lean, barbels, cap and face all read.
- s187, s188: `diving_suit` → `diving_suit_sit`. The suit sits on the hips, and the thighs come out of the base.

### Required fix (illustrator)
1. **`seven_arm_octopus_male`: redraw the arm sac (s121, s122).** At the moment it is a pale pink disc with concentric red/pink rings, set into the
   wine-red skin. At frame size (s121, scale 1.0) it reads as a sliced cross-section of flesh, or as an open sore by the eye. That breaks
   the never-gory rule and the "no severed-looking ends" rule (026 specimen jars). Redraw it as a **closed, bulging translucent sac**:
   - It sits in the same place, local (+100, -100), and bulges out past the body outline so it reads as a pouch.
   - Fill it with pale lilac/cream `#e9dcef` plus a soft white highlight arc, and a 3-4 px black outline.
   - Inside, show the coiled arm as a **tube** in the body's own wine red, with a darker edge and 3-4 pale sucker dots along it, coiling
     about 1.5 turns, so it reads as an arm wound up and not as rings.
   - No pink-on-red concentric circles, and no red centre.
   - Keep the s121 arrow target at local (+100, -100).
   - Re-run `asset-preview seven_arm_octopus_male` and send me s121 only.

### Approved (53)
`day_octopus`, `day_octopus_punch`, `day_octopus_crack`, `goatfish`, `blacktip_grouper`, `roving_coral_grouper_open`, `goatfish_costume`,
`goatfish_costume_swim`, `goatfish_costume_flat`, `octopus_outline_diagram`, `octopus_outline_arms_red`, `mimic_octopus`,
`mimic_octopus_flatfish`, `mimic_octopus_lionfish`, `mimic_octopus_seasnake`, `banded_sole`, `lionfish`, `banded_sea_snake`, `damselfish`,
`damselfish_costume`, `octopus_eye`, `raincoat`, `shell_midden`, `gloomy_octopus`, `gloomy_octopus_throw`, `gloomy_octopus_dark`,
`gloomy_octopus_duck`, `blanket_octopus`, `blanket_octopus_cape`, `blanket_octopus_male`, `man_o_war_costume`, `man_o_war_costume_flat`,
`glass_octopus`, `dishwasher_open`, `seven_arm_octopus`, `seven_arm_octopus_holding`, `seven_arm_octopus_holding_front`, `egg_yolk_jelly`,
`jelly_costume`, `jelly_costume_flat`, `brooding_octopus`, `octopus_egg_cases_empty`, `octopus_hatchling`, `folding_stool`, `doug_beard`,
`doug_beard_lying`, `pearl_octopus`, `grapefruit`, `diving_suit`, `diving_suit_sit`, `diving_suit_flat`, `dumbo_octopus`,
`yellow_submarine_crumpled`.

Notes on what passed:
- **Two-tier contrast:** it holds throughout. The creatures have layered fills, spray shading, darker backs and lighter bellies, and 3-5 px outlines. The costumes are flat felt, and Doug stays crude.
- **Kid appeal:** every octopus eye is small, with a bar pupil under a heavy lid or a plain dark dot. There are no smiles, blush or shine.
  The dumbo (s203, s209) reads as a pale, odd deep-sea animal, not a mascot. The hatchling has a simple dark eye and no mouth.
- **No gore:** the man-of-war strands end in beads, and there is no ink. `day_octopus_crack` shows arms trailing out of a crack, with no cut ends.
  The arms of `mimic_octopus_seasnake` end in rounded black tips. The goatfish, man-of-war, jelly and diving-suit flats all carry the X eye or
  X plate with the cap on top. That is the 008 grammar, and it reads.
- **Dark grounds:** `glass_octopus` reads as glass on `#1b4f86` (s096, s105). It has a faint outline, a see-through fill, and solid eyes and gut.
  The upright tube eyes are fine. The `octopus_egg_cases_empty` and `octopus_outline_diagram` outlines read on `#15181a` (s159, s160, s162).
  `gloomy_octopus_dark` stays a mid-tone on blue (s063). The `blanket_octopus` silhouette has a clean red rim (s073).
- **Costumes:** cap, face and head are clear in every fit: goatfish (float, point, fall -30, swim), damselfish (swim, flipped), man-of-war
  float vest, jelly cape, and diving suit with helmet. Treat `damselfish_costume` as the fish body with Doug's head at the nose. It reads,
  and it's funny. The diving suit has no padded sleeves. I accept that, because the narrow barrel and swinging arms read better than
  sleeves fighting the walk loop.
- **Beards:** `doug_beard` / `doug_beard_lying` stay off the eyes and cap and read as props (s156, s157).

### Composition notes for the director (keyframe round; not part of this asset gate)
These came up in the in-context renders. Please fix them before you send keyframes.
2. **Reef scenes s019-s025: orange sand speckle across the whole water column.** The sand `spray` at (960, 950) with r 900 reaches up to
   y about 50, so `#d4a960` dots fleck the blue water everywhere. Cut r to about 300 and spread it with 3 sprays along the sand. Or add a `#3a9ad9`
   water `rect` (y < 820) after the spray, and then re-add the `#6fc1ee` water speckle. Check `reef()` and every scene that reuses it.
3. **s187/s188: Doug sits into the seabed with nothing under him.** With hips at y 690 in `sit` at 0.48, the base of the suit lands about
   25 px below the rock line at x 960. The art bible says a seated Doug sits *on* something. Either put a rock or vent lump under him, with its top at
   the seat line, or raise Doug and `diving_suit_sit` together (same x/y) until the seat is on the floor line.
4. **s157 (minor):** the zigzag tips of `doug_beard_lying` dip about 8 px below the floor line. Raise Doug and the beard together by 8 px.
5. **s121/s122:** re-check the arrow tip once the sac is redrawn (fix 1). Keep it on the coil and not on the eye.
