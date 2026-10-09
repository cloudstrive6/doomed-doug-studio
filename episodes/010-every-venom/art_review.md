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

---

# Keyframe review: 010 How Every Deadly Venom Would Kill Doug

Reviewer: art director · 2026-10-09
Scope: all 286 keyframes (`build/contact/sheet_01..24.png`), with full-res crops of the counter zone (s005, s047, s070, s093, s118, s138, s144,
s161, s174, s185, s204, s211, s233, s234, s245, s257, s064, s190) and detail crops (s020, s069, s097, s115, s154, s175, s202, s207, s210,
s224, s235, s258). I also cross-checked the shotlist JSON for the counter values, the field-guide overlays, the death poses and the Doug placement.

## Verdict: FAIL (composition fixes, mostly 1-line moves). Re-render only the listed shots. I will re-check the contact sheets for those shots only.

### What already works (keep it)
- **Style consistency:** one look across 286 shots. Crude Doug against detailed-tier animals everywhere. Palettes are consistent per item (platypus
  creek, rainforest, dune orange for hornet/Komodo/viper, night interior for the scorpion, rock pool teal, night savanna, porch night, outback,
  dusk sea, near-black sea for the box jelly). Every item gets a new environment, so the severity axis reads visually as it gets darker toward the boss.
- **Death counter:** it ticks exactly on the death shot, 84 to 93: s069 85, s091 86, s117 87, s136 88, s159 89, s182 90, s210 91, s256 92, s281 93. It
  holds on the survival beats (s023, s045, s232) and the alive `on_back` float (s253-s255 keep 91, with living expressions and no `rotate`). Every death uses
  `on_back` + `dead` with no `rotate`. The cap stays in frame on all the no-body deaths (s210, s256, s281). The persistent counter matches the 008/009 convention.
- **Field guide:** it sits at (330, 880) at 0.55 on every outcome beat, it is the same page every time, the name, tick and stamp sit in their zones,
  and nothing crosses the spine. The names are legible at 1080p (s020 crop). The hero sizes are right: 1.2 at s282, 1.1 at s285/s286. The closed guide is
  in hand at 0.42-0.45 (s002, s003, s005). The stamps are correct (MAYBE: platypus, bullet ant, taipan; NO: the other 9). The s283/s284 grid matches.
  The colours differ slightly from my spec (tick `#2fae3a`, MAYBE `#e07b00` + black outline, name `#2b2b2b`, stamps upright because the engine's
  `text` cannot rotate). They read better on cream, so **I accept them and have updated the art bible to match**. No change is needed.
- **Box jelly rhopalia** (asset fix 1) read as eye blocks, not faces (s258 crop). The viper fix holds at 2.4 (s127).
- **Gore:** none. All the deaths are cartoon. The ant glove (s041/s042) is respectful.

## Required fixes: shotlist (director)

**Counter zone (x 1300-1860, y 110-230) is reserved.** The item title cards sit at y 250-280 at size 120-160. Their cap tops land at y 195-220 and
run past x 1300, so they touch or butt against the counter box:
1. **s093, s138, s161, s234, s257** (they touch the box, which is the worst case) and **s047, s070, s118, s211** (inside the zone): move every item title
   card to **y 340-360**, the same as the section cards ("PAIN ONLY" s004 at 360 is clean), or cap the title size so the glyph tops stay at y ≥ 250. s025 (330) and s185 (300/108) are fine.
2. **s070:** the "KOMODO DRAGON" N overlaps the sun. Once the title moves to y 350, move the sun to (1760, 520) or drop it from this shot.
3. **s185:** the moon at about (300, 240) sits behind the "S" of SYDNEY. Move the moon to (200, 500) or drop it.
4. **s174:** the "MOUTH" label (1650, 250) sits in the zone, directly under the counter. Move it to about (1500, 420) and re-aim the arrow.
5. **s204:** the "PREDATORS" label (1300, 220) abuts the counter box. Move it to y ≥ 320.
6. **s245:** the "SOARING" label (1420, 240) is in the zone. Move it to y ≥ 320, or put it at the arrow's base.
7. **s190:** the "!" at (1500, 260) touches the zone. Move it to y ≥ 340. **s064:** the top hornet + "!" (1300, 200-300) touch the zone's left edge. Move that pair to y ≥ 330.
8. **s028, s040:** the world map's top-right corner (about x 1580-1660, y 180) runs under the counter box. Use the s059 framing (scale 0.82, y 590).
   Also, **s028 "BULLET ANT"** and **s040 "BRAZILIAN AMAZON"** labels straddle the map's top frame line. Put them above the frame (y ≤ 200 after the
   map moves, and clear of the zone) or as a side-margin label. **s040:** the bullet ant (1640, 840) sits on the map's right frame. Move it to x ≥ 1720.
9. **s233** (narrator deletes the death): the struck-through "DOUG DEATHS: 92" box (1590, 290) sits on top of the sun, and the red X at (1150, 600)
   floats in empty sky with no target. Drop the sun from s232-s233 (or move it to (300, 330)) and delete the stray red X (the strike line already
   carries the gag). If you want an X, put it on the 92 box.

**Map frames (art bible Text):**
10. **s216:** the "CHANNEL COUNTRY" side label (1500, 640) starts on the map's right frame line. Put it in the side margin at x about 1680, size 36, on two lines ("CHANNEL\nCOUNTRY").
11. **s132:** the viper (1600, 300) sits on the map's top-right corner. Move it to (1700, 760), next to Doug.

