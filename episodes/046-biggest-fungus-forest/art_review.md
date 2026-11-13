# 046-biggest-fungus-forest: art review, new assets (art director, 2026-11-13)

**Verdict: PASS.** All 34 requested assets exist; the request lists 34, not 35. Every one is **APPROVE**. Two small fixes were made in place, and two notes go to the director.

Method: each asset was rendered fitted to frame. Costumes were checked worn by Doug in `stand`. The assets were also checked in context in 16 keyframes: s003 s026 s041 s050 s070 s087 s108 s109 s111 s130 s143 s151 s152 s171 s179 s180. Those keyframes cover dark soil, the foxfire card, night, grey dusk, the silhouette beats and the small-scale uses. Checked against the art bible (fungus rules, zone colours) and style bible sec 7 (rules 1, 7 and 8).
Note: `haustorium_collar` and `tomato_costume_flat` have uncommitted illustrator revisions made after commit e8e89980. Those revised versions are the ones reviewed and approved.

## Per asset
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | rafflesia_flower | APPROVE | Warty brick-red lobes, dark cup with a spiked rim. Still reads as a giant ugly flower at 0.35 on the belly (s026). |
| 2 | rafflesia_bud | APPROVE | Cabbage-like bracts with a woody collar. |
| 3 | tetrastigma_vine | APPROVE | Woody liana with compound leaves. |
| 4 | vine_cells_diagram | APPROVE | Green cells with purple-pink threads woven through. |
| 5 | vine_costume | APPROVE | Spiral coil, cap and face clear, plain belly coil for the bloom. |
| 6 | dodder_hedge | APPROVE | Reads as orange string dumped on a hedge. |
| 7 | dodder_seedling | APPROVE | Leaning thread with a hooked tip. Silhouette-safe. |
| 8 | tomato_plant | APPROVE | Straight central stem for the coils. It is about 616 tall against the 520 in the request, which is fine in the frames checked. |
| 9 | wheat_plant | APPROVE | |
| 10 | dodder_on_stem | APPROVE | Tight coils with haustoria bumps and a withered grey root at the left. |
| 11 | haustoria_diagram | APPROVE | Pegs clearly reach the blue vessels (s041). |
| 12 | tomato_costume | APPROVE | Deadpan felt tomato with a calyx collar. Arms and legs come out of it. |
| 13 | tomato_costume_flat | APPROVE | Empty and tangled. `doug_cap` sits correctly on top (s050). |
| 14 | perch_fish | APPROVE | Bars, spiny dorsal fin with its spot, orange fins. |
| 15 | pike_fish | APPROVE | Bean spots, duck-bill snout, dorsal fin set far back. |
| 16 | nuytsia_tree | APPROVE | Golden crown. The silhouette reads (s070). |
| 17 | haustorium_collar | APPROVE | The y -14..+14 gap is kept and the blade reads. |
| 18 | gum_tree | APPROVE | |
| 19 | phone_handset | APPROVE (fixed) | The cord coil was 3 px and read as a little white puff at large scale. I widened it to 4 px. |
| 20 | aspen_tree | APPROVE | Slim and repeatable in rows (s108/s109). |
| 21 | aspen_sprout | APPROVE | |
| 22 | aspen_sprout_bitten | APPROVE | Flat bitten top. The cap sits on it (s108). |
| 23 | aspen_sprout_costume | APPROVE | The leaves on wires do not cover the cap. |
| 24 | deer_fence | APPROVE | The mesh is see-through. |
| 25 | rhizomorph_web | APPROVE | The tan rim reads on `#665244` (s111) and near-black (s003). The silhouette works (s109). |
| 26 | honey_mushroom_cluster | APPROVE | Readable on the dark Oregon ground (s171/s180). White rings, no faces. |
| 27 | oak_tree | APPROVE | |
| 28 | red_oak_costume | APPROVE | The crown hat rim sits on the cap and the cap stays fully visible (s130). |
| 29 | conifer_dead | APPROVE | Lighter than the dusk sky, so it reads well next to `pine_tree` (s171). |
| 30 | bark_cutaway | APPROVE | Off-white fungus fan between bark and wood. The BARK/WOOD label space is clear (s143). |
| 31 | pine_costume | APPROVE | Mid-tone felt. Works with white-inked Doug at night (s151). |
| 32 | pine_costume_fuzz | APPROVE (fixed) | Ten grey arc "speckles", four of them on the head, read as closed eyes and a frown, which breaks the no-face rule. I turned them into round speckle dots. The head is now faceless (s152). |
| 33 | douglas_fir_costume | APPROVE | Drooping tiers and bract cones. Reads on grey dusk (s179). |
| 34 | douglas_fir_costume_fallen | APPROVE | Empty and lying horizontal (s180). |

## Fixes made by the art director
1. `assets/library/pine_costume_fuzz.json`: 10 `#b8b8b0` arc curves were turned into round speckle dots, so no face-like marks are left.
2. `assets/library/phone_handset.json`: the cord stub width went from 3 to 4.

