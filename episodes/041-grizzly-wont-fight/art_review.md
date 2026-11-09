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

---

# 041 keyframe review (art director, 2026-11-09)

Reviewed all 17 contact sheets (s001-s194 + endslate, 195 frames) in `build/contact/`. The `moose_front_leg` blocker above is
resolved: the asset is now in the library and s085/s086 render. s001 renders from `thumbnail.json`.

## Verdict: PASS (after 7 art-director fixes, applied in `build/gen.py` and regenerated into `shotlist.json`, keyframes re-rendered)

### What holds up
- **Doug is on-model in every frame**: red cap, big head with grey crescent, thin lines. Ghost/dead/float, cower, referee,
  porcupine-costume, deckchair and arms_up variants all read. Ink goes white correctly on the six dark death cards
  (s026, s074, s100, s120, s164, s190).
- **Zone colours are consistent per chapter** and distinct between chapters: Yellowstone snow (wolf pack), snowy pines
  (wolverine), dry porcupine ground with pines, sage willow meadow (moose), cold bison flats, river sedge meadow (big male),
  dusk taiga (tiger), orange Montana trail (human). Cream explainer cards, dark map/death cards and the parking lot
  break up each chapter.
- **HUD**: the chapter tag, `DOUG DEATHS: N` and the BEAR'S COST tag are in the same place in every frame. The counter
  runs 315→322 and steps on each death card. The cost tag changes DINNER/FACE/BONES/CUBS/LIFE on each COST card (s004, s052,
  s077, s123, s147), and LIFE is red as intended.
- **Variety**: no run of the same composition. Every chapter mixes title card, silhouette tease, comparison, scale gag
  (Doug rows, pie, calendar, map, ruler), Doug-in-scene gag and a death card.
- **Never gory**: the quill cutaway, the moose kick and the tiger death are all off-screen or symbolic (cap, paw prints, ghost).

### Fixed by the art director
1. **s086 (kick arrows):** the "straight up" arrow (x 840) rode the right edge of the leg and read as part of the leg. Moved it to
   **x 900** (`ARR([900, 760], [900, 440])`). It is now clear of the hoof, and the four directions read separately.
2. **Big Male river shots (s121, s122, s123, s126, s127, s128, s132, s138): Doug stood in the river.** His ground was 980-1000
   but the water starts at y≈940. He now stands on y 920-930 grass. In s121, s128 and s138 he was also moved off the grass tufts
   (x 1560/1640/1560).
3. **s129:** the "SEXUALLY SELECTED INFANTICIDE" label overlapped the bear's back. Moved it up to y 300.
4. **s134/s135:** the "ABOUT 780 M" label covered the second house. Moved it to (1000, 560), right of the houses and above the red dot.
5. **s133-s135:** the map frame's top edge ran behind the counter/cost tag. Moved the frame top from 180 to 290. "CLOSER TO
   PEOPLE" moved to y 380 to stay inside it.
6. **s140/s141:** "BABYSITTER" ran off both edges of the placard. The placard is now 0.65 at x 1180 and the text is 27 px, so it fits
   inside the board and reads at 1080p.
7. `validate shotlist` is OK after the changes: narration is unchanged (2,094 words) and Doug's share is 0.88.

### Notes (non-blocking, no change needed)
- The chapter tag still names the previous chapter during each "the next animal..." tease (s027-s028, s050-s051, s075-s076,
  s101, s121-s122, s145-s146), and the background stays on the old zone. This is consistent across all chapters and works
  as a bridge, so it stays.
- s128: Doug stands close to the piano bench at 0.28. It is readable and fine.
- The asset optional notes above (tiger ruff, tiger scat) still stand. Scat reads acceptably in s156.

Routing: no illustrator fixes are needed. The director should keep the `gen.py` edits above if the shotlist is regenerated (gen.py is
the authoritative source but sits in git-ignored build/, so the committed `shotlist.json` carries the fixes).

---

# 041 art review, round 2 (art director, 2026-11-09)

Reviewed: the re-rendered contact sheets 01-17 (s001-s194 + endslate, rendered 06:55), full-res keyframes s017, s086, s093,
s115 and s123, the four new or changed assets (previews `assets/previews/041-fix-r2.png`, `041-fix-test.png`,
`041-fix-keyframes.png`), the 030 re-check of `price_tag` (in-scene render of 030 s198), and thumbnails A/B/C at
1280x720 and 168x94.

## Verdict: FAIL. All 4 assets PASS, and the round-1 visual-review fixes are in. Three small composition/thumbnail fixes remain (below).

