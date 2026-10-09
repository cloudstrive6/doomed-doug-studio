# Art review: 010 How Every Deadly Venom Would Kill Doug (library assets)

Reviewer: art director · 2026-10-09
Scope: the 41 new library drawings in `asset_requests.md` (previews `assets/previews/010-every-venom-assets-b1/b2a/b2b/c1/c2/c3.png`),
the new recurring prop `field_guide_open` / `field_guide`, the engine notes (alive `on_back`, `EDGE_PX`).
Extra test renders I made: the dark set on `#1f5f66` / `#060c12` (octopus x2, mamba, funnel-web, Irukandji, box jelly x2, torch),
the costumes over Doug `stand`/`sit`, the field guide at 0.55 and 1.15 with `doug_cap`, the platypus at 2.0, the viper at 2.4, the hornets at 0.22
(one rotated 170), the scorpion at 0.22 rotated, the flash octopus at 0.3, and the bullet-ant / Komodo silhouettes.

## Verdict: REVISE (2 assets, both small fixes). Everything else is APPROVED.

The batch is strong. It is clearly in the detailed tier against crude Doug, on palette, and every animal reads as dangerous rather than plush.
There are no wounds, drips or blood anywhere. The dark-scene assets (octopus, funnel-web, Irukandji, box jelly, torch) all read on
`#1f5f66` and `#060c12`. The box jelly's auto-ink outlines and tentacles flip to white and look great on near-black.

## Required fixes (illustrator)

1. **`box_jellyfish` + `box_jellyfish_eyes`: the rhopalia read as tiny grinning faces.** Each cluster is two big dots (r 3.5) above
   an arc of four small dots (r 2), which makes two eyes and a smile. At mid scale on dark water they look like little skull or smiley faces
   (kid appeal, and it undercuts the boss). Redraw the six eyes in each cluster as **equal-size dots (r 2.5) in a tight 2-wide x 3-tall
   vertical block** (for example x ±4, y -6/0/+6 around each cluster centre). Use no arc and no bigger "eye pair". Keep the four cluster
   centres exactly at (-120,+95), (+120,+95), (-50,+115), (+50,+115). Apply the same new layout to the 24 lit yellow eyes in
   `box_jellyfish_eyes` (it has the identical smile layout) so the overlay still lines up at the same x/y/scale.
2. **`saw_scaled_viper`: stray black stub reads as a second eye at the left loop end.** Elements 72 (`[-161.8,0.2]->[-160.1,4.5]`)
   and 168 (`[-162.0,19.1]->[-164.1,21.7]`) are width-5 black outline stubs at the coil seam. At 2.4 (scales close-up) they render as a dark dot
   on the left end of the middle coil, so that end looks like a second head. Remove them, or blend them into the continuous outline. The head
   cross mark, the saddles and the keeled-scale texture hold up well at 2.4. Keep everything else.

Re-render the b2b preview (box jellies) and b1 preview (viper) after the fix. I will approve on sight, and no new full review is needed.

## Per asset

