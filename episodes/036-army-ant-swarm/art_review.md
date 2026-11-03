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

---

# Round 2: keyframes (s001-s218 + end slate)

Reviewer: art director, 2026-11-03
Scope: all 219 keyframes on `build/contact/sheet_01..19.png`, checked against `channel/art_bible.md` and style bible 7 (Art Director rules 1-9).
After my direct fixes I re-rendered the full set, so sheets 01-19 are current.

## What holds
- **Two tiers:** ants, birds, props and places carry interior shading. Doug, the scientists, the naturalist and the road workers stay crude. There is no gore anywhere, and every death is cartoon only: 281 ghost on black, 282 the flat costume, 283 X eyes on the logs, 284 still walking the mill, 285 the empty tent, 286 the nest silhouette plus ghost, 287 a small `on_back` on black.
- **Doug:** on-model in every frame, expressions from the fixed set, ink white on the black cards. Caps: the ghost cap plus the cap as cargo or on the ground (s027, s149, s170) follows the "one cap per frame" ghost rule. Capless s166-s168 is the logged exception, and the cap is in frame in s166.
- **Zone colours:** the director's distance ramp holds in every shot: pale front `#dde8cc`, followers and menu mid-greens, the soldiers and road crew `#9db085`, the brown mill floor, night `#1b2f4a`, dusk purple, nest `#46523f`/`#3a4535`, and dawn-orange Africa. The cream diagram cards are consistent.
- **HUD:** the caption bar, `DOUG DEATHS` (280 to 287, one tick per death) and the `DISTANCE TO QUEEN` sign sit in the same place everywhere, inside the safe area. The section header cards (THE FRONT., THE TRAIL., THE NEST., THE BIGGER NEST.) are white with an outline and have no top bar, as the bible requires. Item title cards are red.
- **Reveals and annotations:** silhouette-then-colour works for the soldier, the queen, the living nest and the driver queen. Every item has arrows, "?"/"!", X marks or a warning triangle.
- **Variety:** mostly good. The episode uses maps, a bus scale, tennis-pitch and athletics-track scales, a pie chart, a bar chart, calendars, a stadium, a thumb, a banknote, a cutaway, split cards, the field guide and the hammock callback.

## Fixed directly by the art director (shotlist edited, keyframes re-rendered)
1. **Rule 4 (max 2 labels):** s010 dropped the `SWARM` label, so NEST and 200,000 remain. s011 dropped `SWARM` (NEST and 200 M remain). s069 dropped `WORKER` (SOLDIER and CATCH NOTHING remain). s102 dropped `WITH PLUGS`, since s101 sets up the tall bar one beat earlier (WITHOUT and UP TO 30% LESS remain). s164 dropped `WARMER`, because the thermometers carry it (PUPAE and LARVAE remain).
2. **s105-s107 ant column:** the ants were a straight row at y 626, floating about 90 px above the log tops and crossing Doug's cap brim at eye height. They now walk on the log tops (y 712), go over the cap crown (y 604), along his body line (650/680/700), and back onto the far log. Nothing crosses his face. This is now an art bible rule ("Creatures walking over Doug").

## Verdict: FAIL (5 composition fixes for the director; no asset fixes)

### Fixes (director)
1. **s031: the notes stack is three plain white rectangles** (known). It reads as blank boxes, not decades of notes. Draw each sheet the way s032's page is drawn: white fill, 3 px black outline, and grey `#8a8a8a` width-2 rule lines every 20 px. Offset the three sheets so they read as a stack (x 1172 / 1188 / 1180, each 8-10 px lower than the one above), and give the lower two a `#ece8d6` fill. Keep the appear timings.
2. **s172-s178: the same queen composition five times** (queen at (960,680) scale 1.1-1.2 on the nest green, with the same flanking workers). **Doug is also absent from s173 to s182** except for s174-s175. Doug should be in at least s173, s176 and s178:
   - **s173:** add Doug `stand`, `shock`, facing left, at x 1720, feet on the ground line (scale 0.5), `appear` 0.5, so he reacts to the egg piles. Keep the egg piles clear of him.
   - **s176:** change it to a cream `#f4f1dc` diagram card: the queen side-on at x 760, scale 0.9, the "55,000 TO 66,000 EGGS" label above her gaster, the `1 WEEK` calendar kept at the top left, and Doug `point` at x 1650 aimed at the gaster. Remove the 1.06 zoom, which does not read.
   - **s177:** use a different layout from s176. Put three calendars in a row across the upper middle (x 560 / 960 / 1360, scale 0.6, each labelled AGAIN, which is one repeated label in a single row), with the queen small (0.6) centred below them. Keep it to two distinct label texts.
   - **s178:** add Doug `point`, `hopeful`, facing left, at x 1700 on the ground line. Put a red curved arrow from his hand to the blue paint dot, replacing the current top arrow so there is one arrow, not two. Keep the 4.5 YEARS wordart.
3. **s179 to s180: near-duplicate** (three small queens in the same places). In s180, add `camera: {move: "zoom_in", x: 1500, y: 700, zoom: 1.4}` so the one queen that makes it fills the frame, and move NEW NEST to about (1500, 470) so it stays in the zoomed frame. In s179, add Doug `stand`, `flat`, facing left, at x 1780 on the ground line. That gives Doug a beat in the run without crowding s180.
4. **s119 to s120: near-duplicate** (the same track, ellipse and ABOUT 365 M label; only Doug's pose changes). For "almost one full lap", replace the closed red ellipse in s120 with a red `curve` that follows the same oval but stops about 60 px short of where it starts, at the finish line. Put a red "!" in the gap, and change the label to `ALMOST 1 LAP` at the same spot.
5. **s062 to s063: near-duplicate** (the same Doug and carpet; only the GOES WELL wordart is added). Add `camera: {move: "zoom_in", x: 1100, y: 640, zoom: 1.3}` to s063 so "for a while it goes well" plays on Doug's face. The wordart at (640, 330) stays in frame.

### Not blocking (director's call)
- **s008, s020:** the swarm front is a flat brown slab or blob with no ant texture, while the same swarm in s010-s012 has ant columns. A `#4a1e10` spray (density about 0.25) plus a row of `army_ant_carpet` at about 0.3 along the leading edge would keep it in the detailed tier.
- **Death cards vary:** the big "DOUG DEATHS: N" text is at the top in s026, absent in s066 and s191, and at the bottom in s169. Pick one (top, as in s026) or drop it, since the counter is already on screen.
- **s135:** the tiny queen silhouette on cream has no glow (`glow_r` 0). That is fine as an icon, but it is not a reveal (her reveal is s139 and then s172).
- **s217:** the "DOUG DEATHS: 287" wordart repeats s216's big text. "A SHORT WALK" alone would be cleaner.
- **`army_ant_soldier_head` close-ups (s071, s081):** these read correctly now. The illustrator still needs to regenerate the ants preview sheet (round 1 note).
