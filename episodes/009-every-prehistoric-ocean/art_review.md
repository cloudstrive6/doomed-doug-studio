# Art review: 009 One Night in Every Prehistoric Ocean, round 1 (assets)

Reviewer: art director, 2026-10-08. Scope: the 45 new library assets in `asset_requests.md`. This round does not review keyframes.

I checked them against `channel/art_bible.md` (two-tier rendering, palette, no gore), style bible section 7 (Art Director rules 1-9), and the
director's sizes, anchors and named local points. Sources:
- every `assets/previews/009-*` sheet
- my own inspection renders of each asset at scale 1, on white, on Miocene navy `#0a1630`, and as `silhouette: true` on `#112f4f`, with the measured local bbox and anchor
- side-by-side renders against the library look-alikes (`megalodon` vs `great_white_shark`, `livyatan` vs `sperm_whale`, `time_machine_closed` vs `time_machine`)
- an automated check for `spray` discs that leak outside their shape
- 15 draft keyframes (s034, s052, s100, s109, s116, s124, s126, s129, s132, s189, s198, s228, s230, s253, s254) to see the riskier assets in their real shots

## Verdict: FAIL (1 asset rejected, 44 approved)

## Rejected (route to the illustrator)

1. **`helicoprion`** (B SIL, 7 shots, the item's "where the spiral went" payoff). Three problems:
   (a) The whorl does not read as a spiral. The lower-jaw shape (element 41) and its belly band (42) are drawn *after* the whorl (15-40), so they cover the bottom two thirds of it. At phone size s126 ("like a circular saw") shows only a fringe of cream spikes.
   (b) The head is deeper than the body (top y -156, bottom +144 at x 200-300). The fish reads as a tadpole or sperm whale, which is especially clear in the s109 silhouette. The asset is also 376 tall against the director's 300 box.
   (c) The eye (r25, pupil r11, high thin brow) plus the huge gape makes a goofy "shocked" face. That breaks the brief's "predators look dangerous, no cute faces" rule.
   **Exact fixes** (keep the anchor, the whorl centre (+280,+80) and the toothless upper lip through (+285,-60)):
   1. Move elements 41 and 42 (lower jaw and its pale band) so they come **before** element 15. The whorl then sits on top of the jaw. Raise the whorl disc (15) to r 56 and scale the tooth ring (16-29) and spiral (30-40) by 1.15 about (280,80), so the full spiral of about 3 turns is visible, with the largest teeth at the upper right.
   2. Flatten the head. In the body outline (elements 4 and 14) change (386,-124) to (386,-100), (310,-150) to (310,-118), (200,-156) to (200,-128) and (90,-146) to (90,-124). Lower the back band (5) by the same amounts. Move the first dorsal (1, 2) down by 28. Move spray 7 to y -95. Target height is 300 or less (about y -180..+150 including the fin).
   3. Make the eye match our other predators: r 16, pupil r 8 at (+3,+2) from the eye centre, eye centre at (310,-88). Use a heavy brow line of width 6 from (284,-104) to (334,-98) that overlaps the top of the eye (as on `xiphactinus` and `pliosaurus`). Keep the brow above the lip at y -60.
   4. Re-check the silhouette. It must show a pointed snout and a jaw notch, not a round whale head.

## Approved with non-blocking cleanup (illustrator, next pass; these do not hold the stage)
2. **Spray leaking outside shapes.** These read as dust specks on sky or navy. Pull each spray centre inward or shrink `r` until the disc stays inside its fill:
   - `skateboard` #9 (-60,-50) r20, a smudge above the deck
   - `computer_keyboard` #2 (-150,-40) r40, visible as grey dust above the top-left edge on navy
   - `crt_tv` #14 (-200,-140) r50, above the top-left corner
   - `pickup_truck` #13 (120,-250) r40, above the roof
   - `xiphactinus_fossil` #5 (-100,130) r45, below the slab
   - `livyatan_tooth` #4 (150,10) r40
   - `basilosaurus_leg` #12 (110,-60) r50, visible under the body patch in s253
   - `dorset_cliff` #10/#11 can stay, because they read as crumbling dust

   The sparkles on `time_machine_closed` are intentional and match `time_machine`.
3. **`pickup_truck`**: the wheel bottoms reach y +9, not 0. Raise the wheels and tyres by 9 so the truck doesn't sink into the ground line.
4. **`basilosaurus_leg`**: the rounded body patch reads a little like a loaf. If there is time, give the patch flatter top/bottom edges and extend it to the full x -185..+185 width so it reads as a section of the long body. The leg itself (thigh, knee, ankle, three toes) reads clearly.

## For the director (composition, not assets)
5. **s253**: the `KNEE` arrow lands on the body patch and the `ANKLE` arrow lands on the knee. In the asset the knee is at local (-110,+25), the ankle at (-90,+108) and the toes at (+42,+112..+144). Re-aim the arrows (x scale, plus the asset's x/y).

## Per-asset verdicts
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `anomalocaris` | APPROVED | Predatory, not a toy. Spined curled arms, stalked eyes and a tail fan all read in the silhouette. Salmon reads on navy. |
| 2 | `skateboard` | APPROVED | Bottom-centre anchor, wheels on y=0. Cleanup 2. |
| 3 | `snorkel` | APPROVED | Matches `snorkel_gear` (blue J, yellow tip, black mouthpiece). Clean J silhouette. |
| 4 | `endoceras` | APPROVED | Long tapering banded cone, tentacles to the right. Clean silhouette. |
| 5 | `endoceras_shell` | APPROVED | Faded, chipped, flat bottom at y +100, dark hollow opening centred about (+434,+5). Reads in s052. |
| 6 | `nautilus` | APPROVED | Tiger stripes, hood, tentacles. Not a predator, so the softer face is fine. |
| 7 | `pickup_truck` | APPROVED | Dark blue crew cab with a flat open bed. Cleanup 2 and 3. |
| 8 | `jaekelopterus` | APPROVED | Dark glossy red-brown, kidney eyes, paddles, telson, toothed claws. Menacing top view with a clean silhouette. |
| 9 | `jaekelopterus_claw` | APPROVED | Stone-coloured toothed pincer, broken lower tip. |
| 10 | `computer_keyboard` | APPROVED | Width matches the claw. Cleanup 2. |
| 11 | `arthropleura` | APPROVED | Legs touch y about +80. Dark plates with pale edges. |
| 12 | `japanese_spider_crab` | APPROVED | Mostly legs, leg tips at the bottom corners, white spots. |
| 13 | `garden_spider` | APPROVED | Reads as a spider icon at small size. |
| 14 | `lobster` | APPROVED | Dark red-brown, claws forward, tail fan. |
| 15 | `dunkleosteus_old` | APPROVED | Same armoured head on a long faded eel body. Reads as "old textbook" next to `dunkleosteus` (s100). |
| 16 | `helicoprion_whorl` | APPROVED | Three-turn spiral, largest teeth at the outer upper right, grey stone disc. |
| 17 | `helicoprion` | **REJECTED** | See fix 1. |
| 18 | `helicoprion_guess_nose` | APPROVED | Sepia old-book look, whorl curls up and back from the snout. Transparent background. |
| 19 | `helicoprion_guess_tail` | APPROVED | Same fish, whorl replaces the tail. |
| 20 | `helicoprion_guess_fin` | APPROVED | Same fish, whorl stands on the dorsal. The trio is clearly a set (s132). |
| 21 | `ratfish` | APPROVED | Mid-tone, green eye, tooth plates, wing pectorals, rat tail. Reads on `#0a1630`. |
| 22 | `cymbospondylus` | APPROVED | Slim with a long toothy snout, clearly not our chunky `ichthyosaur`. Silhouette OK. |
| 23 | `cymbospondylus_skull` | APPROVED | Sclerotic ring, long toothy snout, cream bone. |
| 24 | `pliosaurus` | APPROVED | Big croc head, white teeth on a dark red mouth, angry eye. The neck seam is a little hard but fits the armoured look. |
| 25 | `pliosaur_skull` | APPROVED | Large conical teeth, eye socket. Fits the `dorset_cliff` hollow. |
| 26 | `crt_tv` | APPROVED | Screen measured at centre (-9,-16), 342x264, empty apart from a faint static glow. Cleanup 2. |
| 27 | `dorset_cliff` | APPROVED | Grey/cream bands, cracks, loose rocks. Hollow measured at about x -180..+186, y -178..-28 (centre about (0,-103)), and the skull fits. |
| 28 | `xiphactinus` | APPROVED | Bulldog underbite with fangs, steel back, silver sides. Not cute. Silhouette shows the fangs. |
| 29 | `xiphactinus_fossil` | APPROVED | Gillicus skeleton inside the ribcage at (0,0). Cleanup 2. |
| 30 | `gillicus` | APPROVED | Slim silvery prey fish with a deep head and forked tail. |
| 31 | `interior_seaway_map` | APPROVED | Matches the `world_map` palette and frame. The seaway runs N-S, Kansas at (+20,0) is in the seaway, and the white corner is deliberate Greenland ice. |
| 32 | `tylosaurus` | APPROVED | Pointed snout, teeth, four paddles, downturned fluke, angry eye. Silhouette OK. |
| 33 | `tylosaurus_fossil` | APPROVED | Plesiosaur skeleton (contrasting tan) inside the ribcage at (0,0). |
| 34 | `tylosaurus_mouth` | APPROVED | Symmetric. Throat at (0,-180), and the s230 arrow lands on it. Pterygoid rows read. Cartoon reds, no gore. |
| 35 | `plesiosaur` | APPROVED | Long neck, small head, four flippers, olive-teal. |
| 36 | `basilosaurus` | APPROVED | Very long eel-whale, cheek teeth. Tiny hind legs at (-226..-168, +50..+99) stay visible in the silhouette. Mid-tone on navy. |
| 37 | `basilosaurus_leg` | APPROVED | Knee/ankle/toes clear. Cleanup 2 and 4, director note 5. |
| 38 | `dorudon` | APPROVED | Small toothy early whale with an angry eye. |
| 39 | `livyatan` | APPROVED | Boxy brown head with big interlocking teeth in both jaws. Clearly different from `sperm_whale` (grey, scars, peg teeth). Mid-tone on navy. |
| 40 | `livyatan_tooth` | APPROVED | Banana curve, cream enamel, darker root. Cleanup 2. |
| 41 | `ruler` | APPROVED | Yellow, 0-30 cm, legible ticks. |
| 42 | `megalodon_tooth` | APPROVED | Serrated, dark grey-blue enamel, tan root band. Reads on near-black navy and when rotated. |
| 43 | `megalodon` | APPROVED | Longer and slimmer than `great_white_shark`, with bigger red-mouth teeth and a tall dorsal. Boss-worthy and mid-tone on navy. |
| 44 | `hand_outline` | APPROVED | Traced hand, fingers up, white inside, so it reads on dark too. |
| 45 | `time_machine_closed` | APPROVED | Identical footprint, roof at y -640 and TIME sign as `time_machine`, with the door shut. The tooth at (+63,-326) and the cap on the roof both land correctly. |

## Rejected assets
- `helicoprion`
