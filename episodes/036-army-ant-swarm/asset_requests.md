# 036-army-ant-swarm: asset requests (director)

House style: detailed tier for creatures, places and props (outlines 4-6, flat fills, interior shading with `spray`, darker backs and lighter bellies). Humans use the crude tier (Doug's line, `auto_ink`). Everything faces **right** unless noted. Sizes are local units at scale 1.

**I laid out the shotlist against the anchors and extents below.** I rendered a stand-in pass with boxes of exactly these extents and checked it on contact sheets, so please keep them. If something has to move, tell me and I will re-place it.

33 new drawings, in priority order. The ants come first: `army_ant_carpet` and `army_ant_worker` are in about 100 of the 218 shots.

## Rules from the brief (section 7) that apply to every ant drawing
- **The ants are never cute.** No faces, no smiles, no googly eyes, no eye shine, no pupils. The only eye allowed is a single tiny dark dot on the worker's head, because the script says "its eye is a single dot". No marching-band or "ant army" military-cartoon look. The soldiers' jaws read as tools, not characters.
- **Ant palette (director proposal for the art director):** body dark red-brown `#6e2e1c`, gaster (abdomen) a little darker `#5a2a18`, highlights and the rim light on the top edge `#a0583a`, legs `#4a1e10`, outline black 4-5. The soldiers' big heads are pale ochre `#d9b25a` (real *Eciton burchellii* soldiers have pale heads), with dark `#3a1a0c` sickle jaws.
  The ants have to stay mid-tone so they read on six grounds: pale forest `#dde8cc`, mid forest `#87996f`, night `#1b2f4a`, nest dusk `#46523f` / `#3a4535`, dawn orange `#f2a24a` / `#f6c45a`, and cream `#f4f1dc`. Keep the `#a0583a` rim on the top edge of every body part.
- **No prey being cut up, no ants on skin, no carcasses, no bites, no blood** anywhere. Cargo (larvae, a grasshopper, the cap) is carried whole and held above the column.
- Silhouette use: `army_ant_soldier`, `army_ant_queen`, `ant_bivouac`, `army_ant_carpet`, `driver_ant_queen` and `driver_ant_head_jaws` are shown with `silhouette: true` (filled black). Keep their outlines clean: jaws, legs and antennae should read as separate shapes.

## Episode palette (director proposal: a "distance to the queen" ramp, one step darker per item along the trail)
| Item | Sky / canopy light | Background trunks | Ground (leaf litter speckle) |
|---|---|---|---|
| 1 The Swarm Front | `#dde8cc` | `#b7c6a2` | `#a8804f` (`#8a6438`) |
| 2 The Followers | `#d0deba` | `#a9b993` | `#9f7848` |
| 3 The Menu | `#c2d2a9` | `#9bab84` | `#957044` |
| 4 The Soldiers | `#b1c398` | `#8b9c76` | `#8a6640` |
| 5 The Road Crew | `#9db085` | `#7a8a66` | `#7e5d3a` |
| 6 The Death Spiral | `#87996f` (bare-ground cards `#a08460`) | `#687757` | `#715334` |
| 7 The Night Move | night `#1b2f4a`, dusk `#4a3f5e`, morning `#dfe7d6` | `#14233a` | `#3a3426` |
| 8 The Living Nest | `#46523f` | `#363f30` | `#5a4630` |
| 9 The Queen | `#3a4535` | `#2c3428` | `#4e3c28` |
| 10 The Driver Ants (Africa, dawn) | `#f2a24a` over `#f6c45a` | `#c9803a` | laterite `#9a5a32` |
| Death beats / diagram cards | `#0b0f14` / cream `#f4f1dc` | | |

The forest skies count as green grounds, so their wordart uses the white-to-yellow override. On cream, night and dawn the default gradient is used.

HUD (drawn by the shotlist): `DOUG DEATHS: N` at (1590,162). Under it is the new **DISTANCE TO QUEEN** sign: a size-28 `label` at (1580,238) with wood fill `#e8c07a`, reading ABOUT 200 M, 200 M, 150 M, 100 M, 50 M, 30 M, 10 M, 0 M and then AFRICA in red. No icon is needed.

Reused from the library, no request needed: `hammock` (the low hammock, items 1 and 10), `fallen_log`, `tree_branch`, `tree_stump` (Doug's watching perch beside the carpet), `rainforest_tree`, `leaf`, `tent`, `campfire`, `field_guide_open` (ARMY ANT page overlays: NO stamps, MAYBE, the JUST WALK AWAY sticky note), `doug_cap`, `city_bus`, `panama_isthmus_map`, `africa_map`, `clock`, `wait_stopwatch`, `calendar`, `stick_man_plain`, `scientist`, `scientist_woman`, `pencil`, `rice_grain`, `coat_hook`, `sofa`, `fishing_boat`, `indian_red_scorpion`, `giant_tarantula`, `cockroach`, `lizard`, `black_mamba`, `feather_nest`, `house_fly` (parasitic flies), `parasitic_wasp`, `tape_measure`, `traffic_cone`, `small_car`, `angry_sun`, `thumbs_up_hand`, `stew_bowl`, `thermometer`, `stadium` (Wembley stand-in, no logos), `city_skyline_small` (greater New York stand-in), `travel_suitcase`, `signboard` (the big DISTANCE TO QUEEN sign), `narrator_hand_pencil`, `question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`.
The shotlist draws these with primitives: the pie chart, the football pitches, the motorway, the bar chart, the ballot box, the egg piles, the index cards and the soil tunnels.

---

## The ants

## `army_ant_carpet`
**The swarm front, side view (the hero drawing: about 50 shots, tiled edge to edge).**
- Look: a low, dense, living carpet of *Eciton burchellii* workers seen from the side at ground level. Dozens of overlapping dark red-brown ant bodies with legs and elbowed antennae poking up along a ragged top edge, and a few slightly larger pale-headed soldiers mixed in near the top. The bottom edge sits flat on the ground. The **right end is the leading edge**: ragged and thinning out, with a few scouts running ahead. The left end is cut straight so tiles can butt together. Use a darker interior (`#5a2a18` with `#3a160c` speckle) and a lighter `#a0583a` rim along the top edge, so it reads as a mass and not as a brown rectangle.
- Facing / anchor / size: moves right. **Bottom-centre anchor, x -600..600, y -220..0.** Ragged front zone x +480..+600.
- Tiling: the shotlist places tiles every **1080 units** (120 units overlap). Each later tile is drawn on top of the one to its left, so its straight left edge covers the previous tile's ragged right end. Please keep the left edge straight and opaque for its first 120 units.
- Notes: used at 0.45-1.1. Some uses: as a black silhouette (s195, the driver-ant title card), climbing the hammock legs (s024-s025), flowing past Doug in front of and behind him (s062-s065), and on dawn orange in the Driver Ants item. It must still read as "many ants" at 0.45.
- Shots: s004-s007, s009, s015-s018, s022-s025, s027, s029-s030, s033-s035, s037-s038, s040-s042, s044-s046, s058, s060-s065, s084, s088-s089, s108, s148, s182, s194-s196, s198, s204-s207, s209-s212
- **DONE (illustrator)**: `assets/library/army_ant_carpet.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png). Tiles seamlessly at 1080: full height to +480, thins only in the +480..+600 overlap zone. Measured bbox x -606..612, y -207..+5.

## `army_ant_worker`
**One worker, side view (about 50 shots, from tiny cargo teams at 0.16 to a close-up at 2.6).**
- Look: an *Eciton* worker. Slim, long-legged, dark red-brown. Rounded head at the right with **one tiny dark dot eye** and no other face, short curved mandibles, and elbowed antennae. Narrow thorax, two small petiole nodes (the waist), and an oval gaster at the left with a **small visible sting tip** at its end. Six long thin jointed legs, feet on the ground line.
- Facing / anchor / size: facing right. **Centre anchor, x -180..180, y -90..90** (feet at y +90). Eye dot at about (+150,-40). Sting tip at about (-175,+30) (s083 circles it in red). Head x +110..+180.
- Notes: used rotated ±35 climbing the hammock ropes, rotated 80 climbing up to the wasp nest, and flipped. It carries cargo held above it: the shotlist puts larvae, the cap and a grasshopper on top of 2-6 workers at scale 0.22-0.35. At 2.6 (s013) it fills most of the frame, so the detail tier must hold up there: a couple of plates on the gaster, leg joints, and a highlight on the head.
- Shots: s002, s009, s013-s014, s024-s025, s027, s041, s049, s055-s057, s069, s078-s080, s083, s091-s096, s098, s105-s107, s112, s121, s123-s124, s131-s133, s137-s140, s143, s145, s150, s172-s173, s176-s178, s181-s182, s185, s189-s190
- **DONE (illustrator)**: `assets/library/army_ant_worker.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png). Eye dot (+150,-40), sting tip (-178,+31), feet on +90.

## `army_ant_soldier`
**The soldier caste, side view.**
- Look: a bigger *Eciton burchellii* soldier. Same body family as the worker, but with a **much bigger pale ochre head** (`#d9b25a` with a darker `#b08a3a` back edge) and two **long, thin, curved sickle jaws** (dark `#3a1a0c`) hooking forward and up from the front of the head like two coat hooks. No face, no eye shine. Long legs, dark red-brown body.
- Facing / anchor / size: facing right. **Centre anchor, x -240..240, y -110..110**, head x +60..+170, jaw tips at about (+235,-20). **Total length tip to tail 480 units**: at scale 1.25 it must match two `rice_grain` end to end (600 px, s073).
- Notes: s085-s087 have a brown stick line ending in its jaws at about (+190..+240, -10..+50) x scale (Doug's stick, which it keeps), so leave the jaw gap open. Used as a red-glow silhouette for the chapter title (s068) and the item-3 teaser (s067), and as a tiny icon in a thought bubble wearing `officer_cap` (s076-s077).
- Shots: s005, s067-s070, s072-s073, s076-s078, s085-s087
- **DONE (illustrator)**: `assets/library/army_ant_soldier.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png). Jaw tip (+236,-20); jaw hook gap left open for the stick.

## `army_ant_soldier_head`
**Front-view close-up of the soldier's head (the coat-hook comparison and "these jaws can't cut").**
- Look: the pale ochre soldier head seen from the front, filling the drawing. Two long dark curved sickle mandibles hang down and curve inward and up at the tips, like two J hooks. Short elbowed antennae, and two tiny dark dot eyes at most (no shine, no brows, no mouth). The inner edges of the jaws are smooth, with no teeth, because they don't cut.
- Facing / anchor / size: front view. **Centre anchor, x -300..300, y -300..300**, jaws in the lower half (tips around (±60,+280)).
- Notes: s071 sets it beside `coat_hook` at 1.8 with an "=" sign, so the J-hook resemblance must be obvious. The graphic designer may also want it for the thumbnail (brief section 8: "giant soldier head, sickle jaws, no face").
- Shots: s071, s081-s082
- **DONE (illustrator)**: `assets/library/army_ant_soldier_head.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png). No eyes or mouth. Jaw tips about (+-56,+268). Antennae are short feelers at the upper sides (x to +-290).

## `army_ant_soldier_top`
**A soldier seen from directly above (for the overhead column diagram).**
- Look: top-down view. Big pale ochre head at the right with the two sickle jaws curving forward. The dark red-brown thorax and gaster behind it, and six legs splayed out to both sides.
- Facing / anchor / size: head right. **Centre anchor, x -240..240, y -100..100.**
- Notes: used at 0.42 in two rows along both edges of `army_ant_column_top`, and once rotated 40 (a clumsy soldier stumbling into the crowd, s075).
- Shots: s074-s075
- **DONE (illustrator)**: `assets/library/army_ant_soldier_top.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png).

## `army_ant_column_top`
**The raiding column seen from above, as a tileable strip.**
- Look: an overhead view of a dense stream of small dark red-brown workers all heading right, two to three bodies deep, with legs and antennae visible. Lighter `#a0583a` highlights on the heads so it isn't a flat brown bar. Straight cut ends on the left and right so it tiles.
- Facing / anchor / size: flows right. **Centre anchor, x -600..600, y -70..70.** Tiles every 1200 units.
- Notes: used at 0.45-1.0 on cream, bare-ground `#a08460` and brown `#a8804f` cards. It is also used tilted 20 (a group cut off from the raid, s114).
- Shots: s010-s012, s074-s075, s090, s113-s114, s126, s141-s142
- **DONE (illustrator)**: `assets/library/army_ant_column_top.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png). Periodic at 1200; edge ants poke out about 4 units past +-600.

## `army_ant_mill`
**The death spiral: a closed ring of ants running in a circle, seen from above.**
- Look: a thick ring of overhead-view workers (top-down, same family as the column) all running **counterclockwise** nose-to-tail, three or four bodies deep. No trail leads in or out. The middle of the ring is empty bare ground (transparent, so the card colour shows through). Add a few small curved motion ticks on the outside.
- Facing / anchor / size: **centre anchor, x -400..400, y -400..400.** Outer radius about 380, inner radius about 260, so the ring path runs at about radius 320.
- Notes: s127-s129 stand Doug (a side-view stick man, scale 0.5) on the **bottom of the ring** at local (0,+330) x 0.7 with his feet on it. Keep that bottom-centre stretch readable as part of the ring. Used at 0.4-0.8 on `#a08460`, cream and forest grounds.
- Shots: s109-s111, s116-s118, s122-s130
- **DONE (illustrator)**: `assets/library/army_ant_mill.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png). Counterclockwise, ring r 260..385, motion ticks at r about 392.

## `army_ant_queen`
**The *Eciton* queen (first a silhouette, full reveal at The Queen).**
- Look: a large wingless queen, side view. Smallish head with jaws at the right, a long thorax, and a **huge swollen gaster** at the left with pale cream membrane bands (`#efe2c0`) showing between dark plates. She is visibly much bigger than a worker. No face. Six legs.
- Facing / anchor / size: facing right. **Centre anchor, x -320..320, y -130..130.** Gaster x -320..-40, thorax mid at about (+140,-60) (s178 dots her there with blue paint).
- Notes: used as a black silhouette in s080, s135, s139-s140, and in colour from s172 onward. It is also the "young queens" crowd at 0.45 (s179-s182), and sits on cream cards at 0.65-0.9. Workers stand around her at 0.25-0.35.
- Shots: s080, s135, s139-s140, s172-s173, s175-s190
- **DONE (illustrator)**: `assets/library/army_ant_queen.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png).

## `ant_bivouac`
**The living nest: a hanging mass made entirely of ants.**
- Look: a big rounded mass hanging down like a lumpy sack. Its surface is made of countless interlocked ant bodies and legs (dark red-brown with `#a0583a` speckle highlights). A few short ant chains dangle from the bottom, and there are a few small dark holes (airways). The top is flat where it clings to a log or branch.
- Facing / anchor / size: **top-centre anchor (0,0) = the attachment point. x -310..310, y 0..560.**
- Notes: hangs under `fallen_log` (log at scale 1.15, attachment y about 10 below its anchor), under `tree_branch`, and in a buttress gap. Used at 0.22-0.75, and as a silhouette in s152 (red glow) and s169. In s167-s168 Doug stands **behind** it (drawn before it) with his legs showing below its bottom edge, as "he climbed in". So keep the bottom edge clean, with no chains hanging in the middle 120 units. In s166 `doug_cap` sits on its right edge at local about (+290,+400) x 0.7.
- Shots: s010-s012, s084, s151-s153, s155-s159, s161-s162, s166-s170, s187-s189
- **Done (illustrator):** `assets/library/ant_bivouac.json`, preview `assets/previews/036-army-ant-swarm-bivouacs.png` (log, nest-dusk ground, silhouette, and 0.4 on pale forest). Flat gripping top x -172..172 at y 0; body x -310..310, mass bottom about +500, chains to about +560 at x -236, -150, -100, +110, +176, +246 (none in x -60..60). Edge bristles with legs and ants so the silhouette reads as ants.

## `ant_bivouac_cutaway`
**The same mass, cut open.**
- Look: the `ant_bivouac` outline with the front cut away. Inside is a warmer cavity (`#8a4a2a`), a cluster of small white larvae left of centre at about (-80,+220), and one large queen just right of centre at about (+40,+300) (a small version of `army_ant_queen`). Layers of ant chains form the walls.
- Facing / anchor / size: **identical outline, anchor and extents to `ant_bivouac`** (x -310..310, y 0..560), so the shots can swap one for the other.
- Notes: at scale 0.7 the shotlist rings the queen with a red circle at local about (+43,+343) and points arrows at the larvae and the queen.
- Shots: s160, s163, s171
- **Done (illustrator):** `assets/library/ant_bivouac_cutaway.json`, preview `assets/previews/036-army-ant-swarm-bivouacs.png` (log, nest-dusk ground, silhouette, and 0.4 on pale forest). Same outline, anchor and chains as `ant_bivouac`. Larva heap centred (-80,+220) (uses `ant_larva` at 0.42); queen (gaster at the left) spans about x -77..+156, y +286..+374, centred near (+40,+330), so the red circle at (+43,+343) rings her.

## `ant_feet_chain`
**Close-up: ant legs hooked together claw to claw.**
- Look: a macro view of several red-brown ant legs crossing and hooking into each other. Each foot ends in a tiny **double hooked claw** gripping the next leg. It reads as chain links, three or four layers deep. No heads or faces.
- Facing / anchor / size: **centre anchor, x -350..350, y -225..225.** One clearly visible claw at about (+250,-30) for the red arrow.
- Shots: s154
- **Done (illustrator):** `assets/library/ant_feet_chain.json`, preview `assets/previews/036-army-ant-swarm-assets-illustrator2.png`. Six legs in three layers; each tarsus ends in a double hook wrapped round the next leg. The arrow claw grips at (+250,-33).

## `ant_larva` and `ant_pupa_cocoon`
- `ant_larva`: a plump white `#fbf6e6` curved grub with faint segment lines and a grey outline. No face. **Centre anchor, x -60..60, y -30..30.**
- `ant_pupa_cocoon`: a pale tan `#e8d8b0` oval silk cocoon with a slightly darker end and a soft highlight. **Centre anchor, x -65..65, y -30..30.**
- Notes: carried above workers at 0.33-0.4, shown on the ground ahead of the swarm (s016-s017), and as big diagram icons at 0.9-1.2 on cream (s145-s146, s164-s165).
- Shots: larva s016-s017, s049-s050, s079-s080, s131-s133, s138-s140, s143, s146, s150, s164-s165 · cocoon s017, s049-s050, s145-s146, s164-s165
- **Done (illustrator):** `assets/library/ant_larva.json` and `assets/library/ant_pupa_cocoon.json`, preview `assets/previews/036-army-ant-swarm-assets-illustrator2.png`.

## `driver_ant_queen`
**The African driver-ant (*Dorylus*) queen, the largest ant known.**
- Look: side view. Small head and thorax at the right, and an enormously long, sausage-shaped, pale-banded gaster stretching left (about two thirds of her length). Dark red-brown with cream membrane bands. Wingless, no face.
- Facing / anchor / size: facing right. **Centre anchor, x -400..400, y -110..110.**
- Notes: s199 shows her as a red-glow silhouette, then in colour next to `thumbs_up_hand` (s200) and over a pile of eggs (s201).
- Shots: s199-s201
- **DONE (illustrator)**: `assets/library/driver_ant_queen.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png). Measured y -87..+109.

## `driver_ant_head_jaws`
**Close-up of a driver ant's head and jaws: "these jaws do cut".**
- Look: a front three-quarter view of a dark red-brown driver-ant head with two broad, curved, **blade-like mandibles whose inner edges carry a row of sharp teeth**. They should look clearly different from the smooth soldier hooks. No eyes, no face.
- Facing / anchor / size: **centre anchor, x -300..300, y -250..250.** Toothed inner edge around (+130,0) for the red arrow (s203).
- Notes: s082 uses it as a small silhouette teaser on `africa_map`.
- Shots: s082, s203
- **DONE (illustrator)**: `assets/library/driver_ant_head_jaws.json`. Preview: assets/previews/036-army-ant-swarm-ants.png (in context: assets/previews/036-army-ant-swarm-ants-context.png). Blind, no face. Toothed inner edge of the near jaw runs from about (+130,0) to (+150,+180).

## `ant_living_bridge`
**A living bridge: ants hooked together across a gap.**
- Look: a sagging chain of eight to ten workers linked leg to leg and jaw to leg, spanning a gap. Two or three bodies thick in the middle and thinner at the ends, which grip the twigs. Side view.
- Facing / anchor / size: **centre anchor, x -300..300, y -40..160.** End grips at (-300,0) and (+300,0); the lowest sag is at about (0,+150). The twigs are not included: the shotlist puts `tree_branch` pieces on each side.
- Notes: at scale 1.2. In s098 a line of small workers (scale 0.22) walks across the top at about y -35 local.
- Shots: s097-s098
- **Done (illustrator):** `assets/library/ant_living_bridge.json`, preview `assets/previews/036-army-ant-swarm-assets-illustrator2.png`. Three layers of linked workers (one at the ends, three in the middle); end ants grip at (+-300,0); lowest legs about +160; top surface about y -10 at the ends, about +80 in the middle.

## The other animals

## `ocellated_antbird`
- Look: *Phaenostictus mcleannani*, perched side view. A **bright blue bare-skin patch around the eye**, black throat, rufous-chestnut neck and breast, and a buff-olive back and wings covered in black scalloped "eye" spots (the ocelli). Long legs gripping the perch, a slim dark bill, and a medium tail. Not cute: a small dark eye inside the blue patch, no smile, no blush.
- Facing / anchor / size: facing right. **Bottom-centre anchor = feet on the perch (0,0). Bill tip to tail tip x -225..225, y -230..0.** It must be exactly 450 long because s036 sets it above the 450-long `pencil` at the same scale: "about the length of a pencil".
- Notes: perched on `tree_branch` (feet at the branch top) at 0.42-0.75, and flipped.
- Shots: s028-s030, s033-s036, s040-s046
- **Done (illustrator):** `assets/library/ocellated_antbird.json`, preview `assets/previews/036-army-ant-swarm-assets-a.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).

