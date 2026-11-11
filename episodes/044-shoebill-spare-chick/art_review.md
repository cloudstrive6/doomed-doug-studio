# 044 art review: new assets (art director, 2026-11-11)

**Verdict: PASS** (29/29 approved). I applied one asset fix myself (shoebill_chick_big). The director has one shotlist fix to make (D1) before the keyframe review.

What I checked: the 6 previews `assets/previews/044-*` (the shoebill sheet, key points on cream and on night navy, animals, costumes,
props). I also ran a 13-shot keyframe test (s022, s028, s050, s063, s082, s085, s089, s121, s124, s147, s158, s160, s188) to check the
costumes on Doug, the pose key points, and readability at shot scale. On top of that I rendered the chick and nest on dusk `#e88a4a` and
night `#3b3550` at 1.5, 0.6 and 0.16 (tally icon) scale.

Both tiers hold. The birds, animals and props have interior shading, layered fills and bold black outlines, and they sit against crude
Doug. All seven shoebill poses are clearly one bird: the same slate palette, horn bill with blotches, pale eye and tuft. The statue's stare
works from 0.28 up to full frame. Nothing is cute: no big shiny eyes, no smiles, no pastels. There is no gore anywhere. The collapse and
gulp are bloodless, and the empty costumes stand in for the deaths.

## Fix applied by the art director
1. **shoebill_chick_big**: the bill was two parallel upright dark slabs, and with the "(((" lines above the head it read as **rabbit ears**
   at shot scale (s147, s160, s188). This asset is in 32 shots and is the episode's antagonist, so it has to read as a bird.
   - I redrew it as one broad wedge upper mandible with a small hooked tip, pointing up-right. Under it there is a short lower mandible
     with a dark gape (begging, slightly open).
   - I removed the three wavy lines above the head.
   - Anchor, bbox and bill tip (~(+40,-302)) are unchanged. It now reads as a lumpy grey bird chick at 1.5, 0.6 and 0.16.
   - The original is backed up at `/tmp/chick_orig.json` for this session only.

## Director fix (composition, route to director)
- **D1. s160 cap on `shoebill_looking_down`**: the crown is at about (+200,-457) in the drawing, not the (+200,-430) given in the request.
  At -430 the cap sinks into the head (visible in the s160 test keyframe). In `build/gen_shotlist.py`, place the cap at y ≈ -455 relative
  to the bird's anchor, scaled with the bird. Check it again in the keyframe review.

## Per asset
| # | Asset | Result | Notes |
|---|---|---|---|
| 1 | shoebill_statue | APPROVE | The hero drawing. Front-facing, bill down on the chest, two pale eyes staring with a heavy brow. Reads at 0.28 (s082) and full frame (s028). Bbox and bill tip match. |
| 2 | shoebill_side | APPROVE | Clean profile with a closed plain bill at the grip point. Head-top point is on the crown. Reads standing on the mat (s089). |
| 3 | shoebill_collapse | APPROVE | Wings flung up, legs trailing up-left, bill first into the water. Comic, with no prey and no blood. The night version adds splash ticks at the bill. |
| 4 | shoebill_looking_down | APPROVE | Bill slightly open toward the nest, eye down along the bill, never at the viewer. Bill tip (+300,-180) is correct. The crown is higher than requested, see D1. |
| 5 | shoebill_gulp | APPROVE | Bill to the sky, tilapia tail at the tip, round throat bulge. The head blob is a little lumpy, but it reads as a swallow. |
| 6 | shoebill_head_profile | APPROVE | The bill is the hero: broad, edge line, dark hook, blotches. The anchor and the 460-unit tip at (+460,+40) check out for the ruler. The neck bulges ~15 units left of the stated x -220, which is harmless. It reads small on the podium (s050). |
| 7 | shoebill_chick_big | APPROVE (after AD fix) | See fix 1. Ugly grey lump, dull eye, no shine. |
| 8 | shoebill_nest | APPROVE | Trampled flat platform that reads on dusk, night and cream. The right rim ends in a pointed stem tuft ~40 units past x +420. If a shot butts it against something on the right, allow for that. |
| 9 | shoebill_egg_hatched | APPROVE | Matches croc_egg chalk white, zigzag rim, loose cap to the right. Doug's hips sit on the rim and his legs are hidden correctly (s188). |
| 10 | lungfish | APPROVE | Marbled olive body, pale belly, thread fins clearly visible, pointed tail. |
| 11 | lungfish_cocoon | APPROVE | Cracked mud cutaway, U-curled fish in a darker-lined chamber, breathing tube to the top. Clear at a glance. |
| 12 | catfish | APPROVE | Broad flat head with long barbels, long dorsal, rounded tail. Reads instantly. |
| 13 | nile_monitor | APPROVE | Dark olive with yellow spot bands, keeled tail to the left, calm. Has a strong silhouette for the black version. |
| 14 | water_snake | APPROVE | Slim S-curve, dark stripe, head right. |
| 15 | hamerkop | APPROVE | The hammer head (crest balancing the bill) is the read. Dull brown, not cute. |
| 16 | lungfish_costume | APPROVE | Felt seams, marbling and floppy thread fins. Doug's head and cap are clear above it (s022). |
| 17 | catfish_costume | APPROVE | Head-flap with drooping barbels reads as catfish on Doug (s063). |
| 18 | monitor_costume | APPROVE | Yellow sewn spots, claw mitts, long tail. Reads at shot scale (s082). |
| 19 | monitor_costume_empty | APPROVE | Flat and empty. The cap on the tail-tip point is right (s085). |
| 20 | croc_hatchling_costume | APPROVE | Green with scute bands and a snout visor, clearly not the white 2025 suit (s121). |
| 21 | croc_hatchling_costume_empty | APPROVE | Collapsed suit, cap point (0,-110) is correct (s124). |
| 22 | tilapia_costume | APPROVE | Silver with faint bars, spiny dorsal, fan tail. Small in s158 but it reads as a fish suit. |
| 23 | shoebill_chick_costume | APPROVE | Grey felt fluff with a short bill on the chest and a deadpan face. Doug is legible in the egg (s188). |
| 24 | floating_mat | APPROVE | Thin, ragged, floating. It looks like it holds a bird and not a man, which is the joke (s089). |
| 25 | wooden_spoon | APPROVE | |
| 26 | garden_hose_claws | APPROVE | Coiled hose, small claws, annoyed heavy-lidded face. Adult-coded deadpan, not cute. |
| 27 | wooden_clog | APPROVE | Pale wood clog, toe right. Reads as a clog, not a slipper. |
| 28 | watering_can | APPROVE | Rose on the spout, metal shading. |
| 29 | spare_tyre_boot | APPROVE | Rear view, boot open, spare tyre in the well. There is clear dark floor at lower right for the "IN CASE" tag. |

## Notes for the keyframe review
- s147/s160/s188 must be re-rendered with the new chick bill before contact sheets are judged.
- In the test frames the wordart sits well clear of the death counter and the caption bar. I will run the full safe-area and variety
  checks at keyframe review.