## For the director (composition, not blocking asset approval)
1. s087: the handset (0.5) overlaps Doug's cap brim. Move it about 40 px right or up so the cap stays clean.
2. s152: the green glow in the shot is a large spray disc that covers the whole lower frame. The asset already carries its own faint base glow, so think about shrinking or dropping the shot-level glow.

Full keyframe review follows at the art_approved gate.

---

# Keyframe review (art director, 2026-11-13)

Sheets checked: `build/contact/sheet_01..16.png` (s001-s184 and the endslate).

## What works
- The style holds across all 184 shots. The detailed-tier assets sit next to a crude Doug, and the boil and spray texture is consistent.
- Doug is on-model everywhere: red cap, oval eyes, white ink on the night and dark-soil plates. Every costume keeps the cap visible (vine, tomato, aspen, oak, pine, fuzz pine, Douglas fir). Deaths are clean: an empty costume, a cap on the ground, a ghost, a tombstone. Nothing is gory.
- Zone colours stay consistent within each segment: corpse flower in jungle green, dodder in cream and dun, tapeworm in sky and sand, cable tree in ochre, Pando in beige, the Michigan fungus in sage, the glowing forest in navy, Blue Mountains in slate. The rhizomorph cutaway reads on every ground colour.
- The HUD is consistent. The death counter steps correctly at s050, s088, s108, s131, s152 and s180. The HOW BIG chip turns red for the record holder.
- The black-silhouette-on-spray teaser (s028, s051, s101) is used consistently as a device.

## Verdict: FAIL (composition only, no asset changes needed). Route to the director.

### Text overlapping art (the director's list, all confirmed)
1. s003: "1,000 PITCHES" sits on the rhizomorph strands and the stroke breaks up. Move it into the sky band (y about 120) or put a dark backing plate behind it.
2. s031: "SOMEBODY ELSE" runs into the stem's leaves. Shift it right to x about 1150, clear of the stem.
3. s043: "IT HAS A TOMATO" crosses the tomato plant. Move the plant left to x about 300, or set the text at y about 300 on the right half.
4. s093: "47,000 TRUNKS" sits on an aspen crown, and "ONE LIVING THING" crosses the trunks and almost touches Doug's cap. Remove the 3 centre trunks to make a text window, or put both lines over the ground band. Keep Doug's head clear.
5. s096: "ONE TREE" sits on the right edge of the pitch grid. Shrink the grid to about 9 columns, or put the wordart under the grid above "60 PITCHES".
6. s147: "FOXFIRE" sits on the strands and the top-right mushroom. Move it to the top-left corner (x about 450, y about 140), off the web.

### Other text and safe-area fixes
7. s114 and s149: the wordart is at y=990, so the descenders fall outside the 90% title-safe area and sit on the strands and the mushroom at the bottom. Raise it to y of 900 or less (s149: put it in the sky above the ground line).
8. s111: "UNDER A FOREST." has the same strand-crossing problem as s003. Use the same fix.
9. s036: "TOMATO" overlaps the top of the plant. Move it up and right (x about 900).
10. s072 and s112: the second line of the title card ("TREE" / "FUNGUS") lands on the crown or cap below it. Drop the art about 80 px, or scale it to about 0.85.
11. s074 and s075: "CHRISTMAS TREE" and "GOLDEN-ORANGE" are written over the crown and trunk. Shift the tree left by about 150 px, or move the text to the right third.
12. s139: the end of "DOESN'T WAIT" touches the HOW BIG chip. Move it left or down by about 60 px.
13. s143: "DRIED PAINT" sits on top of Doug's cap. Move Doug right by about 120 px, or move the text up beside "WOOD".
14. s172: "ONLY PART" overlaps the centre conifer. Shift it right to x about 1200.
15. s121: the dead conifer's tip touches the HOW BIG chip. Move the tree left to x about 1100.
16. s005: the line "INSIDE SOMETHING." does not match the narration ("The Corpse Flower.") and crowds the title. Drop it, or move it to s004 if it is meant as a stinger.

### Layout variety
17. s091-s093: three aspen-row frames in a row. Make s092 (the PANDO title) different, for example a low wide shot with the title over a single big trunk, or the map.
18. s122-s123 (after s110 and s121): four near-identical rhizomorph cutaways. Change s123 ("same individual"), for example a close crop on one strand with a DNA tag, or a top-down map.
19. s164 and s165: the same calendar layout back to back, with only the label changed. For s165, use a calendar stack or a split comparison (2,400 vs 8,650), or zoom the existing calendar.
20. s061 and s062: the same clipboard composition. A small change is enough, such as pushing in on s062 or dropping the clipboard and keeping only Doug with "NO SYMPTOMS".

Re-render the affected shots (`python -m studio keyframes 046-biggest-fungus-forest --shots s003,s005,s031,s036,s043,s072,s074,s075,s092,s093,s096,s111,s112,s114,s121,s123,s139,s143,s147,s149,s165,s062,s172`). I re-check these only.
