# Art review: 008 Every Step of the Ocean Food Chain, round 1 (assets)

Reviewer: art director, 2026-10-05. Scope: all new library assets from `asset_requests.md` (items 1-11) plus the
`cap_off` engine request. Keyframes are not reviewed in this round.

Checked against `channel/art_bible.md`, style bible section 7 (Art Director rules 1-9) and the director's sizes and
anchors. Sources: every `assets/previews/008-*` sheet, plus my own test renders. In those renders every costume was
worn on every pose the shotlist pairs it with. I also placed pins on the maps with the director's projection
formulas, checked the orca with `doug_cap` at (+210,-120) x scale, put Doug at the sailboat helm, checked
`cap_off` on `stand`/`wave`, and checked every `*_flat` next to an `on_back` Doug.

## Verdict: PASS (assets APPROVED), with 2 fixes I applied myself and 1 composition fix for the director

## Fixed by the art director (trivial geometry, already in `assets/library/`)
1. **`tern_costume`**: the headband bill sat at y -233..-212 and covered the lower half of the cap brim
   (y -248..-225). I lowered it to y -222..-200 (tip at (196,-210)). The brim is now fully visible, and the bill still starts
   at x +62, clear of Doug's eyes. Verified on `stand`, `float`, `panic1`, `arms_up`.
2. **`crab_costume`**: the right eye stalk curved through the cap brim tip (stalk point at (132,-232)). I lowered both stalk
   roots to y -206 and re-routed them out to x +-150..+-170, so they now pass under the brim tip and rise beside it. The eye
   balls are now at (+-166,-350) and the bbox is x -186..+186. Cap, brim and face are fully visible on `stand`, `walk1`,
   `arms_up`. The flat version is unchanged.
   Verification sheet: `assets/previews/008-art-review-costume-fixes.png`. (`008-item3-*` and `008-item4-*` still show the
   old stalks/bill. They are stale, but nothing needs redoing.)

## For the director (composition, not assets)
3. **s057, s058: `reef_fish_costume` on `pose: "cower"`**. Cower drops Doug's head into the suit, so the suit's top edge
   covers his mouth and chin. That breaks the "head, face and cap fully visible" rule. Use `float` or `stand` with
   `expression: "shock"`, which already reads fine in 15 other shots. Every other costume/pose pairing in the shotlist renders
   on-model.

## Engine request: DONE and verified
- `gear: ["cap_off"]` on non-flat poses omits the cap and draws nothing on the ground. Head and face are unchanged. Tested on `stand`
  and `wave`. The art bible already logs the rule ("Capless upright Doug (from 008)"), and the exception is in `decisions.md`.
  This no longer blocks s313, s314, s318, s319.

