# 026 Deep Sea Giants: art review, round 1 (art director, 2026-10-23)

Scope: the new library drawings in `asset_requests.md` (commit 4c54ebc: 30 JSON files, counting `giant_sea_spider`,
`_xray` and `_cap` separately), previews `assets/previews/026-*`, plus my own check renders of harness poses, oarfish
rotations, close-ups at shot scale, and s227/s055. Also rulings on the director's two calls in `decisions.md` and the
illustrator's notes. (`assets/previews/026-assets-a.png` is a stale first pass with the old oarfish and dropcam; I
ignored it.)

**Verdict: FAIL.** 27 assets approved, 3 need fixes (illustrator). The director has 5 composition fixes. None of it
is big. Once the 3 assets are redrawn and re-previewed I re-check only those, then the episode can go to keyframes.

## Assets

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | cable_harness | APPROVED | The strop clears the head and brim in float, point, arms_up, crouch, cower and swim. The ring sits at (-170,-400). Reads on navy and white. |
| 2 | cable_counter_icon | APPROVED | Reads as a winch drum with a red crank at 0.16. Clearly not 006's depth gauge. |
| 3 | why_clipboard | APPROVED | Sheet is flat white, the text zone is empty, and the clip is clear of the title line. |
| 4 | drop_camera | APPROVED | Yellow frame, two orange floats, camera and lamp, lifting ring. Bold. |
| 5 | giant_oarfish | APPROVED | Silver ribbon, red crest and full dorsal, streamers. Reads as an oarfish. Silhouette and rim are clean. See ruling R3 for rotation. |
| 6 | giant_oarfish_beached | APPROVED | Limp crest, cartoon X eye, no wounds. Head right. |
| 7 | japan_map | APPROVED | Four main islands are recognisable at 1.4x (I checked). On the world_map style. |
| 8 | japan_map_cracked | APPROVED | Crack and chips sit across Honshu. The geometry matches japan_map. |
| 9 | spider_crab_folded | APPROVED | Reads as a closed tent or umbrella. Optional, not blocking: the two stubby claws under the round spotted body read slightly as little feet on a cookie. Thinner, longer claws tucked in front would be safer. |
| 10 | japanese_spider_crab_cap | APPROVED | Cap held clearly in the raised claw with the brim to the right. The crab matches the library version. |
| 11 | giant_phantom_jelly | APPROVED | Four ribbon arms, maroon is mid-tone on navy, the bell has a lighter rim. It is a solid shape, so it never reads as blood. |
| 12 | pelagic_brotula | APPROVED | Optional: in silhouette the chin filaments read as a little foot (s071 only). Shortening them by about a third would fix it. |
| 13 | tennis_court_top | APPROVED | Net at the top, service line about 54 % down, centre service line, singles and doubles lines. Correct proportions. |
| 14 | giant_isopod | APPROVED | Segmented armour, dark compound eye, antennae, tail fan, 7 visible legs. Unbothered, not cute. |
| 15 | giant_isopod_rolled | APPROVED | Armoured ball with the eye and tail just showing. Clean circle silhouette. |
| 16 | giant_isopod_full | APPROVED | Pale belly bulges between the plates, sweat drop. The joke reads at 168 px. |
| 17 | colossal_squid | APPROVED | Heavy maroon mantle, fins, huge pale eye with a heavy lid (grumpy, not cute), hook rows visible. |
| 18 | colossal_squid_juvenile | APPROVED | Glassy, chromatophore dots, big eye, no smile. |
| 19 | **colossal_squid_hook_arm** | **NEEDS FIX** (illustrator) | See fix A1. |
| 20 | greenland_shark | APPROVED | Heavy cigar body, dorsals set far back, tiny pale eye, flat mouth. |
| 21 | mayflower_ship | APPROVED | Bold, period-correct enough, red pennants, clean silhouette. |
| 22 | giant_tube_worms | APPROVED | Thick white ringed tubes, red plumes, rubble base. Clearly not `tubeworm_cluster`. |
| 23 | bigfin_squid | APPROVED | Mantle up, big fins, elbowed arms, long filaments. Eerie at every size. The filaments are thin but still read on hadal black. |
| 24 | giant_sea_spider | APPROVED | Eight jointed legs, tiny body, proboscis. |
| 25 | giant_sea_spider_xray | APPROVED | The orange gut branches and red heart show at 0.6. This is the minimum, so keep it at 0.6 or larger in s221-s225. |
| 26 | giant_sea_spider_cap | APPROVED | The lifted front-right leg carries the cap clearly. |
| 27 | stethoscope_crouch | APPROVED | Earpieces at the head sides, tubing clear of the face and cap, chest piece in the front hand. |
| 28 | supergiant_amphipod | APPROVED | Long segmented body, side plates, antennae. It is distinct from the isopod at swarm scale. |
| 29 | **xenophyophore** | **NEEDS FIX** (illustrator) | See fix A2. Blocking: this is the boss, at 1.6-2.2 in s257-s275. |
| 30 | **foram_shell** | **NEEDS FIX** (illustrator) | See fix A3. Small. |

