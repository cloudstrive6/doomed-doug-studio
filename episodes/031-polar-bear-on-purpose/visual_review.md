# Visual review: 031-polar-bear-on-purpose

## Round 1: pre-render keyframes (2026-10-29)

I looked at contact sheets sheet_01 to sheet_20 (s001 to s234 and the endslate). s001 is the thumbnail placeholder, so I skipped it.

VERDICT: FAIL

The episode is in good shape overall. Doug is on-model in every shot: red cap, white head, readable on every background, including the ghost, the seal suit and the dark scenes. Every death is cartoon and off-screen: rubble plus cap, the cap on the thermal screen, binoculars plus cap, a sliding cap, the collapsed tent, the bowl of berries, the cap in a cell. There is no gore, no blood and no realistic violence. The open red mouth on the stairwell bear (s151) is cartoon. Nothing has a nursery or kids-show tone. Text is spelled right and nothing is cropped. The maps put Svalbard, Novaya Zemlya and Churchill in sensible places. The counts check out: 62 lairs vs 6 seals, track rows in a 3/16/8 ratio for 15/80/41 m, 19 of 20 bears with one gaining.

It fails on one continuity error the viewer can see and hear (the distance tracker contradicts the spoken chapter cards), one prop that doesn't read (the seal suit), and four runs of near-identical compositions. All are cheap fixes.

### Required fixes

1. **Director: the bear tracker contradicts the narration on s106/s107 and s157/s158.** The narrator says "Ten meters." and the big card reads TEN METERS, but the HUD says `BEAR: 20 M`, which it has said since s080. The narrator then says "Zero." over a `BEAR: 3 M` HUD. Make the tracker match each spoken distance card:
   - s105 to s129: `BEAR: 10 M`. The narration says "from ten meters" at s105.
   - s157 onward: `BEAR: 0`, so the tracker hits zero at the Tent chapter.
   - The 3 M, 1 M and 0.5 M steps then go. If you want to keep the "creeps closer after every death" steps, put them only in stretches where no spoken distance card contradicts them (s080 to s104 can stay 20 M).
2. **Illustrator: the prone seal suit (s099, s100 reuses the gag, s101, s102, s103, s104, s221) reads as a sea turtle or fish, not a seal.** It's drawn top-down with four flippers, a forked fish tail and a beige oval belly. Redraw it as a side-profile ringed-seal body to match the `ringed_seal` asset: grey with ring spots, a short tapered body, a small rear flipper pair. Add a seal hood with whiskers around Doug's head, like the upright "LAST TIME" inset in s100. Keep Doug's head and cap fully visible. Without the DRESSED AS A SEAL caption, s101 to s104 don't read.
3. **Director: variety, s016 to s020 are 5 near-identical crosswind diagrams** (same pale field, same three blue wind arrows, same red dashed path, small bear; s019 only recolours to night). Recompose two of them:
   - s018 (MOVING FAST): a mid-shot of the bear trotting with speed lines and the WIND UNDER 36 KM/H label on a wind sock.
   - s020 (THE MOST SCENT): top-down, with the bear's zig-zag crosswind path cutting through several scent plumes, and a nose-height close-up of the bear sniffing on the left.
4. **Director: variety, s116 to s120 are 5 near-identical paw close-ups** (the same paw in the same place in 4 of the 5).
   - s118 (SNOWSHOES): show the paw pressing on thin ice with a crack spreading around it, side view, with a small Doug sinking next to it for contrast.
   - s120 (gripping "anything slippery"): show the claws hooked into a seal-shaped silhouette or a fish on the ice, with no wound. Or show Doug slipping on ice next to the planted paw.
5. **Director: variety, s152 to s155 are 4 identical three-cell shots with Doug in the middle cell.**
   - s153 (DOUG IS FINE): close-up of Doug's face through the bars, giving a thumbs-up.
   - s154 (NOT BEING FED): an empty bowl outside the bars with a NO FOOD tag.
   - s155 (STILL 250): zoom in on the death counter, or show Doug pointing at it.
