# 025-too-much-oxygen: art review (new library drawings)

Reviewer: art-director, 2026-10-22
Scope: the 27 new drawings in `asset_requests.md`. I reviewed them in the previews (`assets/previews/025-*`), in my own ink, silhouette and X-ray
test renders, and in 20 rendered keyframes (s027, s039, s073, s082, s096, s111, s122, s141, s147, s161, s170, s179, s193, s194, s198, s199,
s236, s250, s251, s254).

## Verdict: FAIL (4 drawings need fixes; 23 approved)

These four must be redrawn before `art_approved`: **tree_fern, arthropleura_head, fern_saddle, leaf_hat**. Everything else is approved as it is.
The illustrator only needs to re-preview these four. The director does not need to change the shotlist for them because the anchors and
bboxes stay the same.

## Required fixes (route: illustrator)

1. **tree_fern**: FAIL. In context (s111) it reads as a **palm tree**. The brown cluster at the centre of the crown looks like coconuts, and the
   smooth tapered trunk is a palm trunk. That breaks the setting: a viewer will see the tropics, not a Carboniferous coal forest.
   - Remove the brown cluster at the crown centre. Replace it with 2-3 **coiled fiddleheads (croziers)** pointing up out of the crown. That is
     the strongest "this is a fern" cue.
   - Make the fronds long and feathery: arch them up and then down, and give each one clearly separate small leaflets (pinnae) along a midrib.
     Do not use one serrated blade. Use both greens (#4f8a3a / #3a6a2a) so the fronds read as layered.
   - Make the trunk **widen towards the base** into a shaggy skirt of matted roots (Psaronius root mantle), with darker vertical root strands.
     It should not taper like a palm. Optional: add a few hanging dead brown fronds under the crown, but only as drooping blades, never round
     shapes.
   - Keep the bottom-centre anchor and the y -620..0 height limit, because s111 places it under the death counter.

2. **arthropleura_head** (illustrator flagged the view): FAIL. It does not match the request, and it does not match `arthropleura`.
   - The view is plain side-on. The request is **front 3/4**: the head should be turned towards the viewer and right, so that both eye stalks,
     both antennae and the mouthparts are all visible.
   - The body segments are drawn as tall upright slabs (they read as loaves or books standing on end). `arthropleura`'s plates are **low, wide
     and flat with side lobes**. Redraw the first 3-4 segments as wide, flat, overlapping plates that recede in perspective, using the same
     colours and light plate edge as `arthropleura` so that s236 and s250 read as the same animal.
   - Draw the two antennae as a matching pair. Right now one is a plain thin line and the other is striped. Make both short and segmented.
   - Make the mouthparts readable: a pair of jaw-like mandibles plus small leg-like palps under the head, in darker brown. This is what the
     "CENTIPEDE-LIKE" arrow in s236 points at. Right now the arrow lands on a plain antenna.
   - Keep the eyes on short stalks, but spread them apart on the head and make them smaller. At the moment the two big dark knobs read as a
     snail or crab. No shine highlight on the eyes (no cute or mascot look).
   - Keep it legible at 0.6 inside `crt_tv`, so use a bold outer outline and few small details. bbox x -220..220, y -170..170.

3. **fern_saddle** (illustrator flagged): FAIL. At s250/s251 (scale 0.6, held next to Doug and Arthropleura's head) and s254 (0.5, on the ground)
   the smooth green curved tube reads as a **green caterpillar, lizard or banana**, not as a saddle.
   - Build the seat out of visible **fern fronds**: two or three fronds laid side by side, with their leaflets clearly showing along the top
     edge and hanging over the sides. Do not draw a solid smooth tube.
   - Give it a real saddle profile: a raised **pommel** at the front, a lower dipped seat, and a raised **cantle** at the back. Add a dark green
     shadow under the seat lip so it reads as a 3D object.
   - Draw the stirrups as **loops of twisted stem** (rounded D shapes). The current triangles read as coat hangers. Keep the twisted-stem
     straps.
   - Remove the small curl on the top-left tip. It reads as an eye or tail.
   - Optional but useful: lay a couple of fern-stem straps around the underside so it reads as "made to strap on".
   - Keep the centre anchor and the bbox at x -160..160, y -90..90.

4. **leaf_hat**: FAIL. At scale 0.55 (s111) it is a small round pile of leaves sitting on top of a fully visible cap. It reads as broccoli or a
   bunch of grapes balanced on his head, not as camouflage.
   - Make it a **dome that covers the cap**, with larger pointed leaves (with midribs) in #4f8a3a / #6fae4a, spilling down over the sides of
     Doug's head as far as the cap's lower edge.
   - The **red cap brim must stick out of the front**, and the red top of the cap dome must show through a gap at the crown ("the red cap poking
     through the top"). The red should be visible, but less than half the cap.
   - Doug's face (eyes) must stay clear. No leaves below eye level.
   - Keep the anchor as it is (Doug's hips, stand pose, rim bottom about y -293, leaves up to about y -420). Test it at 0.55 with stand,
     hands_hips and thumbs_up (s110-s117).

## Approved (no changes required)

| # | Drawing | Notes |
|---|---|---|
| 5 | bojophlebia | APPROVE. Four broad, rounded, smoky wings, a brown body and tail filaments. Clearly not `meganeura` (s039). The silhouette reads well. |
| 6 | megarachne_spider_1980 | APPROVE. Heavy and creepy tarantula, not cute. The X-ray `#9fe6ff` ink keeps a clean outline. |
| 7 | megarachne | APPROVE. Round head shield, comb rakes, stubby back end. Nothing like `jaekelopterus`. |
| 8 | giant_tarantula | APPROVE. Lighter, pinker and smaller, so it reads beside the 1980 spider (s073). |
| 9 | mazothairos | APPROVE. The beak is clear and points down and forward, the banded wings are good, and there are no winglets. Optional (not blocking): splay the wings a little wider so it reads less like a folded moth at 0.5 (s096, s111). |
| 10 | six_winged_insect | APPROVE. The winglets behind the head are visible, and the 1-6 number spots land on wings and flaps. |
| 11 | pulmonoscorpius | APPROVE. Heavy and dark, small pincers, arched tail. The red-glow silhouette reads instantly as a scorpion. |
| 12 | pulmonoscorpius_underside | APPROVE. Four pairs of book-lung slits are clearly visible (s161). |
| 13 | hibbertopterus | APPROVE. Very broad, slow and heavy, and works over Doug (s194). Optional (not blocking): its silhouette is close to `megarachne` (s065 vs s178). The two are related, so this is acceptable, but a wider and flatter head-shield edge would separate them further. |
| 14 | hibbertopterus_trackway (flagged) | APPROVE. Two bands of prints, a wavy tail groove, and a readable middle band with Doug inside it at 1.2 (s193/s194). Optional: vary a few print shapes so the paired comma-and-crescent marks read less like a repeated "3)" glyph. |
| 15 | crassigyrinus | APPROVE. Flat eel body, tiny limbs, low toothy head. Reads as "tadpole from hell" and works as a red-rim silhouette (s199). |
| 16 | crassigyrinus_eyes | APPROVE. Lurking eyes on bumps with heavy lids. Reads as not-a-crocodile (s198). |
| 17 | crassigyrinus_skull | APPROVE. Low, flat skull with big teeth in the cream bone palette. Lower and flatter than `crocodile_skull`. |
| 18 | crassigyrinus_old_head | APPROVE. Engraving-plate style that matches `old_hallucigenia_1977`. Tall, narrow, moray-like head. |
| 19 | arthropleura_fossil_boulder | APPROVE. Split sandstone block with a segmented plate strip that matches `arthropleura`. |
| 20 | doug_silhouette | APPROVE. Reads as Doug from the outline alone (cap brim and big head). Grey with no red, as specified (s039, s082, s122, s179). |
| 21 | cupcake_candle | APPROVE. |
| 22 | candle_flare | APPROVE. A good roaring column with no smoke over faces (s027). |
| 23 | fire_flames | APPROVE. |
| 24 | bug_net | APPROVE. Works in s141. |
| 25 | bathtub | APPROVE. Optional: the plug chain is barely visible. Not needed for s179. |
| 26 | bicycle_wheel | APPROVE. |
| 27 | ukulele | APPROVE. Four pegs, clearly not `guitar`. |

## Notes for the director (composition, not asset fixes)

- **s170**: the `fallen_log` is drawn over `pulmonoscorpius`, so the "about as long as the log" comparison can't be read. Put the log and the
  scorpion side by side, or one above the other with their left ends lined up and no overlap.
- **s141**: Doug overlaps the middle `scale_tree` trunk, and the net hoop is hidden under Meganeura. Move the tree or the group so that Doug
  hangs against open background.
- Ink recolour (`ink: #4a4a4a`) changes only the outline. The fills keep their colours (bojophlebia s046, megarachne s077, crassigyrinus
  s206). To make a fossil read as a fossil, put it on a grey slab and/or use a grey wash behind it. This is a shot choice, not an asset fix.
