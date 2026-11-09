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