## Fixes for the illustrator

**A1. `colossal_squid_hook_arm`** (s119, s120, s126-s127, s132-s135)
1. The arm ends in a flat, squared-off cut at about y -560..-600, with a round knob on the corner. On a red tentacle, a
   flat end reads as a severed stump (gore-adjacent) or a pipe. Taper the tip into a rounded club, narrowing from about
   90 to 50 units wide over the top 120 units, with no straight cut edge.
2. The top hook currently reads as a closed loop or bag handle (cream ring from about (-22,-630) round to the knob
   at (40,-560)). Redraw it as an open claw hook, a J that curls up and over, with a sharp tip pointing down and
   **a visible gap** between the tip and the arm. Then the cap reads as *snagged*, not threaded on a handle. Keep the cap
   hang point at local **(0,-580)** and the top-hook bbox within about x -30..50, y -640..-540, so s132-s135 do not move.
3. Put 2-3 of the smaller hooks on the right edge as well, so the hooks are not a one-sided comb. Keep them the same cream `#efe6d0`
   with a dark outline.
4. Re-preview on `#0b2447` at 0.75 with `doug_cap` at 0.4 placed as in s132 (asset at (760,1080), cap at (760,655)).

**A2. `xenophyophore`** (s003, s253 silhouettes; s256-s281, close-ups at 1.6-2.2)
1. **Pareidolia face.** At 2.0, the pores at about (-45,-105) and (+45,-110) with the big one at (+5,-50) form two eyes and
   a shocked open mouth. The brief says no face, and this is the boss close-up. Break the triangle: move the
   largest pore off-centre (for example to (+70,-45)), change the sizes so no two pores at the same height match, and do not
   line two similar pores up horizontally above a bigger one.
2. **Honeycombed is missing.** Right now it reads as a grey rock or meteorite. Add a fine reticulate texture (a net of
   thin ridge lines `#6e675b`, width 2-3, about 15-25 unit cells) over the lumps, plus 6-10 small pinhole pores
   (r 4-7) between the 6 tenant pores. The fragile, layered "mud-grain sponge" look is what makes the twist land.
3. Keep the outer outline, bbox (x -132..132, y -196..0) and flat base exactly as they are. The silhouette shots are
   already laid out, and the silhouette is fine.
4. Re-preview on `#020308` at 2.0 and at 0.5.

**A3. `foram_shell`** (s259)
1. The brown rod with a knob coming out of the aperture at about (+30,+30)..(+50,+45) reads as a lollipop stick or a
   matchstick through the shell. Remove it. If you want life signs, use 3-4 very thin pale `#f6f0e0` branching
   pseudopod threads (width 2) out of the aperture instead.
2. Otherwise approved: the chamber spiral, cream fill and thick outline read well under a microscope view.

## Fixes for the director (shotlist)

**D1. s010 and s020 oarfish orientation (illustrator note).** `rotate: 90` turns the fish **belly-up**: head right,
dorsal fin underneath, streamers on top. It reads as a dead fish (render checked). Use `"rotate": 90, "flip": true`,
which gives head right, dorsal on top and streamers below, matching `giant_oarfish_beached`. (`"rotate": -90` without flip is
also upright but faces left.) Same anchor and size, so the layout does not change.

**D2. s227 spider legs over Doug (illustrator note).** I do not accept "legs framing him". At (1150, 935) x1.4, one
leg passes behind his head and another runs through the cap brim and stethoscope. Also, Doug's feet are about 30 px
below the seabed (hip 870 at 0.6 puts the feet at 961, and the ground is at about 930). I rendered and checked this fix:
- `doug` and `stethoscope_crouch` at **(700, 839)**, scale 0.6, so the feet land on the ground line.
- `giant_sea_spider` at **(1320, 935), scale 1.25**. Its outermost left leg then passes right through the chest piece
  (canvas about (803, 810)). The leg clears the cap brim by about 75 px, no leg crosses Doug, and the right leg tips stay in
  frame at about x 1845. DIGESTION at (1250, 340) stays clear of the leg tops, which are at about y 450.
