# 052 asset requests (director, 2026-11-19)

34 new drawings. The shotlist already places them using the anchors and footprints below (local units, scale 1). Please keep
those, or tell me what changed and I'll re-place them. I checked the layout with grey placeholder boxes of exactly these
footprints, so a drawing that grows much past its box will hit the HUD or a neighbour.

**Tiers.** Creatures and places use the detailed tier: layered fills, interior shading (darker back, lighter belly), texture
strokes 2-3 and outlines 3-5. Humans and hands use the crude tier: Doug's line weight, `auto_ink`, and `keep_ink` on the white
hand and face fills. Everything faces RIGHT unless noted; the shotlist flips them.

**Gore and kid appeal are the top risks (brief section 7).** Bites, stings and big-cat kills are the subject, so:
- Never draw blood, wounds, bite marks or a badger being hurt. The swollen cheek is a smooth pale bump, not a wound.
- Teeth show only as clean white cartoon teeth, with no red inside the mouth beyond the usual `#7a0d0d` mouth dark.
- The stink is a green cartoon cloud, never brown and never poop-shaped.
- No cute faces: no big shiny eyes, no smiles and no blush on the badger, lions, leopard, jackal or birds. Use the library
  `honey_badger` look (tiny eye, blunt black face) as the reference for every badger variant, so all seven read as the same animal.

**HUD.** On every shot the death counter plus the WEIGH-IN (a `platform_scale` icon at 0.36 with two size-28 labels, "BADGER: ~9 kg"
and the attacker) fill x ~1140-1860, y 110-305. Tall drawings are placed with that in mind.

**Reused from the library (no work needed):** `honey_badger`, `jackal`, `leopard`, `leopard_lying`, `lion_male`, `lioness`,
`lioness_walking`, `lioness_running`, `lioness_sitting`, `lioness_crouched`, `mongoose`, `pig`, `honeybee`, `ant_larva` (larvae in the
thought bubble), `beehive`, `beekeeper_suit`, `beekeeper_suit_stand`, `beekeeper_suit_on_back`, `hollow_tree` (wild bees' nest tree,
and the dead snag the goshawk perches on at night), `tree_branch`, `savanna_bush`, `safari_jeep`, `africa_map`, `field_guide_open`,
`narrator_hand_pencil`, `platform_scale` (WEIGH-IN icon and the leopard/Doug weighbridge), `balance_scale`, `bucket` (the 10-litre
bucket analogy), `swimming_pool` (as the Olympic pool), `finish_banner`, `alarm_clock`, `chalkboard`, `signboard`, `hand_saw`,
`journal_paper`, `stick_man_plain`, `scientist_woman`, `lion_head_icon`, `hyena_head_icon`, `dust_cloud`, `doug_cap`, `gravestone`, and
the annotation set (`question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`).

**Art director, one approval:** THE WEIGH-IN is a relabel of the library `platform_scale` (icon at 0.36, left of two size-28 labels
under the counter, with a small red needle line on the dial that steps up each item and hits the end stop at The Pride, where the
attacker label turns red `#ffd2cc` / `#e0201b`). Nothing needs drawing for it.

---

## The honey badger variants (same animal as library `honey_badger`)

### `honey_badger_swollen` (s002, s010, s016, s017)
- The library badger standing alert, head slightly raised and nose forward ("already looking for the next snake"). One near cheek
  is visibly puffed out: a smooth rounded bump in the same black, with a soft grey highlight so it reads. No wound, no fang marks.
- Anchor bottom-centre (feet on y 0). Footprint x -225..250, y -180..0, the same as `honey_badger`. Used at 0.9-0.95.

### `honey_badger_digging` (s048-s066, s157; 13 shots)
- Seen from the side, facing LEFT. Head and front legs are down in a hole at about local (-150, 0), so the face is hidden. The rump
  is up on the right with the white mantle arched and the stubby tail up. Front claws are kicking. Draw a small dark hole opening
  and a low dirt rim at the head end only; I add the flying dirt with sprays.
- Anchor bottom-centre on the ground line. Footprint x -230..230, y -220..+20 (the hole dips just below 0). Used at 0.7-1.0, on night
  sand `#5a4b3d` and on the dark pride ground `#4f3a2a`, so keep the white mantle bright and give the black body a mid-grey rim
  highlight.

### `honey_badger_climbing` (s030, s031, s033)
- Side view, clinging vertically to a tree trunk, head UP, claws hooked into the bark, tail hanging down. It is climbing toward the
  bees' nest above it.
