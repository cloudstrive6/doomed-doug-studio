# 022 Why the Komodo Dragon Can Kill Doug Without Chasing Him: art review (art director, 2026-10-18)

Scope:
- **Assets:** the 30 new library files from `asset_requests.md`, plus the AD-owned `bandage` gear. I checked them in
  `assets/previews/022-komodo-can-wait-{assets,assets-b,assets-megalania,props,props-onbg,map}.png`. I also ran an AD test render
  of `wait_stopwatch` at 1.0 and 0.16 with a "17 MIN" overlay, `bandage` on stand/walk1/walk2/thumbs_up/on_back on light and night
  ground, and `komodo_young` / `komodo_dragon` / `megalania` side by side on navy.
- **Keyframes:** all 24 contact sheets (s001-s288), plus full-res checks of s010, s029, s049, s096, s122, s165, s209, s277 and s284.
- `validate` is clean apart from the s001 `thumbnail` scene_ref, which the graphic designer still owes.

## Verdict: FAIL
- **Assets:** 28 of 30 approved, plus the bandage gear. 2 go back to the illustrator: `water_buffalo` and `komodo_mouth_teeth`.
- **Keyframes:** FAIL, routed to the director. The style is consistent and Doug is on-model in every frame. Zone colours follow
  the THE WAIT ramp, the counter and meter are legible, and nothing is gory. What fails:
  - disembodied dragon heads placed on open ground (the biggest problem);
  - long runs of the same composition;
  - the three items the director flagged (s120, s146, s187-s189);
  - a handful of placement bugs.

Once the illustrator fixes A1-A2 and the director fixes K1-K12, this becomes PASS. Only the listed shots need a re-review.

## Required fixes: assets (illustrator)
**A1. `water_buffalo`: the horns don't read as horns.** At scene scale (0.9) the horn is one black ridged slab lying back over
the poll, with a second fragment behind it. In every Buffalo shot (s144-s167) it reads as a black mohawk or wig.

Redraw both horns as **wide, swept-back crescents**:
- They come out sideways from the top of the skull, sweep back and slightly up, and taper to clear points.
- Near horn: about 260 units long. Colour slate `#3a3a3a`, with 5-6 lighter `#6a6a6a` transverse ridge lines.
- Far horn: shows as a second crescent behind the head, one shade darker.
- Leave clear sky between the horn curve and the back so the crescent silhouette reads.

Keep the body, legs, anchor, bbox height (it may grow to about y -480) and the calm half-lidded eye exactly as they are.
Re-preview at 0.9 and 0.45 on `#ecc27a` / `#c9a24a`.

**A2. `komodo_mouth_teeth`: hard vertical cut at the left edge.** Wherever the left edge isn't bled off-frame, the straight cut
reads as a **severed head**: s029 and s040 on the savanna, and s033 and s034 on the card. Give it the same soft, darker scaly
neck fade as `komodo_head`: extend about 80 units left and fade into a darker spray edge, so no straight cut line ever shows.

Keep the jaws, teeth, gum, `#7a0d0d` interior and the eye as they are. The interior stays within the house rule, so no colour
change. Re-preview on white and on `#e4f3fb`.

