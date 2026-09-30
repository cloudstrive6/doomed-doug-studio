# The Paint Explainer: Style Bible (reverse-engineered for Doomed Doug)

Compiled 2026-09-29 from a full scrape of @ThePaintExplainer: 166 long-form videos, 2.0M subs, 318M total long-form views,
first upload 2023-11-26. Sources: watch-page metadata for all 166 videos; 34 thumbnails; YouTube storyboard sprites for 9 videos;
full-length auto-captions for 11 videos; competitor scrapes of Mr. Science (@mr.scienceYT) and Paintify (@Paintify7).
Raw data is in the session scratchpad, `pe/` (meta.json, title_stats.txt, thumbs/, sb/, tx/).

**Scope:** We copy his *techniques* (structure, pacing, packaging, visual grammar). We never copy his titles, drawings,
item lists or wording. The quoted fragments below are only a few words each and exist only to show a pattern.

Confidence tags: **[H]** measured from data, **[M]** inferred from several samples, **[L]** a guess or a single sample.

---

## 0. The format on one page

1. **The package does the hooking and the video delivers at once.** 9 of 11 transcripts start with item #1's *name* at 0:00.
   There is no channel intro, no "in this video", and no request to subscribe up front. [H]
2. **A list of 6 to 25 self-contained items**, each opened by its name as a one-line sentence. The same name sits in a
   caption bar at the top of the screen and in a YouTube chapter. [H]
3. **Each item is a mini-story:** name, frame, mechanism, twist beat, stark kicker. Then a hard cut to the next name. [H]
4. **Items escalate along a physical or severity axis** (depth, era, distance from the sun, least to most painful).
   The biggest or most famous item goes last. [H]
5. **Dry, fast AI narration** at about 195 WPM. Humor is rare and deadpan. [H]
6. **The visuals are MS Paint stick men with meme faces** reacting to detailed cartoon creatures, plus real photos as evidence.
   The image changes every few seconds. [H]
7. **The ending is a one-line Discord CTA.** No summary and no subscribe pitch (older videos had one short subscribe line). [H]
8. **The thumbnail is a labeled grid (a "table of contents")** or one gory hero close-up. It never shows a stick man as the
   hero and almost never repeats the title. [H]

---

## 1. Titles

### 1.1 Dataset facts [H]
- 166 videos. Median views **1.20M**, mean 1.92M.
- Title length: median **45 characters** (range 25 to 86) and **7 words**. Median for the last 40 uploads is 48.5 characters.
  The 25 biggest outliers have a median of 47 characters and 8 words.
- **All 166 titles are in Title Case.** 1 colon, 7 commas, 1 question mark, 19 parentheses (almost all "(Pt. 2)").
- 74 titles contain a digit, and 54 of those are the "in N Minutes" suffix. Numbers as list counts ("The 8 Ways...")
  appear only 3 times.
- ALL-CAPS emphasis words appear 5 times (for example "DISTURBING BANNED") and **underperform** (median 650K against 1.21M).
- No tags or keywords on any video. No hashtags in any title.

### 1.2 How performance was measured
Raw median views are skewed by age: 2023-24 videos had years to grow, and the channel's views are falling
(2026 H2 median is 330K). So each video is scored by its **outlier ratio**: its views divided by the median of the
5 uploads before it and the 5 after it. A ratio of 1.0 is normal for the channel at that point in time.

### 1.3 Title templates, ranked by median outlier ratio

