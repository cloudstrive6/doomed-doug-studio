# 023-hippo-every-era: post-render visual screen

Screener: visual-screener · 2026-10-19 · nothing re-rendered.

## Inputs checked
- `build/final.mp4` (990.3 s, 1920x1080); `build/qc.json` reports `problems: []`
- `build/samples/f_001..f_033` (one every 30 s, starting at t=15 s), mapped to shots using `build/timing.json`
- `build/thumbnail.png`, `build/thumbnail_small.png`, `metadata.json`
- `build/shorts/short01-03.mp4` (1080x1920; 54.9 / 57.2 / 46.6 s), `*_preview.png`, and frames from each Short at 1, 8, 20 and 35 s and at end-8/5/3/1.5 s (full-res end cards)

## Main video
No black, blank, frozen or glitched frames. Top bar (chapter name, DOUG DEATHS 186 to 195, HIPPO SURVIVED x/12) is legible and consistent the whole way through, and the counter only ever goes up. Doug is on-model in every frame (red cap, white head), and ghost/dead poses are used for the deaths. Creatures are easy to recognise: hippo, cave lion, Purussaurus, Ambulocetus, Titanoboa, Triceratops, T. rex, Allosaurus silhouette, sauropod, gorgonopsian strip, Hyneria, Climactichnites. No gore and no realistic violence. Nothing reads as a kids' show: the "cousin?" party-hat portrait is a dry gag, not a nursery one. Compositions vary from frame to frame, with no run of 4 or more near-identical layouts.

Minor defects. None of these block the release; fix them if the episode gets re-rendered for any other reason:
1. **s295** (t≈972-977 s, last payoff shot, director): the `flag_doug_was_here` asset has `rotate: 70`, but its text does not rotate with it. "DOUG WAS" runs off the right edge of the flag and "HERE" is drawn on top of it, so the text looks garbled. Fix: set `rotate: 0` (stand the flag upright in the ground) or remove the rotate, so the text sits inside the flag.
2. **s102** (t≈314-316 s, director): when `ambulocetus` (x1300, rotate 12) appears at 0.7, it is drawn on top of `croc_eyes_water` (x1450). Two creatures stack into one muddle, and the Ambulocetus legs float above the waterline. Fix: remove `croc_eyes_water` from s102, or move it to x≈1750, clear of the Ambulocetus.
3. **s156 / s295 chalkboards** (director): "HIPPO SURVIVED" (size 59 at board scale 0.7; size 50 at scale 0.6) fills the board edge to edge and touches the left inner frame. Fix: drop the text size to 50 and 43 respectively. Cosmetic only.
4. **s026** (t≈73 s, director): Doug stands exactly on the TODAY/THEN divider at x=960, so the black line runs through his body. Fix: move him to x≈1060 on the THEN side. Cosmetic only.

## Thumbnail
"BAD TIMING" is large, high-contrast and readable at feed size (320x180). The hippo (side-eyeing, mouth shut) and the T. rex head nose-to-nose are clear at a glance, and Doug's red cap on the hippo's back still shows at small size. The text uses no title words, it fits the title's question, and it does not mislead: the episode contains a T. rex stop. The duration badge in the bottom-right corner only covers the T. rex neck. PASS.

## Shorts
- **short01** "This Ancient Caiman Weighed More Than Five Hippos": the title is readable, and the payoff is shown (12.5 M / 8.4 TONNES, the caiman next to 5 hippos). The subtitles are legible and nothing is cut off at the sides. The cliffhanger "WHAT DID THE RIVER KEEP?" is specific, and the Short does not answer it. The Purussaurus silhouette has a red outline and still reads as a crocodilian (serrated tail, snout), although "???" covers the middle of it. Acceptable.
- **short02** "Titanoboa Was Longer Than a City Bus": the bus comparison and the 13 M label are shown, so the title pays off. The tease "WHAT FOUND THE HIPPO'S LAST GRASS?" goes with a clear T. rex silhouette that the Short never reveals. Good.
- **short03** "These Dinosaur Footprints Were a Meter Long": the footprint-pool payoff is shown. "WHO DID THE ALLOSAURUS PICK?" goes with a recognisable Allosaurus silhouette, and the choice is never shown (the Short cuts off at "Doug hides behind a..."). Good.
- In all three, the end-card arrow points down toward the link and the @DoomedDoug handle is legible. The subtitle in the short02 preview, "crocodile relativ", is cut short only because the preview still truncates at 40 chars (`studio/shorts.py`). The real video subtitles are complete.

VERDICT (main): PASS
VERDICT (shorts): PASS