## Assets: verdicts
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `wait_stopwatch` | APPROVE | Bold crown and side button. At 0.16 it reads as a stopwatch, including on night navy. The face fits "17 MIN" / "4,000,000 YR". |
| 2 | `komodo_log` | APPROVE | Flat, closed lid, dusty back. Passes for a log at a glance, which is the gag. |
| 3 | `komodo_log_eye` | APPROVE | Same geometry. The single amber eye under a heavy brow swaps seamlessly (s024 to s025). |
| 4 | `komodo_head` | APPROVE | Hard eye, wide-forked yellow tongue, soft neck fade. Works over ridges, round the boulder and on close-up cards. Misused on open ground (see K1). |
| 5 | `komodo_mouth_teeth` | **FIX A2** | Teeth, serration and gum are good. The left cut is the problem. |
| 6 | `komodo_tooth` | APPROVE | Orange iron edge and tip read instantly (s038-s039). No red. |
| 7 | `komodo_skull` | APPROVE | Light and long, and clearly different from the croc. |
| 8 | `crocodile_skull` | APPROVE | Deep heavy jaw and conical teeth. The 6.5x arrow pair reads. |
| 9 | `komodo_swim` | APPROVE | Head up with a low back line and a wake. Holds on `#3a9ad9`. |
| 10 | `komodo_rearing_pair` | APPROVE | Reads as two grappling dragons at s138 scale. Nitpick, not blocking: the right head sits higher where the spec asked for the left. |
| 11 | `komodo_bloated` | APPROVE | Sagging belly and a half lid that looks hard, not sleepy. No prey shapes inside. |
| 12 | `komodo_young` | APPROVE | Lean, wiry, banded, narrow eye, never cute. Holds at 0.25 and rotated on the trunk. |
| 13 | `megalania` | APPROVE | About 1.8x the Komodo and bulkier. Reads as a monitor, not a dinosaur. SIL-safe. |
| 14 | `megalania_grey` | APPROVE | Same geometry. Reads as "gone". |
| 15 | `water_buffalo` | **FIX A1** | Body and face are good. Horns are the problem. |
| 16 | `wild_boar` | APPROVE | Bristle crest, tusks, snout. |
| 17 | `smilodon` | APPROVE | Sabres clear past the jaw and it faces the shark. |
| 18 | `nest_mound` | APPROVE | Also works empty as the decoy. |
| 19 | `komodo_eggs` | APPROVE | Leathery, matte, elongated. |
| 20 | `komodo_eggs_hatching` | APPROVE | Same banded young design. Nothing cute. |
| 21 | `placard` | APPROVE | The blank card works. The s164-s165 placement is wrong (K10). |
| 22 | `signboard` | APPROVE | |
| 23 | `big_water_bottle` | APPROVE | Fifteen in a row read cleanly (s175). |
| 24 | `stick_cyclist` | APPROVE | Crude tier with `auto_ink` and no cap, so it isn't Doug. |
| 25 | `picnic_basket` | APPROVE | |
| 26 | `flower_bouquet` | APPROVE | The ribbon is red but small and reads as a ribbon. |
| 27 | `boulder` | APPROVE | No face shapes. The flat top holds the cap (s076). |
| 28 | `flat_rock` | APPROVE | |
| 29 | `komodo_np_map` | APPROVE | The s007 rings land on Komodo, Rinca and west Flores, and all ten s106 dots are on land. |
| 30 | `bread_knife` | APPROVE | |
| G | `bandage` gear (AD) | APPROVE | Verified on stand/walk/thumbs_up/on_back, day and night. White with a grey outline, never red. It is small at Doug scale 0.45-0.5 by design, so the reveal shot has to frame it (K5). |

## Required fixes: keyframes (director)
**K1. Floating dragon heads on open ground** (the biggest problem). `komodo_head` was specified for ridges, the boulder and
close-up cards. Placed on bare savanna, its neck fade ends in mid-air and the frame reads as severed heads lying in the grass.
That is a gore-adjacent read. Shots:
- s055, s057, s061, s062, s066, s069, s070
- s123, s127, s128
- s129, s130, s132, s133
- s158, s159, s160
- s165

Fix each one with one of these:
- (a) Swap to full-body `komodo_dragon` at the same x and facing. Scale about 0.35-0.45 for the crowd stacks, 0.55-0.7 for singles.
- (b) Put the head behind cover: add a foreground grass or ridge `poly`, drawn after the heads, that covers the neck ends, like
  s125/s126/s139-s141, which are correct.
- (c) Bleed the neck end off the frame edge.

For the "crowd around an off-frame meal" stacks (s129-s133, s158-s160), (a) or (b) both work. Keep the meal off-frame either way.
These shots are fine and stay as they are:
- s053, s058-s060, s063-s065 (close-up cards);
- s076-s077 (round the boulder);
- s125, s126, s139-s141, s143 (over the ridge).

**K2. `komodo_mouth_teeth` sitting on the savanna (s029, s040).** Even after A2 it reads as a head lying on the ground. Make
s029 and s040 close-up inserts on a plain `#e4f3fb` card like s033, or bleed the head off the left frame edge at scale 1.0+.

**K3. Same composition many times in a row** (style bible: no five-in-a-row). Keep the narration and elements, but vary the
camera or layout. Change at least one shot in every three:
- **s008-s012** (charging dragon left, Doug right, five shots): make s010 a zoom on the dragon and dust with the label, and s012
  a wide that shows the dust trail stopping.
- **s013-s028** (log centre-right, Doug left; 16 shots apart from s022): add a tight close-up on the log's head at s020
  ("perfectly quiet") and at s025 (the eye opens; use `camera` zoom_in toward the eye). Use a low wide with Doug tiny at s023.
- **s177-s181** (bloated on the rock, five shots): zoom on the half-lid at s178 and on the sun/rock at s179.
- **s205-s212** (bloated on the rock, eight shots in a row): stage s207 ("a hundred easy chances") as a high wide with the
  line of deer filling the frame and the rock small. Make s210 a tight close-up of the unmoved half-lidded head next to Doug's
  waving hand. Make s212 a medium two-shot from the other side (flip).
- **s222-s234** (the same tree, 13 shots): make s223 and s228 close-ups up the trunk (canopy and climbing young only). Shoot
  s225-s227 low on the adult at the trunk base. Shoot s232 up in the canopy (branch, young dragon, Doug clinging).

