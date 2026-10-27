# 029 Leopard Seal Under the Ice: visual review

## Round 2: pre-render (keyframes + thumbnails), 2026-10-27

Inputs checked: all 23 contact sheets (s001-s264 + endslate, regenerated 18:33 after commit 332a9df). I zoomed into the full-res
keyframes for s022, s073, s074, s083, s092, s099 and s182. I also checked `build/thumbnail.png`, `thumbnail_b.png` and
`thumbnail_c.png`, plus their `_small` versions at 168x94 (1x and 3x). Title: "How the Leopard Seal Kills Doug From Under the Ice".

VERDICT: PASS

All six round-1 blocking items are fixed. No new blocking problems: no gore, no kids'-show tone, Doug is on-model throughout,
the text is legible and nothing is cropped. The items under "Remaining recommendations" are optional polish. Do them if time
allows; they do not block the render.

### Round-1 blocking items: status

1. **s094-s096: fixed.** Doug now stands in the water with the waterline at his waist, ripple rings at hip height, and the oar
   upright beside him. This matches "standing waist deep". The "WAIST DEEP" label (s095) is clear.
2. **s144: fixed.** The red X over Paul Nicklen is gone. The shot now has a "PENGUINS CAUGHT: 0" label and a penguin swimming past
   him. It no longer implies a death.
3. **s224: fixed.** A new sober card on `#15181a` reads "ITS REPUTATION: / PENGUINS AND SEALS. / NOT PEOPLE.", with no Doug and no
   counter. The picture now matches the reassurance.
4. **s022: fixed.** Frank Wild aims a rifle at the seal at the floe edge, with a yellow "BANG" burst. There is no blood and no
   wound. This is clean cartoon violence.
5. **Thumbnail A: fixed.** The seal now sits fully below the floe, with a band of water above its head. Doug's shadow is a large
   dark ellipse on the floe underside, directly over the seal's eye, so "it follows his shadow from under the ice" reads at
   168x94. "IT FOLLOWS" sits clear of the bottom edge. s001 carries the change.
6. **Thumbnail C: accepted.** C is now a 3x2 labeled tile grid (Chase, Visitor, Head, Gift, Sieve, Song). That is the style
   bible's default archetype A, so a grid is valid here and the "single focal point" rule applies per tile. At 168x94 every tile
   subject reads and the labels are just legible. **B ("CORNERED")** is still the strongest at feed size: one focal point, the
   reptile head towering over tiny Doug (now about 0.38x scale), and no title words. A is a clear second.

### Round-1 recommended items: status

- **#7 variety: done.** s015-s020 are now a full-frame floe cross-section (HIS SHADOW / FLOOR / WINDOW), with no inset and no side
  Doug. s041 and s047 are underwater views of the strip, and s057 is a Doug close-up. s135, s138 and s139 push in on the diver,
  seal and penguin. No run of 4 or more identical compositions remains outside deliberate builds.
- **#8 marina: mostly done.** Doug is clear of the piling and the hull in s071-s083 (see recommendation R2).
- **#9 tease ripples: done.** The ripples are white in s099 and s182. The red is now only on the silhouette rim.
- **#11 beach contrast: done.** The beach is lighter grey-tan, so the pups read clearly and the 7 circled pups in s185 are
  countable.
- **#12 s258: done.** MAYBE is struck through in red and NO is stamped below it.
- **#13 s179: done.** The floating sign reads "KRILL".
- **#10 sieve head: not done** (see R1).
- **#14 upside-down Doug: not done** (low priority; see R4).

### Remaining recommendations (non-blocking)

R1. **s155, s161-s164, s169, s172-s173 (illustrator):** this is unchanged from round 1. The pale grey head-with-teeth asset still
    reads as a generic whale or ghost blob, not the spotted, reptile-headed seal from "The Head" (s103-s105) a minute earlier.
    Add the leopard seal's dark dorsal shading and spot pattern, a nostril and whisker dots to that asset. All seven shots update
    together.

R2. **s071-s083 marina (director):** Doug is now clear of the piling, but he has no support. His feet rest on the water surface
    behind the pontoon, between the sailboat and the skyline (clearest in s073, s074 and s083), so he looks as if he is standing
    on the water. Put his feet on the pontoon deck (top of the deck at y about 690 in s073), left of the seal.

