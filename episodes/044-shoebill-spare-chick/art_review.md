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

---

# 044 keyframe review (art director, 2026-11-11)

**Verdict: FAIL.** 9 blocking fixes: 8 for the director and 1 asset fix for the illustrator. 9 more non-blocking fixes are listed after them.
Re-render the listed shots with `python -m studio keyframes 044-shoebill-spare-chick --shots ...` and send them back for a delta review.

What I checked: all 195 shots plus the endslate on contact sheets 01-17. I looked at full-res crops of s025, s047, s067, s079, s103, s123, s140,
s147, s158, s160, s164 and s176.

What already passes:
- Doug is on-model in every shot. The cap is visible on ghost Doug and on all six costumes.
- The two tiers hold: the birds, animals and props are detailed and Doug is crude.
- There is no gore. Every death is cartoon: ghost, empty costume, cap left behind, or a cut to black at s191.
- The counter is correct from 336 to 343, with exactly 7 ticks (s026, s066, s085, s104, s124, s161, s191).
- Caption bars match the item names. Item title cards are red, and section headers (FISH. / REPTILES. / FAMILY.) are white.
- The olive swamp chapters use the white-to-yellow WordArt override. No WordArt sits on green ground.
- Nothing touches the counter zone, and all text stays inside the safe area.
- Silhouette reveals are right: the monitor at s067 then s069, the croc at s106 then s107, the python at s118 then s119. On the brown bank the glow is the
  purple speckle, as the bible requires.
- D1 is resolved: the cap now sits on the crown of `shoebill_looking_down` (s160).
- The day ramp reads well: blue day, overcast swamp, hot pale day, dusk, night, then black for the boss death.

## Blocking fixes