- Anchor centre. Footprint x -100..100, y -210..210. Placed on `hollow_tree` (x 950, scale 0.8) at (950, 600), scale 0.65, so its
  head ends just under the hollow at (950, 482).

### `honey_badger_turned` (s077, s078, s084)
- The badger caught by the scruff. The loose skin is bunched and pulled up into a fold at the scruff grip point (+110, -170), the
  same point as on the plain `honey_badger`, which is where `grabbing_hand` grips. Inside that skin the body has twisted: the head
  turns back up and round toward the grip point, mouth open with white teeth facing the hand, not touching it. Add swirl lines at
  the shoulders to show that the skin stayed put while the body turned.
- No bite and no contact. Anchor bottom-centre. Footprint x -225..250, y -240..0.

### `honey_badger_sniffing` (s100, s120, s164)
- Walking slowly, head low and nose to the ground, with three small sniff lines in front of the nose.
- Anchor bottom-centre. Footprint x -225..250, y -170..0. Used at 0.5-0.8, under the wobbly hive stand, at cat tracks and at the cap.

### `honey_badger_charging` (s144, s148-s150)
- Full-tilt run: legs stretched fore and aft, body low, white mantle streaming, ears flat, mouth open with white teeth showing.
  It looks determined, not cute.
- Anchor bottom-centre (lowest paw on y 0). Footprint x -260..260, y -200..0. Used at 0.6-0.8 on the dark dirt road.

### `honey_badger_snarl` (s126, s127, s157)
- Standing braced, front end up a little, mantle fluffed up (hackles), tail up, mouth open with teeth, a "blur of teeth and fur"
  facing a lioness. Add a few short motion ticks around the body.
- Anchor bottom-centre. Footprint x -240..240, y -220..0.

### `honey_badger_swipe` (s151)
- Half-reared on its hind legs, facing right, one front paw swinging forward and up with pale claws (no red), mouth open growling.
  It is swinging at a young male lion's face, but the drawing has no contact.
- Anchor bottom-centre. Footprint x -210..210, y -300..0. Used at 0.85.

## Item 1: The Puff Adder

### `puff_adder` (s002, s005, s011-s013, s023, s079)
- A coiled puff adder (*Bitis arietans*) lying in ambush: thick, heavy body; straw-tan `#c9a86a` ground colour with bold dark
  brown-black chevrons pointing back along the body, each edged in pale yellow; a broad, flat, triangular head held low at the right;
  a short tail. Mouth closed, no fangs.
- Anchor bottom-centre. Footprint x -220..220, y -200..0. It must still read at 0.3 (a small icon in s079) and at 1.0 beside the bat.

### `puff_adder_held` (s021, s022)
- The same snake stretched almost straight, held horizontally at both ends with a slight sag in the middle. The thin tail tip is at
  the left end (-440, 0), where Doug's front hand is. The head is at the right (+440, -10), mouth closed and pointing right/down
  toward the badger at that end.
- Anchor centre. Footprint x -450..450, y -45..45. Placed at (860, 740), scale 0.9.

### `baseball_bat` (s011)
- A wooden baseball bat lying horizontal: pale wood `#d9b07a` with grain strokes, black grip tape on the thin handle (left), knob
  end, thick barrel (right).
- Anchor centre. Footprint x -430..430, y -35..35, the same length as the coiled adder's stretched body. It sits under it with a dotted
  line, at 1.0.

### `receptor_lock_diagram` (s006-s009, s014, s015)
- A crude MS Paint biology card on a transparent background:
  - the bottom half is a block of cartoon-pink muscle `#f4c6c4` with darker striation lines (top surface at y -40);
  - a lilac nerve ending comes down from the top centre to a rounded terminal bulb at (0, -230);
  - in the muscle's top surface at (0, -60) sits a big grey keyhole-shaped receptor socket (about 120 wide x 180 tall, dark
    interior).
- Leave a clear gap between bulb and keyhole (y -200..-120) for the toxin, and keep the keyhole centre clear for my red "+" overlay.
- Anchor centre. Footprint x -450..450, y -280..280. Placed at (800, 640), scale 0.95.

### `toxin_key` (s006, s007, s009, s014)
- The cobra-type nerve toxin as a purple `#8a4fbf` blob with a key-shaped prong sticking down (the shape that fits the keyhole). No
  face.
- Anchor centre. Footprint x -100..100, y -80..80. Also rotated -25 for "struggles to hold on".

### `receptor_keyhole_icon` (s018-s020)
- A small round pink badge with the same grey keyhole in the middle (the receptor in miniature). Keep the centre clear for a red "+"
  overlay or my white sugar-cube squares.
