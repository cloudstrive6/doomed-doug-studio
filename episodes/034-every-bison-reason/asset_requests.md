# 034-every-bison-reason: asset requests (director)

House style: detailed tier for creatures, places and props (dark outlines 4-6, flat fills, interior shading with `spray` and darker backs / lighter bellies), crude tier (Doug's line, `auto_ink`) for humans. Everything faces **right** unless noted. Sizes are local units at scale 1. **The shotlist is laid out against these anchors, extents and key points** (a stand-in layout pass was rendered and checked against them), so please keep them, or tell me what moved and I will re-place.

**Status: all 17 drawn (illustrator, 2026-11-01).** Preview sheet `assets/previews/034-every-bison-reason-assets.png`; context sheet (white, snow, flipped, dusk, silhouette, night, thumbnail size) `assets/previews/034-every-bison-reason-context.png`. Moved key points are flagged in bold under each item.

Listed in priority order: the bison family first (on screen in about 150 of 208 shots), then the other animals, then props and places.

## Rules from the CD and the brief (decisions.md 2026-11-01, section 5, and brief section 7) that apply to every drawing
- **It must read as an American bison at feed size, never a cow, a buffalo or a bear.** That means the high shoulder hump, the shaggy dark-brown cape over the head, shoulders and front legs, the beard, the low-slung huge head, the short upward-curving horns, the slimmer, paler, shorter-haired hindquarters, and the short tufted tail. Use the hide palette `#4a2f1e` (cape) / `#6b4a2f` (body) / `#8a6a4a` (hindquarters), with horns `#2a2a2a` tipped grey and dark hooves. It is **not** the `steppe_bison` (that one has long wide horns): modern horns are short and curve *up*.
- **No horn contact with Doug anywhere** (decision 5a). No drawing shows a horn touching, hooking or lifting anything. The charging pose has the head low and the horns forward, with nothing on them.
- **The calf is distant and plain** (decision 5c): small, orange-red, a dot eye with no shine, no big eyes, no smile, no close-up version. It is only ever used at scale 0.28-0.35, or as a plain black silhouette.
- **Wolves never kill anything on screen** (decision 5f). The existing `grey_wolf` is used; no new wolf attack poses.
- **No blood, no wounds, no injured bodies, no carcasses.** The cutaway shows muscle in cartoon pink `#e79aa0` and bones in cream, never realistic.
- **No real people in danger.** The car in The Jam is drawn by the shotlist with the existing `small_car` (glazed windows, nobody inside).

## Episode palette (director's proposal for the art director: a Yellowstone calendar ramp, one month per item, light winter to dusk rut)
| Item | Sky | Ground / extra |
|---|---|---|
| Wolves (JAN) | `#cfe9ff`, mountains `#b9cde0` with `#f7fbff` snow caps | snow `#f7fbff` |
| Snowplow (FEB) | `#dbe6ee` | snow `#f2f6fa`; Madison River `#3a9ad9` |
| Hump (MAR) | overcast `#c9d3dc` | slush `#d6d9d2`, bare mud patches `#8a7a5a` |
| Calf (MAY) | `#8fd3ff`, hills `#6fb24f` | grass `#7cc25a` (green: wordart uses the white/yellow override, and sits in the sky); river `#3a9ad9`; sober grey card `#8a8f94` / `#7a7f84` |
| Speed (JUN) | `#8fd3ff`, hills `#8cb84f` | grass `#9cc25a` |
| Record (JUL) | `#cfe9ff`, hills `#b9c8d6` | geyser-basin sinter `#ece4d0`, boardwalk `#a0522d`; sober card `#15181a` with white text, no Doug, no counter |
| Jam (JUL) | `#8fd3ff`, hills `#a8b06a` | verge `#c9c46a`, road `#6a6a6a` with `#ffe24a` dashes |
| Wallow (AUG) | `#f6dcae`, hills `#e2b86a` | dry dirt `#d9b45a`, wallow `#a07a4a` |
| Rut (AUG) | dusk `#f2a24a` over `#e88a4a`, hills `#c97a4a` | `#b8913a`; honesty card `#4a4f5e`; end slate `#2a2030` |
| Death beats | `#0b0f14` | `#141a14` (cap on the ground, ghost Doug) |
| Diagram cards | cream `#f4f1dc` | |

Bison fills must read on both snow (white) and dusk orange, so keep the mid-tone browns above, not near-black. The silhouettes (s002, s003, s169, s204-s205) are made by the engine (`silhouette: true`), so keep the outline clean: separated legs, a clear hump, horns and beard.

HUD (all drawn by the shotlist, no asset needed): `DOUG DEATHS: N` at (1590,162) and, under it, the library `calendar` at 0.17 at (1530,240) plus a size-30 month label at (1610,240) (JAN to AUG, then a red RUT after s195).

Reused from the library (no request): `calendar`, `grey_wolf`, `grey_wolf_sitting`, `grizzly_bear`, `steppe_bison` (005 callback only, s047-s048, and the 012 tar-pit memory s089), `doug_cap`, `dust_plume`, `small_car`, `field_guide_open` (AMERICAN BISON page drawn as overlays: name, MAYBE, NO stamps, the PLANT EATER sticky note), `referee_shirt`, `whistle`, `snow_shovel`, `selfie_stick_phone`, `phone`, `wait_stopwatch` (as a plain stopwatch prop), `clipboard`, `chalkboard`, `balance_scale`, `baby_grand_piano`, `platform_scale`, `suitcase`, `bathroom_scale`, `tennis_court_side`, `finish_banner`, `speedometer`, `clock`, `sofa`, `rug`, `usa_map`, `american_football`, `soccer_ball`, `shipping_crate`, `scientist`, `binoculars`, `stew_bowl`, `grass_tuft`, `paw_print_icon` (tracks in the snow), `narrator_hand_pencil`, `pencil`, `gravestone`, `question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`.

---

## The bison family

### `american_bison`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. hooves on y=0, hump top (+70,-421); **front horn tip (+285,-315)** (cap hang still fine at (+290,-300-18/scale): it sits on the upper horn); eye (+277,-216); muzzle front (+340,-124), extents x -330..+346; beard to about y -78.
**The workhorse bull (69 shots).** Adult American bison bull standing in side view, calm and alert, head held low (the natural carriage: the top of the head sits below the hump).
- Look: see the rules above. The hump is the highest point. A thick shaggy cape covers the head, the neck, the shoulders and the front legs down to the knees ("chaps"). There is a long chin beard, and a dark curly forehead mop between the horns. The small dark eye has a lid line and sits low on the side of the head. The horns are short and black and curve up and slightly in. The hindquarters are noticeably slimmer, smoother and lighter. The tail is short with a tuft.
- **Anchor bottom-centre (hooves on y=0). Extents about x -310..+330, y -420..0.** Key points used by the shotlist: **hump top about (+60,-420); horn tip (front horn) at (+290,-300)** (the closing shot hangs Doug's cap on it at (+290,-300-18/scale)); eye about (+275,-240); muzzle about (+320,-150); beard down to about y -110.
- Used flipped (facing left) in about half its shots, at scales 0.2-1.0, and as an engine silhouette (s002, s003, s169, s204-s205). So the outline must be clean, with the legs separated.
- Shots: s002-s003, s008-s009, s012, s014, s016-s019, s023-s024, s031, s034-s035, s037, s051-s052, s054-s056, s073, s076-s077, s082, s084-s086, s088, s100, s102, s109, s115, s130, s133-s139, s145, s147, s149-s152, s154-s155, s162, s169, s171-s173, s176-s184, s187, s193, s196-s197, s204-s205.

### `american_bison_grazing`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. muzzle on the grass at (+300,0), hump top (+45,-406), half-lidded eye; extents x -330..+338, y -406..0.
Same bull, **head down to the grass, eating**: the muzzle is on the ground at about (+300,-10), the hump is even more prominent at about (+40,-400), and the eye is half-closed and placid. This is the "sofa with a beard" look (The Speed), the least athletic animal in the park. Anchor and extents the same as `american_bison` (x -310..+330, y -410..0). Used flipped too.
- Shots: s010, s037-s038, s069-s070, s095-s096, s104-s108, s112-s113, s116-s117, s128-s129, s132-s133, s138, s191, s194.

### `american_bison_snowplow`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. muzzle (+299,-23); snow spray kept in x +300..+342, y -50..-140; area round (+330,-90) has only small flecks. Extents x -330..+342.
**The winter snow-swing (The Snowplow, The Hump).** The bull with its head swung low and to the side, sweeping snow. The head is down near the ground at the front with the muzzle at about (+300,-30). Thick white snow is caked on the forehead mop and the beard (white `#ffffff` clumps with pale-blue `#cfe6f5` shading), a few frosted clumps sit on the hump, and a small arc of snow spray leaves the face toward the front (keep the spray inside x +260..+340). Calm, busy face: half-lidded eye, not angry.
- Anchor bottom-centre, x -310..+340, y -410..0. The shotlist adds its own bigger snow sprays at about (+330,-90) x scale, so leave that area open.
- Shots: s027-s030, s038, s041-s044, s046, s050, s065-s068.

### `american_bison_charging`
**ROUND 2 DONE (illustrator 2026-11-01, art_review fix 1)**: `assets/previews/034-every-bison-reason-assets-r2.png`, checks `assets/previews/034-every-bison-reason-charging-r2-checks.png` (1.0, 0.32, red-glow silhouette, flipped rotate -12, 0.32 silhouette rotated). Both front legs now show below the head: near leg reaching, hoof x +264..+304, y -36..-2; far leg folded under the chest, x +120..+184, y -126..-69. Head squashed vertically to clear the legs, horn tip unchanged at (+297,-202). **Moved**: eye (+275,-150) (was -117), muzzle (+310,-98) (was -38), head bottom about -80 (was -7); beard is now a short tuft from the throat. Extents x -346..+325, y -394..0 (inside +340).
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. horn tip (+297,-201), lowest hoof y=0; tail up; dust is `spray` only (invisible in silhouette). No speed lines (keeps x -344..+323), add them in the shotlist if wanted.
**Galloping charge**, side view: the body stretched out, the front legs reaching forward, the hind legs pushing back, **the head very low with the horns forward and nothing on them**, the tail up (a real charge sign), and the cape and beard swept back. A couple of dust puffs at the hind hooves are fine. Determined eye, no teeth.
- Anchor bottom-centre (lowest hoof on y=0), x -330..+340, y -380..0; horn tip about (+300,-200).
- Used flipped, rotated -12 for the fence jump (s101), and at 0.32 crossing a tennis court (s098-s099).
- Shots: s097-s099, s101, s110, s146, s199-s200.

### `american_bison_cow`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. extents x -280..+268, y -323..0 (hump a bit lower than requested -360, on purpose: reads clearly smaller than the bull).
Adult **cow**, side view: the same build but clearly smaller and slimmer, with a lower hump, a thinner neck cape, a shorter beard, and **thinner horns that curve up more sharply** (both sexes have horns: s054, "BOTH HAVE THEM", so her horns must be clearly visible). Alert, protective eye.
- Anchor bottom-centre, x -270..+280, y -360..0. She is used very large (scale 1.45 in s076; **2.3 in s091**, where she fills the frame and her lower body runs off the bottom), so keep the hide texture and shading clean at large sizes.
- Shots: s036, s054-s056, s073, s075-s079, s082-s084, s088, s091, s094, s137, s151-s152, s154, s181-s183.

### `bison_calf`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. extents x -108..+126, y -166..0. Reads at 0.3 and as a silhouette. Scale preview: `assets/previews/034-every-bison-reason-assets-small.png`.
**Newborn "red dog" calf, distant and plain** (decision 5c): small, with a **bright orange-red `#c8642a` coat** (shade `#a84e1e`), no hump yet, no horns, short legs, a stubby muzzle, small ears, and a dot eye with no highlight. **No big eyes, no smile, no cute features.** It should read simply as "small orange bison" at 0.3.
- Anchor bottom-centre, x -110..+120, y -170..0. Used at 0.28-0.35 only, and as a black silhouette on the grey card (s085-s086) and on the scale (s080).
- Shots: s073, s076-s080, s082-s086, s090-s091.

### `american_bison_face`
**ROUND 2 DONE (illustrator 2026-11-01, art_review fixes 2-3)**: `assets/previews/034-every-bison-reason-assets-r2.png`, in-context `assets/previews/034-every-bison-reason-face-r2-context.png`. Mouth is now a short flat line dipping slightly at the ends (no smile), eyes unchanged. Hump and chest extended to **y +340** with shading and texture; nothing above y +240 moved. Extents x -232..+232, y -260..+340 (bottom edge off-frame at s039/s049/s053).
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. horn tips at (+-172,-178), clear of the mop; extents x -230..+230, y -250..+240.
**Front view of the bull's head and hump** (close-ups): the broad shaggy head facing the camera, the dark curly forehead mop, the two short horns curving up and in at about (±170,-170), small eyes set wide and half-lidded (flat, calm, faintly unimpressed, not angry), the nostrils, the beard hanging to the bottom, and the hump rising behind the head.
- **Anchor centre; extents x -230..+230, y -260..+240.** Used at 1.4-1.6 (s039-s040 "does not care about you", s049 "less forgiving", s053 horns with red arrows from (700,420) and (1700,420)). Keep the horns clearly separated from the mop.
- Shots: s039-s040, s049, s053.

### `american_bison_wallowing`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. ground under the back y=0, dirt patch to y +4; extents x -310..+310, y -281..+4. Head near-upright on its cheek, eye open, horn up, legs kicking.
**A bull rolling on its back in a dirt wallow**: the body twisted onto its back and side, hooves in the air, the head turned with one horn and the beard visible, a bare dirt patch under it (`#a07a4a`), and tan dust puffs (`#e2d3b0` / `#c8b58a`) around the shoulders. It reads as a big animal throwing itself on the ground, not as a dead or hurt one: legs kicking, eye open.
- Anchor bottom-centre (the ground under the back), x -300..+300, y -300..0. Used rotated +8 for "rolls violently" (s163), and on a giant rug in s167.
- Shots: s157, s159-s161, s163, s167, s170.

### `american_bison_bellowing`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. **mouth at (+322,-305)**; extents x -330..+350, y -429..0.
The bull standing, **head raised and stretched forward, mouth open** (dark `#7a0d0d` mouth, no teeth showing, no tongue), bellowing; the beard swings forward. **The mouth is at about (+320,-300)**: the shotlist draws sound-ring arcs from there.
- Anchor bottom-centre, x -310..+340, y -440..0. Used flipped and small (0.35) for the far rival (s176).
- Shots: s164-s165, s176, s183.

### `bison_bulls_locked`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. forehead contact (0,-200), hooves on y=0; extents x -665..+665 (about 45 wider each side than asked), y -427..0. At 0.8 that is 1064 px wide.
**Two bulls head to head, locked horns**: one facing right and one facing left, their foreheads pressed together at the centre, the rear legs braced, a dust puff at the front hooves. The horns overlap but nothing is hooked or bleeding. It must read as shoving, not goring.
- Anchor bottom-centre, with **the forehead contact point at about (0,-200)**; extents x -620..+620, y -420..0. Used at 0.8 with `dust_plume` behind it.
- Shots: s185-s186.

### `bison_hump_cutaway`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. same pose/anchor as `american_bison`; (0,-330) lands on pink muscle, (+100,-330) on a long spine; tallest spine at x +61 (top -402); backbone y -270.
**Diagram of the hump**: the `american_bison` outline (same pose, same anchor and extents, x -310..+330, y -420..0, so it swaps in place in s031 to s032). Over the shoulders a cutaway window shows the **tall spines of the backbone** (a row of cream `#f4ecd2` bones rising from a horizontal backbone line at about y -260 up into the hump, the tallest at the hump top), wrapped in **cartoon-pink `#e79aa0` muscle bands** (`#c97a80` stripes) running up to the neck and head. The rest of the body is in normal colours. Clean and diagrammatic, never realistic.
- The labels are drawn by the shotlist: MUSCLE with an arrow ending at about (+0,-330) and LONG BONES with an arrow ending at about (+100,-330).
- Shots: s032-s033.

### `bison_head_icon`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. x -70..+70, y -56..+56; no people.
**Small flat bison head icon**, side view facing right: a dark-brown `#4a2f1e` shaggy head with the hump line behind it, a beard, one short black horn curving up, a small eye and a thick outline. It must read at 0.45 (tally marks, a calendar grid, the "7 of them" row) and at 1.2-1.4 (the BUTT / HOOK icons in s059-s061: **no people in them**, decision 5b).
- Anchor centre, about 140x110 (x -70..+70, y -55..+55).
- Shots: s059-s061, s063, s122-s123, s132, s144, s148-s149, s190, s207.

## Other animals and costume

### `elk_bull`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. extents x -190..+234, y -486..0; 6 points a side, cream rump patch, chocolate mane.
Yellowstone **bull elk** standing in side view: tan-brown body `#a8805a` with a darker chocolate neck mane `#5a3a24`, a pale cream rump patch, long slim legs, and **large branching antlers** (6 points a side, pale brown) clearly bigger than the head. Alert. It must not look like the `deer`.
- Anchor bottom-centre, x -200..+230, y -480..0. Used flipped (facing the wolves), as a silhouette in the s002 line-up (the bear, wolf, elk and bison row), and at 0.42-0.55.
- Shots: s002, s006-s007, s011-s012.

### `wolf_costume`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. built on the `cat_costume` fit (same rig points): ears at x -124..-56, y -338..-232 left of the cap dome; tail hangs to (-186,+122).
**Doug's homemade grey wolf onesie** (worn prop, like `cat_costume`): a grey `#8d9096` suit with a darker `#5f6368` saddle across the shoulders, a pale grey chest panel, a front zipper with a pull tab, sleeves ending in grey mitten paws at the hands (±70,-12), leg sleeves to paw boots at the feet, a **bushy grey tail with a dark tip** out of the back at hip height, and a hood bunched round the face with **two upright pointed wolf ears at the back of the head (left of the cap dome)**. **The face and the red cap stay fully visible. There is no wolf snout or mascot face** (brief: the costume stays deadpan). "The red cap sits on top of the wolf ears": the ears poke up behind the cap.
- Anchor = Doug's hips; it is listed after Doug at the same x/y/scale in the `stand` pose (scales 0.42 and 0.95).
- Shots: s020-s024.

### `dog_rolling`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. extents x -172..+170, y -162..0.
A **large dog rolling happily on its back** (for "picture a dog rolling on the rug"): the same tan and black German-shepherd look as `large_dog`, on its back with its paws in the air and the head turned to the side, tongue in. Anchor bottom-centre (its back on y=0), x -170..+170, y -160..0. Placed on `rug` at 2.0.
- Shot: s166.

## Places and props

### `geyser_steam`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. extents x -200..+210, y -620..0 (plume top billow rises about 20 above -600).
**A steaming thermal vent / geyser basin feature**: a low pale sinter mound (`#e8e4da`, with grey-white crust lines and a little blue-green `#6fb7a8` pool rim at the top), and a tall soft white **steam plume** rising from it (white billows shaded pale grey-blue `#d6e2ec`, drifting slightly right, with soft edges). No eruption jet, just steam.
- Anchor bottom-centre (the mound base on y=0), x -200..+200, y -600..0. Used at 0.35-0.8 behind small bison.
- Shots: s037, s116, s120.

### `forklift`
**DONE (illustrator 2026-11-01)**: `assets/previews/034-every-bison-reason-assets.png`. fork tips at (+330,-44..-32), mast top y -330; empty cab.
A simple **yellow warehouse forklift** in side view facing right: a yellow `#f2c12e` body, a black overhead guard, a grey mast at the front, and **two forks sticking out forward at about y -40 with their tips at x +330**, plus black tyres. Nobody in the seat (empty cab).
- Anchor bottom-centre, x -200..+330, y -330..0. The shotlist flips a `shipping_crate` into the air above the fork tips.
- Shot: s063.

---

## Built by the shotlist (no asset needed, listed so you know they exist)
The BUTT / HOOK / TOSS boxes, the 5x5 injury grid, the tennis-court and finish-line layouts, the high-jump bar, the YIELD sign (a red-white triangle with `bison_head_icon` inside), the phone selfie frame, the boardwalk and the stick-head crowd, the paycheck calendar grid, the pie chart, the sober text cards, the tar pit in the 012 memory, the river crossings, the field-guide overlays (AMERICAN BISON, MAYBE in orange then rubbed out at s093, up to 7 red NO stamps at 3 per row with an 80-unit step, and the yellow PLANT EATER sticky note at local (-140,-5) on the left page, clear of the coffee ring), and the big RUT stamp on the torn calendar (s195).
