# 052 honey badger: visual review

## Round 1: pre-render (keyframes + thumbnails), 2026-11-19

Inputs: `build/contact/sheet_01..14.png` (168 tiles, s001-s167 + endslate), full-res `build/keyframes/*.png` for
zooms, `build/thumbnail{,_b,_c}.png` and `_small.png`, titles from `metadata.json` packaging variants.

### Scorecard

| Item | Verdict | Note |
|---|---|---|
| Keyframes (s001-s167, endslate) | **FAIL** | 2 blockers: shots that could read as gore (red glow, skin cut-away), plus a count error and label overlaps |
| Thumbnail A `thumbnail.png` (TOO MUCH WORK) | **PASS** | Reads at feed size: one big lion, badger, text. Doug only shows as a red cap at 168 px, as the brief intends |
| Thumbnail B `thumbnail_b.png` (IT CHARGED) | **FAIL** | The six lions blur into one tan smear at feed size, and the right-hand lion is cut off by the frame |
| Thumbnail C `thumbnail_c.png` (IT BITES BACK) | **FAIL** | Nothing is holding the badger, so it floats in mid-air and the raised scruff looks like a shark fin |

What works across the cut: Doug is on-model in every shot (red cap, white head) and shows up where expected. The death
counter goes 386 > 391 at the right beats. Chapter cards and wordart are spelled right and readable. All the
creatures are recognisable (adder, honeyguide, jackal, goshawk, leopard, lions, gerbil). Nothing has a kids-show
tone. Deaths are cartoon only (ghost Doug, cap on the ground, X eyes, tombstone). The ending pays off the title (the
badger takes the hole, and the lions lose interest in it and in Doug) and ends cleanly on the end slate, with no
"???" teaser. Variety: no run of 4 or more near-identical shots. The longest are 3, at s037-s039 (map), s049-s051
(dig + jackal) and s139-s141 (Doug behind the badger).

### VERDICT: FAIL

Required fixes (blockers first):

1. **s142: change, owner: director.** Each silhouette has a red `glow_r: 360` glow. On the brown ground these read as
   four **blood pools under the animals**. The shot also says **SIX** but shows only 4 silhouettes plus the ONE lit
   lion (5 animals), and the sitting silhouette overlaps the ONE lion's hind leg.
   - Remove `glow_r` from all four silhouettes, or use a dark grey or desaturated purple halo that sits in the sky band
     only.
   - Show **six** silhouettes, with the separate lit lion under ONE. For example, shrink them to scale 0.4 and space
     them about 230 px apart across x 200-1500, then move the lit lion to x 1650 so nothing overlaps.
2. **s048: change, owner: director.** The jackal silhouette's red `glow_r: 320` spray falls on the brown ground under
   it and reads as a blood splatter next to a digging animal. Drop the glow, or make it a dim, non-red rim. The same
   threat glow on s087 (leopard over the sky band) is acceptable. Don't put a red ground glow on any other shot.
3. **s072, s073, s074, s079: change, owner: illustrator (asset) and art director (style).** The skin cut-away is a
   chopped-off front half of a badger with a **jagged pink tear** in its side. It reads as a torn-open wound or
   butchered meat, not a diagram.
   - Redraw the cut-away as a clean diagram: a whole badger in side view, with a neat straight or circular inset (a
     "magnifier" circle) showing a thick black/grey skin layer over a plain body layer.
   - The body layer should be a neutral colour (light grey or beige), not flesh pink, with no zig-zag tear.
   - Keep the 6 MM, BELLY: THIN and SOME labels and arrows pointing at the skin layer.
4. **s144: change, owner: director.** The `2012` label (260, 640) covers the first lioness's head and front legs.
   Move it to the clear sky band, for example (200, 470), or put it on the jeep's door.
5. **s148: change, owner: director.** The `GROAN` label covers the charging badger's face and teeth, which are the key
   detail ("teeth showing"). Move it about 120 px up and in front of the snout, for example (1000, 900) with an arrow
   to the mouth, or make it a speech-tail label above the head.
6. **s002, s003, s004: change, owner: director.** The scale HUD's second line reads **`VS: --`**. It looks like
   unfinished placeholder text. Change it to `VS: ?`. Better: drop the second line until
   s005, when `PUFF ADDER: UP TO ~6 kg` arrives.
7. **s002: change, owner: director.** The `exclamation_mark` at (1000, 520) floats alone in the sky, about 240 px
   from the badger, and looks like a stray mark. Move it to just above the badger's head, about (880, 740).
8. **s110: change, owner: director or illustrator.** Doug (80 kg) is on the left pan and the right pan is empty, but
   the beam is level. Tip the beam down on Doug's side (rotate the beam and drop the left pan). s111 can stay level,
   because 8 buckets is about 80 kg.

