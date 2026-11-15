# 048 art review: new assets + director one-offs (art director, 2026-11-15)

**Verdict: APPROVED.** All 15 assets are approved and so are the three director one-offs. I made one composition fix myself (s021, see below). The remaining notes are optional and do not block.

Checked against `channel/art_bible.md` using the three preview sheets plus fresh keyframes of s019, s021, s046, s080, s104, s108, s128, s161 and s169. I also rendered a side-by-side test of the mahi suit worn next to `dolphin_costume`.

## Assets (15/15 PASS)
| Asset | Verdict | Notes |
|---|---|---|
| false_killer_whale | PASS | Slender charcoal body, rounded melon, falcate dorsal fin, bent flippers. It cannot be mistaken for an orca (no patches) or a shark, and it reads on `#2563a0` (s104). |
| false_killer_whale_open | PASS | Maroon interior, plain conical teeth, calm eye, no red. |
| false_killer_whale_tuna | PASS | The tuna is intact, clean and held crosswise. Bold silhouette for the boss shot. |
| false_killer_whale_fin | PASS | Reads at 0.16 as the HUD icon. Lower and more curved than `orca_fin`. |
| false_killer_whale_skull | PASS | Aged bone with fen staining. Not broken-looking. |
| yellowfin_tuna | PASS | Yellow sickle fins, finlets and stripe all read. |
| mahi_mahi | PASS | Bull forehead, full-length dorsal fin, forked tail, blue spots. |
| golden_retriever | PASS (weak) | Recognisable, especially with the wordart in s169, but the legs are stiff, boxy slabs. Optional illustrator polish: taper the legs and add feathering under the belly and tail. Used in 1 shot only. |
| sperm_whale_fluke | PASS | Pale-blue streaming water, no white zigzags. |
| dougs_plate | PASS | Low 3/4 view, fork left and knife right, empty. Does not echo 021's MENU card. Reads at 0.42. |
| tuna_head_hook | PASS | The scalloped bite edge is in body colours, with no flesh or red. At 0.6 it reads as a cartoon "only the head", helped by the ONLY A HEAD wordart. |
| hawaii_map | PASS | world_map style, no labels. The Lanai (+91,-37) and Kona (+242,+154) check points sit on the right coasts. |
| mahi_mahi_costume | PASS | Same construction as `dolphin_costume`. The blunt forehead hood sits over the cap, and the cap, brim, face and eyes are fully visible. Deadpan. |
| mahi_mahi_costume_flat | PASS | Matches the 047 flat-suit convention. Head, X eyes and cap are clear (s108). |
| dolphin_costume_flat | PASS | Same as above (s046). |

No gore, nothing cute and no smiles on any creature. Every creature is in the detailed tier against crude Doug.

## Director one-offs (signed off; log them as approved exceptions)
1. **"FALSE KILLER WHALE", 3 words on 2 lines in the field guide (art bible: max 2 words).** APPROVED for 048 only. The species name cannot be shortened without becoming wrong ("killer whale" is the exact confusion the episode is about). It stays inside the name zone and clear of the spine and coffee ring (s019).
2. **The Beach: upright Doug with `cap_off`, holding `doug_cap`.** APPROVED. There is exactly one cap in frame (s128), the red still marks Doug on the dusk palette, and the sober tone works. Keep the cap at hip height in every Beach shot. It must never be on the sand or on a whale.
3. **s161: the narrator's pre-drawn death as a sketch on a white card, with no counter tick.** APPROVED. The counter holds at 367, and the pencil sleeve is carried to the frame edge (047 rule). Optional director note: the sketch fills only about 1/8 of the card. Scale it about 1.8x and centre it under "368?" so it reads on a phone.

## Fix applied by the art director
- **s021:** `sperm_whale_fluke` was at scale 0.6, which put its tips at y ~154, on top of the HUD `dougs_plate` (x 1090-1270, y 141-191). I changed it to x 1080, scale 0.48, so the tips are now at y ~222 and clear of the plate. The beat still reads (keyframe re-rendered). Director: keep any tall element under x 1050-1300 below y 200 on HUD shots.

## Optional (director)
- s169 and other short meter readings: "TO DOUG: 0 M" centred at 1622 leaves a ~70 px gap after the fin icon at 1418. Either move the label so its left edge sits about 30 px right of the icon, or move the icon to the label's left edge minus 34 (night-clock rule).

---

# 048 keyframe review: contact sheets 01-16 (art director, 2026-11-15)

**Verdict: FAIL.** There are 8 composition fixes, all routed to the **director**. No asset fixes are needed. Re-render the listed shots and resubmit only those sheets.

What passes: the style holds across all 186 frames, with the detailed creatures set against crude Doug. Doug is on-model everywhere, and the cap rule holds: exactly one cap per frame on the Beach, the cap stays in frame on all 6 death beats, and the counter runs 362 to 368 with one tick per death. The HUD (counter, plate, TO DOUG meter) is consistent and stays clear of titles and wordart. The regional water ramp darkens item by item as logged (`#3a9ad9` to `#14365e`), apart from fix 2. Text is legible and inside the safe area. There is no gore and nothing cute, and the reveals use a red rim with a dark glow underwater. Layout variety is good overall, with maps, cards, timelines, split screens and HUD scenes mixed in.