- Anchor centre. Footprint x -80..80, y -80..80. Used at 0.7-0.9.

### `hedgehog` (s018, s019)
- An African pygmy-type hedgehog, side view: brown-grey spines with cream tips, pale face and belly, dark nose, small dark eye,
  little feet. Calm, not cute.
- Anchor bottom-centre. Footprint x -160..160, y -200..0. Sits in a portrait box at 0.8, beside library `pig` (0.45) and `mongoose` (0.55).

## Item 2: The Hive

### `wild_honeycomb` (s025-s047; 12 shots)
- A wild bees' nest: three or four pale gold `#e9c25a` wax combs hanging vertically side by side, a few capped cells, some amber
  honey, and a few small bees on the comb.
- Anchor centre. Footprint x -90..90, y -110..110. It sits inside `hollow_tree`'s hollow (rx 90, ry 110 at local (0, -360)) at tree
  scale 0.8 and may bulge out of the hollow a little so it reads.

### `bee_cloud` (s025, s027, s030, s031, s045, s046)
- A loose angry swarm of 30-40 small honeybees (golden with dark bands and white wings) with scribbly motion loops. It is open, so the
  sky shows through: no dark blob, no black speckle.
- Anchor centre. Footprint x -260..260, y -180..180. Used at 0.4-0.6.

### `honeyguide` (s028, s029, s032, s035, s036, s047)
- A greater honeyguide (*Indicator indicator*) perched, facing right: drab brown-grey back, paler grey-white underside, white outer
  tail feathers, a small pink bill, and the male's black throat with a white cheek patch.
- Anchor at the feet on the perch (0, 0). Footprint x -100..100, y -170..0. Used at 0.6-0.7 on a branch and the tree top, and as a hero
  at 1.6 next to a drawn egg ("weighs about as much as an egg").

### `honeyguide_flying` (s033, s034, s040-s044)
- The same bird in flight, wings spread, white outer tail feathers fanned, facing right.
- Anchor centre. Footprint x -150..150, y -85..85. Used at 0.6-0.8.

### `yao_honey_hunter` (s041, s042)
- A crude-tier stick man in Doug's line weight (`auto_ink`), with no cap, short black hair and a plain shirt as a simple flat colour,
  so it is a generic man, not a likeness. Both hands are cupped at his mouth, calling. He faces LEFT.
- Anchor at the feet (0, 0), hips at (0, -150), about 450 tall like `stick_man_plain`. Used at 0.5. The "brrr-hm" speech tail points
  at his head (about (0, -400)).

## Item 3: The Jackal

### `pale_chanting_goshawk` (s051, s054, s056, s057, s060, s061, s068)
- Perched upright, facing right: pale grey head, back and breast; white belly finely barred with grey; long coral-red legs and a
  coral-red cere; dark eye; long grey tail. It must read on the night sky `#1b2f5a`, so keep the grey light.
- Anchor at the feet (0, 0). Footprint x -100..100, y -360..0. Used at 0.45-0.5 on top of `hollow_tree` (the dead snag), at 0.8 on a
  cream card, and at 0.35 as a follower.

### `gerbil` (s054)
- A Kalahari hairy-footed gerbil running, facing right: sandy orange-buff back, white belly, big dark eye, long tail with a small
  tuft.
- Anchor bottom-centre. Footprint x -100..100, y -90..0. Used at 0.6 on night sand.

### `jackal_with_gerbil` (s065, s067)
- The library `jackal` (same build and colours) trotting, facing right, with a whole gerbil held crosswise in its mouth: limp tail
  hanging, closed-line eyes, no blood.
- Anchor bottom-centre. Same footprint as `jackal` (x -225..225, y -270..0). Used at 0.6.

## Item 4: The Skin

### `badger_skin_cutaway` (s072-s074, s079)
- The badger's head and neck in profile facing right, with a crude cutaway window over the neck and throat. It shows a thick
  pale-pink skin band (about 30 units thick) over a darker body layer, and a loose fold of skin at the scruff.
- Put the thick throat skin at about (+80, +20), where my "6 MM" arrow lands. Put a visibly thin skin line on the belly edge at about
  (-60, +140), where the "BELLY: THIN" arrow lands.
- Cartoon anatomy only (flat colours, no flesh texture).
- Anchor centre. Footprint x -300..300, y -190..190. Used at 1.1-1.2.

