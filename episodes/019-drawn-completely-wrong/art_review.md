# 019 art review: new assets (art director)

Date: 2026-10-15. Scope: all 68 new drawings in `asset_requests.md`. I judged them from the illustrators' previews
(`assets/previews/019-*`) and from my own renders: bbox at scale 1 for every asset against the requested extents, the worn
props on Doug (stand / thumbs_up, scale 1 and 0.4), silhouette + red rim on navy for `therizinosaurus`,
`spinosaurus_mystery` and `elasmosaurus_neck_rising`, and real keyframes s050, s056 and s224.

## Verdict: PASS (after two AD fixes below). Two arrow aims go back to the director. They don't block the asset gate.

All 68 assets are on file. Every bbox matches its request within a few units, and nothing overflows its anchor box.
- **Style:** the two tiers are consistent. Creatures and props are detailed (thick black outline, flat fills, interior shading,
  spray texture). Humans are crude (`victorian_woman` and the dinner guests in `iguanodon_mould_dinner`).
- **`old_*` plates:** the eleven plates form a coherent family: brown ink `#5a3a1e`, parchment fills, cross-hatching, stiff
  engraving posture, no text. Each "wrong part" is obvious: boxy head, `?` body, backwards neck, stilt spines and head blob,
  nose horn, elephant legs, roof tiles and wrist spikes, turtle shell and flipper claws, and the four Spinosaurus postures.
  The pale `#fff8e0` highlight on claws, teeth and spikes is shared by the whole set and reads well on `old_drawing_card`.
- **Gore and kid appeal:** no gore anywhere. The Elasmosaurus mouth, the `hallucigenia_head` throat and the Megalosaurus
  mouth are dark-red interiors, not blood. Nothing is cute or kids-show. The gift-shop toys are clearly toys in context, and
  the Doug family photo is our house crude style.

### Fixes made directly in the library
1. **`iguanodon`: the thumb spike was too small.** The spike was about 44 units long, roughly 25 px in a typical shot. That is
   too small for the shots whose whole beat is the thumb (s050-s056). I scaled the cream cone 1.5x about its tip, so the
   tip stays at (+94,-226) and the base now sits in the hand. The s050 "THUMB" arrow still lands on it (verified in the keyframe).
2. **`therizinosaurus`: the claws read as straws.** The six claw polygons were about 17 units thick, so the "huge scythe
   claws" looked like thin bristles, and the silhouette only gave you thin fingers. I widened every claw blade about 1.7x
   around its centre line. Length, tips and the requested claw position (about (+250,-330)) are unchanged. They now read as
   broad scythes in colour and in silhouette (s224 checked).

### For the director (composition, not blocking)
1. **s178 arrow:** it lands at about (-150,-108) in `hallucigenia_head` space, which is about 40 units below the eyes
   (-150,-150) and (-88,-164). If the line is about the eyes, aim it at about (-120,-160) (screen ≈ (676,408) at x820/y600/scale 1.2).
   If it is about the mouth or teeth, aim it at the right-hand mouth ring or the dashed throat window instead.
2. **s249 arrow:** it lands at about (-160,-60) in `homo_diluvii_slab_exposed` space, about 90 units below the left front leg
   (-150,-150). Re-aim it to about screen (610,430) so it touches the leg and toes.
3. **`hallucigenia` feet offset (illustrator flag):** the legs are not exactly under the spine pairs, and the head-end
   tentacles bunch up. That is fine at the scales used. If a shot puts a label or arrow on "legs", aim it at the middle leg
   pairs (x -120..+60, y +60..+100).

### Notes (approved as drawn, optional polish later)
- `elasmosaurus` / `elasmosaurus_underwater_body`: the tail tapers a little long, but the neck is still clearly the longest
  part, so the real animal reads correctly against `old_elasmosaurus_backwards`.
- `therizinosaurus`: the small triangle "feather tufts" read slightly as thorns. It still reads as shaggy at video scale.
- `big_shield`: oval rather than round, carried beside Doug's body per the requested bbox (x -10..150). Head, cap and
  face stay clear. Approved.
