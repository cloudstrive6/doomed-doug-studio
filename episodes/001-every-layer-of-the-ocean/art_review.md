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