### Assets: PASS (4/4)
- **`moose_cow_icon`**: an exact antlerless twin of `moose_icon` (same body, footprint and anchor). It reads as a cow next to the bull
  icon at row size. s090/s091 now show cows, s093 shows 28 cows + 4 bulls (matches "almost nine in ten"), and s095 keeps
  the 4 antlered bulls. On-palette.
- **`pizza_table_twelve`**: 6 people face us behind the cloth and 6 sit with their backs to us on the near bench. Every head is clear of the table
  edge, every knife is raised, and the cloth is whole. It reads in s016 and s017, and the "two-headed figures" problem is gone. Crude tier for the people,
  which is correct (they are Doug-tier extras, not detailed props).
- **`bison_calf`**: it now reads as a bison calf (reddish-tan, small hump, darker forequarters, dark muzzle), not a dog or piglet.
  At s115 it is clearly smaller than and different from the adult bison in s116. Detailed tier, bold silhouette.
- **`price_tag`**: the grommet now clears the text on all five COST cards (DINNER/FACE/BONES/CUBS/LIFE) and on the HUD mini tag.
  **Other episodes:** only **030** uses it (s198, the amber market stall; 032 and 034 do not reference `price_tag`). I re-rendered 030
  s198 with the new geometry. The tag is blank there, sits on the amber tray at 0.9, and the longer point and string read fine
  (the string loop overlaps one amber bead, which is harmless). No change is needed in 030.

### Round-1 visual-review fixes: verified in the re-render
s016/s017 pizza table (single "?", knives kept, box cleanly removed), s057 forearm runs off frame, s085/s086 show the whole
rearing bull (no loose leg), s090-s093 cow icons, s103/s104 dark bison carcass, s114 MARCH fits, s115 calf, s121/s122/s128/s138
Doug on the grass, s126/s130 cub as the arrow target (no contact), s134/s135 label and frame, s165 tiger added, s172-s177 now a
map → bounty map → bar chart → zoomed range sequence (no five-in-a-row repeats), and s186-s189 broken up by the s188 close-up and the
s189 bear disappearing into the trees. Doug is on-model everywhere, the counter runs 315→322, the cost tag and zone colours are unchanged, and nothing is gory.

### Required fixes
1. **s086 (director): the "EVERY WAY" wordart runs into Doug.** The final "Y" (wordart centre x 1420, size 90, ends at about x 1685)
   touches Doug's cap brim at (1720, ~815). Move the wordart to **x 1330, y 860** (or Doug to x 1790). Keep ≥ 40 px clear. Also, the
   "straight up" arrow `[930,300]→[930,90]` ends with its head touching the bottom of the chapter tag (tag bottom ≈ y 83). Shorten it to
   **`[930,300]→[930,140]`**.
2. **s017 (director): the large man's pizza box floats.** The box (`pizza_box` x 1330, y 620, scale 0.6) sits about 50 px above the large
   man's two arm lines (y ≈ 730-775), so it hovers in front of his face instead of resting on his arms. Move it to **y 680** so the box's
   bottom edge sits on the arms. The fix is in the final frame (`appear` 0.42), so check the keyframe.
3. **Thumbnail A (graphic designer): the tiger's cheek ruff still reads as a cone collar or bandage at 168x94.** The softened ruff group is
   in, but it still has a 6 px black outline running all the way round the inside edge (between the ruff and the orange face), so at feed
   size it reads as a white band strapped round the jaw. Drop the inner outline (`width` 0 or no-outline on the face-side edge) and let
   the ruff blend into the cheek as two or three spiky white tufts that break the silhouette. Keep the outer edge. The bear, Doug, title and cap gap
   (now about 25 px to the nose) are fine.

### Thumbnails
- **A "NOT WORTH IT"**: needs fix 3 only. Otherwise it is the strongest of the three and on-palette.
- **B "TOO COSTLY"**: PASS. The quill-suit Doug and the porcupine are now separated by background (about 40 px), and they read as two shapes at 168x94.
- **C "IT FEARS US?"**: PASS. One focal point, the heart bubble reads small, and the bear's slight left crop is fine.

### Optional (non-blocking)
- s176 → s177: the two surviving populations are **yellow** ovals in s176 and **brown** blobs (with red rings) in s177. Use one colour
  for both (brown matches the range colour on the 1800 map).
- s126: Doug stands on a grass tuft (x ≈ 1845). Nudge him 60 px left.
- s115: "APRIL" at 56 px fills the calendar page edge to edge. 52 px would give it breathing room.
- The tiger ruff and tiger scat notes from the asset review still stand (scat reads acceptably).

Routing: fixes 1-2 → director (gen.py and shotlist.json, then `keyframes --shots s017,s086`). Fix 3 → graphic designer
(`thumbnail.json`, then `thumbnail`). No illustrator work. Re-review only s017, s086 and thumbnail A. If those three are clean, art is PASS.
