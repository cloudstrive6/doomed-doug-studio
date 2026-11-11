# 044-shoebill-spare-chick: visual review

## Round 1: pre-render keyframes (visual screener, 2026-11-11)

**VERDICT: FAIL**

Screened: `build/contact/sheet_01..17.png` (s001-s195 + endslate), with full-res crops of s002, s165 and s188. s001 says "thumbnail pending"
on purpose, so it is not judged here and must be checked in the post-render round. The keyframes postdate the art director's chick fix
(asset at 17:59, keyframes at 18:04), so the chick below is the fixed version.

What passes: Doug is on-model (red cap, white head) and readable in every shot he appears in, on cream, dusk and night. All the costumes
(lungfish, catfish, lizard, hatchling, tilapia, chick) read with Doug's face clear. The death counter runs 336 to 343 in step with the
deaths (s026, s066, s085, s104/105, s124, s161, s191). No gore: the strikes are collapse plus splash, the swallows have no blood,
siblicide is never shown and "beheaded" (s055) is only a fish in the bill. Nothing looks like a kids' show. The wordart and labels are
spelled right and sit clear of the counter and the chapter tag. The maps (s036, s052, s092-094, s175) and the scale/prey boards read.

### Required fixes

1. **shoebill_chick_big (illustrator), 32 shots incl. s147-s193, s195, and the "A SPARE" payoff s193.** The fixed bill still fails. At
   shot scale it is a dark brown slab standing straight up from the crown, and next to the small dark eye it reads as an ear, a chimney or
   a little hat. It does not read as a beak (full-res s165 and s188 crops: still a lump with something on top). This is the antagonist
   and the title subject, so it must read as a shoebill chick in one second. Change: make the bill **horizontal and big**, a broad
   clog-shaped bill about 45-50% of the head width, pointing sideways (to the right) at eye height. Use a lighter horn-grey fill (about
   `#9a958a`) with a dark outline and a small dark hook at the tip, so it separates from both the grey fluff and the night ground. Put the
   eye just above the base of the bill. Keep it ugly, with no shine. Verify at 0.16, 0.6 and 0.75 on the night `#3b3550` and dusk
   backgrounds, then re-render every chick shot.
2. **s002 (director).** The "UP TO 140 CM" dashed line sits at the head of the comparison figure, and the shoebill's head is clearly
   *below* it. On screen the bird is shorter than the child, which contradicts "stands as tall as a ten-year-old". Scale the
   `shoebill_side` up (or the kid down) so the bird's crown touches the dashed line level with the kid's head. Also add a small
   "10-YEAR-OLD" tag under the capless kid, so viewers do not read him as an off-model Doug in the first 5 seconds.
3. **s165, s166, s176 (director).** "2 CHICKS" (s165) and "the begging of the weaker chick" (s176, "peep peep") play over a nest with one
   chick, a dashed divider and an orange fish. The second chick is never shown, so the labels point at nothing, and the orange fish in
   the empty half reads as the thing being talked about. Keep the no-harm rule but show the subject: put a small, plain grey downy lump
   (shoebill_chick_big at about 0.3 scale, or a half-hatched shell with a grey tuft) in the right half for s165 and s176. The "peep"
   ticks come from it, and the parent's eye stays away from it. s166 can keep "EMPTY" with the lump gone. Remove the orange fish from the
   right half in s164-s177 (keep the two silver fish by the big chick, which is the point: one side gets food).
4. **s041-s047 (director), variety.** Seven near-identical wides in a row: Doug on the log at left, shoebill_statue at right, same
   framing (s041, s042, s043, s044 and s045 are almost pixel-identical). Break the run. s042: tight two-shot or Doug close-up with a blink
   tick. s043: big close-up of the statue's face and stare (about 1.4 scale, cropped at the chest). s044: keep the wide with NOT FOOD.
   s045: Doug close-up, relieved.
5. **s133, s134 (director).** Narration: "After the chicks hatch... cool them down". The frames still show two unhatched eggs. Replace
   the eggs with the chick: shoebill_chick_big at about 0.5 plus the second egg or a small lump (see fix 3) to stay consistent with the
   Family chapters.
6. **s140 (director).** "pours a full bill of swamp water over his head". The water arc loops up and lands on the right-hand egg, not on
   Doug. End the stream on Doug's cap, keeping the parent's head and eye angled at the eggs (screener R2). Swap the grey-green scribble
   cloud above Doug's head (and the same scribbles on the eggs in s143) for blue drip ticks: the current fuzz reads as mould or smoke.
7. **s123 (director).** "So is the shoebill [waiting]" shows **two** shoebills, one standing and one already collapsing onto Doug. The
   double bird is confusing, and the strike lands before the line is about waiting. s123: one shoebill_statue standing behind Doug,
   waiting. Put the collapse into s124 (or keep s124 as the aftermath and accept that the strike happens on the cut).
8. **s079, s080, s081 (director).** The chapter is The Monitor, and the line "the prey is still in the bill" is its "disturbing part".
   The bill holds a catfish. Show a Nile monitor in the bill (nile_monitor asset small, with the body and tail hanging limp from the bill,
   no blood) so the payoff matches the chapter. If the asset cannot be posed in the bill, request a `shoebill_holding_monitor` variant
   from the illustrator.
9. **s103 (director).** "The bird walked away" shows Doug standing on open water to the left of the mat. Put Doug on the low, tilting
   end of the floating_mat (the mat already has a -6 degree rotate), with his feet in the plants, so s104 "The mat kept Doug" follows.
10. **s118 (director).** The threat silhouette over the nest has a **red** speckled halo at night. Over a nest of eggs that reads as blood
    mist. Use the same neutral grey haze as s067 and s106.

### Advisory (fix if cheap)
- **Orange banded fish (art director / illustrator)**, used in s030, s035, s037, s039, s054, s055 and on the nest. It reads as a
  clownfish ("Nemo"), which is wrong for an African swamp and a little kid-coded. A plain silver or olive fish would be better.
- **s097 (director).** The pair of statues overlap into one blob. Space them about 120 px apart.
- **s021, s062 (director).** The field-guide text is unreadable at that scale. Either scale the book up or accept it as a prop, since it
  reads in s058, s059, s180 and s194.
- **s160-s163 and s171-s174 (director).** Both are 4-shot runs of the same nest wide. One close-up in each run (e.g. s163 on the lone
  egg with the cap, s172 on the big chick) would lift the Family chapters.

### Re-screen
After the fixes, re-render the changed shots plus all `shoebill_chick_big` shots, rebuild the contact sheets and send them back for round 2.
