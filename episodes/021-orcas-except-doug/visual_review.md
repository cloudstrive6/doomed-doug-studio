# Visual review: 021-orcas-except-doug

## Round 1: pre-render keyframes (22 contact sheets, s001-s259)

VERDICT: FAIL

What works: Doug stays on-model all the way through (red cap, white head) and is present wherever he should be. All deaths are cartoon deaths (ghost Doug plus a leftover cap or costume), and there is no gore anywhere: no blood on the s001 shark, the s213 "tongue and lips" is shown as a buoy, and the s216/s223 skeleton is a museum display. The tone is not kids-show. The death counter goes 170 to 178 consistently (s029, s050, s099, s120, s140, s159, s200, s246). Creature drawings are recognisable (orca, salmon, otter, seal, dolphin, stingray, moose, great white, gray whale, humpback, whale shark, blue whale). The menu-board running gag is clean and legible.

The FAIL comes from two broken drawings (s145, s163, s167), many text-on-text and object-on-HUD collisions, and three runs of near-identical compositions.

### Must fix (blocking)

1. **s145 and s163: broken car drawing (illustrator, then director).** The right half of the red car is replaced by a flat background-coloured rectangle, with stray black marks left at the bottom right (s145 at about x1180-1420, y790-1010; s163 at about x1550-1730, y760-920). The "half a car" idea reads as a render glitch. Fix: draw a proper `car_half` asset with a clean cut edge (a dashed red cut line, with the missing half drawn as a dashed outline), or show a whole car with a "÷2" label. Do not mask with a rectangle.
2. **s167: broken Unimak map (illustrator).** A thick vertical black bar splits the map at about x760, and the left third is a flat, lighter, empty panel. It looks like a crop seam. Fix: redraw or re-crop the Unimak map so it is one continuous frame, and keep the 150+ fin grid inside the water area.
3. **The DOUG DEATHS box collides with map frames (director).** The counter box sits on top of the map's top-right corner in s105, s106, s107, s128, s131, s132, s133, s188, s189, s197, s205, s228, s229, s252 and s253. In s253 it also half-covers the Norway pin circle. Fix: shrink each map or shift it left/down so its frame clears the counter box (box spans about x1365-1815, y128-196). Keep at least 20 px of clearance.
4. **Text-on-text overlaps (director).**
   - s062: the "MAMMAL EATERS" label is drawn over the bottom of the DOUG DEATHS box. Move it down next to the orca (for example x1250, y300).
   - s063: "FISH EATERS" has the same overlap. Move it next to its subject.
   - s080: the "LARGEST" big text runs into the DOUG DEATHS box. Move it left or down (centre about x900, y330).
   - s254: "THEY WAITED" overlaps the DOUG DEATHS box. Move it to about y300, centred over the orca/boat.
5. **s202: the chapter title covers Doug (director).** The red "THE LAW OF THE TONGUE" title runs straight through Doug's head and cap in the boat. Move the title up (y about 220) or move the boat/Doug down so the cap is fully visible.
6. **s123 and s124: moose hidden by the HUD (director).** In s123 the moose's antlers are tucked behind the DOUG DEATHS box. In s124 the "LAND ANIMAL" label covers the moose's whole body and head, so only its legs show. Fix: move the moose left and down onto the right hillside (x about 1400, head below y260), and move "LAND ANIMAL" below or beside it.
7. **s256: orca fin drawn on top of the menu board (director).** The fin and its splash sit on the menu paper and cover "MOOSE, 364-725 kg". Move the fin into the water beside the board (for example x1300, waterline) or behind the board.
8. **s051: ghost Doug jammed under the DOUG DEATHS box (director).** The ghost's cap touches the bottom of the counter box. Move the ghost down and left (for example x1550, y300).
9. **Variety: runs of 4 or more near-identical compositions (director).**
   - s010-s014: five map shots in a row. The same WA/BC map, Doug at bottom right, a label under the map. Break it up: make s011 ("didn't get enough to eat") a thin, hungry orca with an empty plate or a "6 OF 40" calendar strip, and make s012 ("harbor seals swim through the same waters") an underwater shot of seals passing orcas. Keep the map for s010, s013 and s014.
   - s067-s071: five navy text-only cards in a row ("POINT SUR, CALIFORNIA, 1972" with lines added). There is no picture at all for the only human-bite case, which is the episode's key beat. Keep s067 as the dateline card. Make s068 a surfer on a board with an orca fin turning away and "HE SURVIVED". Make s069 the surfer next to a seal silhouette with "MISTAKEN FOR A SEAL?" and an Erich Hoyt label. Keep s070/s071 as the card if needed. Nothing bloody: no bite marks, only the orca letting go.
   - s247-s250: four identical sunset boat wides. Make s250 ("That part is real") a close-up of the fish lying in Doug's boat with "REAL", or a push-in.

