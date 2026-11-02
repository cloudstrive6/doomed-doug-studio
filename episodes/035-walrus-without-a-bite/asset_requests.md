# 035-walrus-without-a-bite: asset requests (director)

House style: detailed tier for creatures, places and props (dark outlines 4-6, flat fills, interior shading with `spray`, darker backs / lighter bellies), crude tier (Doug's line, `auto_ink`) for humans. Everything faces **right** unless noted. Sizes are local units at scale 1. **The shotlist was laid out against the anchors, extents and key points below** (a stand-in layout pass was rendered with boxes of exactly these extents and checked on contact sheets), so please keep them, or tell me what moved and I will re-place.

22 new drawings, in priority order: the walrus family first (on screen in about 190 of 217 shots), then props and icons.

## Rules from the CD (decisions.md 2026-11-02, section 3) that apply to every drawing
- **Walrus design (3e):** heavy, wrinkled, scarred, small eyes, **no smile, no gentleman-moustache gag** (kid-appeal risk is high for this animal). It must read as a walrus at feed size and never as a seal, a sea lion or a cartoon mascot. Defining features: huge blubbery body with deep skin folds, two long ivory tusks, a broad square whisker pad of stiff pale bristles, tiny eyes set high and wide, no external ears, front flippers that can prop the chest up, rear flippers that fold forward.
- **Walrus palette (director proposal for the art director):** body cinnamon-brown `#b07a5e`, back and folds `#8a5a44`, belly and lighter patches `#c99a80`, scars and wrinkle lines `#d9b8a0` (thin, pale, never red), tusks ivory `#efe6d0` with a `#6a5a4a` outline, whiskers `#e8dcc0`, eyes small and dark. Mid-tone on purpose: it has to read on ice white `#f7fbff`, sea `#3a9ad9`, dusk orange `#e88a4a`, grey gravel `#8c8a84` / `#6e6a64` and cream `#f4f1dc`. No pink-cute tones.
- **Calves (3e):** distant and plain. Only in `walrus_cow_calf` (small, dot eye, no shine, no tusks, no smile). No calf close-up anywhere.
- **No bites, no blood, no wounds, no carcasses (3b-3d, 3f).** No tusk touches anything soft. No seal is ever shown being eaten. Grease stains are grey (drawn by the shotlist as grey `spray`, so leave the shoulders plain).
- **Silhouettes:** `walrus_bull`, `walrus_cow`, `walrus_head_rising`, `walrus_swimming` and `walrus_bull_rearing` are used with `silhouette: true` (the engine fills them black, some with a red rim). Keep their outlines clean: tusks separate from the body and clearly visible, flippers readable.

## Episode palette (director proposal: a head-count ramp, light to dark as the walrus count grows)
| Band / item | Sky | Ground / water |
|---|---|---|
| ONE (Seal Eater, Tusks) | `#cfe9ff` (Tusks `#dbe6ee`) | sea `#3a9ad9`, floe `#f7fbff` / face `#bcd8ec` / edge `#9fb8cc` |
| ONE (Suction, underwater on the shelf) | water `#3a9ad9` | mud floor `#8a7a5a`, speckle `#6b5b4b` |
| TWO (Boat, Fight) | overcast `#c9d3dc` | sea `#3a9ad9`, gravel `#9a9286` |
| HUNDREDS (Sleep) | dusk `#f2a24a` over `#e88a4a` | sea `#3a9ad9`, ice `#f7fbff` |
| HUNDREDS (Polar Bear) | late dusk `#8a6a8a` over `#e59a5e` | dusk snow `#e9e0e6`, ridge `#ddd2dc` |
| 35,000 (Haulout) | grey `#b9c0c8` | gravel `#8c8a84` |
| 35,000 boss (Stampede) | `#4a4f5e` over `#6a6a72` | gravel `#6e6a64` |
| Death beats | `#0b0f14` | ghost Doug only |
| Diagram cards | cream `#f4f1dc` | |
| Sober card / honesty card | `#15181a` / `#4a4f5e`, white text | |
Sea water stays the surface colour `#3a9ad9` throughout (art bible); the ramp is carried by the sky and the ground.

HUD (drawn by the shotlist): `DOUG DEATHS: N` at (1590,162); under it a size-28 label `WALRUS COUNT: 1 / 2 / ABOUT 300 / ABOUT 35,000` at y 238 with `walrus_head_icon` at 0.3 to its left (red label after death 280).

Reused from the library (no request): `ringed_seal`, `bearded_seal`, `polar_bear`, `polar_bear_lying`, `polar_bear_sniffing`, `clam`, `inflatable_dinghy`, `inflatable_dinghy_swamped`, `rowboat`, `canoe_paddle`, `marina_pontoon`, `sailboat`, `fishing_boat`, `bush_plane` (the narrator's "AERIAL SURVEY" plane), `arctic_map` (Franz Josef Land ring at local (360,-245)), `field_guide_open` (WALRUS page overlays: NO stamps, pencilled MAYBE, the EATS CLAMS sticky note), `platform_scale`, `seesaw`, `speedometer` (the pressure gauge), `calendar`, `clock`, `bed`, `music_note` (the bell sounds), `tape_measure`, `placard` (QUIET PLEASE / nope), `signboard`, `house`, `stick_man_plain`, `wildlife_official`, `empire_state_building`, `beach_towel`, `doug_sunglasses`, `travel_suitcase`, `binoculars`, `tall_ladder`, `ice_chunk`, `silver_fish` (the mackerel), `clipboard`, `heart_icon`, `giant_cartoon_jaw`, `narrator_hand_pencil`, `doug_cap`, `water_splash`, `water_splash_small`, `dust_plume`, `thermometer`, `question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`. The jam jar, pull-up bar, neck cross-section, phone stack, pool tank and shelf diagram are drawn in the shotlist with primitives.

---

## The walrus family

## `walrus_bull`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_bull.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). tusk tips (+274..+300,-12); pad reaches x +320. Boss zone has bosses only, no stains.
**Creature (the hero drawing: every item).**
- Look: Adult bull walrus hauled out on its belly, side view facing right, chest propped up on straight front flippers, head raised and level, looking ahead. Huge, heavy, wrinkled cinnamon-brown body; thick neck and shoulders covered in the knobbly **bosses** (lumpy raised skin, clearly visible, adult males only), a few pale old scars on the neck and shoulders; small dark eyes high on the head; broad whisker pad of stiff pale bristles; two long ivory tusks (the longest of any walrus drawing) hanging straight down from the upper jaw past the chin; rear flippers folded forward under the hindquarters at the left.
- Facing / anchor / size: Facing right. Bottom-centre anchor (belly and flippers on y=0). About 620 x 340 (x -310..310, y -340..0). Head centre about (+220,-200), eye (+240,-240), whisker pad (+275,-160), tusks from (+260,-130) down to tips at about (+300,-10). **Neck/shoulder boss zone x +40..+170, y -320..-200** (the shotlist circles it in s112 and sprays grey grease on it in s013/s014: keep that zone plain skin texture, no pre-drawn stains).
- Notes: Used from 0.28 (crowds) to 1.5 (close-ups, s013, s111-s112), as a black silhouette with red spray (s006) and flipped. Must read at 0.28 on gravel and snow.
- Shots: s005, s006, s007, s011, s013, s014, s018, s019, s023 (rotated +12 while rolling), s057, s058, s066, s077, s096 (on a dinghy), s108, s109, s111, s112, s113, s115, s144-s162 (herd), s164, s179, s180 (40 shots)

## `walrus_cow`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_cow.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). tusk tips (+234..+250,-22); outline 6.
**Creature (females, crowds, the cow that lies down on Doug's gap).**
- Look: Adult female walrus hauled out, side view facing right, same family as `walrus_bull` but visibly smaller and smoother: no bosses, slimmer neck, fewer scars, **shorter, thinner tusks** (still clearly tusks), chest propped on front flippers, head level. Same palette.
- Facing / anchor / size: Facing right. Bottom-centre anchor. About 520 x 260 (x -260..260, y -260..0). Tusk tips at about (+250,-20).
- Notes: This is the crowd tile: the packed beaches repeat it 20-40 times per frame at 0.28-0.52, often flipped, and as plain black silhouettes in the opener (s003-s004). So keep the silhouette simple and the outline 5-6 so it survives at 0.3. It is also the cow that lies down on the gap (s183-s184, scale 0.6-0.62, rotated -6).
- Shots: s003, s004, s057, s058, s077, s089, s108, s109, s113, s144-s166, s169-s171, s177-s184, s186, s190-s193, s196-s198, s203-s210 (52 shots)

## `walrus_sleeping`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_sleeping.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). **tusk tips run forward to x +344 (24 past the requested +320)** so they lie on the ground ahead of the chin; back top (0,-226).
**Creature (the resting bull, the post-fight rest, the closing image).**
- Look: Walrus lying flat on its belly, fully relaxed, side view facing right, chin resting on the ground, eyes shut (two short curved lines), tusks resting forward on the ground, flippers flat. Same palette as `walrus_bull` (a bull: bosses visible, but smaller in this pose).
- Facing / anchor / size: Facing right. Bottom-centre anchor. About 640 x 230 (x -320..320, y -230..0). Chin about (+290,-20).
- Notes: s186 has `doug_cap` sitting on its back (top of the back about (0,-215)); s213-s214 has the cap peeking out from under its left flank at about (-300,-10). Used at 0.3 on a tiny floe in the shelf diagram (s174-s175).
- Shots: s020, s021, s022, s121, s128, s131, s174, s175, s186, s213, s214 (11 shots)

## `walrus_bull_hug`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_bull_hug.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). **pose deviation:** a walrus's front flippers are at its shoulders, so with the head at the right and the flippers over Doug at x -130..+12 the bull is drawn curled on its side, head resting on its own flank at the right (head x +392..+556, y -326..-190, tusks hanging along its body to y -74). **Body starts at x -138, not -160**, to keep Doug's head/cap clear. Rear flippers on the ground at x +470..+580. Checked on Doug `on_back` at 0.5 and 1.0 (preview `035-walrus-without-a-bite-hug.png`).
**Creature (death 275: "wraps both front flippers around him").**
- Look: The bull, rolled onto its side **behind** Doug, belly toward him, both front flippers draped forward over Doug's chest and belly as in a lazy hug. Eyes half shut and content but **no smile**. Head at the RIGHT end, far from Doug's head (nothing near Doug's face; no mouth contact). No tusk near Doug.
- Facing / anchor / size: **A worn-prop-style overlay: it is placed at exactly the same x / y / scale as Doug's `on_back` hip point** (Doug at scale 0.5; the shotlist draws the hug after Doug). In Doug's `on_back` local frame: hips (0,0), shoulders (-122,0), head centre (-218,0) r 72 plus the cap above it, feet out to +152, ground line y +70. The walrus body lies behind and above him: about x -160..+560, y -340..+60 (body top around y -340, its lower edge just above Doug's torso line at y ~ -30, the bulk of it to the right over and past his feet). The two front flippers come down from the chest at about (-60,-60) and drape over his torso between x -130 and -20 (one over the chest, one over the belly), ending around y +30.
- Notes: **Keep Doug's head and cap fully clear: nothing at x < -140 above y +70.** Draw the hug transparent except for the walrus itself, so Doug's legs and the towel below show.
- Shots: s024, s025 (2 shots)

## `walrus_bull_rearing`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_bull_rearing.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). tusk tips (+228..+252,-252); head top (+150,-560).
**Creature (The Fight).**
- Look: Bull walrus reared up on its front flippers in a threat display, chest high, neck stretched, head lifted and turned slightly down, tusks swung forward and down like two spears. Bosses and scars clearly visible on the neck. Mouth closed, small eyes, no blood, no wounds.
- Facing / anchor / size: Facing right. Bottom-centre anchor (front flippers and belly on y=0). About 460 x 560 (x -220..240, y -560..0). Head top about (+150,-560), tusk tips about (+250,-250).
- Notes: Two copies face to face (one flipped), at 0.75-1.1, also as black silhouettes with red spray (s103), and rotated about ±12 for "both bulls swing" (s119). The swing is cut before contact: the tusks never touch Doug or each other.
- Shots: s103, s104, s105, s106, s107, s118, s119 (7 shots)

## `walrus_cow_calf`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_cow_calf.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). calf at about (-30,-140), x -112..+54, plain dot eye, no mouth; underwater part #8fa9c4 with a #1b4f86 outline.
**Creature (The Boat: the mother protecting her calf).**
- Look: A female walrus swimming at the surface, side view facing right, head and back above the water with short tusks, body fading below the waterline (lighter, bluer tint under water). A **small, plain calf** rides on her back near the middle: brown, rounded, dot eye with no shine, no tusks, no smile, no big eyes.
- Facing / anchor / size: Facing right. Anchor (0,0) = the waterline at the centre. About 560 x 340 (x -280..280, y -220..+120). Mother's head about (+200,-120); calf on her back at about (-40,-170), about 150 long.
- Notes: Used at 0.5-1.4 on open water, flipped once (s102). It must not read as cute: keep the calf small and simple.
- Shots: s083, s086, s087, s088, s091, s092, s093, s097, s098, s099, s102 (11 shots)

## `walrus_swimming`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_swimming.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). tusk tips (+215..+232,+126); throat underside at y ~+90..+98 between x +150..+206.
**Creature (underwater: The Suction, the pool study, the bell songs).**
- Look: Walrus swimming underwater, side view facing right, body stretched out, front flippers back along the sides, rear flippers trailing, tusks pointing down and slightly back, whisker pad forward. Same palette, slightly bluer shading for the underwater light.
- Facing / anchor / size: Facing right. Centre anchor. About 640 x 260 (x -320..320, y -130..130). Mouth about (+300,+40); throat (for the air sacs the shotlist draws) about (+160..+200, +80..+95).
- Notes: Used as a black silhouette with a red rim on blue (s029, s070), rotated -70 (leaning on the pool wall, s128), flipped, at 0.4-1.2.
- Shots: s029, s038, s041, s045, s046, s047, s051, s070, s095, s128, s129, s130, s131, s133, s134, s135 (16 shots)

## `walrus_feeding`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_feeding.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). built from `walrus_swimming` rotated 30 deg; **the trailing rear flipper reaches about (-532,-370), 50 above the requested -320.** Mouth at about (+10,-10).
**Creature (The Suction: nosing the seafloor for clams).**
- Look: Walrus underwater, head down, snout pressed onto the muddy seafloor, the body angled up and back behind it toward the upper left, whiskers fanned out wide on the mud, tusks angled back so they don't dig in. Calm, working.
- Facing / anchor / size: Facing right/down. **Anchor (0,0) = the snout tip on the seafloor.** Body runs up-left to about (-560,-320); about 600 x 330 (x -560..40, y -320..10). Mouth about (+20,-10).
- Notes: The shotlist adds white water-jet arrows from the mouth and a mud puff (s035), and a pile of `clam_empty` beside it (s036). Also tiny (0.35) in the shelf diagram.
- Shots: s030, s035, s036, s173, s174 (5 shots)

## `walrus_head_rising`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_head_rising.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). tusks are marked `silhouette_keep`: on `silhouette: true` they stay ivory on the black head (the neck sits behind them, so a black tusk would vanish). Checked at 0.2 and as a red-rim silhouette.
**Creature (the head that comes up out of the water: The Tusks, The Boat, the thumbnail/opening).**
- Look: **Front view, facing the viewer**: a walrus head and thick neck rising out of the water, small eyes looking straight out, broad whisker pad, both tusks hanging down from the mouth, slightly splayed. Water line across the neck with a few ripples. Heavy, wrinkled, no smile.
- Facing / anchor / size: Facing the viewer. Anchor (0,0) = the waterline at the centre. About 340 x 420 (x -170..170, y -360..+60). Eyes about (±55,-270); whisker pad centre (0,-170), ±90 wide; tusks from (±40,-100) to tips at about (±70,+40) (tips just under the waterline so they can read as hooking over a boat side or a floe edge).
- Notes: Black silhouette with red rim on the opening shot and on The Tusks / The Boat title cards. At 0.18-0.22 it is the "heads in the water" crowd (s143, s153-s154, s213-s214), so it must still read at that size.
- Shots: s002, s054, s059, s073, s076, s078, s079, s090, s099, s143, s153, s154, s213, s214 (14 shots)

## `walrus_hauling_out`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_hauling_out.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). nothing at x>0 below y 0 (the ice); tusk tips (+124..+150,+6); flipper on ice x +4..+96.
**Creature (The Tusks: "tooth walker").**
- Look: Side view facing right: a walrus heaving itself out of the sea onto the edge of a floe, **tusks driven into the ice top**, front flippers on the ice, chest pressed against the ice edge, the rear half still in the water (lighter, bluer tint below the waterline). Straining, not angry.
- Facing / anchor / size: Facing right. **Anchor (0,0) = the top corner of the floe edge** (the ice surface runs right from here along y=0; the sea is at about y +40 to the left/below). The drawing has no ice of its own (the shotlist draws the floe). About 620 x 470 (x -420..200, y -330..+140). Tusk tips in the ice top at about (+120..+150, +5); front flippers at about (+40,0).
- Notes: s074 rotates it -14 on a tipping floe.
- Shots: s055, s060, s064, s074 (4 shots)

## `walrus_hanging_asleep`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_hanging_asleep.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). rear flippers reach y +444 (24 below the requested +420); tusk tips on the ice at (+56..+76,-4).
**Creature (The Sleep: side close-up).**
- Look: Side view facing right: a walrus asleep in the water, **tusks hooked over the edge of an ice floe** so the head rests at the edge, eyes shut, body hanging straight down below the waterline (cross-section style: the underwater part lighter and bluer). Peaceful.
- Facing / anchor / size: Facing right. **Anchor (0,0) = the top corner of the ice edge** (the ice is to the right of x=0; the waterline is at about y +40). No ice drawn in the asset. About 350 x 620 (x -260..90, y -200..+420). Tusk tips resting on the ice top at about (+70,0).
- Shots: s126, s127 (2 shots)

## `walrus_hanging_front`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_hanging_front.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). head flat-bottomed on the edge line, tusk tips (±45,+70). Checked as a row of 12 at 0.34 on the dusk sea.
**Creature (The Sleep: the row of hundreds).**
- Look: Seen from on the ice looking out to sea: a walrus head just beyond a horizontal ice edge, eyes shut, chin near the water, **both tusks reaching forward over the edge and resting on the ice** toward the viewer. Simple and bold, a repeatable tile.
- Facing / anchor / size: Facing the viewer. **Anchor (0,0) = the ice edge line**: the head is above it (y < 0, in the water), the tusks cross it and rest on the ice (y > 0). About 240 x 310 (x -120..120, y -240..+70). Tusk tips at about (±45,+70).
- Notes: Repeated 12-16 times in a row at 0.32-0.42 on a dusk sea (`#3a9ad9` under `#e88a4a`), with the ice strip in front at y 820. Must read at 0.32.
- Shots: s122, s123, s124, s125, s136, s137, s138, s139 (8 shots)

## `walrus_snout_closeup`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_snout_closeup.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). 14 bristle rows at y -106..+66; lower lip at (0,+96); tusks slim (40 wide at the root) to (±120,+520).
**Creature (The Suction / The Tusks diagram close-ups).**
- Look: Front close-up of a walrus face: tiny eyes high and wide, the broad square whisker pad covered in **many rows of stiff pale whiskers** (13-15 neat-ish rows, so the "rows" label makes sense), a hint of the lower lip below it, and both **full tusks** hanging straight down to their tips. Wrinkled skin, no smile.
- Facing / anchor / size: Facing the viewer. **Centre anchor at the whisker pad centre.** About 520 x 850 (x -260..260, y -330..+520). Eyes about (±150,-230); whisker pad ±180 wide, y -120..+80; lower lip / mouth (0,+90); tusks from (±80,+60) to tips at (±120,+520).
- Notes: Used at 0.75 on cream cards (the shotlist overlays red dotted lines across the whisker rows at local y -95..+25 and a 1 m bracket beside the tusks), and at 0.6 pressing its mouth onto a sealed jam jar lid (s043-s044: the lip line at local +90 sits on the lid; the tusks hang down in front of the jar, so keep them slim).
- Shots: s033, s034, s043, s044, s052, s053, s056, s061, s062, s063 (10 shots)

## `walrus_mouth_cutaway`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_mouth_cutaway.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). tongue block x +12..+90 on a thin root rod; empty space x -120..+12 above and below the rod; lip opening at about (+268,+40).
**Diagram (The Suction: the tongue as a piston).**
- Look: Side cross-section of a walrus snout, facing right, diagram style: brown exterior outline of the head and whisker pad, cream interior, a domed palate arch, and the **tongue as a pink cartoon piston** (`#e79aa0`, block-shaped with a rounded front) with clear empty space behind it for "pulled back". The lips at the right form a round opening where a clam shell sits. No teeth detail, nothing realistic.
- Facing / anchor / size: Facing right. Centre anchor. About 600 x 400 (x -300..300, y -200..200). Mouth opening at about (+260,+40); tongue front at about (+80,+40); the space behind the tongue about x -120..+20.
- Notes: At 1.2 on cream. The shotlist adds a red PULL arrow under it, a clam at the mouth and the soft clam body (a cream ellipse) inside at about (+100,+40).
- Shots: s031, s032 (2 shots)

## `walrus_top_view`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_top_view.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). tusk tips poke to x +164.
**Creature (aerial crowds: The Haulout, The Stampede).**
- Look: A walrus seen from directly above: an elongated brown oval body with a slightly narrower head end at the right, the two front flippers and the paired rear flippers as small stubs, the two tusk tips just visible poking forward past the head. A few fold lines. Simple and bold.
- Facing / anchor / size: Head to the right. Centre anchor. About 300 x 140 (x -150..150, y -70..70).
- Notes: Tiled 100+ times at 0.25-0.3 on grey gravel (`#8c8a84` and the darker `#6e6a64`) to make the 35,000 beach. Outline 5 so it survives at 0.25.
- Shots: s167, s168, s176, s187, s188, s189 (6 shots)

## `walrus_head_icon`
**DONE (illustrator, 2026-11-02)**: `assets/library/walrus_head_icon.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). 4 px cream rim for near-black frames; reads in the HUD at 0.3.
**Icon (the WALRUS COUNT meter, the "1 in 9" row, the "100 per person" grid).**
- Look: A bold flat walrus face icon, front view: brown round head, two dot eyes, whisker pad, two white tusks down. Thick outline, no shading detail, no smile.
- Facing / anchor / size: Facing the viewer. Centre anchor. About 120 x 120 (x -60..60, y -60..60), tusks inside that box.
- Notes: In the HUD at 0.3 (36 px) on every shot, so it must read at 36 px; in rows at 0.42-1.1 on cream. On the near-black death frames it sits beside a white label, so give it a light rim or keep the brown mid-tone.
- Shots: every shot with the HUD (210 shots), plus s010, s012, s063, s172

---

## Props and icons

## `clam_empty`
**DONE (illustrator, 2026-11-02)**: `assets/library/clam_empty.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). upper valve opens to y -94.
**Prop (the empty shell the walrus leaves behind).**
- Look: An open, empty clam shell: two pale off-white `#e9e4d6` valves hinged and gaping, growth lines, **nothing inside** (clean pale interior). Same family as the library `clam` so they sit together.
- Facing / anchor / size: Bottom-centre anchor (resting on the seafloor or a palm). About 180 x 80 (x -90..90, y -80..0).
- Notes: Stacked into a small hill of 10 at 0.42 (s036); in Doug's palm at 0.32 (s047).
- Shots: s032, s036, s047 (3 shots)

## `dairy_cow`
**DONE (illustrator, 2026-11-02)**: `assets/library/dairy_cow.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). x -300..+318, y -404..0.
**Animal (the weight comparisons: "two and a half dairy cows", "more than a dairy cow").**
- Look: A Holstein dairy cow standing, side view facing right: black-and-white patches, pink udder (small and simple), short horns or none, ear tag optional. Crude-friendly but in the detailed tier. Instantly "dairy cow", not the library Hereford `cow`.
- Facing / anchor / size: Facing right. Bottom-centre anchor. About 610 x 400 (x -300..310, y -400..0).
- Notes: s015 has three in a row at 0.62 with the third half off the right frame edge (that is the "half"). Never cut in half on screen.
- Shots: s015, s089 (2 shots)

## `navy_ship`
**DONE (illustrator, 2026-11-02)**: `assets/library/navy_ship.json`, preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png). hull number 462, no flags, insignia or weapons.
**Vehicle (The Boat: the Northern Fleet expedition ship offshore).**
- Look: A plain grey naval support ship / tug, side view facing right: grey hull `#8a9096` with a darker waterline, a small white superstructure with a bridge and dark windows, a mast, a small hull number. No flags with real insignia, no weapons.
- Facing / anchor / size: Facing right. Anchor (0,0) = waterline at the centre. About 580 x 300 (x -300..280, y -260..+40).
- Shots: s081, s082 (2 shots)

## `eye_icon`, `ear_icon`, `nose_icon`
**DONE (illustrator, 2026-11-02)**: `eye_icon.json`, `ear_icon.json`, `nose_icon.json` (matching white discs, outline 5), preview assets/previews/035-walrus-without-a-bite-assets.png (context: -context.png, -hug.png).
**Icons (The Stampede: "an unusual sight, sound or smell").**
- Look: Three matching bold flat icons on a white disc with a black outline: a single cartoon eye (white with a big black pupil), a cartoon human ear, a cartoon nose. Same line weight and disc size so they read as a set.
- Facing / anchor / size: Centre anchor. About 160 x 120 each (x -80..80, y -60..60).
- Notes: Side by side at 0.6 on the dark boss sky `#4a4f5e`, each with a red "!" beside it.
- Shots: s191 (1 shot each)
