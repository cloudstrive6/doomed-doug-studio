# Art review: 014 What Dying From Every Brain Parasite Would Feel Like (new library assets)

Reviewer: art director. Scope: the 25 new assets in `asset_requests.md`, checked against `channel/art_bible.md`,
style bible section 7 (Art Director rules 1-9) and the request specs (anchors, bboxes, key points, stated backgrounds, tone).

How it was checked:
- `python -m studio asset-preview` for all 25 (`assets/previews/014-ad-review-1/2/3.png`, after fixes `014-ad-review-fixed.png`).
- Each asset was rendered at scale 1 on its brief backgrounds (pond green `#7fae8e`, cream `#f6ecd2`, grass gold, flesh
  pink `#f4c6c4`, maroon `#5a1a24`/`#7a2232`, near-black `#120a0c`, night navy `#2b2f4a`, as relevant), with the requested
  bbox and key points overlaid, and at 0.3 and 0.12 for small-scale reads.
- I measured the rendered pixel extent of every asset against its bbox. Allowing for boil and wobble (up to 6 px), all of them fit
  except `sheep_costume`, which overshoots on purpose (see below).
- Both costumes were rendered on Doug in every pose the shotlist uses with them. I also rendered keyframes s011, s025,
  s059, s064, s083, s224 and s254 to see the assets in context.

## Fixes I made directly (in `assets/library/`)
1. **`sheep`**: two wool-shading sprays, (-30,-110) r60 and (-140,-125) r40, leaked out under the fleece outline as a grey
   speckle patch on the grass between the legs, which looked like a dirty smudge. I moved them to (-30,-150) r50 and (-140,-145) r35.
   The shading now stays inside the fleece.
2. **`worm_icon`, `worm_suitcase`, `worm_boots`**: the `#f2b8b8` worm on the band-2 flesh pink `#f4c6c4` (s108, s113,
   s169, s171, s172, s190) only showed up through its thin outline and almost disappeared at 0.15-0.4. I changed the outline from
   `#a05050` width 5 to `#8a3e3e` width 7 in all three, so the worm is still identical across them. It now reads on flesh pink, cream,
   maroon, near-black and cap red at 0.1-0.4. Fill, shape and highlight are unchanged, and there is still no face or segments.
3. **`balamuthia_amoeba`**: the illustrator's concern was right. A single round nucleus in the dead centre of the blob, with a dark
   pupil-like nucleolus, read as a cyclops eye at the s224 hero scale (1.6). I moved the nucleus off-centre to (-18,+12) at rx 32 / ry 25,
   and shrank and softened the nucleolus (7x6 at (-11,+8), mid-brown `#7a6646` instead of `#4a3a28`). It now reads as a cell, not a face.
   Size, colour and anchor are unchanged.