**K4. s120-s122: Doug lands on the shore he started from (director flag, confirmed).** In s103/s116 he sets off from the
bottom beach toward the far island (top right), but s120-s122 put him back on the bottom beach under the same far hill. Re-stage
s120-s122 as the new island:
- Drop the far hill, or put a small hill at far LEFT for the island he left.
- Add a landmark on the new beach (`palm_tree`) so it's visibly a different shore.
- Beach the ring at the waterline next to him instead of floating mid-strait.

In all Swim shots, darken the beach to the Days ground `#c9a24a` (it is currently `#e8c07a`, almost the same as the `#ecc27a`
sky), so shore and sky separate.

**K5. s049 bandage reveal: the bandage isn't readable, and the arrow points at the wrong leg.** At scale 0.45 the wrap is about
10 px of white on pale sand. Push in (`camera` zoom_in to about 1.6 on Doug's feet, or Doug scale at least 0.9). Aim the red arrow
at the **front** ankle (the bandaged leg, at foot y = hip + 152 x scale). It currently points at the back leg.

**K6. s146 calendar has no text (director flag, confirmed).** A blank calendar reads as an unfinished frame. Either print
"CENTURIES" on the page in the s193 "WEEKS" style (size it to fit inside the page), or drop the calendar. Facts.md has no
specific year, so don't print one.

**K7. s187-s189 unexplained white square (director flag, confirmed).** The `rect` at (764, 830, 46x40) floats at Doug's
shoulder and reads as a render glitch. Remove it from all three shots. If it was meant to be something (napkin, thermos lid),
use a real asset or drop it.

**K8. Speech-bubble tails stop short of Doug.** In s120, s140, s184, s209, s252 and s279, each tail ends on the horizon,
about 50-150 px above his head, so the line floats. Set `tail` to about (doug.x + 20, hip y - 150 x scale - 60), just above the
cap.

**K9. s280 breaks the night boss.** The boss runs on the night palette (`#1b2f5a` / `#2b3d33`), but s280 jumps to the Weeks
orange with a sun between two night shots. Keep s280 night. The "9 HOURS" label (s282) already carries the time passing. If you
want a day-to-night time-lapse instead, log it in `decisions.md` and use the Hours sky `#a9cfe4` / `#d8bd6e`, not Weeks.

**K10. s164-s165 placard across Doug's face.** The stick crosses his cap brim and face, the card sits on top of the cap, and
neither hand holds the stick (art bible: props never over the face). Anchor the placard grip (0,0) at Doug's raised hand point.
Use `point` or `thumbs_up` (hand at local +112, -156 x scale), so the stick runs beside his head and the card clears the cap by
about 30 px. Same in s166-s167, where it already lies on the ground, so no change there.

**K11. s035 contradicts the line.** The narration says "shorter than a quarter is wide", but the enlarged tooth is about twice
the coin's height. Either scale the tooth so its length is just under the coin diameter, with both enlarged together, or label
the tooth "ENLARGED" and draw a 2 cm vs. 24 mm dotted bracket.

**K12. s263-s264 silhouette glow is too faint.** The red spray on `#2b3d33` barely shows at phone size, so the black Megalania
silhouette disappears into the night ground. Add `"rim": {"color": "#e0201b", "px": 4}` to the silhouette and raise `glow_r`
to about 1200 (the illustrator's note).

## Advisory (not blocking)
- s047: put the red X on top of "HOLD", not below it.
- s084: add a "70%" label on the red slice to match "about seventy percent".
- s122: the cap sits on a red stripe of the ring. Move it onto a white segment for contrast.
- s249: the two big blue "Z"s can read as "sleep". Prefer a single label "ZZ = ALWAYS MALE".
- s284: "4,000,000 YR" on the 0.32 stopwatch is tiny. Raise the font to fill the face (half-width up to about 85 local units).
- s096-s097: Doug's sitting legs merge into the log's top outline. Raising the hip about 10 px shows the thighs.
- s001: thumbnail still pending (graphic designer).

## Checked and fine
- Doug is on-model in every frame: cap always visible, including on the ghost and on every death beat. Deaths:
  - 179: cap in the air, then on the ground (s027-s028);
  - 180: on the boulder;
  - 181: on the log;
  - 182: in the ring;
  - 183: by the plate;
  - 184: by the placard;
  - 185: on the branch;
  - 186: on the chair, then the gravestone.
- The counter ticks 178 to 186 correctly.
- THE WAIT meter stays monotonic and legible at 1080p. The background ramp falls band by band:
  - Seconds: `#8fd3ff`;
  - Hours: `#a9cfe4`;
  - Days: `#ecc27a`;
  - Weeks: `#f2a24a`;
  - Months: `#e0844a`;
  - Years: `#8a6a8a`;
  - Night boss: `#1b2f5a`.
- The Swim water is `#3a9ad9`, and Doug auto-inks correctly at night.
- The caption bar is present on every segment frame. Section-header cards follow the house pattern.
- No gore: no carcasses, no feeding on screen, the mouth interior is within the house rule, and the human-attack card (s094) is
  sober.
