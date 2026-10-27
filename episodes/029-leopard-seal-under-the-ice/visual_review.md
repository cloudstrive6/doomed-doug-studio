# 029 Leopard Seal Under the Ice: visual review

## Round 1: pre-render (keyframes + thumbnails), 2026-10-27

Inputs checked: all 23 contact sheets (s001-s264 + endslate), `build/thumbnail.png`, `thumbnail_b.png` and `thumbnail_c.png`,
plus their `_small` versions at feed size (168x94). Title: "How the Leopard Seal Kills Doug From Under the Ice".

VERDICT: FAIL

The picture is mostly clean and on-model. There is no gore, the tone is not kids' show, the Snorkeller is handled soberly (no Doug,
no counter) and the death beats are cartoonish. The blocking problems are a few shots where the picture contradicts or misstates
what is said, one shot that implies a real person died, and thumbnail packaging.

### Blocking fixes

1. **s094, s095, s096 (director):** the narration and the "WAIST DEEP" label say Doug is standing waist deep, but his whole body,
   legs included, stands on top of the water ripple. Lower Doug so the waterline cuts him at the waist: draw the water rect (or a
   water-coloured mask) over his legs, with the ripple ellipse at hip height.
2. **s144 (director):** a red X over Paul Nicklen, a real living person, for "couldn't catch anything on its own" reads as "he
   died". Remove the X. Use a "0" tally or a "CAN'T HUNT" label next to him, or a penguin swimming past his empty hands.
3. **s224 (director):** the line "earns its reputation from penguins and seals, not from people" plays over the "JULY 2003 /
   ONE PERSON DIED" card. The last thing the viewer sees contradicts the reassurance, which is a packaging-honesty risk on a
   real death. Use a new sober card instead, e.g. "ITS REPUTATION: PENGUINS AND SEALS. NOT PEOPLE." (same `#15181a` style, white
   text, no Doug).
4. **s022 (director):** the narration is "and shot it", but the frame is the empty 1916 floe with no Frank Wild, no rifle and no
   seal. Keep Wild (from s021) aiming the rifle at the seal at the floe edge, with a small "BANG" burst at the muzzle. Show no
   blood or wound, only the cartoon shot.
5. **Thumbnail A, `thumbnail.png` (graphic designer):** at 168x94 the "his shadow" idea is lost. The shadow is a small grey
   ellipse that sits on top of the seal's snout, and the snout pokes through the waterline into the white ice band, so the seal
   reads as surfacing, not as lurking *under* the ice the title promises. Fixes:
   - Move the seal down and left so its head is clearly below the floe's underside, with a visible gap of dark water.
   - Make Doug's shadow on the floe underside larger and darker, directly under Doug's feet, so the seal's eye lines up with it.
   - "IT FOLLOWS" sits about 20 px from the bottom edge. Raise it by about 30 px.
   - Keep the yellow-over-dark-blue split, which reads well.
   s001 reuses this image, so the change carries into the opening.
6. **Thumbnail C, `thumbnail_c.png` (graphic designer):** the four-panel grid has no single focal point. At feed size, Doug is
   about 8 px in each tile, and the "Sieve" tile reads as a seal plus pink noise. Either drop C from the A/B test or redo it
   as a single hero image. Thumbnail B ("CORNERED": Doug on a floe with the reptile head rising) is the strongest of the three at
   feed size. It has one focal point, Doug and the threat are obvious, and it avoids title words. I recommend B as the lead or the
   main challenger.

### Recommended fixes (non-blocking, but do them if time allows)

7. **Variety (director):**
   - **s007-s022:** 16 consecutive shots use the identical inset-1916-panel-plus-Doug-on-the-right composition, about 50 s. Within
     it, **s015-s020** (the shadow-tracking beat) should go full-frame on the floe cross-section, with no inset and no Doug on the
     side. This is also the episode's key idea.
   - **s037-s041, s046-s048, s056-s057:** the same row of 8 penguins with Doug at the edge. Change the camera on 2-3 of them, e.g.
     a low underwater view of the 10-20 m strip for s047, or a close-up of Doug at the edge for s057.
   - **s133, s136-s139, s143-s144:** the diver on the left, the seal in the middle and Doug at the bottom right, repeated. Push in
     on the seal and penguin for s138/s139.
8. **s071-s083 marina (director):** Doug stands on the sailboat directly behind the left piling. His body merges with the white
   hull and the post cuts his cap brim (worst in s073, s074 and s083). Move Doug about 120 px left, clear of the post, or
   stand him on the pontoon.
9. **s099 and s182 (illustrator/art director):** the red-outlined tease silhouette has **red ripple rings** at its waterline.
   Next to the black shape, they can read as blood in the water. Make the ripples white or light blue and keep the red only on the
   rim.
10. **s155, s161-s164, s169, s172-s173 sieve head (illustrator):** the pale grey head-with-teeth asset reads as a generic
    whale or ghost blob, not a leopard seal. Add the seal's spot pattern, darker dorsal shading, a nostril and whisker dots, so
    viewers connect it with the reptile head they saw in "The Head".
11. **s182-s188 Cape Shirreff beach (director/illustrator):** the dark-brown fur seal pups on the dark-brown beach (`#6b5b4b`) are
    low-contrast and hard to count, which matters because s185 circles 7 of them. Lighten the beach (e.g. grey-tan `#a59a88`) or
    give the pups a light outline.
12. **s258 (director):** the faded "MAYBE" letters show around the red "NO", so it looks garbled ("M NO E"). Either strike MAYBE
    through clearly with a red line before stamping NO, or cover it fully.
13. **s179 (director):** the floating sign is blank, but s177 established that it says "KRILL". Add the KRILL text so the gag
    carries.
14. **s252-s256 (art director, low priority):** upside-down Doug with the cap at the bottom reads at a glance like a red-and-white
    fishing float. It is within the ceiling-hang convention, so this is not blocking. If you change it, tilt the head about 20
    degrees or add a few bubbles from the mouth, so it reads as a face.

### Checked and fine

- Doug is on-model (red cap, white head) throughout. His deaths are cartoon: silhouette, black cut, ghost and cap (s029-s031,
  s066-s067, s123-s124, s178-s180, s209-s210, s257-s262). There is no blood, no organs and no penguin shown caught.
- The text is legible and spelled correctly, with no cropping. "ENORMOUS GAPE" (s105) sits close to the counter box but does not
  overlap it.
- The Snorkeller block (s212-s223) has no Doug, no counter and no joke, which is respectful.
- The endslate is clear, and the arrow points to the next-video slot.
- s030 and s257 black frames and the s123 flash frame are intentional silent death beats (0.4-0.5 s), not glitches.
