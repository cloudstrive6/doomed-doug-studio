# 018 asset requests (director → illustrator)

40 new drawings. The shotlist already uses these names. Coordinates are **local units at scale 1**, and the
shotlist positions arrows, rings and labels on them, so please keep each listed anchor / key point. If you move a
point, note it here and I'll re-aim the arrows. House style: detailed tier for creatures and props, outlines 4-6,
flat fills plus spray shading, readable at phone size. **Kid-appeal rule (CD):** chicks are never cute. No big
eyes, no blush, no rounded baby proportions. They read as small, scruffy, detailed field-guide birds.

Reuse the existing `cassowary` (bottom-centre, 370x604, head ~(110,-545), casque top (90,-612), beak tip
(194,-534), inner-toe claw ~(150,-25)) as the model sheet for every cassowary variant below: the same palette
(near-black shaggy plumage, bright-blue neck `#3a7bd5`/`#3fc6cf`, red nape and wattles, brown horn casque
`#8a6436`, amber eye, grey scaly legs).

## Cassowary variants (all face RIGHT, anchor bottom-centre = feet on y=0 unless stated)

| name | what / look | key points | shots |
|---|---|---|---|
| `cassowary_head` | Side-view close-up of the head and upper neck: tall brown casque, amber eye under a heavy brow, dark beak, bare bright-blue neck with the red nape patch, two red wattles hanging at the throat, a fringe of black shaggy feathers at the bottom. **Anchor centre**, ~520x620 | casque top (-10,-280), casque centre (0,-200), eye (40,-110), beak tip (230,-80), wattles (+60,+60), neck bottom y +320 | s027 s028 s033 s034 s044 s103 s104 |
| `casque_cutaway` | Diagram cutaway of the casque on a stub of head: smooth brown keratin outer shell drawn as a thick band, inside it a pale-cream honeycomb of bony struts at the lower front, an EMPTY dark-cream space at the back, thin red blood-vessel lines threading through. Textbook-diagram feel, no gore. **Anchor centre**, ~640x520 | shell edge top (0,-240) and front (+50,-230), honeycomb (+90,+60), empty space (-120,-30), vessels around (+40,+150), base y +240 | s030 s031 s035 s042 s043 |
| `cassowary_thermal_cold` | Exactly the `cassowary` pose and outline as a thermal-camera image: whole bird in cold blues/purples (`#2a3a8a`, `#4a5ad0`), with the casque just as cold (deep blue) as the rest. Made for a near-black `#1b1b3a` background | casque (90,-590) | s038 s040 |
| `cassowary_thermal_hot` | Same thermal bird, body warm-orange/magenta and the **casque glowing yellow-white** (`#fff3b0` core, orange `#ff8a2a` rim spray) so it clearly reads as the hottest part | casque (90,-590) | s041 s045 |
| `cassowary_swallow` | Standing bird with its head tipped up, beak pointing at the sky, and a round fruit-shaped lump halfway down the blue neck | beak tip ~(150,-680), lump (100,-470) | s053 s068 s069 |
| `cassowary_swallow_cap` | Identical to `cassowary_swallow`, but the lump is cap-shaped, with a small red curve of Doug's cap brim showing through the blue neck skin, so it reads as "swallowed the cap" (outro). No other changes | lump (100,-470) | s260 |
| `cassowary_head_down` | Feeding/inspecting pose: body level, neck lowered forward so the beak is near the ground and the casque leads | beak tip (+230,-30), casque (+200,-110); ~470x450 | s052 s163 s229 s231 s259 |
| `cassowary_running` | Mid-stride sprint: body lower and leaning forward, neck forward, one leg stretched forward and one back, feathers streaming back, two motion strokes behind. ~560x560 | casque ~(+190,-480) | s029 s165 s167 s169 s170 s172 s175 s177 s179 |
| `cassowary_kick` | Bird standing on its back leg, front leg swung forward and down mid-kick, inner-toe claw leading, wings tucked. Defensive and side-on, no contact, no victim | kicking foot claw at ~(+260,-250); ~600x620 | s235 s236 s237 |
| `cassowary_wing_raised` | The `cassowary` with its near-side stubby wing lifted outward from the body to show **4 long black quills** fanning out and a small curved claw at the wing tip | quill tips around (-200,-470), claw ~(-150,-420) | s113 |
| `cassowary_swimming` | Only head, casque and bright-blue neck above the water, with a dark hump of the back just under the surface and a V wake/ripple ring. **Anchor = the waterline at the neck base (0,0)** | head top ~(+60,-330) | s140 s145 s146 s149 s150 s156 |
| `casque_fin` | Just the brown casque tip (and a sliver of blue head) cutting through the water like a shark fin, with a small V wake. Must read as "fin?" first and "casque" on a second look. **Anchor = waterline centre**, ~180x150. Also used as a `silhouette` with a red `rim` | | s158 s159 |
| `cassowary_on_nest` | Male sitting low on a leaf-litter nest, body fluffed over the eggs, one big green egg peeking out at the front edge, neck up and alert. ~620x480 | | s117-s119 s123-s127 |
| `cassowary_icon` | Tiny simplified cassowary for crowds and counts: black body blob, blue neck, red wattle dot, brown casque, two grey legs. Must read at 40 px. **Bottom-centre**, ~60x90 | | s059 s064 s078 s081 s082 s122 s154 |
| `cassowary_chick` | Juvenile, striped lengthways in cream and dark brown, long legs, no casque, beady eye. **Not cute** (see rule above). Bottom-centre, ~180x200 | | s128-s139 s194 s195 s205 s206 s248 |
| `cassowary_chick_brown` | Same juvenile a few months older: plain scruffy brown, stripes gone, tiny casque bump, slightly taller. Bottom-centre, ~200x230 | | s132 |

