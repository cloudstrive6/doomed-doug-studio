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