### Should fix (non-blocking but recommended)

10. **s129: the water plant reads as a creature (illustrator).** The green plant has dangling stems that look like legs and arms, so it reads like a bug or squid next to the moose. Redraw it as a clump of leafy water plants rooted in or floating on the water, with no limb-like stems.
11. **s086, s087, s100, s233: the dolphin/orca "photo ID" grid doesn't read (director/illustrator).** The grey triangles in white squares don't obviously read as fin photos. In s087 the red orca-scar ticks are too small to see at video size, and "fishing gear" scars aren't shown, so "8x" has nothing to compare against. Fix: label the grid "FIN PHOTOS", make the scar marks 2-3 times larger and thicker, and in s087 add a 1-vs-8 tally (fishing gear vs orca). In s233, change "16 IN ALL 3" to "16 IN ALL 3 HUNTS".
12. **s107: a stingray is drawn on Australia (director).** The point is that New Zealand orcas eat rays. Move the ray icon next to the circled NZ, or remove it.
13. **s152 and s153: a boat sits behind the DOUG DEATHS box (director).** The right-hand boat on the horizon is clipped by the counter. Move it left (for example x1300).
14. **s231: the "FEMALES LEAD" label covers an orca in the bottom row (director).** Move the label to the centre of the frame, or drop that orca.
15. **s153: the "2:00" stopwatch label overlaps the orca's head.** Move it up beside the stopwatch.
16. **s063: the fish-eater calls are shown as a salmon.** Use an orca with a small salmon icon (resident orca) so it pairs with the s062 mammal-eater orca. Right now it reads as "the seal ignores a fish".

### Checked and fine
- s001: shark in the orca's mouth, no blood, cartoon. Fine.
- s029/s030, s050, s099, s120, s140, s159/s160, s200/s201, s246: ghost Doug plus cap, consistent and non-graphic.
- s075: the surfboard notch is a cartoon "bite", Doug fine. OK.
- s111 (ray cropped at the frame edge) and s224-s226 (blue whale overflowing the frame) are deliberate scale crops and read correctly.
- s096 CLEVER/FAMILY and s072/s118/s138 crossed words are intentional and still legible.
- s213 shows the catch as a float, with no carcass. Fine for policy.
- s259: CTA frame clear.

### Routing summary
- Illustrator: 1 (car_half asset), 2 (Unimak map), 10 (water plant), 11 (larger scar marks)
- Director: 1 (re-place car), 3, 4, 5, 6, 7, 8, 9, 11 (labels), 12, 13, 14, 15, 16
- Art director: no style violations found; no action.
- Graphic designer: thumbnail not in scope for this round.

Re-screen after fixes: s010-s014, s051, s062, s063, s067-s071, s080, s086, s087, s100, s105-s107, s123, s124, s128, s129, s131-s133, s145, s152, s153, s163, s167, s188, s189, s197, s202, s205, s228, s229, s231, s233, s247-s250, s252-s254, s256.