## `grasshopper`
- Look: a green rainforest grasshopper, side view. Long body, big folded hind jumping legs, short antennae, a darker green back with a pale belly, and a small dark eye. Plain, not cute.
- Facing / anchor / size: facing right. **Centre anchor, x -180..180, y -90..90.**
- Notes: carried whole by a team of workers (s055-s057, s079-s080, s137), leaping (rotated -30), fleeing, and standing perfectly still (s061).
- Shots: s016, s018, s034, s042, s052, s055-s057, s061, s079-s080, s137, s204
- **Done (illustrator):** `assets/library/grasshopper.json`, preview `assets/previews/036-army-ant-swarm-assets-a.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).

## `ground_beetle`
- Look: a dark metallic blue-black ground beetle, side view. Ridged wing cases, six legs, short antennae.
- Facing / anchor / size: facing right. **Centre anchor, x -150..150, y -80..80.**
- Shots: s052
- **Done (illustrator):** `assets/library/ground_beetle.json`, preview `assets/previews/036-army-ant-swarm-assets-a.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).

## `butterfly`
- Look: a rainforest butterfly with orange and black wings (open, three-quarter view) and thin antennae. No face.
- Facing / anchor / size: **centre anchor, x -100..100, y -75..75.**
- Notes: in s045 it sits on Doug's cap at scale 0.35, so the legs go at the bottom centre.
- Shots: s030, s043, s045-s046
- **Done (illustrator):** `assets/library/butterfly.json`, preview `assets/previews/036-army-ant-swarm-assets-a.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`). The far wings are foreshortened, so the drawing spans x -100..72.

