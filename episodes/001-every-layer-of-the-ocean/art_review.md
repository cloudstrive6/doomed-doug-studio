# Art review: 001 Every Layer of the Ocean (new library assets)

Reviewer: art director · Date: 2026-09-29 · Scope: every drawing in `asset_requests.md` (56 assets), previews in
`assets/previews/001-*.png`. Test renders were made on the real zone colours from the art bible (twilight `#1b4f86`,
midnight `#0b2447`, abyss `#050a1f`, hadal `#020308`), with Doug composited at shot scale, and at small scales for
silhouette and thumbnail reads.

**Verdict: PASS**. All assets are APPROVED. Two character assets had small fixes, which I applied directly (see
"Fixes applied"). No redraws are needed.

## Global checks
- **Two-tier rule (style bible 7.1):** all creatures, places and vehicles use the detailed tier: layered flat fills,
  `spray` shading, a darker back and lighter belly, and 3-5 outlines. `scientist` and `diver` are correctly in
  Doug's crude tier (5 px lines, round head, grey crescent, oval eyes).
- **Gore (7.8):** none. `fish_halves` has flat pink cut faces and a bone line, with no red. The `bobbit_worm_strike`
  jaws are dark red inside, which is the mouth colour and not blood. `black_swallower_full` shows a clean translucent
  belly with the prey outline and nothing visceral.
- **Facing and anchors:** every asset faces right as requested. Anchors were checked in test renders: the man o' war
  waterline sits at y=0, the Everest summit is at about -750 with the flag, the lander feet are at 0, and the
  `squid_costume` hips are at Doug's hips.
- **Dark-zone legibility:** checked on each zone band. The dark creatures (`barreleye_fish`, `black_swallower`,
  `black_swallower_full`, `vampire_squid`, `vampire_squid_pineapple`) stay readable because of their mid-tone fills
  and lighter rims or bellies. Barreleye on twilight has the lowest contrast of the set, but it passes because the
  glowing dome and green eyes carry the read.
- **Palette:** requested hexes are used (`#b8322a` Humboldt, `#c8553d` giant squid, `#6b1f2a` vampire, `#ffd21f` sub,
  `#6bbf59` map, and so on), and nothing clashes with the ocean ramp. `doug_cap` matches rig `_cap()` exactly
  (`#e0201b`, 5 px, about 200 wide at scale 1, the same as the cap on Doug at scale 1).

## Per asset

### Creatures
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | portuguese_man_o_war | APPROVED | Lopsided float, crinkled crest and beaded tentacles to +420. The preview cell crops the tentacles, but the asset itself is correct. |
| 2 | cone_snail | APPROVED | The tented map pattern reads well, and the snail stays recognisable at 0.5 for the s044 grid. |
| 3 | cone_snail_engulf | APPROVED | The pink funnel has the yellow fish inside and the same shell as `cone_snail`, so the two swap cleanly. |
| 4 | small_fish | APPROVED | Cute but not babyish. |
| 5 | fish_halves | APPROVED | Gore-free cut, with whoosh lines. |
| 6 | bobbit_antennae | APPROVED | |
| 7 | bobbit_worm | APPROVED | Long segmented body with an iridescent stripe. The silhouette reads as a worm. |
| 8 | bobbit_worm_strike | APPROVED | Scissor jaws, a sand burst, and no blood. |
| 9 | humboldt_squid | APPROVED | The silhouette stays clear at 0.28. |
| 10 | humboldt_squid_white | APPROVED | Identical geometry, so the flash swap works. |
| 11 | giant_squid | APPROVED | Huge eye, club tentacles. |
| 12 | giant_squid_eye | APPROVED | |
| 13 | sperm_whale | APPROVED | Boxy head with sucker-scar rings. It also reads when rotated 180. |
| 14 | barreleye_fish | APPROVED | Clear dome with green tube eyes, plus the fake-eye nostrils. |
| 15 | barreleye_fish_eyes_forward | APPROVED | Only the eyes change, so the pop-in swap is clean. |
| 16 | vampire_squid | APPROVED | The cape web, blue eye and ear fins all read at midnight. |
| 17 | vampire_squid_pineapple | APPROVED | |
| 18 | anglerfish_male | APPROVED | No lure, as requested. |
| 19 | black_swallower | APPROVED | Looks small and harmless, as intended. |
| 20 | black_swallower_full | APPROVED | Translucent balloon belly with the coiled mackerel inside. |
| 21 | snake_mackerel | APPROVED | |
| 22 | zombie_worms | APPROVED | Reads as "pink shag carpet" and holds up at 3x. |
| 23 | hadal_snailfish | APPROVED | Calm, jelly-like and pale. It reads on hadal black. |
| 24 | amphipod | APPROVED | |
| 25 | crab | APPROVED | |
| 26 | swordfish | APPROVED | |