| Rank | Template (skeleton) | n | Median ratio | Median views | Examples (his, for pattern only) |
|---|---|---|---|---|---|
| 1 | **What [Dying / X] [on / in] Every [Set] Would Be Like** and **What If [scenario]** | 3 | **2.63x** | 3.36M | "What Dying on Every Planet Would Be Like" (12.7M, the channel's top video); "What If a Single Modern Marine Platoon Fought An Entire Roman Legion" (3.36M) |
| 2 | **How Every [Category of Person/Thing] Died** | 6 (5 non-sequels) | **2.62x** | 2.07M (non-sequel) | "How Every Cartel Boss Died" (5.8M, 12.6x, the biggest outlier); "How Every Major Dictator Died" (4.3M) |
| 3 | **The [Creepiest / Most Disturbing] [X] That/We [Revelation]**: "...That Turned Out to Be True", "...That Were Finally Solved", "...We Can't Find An Explanation For", "...That Can't Be Explained" | 22 with a revelation clause | **1.84x** | 1.43M | "The Scariest Urban Legends That Turned Out to Be True" (8.8M); "The Most Disturbing Scientific Anomalies We Can't Find An Explanation For (Pt. 2)" (4.7M, 5.6x) |
| 4 | **The Worst [X] Deaths [Ever / of All Time]** | 22 with "Worst" | **1.69x** | 2.13M | "The Worst Cave Deaths Ever" (6.9M, 9.8x); "The Worst Zoo Deaths Ever" (3.7M) |
| 5 | **The Most Disturbing [Science Category] (Ever Found / in [Place])** | 16 with "Disturbing" | 1.3 to 5.3x in the science cluster | 1.32M | "The Most Disturbing Planets Ever Found" (5.3x); "The Most Disturbing Creatures in Each Ocean Layer" (4.5x); "...Events in Space" (3.3x) |
| 6 | **Every [X] Explained in [N] Minutes** | 50 | 1.04x | 1.76M | The 2023-24 format ("Every Paradox in 8 Minutes", 6.5M). It has since been dropped: 2 uses in 2026. |
| 7 | **The Most [Adjective] [X] (on Earth / in History)** (generic "Most") | 31 | 1.00x | 838K | "The Most Guarded Places on Earth You Can't Visit" (7.0x, recent) |
| 8 | **[Plural noun phrase] That/Who [Y]** (no "The", "Every" or superlative) | 10 | 0.79x | 384K | "Products That Got Discontinued For Solving The Problem" |
| 9 | **Every [X] That [Y]** (no "in N Minutes") | 16 | 0.73x | 753K | "Every Extinct Animal That Might Still Be Alive" |
| 10 | **The Craziest / Weirdest / Silliest [X]** | 13 | **0.16 to 0.46x** | 650K | "Craziest" is the weakest high-use adjective. |

Other signals (median outlier ratio):
- **Topic cluster** (the most important signal for us): science, nature, places and body videos score **1.48x** (n=48).
  Death, crime and dark topics score 0.99x, concepts and psychology 0.80x, and history, war and politics 0.62x.
  **Our lane is his best lane.**
- Titles containing "you" or "your": 1.36x (n=8). Titles containing "death", "died", "dying" or "kill": 1.27x (n=31).
- 12 or more words: 1.88x (n=9, mostly long revelation titles). 6-8 words: 0.90x. 5 or fewer: 0.86x.
- Generic suffix "Ever / of All Time / in History" on its own: 0.59x (n=37). Only use it with a strong noun ("Cave Deaths").
- Sequels "(Pt. 2)", "(Pt. 3)": 1.06x relative to their neighbors, but absolute views usually fall a lot compared with Pt. 1.
  Typical drops are 40-80% (for example 4.3M to 975K, and 3.7M to 2.2M). The one exception rose 72%
  (scientific anomalies, 2.7M to 4.7M). His sequels mostly follow strong Pt. 1 videos.
- Durations: 16+ minutes 1.25x, 13-16 minutes 1.17x, 10-13 minutes 0.89x, 6-10 minutes 0.65x.

### 1.4 Title rules derived from his data
- 38-65 characters, 6-11 words, Title Case (small words like "of", "the", "to", "in" may stay lower-case), no emojis,
  no ALL CAPS, no clickbait punctuation ("!!!", "?!").
- One **dread adjective** from the proven set: Most Disturbing, Worst, Creepiest, Scariest, Deadliest, Most Terrifying.
  Avoid "Craziest", "Weirdest", "Silliest" and "Insane".
- One **completeness/scope device**: "Every", "Each", "From Every [Period]", "in Every [Layer]". This makes the grid
  thumbnail and the list format feel complete.
- Prefer a **death or experience frame** ("What Dying in X Would Be Like", "How Every X Died") or a
  **revelation clause** ("...That Turned Out to Be Real", "...Scientists Still Can't Explain").
- Numbers: do not use "in N Minutes" (worn out). Do not lead with a list count. Numbers are fine inside a
  scale claim (depth, years).
- A "(Pt. 2)" sequel is allowed only when Pt. 1 has at least a 2x outlier ratio after 28 days. The sequel title must be
  identical to Pt. 1 plus " (Pt. 2)".
- The title and the thumbnail must not repeat each other: the title gives the frame, the thumbnail gives the items.

---

## 2. Thumbnails

He uses four thumbnail archetypes. Share by era: 2023-24 is mostly archetype D, and 2025-26 is mostly archetype A with some B and C.

### A. Labeled tile grid (the default; about 70% of the 2025-26 sample) [H for the grammar, M for the share]
- **Canvas:** plain white background (#FFFFFF), no title text, no logo, no border.
- **Tiles:** 6 to 16 tiles in a strict grid (2x3, 3x3, 3x4 or 4x3). Each tile is a rounded-corner rectangle with a
  **thick black outline** (about 6 px at 1280x720). The gap between tiles is about the outline width.
- **Labels:** one label under each tile, in bold, black, rounded "comic" handwriting-style type (Comic Sans Bold look),
  Title Case, 1 to 4 words, centered, with no outline or shadow. The labels are the chapter names.
- **Tile content:**
  - For science, nature and myth topics: custom **cartoon illustrations** on a **saturated flat or sunburst background**
    (magenta, cyan, lemon, red, lime, royal blue), with one subject per tile, often a monster face or a meme-face stick head.
  - For history, crime and places topics: **real photos** with the same black frame.
- **Reading effect:** the thumbnail works as a visual table of contents. The viewer reads 6-16 intriguing labels. The
  title supplies the frame ("Most Disturbing ..."), and the labels create curiosity gaps ("Tully Monster", "Zombie Worms").

### B. Tiered pyramid / "iceberg" (his most-watched grid variant) [H]
- A triangle split into 5 to 12 horizontal color bands. Each band holds tiny creatures or scenes.
- Labels sit **outside** the triangle, alternating left and right, in the same bold comic font.
- This is used when the list has a natural vertical axis: levels of hell (7.2M), ocean layers (1.8M, 4.5x),
  geologic periods. **This is the ideal archetype for "every layer of the ocean".**

### C. Hero horror close-up (his biggest outliers: 12.7M, 6.9M, 6.5M, 5.8M) [H]
- One or two **highly detailed cartoon humans** (not stick men) in a state of body horror: frozen face, cracked
  helmet, skull showing through, a miner trapped as water rises.
- **Big text, 1-3 words:** either the item names in heavy black sans caps above each head (two-subject version,
  for example two planet names), or a stakes phrase in white bold sans with an underline on a flat earth-tone field
  (for example a "stuck for N days" style line).
- Flat single-color background (tan, white). The composition fills the frame.

### D. Icon badge grid (2023-24 "Every X Explained" era) [H]
- 12-15 colored circles (one saturated color each) holding a white pictogram, with a bold comic label below.
  Countryball variants were used for politics.

### Grammar shared by all archetypes [H]
- **No face-cam, no red arrows, no circles** on the thumbnail. (Arrows and circles appear *inside* the videos.)
- Maximum 3 font families. Text is black on white, or white on a flat color.
- The **MS Paint stick man is almost never on the thumbnail.** When a stick head appears, it is one tile among many
  (for example the prehistoric-era grid). The thumbnail sells the *subject*, not the mascot.
- Visible MS Paint artifacts are **not** used on thumbnails. Thumbnails are clean, high-contrast and redrawn at high
  resolution. The "paint" look lives in the video body.

### Title and thumbnail complementarity [H]
- Title = the frame plus the dread adjective. Thumbnail = the list items (grid) or the single worst moment (hero).
- Neither repeats the other. A grid thumbnail pairs with "Every / Most Disturbing X" titles. A hero thumbnail pairs with
  "What Dying on..." and "How Every X Died" titles.

### Competitor cross-check
- Paintify (@Paintify7, launched Nov 2025, 20K subs, 5.6M views) copies archetype A exactly (photo tiles, black
  frames, bold comic labels) and reached 1.5M views on its 10th video.
- Mr. Science (254K subs) uses a completely different look: a photoreal cinematic hero subject, a diver or human for
  scale, and 2-4 words of text with one red accent word. Both approaches work in our niche.

---

## 3. Scripts

### 3.1 Measured narration stats (11 videos, full-length auto-captions) [H]

| Video | Format | Minutes | Words | WPM | Words/sentence | Flesch | "you" count | [music] tags |
|---|---|---|---|---|---|---|---|---|
| Creatures in Each Ocean Layer | list, 25 items | 15.3 | 2,945 | 192 | 17.2 | 61.7 (grade 8.9) | low | 17+ |
| Disturbing Events in the Deep Ocean | narrative, 10 items | 14.5 | 2,808 | 194 | 16.1 | 62.2 | 11 | 21 |
| Disturbing Planets Ever Found | list-narrative, 12 items | 15.2 | 3,049 | 200 | 17.0 | 69.0 | 21 | 19 |
| Scientific Anomalies (Pt. 2) | list-narrative | 15.5 | 2,822 | 182 | 15.9 | 53.5 | 5 | 25 |
| Paleontological Discoveries | list-narrative | 14.0 | 2,770 | 197 | 17.9 | 62.3 | 11 | 19 |
| How You'd Die in Every Prehistoric Era | 2nd-person POV | 14.4 | 3,115 | 217 | 17.9 | 72.6 | **240** | 20 |
| Ancient Folklore That Turned Out True | narrative, 6 items | 12.0 | 2,558 | 213 | 19.8 | 68.5 | 4 | 17 |
| How Every Cartel Boss Died | narrative | 14.9 | 2,806 | 188 | 17.8 | 59.3 | 2 | 0 |
| What Dying on Every Planet Would Be Like | 2nd-person hypothetical | 8.2 | 1,580 | 192 | n/a* | n/a* | 61 | 0 |
| Worst Cave Deaths of All Time | narrative | 16.2 | 3,460 | 214 | n/a* | n/a* | 5 | 0 |
| Worst Punishments in History | ranked list | 12.7 | 2,657 | 209 | n/a* | n/a* | 1 | 0 |

\*Older captions have no punctuation, so sentence stats are invalid for those rows.

**Targets for us:** 190-205 WPM (median 197). About 17 words per sentence, but mix 5-word punches with 25-word
mechanism sentences. Flesch 60-70 (US grade 8-9). About 2,800-3,300 words for 15-17 minutes.

### 3.2 (a) The first 30-60 seconds

**Structure A, "Zero intro" (9 of 11 videos) [H]**
- 0:00: the **item name as a standalone sentence**, for example "[Name]." That is the whole intro.
- Within 1-2 sentences comes one of three **frame lines**:
  1. **Superlative claim:** "This might be the most [horrifying] [X] in the [ocean]."
  2. **Sensory POV:** "If you were standing on [X], you would witness something that seems impossible."
  3. **Cold fact with a body count or date:** "[Date], [N] people suddenly died in [place]."
- Then the mechanism starts immediately. The first twist beat usually lands by **0:20-0:40**.
- He front-loads a **strong item first** (a cold open): the folklore video opens with its deadliest case even though the
  description lists it second. He does *not* save everything for the end.

**Structure B, "One-line route promise" (1 of 11: Ocean Layers) [H]**
- One sentence of about 12-25 words, lasting about 6 seconds. It announces the path and a promise, for example
  "start in [shallow] and work our way toward the [monsters] ... because some are [crazy]". Item 1 starts by 0:06.

**What he never does [H]:** no "Hey guys", no channel name, no ask to like or subscribe, no "before we start",
no summary of the whole list, and no fake teaser montage.

**Mr. Science contrast [H]:** about 40 seconds of poetic cold open over music ("a world we were never meant to see"
style), 122 WPM, and a "we" voice. It is slower and more reverent. Borrow its **stakes line** idea but keep PE's speed.

### 3.3 (b) Segment structure for each item [H]

| Beat | Words | Function | His typical moves |
|---|---|---|---|
| 1. Name | 1-5 | Chapter marker. Identical to the caption bar and the chapter title. | "[Name]." |
| 2. Frame | 15-35 | Sets expectation, often a false comfort. | "At first glance, X looks [beautiful / normal]. However..."; "Most [X] are [Y]. But..."; "This creature is also known as [nickname], and you'll soon understand why." |
| 3. Mechanism | 60-180 (list) or 150-350 (narrative) | Concrete sequence of events with physical verbs. | "It enters... It then... Once... Then..." Plus one **scale analogy** ("the size of a dinner plate", "an elephant balanced on a coin", "100 times taller than Everest"). |
| 4. Twist beat | 25-60 | The escalation inside the item, flagged by a marker phrase. | "The insane part is...", "Here comes the crazy part, though.", "The most disturbing part is...", "However, we haven't talked about the most disturbing thing yet." |
| 5. Kicker | 8-25 | Stark closing line, then a hard cut. | A deadpan fact, an unresolved mystery ("was never officially determined"), or a grim outcome stated flatly. |

- **Item length:** list format has a median of about 35 seconds (about 115 words) per item. The 2025-26 list-narrative
  format has a median of 78-88 seconds (about 250-290 words).
- **Items per video:** 2023-24 median 17; 2025 median 9; 2026 median 12. The 9-14 item band performs best
  (1.25x median ratio, against 0.81x for 15+ and 0.70x for 8 or fewer).
- **Transitions:** none. There are no connective sentences between items. The next item's name *is* the transition.
  Section headers inside a list (ocean zones, periods) are spoken as a two-word sentence ("Twilight zone.") and then
  the item name follows.
- **Escalation order:**
  1. A physical axis (shallow to deep, early to late era, near to far from the sun).
  2. A severity ranking (explicitly "least painful" at the start, "the brutal ones further down").
  3. Fame (most famous name last).
  The final item is always the "boss". Item 1 is a strong hook, not the weakest item.
- **Sponsor placement:** after item 3-5, **23-55% into the video**, lasting 60-70 seconds. It is bridged by a
  one-sentence pun linking the last item to the sponsor, and followed by a hard cut to the next item name.

### 3.4 (c) Humor and voice [H/M]
- **Deadpan, documentary-flat delivery**, with humor in perhaps 1 line per 60-90 seconds. The horror carries the video
  and the jokes are seasoning.
- **Pop-culture comparisons** make creatures legible: "looks like the [Stranger Things monster]", "just like the
  [Alien] inner jaw".
- **Understated comparisons:** a record-breaking storm "would count as a gentle breeze" there. A death described as
  "the cold does the rest, quietly".
- **Casual asides:** "cuz we have some crazy ones", "since that's a boring outcome, let's assume you have a
  hypothetical suit".
- **Crude, juvenile vocabulary** used sparingly (a "radioactive clumps of poop" level). **Do not use this on our
  channel**; our series bible bans being gross for its own sake.
- **Callbacks** appear in the POV format ("paying more attention than last time, after what happened in the previous era").
  **This is our Doug death-counter mechanic.**
- Self-deprecation: none. Irony: rare. Rhetorical questions: almost none (0-3 per video).
- **Verbal tics** (use this *type* of tic but write our own): "However," (4-13 per video); "actually", "incredibly",
  "essentially", "literally"; triads of "No X, no Y, no Z."; "you'll soon understand why"; "To put that in context...";
  "What no one realized was..."; "The [adjective] part is...".

### 3.5 (d) Escalation across the video and the ending [H]
- Escalation is structural (the axis), not rhetorical. He does not say "it gets worse". The layers or eras simply get
  deeper and darker, and the visuals get darker too (backgrounds move from sky blue to navy to black).
- **Ending:** the last item's kicker, then a one-line CTA of about 15-25 words and 5 seconds: join the Discord to
  "discuss this video or suggest an idea for the next one" (link in description). Older videos had one short
  "subscribe for similar ones" line. There is no recap, no moral, and no teaser for the next video.
- Mr. Science ends with a reflective line about how much remains unknown. Paintify ends on an eerie kicker with no CTA.

### 3.6 Script template for 15-20 minutes (Doomed Doug adaptation)

Target 17:00 at 195 WPM, which is about **3,300 narrated words** (without sponsor). Use 12 items (the best-performing
band is 9-14).

| Section | Time | Words | Rules |
|---|---|---|---|
| Cold open | 0:00-0:10 | 15-35 | One route-and-stakes sentence plus a Doug line. The first item name must be spoken by 0:10. Optional: open straight on item 1. |
| Item 1 (the hook item, second-strongest) | 0:10-1:35 | 240-280 | Must hit its twist beat by 0:45 and contain Doug's first death or near-death. |
| Items 2-4 | 1:35-5:40 | 230-270 each | Escalate along the axis. One scale analogy per item. |
| (Sponsor slot) | about 5:40 | 20-word bridge plus 150-200 read | Only if sponsored. Place it after item 4. Hard cut back. |
| Items 5-8 | 5:40-11:10 | 240-290 each | Midpoint "zone shift" (a spoken 2-word section header plus a darker background) at about 50%. |
| Items 9-11 | 11:10-15:20 | 260-300 each | The darkest material. Callbacks to earlier Doug deaths are allowed. |
| Item 12 (the boss) | 15:20-16:50 | 300-380 | The biggest or most extreme item. Longest mechanism. Best kicker. |
| Outro CTA | 16:50-17:00 | 15-30 | One line: death-counter update plus a comment prompt or next destination. No recap. |

Beat budget inside each item (total 240-290 words): Name 1-5, Frame 20-35, Mechanism 120-180, Twist 30-50,
Kicker 8-20, Doug beat 15-30 (Doug's reaction, speech bubble, or cartoon death, placed right after the twist or as the kicker).

### 3.7 Three original example hooks (our voice, not his wording)

1. **"Every Layer of the Ocean" (tiered-pyramid episode)**
   > "Doug is going to the bottom of the ocean, one layer at a time, and the ocean gets a vote at every stop. Sunlight
   > zone. Doug's first mistake is waving at something that looks like a floating purple bag."

   (35 words, first item by about 0:07.)

2. **Parasites**
   > "Every parasite on this list has done something unforgivable to a real animal. Today, each one gets to try it on
   > Doug. Doug did not agree to this. Jewel wasp."

   (30 words, first item by about 0:09.)

3. **Prehistoric oceans**
   > "Doug has a time machine, a snorkel, and no survival instincts. He's swimming in every ocean Earth has ever had,
   > starting half a billion years ago. Cambrian. The water looks empty, which is exactly the problem."

   (38 words, first item by about 0:08.)

---

## 4. Visuals and editing (from storyboards at 5-10 s sampling, thumbnails and descriptions)

### 4.1 Pacing [H/M]
- The storyboard frame differs from the previous one in **82-98% of 5-second samples** (9 videos; median about 92%).
  So a new image or a new element arrives **at least every 5 seconds**. The true cut or build rate is probably
  **one change every 2.5-4 seconds**. [M]
- Images are **mostly static compositions that build up:** the same background persists across 2-6 beats while
  elements are added (a creature, then an arrow, then a label, then blood splatter, then a reaction head). [H]
- Motion: storyboards cannot show animation. There is no evidence of heavy animation; light pop-in and slides are
  likely, and slow zooms are possible. [L]
- Very first frame: the **thumbnail grid or pyramid is shown as the opening image** (a table of contents) for about
  0-5 seconds, then the frame cuts in to item 1. [H]

### 4.2 Screen furniture [H]
- **Persistent top-center caption bar** shows the current item name in ALL CAPS, in a thin handwritten-sans font on a
  thin white strip, on every frame of the segment. This functions as an always-on chapter label.
- **Keyword labels:** 1-3 words that echo the narration ("Theories", "In 1999", "Disappeared", "10 feet tall /
  3 meters"). They use a WordArt-like **yellow-to-green gradient fill with a thin dark outline**, or a **red
  handwritten** style. They are placed near the subject, never centered like subtitles.
- **Annotation marks:** red curved arrows (to point at features or show "this leads to that"), big red "?" and "!"
  marks, yellow warning triangles, a red "X" through things, thermometers, radar sweeps, redacted documents,
  maps with one highlighted region, and dotted distance lines between planets.
- **Real photos as evidence:** photos are inset with a thin black frame, often with a stick man beside them pointing
  or reacting. About 10-20% of frames in science videos use them.
- **Silhouettes:** unknown or terrifying creatures are first shown as a black silhouette with a red glow, then revealed.

### 4.3 Drawing style [H]
- **Two-tier rendering:**
  1. Humans are crude **MS Paint stick men**.
  2. Creatures, planets and environments are **clean, detailed digital cartoon illustrations** with soft shading.
  The contrast between them is part of the joke and the horror.
- **The stick man:**
  - Big round head (about 35-40% of figure height), white fill with a light gray shading crescent on one side,
    and a black outline about 3-4 px at 1080p.
  - Eyes are two vertical ovals with black dot pupils. The brows are single strokes.
  - Expressions come from rage-comic and meme faces: wide open "shock" mouth with a pink tongue (the most common),
    a gritted-teeth grid (fear), a flat line (unimpressed), and a squint with a smirk.
  - The body is single thin lines: straight torso, V legs, and arms that gesture or point.
  - Roles are shown by props: glasses plus a lab coat (the scientist, who acts as the recurring presenter at video
    starts), pith helmet (explorer), mustache plus peaked cap (official), captain hat (sailor), dive mask, spacesuit.
  - Crowds are drawn as 3-6 identical heads.
- **Backgrounds:**
  - Flat or vertical gradients: ocean blue that darkens with depth, sky-to-sand horizon strips, starfields.
  - Plain white backgrounds are used for concept beats. The share of mostly-white frames ranges from 5% (planets,
    ocean) to 86% (old concept videos).
  - Desaturated or gray-washed backgrounds are used for fossils and "dead" states.
- **Palette:**
  - Saturated primary colors on white, with gore in bright cartoon red.
  - Depth and horror are expressed through background value (light to dark), not through desaturating the characters.
- **Line weight:** uniform black outlines (about 3 px) on characters. Creature art has thinner and variable lines
  with interior shading.

### 4.4 Sound [M]
- 2026 captions carry **17-25 "[music]" tags per video**, clustered at item transitions (the pattern is
  ">> [music] >>" right after a kicker). This suggests a music sting or bed that swells between items.
- 2024-early 2025 captions carry 0 tags. Either there was no music or it sat too low for the captioner to tag.
- There is no evidence of heavy sound effects [L].
- **Voice:** generic AI TTS preset (his descriptions disclose this), neutral American male, flat affect, 182-217 WPM.

### 4.5 Implications for our engine
- Implement: a caption bar, gradient WordArt labels, a red arrow and "?"/"!" stamp library, a warning-triangle icon,
  a thermometer, and a depth-gradient background generator.
- Doug replaces the generic meme stick man. He keeps the red cap, and rage-comic-style expressions are drawn in our own lines.
- Creatures must be rendered at a higher detail tier than Doug.

---

## 5. Packaging and cadence

- **Upload cadence [H]:** 166 uploads in 22 months. The median gap is **5 days** overall (about 6-7 per month in 2025)
  and **7 days in 2026** (3-5 per month).
  - Upload days: mostly **Sunday, Wednesday and Monday**.
  - Upload time: overwhelmingly **09:00 Pacific**. That equals our configured 12:00 ET.
- **Durations over time [H]:**
  - 2023-24: median 8.8 minutes.
  - 2025: 12.1 minutes.
  - 2026: 14.6 minutes. It peaked at about 18-21 minutes in Jan-Mar 2026 and settled at 12-15 minutes.
  - Videos of 13+ minutes outperform (1.17-1.25x).
- **Channel health [H]:** monthly median views fell from 1-4M (2024-25) to about 300K (Jul-Aug 2026). The breakouts
  still come from the science and "forbidden places" topics (2.2M and 7.0x in Sep 2026).
- **Description template [H]** (on all 166 videos, in this order):
  1. Sponsor line with "#adv #[sponsor]" (36 of 166 videos).
  2. "Join my Discord to discuss this video" plus the link.
  3. "Subscribe and activate the bell!"
  4. Business mail.
  5. "— TIMESTAMPS —": item names starting at 0:00, including a sponsor range line.
  6. "— FURTHER READING & LINKS —": 10-60 source URLs, mostly Wikipedia plus news or science outlets (99 of 166 videos).
  7. "— DISCLAIMER —": edutainment, do your own research.
  8. "— COPYRIGHT —".
  9. "— AI USE —": says the voice is generic TTS, AI assisted research and scripting, and the drawings are by human artists.
- **Chapters [H]:** 154 of 166 videos have working chapters, and 160 have timestamps in the description. Chapter titles
  are exactly the item names. At least one video lost its chapters because its list started at 0:02 instead of 0:00.
  **Always start at 0:00.**
- **Tags and hashtags [H]:** zero tags on all 166 videos. The only hashtags are "#adv #sponsor" in sponsored descriptions.
- **Pinned comments [M]:** used for sponsor links ("link in the description and pinned comment") and for disclaimers
  on sensitive videos. Comments could not be scraped directly.
- **Playlists [H]:** 1 ("FULL PLAYLIST"). Playlists are not a strategy for him. (Our series playlists are an upgrade.)
- **Compilations [H]:**
  - "The Worst Cave Deaths Of All Time (Full Series)" is 73:51 long, stitches the cave series, and got 2.43M views (2.0x).
  - Paintify repeated this with a 34-minute "Full Series" (1M).
  - He also **reuses a near-identical title for a series**: "The Worst Cave Deaths Ever / of All Time / in History",
    7 uploads in 4 months, 1-6.9M each.
- **Shorts [H]:** none. The channel has no Shorts tab.
- **Community posts [H]:** 5 in total (idea polls, the milestone post, a scam warning, artist credit). Idea polls ask
  viewers to vote for formats.
- **Engagement [H]:** median of about 56 views per like.

---

## 6. Niche breakouts: what to borrow

### Mr. Science (@mr.scienceYT), 254K subs, 18 videos, 47.4M views (joined 2022)
- **Titles:**
  - "Nothing About [Animal] Is Normal... Here's Why" (5 videos, 1-3.8M).
  - "Why Deep Sea Creatures Get Creepier the Deeper You Go" (17M).
  - The "When Earth [Had / Was] [Extreme State]" series (2.4-3.9M, current run).
  - "We Were Completely WRONG About [Megalodon]".
- **Durations:** 15-30 minutes, trending longer (the latest are 25-30 minutes).
- **Script:** 122 WPM, 31 music tags, a 40-second atmospheric cold open, a "we" voice, a depth-descent structure
  (sunlight, twilight, midnight zone), and a reflective ending.
- **What to borrow:**
  1. The **descent-by-depth frame**, proven twice (his 17M and PE's 4.5x ocean-layer video).
  2. A **human-for-scale** figure next to a giant creature on the thumbnail. For us, a tiny Doug beside the monster.
  3. **Single-subject deep dives** ("Nothing about X is normal") as a second format between list episodes.
  4. **Deep-time "When Earth was..." scenarios**, which fit Doug vs. Prehistoric Earth.
  5. A one-line **stakes statistic** ("less than 5% explored") inside the opening 15 seconds.
- **What not to borrow:** the slow pace, and the photoreal AI art (it conflicts with our MS Paint identity).

### Paintify (@Paintify7), 20.1K subs, 12 videos, 5.6M views (joined Nov 2025)
- **Titles:** strict "Every [X]" framing: "Every Unexplored Place on Earth" (1.5M) and its Pt. 2 (1.2M), Pt. 3 (419K)
  and Full Series (1M); "Every Horrifying Place In The Ocean" (496K); "Every Planet That's Worse Than Hell".
- **Durations:** 8-14 minutes, plus a 35-minute compilation.
- **Script:** zero intro (item name at 0:00), 182 WPM, **very short sentences** (9.9 words each), stacked fragments
  for tension ("No warning. No time to send a signal." style), no CTA, and it ends on an eerie kicker.
- **Packaging:** a clone of PE archetype A (photo tile grid).
- **What to borrow:**
  1. Proof that a new channel can break out within about 6 videos using PE grammar in a "places and ocean" niche.
  2. The Pt. 2 / Pt. 3 / Full Series stacking, done within 5 months.
  3. Fragment bursts at twist beats.
- **What to avoid:** several claims sound unverifiable (for example unexplained "symmetrical structures"). That is a
  credibility and policy risk. We cite sources.

---

## 7. Rules for our agents

Each rule is written so it can be checked. "Must" means a rejection if it fails.

### Titler (youtube-titler)
1. The title must be 38-65 characters and 6-11 words.
2. Title Case is required. Zero ALL-CAPS words (acronyms like "USS" are exempt). Zero emojis. Zero "!".
   At most one "?", and only in a "What If..." title.
3. The title must match one of these skeletons:
   - (T1) "What [Dying/Surviving/Living] [in/on] Every [Set] Would Be Like"
   - (T2) "How Doug Would Die in Every [Set]" or "How [Every X] [Kills/Died]"
   - (T3) "The Most Disturbing [Creatures/Places/Discoveries] in Every/Each [Set]"
   - (T4) "The [Creepiest/Most Disturbing] [X] That/Scientists [Revelation clause]"
   - (T5) "The Worst [X] Deaths Ever"
   - (T6) "Nothing About [X] Is Normal" / "Why [X] Gets [Creepier/Deadlier] the [Deeper/Longer] You Go"
4. The title must contain exactly one dread adjective from {Most Disturbing, Worst, Creepiest, Scariest, Deadliest,
   Most Terrifying} or a death verb (Die/Died/Dying/Kill). "Craziest", "Weirdest", "Silliest" and "Insane" are banned.
5. The title must contain a scope device ("Every", "Each", "From Every", "in Every") or a revelation clause.
6. "in N Minutes" is banned. Leading list counts ("The 7 ...") are banned.
7. Titles must not include a word that appears as a label on the thumbnail (no duplication).
8. Sequels are allowed only if Pt. 1 is at least 2x the channel median at day 28. Format: "<Pt. 1 title> (Pt. 2)".
9. Produce 5 candidate titles, labelled by skeleton ID, with the chosen one first.
10. Titles must never reuse a Paint Explainer title verbatim, or with only a noun swapped.

### Script Writer (script-writer)
1. Total narration must be 2,800-3,500 words for a 15-18 minute video at 195 WPM. Report the word count and estimated runtime.
2. The first item name must appear within the first 35 words. No greeting, channel name, "in this video" or subscribe
   ask before item 1.
3. The item count must be 9-14. Every item must start with a standalone name sentence of 1-5 words that exactly
   matches its chapter title and caption bar.
4. Every item must contain these beats: Name, Frame (15-35 words), Mechanism, Twist beat (flagged by a marker such as
   "The worst part is", "Here's the problem", "But that's not the disturbing part"), Kicker (8-25 words, last sentence
   of the item), and a Doug beat (15-30 words).
5. Items must be ordered along one declared axis (depth, era, distance or severity). The script header must state the
   axis. The last item must be the most extreme on that axis.
6. Item 1 must reach its twist beat within 45 seconds (about 145 words).
7. There must be zero transition sentences between items; the next item name is the transition. Spoken section headers
   (for example "Midnight zone.") are allowed.
8. Each item needs at least one concrete scale analogy using everyday objects.
9. Average sentence length must be 14-19 words. At least one sentence of 6 words or fewer per item. No sentence over
   35 words. Flesch Reading Ease must be 60-72.
10. Humor: at most one joke line per 60 seconds. Deadpan only. No gross-out, no gore, and no crude sexual or bathroom humor.
11. Every factual claim needs a source URL in facts.md. Claims that can't be sourced must be cut, not hedged.
12. The ending must be the final item's kicker, then an outro of 30 words or fewer (death counter plus one CTA).
    No recap, no moral, no "thanks for watching".
13. Use each tic phrase ("However", "actually", "essentially", "incredibly") at most 6 times. Rotate twist markers:
    the same marker may not appear twice in a row.
14. Use no more than 3 consecutive words from any Paint Explainer transcript, and no PE item lists.

### Art Director / Illustrator (art-director, illustrator, graphic-designer)
1. Two-tier rendering is required: Doug and humans are crude stick figures (uniform 3-4 px black line at 1080p).
   Creatures and environments are detailed cartoon illustrations with interior shading.
2. Doug's expressions come from a fixed set: {shock-open-mouth, gritted-teeth, flat-unimpressed, hopeful-smile,
   X-eyes-dead}. The red cap is always visible, including on ghost Doug.
3. Every segment frame must have the top-center caption bar with the item name in ALL CAPS, matching the script name exactly.
4. Keyword labels: 1-4 words, gradient WordArt or red handwritten style, placed next to the subject.
   At most 2 labels on screen at once. Each label must echo a word spoken within ±2 seconds.
5. Annotation library: red curved arrow, red "?", red "!", yellow warning triangle, red X, thermometer, map highlight,
   dotted distance line. At least 1 annotation per item.
6. Depth or danger is shown through the background value ramp. Ocean backgrounds must get darker per zone
   (sunlight, then twilight, then midnight, then abyss, then trench, ending near-black navy).
7. Unknown or terrifying reveals start as a black silhouette with a red glow, then a full reveal 1-3 beats later.
8. Gore is never realistic. Only bright cartoon-red splashes and cartoon deaths (X eyes, ghost floats up).
9. Real photos may be inset only with a verified license or public-domain status. They get a 4 px black frame.
10. **Thumbnail:**
    - Archetype A (white background, 6-12 tiles, black rounded frames about 6 px at 1280x720, bold comic label under each
      tile, labels = chapter names), or
    - Archetype B (tiered pyramid, labels outside and alternating sides) for any layered or era topic, or
    - Archetype C (one or two hero subjects, 1-3 words of text, flat background, tiny Doug for scale).
    - Maximum 3 fonts. No title text. No gore beyond cartoon level. Doug may appear only as a small scale figure or as one tile.
11. The thumbnail must be readable at 168x94 px: at most 12 tiles, labels of 4 words or fewer, and tile subjects that
    stay recognizable at that size.

### Editor (director, editor)
1. There must be a visual change (a new image or a newly added element) at least every 5.0 seconds. Target an average of
   one change every 3 seconds. QC must fail any static stretch longer than 6 seconds.
2. Build-up composition: keep one background per beat group of 2-6 changes and add elements rather than hard-cutting everything.
3. Open with the thumbnail grid or pyramid for 1.5-4 seconds, then cut to item 1's first frame.
4. Motion must be light only: pop-in, slide-in and slow push-in of up to 10% are allowed. No 3D transitions and no whooshing wipes.
5. Voice: TTS at 190-205 WPM effective. Set speaking_rate so that measured WPM falls in this band; the fallback_wpm of
   165 in channel.yaml is too slow for this format.
6. Music: a low bed under narration at about -28 to -24 LUFS relative. A short sting or swell at every item transition
   (on the kicker-to-name cut). Keep music below the voice throughout.
7. The chapter list must start at 0:00, and there must be one chapter per item named exactly like the item.
8. The description must follow the template order: sponsor (if any), comment/Discord CTA, subscribe line,
   "— TIMESTAMPS —", "— SOURCES —" (all facts.md URLs), "— DISCLAIMER —", "— AI USE —" (honest disclosure of TTS and
   AI assistance). No tags spam; at most 3 hashtags.
9. Sponsor segments go after item 3-5, at 25-45% of runtime, and last 60 seconds or less. They are bridged by one line
   and followed by a hard cut to the next item name.
10. The target runtime is 15-18 minutes. Hard limits are 12-22 minutes. After every 3 parts of a series, assemble a
    "(Full Series)" compilation.