## `wasp_nest_leaf`
- Look: a small grey-tan paper wasp comb hanging from the underside of a broad leaf. Hexagonal cells are visible from the side and below, with a few cells showing white larvae. No wasps drawn.
- Facing / anchor / size: **top-centre anchor (0,0) = the leaf stem, attached under a branch. x -180..180, y 0..300.**
- Shots: s047-s049
- **Done (illustrator):** `assets/library/wasp_nest_leaf.json`, preview `assets/previews/036-army-ant-swarm-assets-a.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).

## `seagull`
- Look: a white and grey gull in flight, wings spread, with a yellow bill.
- Facing / anchor / size: **centre anchor, x -120..120, y -60..60.**
- Shots: s039-s040
- **Done (illustrator):** `assets/library/seagull.json`, preview `assets/previews/036-army-ant-swarm-assets-a.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).

## Doug's props and costume

## `grasshopper_costume`
**Worn over Doug (The Menu: "Doug is dressed as a grasshopper").**
- Look: a green grasshopper body suit. A segmented green torso suit with a paler belly, a long abdomen tube sticking out **behind** his hips, two big folded hind jumping legs on the back side, and two short antennae rising from **behind** his head on a thin headband. **Doug's head, face and red cap stay fully visible.**
- Facing / anchor / size: **anchor = Doug's hips (stand pose, scale 1). Extents x -170..170, y -160..160.** Torso panel x -60..+40 from the neck (y -150) to the hips (y 0). Abdomen tube x -170..-60 at y -60..+20. Hind legs x -200..-40, y -40..+150.
- **Keep the front side (x > +40) and the arms clear.** Doug's arms are drawn before the costume, and s065 has him give a **thumbs up**: the hand point is at local (+112,-156) and the thumb tip at about (+112,-198). Nothing of the suit may cover that.
- Notes: used at 0.7-0.75 with the `stand` and `thumbs_up` poses.
- Shots: s059-s065
- **Done (illustrator):** `assets/library/grasshopper_costume.json`, preview `assets/previews/036-army-ant-swarm-assets-illustrator2.png`. Checked on `stand` and `thumbs_up`: front edge at x +42, thumb and hand clear; antennae rise from a small band at the back of the head (to about (-136,-310)).

