# Visual review: 022-komodo-can-wait

## Round 3: s184 re-check, thumbnail and s001 (2026-10-18)

Scope: `build/keyframes/s184.png`, `build/thumbnail.png` (1280x720), `build/thumbnail_small.png` (320x180, feed
size), and `build/keyframes/s001.png`. The s001 keyframe on disk was still the 17:36 "(thumbnail pending)"
placeholder because it was rendered before `thumbnail.json` existed. I re-ran
`python -m studio keyframes 022-komodo-can-wait --shots s001`, and it now resolves `scene_ref: thumbnail`
correctly.

**KEYFRAMES VERDICT: PASS**
**THUMBNAIL VERDICT: PASS**

### Keyframes
- s184: FIXED. The "peace?" tail now ends at about y 695, just above the cap of the sitting Doug (the cap starts at
  about y 715). It no longer stops on the horizon, and it clearly comes from Doug. The thermos, basket, blanket and
  sandwiches all read, the dragon on the right is on-model, and the HUD (DEATHS 184, THE WAIT: 5 DAYS) is legible.
- s001: PASS. It is the same picture as the thumbnail, at full resolution, which follows the opening-image
  convention. No text is cropped and Doug is fully in frame.
- Every other shot passed in round 2 and was not changed.

### Thumbnail (archetype C, "IT CAN WAIT")
- Feed size (320x180): "IT CAN WAIT" is the strongest element and is easy to read. The huge dragon head, its orange
  eye and the yellow forked tongue read in under a second. Doug's red cap and white head still stand out at the
  right edge.
- Story: a huge, still predator watches tiny Doug as he strolls away whistling (music note), and the tongue is
  already reaching his ankle. This fits the title "How the Komodo Dragon Kills Doug Without Chasing Him" without
  repeating any title word, and it isn't misleading.
- Brief compliance: the dragon is low and flat, the eye is hard and hooded, and the tongue is out. It has no wings
  or fire and nothing about it is cute. Doug has a white ankle bandage with no red and no wound. There is no gore
  and no kids'-show tone.
- Layout: Doug sits at about x 1140 to 1265 and y 415 to 615 in the 1280x720 version, which keeps him clear of
  YouTube's duration badge in the bottom right (about y 670 or lower). The music note is about 15 px from the right
  edge. That is tight but not cropped.

### Advisories (non-blocking, graphic designer)
- A. At feed size the claws (small white marks at about x 430 to 500, y 615 to 640) vanish, and the front leg
  reads as a featureless lump. The forked tongue alone is what says "lizard". Two or three bold dark claws on that
  foot would make it read more clearly as a Komodo and less like a catfish or seal head.
- B. The white underline under the text adds nothing. You can drop it, or keep it if that is the channel's
  thumbnail grammar.
- C. The ankle bandage can't be seen at 320 px. That's fine because it is a full-size detail.

### Round history
| Round | Scope | Verdict |
|---|---|---|
| 1 | All 24 contact sheets | FAIL (11 fixes) |
| 2 | Re-rendered sheets | FAIL (1 fix: s184 tail) |
| 3 | s184, thumbnail, s001 | Keyframes PASS · Thumbnail PASS |

---

## Round 2: pre-render keyframes (2026-10-18), FAIL (history)

Scope: all 24 re-rendered contact sheets (s001 to s288, all regenerated 17:36) in `build/contact/`. I checked
s035, s120, s140, s162 and s184 at full size in `build/keyframes/` and compared the speech-bubble tails against the
`doug`/`speech` coordinates in `shotlist.json`. s001 is still the "(thumbnail pending)" placeholder, which is
expected at this stage. The thumbnail gets its own check after packaging.

**VERDICT: FAIL** (one small fix left; everything else passes)

### Round 1 fixes re-checked
1. **s187, s188, s189 stray white square: FIXED.** The square is gone from all three. s189 now shows a green
   thermos that matches the s184 picnic, with "NOT FOOD" and an arrow into the dragon's mouth. It reads at once.
2. **s146 blank calendar: FIXED.** The calendar now says "CENTURIES" next to the "A FEW CENTURIES AGO" label. That
   is legible and matches the narration.
3. **s120 to s122 geography: FIXED.** The old island is now a small hill on the far left horizon. Doug, the ring
   and the "DOUG WAS HERE" flag are on the foreground beach, with a palm tree for the new island. The s121 dragon
   and the s122 lying dragon read as "already waiting on the beach". The "safe" tail now ends about 25 px above
   Doug's cap.
4. **s035 tooth vs quarter: FIXED.** The tooth (about 320 px) is clearly shorter than the coin's 380 px diameter.
   Both stand on one baseline, with the "24 MM" span and "(BOTH ENLARGED)" note.
5. **Floating head cut-outs: FIXED.** s055, s057, s061, s062, s066, s076, s077, s123, s127 to s133, s158 to s160
   and s165 now use full-body dragons. s069 and s070 run the head off the left edge. The ridge crowds (s125, s126,
   s139 to s141) put the ground polygon over the heads, so no neck edge shows. s123 is now three full-body dragons
   and no longer reads as a kiss.
