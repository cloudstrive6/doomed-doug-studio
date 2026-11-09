# 042 anaconda-no-venom: visual review, keyframes (round 2, 2026-11-09)

VERDICT: FAIL

Scope: I re-checked all 15 contact sheets, which were re-rendered at 18:34 after commit e2e6f79. 57 shots changed since 380ce76. At full resolution I checked s068, s141 (the label against the moon) and s144 (the title against the moon). s001 is still "(thumbnail pending)" and was skipped as instructed. The shotlist was not edited.

## Round-1 blocking items: status
| # | Shot(s) | Status |
|---|---|---|
| 1 | s027 two anacondas | FIXED. The dark underwater body now runs up into the surfaced snout. The arrow starts beside "SNOUT ONLY". |
| 2 | s081 no rat | FIXED. The rat's head and tail now show out of the boa coil. |
| 3 | s096-s099 hidden rat, slab, overlaps | FIXED. The rat is visible, X eyes are on the s098 close-up and the slab is gone. The s097 "ARTIFICIAL HEART" label is clear of the arrow. The s096 "WHEN TO STOP" is clear of the monitor. |
| 4 | s141, s142 floating leg | FIXED. The leg comes down from the frame top onto the caiman among the lily pads. "UNDER THE PLANTS" is clear of the leg and the moon. |
| 5 | s130/s133/s138/s144/s145 moon behind titles | FIXED. The moon is clear of every title in all five shots. |
| 6 | s109 stray flatline | FIXED. The flatline now sits inside a heart monitor. |
| 7 | s064 X's over text | FIXED. The X's sit beside the labels, and "NO FOLDING FANGS" and "NO POISON" are readable. |
| 8 | s069, s072 severed head | FIXED. The head now rises from a splash at the water line (also in s066/s067/s068). |
| 9 | Variety runs | FIXED. s041-s047 now include a close-up (s043), a 1-13 count strip (s045) and calendars (s046). s096-s099, s103-s106 and s112-s115 now each have 2 or more different compositions. No run of 4 or more near-identical shots remains. |

## Required fixes (blocking)
1. **s068 (director).** The frame reads as two anacondas. The strike head rises from the splash at about (640, 780), while a separate full `green_anaconda` (x 1200, flipped) has its own head under the capybara at about (850, 850). The narration says "while *the rest of the snake* arrives", but the picture shows a second snake with its own head. This is the same defect class as round-1 s027. Fix it in one of two ways:
   - Hide the full body's head: start the body underwater at the splash (a dark-green silhouette trailing right from x 640 to x 1600, like s025/s027), and keep the arrow and "WRAP".
   - Or drop the strike head in this shot, and have the one full body loop around the capybara's legs with its head biting the capybara's rump.

## Should fix (non-blocking)
2. **s066, s067, s069 (director).** The strike head snaps at empty air beside the capybara (about 100 px gap in s067/s069), but "HOLD" / "bites back" implies contact. Move the head right so the jaws overlap the capybara's rear or flank.
3. **s118, s119 (illustrator).** This carries over from round 1 #11. The mouth cutaway still reads as a giant eyeball at first glance. Add nostrils and a jaw gap at one end.
4. **s040 (illustrator).** This carries over from round 1 #18. The breeding-ball silhouette is still a black blob with arms. Use a dark-green silhouette with visible heads.
5. **s042, s166 (director).** This carries over from round 1 #17. The calendar text "DRY SEASON" and "MONTHS" is still small at playback size. Enlarge the calendar or add a label.
6. **s143, s144 (director).** The "CAIMAN" flag text is about 12 px tall and too small to read. Enlarge it to about 28 px, or put it on the flag cloth.
7. **s148, s164 (director, note).** The red "KEPT" highlight is wider than its plank and spills off both sides. That is acceptable as emphasis, but it would be cleaner at the plank's width.
8. **s007 (art director/editor).** This carries over from round 1 #19. The contact-sheet caption shows "Jes s". Confirm that the subtitle font in the final render draws "ú".
9. **s001 (graphic designer).** This must be re-screened once the thumbnail exists.

Re-screen needed after fixes: s068 (and s001 once the thumbnail lands).

# 042 anaconda-no-venom: visual review, keyframes (round 3, 2026-11-09)

VERDICT: PASS (keyframes). s001 has to inherit the thumbnail A fix below.

Scope: I re-checked the contact sheets (re-rendered 18:38). At full resolution I checked s067, s068, s069 and s001. s066 was checked on sheet_06.

## Round-2 items: status
| # | Shot(s) | Status |
|---|---|---|
| 1 | s068 two anacondas | FIXED. There is now one snake. The strike head bites from the splash, and the rest of the body is a dark underwater silhouette trailing right to the bank. The arrow and "WRAP" match "the rest of the snake arrives". |
| 2 | s066/s067/s069 bite gap | FIXED. In s067-s069 the jaws now overlap the capybara's rump. In s066 the strike is at empty water, which is fine for "not what the bite is for". |
| 9 | s001 | The thumbnail has landed, and s001 equals thumbnail A. See thumbnails fix T1. |

## Notes (non-blocking)
- s068 (director): Doug is absent, while he is on the bank in s067 and s069. That is a small continuity blip. Optionally put him back at (1650, 940).
- Round-2 should-fix items 3-8 (s118/s119, s040, s042/s166, s143/s144, s148/s164, s007 "ú") were not re-checked this round and are still open as non-blocking.

