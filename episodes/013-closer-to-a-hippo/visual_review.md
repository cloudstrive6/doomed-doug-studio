# Visual review: 013-closer-to-a-hippo

## Round 1: keyframes (pre-render), 2026-10-09

Scope: contact sheets `build/contact/sheet_01..22.png` (s001-s253), plus full-size keyframes s003, s044, s061,
s126, s128, s146, s164, s220 and s229.

### Overall
Strong episode visually. Doug is on-model in every shot I checked (red cap, white head, stick body) and readable on
every background, including the night chapter and the dark-maroon "Mouth" chapter. Chapter cards, the death counter
(107 to 114) and the distance-to-hippo counter step down correctly by chapter. Analogies read in about a second
(cars, sofa, suitcases, ruler, football pitches, astronaut). The hippo asset reads well in every pose: side, yawn,
underwater bound, eyes-and-ears surface and front-on mouth. Deaths are all cartoon (dust cloud, ghost Doug, cap left
behind, RIP stone), and the tone is adult and dry, not a kids' show. s001 is a "(thumbnail pending)" placeholder, so
the thumbnail still needs its own check.

Two shots use a red speckle effect that reads as blood (policy risk), and one analogy doesn't read. That makes this
round a FAIL. Everything else below is small.

### Required fixes
1. **s061 (director + illustrator).** The black hippo silhouette has a cloud of red speckle under its feet on the
   path. At a glance it looks like a blood spray or blood pool under the animal ("something extremely heavy travels
   over it"). Remove the red speckle. If the shot needs a threat cue, use a flat yellow/white glow behind the
   silhouette, or the existing warning triangle alone.
2. **s164 (director + art director).** The red speckle halo around the black underwater hippo spreads into the
   water and the riverbed. It reads as a blood cloud in water, which is the worst possible connotation for this
   lane. Replace it with a non-red reveal treatment, such as a flat light halo or bubbles plus the silhouette.
   Art director: the same red-speckle "reveal glow" also appears in s086 (film frame), s119 (yawn silhouette) and
   s245-s248 (mouth silhouettes). It's acceptable there because it sits behind the subject on dry land or on a red
   background, but please make it a non-red colour across the episode for consistency.
3. **s126 (illustrator + director).** The "ajar vs thrown back against the wall" analogy is drawn as a top-down
   floor plan (black wall lines with a brown plank and a red arc). Next to it is a single closed front-view door.
   Viewers won't read this as doors. Draw two front/perspective doors instead: left one slightly open (about 45°,
   labelled AJAR), right one swung flat against the wall (about 150°, labelled ALL THE WAY). Optionally put the
   45°/150° labels on them.
4. **s044 (illustrator).** The dung spray is a solid brown zigzag wedge that covers almost all of Doug, apart from
   his cap and one eye. It reads as a broken polygon, not as flicked dung. Redraw it as a fan of separate brown clumps
   and droplets coming in from the right, with motion lines, and keep Doug's face and body visible behind the spatter.

### Recommended fixes (not blocking)
5. **Distance counter changes one shot early (director).** It updates on the last shot of the outgoing chapter
   instead of on the next chapter card: s024 (1 km while still in Colombia), s047 (300 m), s069 (50 m), s093 (10 m),
   s117 (5 m), s142 (2 m), s167 (1 m), s194 (0.5 m), s217 (0 m). Move each update to the following title card (s025,
   s048, s070, s094, s118, s143, s168, s195, s219).
6. **s003 (director).** "AS FAR AS HE COULD" sits across the map's bottom frame line and the white Antarctica band.
   Move it fully below the map, or onto the open ocean area inside it.
7. **s087 (director).** The same problem: "ALL FOUR FEET" overlaps the film-strip's bottom border. Move it below the
   frame.
8. **s121 (director).** The red X covers the middle of both "BORED?" and "SLEEPY?", so neither word is readable. Use
   a smaller X on each word, or a strike-through line, so the words stay legible.
9. **s229 (director).** The warning triangle only partly covers the middle "500?" card, and a red fragment of the
   hidden text pokes out. Either cover the card completely or blank its text.
10. **s241 (director).** The three extra lettuces sit on the hippo's eyes and nose. "Appreciate a great many
    vegetables at once" would read better with the lettuces stacked in or lined up in front of the mouth.
11. **s242 (director).** The big "DISTANCE TO HIPPO: 0 m" label duplicates the HUD counter right beside it. Use
    "0 M" centred over the gap between Doug and the mouth instead.
12. **s108 (illustrator).** The blue vertical rectangle doesn't clearly read as a bank card. Draw it with rounded
    corners, a chip and card-number dashes, or add a "BANK CARD" label.
13. **s055 / s058 (director).** These use an identical hippo pose and position (only "munch" differs). Flip or
    reframe s058, for example as a closer crop on the mouth and grass.
14. **s245-s248 (director, optional).** Four near-identical black-mouth silhouettes in a row. This is acceptable as
    the deliberate "four sentences" beat, and s247 varies with the lettuce. A slow push-in across the four would keep
    it from feeling frozen.

### Note for post-render
- s250 is a deliberate full-black frame with only the death counter. Make sure QC's black-frame detection doesn't
  flag it as a fault, and keep it under about 1.5 s.

