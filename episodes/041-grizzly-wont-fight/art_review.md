# 041 art review: new assets (art director, 2026-11-09)

Reviewed: `assets/previews/041-grizzly-wont-fight-assets-creatures.png`, `041-grizzly-wont-fight-creatures-check.png`
(light/dark/red-glow silhouette), `041-assets-props-b.png`, `041-porcupine-costume-on-doug.png`,
`041-grizzly-wont-fight-assets-props-maps-1/2/3-dark.png`, plus my own in-scene test renders.

Count: asset_requests.md lists **31** drawings (30 sections; the skulls share one). The "33" in status.json was a
miscount. The shotlist also uses one asset that was never requested (see Blocker 1).

## Verdict: PASS for all 31 requested assets (29 approved as drawn, 2 fixed by the art director). Episode art is still blocked by one missing asset.

### Approved as drawn (29)
- **Creatures:** `amur_tiger` (calm, closed mouth, white ruff and eye patches, ringed tail; the silhouette reads as a big cat with
  head, tail and legs), `amur_tiger_stalking` (low, paw lifted, same tiger), `wolverine` (squat, tan flank band, snarl uses the
  dark-red mouth only, no drool; the silhouette reads squat and low), `porcupine` (quill dome reads both ways up, not cute),
  `cougar` (plain tawny, black tail tip, reads as a big cat in silhouette), `fisher` (grizzled head, long bushy tail, distinct from
  the wolverine), `grizzly_sitting` (on-model with the library grizzly, no smile), `grizzly_paw` (the arm runs off the right edge
  and no cut end shows).
- **Props:** `porcupine_quill` (barbs at local x +122..+240, so the s059 ring at (+192,0) frames them), `porcupine_costume`
  (quills point out, face and cap clear at 0.5; the thumbs_up is the standard rig hand), `porcupine_costume_cutaway`
  (quills point in, no punctures, gritted face visible), `pincushion_smug` (half-lidded smirk, adult-coded),
  `wolverine_skull` / `dog_skull` (clearly different: the wolverine's is short and deep-jawed with a crest, the dog's long and slim),
  `chainsaw`, `radio_collar`, `elk_leg` (butcher-paper wrap, no cut edge), `pizza_box`, `vending_machine` (no readable text),
  `bison_car` (flat, unimpressed headlight eyes; funny, not cute), `upright_piano`, `touring_motorbike` (no brand),
  `tiger_paw_print` (reads on snow and on night ground), `tiger_scat` (tidy, no flies), `bear_face_icon`.
- **People:** `large_man` and `tourist_camera` (crude tier, grey crescent, no cap, auto_ink goes white on dark).
- **Maps:** `russia_far_east_map` (Korea, the Sea of Japan and Sakhalin's tip read, no labels), `usa_map_grizzly_1800`
  (same geometry as `usa_map`, brown range to 100W, state lines visible through it).

### Fixed by the art director (2), now approved
1. **`grizzly_somersault`: the back was straight** (the rotated library bear read as a stiff log diving head-first). I applied a
   bend pass to the bear group: the body is now a tucked curl with a rounded back, the legs and claws are in the air, and the head is
   low on the left. Rotate is 150, the shoulders sit on y=0, and the motion arcs and puffs are unchanged. In-scene check beside
   `moose_cow_rearing` at the s080 scale: `assets/previews/041-ad-fix-somersault-in-scene.png`.
2. **`moose_calf_costume_hanger`: it read as a standing creature, and the hood smiled.** The hanger shoulder wires were hidden
   under the onesie. Now there are outlined grey wire shoulders on the onesie shoulders and a bigger outlined hook and stem above the
   hood (hook top at y ≈ -207, previously -192, so the anchor is unchanged). The hood mouth is now flat (brief: no smiles on
   animals). The s097/s098 (0.6) and s099 (0.5, rotate 30) placements are checked in `assets/previews/041-ad-fix-hanger-in-scene.png`.
   **s099 already references it** (`moose_calf_costume_hanger`, x 880, y 860, scale 0.5, rotate 30), so the director doesn't need to wire anything.

### Blockers (not asset fixes)
1. **`moose_front_leg` is missing from the library and was never requested.** s085 and s086 place it at (800, 580), scale 1.0, and
   the s086 kick arrows span about y 300-800 around it. Director: add it to asset_requests.md. Illustrator: draw it in the
   detailed tier, using the library `moose` leg palette, one long front leg with a cloven hoof, side view, anchor centre, about
   260x620, with no cut edge (the top runs off-frame or fades into a body-colour shoulder). `validate shotlist` fails on it.
2. **s001 `scene_ref: thumbnail`:** `thumbnail.json` doesn't exist yet. This belongs to the graphic designer, not art, but keyframes
   will fail until it exists.

### Optional (non-blocking)
- `amur_tiger`: the white chin ruff's lower notch reads a little like a bow tie at 1.0. Rounding it into a single cheek tuft would
  be cleaner on the next pass. It's invisible in the silhouette shots.
- `tiger_scat`: three round lumps can read as pebbles. A slightly longer, joined log would read better in the s156 row of 12.
