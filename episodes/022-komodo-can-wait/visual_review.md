# Visual review: 022-komodo-can-wait

## Round 1: pre-render keyframes (2026-10-18)

Scope: all 24 contact sheets (s001 to s288) in `build/contact/`, with full-size checks of s061, s187 and s232 in
`build/keyframes/`. s001 is a "(thumbnail pending)" placeholder, which is expected at this stage. The thumbnail
gets its own check after packaging.

**VERDICT: FAIL**

### What already works
- Doug is on-model in every shot (red cap, white head) and reads against every background, the night and purple
  bands included.
- The HUD works. DOUG DEATHS goes 178 to 186 with one step per death (s027, s076, s098, s121, s142, s166, s233,
  s282), and that matches the series bible. THE WAIT only ever goes up (0 S to ABOUT 4,000,000 YR). The six band
  cards (SECONDS. / HOURS. / DAYS. / WEEKS. / MONTHS. / YEARS.) are clear.
- There is no gore anywhere. Every death is a dust cloud, a dropped cap or the ghost Doug. The tooth close-ups
  (s029, s033, s034, s040) show dark-red gums with no blood. "Adults eat young dragons" (s225, s226) is drawn as
  an arrow and a label, never as eating. The RIP stone (s286) is fine.
- There is no kids'-show risk. Hatchlings, tennis balls, flowers and the picnic are drawn flat and dry, and the
  jokes stay adult ("full, not friendly", "Doug was not required"). The chapter title "The Nursery" is fine in
  context.
- Most data visuals are clear: the pie charts (s084 to s087), the meal calendars (s194 to s200), the bottles
  (s175), the timeline (s272) and the maps (s007, s106 to s109, s260 to s262). Labels are spelled correctly and
  none are cropped.

### Required fixes

1. **s187, s188, s189: delete the stray white square.** Director. Each of these shots contains a raw element
   `{"type":"rect","x":764,"y":830,"w":46,"h":40,"fill":"#ffffff"}` that sits beside Doug's hand like a broken
   prop. Remove it from all three shots. In s189 the line is about the thermos, but no thermos is shown. Show one
   next to "NOT FOOD" (crossed out with `red_x`, or as an outline inside the dragon). The library has no thermos
   drawing, so the illustrator needs to draw a small `thermos` asset that matches the green flask in the s184
   picnic blanket.
2. **s146: the calendar is blank.** Director. Copy the s119 approach and add a text element on the calendar:
   `{"type":"text","text":"300 YRS","x":400,"y":540,"size":34,"bold":true,"appear":0.2}`. This matches facts.md:
   "introduced only 300 years ago" (Fry). If you would rather not add the number, delete the calendar and let the
   "A FEW CENTURIES AGO" label carry the shot.
3. **s120, s121, s122: Doug claims the "next island" on the shore he started from.** Director. In s116 to s119 the
   far island is the hill on the top horizon and the near beach is home. In s120 Doug and the flag stand on that
   same near beach, so it looks like he paddled back. Reverse the geography for s120 to s122: make the foreground
   beach the new island, put the old island's hill (the s116 hill) small on the far horizon, beach the ring at the
   waterline, and keep Doug and the flag on the foreground sand. The dragon in s121 and the lying dragon in s122
   then read as "already waiting on the beach". Also end the "safe" bubble's tail at Doug's head. Right now it stops
   at the waterline, about 115 px away.
4. **s035: the tooth is drawn bigger than the coin, but the narration says it is "shorter than a quarter is
   wide".** Director. The tooth (`komodo_tooth`, scale 0.9) stands about 1.5 times the coin's height. Scale the
   tooth to about 0.45 or enlarge the coin (r about 180) so the tooth is clearly smaller than the coin's diameter,
   and put them side by side on the same baseline.
