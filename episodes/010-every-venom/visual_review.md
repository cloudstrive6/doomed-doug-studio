# 010-every-venom: Visual review

## Round 2 (pre-render: re-rendered keyframes + new thumbnail), 2026-10-09

I checked every round 1 item against the full-size keyframes in `build/keyframes`. I also checked every other shot that changed in commit 8b48e86 (59 shots in total), looking for regressions: s010, s028, s040, s047, s058, s059, s064, s069, s075, s083, s097, s103, s112, s115, s116, s118, s119, s123, s132, s176, s190, s200 to s202, s205 to s208, s210, s215, s216, s232, s237, s241, s245 and s262. I then checked the new thumbnail at full size and at feed size.

### Round 1 items

| # | Shot | Result |
|---|---|---|
| 1 | s175 two-headed mamba | **Fixed.** The coil now ends in a plain tail, with one head only. It matches s176. |
| 2 | s211 to s223 sunburn | **Fixed.** s211, s212, s214, s217, s221, s222 and s223 all show standard Doug with a white head. The sunburn starts at s230 and carries through s232 and s233, as the script says ("walked for days"). |
| 3 | s036 PONERATOXIN on the ant | **Fixed.** The label sits low and right, clear of the mandibles. |
| 4 | s204 PREDATORS under the counter | **Fixed.** The label is now at about y 330, clear of the counter. (See minor note A.) |
| 5 | Thumbnail taipan X-eyes | **Fixed.** The taipan tile shows a worried, sweating, sunburnt Doug, which matches "Doug is fine". |
| 6 | Title cards vs counter (s093, s138, s161, s234, s257) | **Fixed.** Every big red title now sits clearly below the DOUG DEATHS box. No letters are clipped. |
| 7 | s070 / s185 titles over scenery | s070 **fixed**: the sun moved right, clear of KOMODO DRAGON. s185 is **partly fixed**: the moon moved left, but the title still runs over the house roofline, door and window. It is fully legible (red with a black outline on grey-blue), so this does not block. (See minor note B.) |
| 8 | s174 MOUTH label | **Fixed.** The label sits clear of the counter, and the arrow still points to the mouth. |
| 9 | s224 fish tank | **Fixed.** It is now a dry terrarium with sand, a rock, a branch, a water dish and a heat lamp. It reads as a snake enclosure. |
| 10 | s235 "BIG" jellyfish | **Fixed.** The new moon jellyfish has a domed bell, gonad rings, a fringe and wavy oral arms. It reads instantly as a jellyfish. |
| 11 | s013 MORPHINE hidden | **Fixed.** A MORPHINE label now sits above the bottle cap, so the word reads even though the X still crosses the bottle label. |
| 12 | s109 scorpion cropped | **Fixed.** The scorpion is fully in frame. The bottom edge of the glow halo still just touches the frame edge, which is acceptable. |
| 13 | s233 sun behind struck-out counter | **Fixed.** The sun moved to the far left. The struck-out "DOUG DEATHS: 92" box sits on clean sky. |

### Regression sweep (other changed shots)

I found no new defects. Doug is on-model everywhere, including the cat-costume shots s202 to s210, where the red cap and white head stay readable. The counter steps correctly: 84 (platypus) to 85 (after the hornet), 86, 87, 89, 90, 91 (funnel-web death at s210), 91 through the taipan survival, and 92 at the box jellyfish. All the labels I checked are spelled correctly and sit inside the frame. The world maps (s028, s040, s059, s123, s132) and the Australia map (s216) circle the right regions. Nothing shows gore. The red speckle "danger glow" on the title silhouettes is a stylised halo, not blood. Nothing reads as a kids' show.

### Thumbnail

- **Full size (1280x720):** all 12 tiles read clearly. The Doug heads are now about 1.5x larger, so the expressions run from smile to grimace to sweat to X-eyes across the tiles. The box jellyfish sits alone on the darkest tile. The labels avoid the title words. It works with "How Every Deadly Venom Would Kill Doug" and is not misleading.
- **Feed size (320x180):** the red caps and the progression of faces survive. The octopus, hornet, mamba and box jellyfish stand out. The labels are small but legible.

### Minor notes (optional, do not block the render)

A. **s204 (director):** the bottom edge of the PREDATORS box touches the robin's head. Nudge the label up about 20 px, to about y 310, or move the robin down 20 px.
B. **s185 (director):** to finish round 1 item 7, lower the title to about y 560, over the open night sky above the spider, or scale it to 85% so it ends left of the house at about x 1030.
C. **Thumbnail (graphic designer):** in the middle row, "Saw-Scaled Viper" and "Blue-Ring Octopus" almost touch. Tighten the letter spacing or use a size about 5% smaller for those two labels. Also consider "Blue-Ringed Octopus", the standard common name, if it fits.

### Carried over for the editor (post-render)

- Check that the subtitle font renders the é in "Sateré-Mawé" (s040) correctly in final.mp4 and the Shorts.

VERDICT: PASS
