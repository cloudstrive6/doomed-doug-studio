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

---

# Keyframes review, round 1 (art director, 2026-10-23)

Scope: all 24 contact sheets (s001-s281 plus the endslate), with full-size checks of s126, s127, s161, s177, s186, s213,
s229, s238 and s254, and the 3 thumbnails (`build/thumbnail.png`, `_b`, `_c`, plus their `_small` versions).

**Round-1 fixes: all verified.** A1 (the hook arm has a rounded club tip and an open J hook with a gap, seen in s119-s135
and thumbnail A), A2 (the xenophyophore is reticulate with no face at 2.0 in s257/s258/s275), A3 (the foram has no stick),
D1 (s010/s020 oarfish upright, head right), D2 (s227 Doug at 700/839, the leg runs through the chest piece, the empty
`rope_hook` shows he unclipped, and his feet are on the ground in s227 and s228), D3 (one cap per frame in s055/s056),
D4 (the s054 cable ends on the ring), D5 (every first-reveal silhouette has `glow_r: 0` and a red rim), R1 (the s054 cap
sits at about x 1805).

**What works.** Doug is on-model in every shot. He auto-inks white on all the dark zones and keeps his red cap, including
on the ghosts. The two-tier contrast holds everywhere. The zone ramp is correct from s078 on (midnight `#0b2447`, abyss
`#050a1f`, hadal `#020308`). The counter and the CABLE OUT meter are never touched. Layouts vary well: maps, depth bars,
the aquarium set, the Te Papa set, close-ups (s117, s118), the split screen (s178), graphs (s144, s241), the recap
pyramid (s274) and the TV ending (s278-s281). Thumbnails A and B pass.

**Verdict: FAIL.** There are 4 blocking fixes (K1-K4: three gore or "impaled" reads and one invisible subject) and 10
smaller fixes. They are all shotlist or composition fixes, so they go to the **director**. T1 goes to the graphic
designer. No new assets are needed.

## Blocking (director)

**K1. s229: Doug looks skewered.** The giant sea spider (1050, 935, x1.1) has 4 left legs that pass straight through
Doug's head, cap and body (Doug is `on_back` at 760, 888). It reads as impaled (art bible: no lines through Doug).
Move Doug to **x ≤ 430** (same y and scale) so the leftmost leg tip (about x 590) clears his feet by at least 30 px.
Or, if the death needs contact, rest one leg tip *on* his chest from above and let no leg cross his head, cap or limbs.

**K2. s126 and s127: the arm piece reads as a severed limb or a wound.**
- s126: `colossal_squid_hook_arm` lies `rotate: 90` on the floor, and its flat base cut shows at about (1145, 900-940).
  That is the exact "severed stump" read that A1 removed from the tip. Put the piece inside a specimen jar
  (`glass_jar`, with the cut end hidden behind the jar's lower rim or label), or crop it so the base runs off-frame or
  behind the scientist's feet. The cut edge must never show.
- s127: the dark-red sliver at 0.18 sits on the whale's belly next to the flipper (1050, 700). It reads as a bleeding
  gash, not as stomach contents. Show the stomach as a cartoon x-ray: fill the ellipse with pale `#f3e6e0` at about 70 %
  opacity, or use a white inset circle with a black 4 px frame. Put 2-3 arm pieces inside at 0.22 or larger, clear of the
  flipper, with no cut ends showing (curl them or overlap them). The arrow stays.

**K3. s185 and s186: bigfin silhouette filaments read as red drips.** The 4 px red rim on hair-thin filaments turns
them into 16 solid red streaks running down to the seabed (s186 full size). That reads as blood running, and it hides the
"something **pale**" in the narration. Keep the silhouette and rim on the mantle, fins and arms only. Either draw the
filaments as unsilhouetted thin lines in `#3a3f52` (the same asset at the same x/y/scale, under a silhouetted copy masked
above y ≈ the elbow line), or drop the rim to `{"color": "#8a1a1a", "px": 2}` for these two shots. Re-render both. In
s185, also keep the BIGFIN SQUID title clear of the fins: move the squid to y 470 or the title to x 880.

**K4. s213: the "few millimetre" spider is invisible.** At scale 0.04 the spider is a speck on Doug's cap brim, so the
"A FEW MM" arrow points at the **cap**. Put the tiny spider on Doug's front hand (about 850, 828). Add a white magnifier
inset circle (r about 150, black 4 px frame) at about (1180, 700), with `giant_sea_spider` at 0.22 inside it and a dotted
line from the hand to the circle. Point the arrow from the label to the inset. Keep the label where it is.

## Fixes (director)

**K5. Clipboard (R2 conditions) in s177, s238, s254.** "BRING YOUR OWN FOOD" runs edge to edge on the sheet with
0-2 px margin, and in s238 and s254 the narrator's glove touches the "MORE OXYGEN" / "PRESSURE?" lines. R2 requires the
hand to stay clear of the text. Fixes:
- Keep at least **14 px** of white margin on both sides of every line. Wrap "BRING YOUR / OWN FOOD" onto two lines
  (with line spacing tightened from 60 to about 52 x scale so 6 lines plus the title still fit). Never go below 26 px glyphs.
- Glove fingertips at least **20 px** from any glyph. Bring the hand in at the board's lower-right corner (below the last
  line) or hold the board edge at x ≥ the sheet's right edge + 10.
