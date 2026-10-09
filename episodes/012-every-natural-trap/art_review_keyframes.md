# 012 Every Natural Trap: art director keyframe review

Date: 2026-10-09. Scope: contact sheets `build/contact/sheet_01..25.png` (s001-s298) plus full-size frames in `build/keyframes/`
for every suspect shot. s001 was skipped because the thumbnail is still pending.

## Verdict: FAIL (7 required fixes, all small and all in `shotlist.json`)

The episode is on-model and on-palette, and the item colour sequence reads well: sky-blue snow, red-orange canyon, under-ice blue
`#3a9ad9`, grey avalanche, turquoise Dead Sea, glacier blue-grey, then the purple/orange Ice Age, the brown cave and amber. Every item has a
caption bar that matches its chapter name in caps. Item title cards are red with an outline and sit below the counter zone. The counter runs
100 to 107 and ticks only on death beats (s030, s057, s116, s180, s215, s248, s291). Both survivals hold their value (s088, s146). The red cap
is in frame on every death. Real-victim cards (s047-s051, s169-s175) stay muted, with no people and no jokes. Reveals go silhouette first,
colour later (s053, s194 to s205, s202 to s203). Annotations appear in every item, and the layouts vary well. Nothing is gory.

The FAIL comes down to a handful of readability defects where Doug disappears or gets skewered, plus one counter-zone touch.
**All of them go to the director** (composition). Nothing goes to the illustrator.

## Required fixes (director)

1. **s183, s184: Doug's body is invisible.** The `doug` carries `"ink": "#000000"` on the near-black `#2a2e36` night backdrop, so only the
   white head and cap show. Remove the `ink` key so auto-ink turns him white. He stands on dark ground with no light prop behind him, so
   auto-ink is safe here.
2. **s255, s261, s262, s279: Doug flips to white ink on the light amber background.** Doug's `x` (700, or 1700 in s279) lands exactly on
   the black outline of a background post, so the auto-ink sample reads black and turns him white. The result is thin white lines on
   orange and a head with no outline, which doesn't match the black-ink Doug in s253/s254/s256-s259. Per the art bible rule on dark props
   behind Doug, add `"ink": "#000000"` to the `doug` in all four shots, or move him about 40 px off the post edge.
3. **s015, s024: Doug is lost inside the small background pine.** In s015 he is at `x 300`, which is the `pine_tree` at `x 300`, and his
   arms and torso merge into the dark-green zigzags. s024 has the same problem at `x 250`. Move Doug (and his ski line) into the clear
   snow between the small pines and the big tree, for example `x 520` as in s004/s005, so his whole body reads against the pale mountain.
4. **s041, s042, s043: the SE drainage curve runs through Doug's neck and face.** The curve `[[1700,950],[1350,820],[960,700]]` crosses
   Doug at `x 1500, y 939` (his head is about y 820-880). Either end that curve at about `x 1380`, or move Doug to about `x 1650, y 1000`,
   below the line. Keep the same position in all three shots.
5. **s041, s042, s043: the counter zone is touched.** The NE drainage curve ends at `(1800, 180)`, right on the bottom edge of the
   DOUG DEATHS box, and in s042/s043 the second `storm_cloud` at `(1600, 300)` tops out at about y 225, inside the reserved band
   (x 1300-1860, y 110-230). Move the curve's end to about `(1700, 300)` and the cloud to about `(1560, 360)`. MILES AWAY at y about 470
   can stay where it is.
6. **s152 and s004: a red arrow skewers Doug.** In s152 the first arrow `[300,680] -> [900,690]` passes straight through Doug's face
   (head at about y 610-700). Lower both arrows to about y 760 (below the arms and above the 720 flow line), or raise them to about y 560
   on the ice, clear of his head. In s004 the arrow `[900,520] -> [440,700]` from A WEEKEND crosses Doug's torso at about y 690 and stops
   beside the suitcase instead of on it. Re-aim it to `to: [380, 730]` (the suitcase lid) with `bend: 60`, so it arcs over Doug's head
   instead of through his body.
7. **s219-s247 (26 shots with `gear: ["helmet"]`): remove the helmet.** The `helmet` gear is the scuba bubble from 003 (a pale-blue
   ring round the head). In a dry cave it reads as a fishbowl or a halo, and a halo on a living Doug muddles the death grammar
   right before the s248 death. Delete `"helmet"` from `gear` in every Altamura shot (s219, s220, s221, s223-s235, s237-s241, s243-s247).
   Doug already auto-inks white on the cave brown and reads cleanly without it. The caver asset keeps its own helmet.

