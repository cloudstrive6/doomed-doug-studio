# 036-army-ant-swarm: art review (assets)

**Verdict: FAIL.** One asset needs a revision: `ant_feet_chain`. It blocks only s154. The other 32 are approved, and one of them (`army_ant_soldier_head`) I fixed myself.

How I checked: I compared all 7 preview sheets (`assets/previews/036-army-ant-swarm-*.png`) with `channel/art_bible.md` and the brief's section 7 ant rules. I scanned every asset JSON's palette. I re-rendered 19 real-asset keyframes that stress the risky drawings: s013, s024, s036, s045, s065, s066, s071, s081, s085, s098, s100, s127, s154, s166, s167, s173, s195, s203, s207.

Ant palette: all 16 ant drawings use the director's ramp exactly (`#6e2e1c` body, `#5a2a18` gaster, `#a0583a` rim, `#4a1e10` legs, `#d9b25a`/`#b08a3a` soldier heads, `#3a1a0c` jaws). I approve that ramp as the channel's ant palette. On pale forest, mid forest, night, nest dusk, dawn orange and cream they read as mid-tone and stay readable. No ant has a face or eye shine, and nothing on any ant looks military-cartoon.

## Per asset

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `army_ant_carpet` | APPROVE | Reads as a mass, not a brown bar, at 0.5 and on the s195 black silhouette. Soldiers' pale heads break up the top edge. Tiles cleanly (s045, s065, s207). |
| 2 | `army_ant_worker` | APPROVE | Holds up at 2.6 (s013): gaster plates, leg joints, head highlight, single dot eye, sting tip. |
| 3 | `army_ant_soldier` | APPROVE | Sickle jaws read as tools. The jaw gap takes Doug's stick (s085). |
| 4 | `army_ant_soldier_head` | APPROVE (fixed by art director) | The deep top notch plus the long centre line made the head read as a peach or a bottom with hooks (s071 at frame size). I raised the notch from y -232 to -256 (the lobes are at -268), shortened the midline to y -254..-226 and moved the two `#b08a3a` back-edge shading tips to y -252. It now reads as a broad bilobed head with J-hooks. Re-checked in s071 and s081. Note for the illustrator: the sheet `036-army-ant-swarm-ants.png` still shows the old notch, so regenerate it when you next touch the sheet. |
| 5 | `army_ant_soldier_top` | APPROVE | |
| 6 | `army_ant_column_top` | APPROVE | |
| 7 | `army_ant_mill` | APPROVE | Counterclockwise. The bottom stretch reads under Doug (s127). |
| 8 | `army_ant_queen` | APPROVE | Membrane bands read. The silhouette stays clean (s173 colour, sheet silhouette). |
| 9 | `ant_bivouac` | APPROVE | Lumpy, bristling with ants, reads as made of ants. Cap on its right edge reads (s166). Doug behind it reads as "climbed in" (s167). Usage note: the anchor is at the top, so silhouettes need `glow_r: 0` plus a body-centre spray. s152 already does this. |
| 10 | `ant_bivouac_cutaway` | APPROVE | Same outline. Larvae and queen are where the circle and arrows expect them. |
| 11 | `ant_feet_chain` | **REVISE** | See fix 1. |
| 12 | `ant_larva` | APPROVE | |
| 13 | `ant_pupa_cocoon` | APPROVE | |
| 14 | `driver_ant_queen` | APPROVE | |
| 15 | `driver_ant_head_jaws` | APPROVE | Toothed blades are clearly different from the smooth soldier hooks (s203). The teeth are black-and-dark-brown shapes, not wounds. |
| 16 | `ant_living_bridge` | APPROVE | Sag and layers read in s098. |
| 17 | `ocellated_antbird` | APPROVE | Blue eye patch, black throat and ocelli read on cream and navy. Optional polish, not blocking: the tail is a flat single-colour bar and reads a little like a stick. A darker `#4e3a22` underside stripe would help. |
| 18 | `grasshopper` | APPROVE | |
| 19 | `ground_beetle` | APPROVE | It is only used on forest ground (s052). Do not put it on the night `#1b2f4a`: navy on navy. |
| 20 | `butterfly` | APPROVE | Reads at 0.35 on the cap (s045). |
| 21 | `wasp_nest_leaf` | APPROVE | |
| 22 | `seagull` | APPROVE | |
| 23 | `grasshopper_costume` | APPROVE | On Doug (s065), the head, face, cap, thumb and hand are all clear. It is a prop, so Doug's design is not changed. |
| 24 | `grasshopper_costume_flat` | APPROVE | Reads on `#0b0f14` and the cap sits on the head end (s066). The X eyes are death grammar, not a cute face. |
| 25 | `tent_open_empty` | APPROVE | |
| 26 | `naturalist_old` | APPROVE | Crude tier, auto-ink works on navy, no red cap. |
| 27 | `officer_cap` | APPROVE | |
| 28 | `road_worker_lying` | APPROVE | Crude tier, no red cap, calm face. |
| 29 | `researcher_camp_chair` | APPROVE | Faces left, calm (s207). |
| 30 | `athletics_track` | APPROVE | No logos. Inner lane is about rx 404, ry 204. |
| 31 | `sesame_seed` | APPROVE | |
| 32 | `banknote` | APPROVE | No numbers, no portrait, no real currency. |
| 33 | `beanbag_chair` | APPROVE | |

## Fixes

1. **`ant_feet_chain` -> illustrator.** Each of the six legs ends in a flat, rounded tube cap floating in mid-frame. In s154 (scale 1.4 on cream, fully in frame) they read as **cut-off ant legs**, which breaks the "no dismemberment" rule and the 026 cut-piece rule ("any severed-looking end is hidden"). The thick, even `#6e2e1c` cylinders with a `#a0583a` highlight also read as wooden logs or bamboo, not legs. Redraw within the same extents (x -350..350, y -225..225) and keep the claw gripping at about (+250,-33):
   - Hide every free leg base. Run each femur off the drawing into a band of ant bodies along the top and bottom edges of the drawing: dark `#3a160c` mass with partly visible thorax and gaster shapes, `#a0583a` rim, the same texture as the `ant_bivouac` surface. That way every leg visibly belongs to an ant and no end is cut. Doing this through the shotlist (cropping at the frame edge) is not enough, because the whole drawing sits inside the frame.
   - Make the legs read as insect legs: tapered segments (femur about 26 wide, tibia about 18, tarsus about 10), joints drawn as small knuckles rather than tube end-caps, and a few short dark hair ticks along the tibiae.
   - Keep the double hooked claws and the three-layer link structure, which already read well.
   - Re-preview on cream at 1.4 and on `#46523f`.

## Note for the director (composition, not blocking the assets)
- s100: the car and the bus sit on top of `road_worker_lying`, wheels on his body. It is cartoon, but it reads as a person being run over. Consider sizing the pothole and car so the wheels straddle the pothole edges and his body shows between them, as "the traffic drives over them" rather than "runs them over". This is your call at the keyframe review.