## Per-asset notes (all APPROVED)
| Item | Assets | Notes |
|---|---|---|
| 1 Mantis shrimp | `mantis_shrimp`, `mantis_shrimp_strike`, `mantis_arm_spring`, `snail_shell_cracked`, `highspeed_camera`, `speedometer` | Body identical in both shrimp states, so the swap is clean. Staircase size (0.17) still reads. The spring diagram is clear. The shell is honey-amber with a clean zigzag split. The speedometer leaves (0,+60) clear. |
| 2 Moray | `giant_moray`, `moray_xray`, `moray_xray_jaws_forward`, `tape_measure`, `roving_coral_grouper`, `reef_fish_costume`, `_flat` | Moray: teeth are white on a `#7a0d0d` mouth, no blood. The silhouette is long and plain, but the mouth notch identifies it once only the head pokes out of the crack (s058). X-ray pair overlays exactly. The grouper face is neutral, not friendly. On the flat costume the button eye is crossed out. |
| 3 Octopus | `giant_pacific_octopus`, `octopus_arm`, `glass_jar`, `jar_lid`, `crab_costume` (fixed), `crab_costume_flat`, `tennis_ball`, `bathroom_scale` | The octopus spans the full width and stays under 620 tall, with slit eyes and no face beyond them. The jar is outline only. Director: in the illustrator's jar preview Doug's feet poke below the jar base. Keep the brief's "feet 30 above base" in s074-s078 (I will check this at keyframes). |
| 4 Trevally | `giant_trevally`, `sooty_tern`, `tern_costume` (fixed) | Steep forehead, scowl and gold eye. Reads well both rotated and as a silhouette. The tern stays bold at 0.28. The costume wings are suitably oversized and homemade. |
| 5 Goliath grouper | `goliath_grouper`, `goliath_grouper_full`, `shark_costume`, `baby_grand_piano`, `shipwreck` | Mouth: small white teeth in a dark-red mouth, heavy and not cute. The full version has bulging cheeks and a grey felt tail tip, no blood. The shark fin stays left of the head and cap. The wreck stays mid-value and in the background. |
| 6 Tiger shark | `tiger_shark`, `tiger_shark_xray`, `tin_can`, `burlap_sack`, `sea_turtle_costume`, `_flat`, `seagrass`, `albatross_chick`, `australia_map` | Blunt snout and stripes. The silhouette is clean. The x-ray stomach is an empty oval as requested. Map pins with the 28 px/deg formula land on Kennedy River/Princess Charlotte Bay, Shark Bay, Bremer Bay and the Torres Strait gap. |
| 7 Croc | `saltwater_crocodile`, `tide_table` | Feet sit flat on y=0. The silhouette is unmistakable. The booklet has no readable text. |
| 8 Polar bear | `polar_bear`, `polar_bear_lying`, `seal_costume`, `_patched`, `_flat`, `cape_fur_seal`, `beaufort_map`, `finish_banner` | The bear has a clear dark outline, so it will read on ice. The lying bear's head is at the left. Seal whiskers sit beside the cheeks, not over the face, and `fall` rotated -20 (s247) reads. Beaufort pins: Point Barrow and the Yukon coast land on the coastline, and the pack-ice edge is at about 73.5 N. |
| 9 Great white | `great_white_shark`, `seal_island`, `seal_decoy`, `six_story_building`, `south_africa_map` | The building has exactly 6 window rows. The contact sheet crops its top row, but the asset itself is correct. Seal Island and Gansbaai pins land in and just east of the False Bay notch. |
| 10 Sperm whale | `sperm_whale_top` | Box head is on the right with white scar circles. Reads from above. |
| 11 Orca | `orca`, `orca_bent_fin`, `sailboat`, `sailboat_no_rudder`, `rudder`, `life_jacket`, `iberia_map` | Powerful, not plush. `doug_cap` at (+210,-120) x scale sits on the head. Doug at local (-20,-110) at the helm reads, with legs hidden by the hull. The life jacket works on `stand`, `wave`, `thumbs_up`. The Iberia map shows Gibraltar and North Africa. |

## Style bible 7 checks (asset-level)
- Rule 1 (two tiers): every creature, place and prop is in the detailed tier, and every costume leaves crude Doug on-model. PASS.
- Rule 2 (cap always visible): PASS after fixes 1-2. The only capless frames are the logged one-off exception.
- Rule 7 (silhouettes): every SIL asset (moray, roving grouper, trevally, goliath, tiger shark, croc, great white, orca) has a
  clean, recognisable outer shape. PASS.
- Rule 8 (no gore): no blood, wounds or carcasses anywhere. Flat costumes use X eyes only, with no tears. PASS.
- Rules 3-6 and 9 apply at keyframe level and will be checked in round 2.

ASSETS: APPROVED (pending director fix 3 at keyframes)

---

# Keyframes round 1

Reviewer: art director, 2026-10-05. Scope: all 321 keyframes (`build/contact/sheet_01..27.png`). The contact folder held only
`sheet_01` from a partial run, so I regenerated the full set with `python -m studio keyframes 008-ocean-food-chain` first.
I checked full-res crops in `build/keyframes/` where a contact tile was ambiguous. References: `channel/art_bible.md` and
style bible section 7 (Art Director rules 1-9).

## Verdict: FAIL (31 numbered fixes, all small; no asset redraws except fix 24)

What already works, so don't touch it: Doug is on-model in every shot (two tiers hold, auto-ink is white on every navy/black
shot, every costume leaves the face and cap clear, and fix 3 from round 1 is done in s057/s058). Item title cards are
consistently red, and the zone cards (REEF / OPEN WATER / APEX / NO PREDATORS) are consistently white. The caption bar
matches the item name on every segment shot. The counter runs 65 to 74 at the right beats. The NO PREDATORS boss card
(s280-s281) and the silent navy shift at s252 both land, and the sperm whale sits on midnight `#0b2447`. Layout variety is good:
reef sets, maps, x-rays, staircases, chalkboards, TV feed, top-down river and depth pan. No run repeats the same composition 5 times
(the s021-s025 force chart and the s119-s122 grouper close-ups are build-ups of 4-5 changes on one background, which is allowed).
No gore anywhere.

## Fixes for the director (composition, `shotlist.json`)