## Required fixes (director)
1. **s041 and s178: the split-screen divider runs straight through Doug** (white line at x 960, and Doug is at x 960). It reads as a skewer through his body. End the line above his head: s041 `points [[960,260],[960,800]]`, s178 `[[960,260],[960,820]]`. Alternatively, keep the line and move Doug at least 60 px to one side.
2. **s139-s141 use `#3a9ad9` water inside The Beach.** That is item 1's colour, and it breaks the "every shot of an item stays on its item colour" rule (The Pod is `#1f5a94`, and the Beach sea band is `#1a4f80`). Recolour the water to `#1a4f80`. In s141 this is the full background. The cream sky in s139/s140 may stay as a diagram card, or switch to the Beach dusk bands. Check that the whales still read; they did on `#1f5a94`.
3. **s142 is a duplicate of s138.** The element lists are identical (same Doug, cap, "?" and beach), and s143 is the same frame again with a title added. Recompose s142 so that it differs from both. For example, use a close-up of Doug (scale ~0.8, left third) looking down at the cap he holds with a "?", or an empty beach with the 4 km dashed line, without Doug.
4. **s184: the yellow "IT MEANT WELL." sticky covers the field guide's coffee ring** (the field guide rule is that nothing crosses the spine or the ring). Move the sticky off the book to its right: rect x 500, y 830, w 137.5, h 68.2, with the text centred at (568.75, 864). That is clear of the book edge at x 484.
5. **s075: Doug overlaps the last hook of row 4** (hook at x 1590-1620, y 880-920, and Doug is at x 1700). Move Doug to x 1800, or delete the hook at (1620, 880).
6. **s133: the 4 km dashed line runs through Doug's legs and hip** (it ends at x 1800, and Doug is at x 1760, hip y 724). End the line at x 1700 so it stops at his feet.
7. **s123: the speech-bubble tail points into the dinghy bow, not at Doug.** The bubble's lower edge also sits on the gunwale, and there is a stray dot at the tail tip. Raise the bubble about 60 px so it clears the boat, and aim the tail at Doug's mouth.
8. **s107: the middle red arrow (930 to 1140 at y 520) passes through the mahi-costumed Doug.** Drop that arrow to y 560 under the costume tail, or raise Doug and the costume together to y 410 (move the worn prop with him).

## Optional (non-blocking)
- s097: the back-row party heads and knives come within about 20 px of the HUD plate. Lower `pizza_table_twelve` by about 50 px to give it some room.
- s100/s101 and s124/s125 are near-identical consecutive frames: only the "?"/"!" changes, or the fins leave. Consider a small camera change (push in or reframe) on s101 and s125.
- s161 (repeated from the earlier review): scale the death sketch to about 1.8x under "368?".

---

# 048 keyframe re-review, round 2 (art director, 2026-11-15)

**Verdict: PASS.** All 8 round-1 fixes are in. I found one leftover problem in s123 and fixed it myself (details below). Checked against full-res `build/keyframes/` s041, s075, s107, s123, s131, s133, s138-s143, s171, s173, s178 and s184, plus the regenerated contact sheets.

1. **s041 / s178: fixed.** In s041 Doug is on the Cocos side (x ~1100), and in s178 he is on the right panel. The divider is clean and nothing crosses his body.
2. **s139-s141: fixed.** The water is now Beach `#1a4f80`. The cream sky stays as a diagram card, and the whales read well on the darker blue.
3. **s142: fixed.** It is now a close-up of Doug (left third, cap held at his hips) with the stranded row along the waterline and the "?" above. It differs from s138 and s143.
4. **s184: fixed.** The sticky sits off the book to its right. The coffee ring and spine are clear.
5. **s075: fixed.** Doug is at x ~1800, clear of the hook grid.
6. **s133: fixed.** The dashed 4 km line stops at x ~1700 at Doug's feet.
7. **s123: partly fixed, finished by the art director.** The bubble had been raised, but the tail tip (962, 262) landed on Doug's raised waving hand. The long, thin wedge read as a stick held in his hand. I changed the speech to `y 140, tail [978, 214]`, so the tail now ends at the top of his cap and stays clear of the arm. The bubble is still clear of the title card and the HUD plate. Keyframe re-rendered.
8. **s107: fixed.** The middle arrow runs under the mahi-costumed Doug, and the costume and Doug moved together.

Also checked:
- **s131 / s133:** the row of intact dark-grey whale silhouettes reads as a mass stranding. It is sober, with no damage and no gore. There is one cap, held at hip height (Beach one-off rule).
- **s171:** the close-up of the open mouth uses the approved `false_killer_whale_open` asset (maroon interior, no red). "LET GO" and the dimension line are legible and inside the safe area.
- **s173:** a cream reaction card with McSweeney (the `diver` asset, not Doug, so no cap is needed), large under a red "!". This breaks up the s170-s174 run.
- HUD continuity holds (367 to 368, TO DOUG 0 M) on all re-rendered frames.

Optional items from round 1 (s097 table, s101/s125 reframes, s161 sketch scale) remain non-blocking.
