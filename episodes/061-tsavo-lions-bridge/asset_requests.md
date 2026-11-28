# 061-tsavo-lions-bridge: asset requests (director, 2026-11-28)

**29 new drawings.** The shotlist already places them by name, so please keep the **anchor, bounding box and key points**
given here. The generator (`episodes/061-tsavo-lions-bridge/build/gen_shotlist.py`, git-ignored scratch) puts Doug, the
cap, Patterson's hat, the lamp and the labels relative to them. If a key point moves, note the real value under the
request (as in 060) and I will re-run the generator. Everything **faces right** unless noted (the shotlist flips).
House style: detailed tier for animals, props and places (thick 5-6 outlines, flat fills, interior shading); crude tier
(Doug's line weight, `auto_ink`) for the humans.

**CD conditions for this episode (brief section 7, decisions.md 2026-11-28):**
- **Lions are lean, maneless males, blank-eyed.** A plain small amber or dark eye under a heavy brow, no highlight
  sparkle, no brows that emote, mouth closed or a flat line, **never a smile, never cute** (Lion King risk). Short-haired
  neck and shoulders, at most a thin scruffy fringe on the cheeks and throat, heavy bull-like shoulders, visible ribs
  only as one or two faint shading strokes. Tawny `#c9964a` with a paler belly and muzzle, dark tail tuft. Mid-tone so
  they read on the night navies (`#3b3550` down to `#080c1c`). Every lion drawing must survive `"silhouette": true`
  (clean outline, legs, tail and ears separated).
- **No blood, no wounds, no claws in anything, no teeth bared at a person.** No rifles anywhere (Patterson's hat only).
- **Real victims are never drawn.** The humans below are generic plain stick men with no caricature of any ethnicity.
- **No trophy imagery**: no lion skins, rugs with heads, or a hunter posing over a lion.

**Art-director approval needed before keyframes:** all `tsavo_lion*` drawings (the Lion King check), `donkey_carcass_outline`
(gore-free), `lion_trap` / `lion_trap_bent_bar` (must not read as a torture device: a crude wooden-and-iron box), and the
episode device below.

**Episode device (no drawing): DAYS WITHOUT AN INCIDENT.** A chalkboard strip under the counter, primitives in the shotlist:
`rect` x 1345-1835, y 212-266, fill `#2f3a33`, 5 px `#a0522d` frame, white `#f4f4ee` bold size-28 text "DAYS WITHOUT AN
INCIDENT: n" centred at (1590,239). Values 0 (opener), 1 (s019), 0 (s039 death), 1 (s057), 0 (s072), 0 (s092 + s109
wipes), 1 (s128), 2 (s146). A wipe re-draws the board with a small pale chalk-smear spray. In s108/s109 a small in-scene
version stands beside Doug (wiped by `lion_paw_reach`); in s163 a bigger in-scene board is wiped, then covered and
replaced by a flat brown plank on the ground ("THUD"), and the HUD board is blacked out at the same moment. **No HUD
board from s164 to the end** (it fell over). The counter is red-on-pink from the s163 tick to the end.

**Other notes for the art director / CD (please log in decisions.md):**
- s057: Doug upright with `gear: ["bandage", "cap_off"]` while `doug_cap` sits on top of the thorn fence (script: "The
  cap sits on top of the fence"). One-off capless exception per the art bible; exactly one cap in frame.
- Death beats are all cut-aways: s039 (cap on the tent pole), s072 (lantern + sketch + cap on black), s092 (dental
  mirror + cap on black), s109 (paw wipes the board, cut to black, cap leaves on the last truck in s110), s163 (board
  falls, lion eyes stay lit on black). Ghost Doug floats on the follow-up shots. No `on_back` bodies anywhere.
- Field guide page "TSAVO LIONS (x2)" on `field_guide_open`: red NO (s040), orange MAYBE (s128), NO plus the library
  `again_stamp` at local (+140,+140) for "a second red NO" (s161).
- Episode ramp (time in 1898, one step darker per item; death cards `#0b0f14`, diagram cards cream `#f4f1dc`, sober
  cards `#15181a` with no Doug and no counter): opener sunset `#e88a4a`/`#f2a24a` over `#b8913a`; 1 day `#f6dcae` /
  `#d9b45a`; then night skies `#3b3550`, `#2c3156`, `#1b2a52`, `#16244a`, `#122040`, `#0f1a36`, `#0c1430`, `#080c1c`
  over brown grounds `#3a3428` down to `#141210` (brown, not green, so the default WordArt is allowed).
- The off-screen BANG text (s123) sits only in the right half and the top; the lion is a small figure inside the trap
  at the left. Nothing is aimed at anything.

---

## Lions (one animal, several views; same colours and head in all of them)

Size convention: **scale 1 = true size next to Doug at scale 1** (Doug is ~450 units tall, about 1.75 m; a male lion is
about 2.7-3 m nose to tail and about 1.1-1.2 m at the shoulder).

### `tsavo_lion`: s002 s009-s013 s022 s060 s062 s063 s065 s067 s089 s120-s123 s127 s144 s166 s170 s171
**Done (illustrator, 2026-11-28)**: `assets/library/tsavo_lion.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Real key points: nose tip (+387,-279), shoulder top (+150,-324) (the hump sits a little higher/further forward than requested), tail tuft bottom (-372,-110).
Adult **maneless** male Tsavo lion, standing, side view, calm, head level. Anchor **bottom-centre (feet on y=0)**,
bbox x -380..380, y -400..0. Key points: nose tip about (+380,-270), shoulder top about (+120,-300), tail tip near
(-380,-120). Used from scale 0.26 (inside the trap, small figure) to 0.95 (s144 measurement diagram: dotted lines run
nose to tail along y +60 and from the shoulder top down). Also used as a silhouette with a grey `rim` on a near-black
sober card (s089) and stiffly in a museum case (s166, s170, s171).

### `tsavo_lion_walking`: s002 s006 s022 s028-s030 s050 s054 s063 s066 s070 s071 s125 s139 s140 s166 s170 s171
**Done (illustrator, 2026-11-28)**: `assets/library/tsavo_lion_walking.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Nose about (+387,-262).
Same lion mid-stride, relaxed, head level (the "silent pads" walk). Anchor bottom-centre, bbox x -380..380, y -400..0.
Often a silhouette with red glow (s028, s054, s139) and small (0.22-0.3) on maps and in the bush.

### `tsavo_lion_charging`: s033 s050 s152 s154 s155
**Done (illustrator, 2026-11-28)**: `assets/library/tsavo_lion_charging.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Nose about (+400,-226); paws in the air on the forelegs, far hind paw on y=0.
Same lion in a full charge / bound: forelegs reaching forward, hind legs pushing, body low and long, mouth **closed**
(no teeth). Anchor bottom-centre, bbox x -400..400, y -360..0. Used rotated -12 deg as a leap over the thorn fence
(s050) and as a silhouette leaping onto a tent (s033).

### `tsavo_lion_sitting`: s091 s093
**Done (illustrator, 2026-11-28)**: `assets/library/tsavo_lion_sitting.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Nose about (+221,-399), eye about (+156,-412); head top -474 (4 over the bbox top).
Same lion sitting upright on its haunches, head level, calm hard stare (Doug's dental "patient"). Anchor bottom-centre,
bbox x -200..220, y -470..0. Flipped in s091 to face Doug.

### `tsavo_lion_looking_up`: s003 s160 s161 s162
**Done (illustrator, 2026-11-28)**: `assets/library/tsavo_lion_looking_up.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Eye about (+89,-442) (not +120,-450), nose tip about (+121,-500).
The finale image: the second lion sitting at the foot of a thin tree, **head tipped back looking straight up**, patient,
mouth closed. Anchor bottom-centre, bbox x -200..220, y -500..0; eyes about (+120,-450). Used at 0.42-0.5 under
`thin_thorn_tree` on `#080c1c`, and as a red-glow silhouette in s003. Must read as waiting, not as roaring.

### `tsavo_lion_head`: s027 s038
**Done (illustrator, 2026-11-28)**: `assets/library/tsavo_lion_head.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Head is drawn at 1.72x the body head; nose about (+148,0), ears to y -131, chin about +98.
Head and neck only, side view, pushing forward (as if into a doorway / against canvas). Anchor **centre** of the head,
bbox x -260..200, y -150..150. The **neck runs off to the left edge (x -260) with no end outline**, so it always
continues behind a tent edge or off-frame (never a cut end). Only ever used as a black silhouette (s027 at the open tent
door with a red glow; s038 flipped, pressing against Doug's lit tent wall from outside).

### `tsavo_lion_mattress`: s034 s035
**Done (illustrator, 2026-11-28)**: `assets/library/tsavo_lion_mattress.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Lion spans x -388..+387; mattress hangs from the mouth (x +296..+470) and its far end lies on the ground to x +520.
Same lion trotting away to the **right**, carrying a striped mattress (blue-and-white ticking `#5a7ab0` / `#ffffff`,
plain, no person on it) in its mouth, the mattress hanging down beside its shoulder. Anchor bottom-centre, bbox x
-420..520, y -380..0. Slightly absurd, not violent.

---

## Camp and places

### `canvas_tent_open`: s027
**Done (illustrator, 2026-11-28)**: `assets/library/canvas_tent_open.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`.
The library `canvas_tent` (same geometry: x -140..150, y -184..0, bottom-centre) with the **front door flaps tied back**
and a dark doorway `#1a1410` (about x -45..45, y -150..0). Empty inside. A lion-head silhouette appears at the door
(s027), so keep the doorway a clean dark shape.

### `canvas_tent_flat`: s033
**Done (illustrator, 2026-11-28)**: `assets/library/canvas_tent_flat.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Snapped pole tip rises to about (+92,-136); heap edge to x +170 on the right.
The same canvas tent collapsed after a lion jumped on it: canvas heap with sagging creases and one snapped ridge pole
sticking up. Same footprint (x -150..150, y about -80..0). Nothing under it.

### `hurricane_lantern`: s026 s038 s069-s072 s112-s128
**Done (illustrator, 2026-11-28)**: `assets/library/hurricane_lantern.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`.
1890s hurricane lantern: wire handle loop on top, metal cap, glass globe with a warm lit flame glow `#ffe9a0`, round
tin base. Centre anchor, bbox x -45..45, y -80..70 (handle top at y -80). Used at 0.35-0.6 on night scenes and on its
side on the s072 death card, so the globe must stay light against near-black.

### `thorn_fence`: s041 s043-s045 s049 s050 s053 s055-s058 s069-s071
**Done (illustrator, 2026-11-28)**: `assets/library/thorn_fence.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Both ends at y -196 with no side outline (tile at 800). Cap hump at (0,-256).
A boma fence segment of **cut thorn bush**: tangled grey-brown branches `#8a7a5a` / `#5a4a32` piled into a rough hedge,
pale paired thorns on the twigs, broken top edge. Anchor bottom-centre, bbox x -400..400, y -260..0, **tileable**:
segments placed 800 units apart join into one fence. Mid-tone so it reads on night navy; no green leaves. Top centre
(0,-260) holds `doug_cap` in s057. In s056 Doug is drawn *behind* two segments at 1.25 (stuck in it).

### `thorn_fence_gap`: s053
**Done (illustrator, 2026-11-28)**: `assets/library/thorn_fence_gap.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`.
The same segment with a **gap pushed open from outside**: branches bent inward around an opening at x -90..+90 down
to the ground. Same anchor and bbox.

### `thin_thorn_tree`: s003 s046 s047 s149-s162
**Done (illustrator, 2026-11-28)**: `assets/library/thin_thorn_tree.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Fork crotch (0,-640) between the leader (x -36..-42, rising to -900) and the right limb; tin branch runs y -560 at x +20 to -574 at x +262.
Tall thin dry thorn tree (not the flat-topped acacia, not leafy): grey-brown `#6a5a4a` trunk, sparse crooked branches,
a few pale thorns, thin crown. Anchor bottom-centre, bbox x -260..260, y -900..0. Key points:
- **Doug's perch**: a fork near the top with a flat-ish surface at (0,-640), x -50..50. Doug stands there hugging the
  trunk at scale 0.24-0.3 (feet on the fork).
- **Tin branch**: one near-horizontal branch on the right at y -560 from x +20 to +260; six oil tins hang from it at
  x +55..+225 (s046/s047).
- **Climbers**: small branches at (-50,-600) and (+50,-700) where two tiny stick men (scale 0.18) stand (s153).
Must read on `#080c1c` (lighter bark edge) and stay below the top bar at scale 1.0 (top at y 60).

### `tree_with_beds`: s101 s102 s107
**Done (illustrator, 2026-11-28)**: `assets/library/tree_with_beds.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`.
A broad camp tree with **three plain camp beds lashed into its branches** with rope (wooden frames, grey blankets, empty;
nobody in them). Anchor bottom-centre, bbox x -360..360, y -820..0.

### `water_tank_beds`: s102
**Done (illustrator, 2026-11-28)**: `assets/library/water_tank_beds.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Tank top ellipse centre y -514 (front rim -500, back rim -528); beds at x -170..-70 and +70..+170, top about -572.
A cylindrical riveted iron water tank `#7a8088` on a short timber stand, with two camp beds on top at the left and right
ends. **Top surface y -520, x -170..170, centre x -60..60 left clear**: Doug sits there (seat at y -520). Anchor
bottom-centre, bbox x -200..200, y -560..0.

### `steam_locomotive_1898`: s096 s098 s099 s107-s110 s158
**Done (illustrator, 2026-11-28)**: `assets/library/steam_locomotive_1898.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Stack top (+230,-314). Boiler is charcoal #34343a with brass bands and a lighter top line so it reads on night skies.
Small 1890s colonial-railway steam locomotive with tender, side view facing right: black boiler, tall flared smokestack,
cowcatcher, red buffer beam, big driving wheels, cab with a roof. No logos or text. Anchor **bottom-centre on the rail
top (y=0)**, bbox x -330..330, y -310..0 (stack top about (+230,-310)). Used at 0.35-0.75; s158 on the finished bridge.

### `rail_truck_open`: s096 s098 s099 s108-s110
**Done (illustrator, 2026-11-28)**: `assets/library/rail_truck_open.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Top rim cap is y -158..-148 (rim top -158); buffers to x +-242.
Open goods wagon (truck) to couple behind the locomotive: low plank sides `#7a5a3a`, iron frame, two axles. Anchor
bottom-centre on the rail top, bbox x -230..230, y -150..0, **top rim at y -150** (the shotlist puts head circles just
above the rim for "packed with people", and `doug_cap` on the last truck's rim at about x +120 in s110).

### `tsavo_bridge`: s158
**Done (illustrator, 2026-11-28)**: `assets/library/tsavo_bridge.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Rail top y -310 across the whole width; handrail to y -346; piers at x +-250 (edges +-286), water to +60.
The finished Tsavo railway bridge: iron girder spans on stone piers over the river, rails on top. Anchor bottom-centre at
the water line, bbox x -800..800, y -420..+60 (piers into the water). **Rail deck top at y -310 across the whole width**
(the locomotive stands on it).

### `tsavo_bridge_unfinished`: s100 s106 s107
**Done (illustrator, 2026-11-28)**: `assets/library/tsavo_bridge_unfinished.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`.
The same bridge with the **middle span missing** (gap x -250..250; two bare piers and a little timber scaffolding).
Same anchor and bbox.

### `lion_trap`: s111-s117 s119-s123 s126 s127
**Done (illustrator, 2026-11-28)**: `assets/library/lion_trap.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Guide posts of the drop door x -352..-298; ground line to x +-360. Note: anything placed inside is drawn over the front bars.
Patterson's trap: a heavy box cage of wooden railway sleepers and iron rails, seen from the side with **barred front
faces so the inside is visible**. Anchor bottom-centre, bbox x -340..340, y -330..0. Key points:
- **Lion room** x -330..+90 (the bigger left part), **divider** of vertical iron rails at x +90..+110, **men's room**
  x +110..+330, **floor / seat level y -20** (stick men and Doug sit there at 0.32-0.36).
- **Drop door** at the far left end, x -340..-310, shown **down** (closed).
- **Lamp hook** at (+260,-220) (`hurricane_lantern` hangs there).
- Roof top at y -330 (labels go above it). Crude, practical, not a torture device.

### `lion_trap_bent_bar`: s124 s125 s128
**Done (illustrator, 2026-11-28)**: `assets/library/lion_trap_bent_bar.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Bent rail curves inward to about x -256 at y -60; dark gap x -338..-300, y -200..-20.
The same trap after the shooting: the drop door is still down but **one of its rails is bent aside**, leaving a
lion-sized gap at the left end (about x -340..-300, y -200..-20). Same anchor and bbox.

### `machan_platform`: s130-s137 s139-s143 s145 s146
**Done (illustrator, 2026-11-28)**: `assets/library/machan_platform.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Deck top y -900 at the left, -896 at the right (slightly uneven), x -176..176.
Patterson's "crazy structure": a small rough deck of lashed poles on **four thin crooked poles**, rope lashings, slightly
uneven. True scale (deck about 3.5 m up): anchor bottom-centre, bbox x -200..200, y -930..0, **deck top surface y -900,
x -170..170** (Patterson and Doug sit on it at 0.25-0.3, side by side at x -60 and +40). Must read as flimsy (s137 points
a red arrow at a pole).

### `donkey_carcass_outline`: s134 s135 s139 s140
**Done (illustrator, 2026-11-28)**: `assets/library/donkey_carcass_outline.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`.
Gore-free kill shape in the library `carcass_outline` style: a donkey lying on its side as one pale flat shape `#d9cfb8`
with a `#6b6358` width-4 outline only, long ears flat, legs tucked, no eye detail, no wound, nothing red. Anchor
bottom-centre, bbox x -230..230, y -130..0. A grey wire line runs from its hind leg to a stump on the left (s135).

---

## People and hands (crude tier, `auto_ink`)

### `stick_man_sitting`: s034 s035 s115-s128 s131-s143
**Done (illustrator, 2026-11-28)**: `assets/library/stick_man_sitting.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`.
Generic seated stick man at exactly Doug's `sit` proportions with **no cap** (like `stick_man_plain`: round white head,
grey crescent, short hair, neutral face, line weight 5). **Anchor = the seat contact point (0,0)**; legs straight out
forward to about x +152 at y 0, hands resting on the thighs, head top about y -300, head centre about (0,-218). Facing
right. Used for the soldiers in the trap (one flipped), the man left sitting on the ground after the mattress theft
(s034/s035, blinking), and seated Patterson on the platform.

### `patterson_hat`: s005 s006 s100 s106 s110 s111 s130-s135 s139-s143 s151-s153 s157 s158
**Done (illustrator, 2026-11-28)**: `assets/library/patterson_hat.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Checked: stick_man_plain head centre is feet **-368** x scale (not -376); stick_man_sitting head centre is seat -218 x scale (correct).
A plain 1890s felt slouch hat (khaki `#a08a5a`, dark band `#5a3a1e`, brim wider at the front) as a **worn prop that turns
a plain stick man into Patterson**. **Anchor = the wearer's head centre**: the brim sits at about y -55 and the crown
rises to about y -130, brim x about -110..110. The shotlist places it at `stick_man_plain` feet -376 x scale and at
`stick_man_sitting` seat -218 x scale; please check both against the real head centres and note any correction. Also put
on a tiny `stick_man_arms_up` in a tree (s153). No rifle, no badge.

### `narrator_hand_side`: s036 s037 s129
**Done (illustrator, 2026-11-28)**: `assets/library/narrator_hand_side.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Pinch point (0,0) with a small pale sticker dot; fist x +44..+158.
The narrator's crude-tier arm and right hand (same look as `narrator_hand`: white hand, thick black outline with
`keep_ink`, grey sleeve with darker cuff) entering **horizontally from the right edge**, thumb and forefinger pinching
something. **Anchor (0,0) = the pinch point**; fist about x 0..+150, y -50..+60; sleeve from +150 to +900, y -45..+45,
running off-frame. It holds an empty wire coat hanger by the hook (s036/s037) and a "DOUG DEATHS: 435" sticker by its
right edge as it lowers it into the desk drawer (s129). Never above y 280 in the shotlist, so it stays clear of the
counter and the top bar.

### `lion_paw_reach`: s109
**Done (illustrator, 2026-11-28)**: `assets/library/lion_paw_reach.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Paw x -70..+138 (toes to +138), y -72..+74.
A big tawny maneless-lion forepaw and forearm entering from the **left** frame edge (no end outline on the arm), paw
flat and wiping, claws **retracted**. Anchor = paw centre (0,0); paw x -60..+120, y -70..+70; the forearm runs left to
x -700. Placed at (200,680) x 0.7 so it wipes the small in-scene DAYS WITHOUT AN INCIDENT board.

---

## Props

### `lion_sketch_paper`: s059 s060 s069-s073
**Done (illustrator, 2026-11-28)**: `assets/library/lion_sketch_paper.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`.
Doug's "wanted" sketch: a cream sheet of paper (240 x 180, centre anchor), pinned at the top, with a crude pencil
drawing of a **big fluffy-maned cartoon lion** (the lion everyone pictures) and the word **LION** printed under it in
pencil. Grey pencil lines only, no colour, not cute (no smile). Used pinned to a post (scale 1.17-1.3), held by Doug
(0.45), on the ground on black (s072, rotated 12 deg), and crossed out with a red X (s073 at 1.4).

### `lion_skull_broken`: s074-s077 s084 s085 s167
**Done (illustrator, 2026-11-28)**: `assets/library/lion_skull_broken.json`, preview `assets/previews/061-tsavo-lions-bridge-assets.png`. Broken lower canine stub at x +136..+166, y +16..+46 with the dark spot at (+151,+54).
Clean diagram lion skull, side view facing right: cream bone `#efe2c0` with a brown outline, big canines, **one lower
canine visibly broken off short** with a small dark spot at its root (the infection; not red). Centre anchor, bbox
x -260..260, y -170..170; **the broken lower canine at about (+150,+40)** (a red ellipse circles it in s075) and a hair
tuft is placed at about (+150,+60) in s167. No gums, no flesh.