**A. Cap missing on a death beat (rule 2, must fix)**
1. **s059, s077**: the death shot shows only the flat costume, with no Doug and no cap. Every other "eaten" death in this episode
   (s137, s163, s193, s219, s277) keeps the red cap in frame, so do the same here: add `doug_cap` (scale 0.5) on the ground beside
   the flat costume. For s059 put it at about (1090, 895) on the crack floor; for s077 put it at about (1150, 880) next to the crab shell.
   Carry the cap into s060/s078 at the same spot.

**B. Counter zone (x 1300-1860, y 110-230 is reserved)**
2. **s015, s016, s017, s018, s019**: the top edge of the SLOW MOTION frame (rect y 150) runs right under the
   "DOUG DEATHS" box. Start the frame at y 250 (h 720), move the SLOW MOTION label to y 300, and check that the shrimp and snail
   are still inside the frame.
3. **s268**: the top-right corner of the squid inset (rect 560,200,800,560) is about 5 px from the counter. Use y 260.
4. **s189**: the white spray disc at (1500,300) reads as a grey smudge and touches the counter zone. Delete it. If you want a "photographed"
   cue, add a small `highspeed_camera` or red "!" at about (1000, 300). **s317**: delete the same white spray at (1300,500)
   for the same reason.

**C. Text crossing a creature, Doug or an arrow**
5. **s060**: INFORMANT (983,260) sits across the upside-down grouper. Move it to about (1450, 480), in the clear water right of the grouper.
6. **s061**: the GIANT PACIFIC OCTOPUS title crosses the octopus's head. Move the title to y 250, or move the octopus down to y 640.
7. **s105**: the red arrow cuts through HUNT THE SKY. End the arrow below the text, or move the wordart to about (1420, 360).
8. **s113**: the title touches the dorsal spines, so raise it to y 290. **s114**: BIGGEST touches the dorsal fin, so raise it to y 195.
9. **s125**: BOOM (1122,330) sits on the grouper's head. Move it to about (1620, 330), above the sound arcs.
10. **s138**: EATS SHARKS overlaps the dorsal fin. Either set y 175 and size 90, or move the grouper down 60.
11. **s143**: SEA TURTLE sits on Doug's cap brim. Move it to y 225, or move Doug and the costume down 60.
12. **s282**: the orca's dorsal fin goes through KILLER WHALE. Move the wordart to the clear water at about (620, 900).

**D. Wordart on green, and text over map frame lines (art bible "Text")**
13. **s179**: THEIR WAY sits on the grey-green estuary (`#6f8a6e`), and lime on green-grey disappears on a phone. Move it onto the sand
    wedge at about (300, 250).
14. **s194**: TOO (1350,560) straddles the waterline. Move it up into the sky at about (1250, 330).
15. **s212**: rejecting the "left as is". 16 MARATHONS crosses the top-right map frame, which is exactly the 007 failure the bible
    forbids. Move it into the right margin at about (1620, 420), size 60 (Doug stays below it). The 16 finish-banner icons at
    scale 0.3 also read as a red scribble, so either use 0.45 with fewer, larger banners (8 at x2) or drop them and leave only the dashed route.
16. **s213**: "+1,800 KM" crosses the right frame edge. Move it to about (1620, 420).
17. **s155**: THOUSANDS OF KM crosses the right frame edge. Put it inside the map over open Pacific at about (1250, 600).
18. **s183**: "590 KM" and "25 DAYS" straddle the top-right frame corner. Move both to x 1660, y 330 and y 430 (clear of the frame and the counter).
19. **s251**: WHOLE SEASON and the calendar cross the right frame edge. Move both into the right margin, x about 1720.
20. **s288**: PORT and STARBOARD sit on the frame edge. Move the two orcas and their labels fully into the right margin (x 1600 or more).
21. **s291**: "2019" sits on the bottom frame line. Put it fully below the frame or fully inside the map above the pin.
22. **s267**: SEE EPISODE 1 overlaps the inset's bottom edge. Move it to y 860.

**E. Readability and props**
23. **s130, s131, s132**: the fishing boat at (700,260) runs into the GOLIATH GROUPER chapter bar. Move the boat to x 320 (and its line with it).
24. **Splash (asset, illustrator)**: the inline white zigzag splash reads as an **iceberg** at contact and phone size. It does this
    in s096, s101, s102, s109, s110, s163, s193, s223, s233, s234, s243, s247, and worst in s243, where three of them in a row look like an ice field.
    The illustrator will draw a library `water_splash` (detailed tier, bottom-centre anchor): a pale blue `#bfe6ff` crown with
    white highlights and `#3a9ad9` inner strokes, 4-6 round droplets flying off the tips, and the base drawn as a ring
    sitting *in* the water. Director: swap it in for every inline splash and anchor it on the waterline. In addition:
    - **s193**: the croc lunges onto sand, so use a sand puff (`#e8c07a`/`#d9ac62` spray) instead of a water splash.
    - **s234**: drop the splash under the kitchen timer, because the timer currently stands on an "iceberg".
    - **s243**: one splash plus the label is enough.