R3. **Thumbnail C, Sieve tile (graphic designer):** at 168x94 the red cap inside the red open mouth, surrounded by pink-red krill,
    reads as a red spray around a bite. That is a mild "blood" read on a packaging test. Close the mouth to a grin with the cap
    poking out, or show the krill more orange with fewer specks around the mouth. This is only needed if C goes live in the A/B
    test.

R4. **s252-s256 (art director, low priority):** this is unchanged. Upside-down Doug with the cap at the bottom still reads at a
    glance like a red-and-white fishing float. It is within the ceiling-hang convention. If you change it, add 2-3 bubbles rising
    from his mouth so the head reads as a face.

R5. **s182 (illustrator, minor):** the dark-blue spray halo behind the tease silhouette spills onto the sand as blue speckle
    noise. Clip the spray to the water band or reduce its radius to about 180.

### Checked and fine

- Deaths 235-240 (s029-s031, s066-s067, s123-s124, s178-s180, s209-s210, s257-s262) are cartoon only: silhouette, black cut or
  flash, ghost and cap. The counter steps 234 to 240 correctly. No penguin is shown caught. "First living ones" (s139) uses the
  live penguin darting away.
- The Snorkeller (s212-s224) has no Doug, no counter and no joke. It uses white text on `#15181a`, and the sources line (s216) is
  small but legible at full res.
- s030 and s257 are intentional silent black frames, and s123 is the intentional selfie flash frame. They are not glitches.
- The endslate is clear and the arrow points to the next-video slot. s264 points off toward the next location.
- Spelling: Orde-Lees, Frank Wild, Westhaven Marina, Owha, Whangarei, Dunedin, Palmer Station, Taronga Zoo, Cape Shirreff,
  Rothera, Tracey Rogers and UNSW are all correct.

## Round 3: post-render (final.mp4, thumbnails, Shorts), 2026-10-27

Inputs checked: `build/qc.json` (698.5 s, no problems), all 23 samples `build/samples/f_001-f_023.png`, a full-res frame grab of
s189/s190 from final.mp4, `thumbnail.png` / `_b` / `_c` and their `_small` versions, and the three `build/shorts/*_preview.png`.
From each Short (1080x1920, 61.8 s / 56.1 s / 53.7 s) I pulled frames at 2, 15, 30 and 45 s, plus the last 8 s at -8, -6, -4,
-2.5 and -1 s. I also zoomed into each end card. Title: "How the Leopard Seal Kills Doug From Under the Ice".

VERDICT (main): PASS
VERDICT (shorts): FAIL

### Main video + thumbnail: PASS

- None of the samples has a black, blank or frozen frame or a render glitch. f_019 (The Snorkeller, `#15181a` text card) and
  f_023 (counter 240 on the empty ice) are intended. The chapter tag and the counter are legible in every sample. The counter
  steps 234 to 240 in order.
- Doug is on-model everywhere: red cap, white head. That includes the seal-costume shot (f_018), the pile of Dougs in f_022, and
  the Shackleton-era men in f_001-f_003, who are bearded explorers, not Doug.
- The seal drawings are consistent and recognisable: reptile head, spotted grey coat (f_002, f_009, f_012, f_020, f_021). There is
  no gore and no blood read. The 69% pie (s190) is a rust-orange data fill with no blood read. Nothing looks like a kids' show.
- s189 at full res is fine: the blank white circle is the empty pie, and "SINCE 2010", the seal and Doug are all on screen.
- **Thumbnail A ("IT FOLLOWS"):** this is the lead. At 168x94 there is one focal story. Doug on the yellow band and his shadow
  on the floe read clearly, and the spotted reptile head sits right under him. The text avoids every title word and supports the
  title's "From Under the Ice". It is not misleading, because nobody is being attacked.
- **Thumbnail B ("CORNERED"):** strong at feed size. Doug's panic and the towering head are clear and on-brief.
- **Thumbnail C (6 tiles):** the Sieve krill is now orange, and the red-spray read from round 2 R3 is mostly gone. The red cap
  still sits inside the open mouth. At 168x94 it reads as "Doug in the mouth", not as blood. Acceptable for the A/B test.
- These round-2 notes are still open and still non-blocking:
  - R1: the Sieve head, s155-s173, is still the pale blob (visible in f_014 and f_015).
  - R2: not visible in the samples.
  - R4 and R5: unchanged.

### Shorts: FAIL (cliffhanger wording, no re-art needed)

