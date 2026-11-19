# 052 honey badger: visual review

## Round 2: pre-render re-screen (keyframes + thumbnails), 2026-11-19

Inputs: the full regenerated set `build/contact/sheet_01..14.png` (168 tiles, s001-s167 + endslate), full-res
`build/keyframes/*.png` crops for the shots that changed, end-state renders of every shot that uses a masking `rect`
(s024, s067, s076, s084, s140, s157, s159), `build/thumbnail{,_b,_c}.png` and `_small.png`, and the titles in
`metadata.json`.

### Scorecard

| Item | Verdict | Note |
|---|---|---|
| Keyframes (s001-s167, endslate) | **FAIL** | All 8 round-1 blockers and the recommended fixes are done. 1 blocker left: a masking rect cuts a square chunk out of the burrow on s159 |
| Thumbnail A `thumbnail.png` (TOO MUCH WORK) | **PASS** | Better than round 1: the stop-paw reads at once and Doug's face now shows at feed size |
| Thumbnail B `thumbnail_b.png` (IT CHARGED) | **PASS** | You can now count six separate lions at 168 px and all of them sit inside the frame. One optional Doug tweak below |
| Thumbnail C `thumbnail_c.png` (IT BITES BACK) | **FAIL** | The gripping arm comes in from the top-right edge and isn't joined to the lion on the left. It reads as a wooden plank or a second, off-screen giant |

### Round-1 fixes: verified

1. s142: FIXED. The red ground glows are gone. Six black silhouettes now sit under SIX (standing, male, standing,
   sitting, standing, lying), and the lit ONE lion stands apart at the right with no overlap.
2. s048: FIXED. The jackal silhouette has no red spray, and no red glow sits on the ground anywhere. The glow behind the
   leopard on s087 stays in the orange sky band, which is acceptable.
3. s072, s073, s074, s079: FIXED. The cut-away is now a whole badger with a round magnifier inset that shows a grey skin
   layer over a beige body layer. There is no pink and no tear, so nothing reads as a wound. The 6 MM arrow lands on
   the skin layer, BELLY: THIN points at the bottom of the inset, and SOME is clear.
4. s144: FIXED. `2012` now sits in the sky band, clear of the lions.
5. s148: FIXED. GROAN has moved above the badger, with an arrow to the mouth, so the teeth are clear. The label just
   touches the lying lioness's tail, which is fine.
6. s002, s003, s004: FIXED. The HUD shows only `BADGER: ~9 kg` until s005 adds the puff adder line.
7. s002: FIXED. The `!` now sits just above the badger's head.
8. s110: FIXED. The beam tips down on Doug's side and s111 stays level.
9. s017, s091, s141: FIXED. Each one uses a single red strike-through, so IMMUNE, NOTHING HUNTS IT and LION stay
   readable.
10. s158: FIXED. The coffee ring has moved to the lower-left corner and PLAN B: FIGHT is clean.
11. s160: FIXED. TOO BIG no longer touches the lioness.
12. s025, s026: FIXED. The HUD second line reads COLONY.
13. s134: FIXED. The capless stick man is gone and Doug stands at the pool edge.

Still good across the cut: Doug is on-model in every shot, including the beekeeper-suit shots s043-s047 and s105-s121.
The death counter goes 386 > 391 at the right beats. Cartoon deaths only (ghost Doug, cap on the ground, tombstone).
Nothing has a kids-show tone. The ending pays off the title (the badger takes the hole and the lions wander off), and
the clip ends cleanly on the end slate with no "???" card. Variety: no run of 4 or more near-identical shots. The
longest runs are 3: s072-s074 (skin diagram) and s139-s141 (Doug behind the badger). The road-and-pride layout comes
back at s143/s144, s148, s150 and s159/s160, but other shots break it up between those.

### VERDICT: FAIL (keyframes)

Required fix:

1. **s159: change, owner: director.** The erase `rect` (x 640, y 900, w 260, h 150, fill `#6a5440`,
   `appear: 0.6`) is drawn on top of `badger_burrow`. It cuts a hard square notch out of the left half of the mound,
   and it chops the diving badger into a stub with a straight edge. In the video the notch pops in at 60 % of the
   shot, which looks like a render glitch. This was already there in round 1 and I missed it.
   - Delete that `rect`.
   - Show the badger going down the hole by drawing `honey_badger_digging` at about (900, 940) **before**
     `badger_burrow` in the element order, so the mound's front lip hides its head and only the rump and hind legs
     show, as on s152.
   - Or, if a second state is wanted at 0.6, swap in a "just the tail tip in the hole" version instead of masking.
   - Keep the red arrow pointing into the hole.