25. **s191**: the tide table at (790,560) floats about 150 px above Doug's pointing hand. Move it to about (800, 730) so he is holding it.
26. **s299**: "15 OF ~40" doesn't read, because all 40 orca icons are identical black silhouettes. Draw 15 of them as the normal colour
    `orca` (or tint them red) and leave 25 as silhouettes.
27. **s058**: the moray silhouette at x 1700 is cut by the frame edge and reads as a black bar. Bring it in to x 1550 so the head
    and mouth notch show (glow_r 0 is fine here, because the moray is already known).
28. **s174**: the family car sits on the sea/horizon line and looks like it is driving on water. Put it on the sand above the croc's
    jaws (about (1300, 760), scale 0.6) with a red down-arrow for "pressing down".
29. **s235, s236**: the rising sun is only a yellow outline arc and looks unfinished. Fill it `#ffe24a`.
30. **Polar under-ice water**: s197, s199, s200, s201, s202 and s205 use `#1b4f86` (twilight) for surface water, while s207 and s210 use
    `#3a9ad9`. That is inconsistent inside one item, and it uses up the navy before the "silent deep-navy shift" at s252. Use `#3a9ad9`
    for all of them. Doug's ink stays black, which is fine on that blue.
31. **s317**: three keyword labels are on screen (AGAIN, PUGET SOUND, 2024), and the maximum is 2. Merge the two into "PUGET SOUND, 2024", the way s189 does.
    Minor and optional: s184's highway sky `#e7f3e7` is off-palette, so `#8fd3ff` would match.