6. **s162 missing buffalo: FIXED.** The new `water_buffalo_lying` lies down with its eyes closed and no wounds.
   Three resting dragons wait around it. The joke lands and stays cartoon-clean.
7. **Variety: FIXED.**
   - Ambush: s016 is the top-down trail with the deer and boar, s020 is the tight log close-up, s024 is Doug's face
     with the open field guide, and s025 is the big dragon foreground with tiny Doug reading. The run is broken up.
   - s181 is now the MON to FRI calendar strip with five ticks.
   - s207 is the long path of deer with "100" and the dragon small in the corner. s210 is the half-closed-eye
     close-up with Doug. s212 is the punch-in on the belly under "FULL". The rock run is broken up.
8. **s034 "SERRATED" overlap: FIXED.** The word now sits under the bread knife, clear of the jaw.
9. **s126 stray red arrow: FIXED.** Removed.
10. **s249 "Z Z" read as snoring: FIXED.** It is now two blue X-shaped chromosome glyphs, each labelled Z, with
    "ZZ = ALWAYS MALE" underneath.
11. **Speech-bubble tails: 3 of 4 FIXED.** s140 ("can I help?"), s209 ("hi friend?") and s252 ("hello?") now end
    about 20 to 30 px above Doug's cap, and so does the new s279 ("I can wait too"). **s184 ("peace?") is still
    wrong, see the required fix below.**

### Round 1 advisories
- s153: FIXED. The dragon is separated from the buffalo, with a dust puff at the leg.
- s250, s251: FIXED. Doug is removed. s251 now shows two shark silhouettes with "?". s257 to s259 still show
  swimming Doug, which is fine.
- s092: FIXED. The sitting Doug is replaced with a standing Doug beside the Titanic card and the snack.
- s284: FIXED. The stopwatch is now large and "4,000,000 YEARS" reads easily.
- s276: NOT CHANGED. The two blue squares still don't say "flooded habitat" on their own. This is still advisory
  and does not block.

### General scan for new problems
- Doug is on-model (red cap, white head) in every shot, including the new close-ups (s024, s210) and the night,
  purple and orange bands.
- The HUD is consistent. DOUG DEATHS goes 178 to 186, one step per death: s027, s076, s098, s121, s142, s166,
  s233, s282. THE WAIT only ever goes up. In s223, s225, s226 and s228 the big tree canopy sits behind the chapter
  label and the HUD, and both stay readable.
- There is no gore and no kids'-show tone. The new lying buffalo, the thermos, the shark silhouettes and the
  Megalania silhouettes (s263, s264) are all clean.
- Text is legible and spelled right, nothing is cropped, and nothing overlaps a drawing.
- Advisory only: s159 and s160 ("feeding on them together" and "a meal that can go on for several days") show the
  dragon crowd running off the right edge with no buffalo in frame. It works as an implied off-screen meal. A buffalo
  rump at the right edge would make it explicit.

### Required fix
1. **s184: the "peace?" tail still ends on the horizon line, about 60 px above Doug.** Director. Doug uses the
   `sit` pose (x 900, y 829), so his head is lower than the standing offset you used. The tail ends at
   [910, 654], right on the horizon, and Doug's cap starts at about y 715. Change the speech `tail` to
   `[910, 695]`.

### Routing summary
- Director: fix 1 (s184, one coordinate).
- Illustrator: nothing. `thermos` and `water_buffalo_lying` both read well.
- Art director: nothing blocking.
- Graphic designer: thumbnail still pending, not reviewed yet.

Re-run `python -m studio keyframes 022-komodo-can-wait --shots s184`. Round 3 only needs to confirm s184. Every
other shot passes as rendered.

---

## Round 1: pre-render keyframes (2026-10-18), FAIL (history)

Scope: all 24 contact sheets, with full-size checks of s061, s187 and s232. The required fixes were:
1. s187 to s189: delete the stray white square, and show the thermos in s189 (new `thermos` asset).
2. s146: the calendar is blank. Add "300 YRS" or remove the calendar.
3. s120 to s122: Doug claims the "next island" on his home shore. Reverse the geography and end the "safe" tail at
   Doug.
4. s035: the tooth is drawn bigger than the quarter. Make the tooth clearly smaller than the coin.
5. `komodo_head` cut-outs on open ground read as severed heads (s055, s057, s061, s062, s066, s069, s070, s076,
   s077, s123, s127 to s133, s158 to s160, s165). Use full bodies or hide the neck edge. s123 reads as a kiss.
6. s162: the buffalo is missing. Add a lying buffalo (new `water_buffalo_lying`).
7. Variety: break up s013 to s028, s177 to s181 and s205 to s212.
8. s034: "SERRATED" overlaps the jaw.
9. s126: a stray red arrow points at empty ground.
10. s249: "Z Z" reads as snoring.
11. Speech tails in s140, s184, s209 and s252 stop short of Doug.

Advisories: s153, s250 and s251, s251, s276, s092, s284.