- s272 (no hand) has the same margin problem, so apply the wrap there too.
Once this holds, I add the clipboard as a recurring layout in the art bible.

**K6. s055 and s056: zone colour.** These are death beats at **350 m**, but the background is midnight `#0b2447`, so they
spend the midnight colour before the 1,000 m mark (art bible: items stay on their zone colour, death beats included;
never borrow a deeper ramp colour). Use twilight `#1b4f86` with the s054 seabed fills (`#5e5a50` / `#4e4a42`).

**K7. s184 "TOO DEEP." card: zone colour.** The meter reads CABLE OUT 3,000 M, but the background is abyss `#050a1f`.
Like BIG. (s005, twilight) and BIGGER. (s078, midnight), the card takes the colour of its own depth: `#0b2447`. (The
other fix is to read 4,000 M, but the narration does not support that.)

**K8. s161: title over plumes.** The tallest tube-worm plume (about 1130, 300-400) sits behind the red "TUBE WORM"
letters, so it is red on red. Move the title up to y 250 or the cluster down/right by about 80 px. The title must clear
every plume by at least 15 px.

**K9. s023: label over Doug.** ROBOT SUBMARINE (560, 820, size 66) runs through Doug (260, 830, 0.32). Move it to
**(660, 760)** so it clears his outstretched arm and the ROV.

**K10. s247: WordArt on pale.** HALF THE OCEANS (960, 1000) sits on the map's bottom frame and the pale ice, so lime on
near-white is unreadable at phone size. Shrink the map to about 0.75 and raise it so its frame ends at least 20 px above
the glyph tops. The WordArt must sit entirely on black.

**K11. s277: cap continuity.** Doug dies on the mud still wearing his cap, then in s278-s279 the cap sinks into frame
from above. Give s277 `"gear": ["cap_taken"]` (not `cap_off`, which drops a second cap on the ground) plus a `doug_cap` at about (900, 520), scale 0.45, rotate
-20, drifting up. Then s278 picks up a cap that is visibly already loose.

**K12. Oarfish run, s022-s029: same composition 8 times.** Doug is left on the cable and the oarfish is vertical right in
eight shots in a row (and s009-s012 before that). The sign beat (s025-s027) is a fair build-up group, so change only s024
and s028:
- s024 ("about fifteen years ago"): a timeline card, 2011 → TODAY, dotted line, small oarfish icon at 2011 (the same
  device as s128).
- s028 ("Doug is fine."): a punch-in on Doug at 0.9-1.0 with a thumbs up, oarfish edge in frame, like s117/s118.

**K13 (minor). s263: night water.** The surface water is deep navy, which reads as a deeper zone. Keep the night sky if
you want it, but make the water the surface colour `#3a9ad9` (art bible: any surface scene uses the surface colour) with
`#6fc1ee` speckle.

**K14 (minor). Labels over filaments.** "BLEND IN" in s203 and "ISN'T DOUG" in s206 cross the bigfin filaments. Move
each label 60-80 px up, or sideways onto clear water.

## Thumbnails (graphic designer)

- **A (`thumbnail.png`): PASS.** Archetype C, one word, the eye reads at 168 px, the hook arm has the fixed club tip and
  open J hook, small scared Doug, dark navy. It is also a clean s001.
