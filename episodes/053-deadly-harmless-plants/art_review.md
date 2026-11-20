# 053-deadly-harmless-plants: art review (art director, 2026-11-20)

## Verdict: PASS (assets and keyframes s002-s195)

s001 not reviewed: it uses `scene_ref: thumbnail`, which does not exist until the graphic designer delivers. This is expected
and is the only `validate shotlist` error.

## 1. New library drawings (44): PASS

I reviewed every file listed in `asset_requests.md`. Each one was previewed fitted to its own footprint, and the spec anchor
points were overlaid (`manchineel_tree` cap hang (+260,-330), `yew_berry_closeup` seed/cup, nightshade arrow cluster (+140,-330),
`manchineel_branch_sap` bead points and label/FRUIT clear zones, `nerve_brake_diagram` pedal and blob gap, heart-wiring blob spots,
pump door centre, Black Sea Trabzon dot and label space, Caribbean Florida tip and island arc). All points land where the
director placed them.

- Tiers are correct. Plants, places and diagrams are detailed (layered fills, interior shading, texture). The crude-tier humans
  (`venetian_lady`, `greek_soldier`, `greek_soldier_lying`) use Doug's line weight with a big round head and grey crescent.
- Safety and tone are correct. No faces on any plant or vegetable, no blisters, wounds or body-fluid drips. Sap is clean white
  beads and venom is one tiny pale droplet. The lying soldiers have closed curved eyes, not X eyes. The hat stand has no face.
- All colours are on palette. Silhouettes read well as black shapes (yew, nightshade, oleander, rhododendron, hogweed, gympie,
  manchineel).
- The interrupted revisions are complete and stable: `manchineel_tree`, `giant_hogweed`, `manchineel_branch_sap`, `yew_tree`
  and `yew_berry_closeup`. The generator scripts stopped changing at 18:09, and every file parses and renders.

Fixes I made myself (generator `build/art/gen_b.py` and the library JSON):
1. `yew_berry_closeup`: the hero berry read as a red teapot. It had a long curved stalk like a handle and a flat pot-lid rim.
   I redrew it as a round glossy aril with an opening sunk into the top, the seed sitting in it, and a short stalk into the
   twig. The seed is still at about (0,-50) and the cup body at (+105,+55), so the SAFE / NOT SAFE arrows still land.
2. `deadly_nightshade`: three berries floated free in the air at the top and edges, and at small sizes they read as flies.
   I moved them onto the foliage at the stem tips. The (+140,-330) arrow cluster is unchanged.

Notes for the illustrator (non-blocking, for the next time these are reused):
- `yew_tree`: the crown is fine, but the trunk could be more fluted and flaky (it currently reads as a generic broadleaf).
- `giant_hogweed`: the main stem could be thicker at the base to sell the 5 m scale.

## 2. Episode devices: SIGNED OFF

- `field_guide_open_plants`: SIGNED OFF. It matches the `field_guide_open` geometry. EDIBLE? and the 44x44 box sit at
  (+90/+205,-115). The generic pressed sprig on the left page is held by two tape strips. The name, stamp and TOUCH? zones are
  clear. It reads at both 0.5 (corner) and 1.15 (close-up).
- `contact_dial`: SIGNED OFF. It is a half disc with four opaque 45-degree wedges (green, yellow, orange, red), 6 px outlines
  and a black hub. It has no text and no pointer and stays legible at 0.36. The fixed-width label fully covers the earlier
  state on s079, s122 and s163. NONE turns red on pink from s163.

## 3. Keyframes (contact sheets 01-17): PASS

Doug is on-model throughout: red cap always visible, ink auto-whitens on the night and rainforest backgrounds, and the
sunburn, sweat, sun hat and Greek helmet gear are correct. Zone and background colours stay consistent per item (marsh blue,
churchyard grey, nightshade peach, highway amber, Pontic hills, frontier dusk, rainforest green, beach blue / storm grey /
night navy). The HUD and caption bar are inside the safe area on every shot. Layouts vary well: hero, map, diagram, icon row,
chalkboard, field-guide stamp and silhouette reveal (s020, s042, s092, s124, s143, s162 with red glow).

Fixes I made to the shotlist (in both `shotlist.json` and `build/gen_shotlist.py`, so a regeneration keeps them):
1. s096: the GRAYANOTOXIN TAPE strip covered the whole switch plate, so the toggle and "ON" were hidden and STUCK ON did
   not read. It is now a narrow slanted strip over the OFF half. The toggle stays up and visible, as the request specified.
2. s014: the CARROT FAMILY text sat on the pressed flower and the coffee ring. I moved it up to just under the WATER
   HEMLOCK name (y 500, size 30).

Remaining notes for the director (non-blocking, optional polish):
- Title-card WordArt overlaps the top of the hero plant in s003, s022, s043, s126, s144 and s164. Every title is still
  fully legible, but in s003 and s126 the overlap covers the umbels, which are the identifying feature. Consider raising the
  title about 60 px or dropping the plant about 60 px.
- s166: the sitting Doug overlaps the manchineel trunk and reads small. Move him about 80 px to the right of the trunk.
- s102: the dropped Greek helmet (rotate 80) reads as a red blob at 0.5. Rotate it about 30 instead, or drop it.
- s124: the "HIS ARM" label sits right under the CONTACT label. Moving it about 40 px lower would give the HUD room.
