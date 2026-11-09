# 042 anaconda-no-venom: post-render visual review (round 1, 2026-11-09)

VERDICT (main): PASS
VERDICT (shorts): PASS

Scope: build/final.mp4 (1920x1080, 656.5 s; qc.json has no problems), 22 samples (build/samples/f_001-f_022), extra frames at 617-639 s (ending) and 435 s (s118 jaws at full res), thumbnails A/B/C and their _small versions, metadata.json, and short01/02/03 (.mp4 at 7 points each, plus previews).

## Main video
- No black, blank, frozen or glitched frames. Every sample matches its narration: s006 female, s011 HER (man-sized) vs HIM (suitcase), s020 tape measure, s028/s036 drinkers at the bank, s045 1-13 males, s062 backwards teeth, s070 capybara bite scars, s079 prey in coils, s085 4x slower, s101 smartwatch, s124 1992 deer, s132 1999 caiman, s139 5 hours, s156 thesis, s162 claim the prize.
- Doug is on-model in every frame (red cap, white head). Topbar, death counter (322 -> 329) and hunt-stage badge are legible and uncropped in every frame.
- Gore: s118 (inside the jaws) has a dark-red dot at the end of the pink windpipe. At full res it reads as the glottis opening, not blood. OK. s124: the deer lies intact with no wound. s164-s168: Doug's death is shown only by the floating cap and a hump. No gore, and nothing has a kids-show tone.
- Ending pays off and ends cleanly: s166 WEEKS OR MONTHS, s168 NOT SWALLOWED (the cap), s169/s170 "NO VENOM. NO NEED.", s171 CTA, then the standard end slate (arrow to the video slot, SUBSCRIBE circle). The s147 "ONE HUNT LEFT ?" is a mid-video transition and the hunt is shown in full, so it is not a withheld-payoff teaser.
- "ú" in "Jesús" (s007): the main video has no burned-in subtitles. Captions are the sidecar build/captions.srt, which is valid UTF-8 with "Jesús" correct on line 31, and YouTube renders it. The s007 frame has no on-screen text with the name. The engine's subtitle font (font(84,"default",True) -> assets/fonts/Arimo.ttf, the one Shorts burn in) draws ú and Ú correctly: a test render of "biologist Jesús Rivas" / "JESÚS" shows the acute accent, not a tofu box (the ú bbox is 62 px tall against 45 px for u, and differs from the .notdef glyph). s007 is the only non-ASCII narration line and it is not in any Short.

## Thumbnails (A NOT A LOG / B IT SQUEEZES / C TWO BUMPS)
They are unchanged since rounds 4/5 PASS. All three are readable at 168x94 with one focal point, Doug plus the threat, and text that complements the title without repeating it. None is misleading. B is still the strongest lead.

## Shorts
- short01 (s087-s093), short02 (s150-s157), short03 (s136 hook + s138-s146): all 1080x1920, at 30.5, 38.5 and 42.9 s. The red titles are fully legible within 3 lines. The burned subtitles are big, white with a black outline, and max 2 lines. The scene band is not cut off at the sides in any sampled frame (the REWARD poster in short02 and the coil in short01 sit inside the frame). Each ends on FULL VIDEO: TAP BELOW with a red arrow pointing straight down. Every title is paid off inside the clip: short01 says "Air was never the problem" then Doug dies; short02 says "Nobody ever tried to claim it"; short03 shows the 5-hour fight and the dead male five days later. No "???" card.

## Notes (non-blocking)
N1. **Director, short03 hook (s136 scene).** The first frame ("Anacondas eat caimans...") shows a small caiman with a tiny snake at its jaw, and a ~20 px Doug at the far left edge. At phone size the snake is barely visible. Next time, use a hook scene with a bigger snake-vs-caiman subject (e.g. the s132 coil-around-caiman, scaled up).
N2. **Editor, short02 s154.** The road in the scene runs into the subtitle zone, so the lower half of the frame is flat grey. Subtitles stay legible. Cosmetic only.
N3. **Editor, preview stills.** short01/short03 previews catch the subtitle mid-reveal ("to wa", "mistak"). The videos are fine. The previews could be taken at a shot boundary.

Re-screen needed: none.
