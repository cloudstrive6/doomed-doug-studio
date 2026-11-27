# Visual review: 060-oarfish-doomsday-fish

## Round 1: pre-render keyframes (contact sheets 01-15, s001-s179 + endslate)

VERDICT: FAIL

Policy and safety checks passed:
- No gore. The autotomy stump (s133-s135) is clean grey with no red. The gut interior (s146-s171) is flat cartoon pink with no blood or organs. All deaths are offscreen or shown as a cap only (s037, s057, s093, s136, s173).
- The oarfish never looks cute. The big-head close-ups (s077-s094, s143-s145) have a flat eye and a neutral mouth, and the full-body drawing reads as an oarfish (red crest, ribbon fins, long silver body).
- Nothing kid-coded.
- Doug stays on-model throughout (red cap, white head). The capless ghost Doug in s174-s179 is intentional because the cap rode the fin.
- The death counter runs 425 to 430 in step with the narration, and the distance HUD is consistent.
- s001 is the expected thumbnail placeholder.

Required fixes:
1. **s004** (director): The narration "Doug is inside one, not alone" plays over Doug on the couch with a black squiggle on the wall, so the picture doesn't match the line and the squiggle is unreadable. Reuse the s154 gut-corridor setup instead: tiny Doug with his torch and two or three tapeworms in the beam, and keep the "NOT ALONE" caption.
2. **s159** (director): The red arrow from "15 CM" points up and right into empty gut wall. Point it at the central worm hanging from the lumen, and draw a 15 cm bracket along that worm.
3. **s072** (director): The red arrow runs through the "P" of "PASSENGER", and the isopod is too small to find in 1 second. End the arrow at the label's left edge, scale the isopod about 2x, and move the zoomed fish body right so it doesn't run under the "THE STANDING FISH" chapter tag (same fix for s073).
4. **s091** (director): The red pelvic fin streamers cross "HURT" in "NO WAY TO HURT". Move the caption up into open water (around y=0.75) or to the left, clear of the fins.
5. **s150-s153 and s157-s160** (director): Variety. These are two runs of 4 identical gut-corridor frames (same camera, Doug at the same spot, torch cone, lumen), and s146-s148 and s162-s171 repeat the same plate. Vary at least one shot in each run:
   - s151: close-up of the worms in the torch beam
   - s152: wide shot with Doug small in the corridor
   - s158: insert of the three worm types side by side with their labels
   - s160: Doug's face reaction close-up
6. **s153** (director): "FURTHER DOWN" sits on Doug's legs. Raise it above the torch cone, or move Doug left.

Advisory (fix if cheap):
7. **s003** (director): The narration says "with Doug attached", but Doug is on the couch. Put Doug holding the dropped tail piece so the teaser reads.
8. **s027** (illustrator): There's an empty stray rectangle in the top-right of the "OLD DRAWING" frame. Remove it, or put a date in it (for example "1772").
9. **s114** (director): The "MOST OF IT" arrow crosses Doug's face. Route it around his head to the fish's tail.
10. **s084** (director): The "NO TEETH" label sits on the fish's belly and fin. Nudge it down or left into open water.
11. **s010-s013** (director): The four quake-chart frames are acceptable as a build, but s012 would hit harder punched in on the single dashed match line.
12. **s172** (director): A near-empty black frame comes right before s173, which is also black. Add Doug's two eyes blinking in the dark so the "torch ran out" beat reads.

## Round 2: recheck of the shots the director changed (s003, s004, s012, s072, s073, s084, s091, s114, s130, s151-s153, s158-s160, s169, s172, s175-s177)

VERDICT: PASS