## Director's "left as is" items: rulings
- **s093, s103, s112, s155, s186 (Doug over the map frame): ACCEPTED.** Doug stands in the margin as a presenter, and the bible's
  frame rule covers text, not Doug. His head and cap stay clear of the frame line in all five (s186 doesn't actually touch it).
  The s155 *label* is still fix 17.
- **s255 (crop): ACCEPTED.** This is a `pan_down` depth-meter shot on a 3240 px canvas, so the keyframe is the end frame of the pan. Towers 5-6
  being cut at the top is just the camera move; all 6 are seen during the pan, and the whale sits on midnight `#0b2447`.
- **s181 (satellite near the caption): ACCEPTED.** It sits below the chapter bar without touching it, and the panels read as a satellite.
- **s212 (label over the edge): REJECTED.** See fix 15. Wordart crossing a map frame is a hard bible rule.

## Style bible 7 checks (keyframe level)
- Rule 1 (two tiers): PASS. Rule 2 (cap always visible): **FAIL** at s059 and s077 (fix 1). Rule 3 (caption bar): PASS.
- Rule 4 (labels, max 2): **FAIL** at s317 (fix 31). Chart axes, depth markers and price tags are counted as furniture.
- Rule 5 (annotations): PASS, every item has several. Rule 6 (value ramp): **FAIL** for the polar water (fix 30). Everything else
  matches the ramp (reef/open water `#3a9ad9`, sperm whale `#0b2447`, and "no light" beats near-black as a lighting device).
- Rule 7 (silhouette then reveal): PASS. First appearances (s047, s246, s270, s279) glow, and shadows of creatures already shown use
  `glow_r: 0`. Rule 8 (no gore): PASS. Rule 9 (photos): not used.

Routing: fixes 1-23 and 25-31 go to the **director**. Fix 24 (`water_splash`) goes to the **illustrator** first, then to the director for the swap.
After the fixes, re-render only the touched shots with `--shots`, and send me the new sheets for round 2.

KEYFRAMES: FAIL (round 1)

# Keyframes round 2

Reviewer: art director, 2026-10-05. Scope: the 70 re-rendered shots from the director's round-1 fix report
(`build/contact/sheet_01..06.png`), full-res crops from `build/keyframes/` where needed (s110, s113, s138, s193, s212, plus
pixel measurement of right-edge text on s186, s212, s213, s251, s288). I also reviewed the new library asset `water_splash` /
`water_splash_small` (`assets/previews/008-ocean-food-chain-splash*.png`).

## Verdict: PASS (with 1 blocking fix: a one-line move; no re-review needed once it is applied)

**Asset `water_splash` / `water_splash_small`: APPROVED.** It reads as a splash (not ice) on sky, open-water and navy backgrounds.
It is in the detailed tier (layered `#bfe6ff` fills, `#3a9ad9` inner strokes, white highlights, droplets), and the base ring sits in
the water. s096, s101, s102, s109, s110, s163, s223, s233, s243 and s247 all anchor it on the waterline. The ice-field read is gone.

**Round-1 fixes verified as done:** 1 (cap on the floor in s059/s060/s077/s078), 2-4 (counter zone clear in s015-s019, s268, s189,
s317), 5-12 (text clear of creatures in s060, s061, s105, s113, s114, s125, s138, s143, s282), 13-22 (s179, s194, s212, s213, s155,
s183, s251 *frame*, s288, s291, s267), 23 (boat at x 320 in s130-s132), 24 (splash swapped; sand puff in s193; no splash under the timer in s234;
a single splash in s243), 25 (tide table in hand in s191), 26 (15 red-tinted of ~40 in s299 now reads), 27 (moray head and mouth
visible in s058), 28 (car on the jaws plus down-arrows in s174), 29 (sun filled in s235/s236), 30 (polar water `#3a9ad9` in s197-s205),
31 (PUGET SOUND, 2024 merged in s317), and the advisory s184 sky `#8fd3ff`. The s212 finish banners at 0.45 now read as banners.

**Director's flagged shots:**
- **s155: OK.** THOUSANDS OF KM sits inside the map over open Pacific, the turtle-Doug presenter is in the margin, and the cap is clear.
- **s193: OK.** The sand puff reads as dust (not water), and the cap on the sand carries rule 2. See advisory A2.
- **s234: OK.** The timer stands in clear sky with no splash. "< 1 MINUTE" (top about y 265) is clear of the counter zone.

Style bible 7, rules 1-9: PASS on all 70. The cap is visible on every death beat, labels stay at 2 or fewer (s317 fixed), the value ramp is consistent, and there is no gore.

## Blocking fix (director)
1. **s251**: WHOLE SEASON (label centred at x 1720, size 40) runs to x 1898, which is 22 px from the frame edge and outside the safe area
   (new art bible "Text" rule: x 64-1856). Set the label to x 1680, size 36, and move the calendar to x 1680 with it. Re-render `--shots s251` only.
   No art re-review is needed: confirm the label's right edge is at 1856 or less and move on.

## Advisory (polish, not blocking)
- A1. **s110**: the grey `spray` (1350,640, `#222222`) meant as tern feathers lands on the trevally's back and reads as a dirty
  smudge. Use `#ffffff`/`#dddddd` at about (1350, 560), above the fish, or delete it.
- A2. **s193**: the croc still sits mostly in the green water band. Drop it to y about 830 so its feet are on the sand where Doug stood,
  and the sand puff will sit under it naturally.
- A3. Right-margin text that is inside the safe area but tight: s212 "16 MARATHONS" reaches x 1855, s288 STARBOARD x 1842, and
  s186 TORRES STRAIT x 1834. If you touch these shots anyway, shift them left about 30 px.

KEYFRAMES: PASS (round 2), conditional on blocking fix 1 (s251)

# Keyframes round 3

Reviewer: art director, 2026-10-05. Scope: blocking fix 1 (s251), spot-check of s077, s078, s109, s110, s186, s193, s212, s288,
and the revised thumbnail (`build/thumbnail.png`) against s001.

- **s251: FIXED.** WHOLE SEASON (x 1680, size 36) box right edge measures x 1840, which is inside the 64-1856 safe area. The calendar moved with it, and the ghost Doug and counter are clear.
- **Advisory A1 (s110): done.** The grey smudge on the trevally is gone. **A2 (s193): done.** The croc's feet are on the sand line, with the sand puff under it, and the cap on the sand carries rule 2.
  **A3: done.** Measured right edges are s212 "16 MARATHONS" x 1825, s288 STARBOARD x 1812 and s186 TORRES STRAIT x 1804.
- **s077/s078:** the cap is on the floor, the ghost Doug is on-model with the cap visible, and PACKAGING wordart is clear of the counter and the caption. OK.
- **s109:** the tern-suit Doug is on-model, the splash is on the waterline, and the shot differs clearly from s110 (a vertical breach versus a re-entry and speech bubble). OK.
- **Thumbnail v2 vs s001:** same pyramid layout, tier colours, creature drawings and Doug-in-shrimp-tier gag. The orca crown reads at small size,
  and the labels are legible. It is consistent with the opening shot.

Style bible 7, rules 1-9: PASS on all checked shots. There is no gore.

Keyframes round 3: PASS