- Optionally slide the yellow digestion squiggle to sit along that outer leg, around (820-900, 700-760).
- Continuity: s226 shows him clipped (harness + cable), but s227-s229 show him on the seabed with no harness and no cable.
  Fine if he has landed and unclipped, but s227 is the first frame of that. Either keep the harness and a slack cable in s227-s228,
  or add an empty `rope_hook` on the cable (as in s055) so the unclipping reads. Also check s228 (cower, hip 870): put his
  feet on the ground line the same way (hip = 930 - 152 x scale).

**D3. s055 and s056: two caps on screen.** In s055 the `on_back` body wears the cap while `japanese_spider_crab_cap`
holds it. In s056 the body wears it while `doug_cap` lies on the ground. Add `"gear": ["cap_taken"]` to the `on_back` Doug
in **both** shots. This is new engine gear (below): no cap on his head and none on the ground. The ghost in s056 keeps its
cap as usual. I verified s055 with it.

**D4. s054 cable end.** The cable line ends at (1200, 600), but the harness ring is at (1224, 580), so there is a 31 px gap.
End the line exactly at **(1224, 580)**. All other harness shots line up within 6 px.

**D5. Silhouette reminder.** s003/s057 correctly use `glow_r: 0` + red `rim` with a dark water-tone spray before them. Keep that on
every first-reveal silhouette (s008, s071, s110, s253). The illustrator's oarfish detail preview uses the default red speckle glow.
Underwater, that reads as blood, so do not copy it into a shot.

## Rulings

**R1. Capless upright Doug in s052-s054 and s132-s133: APPROVED** as a logged one-off. It is script-driven, and the cap is in
frame on the crab or hook in every shot (checked). Conditions:
- In s054 the crab is at 0.5 at x 1700, so the cap sits at about x 1825. Keep the whole cap at x ≤ 1856 in the keyframe, or move the
  crab to x ≤ 1680.
- The cap must stay readable at its size: no smaller than `doug_cap` at 0.4 (s132-s135), and the crab no smaller than 0.4 (s055).
- Doug gets his cap back from s057 onward (he does), and the death bodies in those beats follow D3.

**R2. WHY SO BIG? clipboard over 8 words (up to 13 in s238/s254/s272): APPROVED** as an episode-device exception, on
these conditions, which hold in the current shotlist:
- Only one new line per shot, and it is the red `#c0181b` line. The old lines are dark grey, so the eye goes to the new one.
- No wordart or other label on screen in those shots (true for s238/s254/s272). The narrator hand stays clear of the text.
- Minimum glyph size 26 px at 1080p. The smallest now is "BRING YOUR OWN FOOD" at 26.5 in s254, so do not shrink the
  board below 0.9.
- Any clipboard shot with under 2.5 s of narration gets a `hold` of at least 0.8 s (s238, "That's the next reason on the list.",
  is about 2 s).
I am adding this as a recurring-layout rule in the art bible if it holds through keyframes.

**R3. Rotated oarfish:** see D1. Horizontal oarfish always use `rotate: 90, flip: true` (head right) or `rotate: -90` (head
left). Never plain `rotate: 90`.

**R4. Harness vs swim and other poses: APPROVED as is, no variant asset.** Renders of swim1/swim2, crouch, cower, float, point and
arms_up with the harness:
- float, point, arms_up, wave, shrug, think, thumbs_up, hands_hips, walk, panic, cower: the strop clears the head and brim. Where it
  crosses the back arm, that reads as the strop behind him, which is fine.
- crouch (s102-s104, s276): the belt and loops sit on the hips and thighs. Fine.
- swim (s157-s158 only): the belt stays horizontal and the thigh loops hang under the hip, a little detached from the legs
  that trail out behind. At the shot scale (about 0.42) the loops are about 20 px and read as harness hardware, so they are
  acceptable for two shots. Do not use swim + harness above scale 0.55, or as a hero close-up. If an episode ever needs
  that, I will commission a `cable_harness_swim`.
- Never with `on_back` or `sit`. The current shotlist has none (checked).

## Engine change (art director)
- `studio/doug.py`: new gear **`cap_taken`**. It omits the cap in every pose, including `on_back`, and draws nothing on the
  ground. Use it only when a creature or prop in the same frame holds the cap. Existing `cap_off` behaviour is
  unchanged, and default and cap_off renders were checked unchanged. Documented in `docs/SCENE_SCHEMA.md` and `channel/art_bible.md`
  ("One cap per frame").

## Routing
- Illustrator: A1 (hook arm), A2 (xenophyophore), A3 (foram shell). The optional notes on #9 and #12 are your call.
- Director: D1-D5, then render keyframes for my keyframe review.
