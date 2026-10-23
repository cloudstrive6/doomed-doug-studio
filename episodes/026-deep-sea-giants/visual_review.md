# Visual review: 026-deep-sea-giants

(The round 1 findings, 17 fixes, are in git history at commit e904f67.)

## Round 2: pre-render keyframes + thumbnails re-screen (2026-10-23)

Screened: all 24 re-rendered contact sheets (s001-s281 + endslate). All keyframes date from 18:16-18:17, after the
18:15 shotlist. I viewed the changed shots at full 1080p: s071, s161, s177, s203, s238, s254, s145. I also viewed
`build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` and their `_small` files. The `_small` files are now a
true 168x94. I checked them at real size side by side as a feed mock, and at 4x nearest-neighbour.
Title in `metadata.json`: "Why the Deep Sea Grows Giants Big Enough to Kill Doug".

VERDICT: PASS

### Round 1 blocking fixes: all resolved
1. **s213**: fixed. The sea spider now sits on the mud inside a white magnifier ring, the A FEW MM arrow points at
   the ring, and Doug crouches looking at it. The key subject reads in 1 s.
2. **s177, s238, s254, s272**: fixed. "BRING YOUR / OWN FOOD" wraps and sits inside the paper. In s177, s238 and
   s254 the glove holds the right rim below the text. s272 has no hand.
3. **s161**: fixed. The red title sits on clear water above the worms. It is no longer red on red.
4. **s023**: fixed. ROBOT SUBMARINE sits to the right of Doug and does not cover him.
5. **s018**: fixed. PREDICTS NOTHING clears the map frame.
6. **s262**: fixed. The blood cell is bigger and has a BLOOD CELL label with an arrow.
7. **s165**: fixed. Doug hangs in clear water between the smoker and the door.
8. **s203**: fixed. Doug's pose is now elbows out with forearms down, matching the squid. BLEND IN sits at about
   y 320, clear of the fins, the filaments and the mud.
9. **Variety runs**: fixed. Each run is broken by a different framing: s072 (REC camera crop on the bell and
   brotula), s164 (tight on the plumes), s204 (push-in on Doug and the squid), and s222 and s224 (tight on the
   spider's leg and heart). No run is now 4 or more near-identical shots.
10. **Thumbnail C**: fixed. All six labels are one size. "Colossal / Squid" and "Greenland / Shark" wrap, and all
    labels read at 168x94. "One Cell" is left-aligned, so the duration badge's corner is clear.
11. **Thumbnail B**: fixed. Jelly and Doug are scaled up, and Doug's face sits in the centre third. The stray stub
    is gone. The cable now runs to Doug's lanyard and harness. At 168x94 the cap, face and text read clearly.

Also resolved from the minor list: 12 (s012 ripple), 13 (s027/s065/s190/s206 wordart clear of the creatures),
14 (s057/s185/s253 titles), 15 (s071 brotula silhouette lifted above the bell, red rim, reads as a fish) and
16 (s013/s014/s018 now Doug on the beige explainer background).

### Checks this round
- Doug is on-model everywhere (red cap, white head) and readable on every zone colour. Capless shots are on purpose.
- The counter runs 210 to 218 in order. Deaths are cartoon only (X eyes, ghost Doug, frost ball). No gore.
- Tone is adult deadpan, not a nursery show. All text I checked is spelled correctly and nothing is cropped.

### Thumbnails at 168x94
- **A (HOOKS):** the strongest. One focal point (the eye), with Doug and the hooked arm clear. It is honest, because
  Doug dies to the hooks at s133-s134.
- **B (10 METERS):** now a valid test. Doug's face and red cap are the focal point, and the threat wraps him. The
  10-meter arms are real (s061).
- **C (6-tile grid):** a clean list control. Every label and creature is readable.
All three fit the title and none is misleading.

### Minor, not blocking (fix only if the director touches these shots again)
1. **s136-s159** (art director): the frosted cable is still the original `#eef6ff`, width 13, dash [22, 9]
   (`build/gen_shotlist.py` `dc(..., frost=True)`). It also still switches on and off: frosted in s136-s147, s150,
   s153 and s159, but plain in s148, s151, s152, s154, s155, s157 and s158. At 1080p it now reads as a frosted cable
   rather than a zipper, so this is continuity only. Either frost every on-cable shot in the chapter or drop the
   frost before s148.
2. **s074, s166, s167, s231** (director): small overlaps. LIVE TOGETHER touches the jelly bell's left edge. Doug's
   cable runs through "1977" and through the "G" of SUPERGIANT AMPHIPOD. The GALAPAGOS label touches a plume. All are
   still readable. Nudge each 40-60 px if convenient.

### Not yet screened
Post-render checks (`build/samples/`, `build/qc.json`, final.mp4) and the Shorts. Neither exists yet, so they come
in the next round after render.
