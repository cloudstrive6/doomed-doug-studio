# 056 art review: new assets (art director, 2026-11-23)

**Verdict: PASS** (assets, after one art-director fix to `snake_costume_cobra`). No illustrator fixes are required.
There are four composition fixes for the director, and they are needed before keyframes.

Reviewed: `assets/previews/056-assets-kingcobra.png`, `056-assets-others.png`, `056-assets-props.png`, plus my own context
renders. These show the costumes on Doug in every shotlisted pose, the assets on the dusk/night/slate grounds, the 0.4-0.5
scales, and `all_fours` next to the `clouded_monitor` silhouette.

## King cobra family (olive `#6b7a3a`, pale chevrons, narrow hood)
1. `king_cobra_reared`: **PASS**. The olive body with chevrons that fade toward the head and the small dark eye under a heavy
   brow make it read as *Ophiophagus*. The hood is a narrow ridge, so it cannot be mistaken for the grey 045 mamba or the
   wide-hooded `cobra_hooded`/`indian_cobra`. It still reads at 0.5 in a row, and it stands clearly taller than `indian_cobra`
   at the same scale.
2. `king_cobra_reared_gape`: PASS. The geometry is identical to `king_cobra_reared`, with a pale pink-grey lining, two small
   fangs and no drool.
3. `king_cobra_crawl`: PASS. It is a long shallow S with a forked tongue. The bbox is y -86..0, which is lower than the brief's
   -110, so it is fine for every placement.
4. `king_cobra_strike`: PASS. It is a clear lunge with a wide pink-grey gape and nothing gory.
5. `king_cobra_bulge`: PASS. The bulge is a plain smooth swelling with no body outline inside it, so it is a clean cartoon
   death image.
6. `king_cobra_head_tongue`: PASS. It has strong head shields, a brow, a nostril and a two-tipped tongue. This is the
   detailed tier.
7. `king_cobra_fight`: PASS. It is a looped tangle with each mouth clamped on the other's neck and no wounds. One snake is
   slightly smaller.
8. `king_cobra_hatchling`: **PASS, including the not-cute check.** It is near-black with thin pale chevrons and has an
   adult-proportioned head, a small eye and no smile. It does not look like a nursery toy.
9. `king_cobra_swallowing_krait` / `_rat_snake` / `_naja` / `_viper` / `_king`: PASS. Each prey tail leaves the mouth with no
   blood, and the neck lump is subtle. The `_king` prey is thinner, so the big/small read works. Note: `_naja` (`#7a5a32`)
   and `_rat_snake` (`#8a6a3a`) are nearly the same brown. That is acceptable because they never share a frame and the
   narration names the prey. The director must not cut them back to back without a label.

## Nest family
10. `king_cobra_nest` / `king_cobra_on_nest` / `king_cobra_nest_cutaway` / `_empty`: PASS. The leaf litter (brown, tan and
    rust leaves plus twigs) is clearly different from the earth Komodo `nest_mound`, and it holds up on dusk and on the
    closing slate `#2a2030`. The eggs are white leathery ovals, and the cut edge is leaf litter with no meat tones. The
    on-nest female is alert but not cute.

## Other snakes and the lizard
11. `banded_krait`: PASS. It has bold equal black/yellow rings, a blunt tail and a black head. It is thumbnail-ready.
12. `common_krait`: PASS. It is blue-black with paired white bands, and the `#3a4256` back highlight keeps it readable on
    night/slate grounds. Packaging guard: it never appears inside a king cobra (checked: the `_swallowing_*` set has no
    common-krait variant).
13. `krait_swallowing_krait`: PASS.
14. `indian_rat_snake` / `indian_rat_snake_puffed`: PASS. It is warm brown with a round eye but a neutral face. The puffed
    throat reads as a balloon neck.
15. `indian_cobra`: PASS. It has a wide hood with a spectacle mark, it is brown, and it is clearly smaller than the king.
16. `pit_viper_green`: PASS. It is a compact coil with a triangular head and reads at small size.
17. `clouded_monitor`: PASS. It is grey-brown with cream clouds. Its silhouette (head up, legs clear) rhymes with the new
    `all_fours` Doug (tested on `#1b2f5a`/`#2b3d33`).
18. `reticulated_python`: PASS. It is heavy and gold-tan with a net pattern and white flank spots, and it is shorter and
    fatter than the king cobra.
19. `cobra_python_dead_pair`: PASS. Both snakes have X eyes and there are no wounds. The python reads as one wrap plus
    tangle rather than a strict "twice round", which is fine for a cartoon photo.
20. `snake_knot_doug`: PASS. It is a pretzel knot with both heads X-eyed and the empty suit's neck hole and X eyes visible.
    There is no body and nothing gory. The cap spot is at (0,-330).