## The Quills (the CD flagged these three)

| name | what / look | key points | shots |
|---|---|---|---|
| `cassowary_double_feather` | One cassowary body feather drawn big: **two long, loose, hair-like black shafts of similar length growing in a "V" from one short base**. Strands are loose (no smooth vane), with glossy grey highlights. **Anchor centre**, ~300x520 | base (0,+240), shaft tips (-90,-240) and (+90,-240) | s100 s101 s102 |
| `cassowary_wing_quills` | Close-up of the wing: a stubby wing almost buried in shaggy black body feathers (left), with **4 long, slightly curved, glossy black quills** (bare shafts, no vanes, like knitting needles) sweeping out to the right. **Anchor centre**, ~700x500. Also used as a `silhouette` | quill tips ~(+320,-150), (+330,-60), (+320,+30), (+300,+120) | s106-s109 |
| `cassowary_wing_xray` | X-ray of the same wing for a dark navy `#0d1b2a` background, in the style of `tiger_shark_xray` / `moray_xray`: pale-cyan `#9fe6ff` bones (humerus, forearm, short hand), faint feather outlines, and digit 2 ending in a **curved claw** that is brighter/thicker so it pops. Transparent background. **Anchor centre**, ~700x400 | claw (+260,-40) | s110 s111 |

## Props, places, people

