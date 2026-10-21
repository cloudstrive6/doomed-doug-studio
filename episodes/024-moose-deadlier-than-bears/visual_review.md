# 024-moose-deadlier-than-bears: visual review

## Round 2: keyframes + thumbnails (2026-10-21)

**VERDICT: PASS**

I checked all 24 re-rendered contact sheets (s001 to s279 plus the endslate). I opened full frames for s050, s100, s216 and s266. I viewed the three thumbnails at full size and at the 168x94 feed size.

### Round 1 required fixes: all verified
1. **s071-s074 (grizzly removed).** Fixed. The calf scene has no bear, and at Doug's death in s074 only the cap in the willows and the field guide "NO" are on screen. The "never met a bear" punchline holds.
2. **s143 (rearing bull).** Fixed. The new rearing pose has the palmate rack, so it reads as the same bull from s142. s129 uses it too. s137 is still the cow defending her calf, which is correct.
3. **s035 (plants, waterline).** Fixed. There is one surface line with the board on it, the seagrass is visible on the lake bed, and the "PLANTS" arrow lands on it.
4. **s047 (Doug on water).** Fixed. Doug is back on the paddleboard at the shoreline.
5. **s180 (map label).** Fixed. "ALASKA + NW CANADA" sits right under the circle on Alaska, with the shed rack beside it.
6. **s056 (calendar overflow).** Fixed. "MAY-JUN" fits inside the page with a margin.
7. **s236 (circle over text).** Fixed. An ellipse now surrounds "KILLED: 0" without touching any glyph.
8. **s100 (gravestone).** Fixed. The crossed-out "RIP DOUG" stone with the cap is on the ground, clear of the trunk and the field guide. The red X sits over the lettering on purpose, and "RIP" still reads.

### Round 1 should-fix items
- 9 s229/s230: a red ski-equipped bush plane replaces the jet. Done.
- 10 s114/s119: the divider now starts below the chapter tag. Done.
- 11 s037: "NO OTHER DEER" now sits on clear water and nothing pokes through it. Done.
- 12 s044 "18 FT+" and s046 "18 FT? UNMEASURED". Done.
- 13 s216: the moose is shown from behind, facing the headlight, with Doug at its rump. Done, and the beat reads well.
- 14 s109/s110: the moose and the bear are now separate, with the speed labels over the right animals. Done.
- 15 Variety: s254 is now the black bear on a coastline, which breaks the map run. s261-s263 have large moose-vs-deer icons, so the Maine cards look different from the Newfoundland cards. s042-s046 are still close to each other, but the scale changes and the labels and props differ, so this is acceptable.
- 16 s092/s093, s200, s266: the article picture boxes now show a moose silhouette. Done.
- 17 s050-s052: the surfacing head has broad, outward ears and the pondweed drape, so it reads as a moose. Done.
- s001: the thumbnail is in place as the opening frame. Done.

### Full-episode re-check (no new blockers)
- Doug is on-model and readable in every shot.
- The death counter runs 195 to 203, with deaths at s026, s074, s123, s145, s172, s196, s245 and s274, each after a black beat. The BEAR/MOOSE ticks run to 5-11. The payoff book shows 0 and 8.
- The sober cards (s146-s148, s258-s263) have no gags and their text is legible.
- There is no gore. s077's red halo behind the tree silhouette is a mood glow, not blood.
- Nothing is in a kids'-show tone. All the text I checked is spelled correctly and not cropped.

### Thumbnails (feed size 168x94)
- **A (`thumbnail.png`, "WRONG ANIMAL").** This is the strongest of the three. The head-on bull is the clear focal point, and the nervous grizzly with sweat drops plus tiny Doug read instantly. The text is legible at 168 px and shares no word with the title. It complements the title "Why Moose Are Deadlier to Doug Than Any Bear" without promising anything the video doesn't deliver. PASS.
- **B (`thumbnail_b.png`, "35 MPH").** It has one focal point: the charging bull against yellow, with a fleeing Doug. "35 MPH" is crisp at feed size and matches the sourced ~56 km/h top speed, so it is not misleading. The bear is not shown, so the title's contrast rests on the title alone. That is acceptable for an A/B variant. PASS.
- **C (`thumbnail_c.png`, chapter grid).** It shows a 2x3 grid of chapter tiles: Calf, Dive, Rut, Hooves, Train, Highway. Every tile has a moose. Doug is in four of them, very small, and not in Train or Highway. **The labels are blurry but readable.** At 168 px the labels are about 6 px tall in a thin regular-weight font, so they are soft. In my feed-size render I could still read all six ("The Calf" ... "The Highway"). The tile pictures carry the read even without the labels, so this is not a blocking defect. C is still the weakest of the three for clarity because it has six focal points by design. PASS for A/B testing, with the polish below.

### Optional polish (not blocking)
1. **thumbnail_c (graphic designer).** Make the labels bold (or add the same black outline as A/B), drop "The " so each label is one large word (CALF, DIVE, RUT, HOOVES, TRAIN, HIGHWAY), and enlarge them to about 70 px cap height so they stay sharp at 168 px. Doug is barely visible in four tiles and absent from Train and Highway, so scale him up and add him to those two.
2. **s049, s050 (director).** "MIDDLE" and "POND WEED" are drawn over pine tips, the same layering issue as the old s037. Draw the labels after the treeline or lift them to about y≈80. They are legible as they are, thanks to the outline.

**Routing:** this needs no blocking action. The optional items go to the graphic designer (1) and the director (2). The next screen is post-render: `build/samples/`, `qc.json`, and the Shorts.

## Round 3: thumbnail C re-check (2026-10-21)

VERDICT: PASS

I checked `build/thumbnail_c.png`, rebuilt at 18:21 from the edited `thumbnail_test_c.json`, at full size and downscaled to 168x94 (feed size). `thumbnail_c_small.png` matches the full-size image.
- **Labels: fixed.** They are now one word each in heavy black type (Calf, Dive, Rut, Hooves, Train, Highway), each under its tile on white. All six are crisp at 168 px, and the Round 2 blur is gone. No label uses a title word.
- **Doug in all six tiles: fixed.** He is at scale 0.33, with the red cap and white head readable in every tile at feed size. This includes Train (standing by the moose and locomotive) and Highway (pinned between the car and the bull). His lines are black on every background.
- **Cropping:** nothing important is cropped. The edges trim the Dive antlers, the Highway car's rear and the moose's rump, but those are deliberate bleeds inside the frames. The Hooves bull's hump just touches the top edge of its tile, and its head and hooves are fully in frame.
- **Gore and tone:** none. There are cartoon peril faces only, and no blood or injury marks. In Calf, Doug waves happily at the cow, which is ironic setup rather than a kids' show tone.
- **A and B are unchanged.** `thumbnail.json` and `thumbnail_test_b.json` have not been modified since the last commit. The re-renders match Round 2: A is "WRONG ANIMAL" with the head-on bull, the sweating grizzly and Doug; B is "35 MPH" with the charging bull and Doug running away.

Minor and not blocking (graphic designer): the Hooves tile is the weakest read at 168 px. The rearing bull becomes a brown diagonal blob with stick front legs. Pulling it about 20 px down and right, so the head sits clear of the top edge and nearer Doug, would help. In Highway, Doug's cap brim touches the moose's muzzle. A gap of a few pixels would make the cap pop.

Routing: no action needed. C is cleared for the A/B/C test.