## Doug's costumes (sign-off: one base + palette variants)
21. Base tube suit (`snake_costume_rat`, `_krait`, `_python`, `_king`): **PASS.** On `stand`, `point`, `hands_hips`, `shrug`,
    `arms_up`, `walk1/2`, `wave` and `thumbs_up`, the head, face and the whole red cap stay clear. The felt is deadpan, with no
    snake face. The `_king` narrow felt hood stays below the jaw line and reads as "the cap on the hood".
22. `snake_costume_cobra`: **FIXED by the art director, now PASS.** The illustrator's version put the cardboard flaps out at
    x ±130..±194, y -330..-172, on long diagonal tape strips. Next to Doug it read as two panels on poles (antlers or a
    barbell), not a hood, and the tape crossed the `thumbs_up`/`wave`/`arms_up` hands. I redrew the flaps as **hood wings
    rising from the collar** on each side of the head: x ±36..±200, y -288..-138, with short tape strips over the collar
    joints. The inner edge stays outside the head circle and the cap brim, which reaches x +128 down to y -225. The bottom
    edge at -138 keeps the `point` arm (y -122) visible. The JSON description is updated, and the old version is in git
    history. Pose limit: on `shrug`, `arms_up`, `wave` and `thumbs_up`, the hands go behind the cardboard (see director
    fix 2).
23. `snake_costume_cobra_droop`: PASS. The flaps hang to the shoulders, which is clearly the deflated version of item 22.
24. `snake_costume_rat_flat`: PASS for `on_back` with rotate -90 at +30 x scale (s072), and on its own on the ground (s145).

## Props
25. `deli_ticket_9`: PASS. The 9 still reads at 0.4 (about 40 px), and because it is built from shapes it turns with the
    ticket on the ground.
26. `deli_counter`: PASS. It is empty, with no food and no text, and the red dispenser on its post is at the top right.
27. `takeaway_box_krait`, `garden_rake`, `rice_plants`: PASS.

## Engine: `all_fours` pose (added)
`studio/doug.py` now has `pose: "all_fours"`. Doug is on his hands and knees with his body tilted 70 degrees forward,
straight arms and his shins flat behind him. His head is up and forward, and his face and cap stay upright. Hands and knees
are on the `stand` ground line (local y +150, hips at the usual y), so **no y change** is needed when swapping it in for
`crouch`. Extent: shin tips at x -87, cap brim at x +333, cap top at y -82. Verified with `python -m studio art` on white
and on the s148 night grounds next to the `clouded_monitor` silhouette, at scales 0.9, 0.65 and 0.4, and flipped. It is
documented in `channel/art_bible.md` and `docs/SCENE_SCHEMA.md`.

## Composition fixes (to director)
1. **s147, s148**: switch Doug to `"pose": "all_fours"` with the same x/y/scale. The figure is longer than `crouch` (+333 x
   scale forward), so check the head clearance: in s147, Doug at x 800 scale 0.65 puts the face near x 1015, well clear of the
   cobra at 1450. In s148, check that the `=` sign at x 900 does not touch the cap brim at about x 765.
2. **Cobra-suit poses** (`snake_costume_cobra`, s078-s098): on `shrug` and `arms_up` the hands disappear behind the cardboard
   hood. Use `stand`, `point` or `hands_hips` for those beats (1 `shrug`, 1 `arms_up` in the current shotlist), or flip the
   expression for the emotion.
3. **No costume on `cower`** (s046 rat, s090 cobra, s099 cobra_droop): at y + 0 the collar covers his mouth and his feet stick
   out under the hem. At the illustrator's suggested y + 40 x scale, the hem and tail sink below the ground line. Use
   `arms_up` + `shock` (s046), `stand` + `gritted` (s090) and `stand` + `sad` (s099, the droop beat) instead. This is now an
   art-bible rule.
4. **`_naja` vs `_rat_snake` swallowing**: do not cut s080 directly against a rat-snake swallow without the item label or an
   annotation on screen, because the two prey tails are nearly the same brown.

I will check items 1-4 at keyframes, along with the NOW SERVING HUD reserved zone (x 1300-1860, y 110-275), which must stay
clear of every new asset placement.

---

# 056 keyframe review (art director, 2026-11-23)

**Verdict: FAIL.** There are 12 composition fixes, all for the **director**. No illustrator fixes are needed. The style is
consistent and Doug is on-model, so this is a short re-render: re-run `keyframes --shots` on the listed shots only.

Reviewed: `build/contact/sheet_01..19.png` (s001-s223 + endslate), with full-res crops from `build/keyframes/` for every
flagged shot.

## What passes
- **Two-tier style**: this holds in all 224 frames. Doug and the humans are uniform crude ink. Every snake, the lizard, the dog,
  the nest and the deli counter are detailed tier. Nothing is gory. Every death (s025, s073, s100, s149, s168, s219) is a
  bulge, a knot, a cap or a cut to black.
- **Doug on-model**: he is on-model everywhere. The cap is visible in every shot, including the ghosts (s025, s150, s223), the
  flat suit (s072), the sleeper (s182) and all_fours (s147-s148). Costume continuity matches `decisions.md`. Expressions stay
  within the fixed set.