Each Round 1 item, checked against the new keyframes in build/keyframes/:
1. **s004**: Fixed. Doug is in the gut corridor with his torch, three tapeworms are in the beam, and "NOT ALONE" is clear of everything.
2. **s159**: Fixed. A red bracket runs along the central hanging worm, and the "15 CM" arrow points at it.
3. **s072/s073**: Fixed. The arrow no longer touches "PASSENGER", the isopod is about 2x bigger and easy to find, and the fish body is clear of the chapter tag.
4. **s091**: Fixed. "NO WAY TO HURT" now sits in open water at the bottom left, clear of the fins.
5. **Variety**: Fixed. s151 is a close-up of the worms in the beam, s152 is a wide shot with Doug small, s158 is the three-worm insert with labels, and s160 is a close-up of Doug's face. The longest run of identical gut-corridor frames is now 3 (s146-s148). s162-s171 is broken up by s163/s164 (doors) and s167-s169 (larva to shark).
6. **s153**: Fixed. "FURTHER DOWN" sits above the scene, clear of Doug and the beam.
7. **s003**: Fixed. Doug holds the dropped tail piece while the shortened fish stands upright.
9. **s114**: Fixed. The "MOST OF IT" arrow goes around Doug to the lower body.
10. **s084**: Fixed. "NO TEETH" is in open water, clear of the belly and fins.
11. **s012**: Fixed. The frame is punched in on a single dashed match line with an "A MATCH?" caption.
12. **s172**: Fixed. Two eyes in the dark, so the "torch ran out" beat reads.
- **s169**: A clean larva-to-shark arrow, matches "something bigger to eat it".
- **s175-s177**: Ghost Doug keeps his cap, which follows the art bible rule, so the capless note from Round 1 no longer applies. The cap rides the fin (s175), lies on the seabed (s176), and sits on the RIP DOUG headstone (s177). The counter shows 430 in red.

No gore, nothing kid-coded, and Doug is on-model in every rechecked shot.

Advisory (optional, does not block):
A. **s072** (director): The red arrow now stops about 100 px short of the isopod. Extend the tip to x of about 570 so it touches the animal.
B. **s130** (illustrator, `record_book_open`): The grey bar on the left page doesn't read as anything at frame size. Replace it with a tiny oarfish silhouette, or remove it.
C. **s027** (Round 1 item 8) was not in this recheck set. Confirm the stray rectangle has been removed.

Note: build/contact/ only holds sheet_01 (s160 and s172). The other shots were checked from the individual keyframes and a montage of s144-s174 made for this review.

## Round 3: thumbnails A/B/C (build/thumbnail*.png, *_small.png at 168x94) and s001 recheck

VERDICT: FAIL (variant B only; A and C pass)

**s001**: Confirmed after a re-render. The keyframe on disk was stale: it was rendered at 18:02, before the thumbnails were made at 18:13, and still showed "(thumbnail pending)". I re-ran `python -m studio keyframes 060-oarfish-doomsday-fish --shots s001`, and s001 now shows thumbnail A ("IT LET GO"), matching build/thumbnail.png. The editor must render after the thumbnails exist (they do now).

**A, "IT LET GO"** (title: "Why an 8 Meter Oarfish Can Drop Its Own Tail and Not Die"): PASS. The text is readable at 168x94. There is one focal pair: the upright fish and the dropped piece. Doug is on-model, panicked and readable against the dark blue. The stump is clean and rounded, with no red. There is no gore and nothing kid-coded. The text doesn't repeat the title and pays off "drop its own tail".
 Advisory (graphic designer): (a) The thin tip of the dropped tail ends between Doug's raised hand and his chin, so at feed size it can look like it's poking his mouth. Put the tip clearly in one fist. (b) The fish's rounded stump touches the bottom edge, and a small black spike pokes out below it at x of about 350 (1280 scale). Raise the fish about 30 px so the whole healed stump is inside the frame and the spike is gone.

**B, "NO TEETH"** (title: "Doug Died 5 Times Near an Oarfish That Did Nothing"): FAIL. Fixes, all for the graphic designer:
1. **Kid-show tone.** A smiling, waving Doug, a big round-eyed fish with a pale blush circle on its cheek, and bright sky-blue water add up to the most nursery-looking frame of the three, and nothing in it says "died". Change these:
   - Remove the cheek blush circle at about (590,480).
   - Make the eye blank and dead-looking: no white ring around a centred pupil. Use a flat pale disc with a small off-centre pupil, the same as A and C.
   - Switch the water to the episode's dark blue (#1B4F86 as in A, or darker).
   - Give Doug a nervous or fake grin with a sweat drop instead of the happy smile.
