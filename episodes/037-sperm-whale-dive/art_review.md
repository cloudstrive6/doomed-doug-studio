# 037 art review: new assets (art director, 2026-11-04)

**Verdict: PASS** (asset gate). All 13 new assets APPROVED as drawn; no fixes required. Keyframes still to be reviewed
once `build/contact/` exists.

Checked on: assets/previews/037-sperm-whale-dive-assets-whales.png, -props.png, -dark.png (navy water), plus a
0.2x small-size render of shopping_trolley / squid_beak / dentist_mirror.

## Per asset
1. **sperm_whale_head_rising**: APPROVE. Blunt block, wrinkles, scar rings, small low eye, jaw line with teeth on the
   right; water runs read well on both white and navy. Not cute, no smile. Thumbnail-hero worthy.
   (The top is clipped in the whales sheet; that is the preview grid only, the dark sheet shows the full asset.)
2. **sperm_whale_head_cutaway**: APPROVE. Spermaceti (yellow) over the junk (cream lens stack), pink brain far back,
   skull wedge, dashed cut line at the back. Clean diagram; leaves room for shotlist labels.
3. **cartoon_brain**: APPROVE. Pink, folds, stem nub, no blood.
4. **dtag**: APPROVE. Orange float, antenna, four suction cups; reads instantly.
5. **hydrophone**: APPROVE. Grey cylinder, black cap, cable nub at the anchor.
6. **dive_certificate**: APPROVE. Creases, dog ear, wave border, diver flag, blank panel for "40 M".
7. **shopping_trolley**: APPROVE. Red handle + wheels keep it readable at ~60 px (checked at 0.2x).
8. **sperm_whale_jaw_open**: APPROVE. Correct anatomy (hinge at the back, jaw drops toward the front), upright ivory
   cones, socket row on the upper jaw, pale lining (no red). Open gap shows the background water, which is fine.
9. **sperm_whale_tooth**: APPROVE. Cream cone, growth lines, shaded side.
10. **sperm_whale_bent_jaw**: APPROVE. Plump healthy body, crooked S-jaw, no wounds. Matches `sperm_whale`.
11. **dentist_mirror**: APPROVE. Small by design; glint reads.
12. **squid_beak**: APPROVE. Hook and amber wing still visible at ~40 px; in a pile of 30 it reads as "hard bits".
13. **scuba_tank_crumpled**: APPROVE. Rig yellow, zigzag crush, bent valve; cartoon only.

All whale assets share the `sperm_whale` grey, white scar rings and light underside edge, and hold up on `#081a36`.

## Decisions
- **whale_skeleton for the bone-damage shots (s177, s189, s190, s191-s193): ACCEPTABLE, no sperm_whale_skeleton
  needed.** The narration and the dead-bone spray dots are about the ribs and tail vertebrae, which this asset shows
  clearly; the skull is a generic round cetacean skull, not obviously baleen (no baleen plates drawn). At s189's
  0.13 scale nobody can read skull shape. Director note (optional): keep the dead-bone dots and arrows on the
  ribs/tail so the eye stays there, and do not label the skull.
- **mayflower_ship as the Essex and the Ann Alexander (s016-s024): ACCEPTABLE.** At 0.8-0.9 scale behind the sea
  rect it reads as a generic 19th-century three-master sailing ship; the date labels carry the identity. The high
  stern castle is a little old-fashioned for 1820 but not worth a new asset. Director note: keep the two ships
  visually separated by their date/name labels (and ideally different scale or framing) so s022-s023 do not look
  like a repeat of s017.
- **Dive light**: the library `torch` in Doug's point pose is fine for this episode; no new gear.

## Routing
Illustrator: nothing outstanding. Director: the two optional framing notes above.
