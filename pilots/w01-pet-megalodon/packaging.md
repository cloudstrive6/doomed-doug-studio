# w01 packaging: title, thumbnail, description, tags

Written 2026-11-26 with the yt-package skill (Jakeschincariol/youtube-agent-skill). Every title went through the skill's `title.py` linter, and a word-level edit distance was measured against all 39 DOOMPERK titles in `Z:\Bryce-Brain\raw-sources\doomperk-teardown-2026-11\doomperk-videos.txt`. The working title "What If You Had a PET Megalodon?" is 1 word off "What If You Had a PET Tornado?" and is retired. The script's H1 still carries it; change that line before render if the title card reads it.

Rules applied: under 60 characters, "What If" question form, exactly one CAPS word, at least 4 words away from every DOOMPERK title, and no "You Had a PET" pattern. Thumbnail labels never repeat a title word.

## 1. Ten title candidates, ranked

Scores are 1 to 5. Search fit is measured against "pet megalodon", "baby megalodon" and "megalodon in pool". Distance is the word edit distance to the nearest DOOMPERK title (4 or more words off scores 4 at least; a "pet" plus creature echo costs a point).

| Rank | Title | Chars | Curiosity | Clarity | Search fit | Distance | Total | Nearest DOOMPERK title (words off) | Linter |
|---|---|---|---|---|---|---|---|---|---|
| 1 | What If a Baby MEGALODON Lived in Your Pool for 30 Days? | 56 | 5 | 5 | 5 | 5 | 20 | SAITAMA Trained You for 100 Days (8) | 100 |
| 2 | What If a Baby MEGALODON Landed in Your Pool? | 45 | 4 | 5 | 5 | 5 | 19 | Every Girl Could See YOUR Rating (6) | 84, no number |
| 3 | What If Your Pet MEGALODON Outgrew Your Pool in 12 Days? | 56 | 5 | 5 | 5 | 4 | 19 | Your CRUSH Was a Secret AGENT (8) | 100 |
| 4 | What If You Raised a Baby MEGALODON in Your Pool? | 49 | 3 | 5 | 5 | 5 | 18 | You Had a DOMAIN EXPANSION in Real Life (5) | 84, no number |
| 5 | What If You Raised a Baby MEGALODON for 30 Days? | 48 | 4 | 5 | 4 | 4 | 17 | SAITAMA Trained You for 100 Days (6, same "for N Days" ending) | 100 |
| 6 | What If You Woke Up to a MEGALODON in Your Pool? | 48 | 4 | 5 | 4 | 4 | 17 | You Could CONTROL All Rats in Your City (6) | 84, no number |
| 7 | What If a Storm Threw a MEGALODON in Your Pool? | 47 | 4 | 4 | 4 | 5 | 17 | You Could CONTROL All Rats in Your City (6) | 84, no number |
| 8 | What If You Kept a Baby MEGALODON as a Pet? | 43 | 3 | 5 | 5 | 3 | 16 | You Had a DOMAIN EXPANSION in Real Life (6; "pet" framing echoes PET Tornado) | 84, no number |
| 9 | What If Your Pool Shark Was a Baby MEGALODON? | 45 | 4 | 3 | 4 | 4 | 15 | Your CRUSH Was a Secret AGENT (4) | 84, no number |
| 10 | What If a MEGALODON Pup Chose You as Its Owner? | 47 | 4 | 3 | 2 | 5 | 14 | SAITAMA Trained You for 100 Days (7) | 84, no number |

Every title runs past the 40 character mobile cut, but in each the subject (baby megalodon, pet megalodon) sits inside the first 40 characters, so the mobile feed still shows what the video is about.

## 2. Top 3 with thumbnails

The title and thumbnail are one unit: the label says what the title does not.

| Rank | Title | Thumbnail | Label | Why the pair works |
|---|---|---|---|---|
| 1 | What If a Baby MEGALODON Lived in Your Pool for 30 Days? | A: smug Doug waist deep in his pool, the megalodon rising huge behind him | GOOD BOY | The title says baby; the image shows the shark is no longer small. The label is Doug's proud owner line, and the gap between "good boy" and the teeth behind him is the click. Keep the shark at story scale (about 4 m, filling the pool), not a sea monster, so the thumbnail does not oversell. |
| 2 | What If a Baby MEGALODON Landed in Your Pool? | B: split, DAY 1 pup in the pool, DAY 12 the shark too big for the pool, water spilling | TOO BIG | The title gives the arrival; the split gives the problem it turns into. "DAY 1" and "DAY 12" stay as small corner tags; the big label is TOO BIG across the right panel. |
| 3 | What If Your Pet MEGALODON Outgrew Your Pool in 12 Days? | C: Doug in the pool with the pup while the influencer neighbour films in shock | FOR SALE | The title already says it outgrows the pool, so option B would repeat it. C adds the second threat: the neighbour wants to sell it. Put FOR SALE on the ring light phone screen or as a tag hung on the fence. |

Thumbnail brief for the winner (A, GOOD BOY): Doug front left, waist deep, chin up, eyes half shut, smug grin, red cap; the shark's head and open grin rise out of the water behind his right shoulder, its eyes big and friendly so it reads as a pet and not a kill. Background: bright blue pool and a hot yellow or orange sky, so the grey shark and red cap hold contrast at feed size. Label in heavy white letters with a black outline, top right, clear of the YouTube timestamp corner.

## 3. Description

Under 120 words (117).

```
A storm throws a two metre megalodon pup over your back fence and into your swimming pool. Now you have one fisheries officer, a neighbour who wants to sell it, and a shark that will not stop growing.

What is real: every science card. Megalodon died out about 3.6 million years ago, its name means big tooth, and scientists still argue about its size, its speed and how big its babies were. We show both sides.

What is invented: a living megalodon, the pool, the deadline and the rescue at sea.

Shark bites are rare, about 70 unprovoked bites a year worldwide. Swim with a buddy.

Chapters: [to be added from the final cut]

#megalodon #whatif #sharks
```

## 4. Tags

```
pet megalodon, baby megalodon, megalodon in pool, megalodon pup, megalodon facts, what if megalodon was alive, megalodon cartoon, shark story animation, what if, doomed doug
```

## Ship it, or change it?

Recommended: rank 1, "What If a Baby MEGALODON Lived in Your Pool for 30 Days?" with thumbnail A and the label GOOD BOY. Nothing here is published; Bryce or the pipeline publishes.