## `grasshopper_costume_flat`
**The death image for The Menu: the costume lying flat and empty.**
- Look: the same green costume lying flat on the ground, deflated and empty. The hind legs splay out, and the antennae headband lies at the left end. **Two small X eyes are printed on the headband patch** (the script: "the costume lies flat with X eyes"). Doug's body is not inside it.
- Facing / anchor / size: **centre anchor, x -260..260, y -70..70.** Head end on the left (x -260..-150). The shotlist puts `doug_cap` on top of the head end at local about (-150,-70).
- Notes: shown on black `#0b0f14` at 0.9 (it needs a mid-green fill so it reads on black) and folded into a COSTUMES box at 0.5 (s067).
- Shots: s066-s067
- **Done (illustrator):** `assets/library/grasshopper_costume_flat.json`, preview `assets/previews/036-army-ant-swarm-assets-illustrator2.png`. Checked on #0b0f14 with `doug_cap` at (-150,-70).

## `tent_open_empty`
- Look: the library `tent` exactly (same geometry, colours and anchor) but with the **front zip hanging open**. The door flap is pulled back, the inside is dark and empty, and a pull tab dangles. Morning light, nobody inside.
- Facing / anchor / size: **same anchor and extents as `tent`.**
- Shots: s149
- **Done (illustrator):** `assets/library/tent_open_empty.json`, preview `assets/previews/036-army-ant-swarm-assets-illustrator2.png`. Built from `tent.json` (same geometry, colours and anchor); only the door differs.