Re-render only s159 (`python -m studio keyframes 052-honey-badger-lions --shots s159`). If it reads cleanly, keyframes
PASS. No other shot needs to change.

### Thumbnails

**A `thumbnail.png` / `_small.png`: PASS** (title: *Every Reason Lions Think Twice About a 9 kg Honey Badger*)
- At 168 px, TOO MUCH WORK is readable. The lion's lifted "stop" paw and its half-closed eyes give the verdict in one
  look. The black-and-white badger stands out against the orange, and Doug's red cap and white face now show behind
  the badger's rump.
- The badger's dark-red open mouth is a cartoon snarl: no blood, no wound. It is not misleading and pairs well with the
  title.

**B `thumbnail_b.png` / `_small.png`: PASS** (title: *Every Reason Six Lions Lost Interest in One Honey Badger*)
- At feed size you can count six separate lions (2 males, 3 standing lionesses and 1 sitting), and every lion is fully
  in frame. IT CHARGED, the long charging badger and the threat all read, and the image matches the title's "six
  lions".
- Optional (graphic designer, `thumbnail_test_b.json`): the badger's black hind leg is drawn over Doug's body, so up
  close Doug looks like a head stuck to the badger's rump. Move the badger to about x 470, or move Doug about 40 px up
  and left (x 80, y 670), so his stick body is clear behind the tail. Not blocking: at 168 px he still reads as a red
  cap behind the badger.

**C `thumbnail_c.png` / `_small.png`: FAIL** (title: *Every Reason Lions Think Twice Before Killing a Honey Badger*)
- The new `lion_paw_grip` does explain the raised scruff, but the forearm enters from the top-right corner (x 1240,
  y 40) while the lion is at the far left. The limb isn't joined to any body. Its light tan, wood-grain shading and
  straight edges make it read as a wooden beam or a cricket bat swinging into the badger. At 168 px the image reads as
  "something is hitting a badger", not "a lion is holding a badger".
- The paw's white curved claws hook into the white scruff fold. Up close, that edges toward "claws in skin", which the
  brief rules out.
- **Fix (graphic designer, using the illustrator if the asset needs redrawing), `thumbnail_test_c.json`:**
  1. Join the grip to the lion on the left. Run the lion's own foreleg from its chest or mane (about x 330, y 470) up
     and right to the scruff at about (740, 250), with the paw closed on top of the fold. Delete the arm from the
     top-right.
  2. Shade the leg like the lion's body: same tan, with fur strokes instead of grain lines. A rounded outline, not a
     straight-edged slab.
  3. Draw the paw as a padded grip with no visible claws, or with the claw tips hidden behind the fold.
  4. Keep the badger's head twisted back with teeth toward the lion, clear of the paw. Keep IT BITES BACK, the sky,
     the ground and Doug as they are.

### Routing summary
- **director:** keyframe fix 1 (s159)
- **graphic designer (+ illustrator for the `lion_paw_grip` foreleg):** thumbnail C fixes 1-4. Thumbnail B Doug tweak
  is optional.
- **art director:** nothing this round

To re-screen: `python -m studio keyframes 052-honey-badger-lions --shots s159` and
`python -m studio thumbnail 052-honey-badger-lions`. I'll write the Round 3 section here.

## Round 3 (2026-11-19): s159 keyframe + thumbnail C re-check

**VERDICT: PASS** (keyframes PASS; thumbnails A, B, C all PASS)

### Keyframe s159 (re-rendered with `python -m studio keyframes 052-honey-badger-lions --shots s159`)
- The masking `rect` is gone. The mound is whole, with no square notch and no hard-edged stub, so the render
  glitch can't come back at 60 %.
- `honey_badger_digging` at (900, 975) x0.45 sits in the hole mouth: head down inside, black-and-white back and
  rump arched up, hind legs on the rim. It reads as "badger going down the hole" in about 1 s and matches the
  narration. The red arrow (appear 0.5) points into the hole. Doug (red cap, white head, gritted) stands clearly on
  the left, and all six lions and the labels are in frame and legible.
- Nit, not blocking (illustrator, optional): the asset's little tan dirt clod at the front-left of the hole (around
  x 815, y 970) looks a bit like a separate pebble. Fine as kicked-up dirt.

### Thumbnail C `thumbnail_c.png` / `_small.png`: PASS (title: *Every Reason Lions Think Twice Before Killing a Honey Badger*)
- The forearm now comes out of the lion's own chest and mane and runs up to the scruff. The detached top-right arm
  is gone, and the limb is the lion's tan with rounded edges, so it no longer reads as a beam or bat.
