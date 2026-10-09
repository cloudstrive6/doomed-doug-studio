# Visual review: 012-every-natural-trap

## Round 1: keyframes (pre-render), 2026-10-09

Scope: all 25 contact sheets (s001 to s298) plus full-res crops of s031, s039, s089, s145, s222, s227 and s261.
s001 skipped because the thumbnail is still pending.

VERDICT: PASS

I found no blocking defects. Nothing is cropped, broken or garbled. Doug is on-model in every shot (red cap,
white head), including the costume shots (sea star in s084 to s091, gall mite in s286 to s290), the ghost gags
(s031, s059, s060, s117, s180, s215 to s217) and the cave shots, where his head is outlined so it shows up on the
dark rock. The death counter goes up correctly: 100 at the start, 107 at s291. The seven suitcase stickers in
s294 match the seven deaths. There are no stickers for Brinicle or Dead Sea, which is correct because Doug survives
both. All text is spelled correctly and none of it is cut off.

Gore and kid appeal: clean. The deaths are cartoon only: skis sticking out of the snow, a lone cap, sinking in tar
with X eyes, a popcorn-lump Doug, Doug in amber. There is no blood and no body horror, and the tone stays adult
and dry. Nothing reads as a nursery show.

Real-victim sensitivity: handled well.
- Lower Antelope Canyon 1997 (s047 to s051) uses sober dark title cards with no Doug, no jokes and only abstract
  canyon blocks. The Doug gag starts at s054, after the facts.
- The Tsanfleuron couple and the Valais missing list (s169 to s175) use the same sober cards, with no remains shown
  and no Doug.
- The Altamura Neanderthal is drawn as an abstract calcite lump with no skeleton. That is respectful.

### Advisory fixes (non-blocking; do them if time allows)

1. **s018 to s023, director (composition):** six shots in a row use the same tree-well cross-section, only the
   overlay changes. s020 is just the tree with a "!". Fix: in s020, cut back to the wide mountain shot (the s014
   framing) with Doug skiing toward the tree. In s021, show Doug tipping head-first into the well instead of
   standing at the right edge while an arrow does the work.
2. **s222, director/illustrator:** the "A NEANDERTHAL" caption sits on a beige rock with a "?", and on its own it
   doesn't read as a person. Fix: add a small "NEANDERTHAL" label box with a pointer, or suggest a skull outline
   at the top of the lump (no bones showing). Keep it abstract.
3. **s227, director (composition):** the water drop under the stalactite lands right on the "I" of "DRIPS", so it
   reads like "DRÎPS". Fix: move the text 40 to 60 px down or left, or move the drop into the gap above the text.
4. **s089, illustrator:** the payoff is "the sticker had already been printed", but the BRINICLE sticker is about
   15 px tall at 1080p and won't read at phone size. Fix: scale the sticker about 2.5x or zoom the camera onto it.
5. **s145, illustrator:** the "MORECAMBE BAY" text on the thought-bubble sign is too small to read. Fix: double
   the sign's size, or add a plain "MORECAMBE BAY" label box under the bubble.
6. **s291 to s293, illustrator:** continuity. Doug wears the gall-mite costume in s286 to s290, but inside the amber
   in s291 to s293 he is a plain stick figure. Fix: put the costume on the preserved Doug as well, or accept it as
   intentional.
7. **s015, director:** the red X strikes cover letters in "AVALANCHE", "CLIFF" and "STORM". They are still
   readable, but a thinner X or a horizontal strike-through would keep the words cleaner.
8. **s064 and s106, director:** both images are weak. In s064 the arrow points at empty water, so the brine is
   invisible. In s106 the powder cloud is barely visible. Fix: add a visible denser brine plume in s064 (darker
   blue streak) and a stronger, more opaque billowing cloud in s106.
9. **s127, s138, s147, s148, illustrator:** the Dead Sea map shape isn't labelled. Add a small "DEAD SEA" label box
   the first time it appears (s127).

Variety otherwise holds up. The brinicle (s061 to s091) and tar pit (s194 to s215) runs reuse one backdrop, but each
shot changes its props, Doug's pose or the camera, so they don't feel frozen.

## Round 2: thumbnail + s001, 2026-10-09

VERDICT: PASS

Checked: `build/thumbnail.png` (1280x720, re-rendered from `thumbnail.json`), `build/thumbnail_small.png`, a
168x94 downscale (viewed native and at 4x nearest), and `build/keyframes/s001.png` (re-rendered with
`keyframes --shots s001`).

- **Archetype A done right:** white canvas, a strict 3x3 grid, thick black rounded frames, a bold comic label under
  each tile, no title text, no arrows or circles. The nine labels match the description's trap order. The grid goes
  with the "Every ..." title and doesn't repeat it.
- **Feed size (168x94):** every tile's colour block stays distinct (snow, red rock, deep blue, grey and white,
  sand, ice, tar, cave, amber). The tree with skis, brinicle, avalanche, sinkholes, crevasse and amber bead read as
  shapes. The labels can't be read at 168, which is normal for a 9-tile grid (PE grids behave the same). They are
  crisp and spelled right at 320 and above.
- **Doug:** he appears only as one tile (amber), which follows the bible. He is on-model (white head, gall-mite
  costume, consistent with the r1 continuity note), and his red cap sits on top of the bead.
- **Policy:** no gore. The tar-pit bison is alive and sinking, and the Altamura figure is an abstract calcite lump.
  Nothing kid-coded.
- **s001 = thumbnail:** the s001 keyframe (`scene_ref: thumbnail`, 1920x1080) shows the same layout, tiles, labels
  and drawings as `thumbnail.png`. The only differences are from rescaling: mean per-channel difference about 5/255
  after downscaling, no structural difference. `thumbnail_small.png` is an exact downscale of `thumbnail.png`.

### Advisory (non-blocking, graphic designer)
1. **Slot Canyon tile:** the flash flood reads as a brown hill with a white zigzag. At 168 it is only a beige wedge
   between red walls. Fix: make the surge read as water by adding a muddy wave front with 2 or 3 curled foam crests
   and spray, and/or a tiny log or debris in it. Or zoom out a little so more of the narrow slot shows above the
   surge.
2. **Amber tile:** at feed size Doug shrinks to a red dot on an orange circle. The cap floating outside the bead,
   apart from his head, looks like a detached prop at full size. Fix: scale Doug up about 1.3x inside the bead and
   seat the cap on his head, poking slightly through the top of the bead. Or keep the gag but add a gap so it
   clearly reads as "cap left outside".
3. **Altamura Cave tile:** the calcite lump reads as an egg or potato. Optional: show a faint skull outline in its
   top third (no bones beyond that), the same suggestion as r1 s222.