2. **Duration badge.** The "H" of TEETH sits at x 1130-1210, y 590-700, inside YouTube's timestamp-badge zone at the bottom right. Move the text left or up so it ends before x of about 1120 or above y of about 620.
3. **Text on top of the drawing.** "NO TEETH" sits over the fish's lower body, and red fin lines stick out under the "O T", which looks like a glitch at feed size. Put the text in open water at the top centre, or bottom left under the tally, and crop the fins so nothing shows below the text.
4. **Brief match** (optional but recommended). The brief says "Doug waving at arm's length", but he is about 250 px away from the mouth. Move him in to just in front of the mouth so "near an oarfish that did nothing" reads at a glance.

**C, "NEVER GROWS BACK"** (title: "Why the Oarfish Can Cut Off Its Own Body and Not Die"): PASS. The text is readable at feed size, and the healed rounded stump and the dropped piece in Doug's hand are both clear. Bubbles sell the sinking. There is no gore and nothing kid-coded, and the bottom right is clear apart from bubbles.
 Advisory (graphic designer): The brief's "cap floating off" is missing, and Doug looks like he's standing rather than sinking. Tilt him about 15 degrees, or float the cap just above his head. "GROWS BACK" starts about 15 px from the left edge, so give it 30 px or more of margin.

## Round 4: revised thumbnails A/B/C (build/thumbnail*.png, *_small.png at 168x94) and s001 recheck

VERDICT: PASS

**s001**: Re-rendered with `python -m studio keyframes 060-oarfish-doomsday-fish --shots s001`. It now shows the revised thumbnail A and matches build/thumbnail.png.

**A, "IT LET GO"**: PASS. Both Round 3 advisories are fixed. (a) Doug now holds the thin tip of the dropped piece in both fists at arm's length, so nothing reads as touching his mouth. (b) The whole healed stump sits inside the frame (bottom at y of about 520) and the black spike is gone. The tug-and-release story reads at 168x94: upright fish, gap, the dropped piece, a panicked Doug. There is no red on either cut end.
 Advisory (graphic designer, optional): Doug is only about 12 px tall at feed size, smaller than in Round 3. Scale him up about 1.3x if it doesn't crowd the text. A short black dash crosses the head outline above the eye at about (290,48) and looks like a stray stroke; remove it unless it's meant as a brow. In "LET" the outlines of the letters merge, and the G has a black bump inside its bowl. It still reads, but widen the tracking slightly.

**B, "NO TEETH"**: PASS. All Round 3 fixes are in:
1. Kid-show tone: the blush is gone, the water is dark navy, the eye is a pale disc with a small off-centre pupil and a flat mouth, and Doug has a nervous teeth-grimace with a sweat drop. It no longer reads as nursery.
2. The text ends at x of about 700 (top left), so the duration-badge zone is clear of text.
3. The text sits in open water and nothing overlaps it. The tally of five sits below it.
4. Doug is about 150 px from the mouth, which is close enough.
 Advisory (graphic designer, optional): The sweat drop is almost invisible at about (320,510) on the cap edge. Make it larger and lighter, or move it to the side of his head. Two red pelvic-fin lines still poke out under the fish at the bottom edge at x of about 820-860. They're harmless now that the text has moved, but they could be cropped.

**C, "NEVER GROWS BACK"**: PASS. The floating cap is waived (engine limit; cap stays on head). Doug is now tilted and sprawled with bubbles rising, so he reads as sinking. "GROWS BACK" now has about 45 px of left margin. The bottom right is clear.
 Advisory (graphic designer, optional): The dropped piece is much thinner at its cut end (about 25 px) than the fish's stump (about 90 px). Thicken the cut end toward the stump width so it reads as the same body.
