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

## Round 3: post-render (final.mp4, thumbnails, Shorts) (2026-10-23)

VERDICT (main): PASS
VERDICT (shorts): FAIL

### Main video (build/samples f_001-f_033, build/qc.json)
- qc.json: 983.75 s, `problems: []`. No black, blank or frozen samples. Every sample has a different composition.
- Every frame has the item title card, the DOUG DEATHS counter (210 to 217 in order across the samples) and the
  CABLE OUT tag (250 m to 10,641 m). Nothing is cropped and all text is spelled correctly.
- Doug is on-model and readable in every sample, including the small cable shots on near-black (f_014, f_023, f_030).
  The deaths are cartoon only: the floating ghost with the cap knocked off (f_009, f_021) and the cap left over the
  amphipod swarm (f_029). There is no gore and nothing reads as a kids' show.
- f_033 end screen: the two dark boxes are the YouTube end-screen element slots, as intended.
- Thumbnails: A (HOOKS, eye + hooked arm + Doug), B (10 METERS, phantom jelly) and C (6-tile grid) all read at
  168x94. Each has one focal point, fits the title "Why the Deep Sea Grows Giants Big Enough to Kill Doug" and is not
  misleading. No change from round 2.

### Shorts (1080x1920; frames at 0.5 s, 3 s, 10 s, mid and the last ~9 s of each)
- The titles are readable, the subtitles are legible, the @DoomedDoug tag is clear, and the end-card arrow points down
  every time.
- short01 (colossal squid, 31.9 s): pays off its title (1925-2025 timeline, then the 30 cm juvenile). The outro tease
  ("what did the hooks grab first", s132) is not answered. The hooked-arm silhouette is readable. PASS.
- short02 (Greenland shark, 41.9 s): pays off with "392 YEARS OLD" and the 1620 Mayflower shot. The slow-shark
  question is open and the shark silhouette is clear. PASS.
- short03 (giant isopod, 50.3 s): pays off with the 5 YEARS aquarium and FEB 2014 calendar. The stethoscope/leg question
  is open and the sea-spider leg silhouette is clear. PASS.
- short04 (oarfish, 46.1 s): pays off with the crossed-out Japan map. **FAIL on the end card.**

### Required fixes (shorts)
1. **short04 end card** (director: `shorts.json` `tease_from`/`tease_asset`/`outro`/`end_card`). The
   `xenophyophore` silhouette is a lumpy black blob with a red rim. Without the colour drawing it reads as a rock or a
   cloud, not a "thing", so the tease is vague. Its large red glow is also cut flat along a hard horizontal edge at
   about y=1315 (sampled at 44.5 s: the glow is about rgb(84,30,23) at y=1300 and background at y=1318). That looks
   like a glitch. Re-point the tease at something recognisable that the clip doesn't answer. Recommended:
   `tease_from: "s251"`, `tease_asset: "supergiant_amphipod"`,
   outro e.g. "The oarfish only ignored Doug. Six kilometers deeper, he lowered a sandwich as bait. Something answered.
   Full video below.", `end_card: "WHAT CAME FOR DOUG'S SANDWICH?"`. The shrimp-shaped silhouette reads instantly and
   is smaller, so the glow fits. If the director wants to keep the giant-cell tease instead, the silhouette must
   become recognisable (for example the cell outline beside Doug for scale), and the glow must not be clipped. Then
   re-render short04 only and re-screen its last 8 s.

### Minor, not blocking
2. short01 end card (director): the "???" sits across the hook arm and covers about half of the hooks. Move the "???"
   above or to the right of the silhouette if the end-card layout allows it.
3. short02 at about 10 s (the eye zoom, "2016: 28 SHARKS"): the shark's tail runs off the left edge. This comes from
   the camera zoom in the source shot and still reads. Leave it unless the shot is touched again.

## Post-render, round 2 (short04 re-render; 2026-10-23)

### Main video (quick re-check)
- qc.json `problems: []`. Re-viewed samples f_002, f_012, f_021, f_029: all clean, Doug on-model, the counter and
  cable tags are correct, deaths are cartoon only. build/thumbnail.png (HOOKS, eye, hooked arm, scared Doug) is
  unchanged and still reads: one focal point, Doug and the threat are obvious. No regressions.

### Shorts
- short01-03 previews: unchanged since round 1 and still fine. The titles and the @DoomedDoug tag are readable and
  nothing is cut off at the sides. The preview subtitles stop mid-word ("nobody filme", "three hundre", "twenty fou")
  because the still is grabbed during the word-by-word reveal. In the video the full words show. Not a defect.
- short04 (oarfish, 46.4 s). Frames checked at 0.5, 3, 10, 23, 35 s, then every 1.5 s from 37.5 s to 46.2 s.
  - Body is unchanged from round 1: the title is readable, the subtitles are legible, the oarfish is complete and the
    crossed-out Japan map pays off the title.
  - The outro ("The oarfish only ignored Doug. Six kilometers deeper, he lowered a sandwich as bait. Something
    answered.") opens one specific question that the clip does not answer.
  - End card: "WHAT CAME FOR DOUG'S SANDWICH?" is legible. The supergiant_amphipod silhouette reads immediately as a
    segmented crustacean, with antennae, legs and tail fan inside a red outline. The red arrow points down, and Doug
    is on-model to the left.
  - Glow: a circular, dithered radial fade that is fully inside the frame. On a 44.5 s full-res frame the columns
    and rows decay smoothly to the background (11,11,19), with no flat horizontal cut. The round-1 hard clip is gone.
  - Minor, not blocking: as in short01, the "???" sits across the middle of the body. The head, antennae, legs and
    tail still carry the shape.

### Fixes
None required. Round-1 minor notes 2 and 3 (the short01 "???" placement and the short02 tail edge at about 10 s)
stay optional.

VERDICT (main): PASS
VERDICT (shorts): PASS
