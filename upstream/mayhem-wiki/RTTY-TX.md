<img width="239" height="320" alt="image" src="https://github.com/user-attachments/assets/427981b0-17ad-48aa-9fb4-2a807c212a59" />

RTTY TX transmits Radio TeleTYpe (RTTY) signals using Baudot/ITA2 encoding. It generates an FSK signal with configurable baud rate, frequency shift, and tone placement.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

**Baud** — Transmission speed. Options: 45, **45.45** (default), 50, 75, 100, 110, 150, 200 baud.

**Shift** — Frequency separation between Mark and Space tones. Options: 85, **170** (default), 200, 450, 850 Hz.

**Inverted** (checkbox, default: on) — Swaps Mark and Space tone assignments. Enabled by default to match the most common RTTY convention.

**Mark t** — Sets the absolute frequency offset of the Mark tone. Options:

| Label | Meaning |
|---|---|
| **CNT** (default) | Centered: Mark = −shift/2, Space = +shift/2 |
| 0 | Mark at 0 Hz offset |
| 2125 | Mark at +2125 Hz (US HF AFSK standard) |
| −2125 | Mark at −2125 Hz |
| 1275 | Mark at +1275 Hz |
| −1275 | Mark at −1275 Hz |

The computed Mark and Space tone values (in Hz, relative to the carrier) are shown on the line below these controls. They update automatically when Shift, Mark t, or Inverted are changed.

**Set message** — Opens the text entry keyboard. The message text is displayed below the button. Default: `PORTAPACK`. The message is encoded using Baudot/ITA2 (USOS disabled for maximum receiver compatibility) and transmitted once per START press.

# RF Parameters

| Parameter | Value |
|---|---|
| Frequency | Stored in persistent memory — typical HF RTTY: 14.080 MHz (20 m) |
| Bandwidth | 2.048 MHz |
| Sample rate | 2.048 MSps |
| Stop bits | 1.5 (fixed) |
| TX gain | 0–47 dB (LNA), 0/14 dB (AMP) |

# Transmission

Press **START** to transmit. The message is sent once and transmission stops automatically when complete. Press **STOP** to abort early.

# Settings Persistence

Settings are saved to `tx_rtty.ini`.