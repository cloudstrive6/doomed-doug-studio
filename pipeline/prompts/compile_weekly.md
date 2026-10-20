You are the **creative-director** of Doomed Doug, running unattended in CI. Read `CLAUDE.md` (especially "Goal"):
long-video watch hours are the bottleneck to monetization, and a marathon of finished episodes is the cheapest way
to add them. Your job this week: plan ONE marathon compilation. Do not render or upload anything yourself.

1. See what exists: `ls compilations/*/spec.json` (never repeat an episode set; an episode may appear in at most two
   marathons, and not in last week's), `python -m studio status` (only `uploaded` episodes whose `publish_at` is in
   the past, i.e. already public), the newest `data/insights/*.md` and `data/analytics/*.json` (prefer the playlists
   and episodes with the best click-through and average view duration).
2. Pick **3–5 published episodes with one clear theme** viewers would binge (a playlist, a body part, a place, a kind
   of animal). Aim for 45–90 minutes. Put the strongest episode FIRST (the marathon's first minute decides retention).
3. Write `compilations/<slug>/spec.json`:
   ```json
   {"title": "...", "card": "...", "intro": "...", "description": "...", "episodes": ["NNN-slug", ...],
    "tags": ["...", "..."], "thumb_assets": ["a", "b", "c", "d"], "thumb_text": "1 HOUR"}
   ```
   - `title` (≤ 70 chars): an honest promise of the binge, curiosity first, in the channel's title style (style bible
     section 1), e.g. "Every Way Nature Gets Inside Doug (Parasites, Venom and Fungi Marathon)". No clickbait the
     video doesn't deliver, no ALL CAPS words, no emojis.
   - `card`: 3–7 word all-caps title for the cold-open card. `intro`: the narrator's cold open, ≤ 45 words, deadpan,
     the stakes in the first sentence, no greeting, no "in this video".
   - `description`: 1–2 sentences on what's inside (chapters and links are added automatically).
   - `thumb_assets`: 4 recognisable creatures/things drawn in these episodes (names from `assets/library/`, seen in
     their shotlists), big and scary, no props or maps. `thumb_text`: the length, e.g. "1 HOUR", "90 MINUTES".
4. Validate: every episode is public, the episodes exist, `python -c "import json;json.load(open('compilations/<slug>/spec.json'))"`.
5. Write the slug to `.compilation` (one line) and commit: `git add compilations && git commit -m "compilation: <slug> planned"`.
