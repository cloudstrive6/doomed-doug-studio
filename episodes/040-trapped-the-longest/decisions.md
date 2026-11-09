## 2026-11-08 Creative director: script gate
Inputs read: script_review.md (round 2: FAIL on one line only; scores hook 8, structure 8, voice 8; policy 0; 2,017 words), script.md draft 2 with the fix applied, brief.md.
- **Required fix 1 checked.** Line 72 now reads "That cave held him for about a day. The next trap took months to let go." This is true (about 27 hours), sober, and no longer conflicts with the sealing about a week later. With it, every screener item is resolved.
- **Approved.** Line 1 is a real death stake, the payoff promise comes at about 0:09, the item name lands at word 34 and the twist at word 97. The duration axis climbs cleanly up to a boss that is genuinely the most extreme item. The real cases (Nutty Putty, Hoyo Negro) stay unnamed and sober, the virus is framed without "zombie", and the humour is adult-coded. I'd keep watching.
- Notes for the director and graphic designer (not blocking): the opening stage direction (script line 16, seafloor mud plus a worm) describes the old thumbnail A. Follow the brief and FLAG 10 instead: the worm belongs to permafrost and the seafloor belongs to microbes. "Doug has died. Again." appears 6 times, so vary the delivery or the staging so it doesn't feel stale. The series bible death total (308 to 315) gets updated at the final gate.

SCRIPT: APPROVED

## 2026-11-08 Director: shotlist
- 202 shots, 2,018 spoken words matched word for word to the script; Doug in 63% of shots; no build gap over 4.6 s (estimated at 195 wpm).
- HUD: DOUG DEATHS at (1590, 162) plus TIME TRAPPED (`wait_stopwatch` 0.16 + size-28 label right-aligned under the counter), blank "--" until the
  Nutty Putty sober card, then 27 HOURS / 2 MONTHS / 5,300 / 12,000 / 46,000 / MORE THAN 48,500 / 160,000 TO 232,000 / 101.5 MILLION (red).
- Real cases: Nutty Putty shots s006-s020 and the sober cards s024-s029, Hoyo Negro s080-s086 have no Doug; sober cards drop the death counter.
  Doug's Nutty Putty beat is a different grey cave (s021-s023) and only his upturned boots show before the cut to black.
- "Doug has died. Again." staged differently each time (CD note): 310 ice over him, then "Again." is the sticker slap on black; 312 a big
  311 -> 312 counter flip; 313 microscope eyepiece with a "SPECIMEN 313" slide label; 314 ghost rises out of the black pit; 315 core death, then
  "Again." is a DEATHS THIS TRIP tally card (7 marks), then "Possibly in the Cretaceous." on a T. rex silhouette. No AGAIN stamp (no repeat site).
- Thumbnail note passed on in asset_requests.md: the worm belongs in permafrost, the seafloor gets microbes (brief section 8).
- Shorts: seafloor microbes (s188-s199 + hook), Ötzi's recovery twist (s055-s066), permafrost worms (s117-s124 + hook). Titles are the titler's.

## 2026-11-09 Director: art round 2 fixes (keyframe review + visual review round 1)
- Art review required: s022 `doug_cap` at the passage mouth; s200-s202 one cap only (Doug `cap_off`, cap beside the suitcase); item titles moved
  into clear sky / above the drawing (s006, s031, s054, s127, s149); s011 and s013 reframed as tight push-ins on the downward crack (head-down /
  uphill arrows) to break up the s006-s014 cross-section run; s197 T. rex glow now red spray `#ff2a1a`, `glow_r: 0`.
- Visual review required: s050 open-suitcase sticker slot + narrator hand holding the SNOWBOUND CAR sticker with red X; s051 Doug walks out of the
  drift with the suitcase (lone cap removed); s118 worm close-up filling the frame, s120 dish family tree "100+ GENERATIONS"; s189 close-up of food
  falling on microbes, s191 Doug shocked close-up + NOT / struck-through DEAD; s088/s089 new assets `smilodon_body` (sabre fangs, cat ears, short
  bobtail kept: Smilodon really had one) and `ground_sloth_rearing` (upright, claws, no trunk), red rim; s145 red `doug_cap` placed on the
  amoeba costume in-shot; s201 single room box right of the gyre sticker.