- **B (`thumbnail_b.png`): PASS.** Archetype C, "10 METERS", the jelly reads, Doug's face and cap stay clear of the
  arms, no gore.
- **C (`thumbnail_c.png`): FAIL. Fix T1.** The auto-fit labels come out in 2 sizes ("Colossal Squid" and "Greenland Shark"
  at about 60 % of the others), so the grid looks uneven at 168 px. Use **one label size** for all 6 tiles (the largest
  size the longest label fits). Rule 10 says labels = chapter names, so use the chapter names where they fit in 4 words or
  fewer: "Giant Oarfish", "Giant Isopod", "Colossal Squid", "Greenland Shark", "Supergiant Amphipod", "The Giant Cell"
  (or drop the "Giant"s consistently if the size gets too small, but treat all tiles the same). The dark grid is accepted
  for this episode under the brief's "thumbnail stays dark" rule.

## Routing
- Director: K1-K14. Then re-render only the affected shots (`--shots s023,s024,s028,s055,s056,s126,s127,s161,s177,s184,s185,s186,s203,s206,s213,s229,s238,s247,s254,s263,s272,s277`)
  and I re-check those frames only.
- Graphic designer: T1 (thumbnail C).
- Illustrator: nothing.
- Stage: **do not** move to `art_approved`. Once my re-check passes **and** the visual-screener passes, run
  `python -m studio stage 026-deep-sea-giants art_approved --note "AD+VS pass"`.

---

# Keyframes review, round 2 (art director, 2026-10-23)

Scope: the re-rendered frames for K1-K14 at full size (s023, s024, s028, s055, s056, s126, s127, s161, s177, s184, s185,
s186, s203-s206, s213, s229, s238, s247, s254, s263, s272, s277, s278), the oarfish run s022-s029, the whole Greenland
chapter s136-s160 (visual review item 17), the three thumbnails and their `_small` files, and the `FEED_SIZE` change in
`studio/__main__.py`.

**Verdict: FAIL.** 13 of the 14 K fixes and T1 are verified. Three small shotlist fixes remain (R2-1 to R2-3). All three go to the
**director**, and all three are one-line edits I have already test-rendered. No new assets are needed.

## Round-1 fixes verified
- **K1 s229: fixed.** Doug is at x ≈ 300 on his back, and the leftmost leg tip (≈ 590) clears his feet by about 75 px. No line crosses him.
  The empty `rope_hook` reads as "unclipped".
- **K2 s127: fixed.** The pale x-ray inset has three hooked pieces whose ends are curled or cropped by the frame. There is no red gash on the
  belly, and the arrow lands on the inset. **s126: almost fixed.** The jar works, but see R2-1.
- **K3 s185/s186: fixed.** The rim is now `#8a1a1a` at 2 px, so the filaments read as dark threads, not red drips. The s185 title clears the fins by about 110 px.
- **K4 s213: fixed.** The tiny spider is on his hand, with a white inset at 0.22, a dotted line, and the arrow on the inset.
- **K5 s177/s238/s254/s272: fixed.** "BRING YOUR / OWN FOOD" is wrapped, the margins are ≥ 14 px and the fingertips are ≥ 50 px from the glyphs. The smallest glyph is
  30.6 px (s254, board 0.9). s238 has `hold 0.8`. The clipboard is now a recurring layout in the art bible.
- **K6 s055/s056: fixed** (twilight `#1b4f86`). **K7 s184: fixed** (`#0b2447`). **K13 s263: fixed** (surface `#3a9ad9` water under
  the night sky).
- **K8 s161: fixed.** The title sits at about y 360 and clears the tallest plume by about 30 px. It crosses the left smoker's smoke and Doug's cable, and is still readable.
- **K9 s023: fixed.** ROBOT SUBMARINE clears Doug's arm and the ROV.
- **K10 s247: fixed.** HALF THE OCEANS is entirely on black.
- **K11 s277: fixed.** `cap_taken` with the cap drifting up, and s278 picks it up on the LIVE feed. There is one cap per frame.
- **K12: fixed.** s024 is now a timeline card (oarfish icon `rotate 90 + flip`, upright with its head right, per R3), and s028 is a punch-in with a thumbs up.
  The run s022-s029 now breaks twice. Optional: in s024 the cable crosses the dotted timeline at x ≈ 500. Moving Doug to x ≈ 960, below
  the line, would clean it up. Not blocking.
