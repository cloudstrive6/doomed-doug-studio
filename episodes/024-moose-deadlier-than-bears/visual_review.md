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

## Round 4: post-render (final.mp4, thumbnails, Shorts) (2026-10-21)

VERDICT (main): PASS
VERDICT (shorts): FAIL

### Main video (`build/samples/f_001-f_032`, `build/qc.json`)
- `qc.json`: duration 967.1 s (16:07), `problems: []`. None of the 32 samples is black, blank, glitched or frozen-looking. Each sample is a different composition and chapter tags progress Deer to Highway.
- Counter continuity: DOUG DEATHS runs 195 to 203 with no reversals. The BEAR/MOOSE tally ends 5-11 and the closing card shows 8 vs 0, matching the script's design (tally = narrator's judgement, not deaths).
- Doug is on-model (red cap, white head) and readable in every frame he appears in. There is no gore. The f_008 red halo is mood glow, the f_012 rearing bull in The Hooves is cartoon, and the f_030 Maine "MOOSE VS DEER" card is sober. Nothing in a kids' show tone. Every caption and label I sampled is spelled correctly, not cropped and legible.
- Minor and not blocking (director): f_002 / s015 catches the ADF&G card before its `question_mark` appears at 0.4, so for about 1 s it is an empty cream box with a small grey source line. Setting `appear` to 0.1, or adding the source line at a larger size, would fill the gap.

### Thumbnails (`thumbnail.png`, `_b`, `_c` + `_small`, re-rendered 18:36)
- They are unchanged from the Round 2/3 approvals. A ("WRONG ANIMAL") is still the strongest: one focal bull, the nervous grizzly and Doug read at 168 px, and it complements "Why Moose Are Deadlier to Doug Than Any Bear" without misleading. B ("35 MPH") and C (one-word grid, Doug in 6/6 tiles) are also readable at feed size. PASS.

### Shorts (`build/shorts/short01-04.mp4` + previews; frames at 1 s, 20/40/60 %, and the last 8 s)
- In all four Shorts the format is correct. The title is legible at the top, the drawings are not clipped at the sides, and the subtitles are legible and centred. (In the short03 preview, "with thei" is a downscale artifact. The video frames at 23-24 s show "bull moose with their" in full.) The end card arrow points down to the link, and each end card has a red-outlined silhouette with "???".
- **short03 (antlers locked): PASS.** The title is paid off (Unalakleet, 8 in of ice, the locked racks). The outro "How that ended is in the full video below" leaves the question open, and the charging-moose silhouette with antlers is recognisable.
- **short01 (Newfoundland): FAIL.** The end card "WHAT WAS STANDING IN THE ROAD?" is answered by its own picture and by the whole Short: the silhouette is a moose, and the outro says "a moose never has to attack anyone". The question gives the viewer nothing left to learn.
- **short02 (nostrils): FAIL.** The outro answers the end-card question. It says "On a snowed-in railway, it won't move for a train", and the card then asks "WHO MOVES FIRST: MOOSE OR TRAIN?". The locomotive silhouette is mostly covered by "???", but the cab and wheels still read, so the silhouette is acceptable.
- **short04 (drunk moose): FAIL.** The outro answers the end-card question. "...could, and it didn't move" means the moose kept the path, so "WHO GAVE UP THE PATH FIRST?" is already answered.

### Required fixes (all `shorts.json` text edits, routed to the director: `outro` / `end_card`; then `shorts render`)
1. **short01:** keep `tease_from` s272 and `tease_asset` moose. Change `end_card` to `DID DOUG SEE IT IN TIME?`. The outro can stay, or tighten it to "On that island's roads, a moose never has to attack anyone. Doug drove home there at night. Full video below."
2. **short02:** change `outro` to "Underwater, a moose ignores you. On a snowed-in railway, Doug and a moose shared one track with a train coming. It's linked below." Change `end_card` to `WHO GOT OFF THE TRACK?`. Keep the `locomotive` tease, or switch `tease_asset` to `moose` so the silhouette reads more clearly.
3. **short04:** change `outro` to "That moose couldn't get down. The one standing at the end of Doug's freshly shoveled Anchorage path could. Full video below." Keep `end_card` `WHO GAVE UP THE PATH FIRST?` and the moose tease.
4. After the re-render, the visual screener only needs to re-check the last 8 s of short01, short02 and short04.

## Round 5: Shorts re-check after end_card/outro fixes (2026-10-21)

Scope: `build/shorts/short01-04.mp4` re-rendered 18:46-18:48 from the updated `shorts.json`. For each Short I checked the opening frame and frames at -9, -7, -5, -3, -1.5 and -0.3 s from the end. Main video and thumbnails are unchanged since Round 4 (`final.mp4` untouched, qc rerun clean), so the Round 4 PASS still applies.

- **short01 (Newfoundland, 36.9 s): PASS.** The opening frame shows the title and the Newfoundland map with the "The island of Newfoundland" subtitle, all legible. The outro subtitles read "...a moose never has / to attack anyone. Doug / drove there at night. / Full video below." The end card asks "DID DOUG SEE IT IN TIME?". The moose silhouette shows what he meets, but nothing in the outro or the card says whether he saw it, so the question stays open. The red-outlined antlered moose with "???" is recognisable, and the arrow points down to the link.
- **short02 (nostrils, 47.4 s): PASS.** The opening is the hook frame of the moose fully under the lake with Doug on a raft above, and the "A moose can vanish" subtitle. The outro reads "Underwater, a moose ignores / you. On a snowed-in / ...moose shared one track / with a train coming. / It's linked below." It no longer says who moved. "WHO GOT OFF THE TRACK?" is open, and the locomotive silhouette (cab, boiler and wheels showing around the "???") reads as a train.
- **short03 (antlers locked, 51.5 s): PASS, unchanged.** The opening shows the Unalakleet ice and the "Two bull moose were" subtitle. The outro ends "How that ended is in the full video below", with "DID THE CARDBOARD ANTLERS FOOL HIM?" and the charging-moose silhouette. The question is not answered.
- **short04 (drunk moose, 50.1 s): PASS.** The opening shows the moose stuck in the apple tree at night with Doug and the house, and the "A moose was stuck" subtitle. The outro reads "...down. The one standing / Doug's freshly shoveled Anchorage / path could. Full video / below." It now says only that this moose could move, not who gave way, so "WHO GAVE UP THE PATH FIRST?" is open. The moose silhouette is recognisable.
- In all four, the title is legible at the top, nothing is clipped at the sides, the end card is centred and has no overlaps, and the @DoomedDoug tag is present. There are no black or frozen frames in the tail.
- Minor and not blocking (titler): the short01 `description` ("what that did to Doug on Newfoundland's night roads") hints at the outcome a little. It is acceptable, but "shows what Doug met on Newfoundland's night roads" would keep the cliffhanger cleaner.

VERDICT (main): PASS
VERDICT (shorts): PASS