The packaging works in all three Shorts:
- The titles are readable: three lines of red on a dark band, never cropped.
- The subtitles are large and legible on every background.
- The arrow points straight down. `@DoomedDoug` is legible.
- Nothing is cut off at the sides that matters. In short02 at 2 s (s139) the seal's tail is clipped at the right edge, but the
  head and the diver are in frame, so this is fine.
- No gore.

The problems are the end-card questions.

1. **short03 (director): the outro answers its own cliffhanger.** The outro says "Then Doug joined them in a seal costume, with
   no scars at all", and the end card then asks "WHO HAS THE SEAL NOT TRIED YET?". The viewer has just been told the answer
   (Doug, in a costume, unscarred), and the real open question (what the seal does to him) is never asked. Fix: in
   `shorts.json` short03, change `end_card` to `"WILL THE SEAL FALL FOR DOUG'S COSTUME?"`. Keep `tease_from: s208` and
   `tease_asset: leopard_seal_head_rising`, which match the new question. Re-render the Short only.
2. **short02 (director): the question and the silhouette don't match.** The end card asks "DID DOUG CATCH THE PENGUIN?", but the
   red-outlined silhouette is the swimming seal (`leopard_seal`). No penguin is shown, so the picture doesn't belong to the
   question. Fix, either:
   - (a) change `end_card` to `"WHAT DID SHE TRY TO FEED DOUG?"`. This fits the outro's "She tried." and the seal silhouette,
     and the Short doesn't answer it; or
   - (b) keep the question and set `tease_asset` to a penguin asset (the one used in s150, the penguin swimming toward Doug).

   Option (a) is preferred, because the seal silhouette is the more recognisable shape.
3. **short01 and short03 end cards (director, minor, do it with fix 1):** the "???" sits on top of the silhouette's neck and head.
   In short03 it covers most of the rising head, which then reads as a black boot or periscope. If the end-card layout allows,
   move the "???" above the silhouette, or shrink it, so the snout and whiskers stay visible.

short01 is otherwise good. It pays off its title (the punctured fender, the capsized dinghy, the 216 regulars). The outro sets up
one specific question ("WHAT DOES THAT SMILE REALLY MEAN?"), and the open-jawed `leopard_seal_gape` silhouette (teeth visible)
matches it. It does not need changes beyond the optional item 3.

## Round 4: post-render re-check (re-rendered Shorts, final round), 2026-10-27

What I checked: the three re-rendered `build/shorts/short01-03.mp4` (frame at 20 s, then frames at -8, -5, -3 and -1 s of each), the three `*_preview.png`, all 23 `build/samples`, `qc.json` (no problems), `thumbnail.png` and `metadata.json`. Nothing was rendered.

### Main video + thumbnail: PASS (unchanged since round 3)
- The samples match round 3. There are no black, blank or frozen frames, the counter steps 234 to 240 in order, Doug is on-model, and there is no gore. `qc.json` reports no problems.
- Thumbnail A ("IT FOLLOWS") still works with the title "How the Leopard Seal Kills Doug From Under the Ice": Doug on the yellow band, his shadow on the floe, and the spotted head underneath. It is honest packaging.
- Round-2 notes R1 (the pale Sieve head) and R4/R5 are still open and still non-blocking.

### Shorts: PASS
1. **short02 (round-3 fix 2): fixed.** The end card now reads "WHAT DID SHE TRY TO FEED DOUG?". It follows the outro's "She tried." and matches the red-outlined swimming-seal silhouette. The Short does not answer it.
2. **short03 (round-3 fix 1): fixed.** The end card now reads "WILL THE SEAL FALL FOR DOUG'S COSTUME?". This is the open question, and the outro no longer answers it. The rising head with whisker ticks and ripples reads as a seal head coming out of the water.
3. **short01:** unchanged and still good. "WHAT DOES THAT SMILE REALLY MEAN?" goes with the open-jaw `leopard_seal_gape` silhouette.
4. Packaging holds in all three Shorts. The titles are readable on three lines and never cropped. The subtitles are large and legible. The arrow points straight down. `@DoomedDoug` is legible. Nothing important is cut off at the sides.
5. Non-blocking, for the next episode: round-3 item 3 was not done. The "???" still sits over the silhouette's head in all three Shorts. It costs a little recognisability (most in short01, where it covers the jaw line), but each silhouette still reads with its question. Director/editor: put "???" above the silhouette by default in the end-card layout.

VERDICT (main): PASS
VERDICT (shorts): PASS