## People and things

## `naturalist_old`
- Look: a crude-tier stick man (Doug's tier, `auto_ink`, no red cap) as an early-1900s naturalist. Pith helmet, round glasses, a bushy moustache, a khaki jacket, and a notebook in his back hand. A generic figure, not a likeness of Beebe.
- Facing / anchor / size: facing right. **Anchor = hips (0,0) like `scientist`: feet +150, head top about -320**, x -90..90.
- Shots: s076-s077, s117-s118
- **Done (illustrator):** `assets/library/naturalist_old.json`, preview `assets/previews/036-army-ant-swarm-assets-b.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).

## `officer_cap`
- Look: a peaked military officer's cap. Dark navy crown, black peak, gold band and badge. It is shown only inside a thought bubble, perched on a tiny soldier ant, and then crossed out.
- Facing / anchor / size: facing right. **Centre anchor, x -100..100, y -55..55.**
- Shots: s076-s077
- **Done (illustrator):** `assets/library/officer_cap.json`, preview `assets/previews/036-army-ant-swarm-assets-illustrator2.png`.

## `road_worker_lying`
- Look: a crude-tier stick man (no red cap) lying flat on his back in an orange hi-vis vest with reflective stripes and a yellow hard hat. Calm, resigned face (flat mouth). He lies horizontally to fill a pothole.
- Facing / anchor / size: head at the left. **Centre anchor, x -210..210, y -55..55.**
- Notes: placed in dark pothole ellipses (rx 170) on a grey motorway at 0.75. A car and a bus are drawn on top of him in s100, so keep him flat.
- Shots: s099-s100
- **Done (illustrator):** `assets/library/road_worker_lying.json`, preview `assets/previews/036-army-ant-swarm-assets-illustrator2.png`. auto_ink, but its sample point is above him (on the road), so his limbs carry a pale halo to stay visible inside a dark pothole.

## `researcher_camp_chair`
- Look: a crude-tier field researcher (no red cap: bush hat, glasses, notebook open on knee) sitting in a green folding camp chair, calmly watching.
- Facing / anchor / size: **facing LEFT** (toward the swarm on the left). **Bottom-centre anchor (chair feet on y=0), x -160..160, y -440..0.**
- Shots: s206-s207
- **Done (illustrator):** `assets/library/researcher_camp_chair.json`, preview `assets/previews/036-army-ant-swarm-assets-b.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).