# 042 anaconda-no-venom: visual review, thumbnails (round 1, 2026-11-09)

VERDICT: FAIL (thumbnail A only; B and C pass)

All three are 1280x720, and the _small versions are 168x94. The text is readable at feed size on all three. None has gore, blood, a prey lump or a capybara. None has a kids-show tone. Doug is on-model in all three (red cap, white head, stick body).

## Required fixes (blocking)
T1. **thumbnail.png (A) and keyframe s001 (graphic designer).** Doug's `thumbs_up` hand reads as a raised middle finger. A single vertical stroke comes straight up from the centre of a round fist, and the hand is raised to head height facing camera (crop at 1280: hand at about (365, 95-125)). On the watch page and in frame 1 at 1920, viewers and ad-suitability reviewers can read this as an obscene gesture. On the main thumbnail of a channel chasing YPP, that is not worth the risk. Fix it with one of these:
   - change the pose to `point` aimed at "NOT A LOG";
   - or use the `thumbs_up_hand` asset from 001, which has a fist with knuckles and the thumb clearly off to one side;
   - or rotate the arm so the thumb sits at the side of the fist rather than on top.

   Re-render the thumbnail and s001 together.

## Should fix (non-blocking)
T2. **A and C (illustrator/graphic designer).** The surfaced anaconda head (two eye bumps plus an orange mouth line) reads as a frog or turtle at full size. A pointed snout tip, nostril dots and a forked tongue flick would make it a snake without breaking the "two bumps" idea. In A the coil stack still reads as a big spotted snake at 168x94, so this is not blocking there. C depends more on the head, but the title supplies "anaconda".
T3. **C (graphic designer, note).** Doug stands on a thin blue line on the water, so it is unclear what he stands on. That is acceptable in a cartoon, but a raft or ripple ring would read better.
T4. **B (note).** B is the strongest at feed size: one focal point, Doug in a coil plus "IT SQUEEZES", and an X'd bottle that stands for "no venom". The bottle label is blank, but adding "VENOM" would break the brief's no-VENOM-on-image rule, so leave it.

Re-screen needed: thumbnail A and s001 after T1.

# 042 anaconda-no-venom: visual review, thumbnails + s001 (round 4, 2026-11-09)

VERDICT: FAIL (thumbnail C only). Thumbnail A, thumbnail B and keyframe s001 pass.

Scope: build/thumbnail.png, thumbnail_b.png and thumbnail_c.png, all 1280x720 and rendered at 18:42. Their _small versions are 168x94. I also checked build/keyframes/s001.png at 1920x1080. The A head and the C bumps were checked at 3x zoom.

## Round-1 items: status
| # | Item | Status |
|---|---|---|
| T1 | A/s001 thumbs_up read as a middle finger | FIXED. Doug now uses `point`: a straight horizontal arm aimed right at the head and "NOT A LOG", with a smiling, oblivious face. There is no hand shape left to misread. s001 matches A exactly at 1920, and the text is not cropped. |
| T2 | Anaconda head reads as frog/turtle | A: FIXED. The head now has a low wedge with a pointed snout, a nostril dot and a red forked tongue, so it reads as a reptile and a snake. The eye ridge still leans a little crocodile, which is not blocking. C: NOT FIXED and now worse, see C1. |
| T3 | C: Doug stands on a bare line | FIXED. There is now a ripple ring under his feet. |
| T4 | B | Unchanged. PASS. |

## Required fix (blocking)
C1. **thumbnail_c.png (illustrator + graphic designer).** The "two bumps" are two separate round green domes. Each has a large yellow eye, and the two pupils don't match: the left one is a round dot and the right one is a crescent. That reads as a frog, or as googly meme eyes peeking out of the water, not as a snake. Nothing on the image says "snake": there is no snout, no tongue and no pattern, and the only cue is the dim underwater silhouette. At 168x94 the bumps are two small dark-green blobs on a near-black lake, so the threat is barely visible at all. Fix:
   - Use one low, flat, wedge-shaped head breaking the surface, like A's head but mostly submerged. Put two small eye bumps on top of that single head, nostril bumps at the snout tip, and a short red forked tongue flick. Keep only the top third above the waterline.
   - Make both pupils matching vertical slits.
   - Move the head about 120 px closer to Doug and scale it up about 1.3x. Lift the underwater body silhouette a little, or add a few black anaconda spots to it, so the threat holds at feed size.

## Creative-director check: clickability
- **B: strongest.** One focal point, a panicked Doug fully wrapped, and "IT SQUEEZES" paired with an X'd bottle. With the title, that reads as "no venom, it squeezes" in under a second, and the colour pops on yellow. If the A/B/C test lets you choose a lead, B should be the primary.
- **A: clickable.** The dramatic irony works: smiling Doug stands on the snake and points at "NOT A LOG". Orange on teal stands out in a feed. Weak spot: at 168x94 the body is a long spotted hump that could read as a crocodile until you spot the tongue. The title carries "anaconda", so this is acceptable.
- **C: weakest, even after C1.** It is dark, the threat is small, and "TWO BUMPS" means nothing without the picture. Once fixed it is a fine test arm, but it should not be the lead.
- Nothing is misleading against the title, and there is no gore or kids-show tone in any of the three.

Re-screen needed: thumbnail_c.png (+ _small) only.