- The paw is a padded grip (pad plus four toes) closed over the white scruff fold, with no claws visible. Nothing
  suggests "claws in skin", and there is no blood or wound.
- The badger's head twists back with its teeth bared at the lion's foreleg, and the paw doesn't touch it. That
  pays off IT BITES BACK and the title's "think twice".
- At 168 px it all reads: IT BITES BACK is legible, there is one clear clash (lion holding badger by the scruff, badger
  biting back), and Doug's red cap and white face show at the right. Not misleading.
- Nit, not blocking: the small tan fur tufts under the foreleg are fine. The leg is long and fairly straight, but
  it is clearly attached and on-palette.

### Routing summary
- Nothing required. All visual gates for keyframes and packaging are clear for this episode. Post-render screening
  (samples, qc.json, Shorts) is still to come after `render --final`.

## Round 4 (2026-11-19): post-render (final.mp4 samples, thumbnails, Shorts)

VERDICT (main): PASS
VERDICT (shorts): PASS

### Main video (`build/samples/f_001..f_021.png`, `build/qc.json`)
- `qc.json`: duration 644.1 s, `problems: []`. The samples fall at 15 s + 30 s·k, mapped to shots through `build/timing.json`.
- None of the 21 samples is black, blank, glitched or frozen. Every chapter card (THE PUFF ADDER / HIVE / JACKAL / SKIN /
  LEOPARD / BEEKEEPER / LION / PRIDE), the death counter (386 to 391, rising in order) and the scale labels are legible,
  spelled right and not cropped.
- Doug is on-model wherever he appears (red cap, white head), including the beekeeper-suit shots s043 and s114/s122.
  He is absent in s059, s092 and s131, which is intended (animal-only beats).
- Pictures match the narration. s006 shows the lock and key for the receptor, s021 the "other end of the snake, for science",
  s052 the ~8 KG / ~9 KG pair, s107 the knocked-over hives in the Western Cape, s114 the raised and strapped hive, s122 the broken stand
  ("beaten by furniture"), s146 the lions playing in a dust cloud on the road, and s163 the cap left by the hole (THE CAP arrow).
- I checked the mid-reveal moments from frames I pulled out of final.mp4. s043: the empty thought bubble fills with the badger at
  appear 0.6, so it resolves. s131: the stink cloud, arrow and STENCH resolve at 0.5 to 0.7. s084: the grabbing_hand (art-director
  approved) holds the scruff and the turned badger bites back, with teeth but no blood.
- Policy: no gore, wounds or blood. Deaths are offscreen or cartoon. The tone is deadpan adult, not nursery.
- Nits, not blocking:
  1. (director, optional) s131 says "Her brother had already caught a young badger", but no badger is in frame. You could add a
     small `honey_badger` at scale 0.3 under the lion's forepaw near (980, 930). Nothing graphic is needed.
  2. (illustrator, optional) In `honey_badger_digging` (s059), the hind legs are very long and blocky compared with the body.
     It still reads as "badger digging".

### Thumbnails (`build/thumbnail{,_b,_c}.png` and `_small.png`)
- These are unchanged from round 3 and still PASS. Each has one focal clash, Doug and the threat are obvious at 168x94, and the text
  (TOO MUCH WORK / IT CHARGED / IT BITES BACK) is legible and doesn't repeat the title. Each matches its paired title in
  `metadata.json` packaging A/B/C, and none is misleading (the video shows the lion walking off, the six-lion charge and the scruff turn-round).

### Shorts (`build/shorts/short01..03.mp4` + `_preview.png`, 8 frames each pulled with ffmpeg)
- All three are 1080x1920 at 60 fps, 57.6 s, 49.7 s and 49.1 s long. The red title block is readable in every frame, and the
  word-chunk subtitles are large and legible in the lower third with no collisions. The @DoomedDoug tag is present.
- The drawings fit the width. In short03 the six lions and the jeep are inside the frame, and short01's branch running off the
  left edge is intentional. Doug is on-model.
- End cards: FULL VIDEO: TAP BELOW, with a red arrow pointing straight down. There is no "???" teaser card.
- Payoffs land before the end card. short01 ends on "nobody has proved it" plus Doug's death, short02 on the stench and skin
  reasons plus "and left", and short03 shows the charge through the middle and the badger's first plan (leave). short03's
  "Then Doug tried to follow it" is a plug for the full video after the title has already paid off, so it is acceptable.
- Nit (editor, optional): in the 9:16 crop, the death counter and scale labels shrink to about 10 px text. They are decorative here,
  so this doesn't block.

### Routing summary
- Nothing is required. The main video, the thumbnails and the Shorts all clear post-render screening.