Re-render only the touched shots (`python -m studio keyframes 012-every-natural-trap --shots s004,s015,s024,s041,s042,s043,s152,s183,s184,s219,...,s247,s255,s261,s262,s279`)
and send the new contact sheets back to me. I will only look at those shots.

## Advisory (not blocking, no re-render needed)

- **Wordart over background ridgelines** (s003-s005, s008, s009, s016, s017, s101, s105, s106, s151, s164, s176-s179): the mountain
  outline runs behind the letters. It stays legible because the wordart has its dark outline, and the ridges are backdrop, not maps or
  land masses, so I'm not failing it. In future shots, prefer clear sky about 60 px above the ridge peak.
- **s194, s202: the silhouette glow is faint** on the dark-brown Ice Age ground (dark red on `#3a2a1a`). It reads as a silhouette, but
  the red-glow cue is weak. Next time use a brighter glow spray (`#ff3a2a`) or a larger `glow_r`.
- **s087 (ONE ARM) and s168 (EVERY YEAR):** the label bottoms sit right on the safe-area line at y about 1040. Nudge them up about 20 px if
  either shot is re-rendered anyway.
- **s029:** Doug's seated torso partly overlaps the tree skirt. He still reads, and it's in keeping with "leaned back against the tree".

## Art bible follow-up (mine, after the fixes land)
Log the new environment colours so later episodes match: Dead Sea water `#8fd8d0` and shore `#f3f1ea`, Ice Age La Brea sky band
(purple over orange over `#3a2a1a` ground), and the amber forest ramp. Add the rule from fix 2: never put Doug's `x` on a prop's outline,
because the auto-ink sample reads the black edge.

**ART (keyframes): FAIL.** Fixes 1-7 go to the director. After the re-render, I will re-check only the touched shots.

---

## Round 2 re-check (2026-10-09)

Scope: only the 46 re-rendered shots, from contact sheets `build/contact/sheet_01..04.png` (changed shots only), with full-size
frames for s004, s015, s043, s152, s168, s183, s261 and s279. These were fix shots s004, s015, s024, s041-s043, s152, s183, s184,
s219-s221, s223-s235, s237-s241, s243-s247, s255, s261, s262 and s279, plus the visual-screener advisories s087, s089, s145, s168,
s227 and s291-s293.

### Verdict: PASS

1. **s183, s184:** fixed. There is no `ink` key now, so Doug auto-inks white and reads in full (head, body, arms, legs) on the night
   backdrop.
2. **s255, s261, s262, s279:** fixed. `ink: "#000000"` is set on all four, and Doug is black-ink, matching s253-s259. In s261 and
   s279 he still stands in front of a post, but his black lines read on the darker post fill and his head keeps its outline. Not blocking.
3. **s015, s024:** fixed. Doug and his skis stand in clear snow at about x 520, away from the pines, and his whole body reads against
   the pale mountain.
4. **s041-s043:** fixed. The SE curve now ends at about x 1380, and Doug stands below and right of it with nothing crossing him. He is
   in the same spot in all three shots.
5. **s041-s043 counter zone:** fixed. The NE curve ends at about (1700, 300), and the second cloud sits at about y 290-410, clear of
   the DOUG DEATHS box.
6. **s152, s004:** fixed. In s152 both arrows run at about y 690 to the right of Doug's head, with nothing touching him. In s004 the
   arrow arcs over Doug's head and lands on the suitcase handle.
7. **s219-s247 helmet:** fixed. No Altamura shot carries `helmet` gear any more. Doug auto-inks white on the cave brown and reads
   cleanly. The caver in s220 keeps his own helmet.

Advisories the director also took:
- s087 ONE ARM and s168 EVERY YEAR were lifted, and the label bottoms now sit at about y 1020, inside the safe area.
- s089: the BRINICLE sticker is scaled up and readable at phone size.
- s145: the MORECAMBE BAY sign is bigger and legible.
- s227: the drop now sits above DRIPS, so the letters are clean.
- s291-s293: preserved Doug wears the gall-mite costume inside the bead (continuity fixed). The cap sits on the outside, and the
  counter reads 107.

No new defects. Style, palette and zone colours match the round 1 shots, Doug is on-model everywhere, and the layouts still vary.
Nothing is gory.

**ART (keyframes): PASS.** I have added the art bible follow-up (012 environment colours and the auto-ink rule about prop outlines)
to `channel/art_bible.md`.