5. **Floating "komodo_head" cut-outs on open ground read as severed heads.** Director. The head asset has a
   feathered neck edge. On close-up plain backgrounds that reads as a crop (s053, s058 to s060, s063 to s065 are
   OK). On open sand it reads as a disembodied head lying on the ground (see the s061 full-size frame). Affected
   shots: s055, s057, s061, s062, s066, s069, s070, s076, s077, s123, s127, s128, s129, s130, s132, s133, s158,
   s159, s160, s165. For each one, either swap in `komodo_dragon` (full body), or place the head so the neck edge
   is hidden: run it off the frame edge, or put it behind the rock, a bush or the ridge line. The ridge-crest
   crowds (s125, s126, s139 to s141) can stay as long as the heads sit just behind the crest line with the neck
   edge covered. s123 has a second problem: two heads meeting tongue-to-tongue on a chapter card reads as a kiss.
   Use two full-body dragons facing the viewer or a ridge-line crowd instead.
6. **s162: the buffalo that "finally lies down for good" is missing.** Director, plus illustrator if needed. The
   frame shows only three resting dragons, which reads as "dragons lie down". Add the buffalo lying on its side
   (cartoon: eyes closed or X-eyes, no wounds) with the dragons waiting at a distance. If `water_buffalo` cannot
   be rotated cleanly, the illustrator should draw a `water_buffalo_lying` asset.
7. **Variety: long runs of near-identical frames.** Director.
   - **s013 to s028 (Ambush):** 14 of these 16 shots use the same frame: dragon log centre-right on the trail,
     Doug left, same desert. Break up the run. s016: top-down trail with deer and boar walking along it. s020
     ("lies low ... perfectly quiet"): tight close-up of the log's open eye (`komodo_log_eye`). s024: close-up of
     Doug's face buried in the field guide. s025: swap s024's closed book for the open field-guide page from s285,
     with the dragon out of focus behind it.
   - **s177 to s181 (dragon on the rock, 5 frames):** make s181 a calendar strip, MON to FRI with all five days
     ticked ("a full working week"), with no rock.
   - **s205 to s212 (`komodo_bloated` on the rock, 8 frames in a row):** make s207 a wide shot looking down the
     path with the line of 100 deer and the dragon small in the corner. Make s209 and s210 a close-up of the
     dragon's half-closed eye with Doug's tiny waving hand at the edge. Make s212 a punch-in on the swollen belly
     under the "FULL" label.
8. **s034: "SERRATED" overlaps the tip of the lower jaw.** Director. Move the word down so it sits under the bread
   knife, or above the snout, clear of the drawing.
9. **s126: the red arrow (1700,700 to 1800,900) points at empty ground.** Director. Remove it, or replace it with
   short scent arrows from each head converging on one point off the right edge.
10. **s249: "Z Z" reads as snoring.** Director. Change the label to "ZZ CHROMOSOMES", or draw two small X-shaped
    chromosome glyphs labelled Z and Z, so a viewer doesn't read it as "Zzz".
11. **Speech-bubble tails stop short of Doug.** Director. In s140 ("can I help?"), s184 ("peace?"), s209
    ("hi friend?") and s252 ("hello?") the tail ends on the horizon line well above Doug's head, so it isn't clear
    who is speaking. Set each `tail` point to just above Doug's head (Doug x, about head y minus 20).

### Advisory (fix if cheap, does not block)
- s153: the attacking dragon is half hidden behind the buffalo's legs. Separate them, with the dragon lunging at a
  hind leg and a dust puff.
- s250, s251, s257 to s259: Doug swimming in the top-right corner has no setup and slightly undercuts "empty
  island" in s250. Consider removing him from s250 and s251.
- s251 ("other animals"): it shows the same Komodo island again. A small shark or snake silhouette with "?" would
  match the line better.
- s276: the two blue squares on the map don't say "flooded habitat". A blue hatched coastline band would read
  faster.
- s092: Doug in the "sit" pose on a plain background looks like he is floating. Give him the log from s096 or use
  the stand pose.
- s284: the "4,000,000 YR" text on the stopwatch is too small to read. Enlarge the stopwatch or rely on the HUD.

### Routing summary
- Director: fixes 1 to 11.
- Illustrator: the `thermos` asset (fix 1) and possibly `water_buffalo_lying` (fix 6).
- Art director: nothing blocking. Please sign off on the head-placement rule in fix 5 (head only when the neck
  edge is hidden) as a standing layout rule.
- Graphic designer: thumbnail not reviewed yet (pending).

Re-run `python -m studio keyframes 022-komodo-can-wait --shots <changed ids>` and send the new sheets back for
round 2.
