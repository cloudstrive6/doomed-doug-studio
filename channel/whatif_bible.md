# Doomed Doug: What If series bible

Owned by the creative director. Every agent that writes, voices, draws or edits a What If episode reads this first. It replaces the old "Doug dies" premise and death counter for this format. Drafted 2026-11-26 for pilot w01.

Format reference: the DOOMPERK teardown in the Bryce-Brain vault (`wiki/answers/doomed-doug-doomperk-restyle-plan.md`). We copy the shape of the story, never its wording, characters, jokes or look.

## Premise

Every episode asks one question: what if you had, or were, something nature never meant a person to have, a pet megalodon, a body full of parasites, a house on an active volcano. The narrator tells the story to you, and you are Doug. Over a counted run of days, the thing goes wrong in new ways, and each problem is solved with real, sourced science that appears on screen as it is said. A named rival makes it worse, a science friend explains it, an official tries to shut it down. The story ends differently every time: a win, a rescue, a narrow escape, a release. Then the narrator says plainly what was real, what was made up, and one real safety rule.

## Doug as "you"

- The narrator always speaks in the second person: "you wake up", "you sign it anyway". The viewer is Doug.
- On screen, you are Doug: the red cap is the one thing that never changes. Everyone else calls him Doug.
- Doug speaks in short lines, one to eight words most of the time ("Hi, buddy!", "He thought it was the moon."). Cheerful, optimistic, a bit gullible.
- New in this format: Doug learns. He falls for something early in the episode and, when the same trick comes back, he does not fall for it again. That learning is usually what wins the ending.
- Doug never dies in this format. No death counter, no ghost Doug, no "Doug deaths" badge. Cartoon peril is allowed; injury detail, blood and gore are not.

## The narrator

- Calm, deadpan, documentary voice, talking to you. Treats your choices with dry patience and is quietly on your side.
- Delivers the science straight, in short sentences, then lands one dry line about the story ("Tanner carried no buckets. He filmed all four hundred.").
- Sits between the cast lines so the picture can cut often. Never mean to the viewer, never preachy, never gross for its own sake.
- Owns the day counter and the time skips ("Day twelve. Meatball is three metres long. The pool is not.").
- Unseen. No body, no avatar.

## Recurring cast

At most six speaking parts per episode, including the narrator and Doug. The rival, sidekick and authority below are built to come back in later episodes; an episode may add a guest in their place, as long as the cap holds. Animals never talk.

| id | name | role | personality | voice brief |
|---|---|---|---|---|
| narrator | Narrator | Second person storyteller | Deadpan, patient, secretly fond of you | Man, forties, calm and dry, warm underneath, unhurried |
| doug | Doug | You, the viewer | Cheerful, hopeful, gullible at first, learns by the end | Man, late twenties, bright and eager, short happy bursts |
| tanner | Tanner Sloane | Rival: next door neighbour and small time influencer | Loud, vain, always filming, turns everything into content; not evil, just hollow, and the story finds the person under the ring light | Man, mid twenties, loud presenter energy, fast, always performing |
| wren | Wren Adeyemi | Science sidekick: bait shop worker, marine biology student | Flat, dry, never impressed, always right, quietly loyal to Doug | Woman, early twenties, flat and quick, deadpan delivery |
| hobbs | Officer Marlene Hobbs | Authority: local fisheries officer | Rule bound, unhurried, bone dry; finds the loophole when it is the right thing to do | Woman, fifties, low and gravelly, slow, bone dry |
| meatball | Meatball | The w01 megalodon pup; non speaking; can return as a lagoon cameo | Friendly, hungry, curious, comes when Doug taps the water twice | No voice. Sound design only: water swooshes, a soft happy click, big crunches |

### LOOK lines for the illustrator (simple 2D cartoon: clean outlines, flat colours, soft shading)

Locked designs as drawn by the toon engine (`studio/toon.py` CAST_LOOKS, `pilots/w01-pet-megalodon/cast_looks.json`), 2026-11-26:

- **Doug:** light peach round head, brown hair under the **red baseball cap** (always on), big oval eyes with white highlights, mustard yellow t-shirt, blue jeans, white trainers. Voice: Chirp 3 HD Puck.
- **Tanner Sloane:** light tan skin, blond quiff, sunglasses, purple jacket, black trousers. Signature item: **phone on a stick with a round ring light**. Voice: Fenrir.
- **Wren Adeyemi:** dark brown skin, black hair in a bun, green t-shirt under a tan bait shop apron, dark trousers. Dry half-lidded look. Voice: Kore.
- **Officer Marlene Hobbs:** fair skin, grey bob, navy fisheries uniform and cap with a gold star, gold badge. Signature item: **brown clipboard**. Voice: Gacrux.
- **Meatball:** slate blue-grey megalodon with a white belly (countershading), big friendly eye as a pup, lunate tail, small triangle teeth when the jaw opens. Drawn by `studio/toon_props.py` at the size the script asks for.
- **Narrator:** Chirp 3 HD Charon (the channel's existing voice).

## Beat sheet

Timing targets assume 1,800 to 2,000 spoken words, about 12 to 13 minutes with the voiced cast (about 150 words a minute). Word numbers count spoken lines only.

| # | Beat | Target | What it must do |
|---|---|---|---|
| 1 | Cold open | 0:00 to 0:15 | Second person, concrete number in the first sentence, the strange thing already happening |
| 2 | Rival named | by 0:20 | A rival with a full name and a name card, plus one joke caption or line about them |
| 3 | Time skip tease | 0:20 to 0:50 | Three or four future beats, the last a cliffhanger that is true to the ending. Vary the form every episode (a list of things coming, dates, counts, places); never reuse the reference channel's phrasing |
| 4 | Title drop | 0:35 to 1:30, spoken words 72 to 153 | The title as a question: "So, what if you had a pet megalodon?" |
| 5 | Story with the voiced cast | 1:00 to 11:00 | About 8 speaker changes a minute, the narrator calm between lines, a DAY badge on every story scene, time skips that follow the counter |
| 6 | Problem, real science, solution | every 60 to 90 seconds inside beat 5 | Each problem is explained with a real fact on a sourced CARD while it is said, then solved. Where scientists disagree, say so in one short plain line |
| 7 | Callbacks and the rival's turn | climax, last quarter of the story | An early detail returns to solve the climax (w01: the tap tap game from day three). The rival gets a turn: a change of heart, a confession or a real moment |
| 8 | Honesty and safety close | last 60 to 75 seconds | What was real, what was made up, one real safety rule with two sources |
| 9 | Comment question | last 10 seconds | Two options from inside the story: "Comment X or Y" |

## Rules

### Science
- Every spoken science claim and every CARD has a row in the episode's `facts.md` with two independent sources (museum, university, peer-reviewed paper or its press release, NOAA, Britannica, Natural History Museum, Smithsonian). One claim, two sources, or it is cut.
- Claims must be current. When a newer study changes a number, use the newer number and say the older one only if it helps.
- Where scientists disagree, say it in one short plain line ("Scientists still disagree.").
- Anything named in narration is on screen as it is said: a CARD for facts, a WORD pop for big words (every 20 to 40 seconds).
- The fiction is announced in the honesty close. Never present a made-up thing as real.

### Policy (YouTube inauthentic content, read 2026-11-26)
- Every episode has a different story and a different outcome. No death counter, no repeated ending, no fixed template of jokes.
- Original cast, names, designs, wording and jokes. The reference channels' scripts, characters, titles and thumbnails are never copied.
- AI tools may draw and voice our own characters and stories only.

### Tone
- Adult-coded humour, clean enough for a general audience. Not made for kids.
- Cartoon peril is fine. Never gore, blood or injury detail. Nobody dies.
- The narrator is dry, not cruel. Jokes land on vanity, bad plans and paperwork, not on real people or groups.

### Outcomes vary
- Rotate the endings across episodes: a win, a rescue, a narrow escape, a release, a trade, a compromise. Log each episode's outcome below and do not repeat the last one.

### Writing for text to speech (Google Chirp 3 HD)
- Short sentences, spoken lines under about 30 words.
- Numbers as words in spoken lines ("eighteen centimetres"); digits are fine on CARD lines.
- No abbreviations, emojis or parentheses in spoken lines. No em dashes or en dashes anywhere; use commas, full stops or "to".

## Episode log

| id | title | outcome | rival turn | lore added | status |
|---|---|---|---|---|---|
| w01 | What If You Had a PET Megalodon? | Rescue and release: Meatball finds Tanner in the dark sea by his electric sense and is released into the Gull Lagoon marine reserve | Tanner confesses to Hobbs that he called her and tried to sell Meatball, with no camera on | Gull Lagoon marine reserve; the tap tap signal; Tanner's crayon contract; Hobbs has no forms for extinct animals | Script draft 2026-11-26 (1,860 spoken words, 27 scenes), not produced |