### Director (`build/gen_shotlist.py`)
1. **s164-s177 (THE SPARE): the spare chick never appears.** The chapter is about the second chick, but the nest shows only the big chick. The other half
   holds an orange goldfish (s164-s173) or an "EMPTY" tag (s166). In s176 the "peep peep" begging comes from empty nest. Put a second, visibly smaller
   chick (`shoebill_chick_big` at about 0.55x the big chick's scale, facing the parent) on the right half in s165, s166, s171-s174, s176 and s177.
   Remove the goldfish. In s166, change "ONLY ONE" so it points at the big chick, and drop "EMPTY". In s176, start the "peep" text from the small chick's bill.
2. **s123: two shoebills in one frame.** `shoebill_collapse` lands on Doug while `shoebill_statue` stands behind him, so the viewer sees two birds.
   Keep only the statue, looming right over Doug ("So is the shoebill" means it is waiting too). The death reads on the cut to s124.
   Alternatively keep only the collapse, but never both.
3. **s025: Doug is not in the frame.** The collapse happens at the waterline in the top-left corner, with a brown sliver under the wing. The viewer can't tell
   it hit Doug. Bring the collapse down to mid-frame and show Doug's head and cap (lungfish costume) popping up into the splash. Keep "GASP" on Doug's side,
   clear of the wing.
4. **s079-s081 (THE MONITOR): wrong prey.** The bird is "handling" a **catfish** for ten minutes in the monitor chapter. Put `nile_monitor`
   (scaled to fit, tail hanging from the bill) or `water_snake` in the bill. The clock progression across the three shots can stay.
5. **s041-s047: the same composition 7 times** (Doug on the log at left, statue at right). s042, s043, s044 and s045 are almost identical frames. Vary them:
   - s042: tight close-up on Doug's face with the "4 SECONDS" label (he blinks).
   - s043: big statue head close-up (`shoebill_statue` about 1.4, cropped at the chest).
   - s044: keep the wide shot with "NOT FOOD".
   - s045: Doug alone, `flat` expression, on cream.
6. **s103: Doug stands on open water.** The mat splits but Doug isn't on either piece. Put him on the left mat piece, tilted with it, `gritted`,
   so s104 ("the mat kept Doug") follows on.
7. **s047: the "bill" is an unreadable pentagon.** The red-outlined beige shape reads as a road sign. Use `shoebill_head_profile` large, with a small Doug
   drawn on top of the bill between the hook and the base, sized to fit inside its outline, so it reads "fits in its bill".
8. **s117-s119 and s125: off-ramp sky colours inside THE BABY CROCODILE.** s117-s119 use savanna night navy `#1b2f5a`, and s125 uses the dusk orange that
   belongs to THE FIRST EGG. That spends night and dusk before the Family chapters and breaks "every shot of an item stays on its item colour".
   Keep s117-s119 on the swamp overcast (`#b9c4a8` / `#5d6b45`). The python's red glow still reads on it, or use the purple glow. Put s125 on the
   swamp overcast too. s120 stays cream (diagram card).

### Illustrator (asset)
9. **`shoebill_chick_big` still reads as ears.** Even after my fix, the bill at shot scale (s147-s193, 30+ shots) is a dark upright wedge plus a dark
   gape, and on the contact sheets it still reads as two dark ears or horns. Make two changes:
   - Turn the bill to point **forward-right, about 15-25° above horizontal** (like the adult's profile), not up.
   - Recolour the mandibles to the adults' horn/tan bill tones with a darker tip and hook, keeping the dark gape small.

   Keep the anchor, bbox and the cap/feeding point the shots use, or give the director the new bill-tip point. Preview it at 0.6 and 0.16 on dusk `#e88a4a`
   and night `#3b3550`, then send it back to me.

## Non-blocking (director)
10. **Variety in the nest chapters.** The same wide nest framing carries about 30 of the shots from s127 to s177.
    - s133/s134 and s137/s138 are identical pairs. Make s134 a close-up on the bill pouring and s138 a cream card with 2 eggs, then 1 chick.
    - In s145-s150 and s155-s157, use a low close-up of the big chick next to the egg for s148 (size gap) and s157 (SECOND).
11. **s140: the water misses Doug.** The stream rises from the nest and lands on the egg, and Doug's head gets a grey speckle cloud that reads as flies or dust.
    Run the stream from the bill tip onto Doug's cap, with a small `water_splash` on his head.
12. **s139:** the narration says "sits down", so use the `sit` pose on the nest rim.
13. **s071:** the label "AFRICA'S BIGGEST LIZARD, NEARLY 2 M" has 6 words, and the limit is 4. Use "NEARLY 2 M" on the dashed length line plus
    a "BIGGEST LIZARD" label (only 2 labels on screen).
14. **Orange goldfish** in s030, s035, s037 and s039 (the tally icons): this is an aquarium fish in an African swamp, and it is also the prop that confuses fix 1.
    Swap it for the silver fish used in s143/s152, or for `lungfish` / `catfish`.
15. **s062:** the "NOT A STORK." sticky note is unreadable at guide scale 0.55. Drop it here (s180 carries it at hero scale), or show the guide at 1.1.
16. **s194 (count beat):** the field guide is the outcome card, so add the bible's red "NO" stamp at (+140,+50), 110 units (Doug died).
    The sticky notes can stay, clear of the spine and coffee ring.
17. **s006:** the swimming lungfish floats in the sky over the dry mud. Put it at the left edge on the last puddle line, or drop it and keep only the arrow
    from "NO OPEN WATER" to the cocoon. s005-s008 also repeat one layout 4 times, so make s008 a closer crop on the cocoon under the cloud.
18. **s009/s010, s013/s014, s061/s062:** these are near-duplicate neighbours. Push one of each pair in closer (bird close-up, or Doug close-up).

Re-review scope: 1-9 are blocking. Send me s006, s025, s041-s047, s079-s081, s103, s117-s119, s123, s125, s133-s194 (after the chick asset is redrawn) and
any shots changed under 10-18.
