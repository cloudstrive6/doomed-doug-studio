# 053-deadly-harmless-plants: visual review

## Round 3: regenerated thumbnails A/B/C and s001 (2026-11-20, visual screener)

Scope: `build/thumbnail.png`, `thumbnail_b.png` and `thumbnail_c.png` at 1280x720, as fresh 168x94 downscales, and
as the delivered `_small` files (all 168x94, all written in the same run). Keyframe s001 at full size, with s013
for comparison. Earlier rounds cleared the rest of the keyframes for render.

VERDICT: PASS

### Thumbnail C (`thumbnail_c.png`, NOT PARSNIP): round-2 fix verified

- The full-height plant is gone, so nothing is cropped at the top edge.
- Doug, the pot and the fire are now large and sit at left-centre. Doug's head is about 120 px at full size and
  clearly visible at 168 px. The red cap pops against the purple, and his smile plus the stirring stick read as
  "happily cooking".
- The root now matches s013: a green-banded crown with pale tubers hanging down. It sits big in the basket at
  right. Next to `NOT PARSNIP`, it reads as "a root vegetable that is not what he thinks".
- The text is crisp, top-right, and does not overlap anything. The field guide was dropped, which round 2 allowed.
- No gore. The image is not misleading, since water hemlock is the s003-s018 chapter.
- Nits, not blocking: (a) the grainy speckle on the steam, pot and fire is the engine's glow texture. It is
  invisible at feed size. (b) Doug's feet run off the bottom edge.

### Thumbnail A (`thumbnail.png`, WRONG TREE): pass

- Doug is bigger and reads at 168 px. The single focal point is the banded tree with Doug under it, with the drips
  falling onto his cap. The text is clean.
- Nit carried over (illustrator/graphic designer, optional): his seated legs are still two long thin lines sticking
  out to the left, and at feed size they read like a stick on the sand.

### Thumbnail B (`thumbnail_b.png`, JUST RAIN): pass

- The peel flakes are gone. The head is flat pink with a shocked face, the white sap drops are obvious, and the
  storm contrast is the strongest of the three.
- Nit (graphic designer, optional): a jagged red outline is left under the chin, around the lower half of the head
  at about x 650-770, y 540-580. It looks like a leftover from the flake shape. It is about 1 px at feed size, but
  at full size it could read as a raw or rash edge. Remove it, or redraw it as the normal black head outline.

### s001

- It is identical to thumbnail A, rendered at 1920x1080. Doug is on-model and there is no gore.
- The narration ("One North American root...") does not match the beach-tree picture. This is the accepted
  convention (thumbnail as opening image, about 2 s), and s002 names the tree straight away, so it is not blocking.

### Still open from earlier rounds (not blocking, not re-checked)

These were not re-checked: items 9, 10 and 13, the s035/s036 SAFE-box nudge, and the s079 cap scale.

Route: none required. The packaging can go to `package check`, and the keyframes can go to render.

## Round 4: post-render (final.mp4, thumbnails, Shorts), 2026-11-20, visual screener

VERDICT (main): PASS
VERDICT (shorts): PASS

### Main video (`build/samples/f_001-f_024`, `build/qc.json`)
- qc.json: 728.2 s, `problems: []`. None of the 24 samples are black, blank, frozen or glitched. Each chapter label matches
  its timestamp in chapters.txt, and the death counter climbs 391 → 396 in order, ending on the `DOUG DEATHS: 396` card
  (f_024).
- The pictures match the narration where I spot-checked them against timing.json: f_002/s011 soup mix bag, f_003/s020
  church yew, f_005/s037 "cherry jelly sweet", f_013/s102 "Doug is fine. Eventually.", f_020/s157 herbarium
  sheet "still wins".
- Doug is on-model in every frame: red cap, white head, and a flat-pink head only in the flushed/sunburn beats. No gore. The mad-honey
  soldiers (f_013) are lying down, not bleeding. The hogweed skin layers (f_017) are a flat diagram. Nothing reads as a kids' show.
- The text is legible and nothing is cropped. The small `CONTACT:` HUD labels are tiny, but they are a secondary element.
- Nit (art director, optional, not blocking): s020 (f_003) has a grainy grey glow behind the black yew silhouette. It reads a little like
  dirt or smoke on the grass. It is the intended silhouette-reveal style (art_review.md), so I am leaving it.

### Thumbnails (A/B/C at 1280x720 and 168x94)
- **Earlier decisions.md items, confirmed fixed:**
  - B: the peel flakes are gone. The head is clean flat pink with a normal black outline. The jagged red chin edge from round 3 is
    gone too.
  - A: Doug is scaled up and moved under the canopy edge. The drips land on his cap, and he reads as a figure at 168 px. The canopy-top
    speckle is gone.
- A (WRONG TREE): one focal point. Banded tree, Doug under it, yellow text clear at feed size. It pays off the title. Carried-over
  nit (seated legs read as a stick) still applies, optional.
- B (JUST RAIN): strongest contrast of the three. White sap drops and a shocked pink Doug are obvious at 168 px.
  Nit (graphic designer, optional): **no red band on the trunk**, unlike A, s164 and short01. The brief says "the same banded
  tree". Add the `#e02020` band at the trunk height used in A, so all arms show the same tree.
- C (NOT PARSNIP): reads at feed size. No change since round 3.
- None of the three are misleading, and none show blisters, rash or gore.

### Shorts (`build/shorts/short01-03`, 1080x1920, 37.2 / 38.8 / 57.9 s)
- I checked the previews plus 6 frames per Short (0.5 s, 4 s, 12 s, 55 %, end-4.5 s, end-0.6 s).
- Titles are legible: red with a dark outline, 2-3 lines, and nothing cut at the edges. Subtitles are large white with an outline. The
  word-by-word reveal cuts words mid-word in the stills ("enou"), which is expected.
- No drawing is cut off at the sides. In short01 at 0 s, Doug sits at the far left (about x 50-110), fully in frame.
- The end cards are clean `FULL VIDEO: TAP BELOW` cards with Doug pointing and a red arrow pointing straight down. There is no "???" teaser.
- Each payoff is delivered before the end card. short01 is the manchineel's sap/rain danger ("anything with" sprinkler beat). short02 is the 2020
  hot-dog test result (TOO WEAK), then the leaves death "Doug has died." short03 is the 100-year herbarium sting ("and it still
  wins"), with the spider and cone-snail comparison drawn.
- No gore. The oleander death is a cartoon car/traffic gag.
- Nit (director, optional): short01 opening, the red `The Manchineel` title-card text sits on the top of the canopy. It stays legible,
  but it would be cleaner about 40 px higher.

### Non-visual note (youtube-titler / creative director, not a visual-gate item)
- metadata.json `"playlist": "parasites"` files a plants episode under "Doug vs. Parasites". No playlist in channel.yaml fits
  plants. Decide whether to add one (for example "Doug vs. Plants") or pick the closest one deliberately, before upload.

Route: none required. The optional nits are B trunk band (graphic designer), short01 title-card position (director) and s020 glow
(art director).
