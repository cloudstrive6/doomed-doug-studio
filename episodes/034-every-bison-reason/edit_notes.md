# Edit notes 034-every-bison-reason (draft stage, not final)

- Runtime: 689.4 s (11.5 min), within the 10-12 min brief target. Includes a 15 s end slate.
- Shots: 209, average 3.30 s. Real voice (Chirp 3 HD), 2,128 words.
- Pace: wpm_speech 198.6 (target 190-205), wpm_overall 185.2.
- Shots over 5 s: 24 (23 plus the 15 s end slate); every one has `appear` pop-ins, so no static stretch over 5 s.
- Draft render built (`render --limit 25`); frames sampled at 2/10/20/40/60 s look fine. The 10 s frame shows black bison silhouettes (looks like an intentional reveal; the visual screener should confirm).

## Changes
- `config/channel.yaml` voice.speaking_rate lowered 1.12 -> 1.085. Reason as given in the task: calibrate wpm_speech into the 190-205 band (I did not re-measure at 1.12). Result at 1.085: 198.6 wpm.
- Added IPA pronunciations: Lamar `ləˈmɑr` and Hayden `ˈheɪdən` (Lamar and Hayden Valleys).
- Script words unchanged.

## Checks
- `validate 034-every-bison-reason`: OK. `shorts validate 034-every-bison-reason`: OK.
