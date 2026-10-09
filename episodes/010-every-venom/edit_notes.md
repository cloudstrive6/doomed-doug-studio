# Edit notes: 010-every-venom

- Narration: real Chirp 3 HD voice. Runtime 961.7 s (16:02), within the 15-18 min brief target.
- Words 3,040; wpm_speech 199.0 (target 190-205), wpm_overall 189.7. No voice-rate change needed.
- Shots: 286, average length 3.36 s. 24 shots run 5.0-7.1 s (longest s260 at 7.1 s); each has 2-5 staggered `appear` pop-ins, so no static stretch exceeds about 3.5 s.
- Chapters: 12 items, generated at render into build/chapters.txt (first at 0:00, last Box Jellyfish at 14:10). metadata.json keeps `{{CHAPTERS}}`, which upload resolves from that file.
- Shorts: validate OK. Durations short01 44.8 s, short02 46.3 s, short03 50.8 s (all under 55 s).
- `python -m studio validate 010-every-venom`: OK.
- Sateré-Mawé: the name is only in narration and the UTF-8 captions.srt. Arimo and ComicNeue both contain the é glyph, so on-screen text is safe.
- Draft (first 25 shots, 74.9 s) frames sampled: pop-ins and layout changes every 2-5 s, caption bar and death counter legible.
- Changes made: none to the shotlist, script, or config. Final render left to CI.