6. **Director: variety, s228 to s231 are 4 identical single-cell shots with the cap.**
   - s230 ("It will not be fed"): an empty bowl in front of the cell.
   - s231 ("That is the policy"): an official holding a POLICY clipboard next to the cell, or a close-up of the cap behind the bars.
7. **Director: s192, the key subject isn't obvious.** A brown, blue and white vertical band with a dashed line, "1979", "2015" and an arrow doesn't say "the ice-free season grew by three weeks". Replace it with two horizontal season bars: 1979 with a short blue "ice-free" segment, and 2015 with the same bar plus a red "+3 WEEKS" extension. Put Doug at the end of the longer bar.
8. **Director: s210 reads as 50%, not 88%.** It shows 12 squares with 6 red and no month labels. Label the squares J F M A M J J A S O N D so it reads as a calendar (July to December in red), and keep "88%" as the headline.
9. **Director: s105, the X sits on the bear's back.** That reads as "bear dead" or "wrong bear". The line is "it doesn't need to swim at all". Move the X onto a small water/swim icon (wave plus ripple) between Doug and the bear, and leave the bear unmarked.

### Polish (do these if they're cheap; they don't block a PASS)

10. **Director:** s149, the COMES BACK caption is laid over the building windows. Move it into the sky above the roofs. s132, the STATE OF EMERGENCY caption touches the roofline; nudge it up about 15 px.
11. **Director:** s204, the small black bear silhouette touches the last "E" of ON PURPOSE. Move it about 60 px right, or down onto the horizon.
12. **Art director:** the paw icon in the tracker is dark on dark and invisible on navy and black backgrounds (s019, s044, s046 to s048, s052, s053, s219). Give the paw icon a white backing or white fill, like the box beside it.
13. **Director:** s216, the red X covers the "O" of PEOPLE ("PE PLE"). Either strike through the word with one line or put the X beside it, so PEOPLE stays readable.
14. **Illustrator:** the berry pile (s178 to s180, s185) is a dark brown mound with dots. At feed size it can read as dung. Lighten the mound to a berry red/purple with brighter blue berries and a couple of leaves, or reuse the bowl of berries from s197.
15. **Director:** s104, the floating empty plate above HAS TO EAT doesn't read on its own. Put the plate on the ice floe in front of the bear, or drop it.
16. **Director:** s031, the black bear on the right can read as a different species (a black bear). Add the BLACK SKIN tag (as in s030) or a "fur removed" dotted outline around it.

### Checked and fine
- Cartoon deaths with no bear on screen at the moment of death (s026, s052, s079, s129, s174, s200, s227). The cap is the readable "Doug died" signal every time, and the counter steps 246 to 253 in order.
- The red-outlined black bear silhouette as a threat or tease (s003, s025, s082, s177, s190, s203, s204). The red-outlined "bubbles" on s082 are bubbles, not blood.
- Recap montage s218 to s222 reuses earlier compositions on purpose. That's fine.
- Endslate: the arrow points to the next-video slot and the subscribe circle is clear.

## Round 2: keyframe fixes and thumbnails (2026-10-29)

I re-checked the re-rendered keyframes (build/keyframes/ and contact sheets sheet_01 to sheet_11, which cover the changed shots) against every round 1 fix. I also screened build/thumbnail.png, thumbnail_b.png and thumbnail_c.png at full size and at 168x94 (`*_small.png`).

VERDICT: PASS