### Places and big props
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 27 | coral_reef | APPROVED | |
| 28 | whale_skeleton | APPROVED | The off-white bones read on abyss. |
| 29 | world_map | APPROVED | Equirectangular. Japan, the Marianas, California, the UK and Indonesia are in the right places. |
| 30 | aquarium | APPROVED | The middle is clear for Barry. |
| 31 | live_rock | APPROVED | |
| 32 | mount_everest | APPROVED | The summit and flag are at about -750. The preview cell crops the top, but the asset is correct. |

### Vehicles
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 33 | yellow_submarine | APPROVED | The porthole is clean for tiny Doug. |
| 34 | submersible | APPROVED | |
| 35 | trieste | APPROVED | |
| 36 | rov | APPROVED | |
| 37 | fishing_boat | APPROVED | |
| 38 | baited_camera_lander | APPROVED | The float top is cropped only in the preview cell. |
| 39 | school_bus | APPROVED | |
| 40 | small_car | APPROVED | |

### Scale-comparison props
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 41 | plastic_bag | APPROVED | The `#dcdcdc` fill reads on hadal black, and the outline is clean for the SIL use. |
| 42-52 | tv_remote, suitcase, traffic_light, basketball, american_football, banana, canoe, sofa, phone, chemical_barrel, harpoon_tooth | APPROVED | All are recognisable at a glance and on-palette. |

### Characters and Doug props
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 53 | squid_costume | APPROVED (prop) | See the ruling below. |
| 54 | doug_cap | APPROVED | Identical to the rig cap. |
| 55 | scientist | APPROVED after fix | Fixes applied (1 and 2 below). |
| 56 | diver | APPROVED after fix | Fix applied (1 below). |

## Ruling: squid_costume is a prop
It counts as a **prop, not a change to Doug's design**. It is a separate library asset drawn on top of the unchanged
rig, and Doug's head, face, grey crescent and red cap stay fully visible above the tube (verified with the `stand`,
`arms_up` and float-away rotate-25 uses). Doug's thin legs peeking between the cardboard tentacles is fine; it sells
the "homemade" joke. Conditions for the director:
1. Use **upright poses only** with the costume (stand, arms_up, panic1/2, wave, shrug, point). A horizontal `swim`
   pose breaks the illusion because the body leaves the tube. The current s082 and s083 use `stand`, and in s084 the
   costume is empty, so no change is needed.
2. Keep the costume's x/y/scale identical to the Doug element's.
I've added this rule to `channel/art_bible.md` (two-tier section).

## Fixes applied (by the art director)
1. **Human-tier ink on dark backgrounds** (`scientist`, `diver`). Their black lines vanished on dark backgrounds:
   the diver sits on twilight `#1b4f86` in s077 and s078, and the scientist on hadal rock in s206. I added the same
   auto white-ink rule that Doug uses. The engine change is in `studio/paint.py`: an asset with `"auto_ink": true`
   switches its black outlines to white when the background under it is dark, and elements marked
   `"keep_ink": true` (face, glasses, mask, coat details inside white shapes) stay black. I set these flags in both
   JSONs, verified them on light and hadal backgrounds, and documented them in `docs/SCENE_SCHEMA.md` and the art bible.
2. **Scientist arms** were drawn inside the lab coat, where they merged with the coat outline and made him look
   armless. I moved them so they start at the shoulders and hang outside the coat (±28,-122 → ±80,-18).

## Redraws needed
None.

## Routing
- Illustrator: nothing outstanding.
- Director: follow the squid_costume pose rule above. Otherwise, proceed to keyframes.

**OVERALL VERDICT: PASS.** All 56 new assets are approved, and art can move to keyframes.