- `fencing_mask`: the mesh pushes slightly forward of the face, like a real mask in profile. Eyes and mouth read through,
  and the cap is untouched (checked on stand and thumbs_up). It is not mirrored for `facing: left`. Keep Doug facing right
  in s055-s058, which is how they are laid out.
- `old_drawing_card`: at 0.14 in Doug's hand, the header is not legible, but the card and drawing read as an "old card".
  This is as intended.

### Per-asset status
| asset | status |
|---|---|
| old_drawing_card | APPROVED |
| gift_shop_shelf | APPROVED |
| old_brontosaurus_boxy | APPROVED |
| old_deinocheirus_arms | APPROVED |
| old_elasmosaurus_backwards | APPROVED |
| old_hallucigenia_1977 | APPROVED |
| old_iguanodon_nosehorn | APPROVED |
| old_megalosaurus_quadruped | APPROVED |
| old_spinosaurus_1915 | APPROVED |
| old_spinosaurus_2014 | APPROVED |
| old_spinosaurus_2020 | APPROVED |
| old_spinosaurus_2022 | APPROVED |
| old_stegosaurus_roof | APPROVED |
| old_therizinosaurus_turtle | APPROVED |
| allosaurus_vertebra | APPROVED |
| apatosaurus_skull | APPROVED (clearly distinct from camarasaurus_skull) |
| camarasaurus_skull | APPROVED |
| big_shield | APPROVED |
| brontosaurus | APPROVED |
| brontosaurus_foot | APPROVED |
| chalkboard | APPROVED |
| classic_museum | APPROVED |
| crystal_palace_iguanodons | APPROVED |
| crystal_palace_megalosaurus | APPROVED |
| deinocheirus | APPROVED |
| deinocheirus_arm_bone | APPROVED |
| deinocheirus_eating | APPROVED |
| dimetrodon | APPROVED |
| dimetrodon_tooth | APPROVED |
| dollar_bill | APPROVED |
| elasmosaurus | APPROVED (note) |
| elasmosaurus_neck_rising | APPROVED (silhouette checked) |
| elasmosaurus_underwater_body | APPROVED (note) |
| family_photo_frame | APPROVED |
| fencing_mask | APPROVED (checked on Doug) |
| fossil_crate | APPROVED |
| giant_salamander | APPROVED |
| gizzard_stones | APPROVED |
| glass_display_case | APPROVED |
| hallucigenia | APPROVED (feet offset: director note 3) |
| hallucigenia_head | APPROVED (s178 arrow: director note 1) |
| homo_diluvii_slab | APPROVED |
| homo_diluvii_slab_exposed | APPROVED (s249 arrow: director note 2) |
| iguanodon | APPROVED (AD fix 1) |
| iguanodon_mould_dinner | APPROVED |
| iguanodon_skeleton | APPROVED |
| iguanodon_teeth | APPROVED |
| iguanodon_thumb_spike | APPROVED |
| iguanodon_thumbs_up | APPROVED |
| journal_paper | APPROVED |
| megalosaurus | APPROVED |
| megalosaurus_bones | APPROVED |
| ping_pong_table | APPROVED (side/length view) |
| ping_pong_table_end | APPROVED (end/width view, clearly different) |
| salamander_outline | APPROVED |
| sauropod_skeleton_headless | APPROVED |
| spinosaurus_mystery | APPROVED (silhouette + rim checked) |
| stegosaurus | APPROVED |
| stegosaurus_fossil_slab | APPROVED |
| stegosaurus_tail_spike | APPROVED |
| synapsid_skull | APPROVED |
| tall_ladder | APPROVED |
| tennis_court_side | APPROVED |
| therizinosaurus | APPROVED (AD fix 2) |
| therizinosaurus_claw | APPROVED |
| us_quarter | APPROVED |
| victorian_woman | APPROVED |
| water_plants_bunch | APPROVED |

68 / 68 APPROVED, 0 REVISE.