Recommended fixes (not blocking, but do them if they are cheap):

9. **s017, s091, s141: change, owner: director.** The red X sits on the middle letters, so the words being struck out
   (IMMUNE, NOTHING HUNTS IT, LION) can't be read in one second. Use a single red strike-through line, like the field
   guide's FEARLESS on s102 and s154, so the word stays readable.
10. **s158: change, owner: director.** The coffee-ring stain sits on `PLAN B: FIGHT` and hides the I. Move the ring
    to the lower-left page corner, as on s155.
11. **s160: change, owner: director.** The `TOO BIG` label touches the lying lioness's back leg. Nudge it about
    40 px right and down.
12. **s025, s026: change, owner: director.** The topbar and HUD still say THE PUFF ADDER / PUFF ADDER: UP TO ~6 kg
    while the narration has moved on to the stingers. This is fine as a bridge, but switch the HUD second line to
    `COLONY` from s025 so it matches the picture.
13. **s134: change, owner: director.** The capless `stick_man_plain` at the pool edge reads as off-model Doug at a
    glance. Give him a different hat or a field shirt, or place Doug beside him reacting to the smell.
14. **s001: note, owner: director.** The opening image is the thumbnail (lion + badger) while the line is "A puff
    adder bit a honey badger on the face." This follows the opening-image rule and lasts about 2 s before s002 shows
    the adder, so keep it. If the editor has room, an `appear` of a small puff adder at the badger's face would tie
    picture and line together.

### Thumbnails

**A `thumbnail.png` / `_small.png`: PASS** (title: *Every Reason Lions Think Twice About a 9 kg Honey Badger*)
- At 168 px: TOO MUCH WORK is readable. The big sitting lion is the single focal point and the black-and-white badger
  stands out against the orange. It pairs well with the title (the title gives the reasons, the image gives the lion's
  verdict) and is not misleading.
- Optional (graphic designer): at feed size Doug is only a red dot behind the badger's rump. Raise him about 20 px or
  scale him 0.42 > 0.5 so his face shows over the badger's back. Optional, not required.

**B `thumbnail_b.png` / `_small.png`: FAIL** (title: *Every Reason Six Lions Lost Interest in One Honey Badger*)
- The six lions (scale 0.27, about 110 px apart, alternately flipped) overlap tail-to-tail into one tan band. At feed
  size you can't count them or tell they are lions, and the lion at x 1200 runs off the right edge. The threat (six
  lions) is the point of this title and it doesn't read.
- **Fix (graphic designer), `thumbnail_test_b.json`:**
  - Scale the lions to about 0.34 and space them about 120-130 px apart over x 520-1180 so every lion is fully inside
    the frame.
  - Have all of them face left toward the badger (no alternating flips), or give each a small gap so there is no
    overlap.
  - Optionally raise the horizon about 40 px so the lions sit larger against the orange sky.
- Keep IT CHARGED, the charging badger and Doug as they are; they read well.

**C `thumbnail_c.png` / `_small.png`: FAIL** (title: *Every Reason Lions Think Twice Before Killing a Honey Badger*)
- The concept is "a lion holding the badger by its loose scruff as it turns round inside its skin". Nothing in the
  image holds the badger. It hangs in mid-air with its feet off the ground, and the pulled-up scruff looks like a
  shark fin. At feed size it reads as a flying badger. The brief's HOW TO HOLD A BADGER card for Doug is also missing.
- **Fix (graphic designer), `thumbnail_test_c.json`:**
  - Add the lion's grip on the scruff fin, either the lion's front paw clamped on it (no claws in skin, no blood) or
    the lion's jaw closed on the loose fold. This explains the raised skin and why the badger is lifted.
  - Keep the badger's head twisted back with teeth toward the lion's nose, and keep it clear of the grip.
  - Optionally put the HOW TO HOLD A BADGER card in Doug's hand, small enough that it doesn't compete with the text.
- Text, colours and the lion's crop are fine.

### Routing summary
- **director:** fixes 1, 2, 4, 5, 6, 7, 8 (+ 9-14 recommended)
- **illustrator / art director:** fix 3 (skin cut-away asset used by s072, s073, s074, s079), s110 beam if it's in the asset
- **graphic designer:** thumbnail B and C fixes (A optional)

To re-screen: re-run `python -m studio keyframes 052-honey-badger-lions --shots s002,s003,s004,s048,s072,s073,s074,s079,s110,s142,s144,s148`
and `python -m studio thumbnail 052-honey-badger-lions`. I'll append Round 2 here.