- Minor/advisory applied: s081 arrow ends on a red glow spot; s121 unreadable circle replaced by a curled worm + DRY FIRST; s036 bigger crossed
  plate; s057 "5,300 YEARS" moved clear of RECENT?; s164 one scaled-up pelvis + PELVIS label; s147 topbar dropped for the transition.
  Not done: extra close-up inside the s130-s145 lab run (optional).
- Re-rendered 39 keyframes (changed shots plus neighbours); `validate shotlist` OK.

## 2026-11-09 Creative Director: thumbnail gate (A/B/C for Test & compare)
Rendered with `python -m studio thumbnail 040-trapped-the-longest`; checked full size and all three `_small` (168x94).

**B. Doug in peril (`thumbnail_test_b.json`): GO.** The strongest of the three, and I'd click it. A mammoth tumbles into a
steep-walled pit onto a shocked Doug standing in the water, with NO EXIT above. One focal moment, the cap and face read at 168x94,
the words don't repeat the title, and the video delivers it (the Mammoth Sinkhole, death 314). Optional: two or three short fall
lines above the mammoth's back so its tilt reads as falling, not floating.

**A. Hero (`thumbnail.json`, also the opening image s001): NO-GO, fix and resubmit.** The worm plus IT WOKE UP reads well at feed size,
but the brief asked for permafrost and this looks like a brown mud cave with fangs. That's the "never seafloor mud" problem again.
1. Remove the `#f7fbff` band at y 0-34. At full size it looks like a cropping bug. Either run the top strata band to y 0, or make it
   a thin frozen surface line with snow on top, at least 60 px tall so it reads as intentional.
2. Make the ground read as frozen. Cool the strata toward the art bible's frozen-ground look (keep the browns, but add pale ice
   veins/lenses `#cfe3ef` with `#4f6b84` crack lines across each band, plus a scatter of small white ice-crystal flecks). Change the two
   cream spikes from `#efe6d0` to ice `#dfe7ee` with a `#4f6b84` outline, or replace them with ice lenses. As drawn they read as teeth or stalactites.
3. Make Doug bigger and give him the brief's reaction. Raise the scale from 0.46 to about 0.7 inside a slightly bigger ice pocket (rx ~190, ry ~160,
   frost-blue outline instead of plain black). Face him toward the worm with his eyes up, so the viewer's eye goes from Doug to the worm.
   At 168x94 he's currently a speck.
4. Move the motion lines so they don't hit Doug's pocket. Right now they sit between the worm's tail and the bubble, as if the bubble is moving.
   Put 2-3 wiggle lines at the worm's head end (right, by the bulb) so it's the worm that's moving/awake.
5. Re-aim the red arrow at the worm's head end (the bulb near x ~1240, y ~450), not at the middle of its back.
After the fixes, s001 must be re-rendered from the new A.

**C. Simple grid (`thumbnail_test_c.json`): GO once fixes 1-3 are in (cosmetic, re-render and check, no new gate).** Four big tiles
with ascending ages are a clean list control, and the 101 MILLION tile with Doug is a good curiosity end point.
1. Remove the black slivers above the two top tiles (y 0-8, they look like a tile frame/shadow clipping at the canvas edge).
   Move both top tiles to y 20 (and the bottom row to y 360) or fix the clip.
2. Tile 1: the worm asset's built-in wiggle lines are cut off by the tile's left edge (three black stubs at x ~20-50). Shift the worm
   right (x ~350) or scale it to ~1.3 so the lines sit inside the tile, or drop them.
3. Label consistency: "101 MILLION" is the only label without the unit. Use "101M YRS" (or "101 MILLION YRS" if it fits at 68 px)
   so the climb reads as one axis.

Summary: B GO now; C GO after small cleanup; A NO-GO until fixes 1-5 are done. Back to the graphic designer.