### `hoodie_figure` (s075, s076)
- A crude-tier stick figure (Doug's line weight, `auto_ink`, no cap) in a hugely oversized plain grey hoodie, hood up, seen from
  the BACK, so no face shows. The sleeves hang past the hands and the hem reaches the knees.
- Anchor at the feet (0, 0). Footprint x -190..190, y -560..0, with the hood top at (0, -520).

### `hoodie_figure_turned` (s076)
- The same hoodie in exactly the same place and outline, hood still up, but the figure inside has turned round to face the viewer:
  a flat annoyed face in the hood opening. Add twist lines at the shoulders and waist (the fabric stayed, the person turned). The
  shotlist swaps it in over the first one.
- Same anchor and footprint.

### `grabbing_hand` (s068, s071, s076, s077, s084)
- A crude-tier arm entering HORIZONTALLY FROM THE LEFT: a white hand (`keep_ink`) closed in a pinch-grip fist, grabbing a fold at
  the anchor. A plain grey sleeve with a darker cuff runs left to x -1200, so it always reaches the frame edge.
- Anchor (0, 0) is the grip point. Footprint x -1200..60, y -50..50. Used at 0.6-0.7 on the badger's scruff and on the hood. It
  never comes down from the top (the caption bar is there).

## Item 5: The Leopard

### `cat_paw_print` (s100, s101)
- One big-cat track pressed into sand: four oval toe pads and a three-lobed palm pad, with no claw marks, in dark brown `#6b4a2a`
  with a slightly darker sand rim. It must read on the dusk ground `#9a7a4a`.
- Anchor centre. Footprint x -60..60, y -60..60. Used in a trail of four at 0.6.

### `leopard_pouncing` (s103)
- The library `leopard` (same coat and rosettes) dropping from a branch: body diagonal, head down-right, front legs reaching
  forward and down, tail up behind, ears back, mouth closed, no claws shown.
- Anchor centre. Footprint x -300..300, y -190..190. Placed at (1300, 560), scale 0.8, above Doug, who is cowering at x 1450.

## Item 6: The Beekeeper

### `hive_on_stand` (s114-s116, s118)
- The library `beehive` (same pale wooden Langstroth boxes) raised on a sturdy black steel stand about 1 m high (four splayed legs
  with a cross-brace), with an orange ratchet strap around the boxes.
- Anchor bottom-centre (feet on y 0). Footprint x -160..160, y -640..0. Used at 0.7-0.9. A badger at 0.5 stands under it looking up.

### `wobbly_hive_stand` (s119-s123)
- Doug's homemade stand: a crude wonky wooden table with four mismatched legs of different lengths and angles (one is just a stick),
  bent nails sticking out and a flat top surface at y -300. It is "legs only a cartoonist could love", but it must look like it
  stands. The library `beehive` sits on top (I place it at y -300 x scale).
- Leave at least 200 units of clear height under the top, because the badger walks under it.
- Anchor bottom-centre. Footprint x -170..170, y -300..0.

### `honey_jar` (s117)
- A glass jar of golden honey with a gold screw lid and a blank white rectangular label centred at (0, +20), about 220 x 120, for my
  "BADGER FRIENDLY" overlay.
- Anchor centre. Footprint x -150..150, y -190..190. Used at 1.2.

## Item 7: The Lion

### `stink_cloud` (s131-s134, s137)
- A green `#8fbf4a` cartoon smell cloud with a darker green swirl and three wavy stink lines rising from it. It is a gas puff, not a
  blob.
- Anchor centre. Footprint x -180..180, y -130..130. Used at 0.3-0.7 (badger tail, drifting to the safari vehicle, on the price list).

### `lion_male_leaning_back` (s140; the graphic designer may reuse it for the thumbnail)
- The library `lion_male` (same mane and colours) sitting back on its haunches, upper body leaning away, one front paw lifted, head
  pulled back with a flat, unimpressed stare, mouth closed. Facing right (the shotlist flips it to face the badger).
- Anchor bottom-centre. Footprint x -310..310, y -480..0. Used at 0.8.

## Item 8: The Pride and the closing

### `badger_burrow` (s004, s057, s100, s101, s152, s153, s158-s165; 13 shots)
- A honey badger burrow entrance in Kalahari sand, front view: a dark oval hole `#1a120c` at (0, -50), about 200 wide x 110 tall,
  with a fan-shaped apron of pale dug sand `#d9b06a` (darker spray) spreading in front and to the sides, and a few pebbles.
- Low profile. Anchor bottom-centre. Footprint x -260..260, y -140..+10.
- It must read on night sand `#5a4b3d`, dusk ground `#9a7a4a`, dawn ground `#8a6a4a` and the dark pride road `#6a5440`, so keep
  the apron pale.
- It is NOT the library `burrow`, which is a wasp burrow.
