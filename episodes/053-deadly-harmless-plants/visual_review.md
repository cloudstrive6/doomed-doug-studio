# 053-deadly-harmless-plants: visual review

## Round 2: keyframe fixes, s001, and thumbnails A/B/C (2026-11-20, visual screener)

Scope: I checked these full-size keyframes: s001, s003, s013, s062, s063, s078, s079, s101, s102, s124, s126, s155,
s166, s184 and s190-s192. I checked these at grid size: s015-s018, s035, s036 and s182-s186. I also checked
`build/thumbnail.png`, `thumbnail_b.png` and `thumbnail_c.png` at 1280x720, as 168x94 downscales, and as the
delivered `_small` files.

VERDICT: FAIL

The keyframes are cleared for render. All four required round-1 fixes are in. The only blocker is thumbnail C.

### Round-1 fixes: verified

- **s013: fixed.** The root is labelled `WATER HEMLOCK`. A small `USDA` tag sits above the "=" sign and no longer
  names the root.
- **s062, s063, s078 and s079: fixed.** The shrub bases now sit in the median band. In s063 the red car drives in
  the upper lane, clear of the hedge. In s079 the small car is in the upper lane. It carries the cap on its roof
  (`cap_taken`), and the body in the car has no cap. This follows the art bible's "One cap per frame" rule.
- **s003 and s126: fixed.** The WordArt is now clear of the umbels, so the hemlock and hogweed flower heads read
  whole. In s126 the title crosses the stem only, which is fine.
- **s190-s192: fixed.** The cap lies on the sand under the canopy at about 2x size, and the drips fall towards it.
  It reads instantly. s191 and s192 keep the same cap. The ghost Doug wearing a cap in s192 is allowed by the art
  bible: the ghost cap is death grammar.
- **s001** (the thumbnail A scene, used as the opening image): it pays off the cold open. The banded tree, the rain
  and Doug smiling dry underneath are all clear. Doug is on-model. There is no gore.
- **Polish items that were fixed:** s017 is now a soup-bowl close-up, which breaks the s015-s018 run. s184 is now a
  close-up of the apple bite, which breaks the s182-s186 run. In s101 the stacked helmet is gone and the plate is
  labelled `HONEY`. s102 now reads cleanly. In s166 Doug is clear of the trunk. In s124 the `HIS ARM` label is
  separate from CONTACT. s155 is labelled `HERBARIUM DRAWER`.
- **Gore and tone:** clean. Doug's pink head and body in s183-s186 are flat colour only.

### Required fix

1. **Thumbnail C (`thumbnail_c.png`), graphic designer.** At 168x94 it has three competing subjects: the tall
   plant, the pot with Doug, and the basket. None of them wins. The plant's top umbels are cropped by the top edge.
   Doug is about 10 px tall. The water hemlock root sticks up out of the basket, bunched and pale, and reads as a
   wheat sheaf or a banana bunch, not as a root. The brief's field-guide `EDIBLE? [x] YES` box is missing, so the
   lie that "NOT PARSNIP" answers is not on the image. Make these changes:
   - Remove the full-height plant, or shrink it to under 50% of the frame height with every umbel inside the frame.
   - Scale Doug, the pot and the fire about 1.6x and make them the focal point at left-centre.
   - Show the root the way s013 shows it: the green-banded crown with the tubers hanging down, large in the front
     of the basket or in Doug's hand.
   - Add the open field guide with a big green-ticked `YES`, or drop it and let the root carry the threat. Keep
     `NOT PARSNIP` top-right. It is readable as it is.

### Thumbnails A and B: pass

- **A (`thumbnail.png`, WRONG TREE):** at feed size it has one focal point: the banded tree with Doug under it.
  The text is crisp and the red cap pops. It complements the title without repeating it and is not misleading,
  since the manchineel rain beat is in s182-s186. Nit, non-blocking: Doug's seated legs (two thin horizontal
  lines) read as stray strokes at 168 px. Thicken them or tuck them in.
- **B (`thumbnail_b.png`, JUST RAIN):** it has the strongest contrast of the three. The dark storm, Doug's pink
  head with his scared mouth, and the drops are all obvious. The pink is flat, with no blisters, so it is
  policy-safe. Nit: Doug's torso is lost behind the branch. Only the head and legs read. That is acceptable.
- The `_small` files match the 168x94 downscales.

### Still open from round 1 (not blocking, not re-verified this round)

- **Items 9, 10 and 13.** Item 9 is the cow design switch, s108-s122. Item 10 is the blank honey-jar labels in
  s083, s094 and s194. Item 13 is the grainy glow in s020, s042 and s092. These were not re-checked this round.
- **Item 14: s035 and s036 (director).** The SAFE box still crosses the berry outline. Nudge it about 30 px right.
- **Nit: s079 (director).** The cap on the small car's roof reads as a police light at feed size. Scale it 1.5x so
  it is clearly Doug's cap.

Route: the graphic designer fixes thumbnail C and returns it, with its `_small` version, to me. The keyframes can
go to render now.