| Asset | Verdict | Notes |
|---|---|---|
| `field_guide_open` | **APPROVE (new recurring prop)** | See decision below. FRIEND? and the box are legible at 0.55, and the name and stamp zones are clear. |
| `field_guide` | APPROVE | At 0.45 it reads as a battered book with a cream label and a red ribbon. |
| `platypus` | APPROVE | Not cute. Holds up at 2.0. The cream spur is visible on the hind ankle. |
| `bullet_ant` | APPROVE | Menacing, with a clean SIL. |
| `asian_giant_hornet` | APPROVE | Bold at 0.22, also rotated 170. The wings span the y -170 line. |
| `komodo_dragon` | APPROVE | Heavy and dusty with no drool. Clean SIL. The tongue runs past +450, so allow for that when cropping on the right. |
| `komodo_head_scan` | APPROVE | Clean textbook diagram. The gland sits at (+60,+90). |
| `indian_red_scorpion` | APPROVE | Reads tiny and rotated (boot shots). |
| `indian_red_scorpion_uv` | APPROVE | Identical geometry (46/46 shapes shared). The glow is good. |
| `saw_scaled_viper` | **REVISE** | Fix 2. |
| `blue_ringed_octopus` | APPROVE | Dull ochre with slit, lidded eyes. Not cute. Reads on teal. |
| `blue_ringed_octopus_flash` | APPROVE | Identical geometry (118/118). Reads as "danger" and holds at 0.3 in the hands. |
| `black_mamba` | APPROVE | Olive-grey, not black. Reads on `#1f5f66`. |
| `black_mamba_gape` | APPROVE | The inky mouth is the only black. Small fangs, no drool. |
| `funnel_web_spider` | APPROVE | `#2a2f38` with blue-grey shine. It does **not** vanish on `#060c12`, and the fangs are clear. The raised legs reach y -305: **director**, check the counter zone on s186-s210 when it is placed high on the right. |
| `inland_taipan` | APPROVE | Calm but snake-serious. |
| `inland_taipan_winter` | APPROVE | Identical geometry (91/91). |
| `irukandji_jellyfish` | APPROVE | Nearly invisible on purpose, but the outline and threads read on dark teal. The red-brown dots are tiny cnidocyte clusters and do not read as blood. |
| `box_jellyfish` | **REVISE** | Fix 1. Otherwise excellent: on near-black, the bell, pedalia and white tentacles make a great boss. |
| `box_jellyfish_eyes` | **REVISE** | Fix 1 (same layout). |
| `cat_costume` | APPROVE | Checked over Doug `stand`. The face and the whole red cap are visible, and the ears sit behind the cap dome. Grim, not mascot. |
| `cat_costume_sit` | APPROVE | Checked over Doug `sit`. The legs line up. |
| `cat_costume_flat` | APPROVE | White X eyes on the hood. Deflated and not gory. The director must keep `doug_cap` in frame (art bible eaten-whole rule). |
| `monkey` | APPROVE | Neutral, not cartoon. |
| `rabbit` | APPROVE | Wild rabbit, not a bunny. |
| `pill_bottle` | APPROVE | Pills sit inside the bottle and none spill. |
| `staple` / `paperclip` | APPROVE | |
| `ant_glove` | APPROVE | Plain, respectful object with the ants in the weave. No costume read. |
| `honeybee` | APPROVE | Its scale is right next to the hornet (about 40%). |
| `matchbox` | APPROVE | |
| `beehive` | APPROVE | |
| `mouthwash_bottle` | APPROVE | The label stays readable when rotated 90. |
| `uv_torch` / `torch` | APPROVE | Both read on near-black. The lens glow sits at +250. |
| `boot` | APPROVE | Fine worn and rotated -80. |
| `binoculars` | APPROVE | Reads on dark. |
| `golf_ball` | APPROVE | |
| `seashell` | APPROVE | The opening is at about (+130,+40) and the dark interior is empty. |
| `guitar` | APPROVE | |
| `basketball_hoop` | APPROVE | The rim and backboard heights match the request. |

## Decision: the field guide is APPROVED as a recurring prop for the `animals` playlist

It is cheap (one asset plus overlays), on-brand, and gives every item a clear outcome beat. A sight gag that never gets explained suits the
channel. I added it to `channel/art_bible.md` (Recurring layouts), and these rules are binding for every episode that uses it:
- **Inset:** `field_guide_open` at scale 0.55, centred at about (330, 880). That keeps it inside the safe area and clear of the counter zone.
  Hero close-ups at 1.1-1.2.
- **Overlays sit in fixed zones (local coordinates):** the animal name is black Arimo text on the left page, centred near (-140,-110), at
  26-34 units, max 2 words. The tick is a green (`#2e8b3a`) check in the box at (+205,-115). The stamp zone is centred at (+140,+50): "NO" in red
  `#e0201b`, about 110 units and slightly rotated (-8 to -12 deg), or "MAYBE" in orange `#ff8a1f`, about 64 units. Nothing crosses the spine
  (x=0) or the coffee ring.
- On death beats the guide inset counts as screen furniture and must not touch the counter zone. At (330, 880) it doesn't.
- **Continuity:** the same page every time. Do not add new printed content to the asset. Episode-specific marks are overlays.

## Engine notes

- **`EDGE_PX = 5` in `studio/scene.py`: CONFIRMED.** 975a6a3 introduced 5 px to rebuild the edge ring deeper than the ~3 px that
  boil/wobble pulls full-bleed backgrounds in by. 35ddca9 rewrote `_clean_edges` with `ring=4` and deleted the constant, but the call still
  passes `EDGE_PX`, hence the `NameError`. 5 is the right value: it is deeper than the worst measured pull, still invisible (5 px of a
  1920 px frame, copied from the adjacent row), and it is what the 009 edge fix was verified at. Non-blocking cleanup for whoever next touches the
  file: make the `_clean_edges` default `ring=EDGE_PX` so the two numbers can't drift apart again.
- **Alive Doug floating `on_back` (s253-s255): APPROVED with conditions.** I checked the shotlist: `hopeful` / `flat` / `gritted`, hip at the
  waterline, and no DOUG DEATHS counter on those shots. Keep it that way. The rules are: never use `dead` or `cap_off`, never show the counter,
  and keep the open eyes visible (no `rotate`). The death beat that follows must change the expression to `dead` and add the counter, so the
  viewer can tell the two shots apart. I logged this in the art bible as an allowed survival or floating use of `on_back`.

## Routing
- Illustrator: fixes 1-2.
- Director: watch the funnel-web leg height near the counter zone, keep `doug_cap` in frame on s210, and follow the field guide overlay spec above.