VERDICT: FAIL (fixes 1-4 required; re-screen s044, s061, s086, s119, s126, s164 and s245-s248 after the changes)

## Round 2: keyframes re-screen (pre-render), 2026-10-09

Scope: all 22 contact sheets `build/contact/sheet_01..22.png` (s001-s253), re-rendered after the fixes in commit 84bd085.
I also checked full-size keyframes s061, s117, s134, s219 and s245-s247, and ran a scripted check of the
distance-counter labels in `shotlist.json`.

### Round 1 items: status
- **1. s061 red speckle:** fixed. The halo is now pale yellow and nothing under the silhouette reads as blood.
- **2. s164 red underwater halo:** fixed. The halo is now a pale green-white glow with bubbles and reads as "something
  under the water". The same non-red glow is used in s086 (warm yellow), s119 (yellow/sand), s065 (green) and
  s245-s248 (yellow on maroon, which mixes to a salmon texture). No red-speckle reveal is left anywhere in the episode.
- **3. s126 doors:** fixed. There are two front-view doors labelled AJAR and ALL THE WAY (the second is flat against the
  wall, with impact marks). It reads at once.
- **4. s044 dung spray:** fixed. The spray is now separate clumps and droplets with motion lines, and Doug's face and
  body stay visible. s045/s046 carry the spatter on Doug in a light brown speckle, which is fine.
- **5. Distance counter:** fixed. The scripted check confirms that every change now happens on the chapter card:
  s025 1 km, s049 300 m, s070 50 m, s094 10 m, s118 5 m, s144 2 m, s168 1 m, s195 0.5 m, s219 0 m. The teaser shots
  s048/s143 keep the outgoing value, which is correct.
- **6. s003, 7. s087:** fixed. Both captions are clear of the frame lines.
- **8. s121:** fixed. A strike-through line is used and both words are legible.
- **9. s229:** fixed. The middle card is fully covered by the triangle and no text pokes out.
- **10. s241:** fixed. The lettuces are now inside the mouth.
- **11. s242:** fixed. "0 M" sits in the mouth gap and isn't duplicated.
- **12. s108:** fixed. The card now has a chip, a logo and number dashes, and reads as a bank card.
- **13. s055/s058:** fixed. s058 is now a close crop on the head and grass.
- **14. s245-s248:** improved. The framing now shifts (centre, right, left, centre) and s247 has the lettuce. This is
  no longer a frozen run.

### Full pass
Doug is on-model in every shot (red cap, white head). The deliberate exception is the sunburn gag in s116/s117,
where his head is tinted pink; the cap still reads, so this is fine. Doug is readable on every background,
including the night chapter, the dark-green shallows and the maroon Mouth chapter. Deaths are all cartoon (dust
cloud, ghost Doug, cap left behind, RIP stone, splash), with no gore. The red sweat in s094-s117 is orange,
labelled NOT BLOOD and backed by the narration, so it doesn't read as injury. The tone is dry and adult throughout.
The counter runs 107 to 114 and steps on each death shot (s066, s092, s141, s166, s193, s217, s250). Spelling is
clean on every label I checked, including HIPPOSUDORIC and NORHIPPOSUDORIC. There are no runs of 4 or more
near-identical compositions.

### Required fixes
None.

### Recommended fixes (not blocking; do them before the final render if cheap)
1. **s061 (director).** The new path patch under the silhouette (the `rect` at 270,652 and the `poly`/lines at
   356-570, y 652-712) leaves a visible boxy ledge with thin straight outlines. It breaks the curved path, and because
   it has `appear: 0.3` the path also visibly changes shape mid-shot. Remove the patch and either move the hippo
   silhouette fully onto the existing path (for example y ≈ 690) or redraw the path polygon once without the patch.
2. **s245, s246, s247 (director).** The white labels (DOESN'T WANT DOUG / NEVER DID / VEGETARIAN) sit on the
   silhouette's head, with the ears poking out above or beside the box. In s246 one ear shows and the other is
   covered, so the head looks lopsided. Either lower the silhouette by about 80 px (or scale it to about 0.68) so the
   labels sit fully on the maroon above the ears, or move each label into the open-mouth gap (s245, s246, s248 have
   it free).
3. **s134 (director).** The vertical red dashed "measurement" line running from the upper jaw down past the lower
   tusk can read as a red drip from the mouth at phone size. Add end ticks (a ⟂ cap at each end) and make it white or
   yellow, or swap it for a small "150°" arc like s137.
4. **s219 (art director).** There's a 1 px vertical seam down the centre of the `hippo_mouth_front` silhouette (visible
   in the head and lower jaw). It's barely visible, but it'll be on screen as the chapter card. Check how the asset's
   two halves join in silhouette mode.
5. **s183 (director).** The "2025" label sits over the sun. Move it left of the sun, or move the sun.

### Still open
- s001 is still "(thumbnail pending)". The thumbnail, the shorts and the post-render samples are screened separately.
- From round 1: keep s250 (deliberate full-black frame) under about 1.5 s and make sure QC doesn't flag it.

VERDICT: PASS (keyframes approved for render; recommended fixes 1-2 strongly suggested)