| name | what / look | key points | shots |
|---|---|---|---|
| `piano_keyboard` | Straight-on piano keyboard strip (top view of the keys): ~52 white keys with black keys in 2-3 groups, dark wood cheek blocks at each end. **Anchor centre**, ~1400x300 | leftmost white key centre (-675,+60) | s010-s013 |
| `cassowary_plum` | Cassowary plum (*Cerbera floribunda*): smooth oval fruit, glossy purplish-blue `#4a3a9a` with a lighter highlight and a small brown stem nub. **Anchor centre**, ~240x150 lying horizontally | | s051 s060-s069 |
| `cassowary_footprint` | One three-toed cassowary footprint pressed into soil, toes pointing up (-y): three thick toe marks, the inner one with a claw nick. **Anchor centre**, ~120x140 | | s056 s064 s258-s265 |
| `narrator_hand` | The narrator's flat, drawn human arm and hand reaching into frame from the top right (crude-tier lines, plain grey shirt cuff, no face), fingers open as if just placing something. **Anchor = the fingertips (0,0)**; the arm runs up-right to about (+700,-600), off-screen | | s066 |
| `cassowary_sign` | Australian yellow diamond warning sign with a black cassowary silhouette (casque visible), on a grey post. **Anchor = foot of the post on the ground (0,0)**. Diamond centre (0,-420), 300 wide; ~320x580 | | s073 s074 s083 s089-s095 |
| `sydney_opera_house` | Crude but recognisable Sydney Opera House: white sail shells with grey shading lines, cream podium base. **Bottom-centre**, ~900x420 | | s080-s082 |
| `tree_stump` | Rainforest tree stump: brown bark, pale cut top with rings, a few roots. **Bottom-centre**, top surface at y -150 (Doug stands on it), ~260x160 | | s046-s048 s112-s115 |
| `cassowary_nest` | Low, flattened nest of leaf litter on the forest floor, **empty** (I place the eggs and the cap on it myself). **Bottom-centre**, ~520x160, top hollow at y -70 | | s120 s122 s134 s208 s209 |
| `cassowary_egg` | Large glossy pale-green to dark-green egg, upright oval, slightly granular texture dots. **Anchor centre**, ~150x200 | | s120-s122 s134 s188 s191 s192 s194 s201 s202 |
| `soccer_ball` | Classic black-and-white football. **Anchor centre**, r ~110 | | s121 |
| `balance_scale` | Simple balance scale: grey base and post, a level beam, two flat pans hanging on short chains. **Bottom-centre**, ~800x500. Pans are level, and their top surfaces are at (-280,-220) and (+280,-220) (things sit there) | | s121 s143 s144 s198 |
| `rice_bag` | Big white woven rice sack with a blue band and plain text "RICE 10 KG". **Bottom-centre**, ~140x190 | | s144 s198 |
| `camper` | Crude-tier stick person in Doug's style (5 px lines, round head with grey crescent), **no cap**, short hair, t-shirt and shorts, front arm pointing forward. `auto_ink: true`. Anchor hips, feet +150 | | s148-s151 s153 |
| `rock_shelter` | New Guinea highland rock shelter: a big grey-brown rock overhang with a dark hollow underneath, a flat dirt floor, ferns at the edges. **Bottom-centre**, ~1200x700. Overhang underside at y -420; interior about x -400..+300 | | s186 s188 s194 s195 s197 s203 |
| `eggshell_fragments` | Pile of curved green-grey cassowary eggshell fragments (about 15 pieces, granular outer surface, paler inside), a few lying concave-up. **Anchor centre**, ~360x140 | | s189 s190 s193 |
| `ancient_person` | Crude-tier stick person (Doug's tier, `auto_ink: true`), no cap, plain brown wrap and a string bag, neutral face. **Not** a caricature: just a person. Anchor hips, feet +150 | | s188 s194 s195 s203 |
| `chicken` | Ordinary farmyard chicken, red comb, white/brown feathers, facing right. **Bottom-centre**, ~260x280 | | s202 |
| `paring_knife` | Kitchen paring knife lying horizontally, blade to the right: steel blade ~260 long from x -40 to +220, black handle. Plain kitchen tool, no blood. **Anchor centre**, ~420x70 | | s217 |
| `deinonychus_foot` | Fossil-skeleton foot of *Deinonychus* (off-white bone `#f4ecd8`, grey outline, for the dark museum `#2c3350` and the dark slate `#1e2622`): the long foot bones and three main toes, with **toe 2 raised and carrying the big curved sickle claw**. **Bottom-centre**, ~450x320 | claw tip (+230,-140) | s219 s221 s222 s224 s225 s226 |
| `plaster_claw_cast` | Museum plaster cast of a raptor sickle claw: chalky white, curved, on a small square base with a tiny paper label. **Anchor centre**, ~150x200 | | s227-s229 s231 |
| `seedling_cap` | **Closing image.** A young rainforest seedling growing out of a small fresh soil mound on the forest floor, with Doug's tiny red cap (exact `doug_cap` shape) sitting on top of the stem like a hat. Two or three broad leaves. **Bottom-centre**, ~240x420. It must read as *planted* (a tree growing where the bird left the seed). No dung pile and no bathroom cue: just clean soil and a seedling. **Fallback (CD note):** if it doesn't read as planted at phone size, the art director swaps s261/s262/s265 to `doug_cap` lying beside the line of footprints and tells me | | s261 s262 s265 |

Existing library assets reused: `cassowary`, `cassowary_foot`, `field_guide(_open)`, `small_car`, `small_plant`,
`australia_map`, `rainforest_tree`, `fern`, `leaf`, `fallen_log`, `doug_cap`, `dust_cloud`, `dust_plume`,
`phone`, `calendar`, `clock`, `thermometer`, `magnifying_glass`, `bank_card`, `heart_icon`, `pencil`,
`songbird`, `pigeon`, `large_dog`, `african_bush_elephant`, `scientist`, `messel_turtle`, `shark_fin`,
`water_splash(_small)`, `birdseed_bag`, `campfire`, `feathered_dinosaur`, `dinosaur_skeleton`, `falcon`,
annotation set.
