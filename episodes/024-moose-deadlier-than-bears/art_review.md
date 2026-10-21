# 024-moose-deadlier-than-bears: art review (assets)

**Verdict: FAIL (1 redraw). 35 assets APPROVED, 1 APPROVED after an art-director fix, 1 needs a redraw.**
Keyframes are not reviewed yet; that review comes later as a separate pass.

Checked against `asset_requests.md` and the house rules (detailed tier vs crude Doug, thick outline, flat fills with interior shading, on-palette, bold silhouette, readable small, no gore). Previews checked: `assets/previews/024-moose-deadlier-than-bears-moose-assets(-detail).png`, `024-moose-deadlier-than-bears-assets-b(-detail).png`, `024-assets-a.png`, `024-assets-b.png`, plus single re-renders on white. I also compared side by side with the library `moose` and `grizzly_bear` drawings.

## Moose batch
| Asset | Verdict | Notes |
|---|---|---|
| moose_warning | APPROVED | Swaps cleanly with `moose`: hump crest spiky, brow lowered, menacing. |
| moose_head_on | APPROVED (AD fix) | The mouth line curved up into a smile, which breaks the brief's "no smile" rule and matters on the thumbnail hero. **Fixed by AD**: element 32 is now a slight downturn. Everything else is strong. |
| moose_cow | APPROVED | Same animal, no antlers, reads at small size. |
| moose_cow_rearing | APPROVED | Silhouette reads as rearing, with the hooves forward at the top. Suitable for the s128 black/red-rim use. |
| moose_calf | APPROVED | Gangly knobbly legs, not cute. |
| moose_charging | APPROVED | Head down, gallop and speed strokes. The antler tips sit front-top, so the flipped pair will lock. |
| moose_velvet | APPROVED | Velvet stubs read as soft and half-grown, with no blood. |
| moose_antler_rack | APPROVED | Full span, palmate, small stub, no skull. |
| moose_head_surfacing | APPROVED | The ears are a little tall and horse-like, but the drooping muzzle, weed and ripples carry the read. Optional polish only. |
| moose_submerged | APPROVED | Blue-shifted palette, bubbles and weed. |
| moose_nose_cutaway | APPROVED | Clear diagram with pink passage and valves, no gore. Nostrils are at (+122,+134)/(+224,+134), within tolerance of the request. |
| moose_in_apple_tree | APPROVED | Moose reads in the crown with dangling legs and falling apples, and has no drunk cues. |
| locked_antlers_ice | **NEEDS FIX** | See fix 1. |
| moose_track | APPROVED | Cloven print with dewclaws, correct length. |
| moose_icon | APPROVED | Still reads as a moose at thumbnail scale. |

## Bears
| Asset | Verdict | Notes |
|---|---|---|
| grizzly_running | APPROVED | Matches `grizzly_bear` palette and claws. It is a sprawling gallop but reads as running, with a closed mouth. |
| grizzly_sleeping | APPROVED | Curled up with closed lids, calm. |
| grizzly_cub | APPROVED | Round but not cute (small eye, no smile). |
| brown_bear_swimming | APPROVED | Head and hump above water, wake visible, muted body below. |
| black_bear | APPROVED | Reads on white, navy and water thanks to the grey-blue highlights and brown muzzle. |

## Props, places, maps
| Asset | Verdict | Notes |
|---|---|---|
| bear_moose_scoreboard | APPROVED | Matches the chalkboard look. Header, divider and underline are correct and the columns are empty. |
| apple | APPROVED | |
| apple_tree | APPROVED | Reads on navy. |
| willow_bush | APPROVED | Dense enough to hide the cow, and does not read as a pine. |
| paddleboard | APPROVED | |
| snow_shovel | APPROVED | |
| cardboard_antlers | APPROVED | Cap brim, face and eyes stay clear. |
| cardboard_antlers_flat | APPROVED | |
| locomotive | APPROVED | Horn and headlight are where the shotlist expects them. No logos. |
| moose_crossing_sign | APPROVED | |
| small_car_driving | APPROVED | Front side window is an open cut-out (x 0..100, y -163..-112). |
| fire_engine | APPROVED | No text or logos. |
| hand_saw | APPROVED | |
| lake_superior_map | APPROVED | Isle Royale pops in yellow. |
| newfoundland_map | APPROVED | Geographically correct, but the dots moved. See fix 2 (director). |
| anchorage_map | APPROVED | Three valleys open toward the city grid. |
| stadium | APPROVED | No logos. |

## Numbered fixes
1. **locked_antlers_ice: redraw (illustrator).** The four antler halves read as clubs or spoons on thin stalks, not as moose palmate racks. The scratched "X" in the middle reads as a mark on the drawing, not as interlocked tines. Redraw as two **broad palmate paddles per rack**, in the same shape language and colours as `moose_antler_rack` (#d9c49a, wide paddles with tines along the rim, short beam). The two racks should meet in the centre with the inner paddles **overlapping**, and the tines should interleave visibly (draw the front rack's tines over the back rack's paddle; no cross-hatch X). Keep the snow caps, the ice line at y=0 and the crack ring. Nothing should appear below the ice. bbox x -350..350, y -260..0. Shots s189 and s190.
2. **newfoundland_map dots (director, composition).** The Gander Bay dot is at (+168,-41) and the Howley dot is at (-121,-9). The request asked for Gander Bay at (+235,-306). Re-place the moose icons and labels in s251–s255 against the real dot positions so they don't float in the sea.
3. Optional, not blocking: moose_head_surfacing could have broader, leaf-shaped ears angled outward so it reads less like a horse at small size.

AD change made: `assets/library/moose_head_on.json` element 32 (mouth curve) changed from an upturned to a slightly downturned line. Re-previewed and verified.