---

# Keyframe review: 001 Every Layer of the Ocean

Reviewer: art director · Date: 2026-09-29 · Scope: all 245 keyframes (`build/keyframes/s001-s245.png`, contact
sheets `build/contact/sheet_01-21.png`). Checked against the art bible (zone ramp, two-tier rule, death counter,
title cards) and style bible section 7 (Art Director rules 1-9).

**Verdict: FAIL**. The style is right and consistent almost everywhere. The fixes below are mostly quick
composition moves for the director, plus the thumbnail for the graphic designer. No asset redraws are needed.

## What passes
- **Two-tier rule (7.1):** Doug, the scientist and the diver stay crude. Every creature, vehicle and set is in the
  detailed tier. The auto white ink works on every dark zone (s066-s245), for Doug and the scientist (s206).
- **Doug on-model (7.2):** the red cap is visible in every shot, including the ghosts, the tiny porthole Doug
  (s230-s245) and the squid costume (s082-s083, which follow the upright-pose rule). Expressions come from the fixed set.
- **Caption bar (7.3):** it's on every segment frame, and each bar matches its chapter name. The intro and outro
  (s001-s003, s244-s245) correctly have no bar.
- **Annotations (7.5):** every item has at least one arrow, X, "?", "!" or warning triangle.
- **Reveals (7.7):** each creature title card starts as a black silhouette with a red glow (s067, s085, s124,
  s145, s181, s207), and the full reveal follows 1-3 beats later.
- **Gore (7.8):** none. `fish_halves` (s055) is clean, and every Doug death is cartoon: X eyes, a ghost, a gravestone,
  or only the cap floating up in s179. The death counter runs 1-7 in the right places (s021, s043, s084, s160,
  s179, s197, s218) and ends with a strong seven-gravestone payoff in s243.
- **Zone ramp (7.6):** the zone title cards step down correctly: sunlight `#3a9ad9` (s004), twilight `#1b4f86`
  (s066), midnight `#0b2447` (s144), abyss `#050a1f` (s180), hadal `#020308` (s199).

## Engine fix applied (by the art director)
- **Blurry, jagged opening shot.** The s001 opening shot uses `scene_ref: thumbnail`, which is drawn at 1280x720.
  The engine was stretching that bitmap 1.5x with nearest-neighbour, so every line and letter came out jagged.
  `studio/assemble.py` → `_upscale_scene()` now redraws any smaller 16:9 referenced scene at 1920x1080 inside a
  scaled `group`, which gives crisp 1080p lines. I also added `studio/scene.py` → `fit_frame()`, used by both the
  renderer and the keyframes. It keeps nearest-neighbour for 1:1 frames and small push-ins, and uses Lanczos only
  for large upscales (1.25x or more). I re-rendered s001 and the contact sheets.

## Required fixes

### Graphic designer (thumbnail = opening shot s001)
1. **s001 / `thumbnail.json`**: the pyramid labels are broken. "ANGLERFISH / BLACK SWALLOWER" (x=50) is cut off at
   the left edge. "ZOMBIE WORMS" (x=1380) is off the 1280 canvas entirely. "MAN O' WAR" sits on the pyramid's edge,
   and the labels are 26 px, which can't be read at 168x94. Rebuild it as Archetype B: labels outside the tiers on
   alternating sides, fully inside the canvas, about 40 px or larger, and 4 words or fewer each. Label the bottom
   (abyss/hadal) tier too. This one blocks packaging anyway.

### Director: zone colours (art bible ramp, 7.6)
2. **s097, s098, s099** (Giant Squid, 630-900 m = twilight): these use midnight `#0b2447`, while the rest of the item
   uses `#1b4f86`. Set them to `#1b4f86`, and let the plankton spray carry "the dark".
3. **s133-s143** (Vampire Squid, 600-900 m = twilight, as s127 itself shows): these use midnight `#0b2447`.
   Set them to `#1b4f86`. The first midnight-coloured frame should be the s144 "MIDNIGHT ZONE" card, or the ramp
   stops reading.
4. **s146 (lower band), s147, s150, s151, s154, s159, s160, s161** (Anglerfish, midnight): these use an off-palette
   near-black `#050a18`, which looks like the abyss and steals s180's step down. Set them to midnight `#0b2447`.
   The red glow and bioluminescent sprays already carry the darkness.

