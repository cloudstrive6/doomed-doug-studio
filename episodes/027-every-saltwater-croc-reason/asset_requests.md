# 027-every-saltwater-croc-reason: asset requests (director to illustrator / art director)

Library assets I reuse as they are: `saltwater_crocodile` (standing croc; also the Nile crocodile on the sensor and Menu cards, labelled), `croc_eyes_water`, `croc_head_rising` (the mother rising behind Doug at The Egg), `croc_jaws_open` (empty open mouth, never near Doug), `crocodile_skull`, `canoe`, `canoe_paddle`, `field_guide_open`, `australia_map`, `world_map`, `tree_branch`, `jetty`, `bathtub`, `small_car_driving`, `helicopter`, `torch`, `rubber_ring`, `calendar`, `clock`, `wait_stopwatch`, `tape_measure`, `fingertip`, `narrator_hand`, `fishing_rod`, `heart_icon`, `water_splash`, `water_splash_small`, `doug_cap`, `palm_tree`, `reeds`, `savanna_bush`, `flat_rock` (Doug's rock at The Legend), `kitchen_counter`, `sandwich`, `magnifying_glass`, `small_fish`, `journal_paper`, `scientist`, `scientist_woman`, `wildlife_official` (the ranger), `fishing_boat` (ranger boat), `rowboat`, `house`, `rosette_badge`, `banana`, `speedometer`, `highspeed_camera`, `finish_banner`, `thermometer`, `question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`.
**Not used, by brief rule:** `croc_log`, `croc_log_eye` (no log gag).

Drawn from primitives in the shotlist (no asset needed): field-guide name and NO stamps, the river/mangrove/dusk/night backgrounds, torch beams, ripples, water drops, the 100-dot hatchling chart, chicken eggs, coin, graphs, tally marks, the dark tank, the Queensland border, the range band on the world map, the spinning-top blur at The Roll, the "HUNTING" and "PROTECTED 1971" stamps.

## House rules for this episode (brief section 7, CD decisions)
- Detailed creature tier: thick black outline (5-6), flat fills with interior shading, readable at phone size. **Every crocodile matches `saltwater_crocodile.json`'s palette** (olive-grey hide `#6b7a4a`-ish, darker back, yellowish flanks/belly, yellow slit-pupil eye, bony scute rows) so they read as the same species.
- **No blood, no wounds, no prey with limbs, nothing in any mouth except the hatchling (small, not cute) and the plain grey shape.** Jaws are CLOSED in every new croc asset unless noted. Teeth never touch Doug: none of these assets include Doug.
- **No croc leaping its body length** (CD rule): `croc_lunge_rising` shows head and front third out of the water only.
- **Hatchlings: small, detailed tier, never cute**: small eyes, no big round pupils, no smile, never chubby.
- Sober-card assets (`myanmar_coast_map`, `record_book`, `record_book_open`, `old_book`, `indonesia_map`, `indonesia_map_ntt`) are plain and muted: no soldiers, no people, no logos, no readable titles. They sit on near-black `#15181a` / `#1a1d22`.
- Everything faces right unless noted (the shotlist flips). Keep to the bbox and anchor below: the shotlist is laid out against them (placeholder previews with these boxes are in `build/contact/`).

---

### mangrove_clump
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: a clump of mangrove trees on the far riverbank (the river backdrop in most items).
- Look: dense rounded dark-green canopy (`#2e5a2e` with lighter `#4a7a3a` leaf clusters) on several thin grey-brown trunks that split into arching **prop roots** standing in the water; muddy base. Must read on light sky (day), olive (mangrove shade) and dusk orange. Not a palm, not a pine.
- Anchor: bottom-centre at the waterline (roots dip to y +30). bbox x -250..250, y -420..30.
- Size: used at scale 0.27-0.35 along the horizon, and 0.9 as the framing tree at The Lunge.
- Shots (103): every river shot from s007 to s267 (backgrounds), plus the Lunge tree s195-s212.

### croc_jaw_closeup / croc_jaw_closeup_lit
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`. Neck edge at x -460.
- **ROUND 2 DONE** (illustrator, 2026-10-26, art review fix A): preview `assets/previews/027-every-saltwater-croc-reason-assets-r2.png`. Neck continues as one body (scale rows, nuchal scutes, belly band, jaw ends at a hinge) with no closing outline to x -1750 in both files; `_lit` geometry identical, glow dots still on the head only. New bbox x -1750..450, y -226..252.
- What: close-up of a saltwater crocodile's snout, side view, for the touch-sensor (ISO) beat.
- Look: the front half of the head, jaws closed, interlocking teeth along the jaw line, eye at the left edge (about (-300,-120)), nostril bump at the snout tip. **The jaw scales are covered in many tiny dark dots** (dome pressure receptors, `#2a2a20`, 4-6 px at scale 1), densest along the jaw edges. `_lit` is identical geometry with each dot **glowing yellow `#ffe24a`** (small solid dot plus a tight pale halo), so it can be overlaid on the plain one.
- Facing: right. Anchor centre. bbox x -450..450, y -190..190.
- Shots: plain s037-s040, s045, s046, s048, s053; lit s040, s053.

### saltwater_crocodile_lit
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: exactly `saltwater_crocodile` (same geometry, overlay-able) with yellow `#ffe24a` sensor dots on **almost every scale of the body** (not just the jaws).
- Anchor/bbox: same as `saltwater_crocodile` (bottom-centre, x -504..502, y -187..0).
- Shots: s044.

### alligator
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: American alligator, side view, for "alligators don't have them" and the sensor and roll studies.
- Look: darker and blacker than our croc (`#3a4232` with `#2a3024` back), broad rounded U-shaped snout, upper teeth only showing (lower teeth hidden), heavy scutes, pale cream belly line, yellow-green eye. Clearly different from `saltwater_crocodile` side by side.
- Facing: right. Anchor bottom-centre (feet on y=0). bbox x -490..490, y -180..0.
- Shots: s041, s042, s072, s218, s225, s227, s271, s272, s273.

### alligator_head_water
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets-small.png`.
- What: an alligator's head at the surface in a dark tank (single-drop experiment).
- Look: only the top of the head above the waterline: eye bumps with a yellow eye, snout ridge, nostrils; a darker shape under the water. Mid-tone fill (`#5a6a4a`) so it reads on near-black `#0c0f12`.
- Facing: right (shotlist flips it to face the ripples). Anchor centre on the waterline. bbox x -230..230, y -60..30.
- Shots: s050-s052.

### croc_tongue_closeup
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- **ROUND 2 DONE** (illustrator, 2026-10-26, fix A): preview `assets/previews/027-every-saltwater-croc-reason-assets-r2.png`. Jaw rims, 3 more teeth per side, gum, tongue (pores in the art director's grey) and throat run open-ended to x -1000. New bbox x -1000..400, y -240..240.
- What: close-up of the saltwater crocodile's tongue inside the open lower jaw (salt glands).
- Look: pale pink-yellow tongue `#f0c8a8` filling the middle, edged by the lower teeth row; **a neat row of tiny dark pores** (salt glands) across the tongue, a few tiny white specks leaving them. No blood, no food.
- Anchor centre. bbox x -400..400, y -220..220.
- Shots: s071.

### croc_swimming
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`. Bow ripple to x +462.
- What: a saltwater crocodile swimming at the surface, heading out to sea.
- Look: head (eye bump, nostrils) and back scutes just above the waterline; the body and tail visible as a darker olive shape just below the surface, tail mid-sweep; a small V wake behind the head. Jaws closed. Reads on bright sea blue `#3a9ad9` and on olive river water.
- Facing: right. Anchor centre on the waterline. bbox x -450..450, y -60..100.
- Shots: s076-s080, s089-s091, s093, s200.

### croc_nest_mound / croc_nest_cutaway
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`. Sticks poke to y -366.
- What: the female's nest: a tall mound of mud, leaves and plant material on a riverbank. `_cutaway` is the same mound cut open.
- Look: tall dome of dark mud `#5a4630` and dead leaves/grass (`#8a7a3a`, `#6b5a2a`), sticks poking out, a few green shoots; clearly a pile of vegetation, not a rock. `_cutaway`: the front third removed showing rows of **about 24 white elongated eggs** packed in the mound (white `#f4f1e8`, grey shading).
- Anchor: bottom-centre (ground y=0). bbox x -300..300, y -330..0 (same footprint for both).
- Shots: mound s094-s098, s104-s107, s110-s113, s117-s122; cutaway s099, s103.

### croc_egg
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets-small.png`.
- What: one saltwater crocodile egg (113 g).
- Look: elongated chalky white oval (both ends round), faint grey shading on one side and a few rough chalky specks. No face.
- Anchor centre, upright. bbox x -70..70, y -110..110.
- Shots: s101, s102.

### egg_carton
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets-small.png`.
- What: an open cardboard dozen egg carton with 12 white chicken eggs.
- Look: grey-beige carton `#c9c0ad` in a low 3/4 view, lid open behind, two rows of six eggs.
- Anchor centre. bbox x -140..140, y -60..60.
- Shots: s100 (4 cartons in a row).

### croc_mother_hatchling
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- **ROUND 2 DONE** (illustrator, 2026-10-26, fix A): preview `assets/previews/027-every-saltwater-croc-reason-assets-r2.png`. Neck and shoulder continue open-ended to x -1000, with nuchal scutes and osteoderm rows, and the throat band slopes down to the ground line (y 0..8). New bbox x -1000..350, y -395..8.
- What: the mother's head in profile carrying a hatchling in her closed jaws.
- Look: saltwater croc head and neck, **jaws closed**, a small hatchling (yellowish-grey with dark bands) just visible between/behind the teeth near the middle of the jaw, head poking out. Gentle, not menacing; hatchling small, not cute.
- Facing: right. Anchor bottom-centre (lower jaw on y=0). bbox x -350..350, y -330..0.
- Shots: s114, s115.

### croc_hatchling
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets-small.png`.
- What: a saltwater crocodile hatchling.
- Look: small, slim, yellowish-tan `#c9b06a` with dark grey cross-bands on body and tail, small yellow eye, closed jaw. Not cute: no big eyes, no smile.
- Facing: right. Anchor bottom-centre. bbox x -150..150, y -80..0.
- Shots: s116, s119, s121, s142 (tiny, on the 1914 calendar page).

### croc_sleeping
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: a huge male lying asleep on a mudbank (The Size).
- Look: same body as `saltwater_crocodile` but lying flat on its belly, legs splayed out to the sides, **eye closed (a curved line)**, jaw closed, relaxed tail. Back legs at about local x -150 (the tape stops there).
- Facing: right. Anchor bottom-centre (belly on y=0). bbox x -504..502, y -170..0.
- Shots: s124-s126, s138, s143-s152.

### croc_in_sling
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: a crocodile being lifted in a cargo sling under a helicopter (relocation study).
- Look: croc lying horizontal inside canvas straps/net, jaws taped closed with a band, two ropes rising from the sling to meet at a hook at the top.
- Anchor: the hook (0,0); croc body hangs at y +250..+420. bbox x -400..400, y 0..420.
- Shots: s154, s175, s176.

### cape_york_map
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: map of the Cape York Peninsula (world_map style: flat green land, dark outline, light-blue sea `#bfe6ff`, black frame, no labels).
- Look/coordinates: equirectangular **lon 140.0..145.0 E, lat 10.0..15.0 S**, 160 px per degree, anchor (0,0) at lon 142.5 / lat -12.5: `x = (lon - 142.5) * 160`, `y = -(lat + 12.5) * 160`. Show the peninsula tip at about (142.5, -10.7), the west (Gulf) coast at about lon 141.6-141.9 between lat -11.5 and -13, the east coast at about lon 143.0-143.6 between lat -11.4 and -13.7, and a few Torres Strait island dots north of the tip. The shotlist draws the route over these points, so the coast must pass near them.
- Anchor centre. bbox x -400..400, y -400..400 (with frame).
- Shots: s160-s165, s168-s172, s177.

### car_trailer
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets-small.png`.
- What: a small open box trailer towed by Doug's car, carrying a crocodile.
- Look: grey-blue steel box trailer, low sides, one wheel visible, tow bar pointing right to about (+240,-40). Flat bed top at y -100 so a croc can lie on it. Empty.
- Facing: right (tow bar right). Anchor bottom-centre (wheel bottom). bbox x -200..240, y -150..0.
- Shots: s178, s179.

### bathtub_croc
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`. Rim at (-180,-80) left clear for doug_cap.
- **ROUND 2 DONE** (illustrator, 2026-10-26, fix B): preview `assets/previews/027-every-saltwater-croc-reason-assets-r2.png`. The boxy back of the head is now a sloping neck with nuchal scutes, running down from behind the eye into the body line. The old hump behind the head is removed. Rim at (-180,-80) is still clear. The bbox is unchanged.
- What: the library `bathtub` with a crocodile lying in it (The Home death and outro callback).
- Look: identical tub geometry; water line just under the rim; the croc's snout and eye bump over the right rim (jaws closed), tail tip over the left rim, scutes along the middle at the water surface. The shotlist places `doug_cap` floating in the tub at about local (-180,-80).
- Anchor/bbox: same as `bathtub` (centre) plus the head rising to y -210: x -334..334, y -210..129.
- Shots: s181, s183-s185, s329.

### croc_bounding
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: a small young crocodile bounding/galloping on land (Hutchinson 2019 beat).
- Look: slim young croc (lighter, banded), back arched, all four legs off the ground mid-bound, tail lifted, jaws closed. Small and light, not a giant.
- Facing: right. Anchor bottom-centre. bbox x -300..300, y -220..0.
- Shots: s190-s193.

### croc_coiled_underwater
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: a crocodile underwater below the branch, body bent, tail curled, ready to push (The Lunge).
- Look: side view, body in a shallow S, head angled slightly up toward the surface, jaws closed, **thick muscular tail curled back**. Mid-tone olive so it reads in murky `#4f5e3a` water (also used as a silhouette with a red rim first).
- Facing: right. Anchor centre. bbox x -400..400, y -160..160.
- Shots: s197-s199, s206, s212.

### croc_lunge_rising
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`. Top at y -320 (only the front third is out of the water).
- What: the diagram lunge: the crocodile rising out of the water toward a low branch.
- Look: **head and front third of the body out of the water, angled up-left (toward a branch on the left), jaws CLOSED**, front legs tucked; the rest of the body and tail submerged as a darker shape, tail sweeping; a splash collar at the waterline. Never the whole body in the air (CD rule).
- Facing: rising up and to the LEFT. Anchor centre on the waterline. bbox x -350..300, y -380..150.
- Shots: s201.

### croc_holding_shape
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`. Snout ripple to x +440.
- **ROUND 2 DONE** (illustrator, 2026-10-26, fix C): preview `assets/previews/027-every-saltwater-croc-reason-assets-r2.png`. The grey oblong now crosses the closed jaw line: it pokes above the snout and below the lower jaw, and the upper jaw fill, upper teeth, jaw line and top outline are drawn over it. Same sloped neck as fix B. The dark rectangle is gone: the submerged body runs under the head instead. The head is raised 22 units. New bbox x -400..440, y -100..50.
- What: a crocodile at the surface holding something too big to swallow (The Roll).
- Look: croc head and back at the surface, jaws closed around a **plain grey oblong shape `#8a8f96`** (no limbs, no features, no colour, clearly "undefined thing"). Water ripples around.
- Facing: right. Anchor centre on the waterline. bbox x -400..400, y -100..100.
- Shots: s213, s214, s216, s229-s231.

### croc_top_c
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`. bbox x -155..155, y -296..282.
- What: a crocodile seen from directly above, bent into a C-curve (death-roll mechanics diagram).
- Look: top view: head curved to one side, tail curved to the other, the body a C (banana) shape; **legs folded flat against the sides**; scute rows down the back. Works on a dark slate diagram background `#2a3040`.
- Anchor centre. bbox x -300..300, y -300..300.
- Shots: s217, s219-s224.

### thin_snout_croc
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: a generic thin-snouted crocodilian (stands in for "thin-snouted species").
- Look: like our croc but with a **very long, narrow snout** and many fine teeth; slimmer body. No bulbous nose knob (keep it generic, not a gharial).
- Facing: right. Anchor bottom-centre. bbox x -500..500, y -180..0.
- Shots: s225-s227.

### spinning_top
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets-small.png`.
- What: a classic toy spinning top (Doug's "dance" idea).
- Look: red and yellow striped wooden top, pointed tip down, short handle on top, two curved motion lines.
- Anchor centre. bbox x -100..100, y -120..120.
- Shots: s232, s237.

### croc_eyeshine
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets-small.png`.
- What: a pair of crocodile eyes shining in torchlight on black water.
- Look: two bright amber-orange `#ffb347` dots with white centres and a soft glow, side by side about 50 units apart, a faint ripple line under them. Must read on near-black `#0b0d10`.
- Anchor centre. bbox x -60..60, y -20..20.
- Shots (15): s239, s268-s270, s288, s291, s293, s295, s302, s316, s318-s323.

### croc_trap_floating
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets-small.png`.
- What: the NT rangers' floating crocodile trap.
- Look: a long horizontal cylindrical cage of silver-grey mesh bars, a door at the right end, sitting on two yellow floats, lower third under the waterline. **Drawn as bars only (see-through)**: the shotlist puts `doug_cap` inside at about local (0,-30), so the cap must show through.
- Facing: door right. Anchor centre on the waterline. bbox x -300..300, y -140..80.
- Shots: s003, s004, s313-s315, s324-s326, s328.

### city_skyline_small / city_skyline_night
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: Darwin-like small city skyline across the harbour (no landmarks, no text).
- Look: a modest row of 8-12 mid-rise towers (6-15 storeys) and lower buildings, a few palms; low profile. Day: pale greys and sand colours with blue windows. Night: same geometry, dark navy `#1a2238` buildings with scattered warm yellow lit windows.
- Anchor bottom-centre (waterline). bbox x -700..700, **y -240..0 (keep it low: the sky above carries labels)**.
- Shots: small s003, s004, s306, s313-s315, s324-s328; night s316-s323.

### myanmar_coast_map
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: sober-card map of the coast of Rakhine (Myanmar) with Ramree Island.
- Look: muted, plain: land `#4a5a48`, sea `#2a3440`, thin pale outline; Ramree Island clearly outlined just off the coast, its mangrove swamp shaded with a darker green hatch `#2f3f2f`; one thin tidal creek line on the island. No labels, no soldiers, no crocodiles, no arrows.
- Anchor centre. bbox x -500..500, y -375..375.
- Shots: s243-s246, s251, s255.

### record_book / record_book_open
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png (open) + 027-every-saltwater-croc-reason-assets-small.png (closed)`.
- What: the "famous record book" (generic: never a real brand or logo).
- Look: closed: big dark-green hardback with a gold border and gold page edges, no readable title. Open: same book open flat, cream pages with grey text lines, **a clear empty margin on the right page around local (+230, 0)** (the shotlist writes "DOUBT" there and a crossed-out number in the middle).
- Anchor centre. Closed bbox x -150..150, y -190..190; open bbox x -300..300, y -190..190.
- Shots: closed s240-s242, s259, s260, s263-s265; open s248, s258, s262, s266.

### old_book
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets-small.png`.
- What: a plain old hardback (the 1962 naturalist's book; the military histories).
- Look: plain brown cloth hardback, slightly worn corners, no text, no stickers, no cobweb (sober card).
- Anchor centre. bbox x -110..110, y -150..150.
- Shots: s246, s251, s252.

### indonesia_map / indonesia_map_ntt
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png (map) + 027-every-saltwater-croc-reason-assets-small.png (ntt overlay)`.
- What: sober-card map of Indonesia for the attack study.
- Look: world_map style but muted for a dark card: land `#5a6a58`, sea `#2a3440`, outline pale. Sumatra, Java, Borneo, Sulawesi, the Lesser Sunda chain, Timor, New Guinea's west. `_ntt`: identical geometry with only **East Nusa Tenggara** (Flores, Sumba, west Timor and the small islands between) filled orange `#ff8a3a` with a white outline, everything else transparent (it is overlaid on the plain map).
- Anchor centre. bbox x -700..700, y -300..300.
- Shots: s279-s283.

### nt_map_sepia
- **DONE** (illustrator, 2026-10-26): preview `assets/previews/027-every-saltwater-croc-reason-assets.png`.
- What: old-map style map of the Northern Territory for the hunting history.
- Look: sepia parchment tones (`#d9c8a0` land, `#c9b48a` sea, brown `#5a4630` ink outline), the Northern Territory outline with its coast, Arnhem Land and the Top End rivers drawn as thin ink lines; the rest of Australia faint. No labels, no rifles, no animals.
- Anchor centre. bbox x -400..400, y -400..400.
- Shots: s296-s301, s303-s305, s309.
