The **Metronome** is a utility app that produces audible click tracks at a configurable tempo and rhythm. It is useful for musicians practicing with the PortaPack's speaker or headphone output.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Controls

| Field | Range | Description |
|-------|-------|-------------|
| **BPM** | 1 – 1000 | Beats per minute (tempo). Default: 120. |
| **Tap Tempo** | — | Opens the Tap Tempo screen to set BPM by tapping. |
| **Accent Beep Tune** | 380 – 24000 Hz | Frequency of the accented beat (first beat of each bar). Default: 880 Hz. |
| **Unaccent Beep Tune** | 380 – 24000 Hz | Frequency of all other beats. Default: 440 Hz. |
| **Rhythm** | 1–99 / 1–99 | Time signature as beats per bar / note value (e.g. 4/4, 3/4, 6/8). |
| **Beep Flash Duration** | 10 – 999 ms | How long each beep lasts. Default: 100 ms. |
| **Volume** | 0 – 99 | Audio output volume. |
| **Play / Stop** | — | Large button at the bottom. Starts or stops the metronome. |

## Progress Bar

The progress bar shows the current beat position within the bar:
- 🔴 **Red** — accented beat (first beat of the bar)
- 🟢 **Green** — unaccented beats

## Tap Tempo Screen

Pressing **Tap Tempo** opens a sub-screen where you can:
- **Tap BPM** — tap the large button repeatedly in rhythm; the app averages the last 4 taps to calculate the BPM.
- **Input BPM** — type a BPM value directly via the keyboard.
- **Apply** — confirm and return to the main screen.
- **Cancel** — discard changes and restore the previous BPM.

## Notes

- The metronome uses the PortaPack's audio output — connect headphones via the 3.5 mm jack or use the internal speaker.
- The accent beat is always the **first beat of each bar**; all other beats are unaccented.
- The Rhythm field follows standard music notation: the left number is beats per bar, the right number is the note value that counts as one beat (e.g. 6/8 plays six eighth-note beats per bar).