### Director: labels, overlaps and safe area
5. **s005**: the red title "PORTUGUESE MAN O' WAR" sits on Doug's cap and the float's crest. Move the title up
   to y≈170, or move Doug and the float down about 80 px.
6. **s009**: the man o' war float is cropped by the top edge and hidden under the caption bar. Move it to about y=380
   at scale 1.2, so the whole float sits below the bar.
7. **s010**: the "THIRTY METERS" word art is crossed by both the purple tentacle line and the white dashed line.
   Move the word art to x≈1150.
8. **s017**: "FLOATING COMMITTEE" overlaps the float, and the "JELLYFISH?" label overlaps the tentacle tips.
   Put the word art at y≈150 and the label at x≈1450, next to Doug.
9. **s027**: "TV REMOTE" runs into the coral. Move it left to x≈1300, above the remote.
10. **s059**: the "CORNWALL, ENGLAND" label sits on the aquarium's top frame. Raise it to y≈150, or shrink the tank
    to scale 1.7.
11. **s068**: "DIABLO ROJO" is written across the boat cabin. Move it to x≈1450, y≈150, or move the boat left.
12. **s080**: "CANNIBALISM" is written over the bottom row of squid. Put it at y≈1000, below the grid, or at the
    top next to the stomach label.
13. **s189**: "SHAG CARPET" is written over the school bus. Move it to x≈1500, y≈420, clear of the bus.
14. **s212**: the two white pressure arrows cut through "800x PRESSURE". Start the arrows below the text
    (from y≈420) or move the text to y≈200.
15. **s176** (pan_up): at the end of the pan, the black swallower is at y=1200, so it's cut off at the bottom edge
    and never visibly reaches the surface. Doug (y=1850) is never on screen at the end either. Put the fish at the
    surface (y≈560, floating in the top band). If you want the rise to show, place Doug and the "GAS" word art
    where the camera actually passes.
16. **s241** (pan_down): the last gravestone (y=3300) ends up under the caption bar, cut off at the top of the
    final frame. Move it to y≈3550. Also, there are 5 gravestones for 7 deaths. Use 7, one per death, in the zone
    where each happened (2 sunlight, 1 twilight, 2 midnight, 1 abyss, 1 hadal).

### Director: at most 2 keyword labels on screen (7.4)
Depth and size markers (dimension tags) count as annotations, not labels. These shots still have 3 or more word labels:
17. **s015**: there are 5 labels (ONE JOB + FLOAT/CATCH/DIGEST/REPRODUCE). Keep "ONE JOB", and merge the four tags
    into one label: "FLOAT · CATCH · DIGEST · BREED".
18. **s131**: merge the crossed "VAMPIRE" and "SQUID" tags into one "VAMPIRE SQUID" label with a red X, and keep
    "LAST SURVIVOR".
19. **s143**: merge "GLOWING" and "STICKY" into one "GLOWING + STICKY" label, and keep "A WIN?".
20. **s156**: drop "FUSED" (s155 already showed the latch). Keep "SHARED BLOOD" and "ALL FROM HER".
21. **s186**: merge the three tags into one label, "NO MOUTH, STOMACH, GUT".
22. **s210**: merge the three tags into one label, "SMALL, SOFT, PALE", and keep "TADPOLE".
23. **s225**: drop "PICCARD + WALSH" or "TRIESTE", leaving 2 labels.
24. **s236**: fold "2017" into the depth tag ("2017 · 7,000-10,000+ m"), or drop it.

### Director: Doug staging and layout variety
25. **s050**: Doug is in the `sit` pose floating in open water. Sit him on the sofa (x≈960, y≈500, scale 0.5).
    That's the joke ("longer than a sofa") and the reason the sofa is there.
    **s051**: switch the `sit` pose to `stand` on the sand (y≈560), or to `float`.
26. **s150**: the tiny rotated, lying Doug at the bottom right (scale 0.3) reads as a dead Doug, a death before
    the actual death in s160. Remove him, or make him a normal-size, upright, curious Doug looking at the lure.
