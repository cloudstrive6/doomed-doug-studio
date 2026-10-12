# Art review: 015 The Deeper Doug Digs (assets)

Reviewer: art director · 2026-10-12 · scope: the 48 new assets in `asset_requests.md` and the strata ramp.

## Verdict: PASS. All 48 assets APPROVED (`repenomamus_fight` passed on re-review, see below).

### Re-review 2026-10-12: `repenomamus_fight` v2 APPROVED
Checked `assets/previews/015-fight-v2.png` (side by side with `psittacosaurus` and `repenomamus`) and `015-fight-shot.png`
(s143 layout, x=1000 y=900 scale 1.3, plus small-size inset). Every point of fix 1 is met:
- The Repenomamus lies along the back with its jaws on the ribs at mid-flank (~(+34,-64)), well clear of the dinosaur head.
  The two heads no longer merge.
- The front paw rests on the lower jaw below the eye. The yellow eye stays fully visible.
- The dinosaur head stands apart at the right with the hooked dark beak, cheek horn, yellow eye and quilled tail of
  `psittacosaurus.json`, so it matches s135/s148. It reads as Psittacosaurus, not a seal or dog.
- No red anywhere in the asset (palette is browns, olives, black and white only). The mouths are dark with white teeth.
  The red circles in the shot preview are hold-point check markers, not part of the asset.
- Bbox is now ~610x195 instead of ~560x300. At scale 1.3 to 1.4 with the `bc` anchor at (1000,900) it spans roughly x 600-1400,
  so it stays inside the safe area and the shotlist layout holds. The silhouette also reads at inset size.
Minor note, no action needed: the reaching foreleg is long and straight. It still reads as a limb because the claws sit at its tip.

Checked every preview sheet (`assets/previews/015-*`), the worn-costume, dark-background and silhouette checks, plus my own
1920x1080 re-renders of the riskier assets. They match the detailed tier against crude Doug: 4-6 px outlines, flat fills with
spray shading. Palette is on, silhouettes are bold, the dark-scene assets read on `#0d1b2a` and near-black rock, and nothing is
gory (no wounds, blood, emergence or hatchling bodies). Creatures look like a dangerous documentary cartoon, not cute.
Note: the grid preview tool centres every asset, so tall `bc` assets (camel, giraffe, mud_wave, sue_skull_case) look cropped
on the sheets. That is a preview artefact. The assets are complete.

## Fixes

1. **`repenomamus_fight` (A, illustrator): REWORK. RESOLVED in v2 (see re-review above).** At hero size the pose doesn't read. The mammal's head sits on the
   dinosaur's neck and shoulder, and its paw crosses the Psittacosaurus face, so the two heads merge into one dog-like blob.
   The Psittacosaurus reads as a seal or dog. Redraw it so that:
   - the Repenomamus lies along the dinosaur's back with its **jaws clamped on the ribs at mid-flank**, well clear of the
     dinosaur's head;
   - one front paw reaches forward onto the **lower jaw** without covering the eye;
   - the dinosaur head stands clearly apart at the right with the same parrot beak, cheek horn and tail quills as
     `psittacosaurus.json` so it matches s135/s148;
   - there is no red inside either mouth (s142-s154 is a fight beat and red mouths read as blood at this size).

   Keep the `bc` anchor and the ~560x300 bbox so the shotlist layout holds.

## Fixed by me (no action needed)

2. `messel_snake_slab`: the lizard in the snake's belly read as a fish spine lost among the snake's rib fans. I added a slightly
   lighter stomach patch behind it, scaled the lizard group up to 1.4 and thickened its limbs. It still centres on (+40,+20),
   so existing ring and arrow targets hold.
3. `sue_skull_case`: removed the white eye glint in the orbit, which made the fossil skull look alive, and added a mounting post
   so the skull no longer floats above the plinth.

## Notes for the director

- `sue_jaw` is a true left-side view, so the **snout is at the LEFT** and the holes sit on the back half at the requested points.
  Don't flip it expecting a right-facing snout.
- `fly_pupa` silhouettes, `aspidorhynchus` silhouettes and `nothosaurus` silhouettes read well at the requested scales.
- Worn gear (`fly_pupa_costume`, `vet_coat`, `referee_shirt`, `cloudina_costume`) keeps Doug on-model: head, eyes and red cap
  stay clear, the stethoscope stays below the face and the whistle doesn't touch the eyes.

## Strata ramp: APPROVED with a correction (now in `channel/art_bible.md`)

The requested ramp got lighter partway down. Layer 5 `#8e4a2c` has luminance 91, but layer 6 `#7a6656` (106) and layer 7
`#6b7280` (114) were both brighter. That breaks the channel rule that each step is darker. Corrected values:

| Layer | Was | Now |
|---|---|---|
| 6 | `#7a6656` | `#665244` (86) |
| 7 | `#6b7280` | `#4a505c` (80) |
| 8 | `#4f5560` | `#3f444d` (68) |

Layers 1-5 and 9-11, the boundary clay stripe `#efe6d0`, the grey bands `#5f5f5f`, the green glow `#2f5a3a`, the shaft
interior `#f1e4c6` and the DEPTH meter placement are approved as requested. I swapped the three hexes in `shotlist.json`
directly (they appear only in the strata rects). `validate shotlist` passes, apart from the expected missing thumbnail on s001.
