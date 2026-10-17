# Visual review: 021-orcas-except-doug

## Round 2: pre-render keyframes (22 contact sheets, s001-s259; re-rendered 18:04 after commit 6833084)

VERDICT: FAIL

Round 1 found 9 blocking items. 8 of them are fixed. Item 9b is still open: s067-s071 are still five near-identical navy text cards, and s068 still has no picture. That is the only reason for the FAIL. No new blocking problems were found. Doug is on-model in every shot. The counter goes 170 to 178 consistently. There is no gore and no kids-show tone.

### Round 1 items: status

| # | Shot(s) | Status |
|---|---|---|
| 1 | s145, s163 car | FIXED. `car_half` now shows a clean solid half, a dashed red cut line with scissors, and the missing half as a dashed ghost outline. No mask rectangle and no stray marks. |
| 2 | s167 Unimak map | FIXED. The new `unimak_map` is one continuous frame. The 150+ fin grid sits in open water. |
| 3 | Counter vs map frames (s105-s107, s128, s131-s133, s188, s189, s197, s205, s228, s229, s252, s253) | FIXED. Every map frame now clears the DOUG DEATHS box. The Norway pin in s253 is fully visible. |
| 4 | s062, s063, s080, s254 text overlaps | FIXED. |
| 5 | s202 title over Doug | FIXED. The title's baseline is at about y330 and the top of Doug's cap is at about y365 (full frame checked). |
| 6 | s123, s124 moose vs HUD | FIXED. The antlers are clear of the counter. "LAND ANIMAL" now sits beside the moose. |
| 7 | s256 fin on menu | FIXED. The fin is in the water to the right of the board. |
| 8 | s051 ghost under counter | FIXED. |
| 9a | s010-s014 map run | FIXED. s011 is now a hungry orca with a crossed-out plate, and s012 shows seals passing underwater. |
| 9b | s067-s071 navy card run | NOT FIXED (see fix 1). |
| 9c | s247-s250 sunset wides | FIXED. s250 is a close-up of Doug with the fish and "REAL". |
| 10 | s129 water plant | FIXED. `water_weed_draped` reads as a floating weed mat. |
| 11 | s086/s087/s100/s233 fin-photo grid | PARTLY FIXED. "FIN PHOTOS" and "16 IN ALL 3 HUNTS" were added. s087 still has no fishing-gear comparison (see fix 2). |
| 12 | s107 ray on Australia | FIXED. The ray now sits next to the circled New Zealand. |
| 13 | s152, s153 boat behind counter | FIXED. |
| 14 | s231 FEMALES LEAD | FIXED. The label is centred and no orca is covered. |
| 15 | s153 2:00 over orca | FIXED. |
| 16 | s063 fish-eater shown as salmon | FIXED. It now shows an orca with a salmon icon. |

### Must fix (blocking)

1. **s067-s071: still five near-identical navy text cards, and s068 has no picture (director; illustrator only if a surfer figure is wanted).**
   - All five shots have the same navy background and the same "POINT SUR, CALIFORNIA, 1972" line, with text lines stacked underneath.
   - s067 and s068 are text only. s069-s071 add the same surfboard and seal pair in the same place.
   - This is the episode's only human-bite case, and the "it let go" beat has nothing to look at.
   - **Fix s068.** Replace the navy card with a seascape: sky over sea water, `surfboard_bitten` floating at the waterline near x700, and `orca_fin` at about x1300 heading right, away from the board. Add a red curved arrow from the board to the fin, and keep "HE SURVIVED" at the top (about y300). If the director wants a rider on the board, use a plain stick figure, not Doug and with no cap, or ask the illustrator for a `surfer` asset. Nothing bloody: no bite marks and no red on the board.
   - **Fix s070 or s071.** Change one of them so they are not both copies of s069. For example, in s071 ("and even then, the orca let go") reuse the s068 seascape with the fin further away and the text "IT LET GO".
   - Keep s067 as the dateline card.
   - Done means no more than 3 navy cards in a row.

### Should fix (non-blocking)

2. **s087: "8x" still has nothing to compare against (director).** The narration compares orca scars with fishing-gear scars, but only orca scars are shown. Under "8x", add a two-row tally: "ORCA SCARS" with 8 red ticks, and "FISHING GEAR" with 1 grey tick (or a small hook/net icon). Make the red scar strokes on the fin tiles about 2x thicker (width 9 now; use about 16).
3. **s255: Doug overlaps the orca fin (director).** Doug's cap and raised arm are drawn over the base of the fin and its splash (full frame: fin at about x1550, Doug at about x1650). Move Doug right to about x1760, or the fin left to about x1420, so there is about 60 px of open water between them. That makes the "they hunt everything" beat read as fin plus Doug, not one merged shape.
4. **s145: the car_half scissors almost touch the shark's pectoral fin (director).** The gap is about 40 px at about x1180-1260, y740-790. Drop the car about 60 px (y+60), or nudge it left about 100 px, so the cut line and scissors read on their own.

### Checked and fine (new this round)
- s011 hungry orca with a crossed-out plate, and s012 seals underwater: both read in 1 second.
- s069 `surfboard_bitten`: the notch is a cartoon notch with no blood. Fine.
- s163 `car_half` next to the calf: it reads as "half a car", which matches the narration.
- s164 shows 20 cars, which matches the narration.
- s227 shows the cars and Doug icons with their counts. Legible.
- s250: the large Doug close-up is on-model (red cap, white head).
- s257/s258 outro: the "MAYBE" book callback reads clearly.
- s259 CTA: the costume lineup is clear and the deaths are cartoon (X eyes, no gore).
- The full frames for s145, s202 and s255 were viewed at 1920x1080.

### Routing summary
- Director: 1 (s068 seascape, s070/s071 variation), 2, 3, 4
- Illustrator: optional `surfer` figure for fix 1 only, if the director wants a rider on the board
- Art director: no style violations; no action
- Graphic designer: thumbnail not in scope this round

Re-screen after fixes: s067-s071, s087, s145, s255.