## Per-asset verdicts
| Asset | Verdict | Notes |
|---|---|---|
| `killifish` | PASS | Slim silver killifish, olive back, faint bars, rounded tail, blunt head. Eye on (+95,-10). Head-top area is light silver, so cysts read (s011 checked). Reads on pond green and cream. |
| `killifish_costume` | PASS | Felt suit, zipper, bars, white belly panel, tail fin and dorsal fin. Head, face and cap fully clear. I approve the sewn button eye: it sells "homemade fish suit" and sits on the shoulder, well away from Doug's face. Good object silhouette for the pile. |
| `horn_snail` | PASS | Tall ribbed spire with a pale rim, dark foot. Reads on mud `#8a7a5a`. |
| `heron` | PASS | S-neck, dagger bill, white face, black stripe and plume, rusty thighs, shaggy breast. Bill tip exactly on (+170,-560). Silhouette (legs + S-neck + bill) is unmistakable. |
| `royal_albert_hall` | PASS | Oval red-brick drum, terracotta frieze, glass dome, arched porch. Recognisable at 510 px. |
| `grass_blade` | PASS | Tip exactly on (+20,-720), midrib, base tuft. Reads on dusk orange, night navy and pale yellow. Cap-on-tip checked in s059. |
| `fluke_icon` | PASS | Lancet shape, pale cream-pink, gut branches, suckers sit inline along the body axis, so no face reading. |
| `cow` | PASS | Hereford colours, polled head with a short horn, tail tuft. Muzzle on (+300,-250). Night silhouette reads as cow. |
| `sheep` | PASS (fixed, see 1) | Suffolk dark face and legs, drooping ear, calm. Muzzle on (+205,-190). |
| `sheep_head_outline` | PASS | Plain diagram head, no interior. The cyst zone at (-40,-60) r110 is completely clear. |
| `sheep_costume` | PASS | Cloud-bump onesie, hoof mittens and boots, hood behind the head with two dark ears. Face and cap visible. **I accept the top at y -292** (above the -190 bbox) because the ears have to reach the cap. In every shot it is used in, the overshoot stays clear of the counter zone (highest case is s071/s081: top at about y 600). |
| `sheepdog` | PASS | Black-and-white collie, blaze, white ruff and chest, low feathered tail. The belly at (-20,-120) is plain black and the s064 tapeworm overlay reads on it (checked). Advisory for future reuse, not blocking: the flank is a flat black slab with only one highlight line, which is on the thin side for the detailed tier. |
| `slug` | PASS | Spotted grey-brown, mantle saddle, eye tentacles, highlight. No face, not slimy. |
| `worm_icon` | PASS (fixed, see 2) | Plain S nematode, no face, mouth or segments. Rotate 180 still reads as belly-up. |
| `worm_suitcase` | PASS (fixed, see 2) | Same worm holding a tiny `#a0522d` hard-shell case. Rendered extent is 172x101, inside the bbox. |
| `worm_boots` | PASS (fixed, see 2) | Same worm in two brown hiking boots, mid-stride. |
| `tapeworm` | PASS | Cream ribbon in S loops, segments widening toward the tail, tiny knob head. Diagram style, no gut. |
| `pork_chop` | PASS | Pink meat, white fat rim, bone. Clean grocery icon, no blood. Reads on flesh pink thanks to the fat rim and outline. |
| `salad_bowl` | PASS | White bowl, mixed leaves, cherry tomatoes, cucumber, red leaf. Clearly a salad, not 013's lettuce head. |
| `frog` | PASS | Green with spots, cream belly, gold eye, no smile. |
| `compost_heap` | PASS | Mid-brown mound, straw, peelings and leaves. Reads on maroon, paddock brown and near-black. |
| `horse` | PASS | Chestnut, dark mane and tail, white blaze, dark hooves, soft-browed calm eye. Eye on (+250,-470), mouth on (+330,-360). No sores, no distress. |
| `mandrill` | PASS | Olive fur, red nose stripe, blue ridged cheeks, yellow beard. Silhouette is a hunched primate with a muzzle and a readable arm and leg gap. Reads on near-black. |
| `balamuthia_amoeba` | PASS (fixed, see 3) | Tan-grey (never lilac), pseudopods, granules, vacuoles. Plain and small at 0.12 on near-black. |
| `flowerpot` | PASS | Terracotta, rim band, soil top on (0,-215). The cap sits correctly in s254 and the pot reads on near-black. |

Tone check (brief section 7): no faces on parasites, no anatomical brains or tissue, no wounds or blood. Animals are documentary,
not cute (no lashes, blush or smiles). The horse, sheep and killifish show no suffering. Two-tier rule holds: the detailed-tier
creatures and props sit clearly apart from crude Doug.

## For the director (composition, does not block assets)
The costumes cover Doug's arms and stick legs, so some poses leave rig lines sticking out of the suit:
1. **s082** (`sheep_costume`, `walk1/walk2`): Doug's stick feet poke out past the boots, and the walk lean shifts his head
   away from the hood, leaving a gap. Use `stand` and carry the walk with the red dotted circle path, or a hop between two
   positions across consecutive shots.
2. **s083** (`sheep_costume`, `wave`): the raised forearm comes out of the woolly shoulder as a bare stick. Use `stand` or `hands_hips`,
   which hide the arms cleanly. The "hi friend?" bubble already carries the greeting.
3. **s025-s026** (`killifish_costume`, `['arms_up','hands_hips']`): `arms_up` shows two short stick stubs above the suit's shoulders.
   At scale 0.6 they are small and partly hidden by the splash, so this is advisory. For a clean shimmy, use `stand` and keep the
   motion lines and splash.
4. s075 (`think`) is fine: the hand-to-chin is hidden and the frame reads as `stand`.

ASSETS: PASS