- **K14 s203/s206: fixed.** BLEND IN and ISN'T DOUG are on clear water.
- **T1 thumbnail C: fixed.** All six tiles use one label size, with the Giants dropped consistently. "One Cell" sits left on purpose to keep the
  duration badge clear, and I accept that. **A** is unchanged: PASS. **B** (re-done for visual item 11): PASS from me. Doug is bigger and
  central, the cable ends at his harness, the stub is gone and there is no gore. One nit for the graphic designer, not blocking: a short white leg line
  shows under the lower tentacle at about (1920, 630) at 1280 scale. Hide it under the tentacle or remove it.

## Remaining fixes (director)

**R2-1. s126: the cut end still peeks out under the SPECIMEN label.** A 45 x 10 px red sliver with a straight black cut edge shows
between the label's bottom (y 880) and the jar floor (about y 890). The bible rule is that no part of a cut end may show. Fix: `colossal_squid_hook_arm` **y 880 → 860**
(same x and scale). I rendered it: the base is fully behind the label, and the J hook stays inside the jar neck.

**R2-2. Visual review item 17, frosted cable: ruling.** Keep the frost, because the script asks for it ("a thin crust of frost on the cable",
item 6). But redraw it and make it consistent. The current overlay (`#eef6ff`, width 13, dash [22,9]) is wider than the cable, and every dash
picks up black end caps, so it reads as a zipper. It also flips on and off from shot to shot (frosted: s136-s141, s145-s147, s150,
s153, s159; plain: s143, s151, s152, s154, s155, s157, s158). New spec (test-rendered, now in the art bible):
- Replace the dashed overlay with a **solid sheath drawn before (under) the cable, using the same points**:
  `{"type": "line", "points": <cable points>, "color": "#c9d6e6", "width": 11}`, then the existing `#c0c6cc` width-5 cable on top.
  No dash and no spray.
- Apply it to **every s136-s159 shot that shows the cable**. That means adding it to s143, s151, s152, s154, s155, s157 and s158 (s157/s158 use the
  same angled points). s142, s144, s148 (the timeline bar itself is not a cable), s149, s156 and s160 have no cable, so leave them alone. It stops at the
  chapter end (s161, tube worms, plain cable).

**R2-3. s203/s204: hands_hips substitution rejected, use the new pose `elbows_out`.** `hands_hips` gives bent elbows, so the narration
is technically true, but the gag is that Doug copies the squid. The bigfin's arms go straight out and then drop sharply at the elbow, and
akimbo arms do not echo that shape. In s203 the hands also disappear behind the harness belt. I have added **`"pose": "elbows_out"`**
to `studio/doug.py`: upper arms straight out sideways, forearms hanging straight down, the same squared silhouette as the squid. I test-rendered s203 and s204 with
it (same x/y/scale, harness on). It reads at once as mimicry, and the strop only crosses the back arm (fine, per R4). Change only the
`pose` field in both shots.

## Engine and tooling
- `studio/doug.py`: new pose `elbows_out` (`arm_f=(90,-90)`, `arm_b=(-90,90)`, legs as in `hands_hips`). This only adds a pose, so no existing pose
  or render changes. Documented in `docs/SCENE_SCHEMA.md` and `channel/art_bible.md` (Doug gear section).
- `studio/__main__.py` `FEED_SIZE = (168, 94)`: **sane, approved.** It matches the 168x94 standard in the style bible (rule 11), the
  graphic-designer and visual-screener briefs and `produce_episode.md`. No other code reads the `_small` files, so nothing else breaks. 168x94 is
  16:9 within half a pixel. Note: the `_small` previews are now LANCZOS-downscaled straight from the source image. That is correct for a feed preview.
- Art bible additions: the clipboard recurring layout (R2 + K5 conditions), the frosted cable spec, and the specimen jar / cut-pieces rule.

## Routing
- Director: R2-1, R2-2, R2-3. Then re-render `--shots s126,s136,s137,s138,s139,s140,s141,s143,s145,s146,s147,s150,s151,s152,s153,s154,s155,s157,s158,s159,s203,s204`.
  I re-check only those frames.
- Graphic designer: the optional thumbnail B leg-line nit.
- Stage: **do not** move to `art_approved` yet. Once my round-3 check passes **and** the visual-screener passes, run
  `python -m studio stage 026-deep-sea-giants art_approved --note "AD+VS pass"`.