27. **s035-s043**: nine reef frames in a row use the same composition (snail left, coral cluster right, sand
    strip). Break it up: make s037/s038 a `zoom_in` close-up on `cone_snail_engulf` with no coral, and s039 a
    white-background "INSULIN WEAPON" card (an insulin-syringe-style harpoon plus the X-ed Doug from s034, or similar).

### Optional (nice to have)
- **s060**: Doug's head overlaps the aquarium's right frame. Move him about 60 px left, inside the glass.
- **s088**: the submersible sits in the South Atlantic on the map while the red circle is at Ogasawara. Move it
  next to Japan, or drop it.
- **s113**: the net reads as a wastebasket (it's only vertical lines). Add cross lines for a mesh.

## Routing
- **Graphic designer:** fix 1 (thumbnail).
- **Director:** fixes 2-27, then re-run `python -m studio keyframes 001-every-layer-of-the-ocean --shots ...`
  for those shots and send them back for a quick recheck.
- **Illustrator:** nothing. All assets read correctly in context.

**OVERALL VERDICT: FAIL.** The style and Doug are consistent, but the zone ramp breaks in three items and there
are overlaps and label-count violations. Expect a PASS once fixes 1-27 land.

---

# Keyframe review, round 2: 001 Every Layer of the Ocean

Reviewer: art director · Date: 2026-09-29 · Scope: all 245 re-rendered keyframes (contact sheets
`build/contact/sheet_01-21.png`, rendered after commit 5044d85). I looked closely at every shot named in round 1, the
visual-review round 1 shots, the new thumbnail (s001) and the new `thumbs_up_hand` asset.

**Verdict: PASS**. All 27 required fixes from round 1 have landed, and the changes introduced no new problems.

## Thumbnail / s001 (fix 1): PASS
- The labels now sit outside the pyramid on alternating sides. All are fully inside the canvas, large, and 2 words or
  fewer. The bottom tier is labelled ("Challenger Deep"), and the plastic bag there lands the payoff joke.
- The tier colours step down the zone ramp (sunlight → hadal). Every creature panel uses a detailed-tier asset on a
  saturated card, so it reads at feed size. Doug is on-model (red cap, crude tier) with a thought bubble, on white.
- s001 renders crisp at 1080p through the round 1 `_upscale_scene()` path.

## New asset: `thumbs_up_hand` (s213): APPROVED
- It is recognisable at a glance, sits in the detailed tier (flat skin fill, a shaded palm side, finger creases, the
  nail highlight), is on-palette, and has a bold silhouette. The car rests on the thumbnail and the composition is
  clear on white, so the "car on your thumbnail" joke works.

## Round 1 fixes verified
- **Zone ramp (2-4):** s097-s099 and s133-s143 are twilight `#1b4f86`. The anglerfish shots (s146-s161) are midnight
  `#0b2447`. The ramp now steps cleanly at s066, s144, s180 and s199.
- **Overlaps and safe area (5-16):** s005, s009, s010, s017, s027, s059, s068, s080, s189 and s212 are all clear.
  s176 ends with the fish at the surface. s241 has 7 gravestones in their zones, and the last one (y=3560) lands
  uncut in the end frame.
- **Label count (17-24):** s015, s131, s143, s156, s186, s210, s225 and s236 all have 2 or fewer word labels.
- **Doug staging and variety (25-27):** Doug now sits on the sofa in s050 and stands on the sand in s051. The s150
  Doug is normal size and alive (swim pose, open eyes), so there is no longer a false death. The reef run is broken
  up by the s037/s038 close-ups and the white s039 "INSULIN WEAPON" card.
- **Optional items:** all were done. s060 Doug is clear of the tank, the s088 sub is by Japan, and the s113 net has
  a mesh.
- **Visual-review items:** s023 and s144 are fixed.

## Per-shot fixes
None required.

### Optional (not blocking)
- **s197/s198 (illustrator):** the ice block is still a flat pale rectangle. A bevel highlight and 2-3 crack lines
  would read more as "ice". This is carried over from the visual review and does not block.

## Routing
- Director: nothing outstanding.
- Graphic designer: nothing outstanding.
- Illustrator: optional ice-block polish only.

**OVERALL VERDICT (round 2): PASS.** Keyframes are art-approved, and the episode can move to `art_approved`.