## `athletics_track`
- Look: a top-down view of a standard 400 m oval running track. Red-brown lanes with white lane lines, a green infield, and a short white start line. No logos.
- Facing / anchor / size: **centre anchor, x -450..450, y -240..240.** At 1.4 the shotlist overlays a red ellipse (rx 560, ry 290) that runs just inside the inner lane, so the inner lane edge should sit at about rx 400, ry 207 local.
- Shots: s119-s121
- **Done (illustrator):** `assets/library/athletics_track.json`, preview `assets/previews/036-army-ant-swarm-assets-b.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`). Inner lane edge is a stadium shape (straights ±200, curve radius 204), so about rx 404, ry 204.

## `sesame_seed`
- Look: one cream sesame seed, a flat teardrop with a faint ridge and a tiny pointed tip.
- Facing / anchor / size: **centre anchor, x -180..180, y -105..105.** It is 360 long on purpose so that at the same scale it matches `army_ant_worker`'s length (3 mm each, s096).
- Shots: s096
- **Done (illustrator):** `assets/library/sesame_seed.json`, preview `assets/previews/036-army-ant-swarm-assets-b.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).

## `banknote`
- Look: a generic paper banknote with no real currency, no numbers and no portrait. Pale green-grey with a darker border, an oval guilloche pattern and a blank seal.
- Facing / anchor / size: horizontal. **Centre anchor, x -210..210, y -100..100.** Used rotated 90, standing beside the swollen column.
- Shots: s142
- **Done (illustrator):** `assets/library/banknote.json`, preview `assets/previews/036-army-ant-swarm-assets-b.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).

## `beanbag_chair`
- Look: a slouchy mustard-yellow beanbag chair with fabric creases and a seam.
- Facing / anchor / size: **bottom-centre anchor, x -210..210, y -360..0.** At 1.1 it matches the `ant_bivouac` width at 0.75 (about 1 m).
- Shots: s158-s159
- **Done (illustrator):** `assets/library/beanbag_chair.json`, preview `assets/previews/036-army-ant-swarm-assets-b.png` (dark-ground check `assets/previews/036-army-ant-swarm-assets-dark-check.png`).