- **Asset-review fixes 1-4 are all done**: `all_fours` is in s147/s148, and the `=` clears the cap brim. The cobra-suit beats
  have no hidden hands. The cower beats were swapped as asked (s046 `arms_up`+shock, s090 `stand`+gritted, s099 `stand`+sad
  droop). s080 carries the INDIAN COBRA label.
- **Zone palette**: it matches the director's severity ramp (night hut, bright day, overcast/canopy, night/dusk, late dusk,
  boss night, closing slate `#2a2030`). Diagram cards are cream. Title cards are red with a black outline. The stinger cards
  (s028, s077, s128, s171) have no caption bar on purpose (`topbar: false`), which is fine as a format beat.
- **Counter + NOW SERVING HUD**: it is consistent on every segment shot and turns red at s218 as specified. Its size-26 text is
  legible at 1080p.

## Fixes (director)
1. **s005, s006, s007, s016, s027 (red glow on brown floor/ground reads as a blood pool).** The krait silhouettes lie in red
   speckle on the hut floor `#5a4b3d` and on `#8a7a5a`. Per the art bible's glow rules for red/brown surfaces, use
   `"glow": "#5e4670"` (dull purple) on these five, or `glow_r: 0` plus a body-centre spray kept above the ground line (003 s146
   method). s004/s076/s127 are on cool grounds and are fine.
2. **s077: "VENOMOUS." crosses the Indian cobra's head.** The text at y 430 sits on the hood. Raise the text to about y 300,
   or drop the cobra about 120 px.
3. **s078: "THE COBRA" title covers the king cobra's head.** Only the eye shows through the "H". Move the cobra left/down
   (head clear of x 560-1700, y 160-280), or move the title to the right/up. The first colour look at the item's creature
   must show its face.
4. **s052: the "hi friend?" bubble enters the reserved HUD zone.** Its right edge is about x 1370, y 200-300. Move the bubble
   left (centre about x 1050) or below y 290.
5. **s176: "AGAIN AND AGAIN" runs into the HUD zone.** It ends at about x 1360, y 220-290, right against the NOW SERVING box.
   Use size about 70 centred at x 760, or move it below y 300.
6. **s190: "NOT A SNAKE" wordart sits on the tree canopy** (green-on-green, against the treeline rule). Move it into the clear
   band at x 700-1200, y about 330, clear of the cobra's head and the HUD.
7. **s159: the red swing arrows cross Doug's face, and his red cap sits on the red sofa.** Keep the arrows above the cap crown
   (arc apex about y 470, ends outside the sofa arms). Change the sofa fill to a non-red colour (e.g. teal `#3f7f86` or
   mustard) so the signature cap still pops.
8. **s091: "NATIONAL ZOO" is printed across the sign's top frame edge.** The text is at y 560 but the board face is about
   y 585-660. Set the text to y about 622 and size about 40 so it sits inside the cream face.
9. **s207: "DOUG" overflows the `price_tag`** (the G is clipped at the tag edge). Use size 24 and x about 1668.
10. **s222, s223: the "10" display box covers the red ticket dispenser** on `deli_counter`. Only a red sliver shows at the
    box's left edge, so the payoff prop is lost. Move the box up so it sits above the dispenser (bottom edge above the
    dispenser top, about 90 px higher), or put it to the right of the dispenser post.
11. **Layout variety: the Nest item repeats one composition** (tree at left, nest at centre, Doug at right) in s171-s181
    (11 shots, broken only by s182) and again in s186-s194 (9 shots). This is more than the 2-6-change beat group. Break each
    run with at least two different set-ups, for example:
    - s174 as a low close-up of the female and the leaves (scale 1.3, no tree);
    - s178 as a cream diagram card (55 cm / 1.5 m on `king_cobra_nest_cutaway`);
    - s179 as a `king_cobra_nest_cutaway` push-in on the eggs;
    - s189 as a cream GUARDING / HUNTING card;
    - s193 framed from the other side, with the tree on the right.
12. **s182: sleeping Doug floats above the roof** (his body extends in mid-air past the peak), and his black lines nearly
    vanish on `#7a3b3a`. Lay him along the left roof slope (rotate to match it, body on the shingles), and add a light ink
    or white outline as on other dark grounds.

## Nits (no re-review needed)
- s025, s150: the ghost wears its cap and a dropped cap is also in frame. That breaks the director's own "never two caps" note.
  For s025, I suggest dropping the floor cap and keeping the ticket. s150 can stay, because the cap beside the bulge is the
  death image from s149.
- s186-s192: the `garden_rake` reads fine at full size but is thin in the contact sheet. You could scale it up to about 1.1.
- s209-s213: these are five identical four-cobra line-ups. This is acceptable as build-up because each shot adds a label or a
  circle, but s213 could push in 8% to close the run.

Once fixes 1-12 are re-rendered, I will re-check those shots only. Composition fixes go to the director. There are no
asset changes.
