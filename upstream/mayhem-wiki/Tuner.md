The **Tuner** is a utility app that plays reference tones through the PortaPack's audio output to help tune musical instruments by ear.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Controls

| Field | Description |
|-------|-------------|
| **Instrument** | Select the instrument preset: Guitar, Violin, or Pitch Fork. |
| **Note** | Select the string or note to tune to. Changes dynamically based on the selected instrument. |
| **Note Frequency** | Displays the frequency (Hz) that will be played. |
| **Note Octave Shift** | Displays the octave shift applied. A value of `-1` means the PortaPack plays one octave lower than the actual target pitch (hardware limitation for very low frequencies). |
| **Volume** | Audio output volume (0–99). |
| **Play / Stop** | Large button at the bottom. Starts or stops the reference tone. |

## Instruments & Notes

### Guitar (Folk Guitar)

| String | Frequency played | Octave shift | Note |
|--------|-----------------|--------------|------|
| E2 | 165 Hz | -1 | PortaPack plays E3; actual string is E2 |
| A2 | 110 Hz | 0 | — |
| D3 | 147 Hz | 0 | — |
| G3 | 196 Hz | 0 | — |
| B3 | 247 Hz | 0 | — |
| E4 | 330 Hz | 0 | — |

### Violin (440 Standard, 12ET)

| String | Frequency |
|--------|-----------|
| G3 | 196 Hz |
| D4 | 294 Hz |
| A4 | 440 Hz |
| E5 | 659 Hz |

### Pitch Fork

| Standard | Frequency |
|----------|-----------|
| 12ET A4 | 440 Hz |
| Sarti's A4 | 436 Hz |
| 1858 A4 | 435 Hz |
| Verdi's A4 | 432 Hz |

## Octave Shift Indicator

When playing a note with a non-zero octave shift, the display shows:
- The **played frequency** (left, in red) — what the speaker actually outputs
- The **real target frequency** (right, in red) — what the actual string should sound like
- The **shift value** in octaves (e.g. `-1 * 8ev`)

When no shift is applied, these indicators are hidden.

## Notes

- Audio output goes to the 3.5 mm headphone jack or the internal speaker.
- The tone plays continuously until the **Stop** button is pressed or the note is changed.
- Changing the note while a tone is playing immediately switches to the new frequency without stopping.
- Very low frequencies (e.g. guitar E2) are played one octave higher due to PortaPack hardware speaker limitations.