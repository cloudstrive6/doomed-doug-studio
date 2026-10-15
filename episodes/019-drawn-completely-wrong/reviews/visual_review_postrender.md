# 019-drawn-completely-wrong: post-render visual review (2026-10-15)

What I checked: all 33 frames in `build/samples/` (one every 30 s, at t = 15 + 30n). `build/qc.json` reports 985.2 s
and no problems. I also checked `build/thumbnail.png`, `build/thumbnail_small.png`, `metadata.json`, the three Shorts
previews, the last 10 s of each Short at 1 fps, and a full-res end card from each Short. I ran the engine's
`camera_rect` over every zoom shot in `shotlist.json` to find text that the camera crops, then pulled the last frame of
each flagged shot from `final.mp4` to confirm. I did not render anything.

VERDICT (main): FAIL
VERDICT (shorts): FAIL

## Main video

No black or blank frames, no frozen shots and no glitches. Doug is on-model in every sample, and there is no gore or
kids'-show tone. The counter steps 154 to 161 in order and the chapter HUD matches each topic. Pictures match the
narration at every sample point. For example: s098 "60-90 cm" points at the tail spikes, s143 "20 cm CLAWS", s160
"WITHOUT CLAWS" shows the fish being caught, s242 shows the ÖHNINGEN circle, and s279 says "TOO BUOYANT".

### Required fixes
1. **s092, s098, s108, s139, s143, s250 (director): the zoom-in crops the DOUG DEATHS counter.** The counter label
   sits at x 1364-1816. At `zoom: 1.08`, the camera targets (`x` of about 500-850) put the right edge of the frame at
   x 1778-1789. That cuts off the last digit for the whole end of the push: "DOUG DEATHS: 15", "...: 16" (s250), and a
   half digit in "156" (s108). This was confirmed in final.mp4 frames and in sample f_011 (s098) and f_016 (s143).
   **Fix:** set `camera.x` to 960 in each of these six shots and leave `zoom`/`y` unchanged. The right edge then lands
   at x 1849. The zoom subjects (tail spikes, claws and so on) all stay in frame.
2. **s007, s015, s043 (director), lower priority but do it in the same pass:** at `zoom: 1.06` with `x: 900`, the
   right edge is x 1811. The digits survive, but the label's right border is shaved off (sample f_001). Set
   `camera.x` to 960.

This is the same defect as 013 post-render fix 1, which was a FAIL there too.

### Advisory (not blocking)
- s242: at map scale 4.0, the `world_map` mountain chevron near (1600, 430) reads as a stray green "^" beside the
  scientist. Optional: nudge the map or the scientist so it isn't floating in open land.
- s186: the upside-down fossil cap looks a bit like a bum-bag on its own. It reads correctly after s185 (red cap),
  so leave it.

### Thumbnail: PASS
Archetype A grid with 11 red-X'd old reconstructions and chapter-name labels. No title words are repeated, and it
complements "...Scientists Drew All Wrong" without being misleading. At 320 px (`thumbnail_small.png`) the tiles,
X's and most labels still read. There is no Doug, which the style bible allows for a grid thumbnail ("sells the
subject, not the mascot"). Unchanged from round 1.

## Shorts

All three have readable titles, clean subtitles (word-by-word captions), drawings not cut off at the sides, the
@DoomedDoug tag, and an end-card arrow pointing down to the link.

- **short01 (Brontosaurus, 59.6 s): PASS.** The 1932/1979 head swap pays off the title. The outro opens one specific
  question ("what did Doug find instead?") that the clip doesn't answer. The red-rimmed sauropod silhouette is
  recognisable from its long neck and tail. It inherits the minor s015 border shave (fix 2).
- **short02 (Dimetrodon, 53.7 s): PASS.** The relatedness claim is paid off with the skull opening and the family
  tree. "WHERE DID DOUG'S CAP END UP?" isn't answered, and the sail-backed silhouette is clearly Dimetrodon with no
  cap visible.
- **short03 (Spinosaurus, 48.9 s): FAIL. The silhouette can't be recognised.** At end-card size, the
  `spinosaurus_mystery` silhouette is a lumpy black mass: the double-hump sail reads as boulders and the raised snout
  as a mitten or arm, and the "???" covers the middle. Nothing says "Spinosaurus", so "WHICH SPINOSAURUS CAME OUT?"
  has no recognisable teased creature. I flagged this risk as an advisory in pre-render round 2. The payoff and outro
  are otherwise fine, and the Short doesn't answer its own question.

### Required fix (short03)
3. **short03 `tease_asset` (illustrator, then director):** leave the main video's `spinosaurus_mystery` alone, since
   s286/s288 work in context and changing them would force another main re-render. Instead:
   - The illustrator adds a tease-only variant, `spinosaurus_mystery_tease`. Keep the same "matches no card" body,
     but give it a readable Spinosaurus profile: a long, low croc snout in side view with a tooth-row notch, and one
     continuous tall sail rather than two humps.
   - The director sets `shorts.json` → short03 `tease_asset: "spinosaurus_mystery_tease"`. Keep `tease_from: s288`
     and the end-card text.
   - Re-render short03 only.

   Do not use one of the four card assets (`old_spinosaurus_1915/2014/2020/2022`). The outro says the creature
   "matched none of the four cards", so a card silhouette would mislead.

## Routing
- Director: fixes 1, 2 (shotlist camera.x), then fix 3 (shorts.json). Then the editor re-renders final + short01 +
  short03, and they come back to me for a final recheck.
- Illustrator: fix 3 asset.
- Graphic designer, art director: nothing required.