**Continuity / readability:**
12. **s175:** **two heads.** `black_mamba` (1080, 760) is still drawn under `black_mamba_gape`, so a second small head pokes out of the coil. Delete
    the `black_mamba` element, because the gape asset is the whole snake.
13. **s115-s116:** the narration says "inside his boot", but the three UV scorpions (y 798-828) crawl over Doug's face and chest, and the UV torch
    sits under the boot. Put the scorpions at the boot opening (about y 930-950, x 870-930, rotated to point out of the boot), centre the teal glow spray on the
    boot rather than on Doug, and keep the torch in his front hand (the s114 position, rotated down toward the boot). Doug's face must stay clear.
14. **s069:** the fly swatter (638, 942, r90) lies across the knocked-off cap, and its mesh sits under Doug's chin, so the cap and the swatter merge into one
    red blob that reads as a stick into his head. Move the swatter to about (1100, 950), past his feet.
15. **s210:** `doug_cap` (1180, 760) covers the hood face of `cat_costume_flat`, which hides the white X eyes. The death then reads as a sleeping cat. Move the cap
    beside the hood on the step (about (1150, 800)) so the X eyes and the cap both show.
16. **s200-s201:** the HUMANS red X (1450, 620, 0.5) is drawn across Doug's cap and face. Raise it to about y 540 so it sits above his head.

**Kid-appeal (cat costume):**
17. **s202, s205-s208:** Doug wears the cat onesie with `smirk`, which renders as closed-eye "^‿^" happiness. Together with the orange tabby suit, ears and tail,
    that is a kids'-mascot read, and `smirk` is not in the style bible's expression set (7.2). Use **`flat`** (deadpan smug) for s202 and s205-s208. Keep
    `gritted` on s209. The costume itself stays approved (face and whole cap visible, tail behind, no cat face on the hood).

**Layout variety (same composition 5+ times in a row):**
101 of 286 shots use "subject centre-left + small Doug standing bottom-right at x ≥ 1580, scale ≤ 0.5". It is fine as a house layout, but these runs
are too long: **s055-s061 (7), s008-s012, s073-s077, s081-s085, s121-s125 (5 each).**
18. Break each run in the middle. In **s058, s010, s075, s083, s123**, move Doug to the left third (mirror the layout: subject right, Doug left at
    x about 300), or drop Doug and push the subject bigger. Change one shot per run, plus s059 in the 7-run (Doug off, or at the left edge of the map).

**Label count (style bible 7.4, max 2 keyword labels on screen):**
19. **s112:** three labels at once (FINDING EACH OTHER / LURING PREY / BLOCKING SUNLIGHT). Keep the three icons, drop the labels to one word each
    and show them **one at a time** with `appear`, removing the previous one, or split the beat into 2 shots (2 labels + 1 label).

**Polish (non-blocking, fix while you are in the file):**
20. **s036:** the "PONERATOXIN" wordart touches the ant's mandibles. Use x 1300, y 820. **s176:** the "BLACK" wordart sits on the coil. Use (1550, 380).
    **s206:** "DOES NOT MATTER" runs across the house's left wall edge. Use x 620 or size 72.
21. **s237, s262:** the size labels sit on the bell top. Move them to the side ((1350, 420) / (560, 260)). **s241:** the "INVISIBLE" label covers the jelly. Use (1350, 760).
22. **s097, s103:** Doug's auto-ink lands on the mid-brown floor, so he renders black on dark brown with low contrast. Set `"ink": "#ffffff"` on those two Dougs.
23. **s119:** the mamba silhouette (1150, 520) floats in the sky. Put it on the ground line (y about 860, x 1350), or make the shot a plain diagram background.
24. **s075:** the "DOUBLE BED" label touches the Komodo's foreleg. Use y 960 beside the bed.

## Required fixes: assets (illustrator)

A1. **s224, new `snake_enclosure`:** the shot reuses `aquarium`, so the inland taipan swims among fish, bubbles and coral under water. That is a visible
    factual error. Draw a dry glass reptile tank in the same footprint and anchor as `aquarium` (so the director only swaps the name): black glass
    frame, mesh lid, sand floor, one rock, a water dish, a branch, and no water fill, fish, bubbles or coral. Detailed tier.
A2. **s235, new `moon_jellyfish`:** the "BIG" jellyfish is an in-shot flat lilac ellipse with three white legs. It reads as a table or mushroom and is
    off-tier. Draw a large, harmless-looking moon jelly: a translucent bell with four horseshoe gonads, a frilled margin, short tentacles and oral arms. It must
    read on `#1f5f66`. Anchor at the bell centre. It must not resemble the box jelly's square bell, so the boss stays unspoiled.
    (Director: swap them in at the current x/y. Use about 0.6-0.8 for `moon_jellyfish` so it reads as "big" next to the boat.)

## Routing
- **Director:** fixes 1-24 (shotlist only), then swap in A1/A2 when they land. Re-render keyframes for every shot listed in fixes 1-24.
- **Illustrator:** A1, A2, plus previews. I approve on sight.
- I am not touching the shotlist. I updated `channel/art_bible.md` (field guide overlay colours as rendered, title-card y rule, alive `on_back` with a persistent counter).