### Round 1 required fixes
1. **Tracker vs narration: fixed.** s080 to s104 read `BEAR: 20 M`. s105 to s156 read `BEAR: 10 M`, so the "Ten meters." card at s106 matches. s157 onward reads `BEAR: 0`, so "Zero." matches. The 3 M, 1 M and 0.5 M steps are gone.
2. **Seal suit: fixed.** s099 to s104 and s221 now show a side-profile grey ringed seal with ring spots, a tapered body and rear flippers. There's a whisker hood, and Doug's head and cap stay fully visible. It reads as a seal without the caption.
3. **Crosswind run: fixed.** s018 is now a trotting mid-shot with speed lines and a wind sock labelled WIND UNDER 36 KM/H. s020 is now top-down, with the zig-zag path through three scent plumes and a sniffing inset. The run is broken.
4. **Paw run: fixed.** s118 shows the bear on thin ice with cracks and Doug sinking. s120 shows the claws hooked into a fish with no wound, and Doug slipping.
5. **Three-cell run: fixed.** s153 is a close-up of Doug through the bars. s154 is a single cell with an empty bowl and a NO FOOD tag. s155 adds a red arrow up to the counter with STILL 250.
6. **Single-cell run: fixed.** s230 adds the empty bowl. s231 adds the official with a POLICY clipboard.
7. **s192: fixed.** It now shows two horizontal season bars: 1979, and 2015 with a red +3 WEEKS extension, with Doug at the end. It reads in one second.
8. **s210: fixed.** The squares are now labelled J F M A M J J A S O N D with July to December in red, and the 88% headline is kept. It reads as a calendar.
9. **s105: fixed.** The X sits on a water-ripple icon and the bear is unmarked.

### Round 1 polish
10 (s149 and s132 captions), 11 (the s204 silhouette is clear of the "E"), 12 (the paw icon now has a white fill and reads on navy and black; checked on s019, s044, s046 and s219), 13 (s216 uses a single strike line and PEOPLE is readable), 14 (the berry pile is now bright red and blue berries on s178, s180 and s185), 15 (the s104 plate is on the floe) and 16 (s031 has the BLACK SKIN tag) are all done.

### New checks on the re-rendered shots
No new defects. Doug is on-model and readable everywhere. There's no gore. The new props (fish, bowl, official, wind sock, season bars) are recognisable. No run of 4 or more near-identical compositions is left: s228/s229 and s230/s231 are pairs only.

### Thumbnails
All three pass policy. They show no gore or blood: the dark-red open mouths are cartoon mouths. No cubs, no real people, and nothing reads as a kids' show. Each pairs Doug with the bear threat and avoids every title and alt word. None is misleading: bears entering buildings and stalking a distracted person are both in the video.

- **A (thumbnail.png): "DINNER TIME", the strongest. Recommend it as the primary.** One clear focal point: a huge bear's head nose-to-glass at a lit cabin window, with tiny Doug unaware inside holding a FIELD GUIDE. At 168x94 the text, the bear and the warm window all read instantly. The yellow-on-navy contrast is strong. It complements "...That Hunts Doug" without repeating it.
- **B (thumbnail_b.png): "BEHIND YOU", passes.** The upright bear with raised claws looms over Doug, who smiles and looks the other way with binoculars. At feed size the text and the two figures read clearly against the cyan sky.
- **C (thumbnail_c.png): six-tile chapter grid, passes as the test variant.** This is the format's grid archetype. At 168x94 it has no single focal point: the tiles become small swatches, though the labels stay legible. Expect it to lose the A/B test against A. Nothing in it blocks.

### Polish (non-blocking; graphic designer)
17. **Thumbnail A:** the lone lower tooth floats as a white triangle on the white lower jaw, below the red mouth. Move it up so it sits on the red mouth edge and points up, like the upper fangs. That way the jaw reads as one mouth, not a separate lump.
18. **Thumbnail B:** the bear's near hind leg starts mid-belly as a separate rectangle, and the forearm is a flat horizontal tube, so the pose reads a little "man in a bear suit". Join the leg into the body contour and give the forearm a downward droop over Doug's cap. That keeps the menace heavy rather than goofy. Also put the binoculars in Doug's raised hand. Right now they float beside his face.
19. **Thumbnail C:** in the Tent tile, the bear's head poking through the tent reads as a white cone at feed size. Show more head (ear plus eye) or swap in the s173 "nose presses into the tent" framing. The "Tent" label ends at about x=1110, close to the YouTube duration badge. Nudge the bottom row labels up about 10 px.

The keyframes are approved for render. Post-render screening (samples, qc.json, Shorts) is still to do.
