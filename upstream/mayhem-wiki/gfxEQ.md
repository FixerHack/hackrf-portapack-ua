![image](https://github.com/user-attachments/assets/14937560-deb0-4a45-a6d0-1711751046cf)

# Introduction

gfxEQ is a Wideband FM (WFM) audio receiver with a full-screen graphic equalizer display. It receives FM broadcast radio and visualises the demodulated audio spectrum as 11 animated bar segments covering the audible frequency range. The display fills almost the entire screen. 20 colour themes are available and can be cycled without interrupting reception.

The gfxEQ widget is also embedded inside the [Radio](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Radio) app, where it appears when you click the waveform display in WFM mode.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

* **Frequency button** (leftmost, labelled `<93.10>` by default): click to open the numeric keypad for direct frequency entry. Use the rotary encoder while focused to step in **25 kHz increments** — suitable for tuning FM broadcast channels. The default frequency is **93.1 MHz**.
* **AMP:** RF preamplifier — 0 = off, 1 = on (+14 dB). Avoid enabling AMP near strong local broadcast transmitters.
* **LNA:** Low Noise Amplifier gain (0–40 dB). Default 32.
* **VGA:** Variable Gain Amplifier / baseband gain (0–62 dB). Default 32.
* **MOOD:** Cycles through 20 built-in colour themes. Each press advances to the next theme. The selected theme is saved and restored on next launch.
* **Volume:** Audio output level. Use the rotary encoder. If the audio is inaudible, try increasing to around 70.

The graphic equalizer occupies the rest of the screen below the controls and updates continuously from the WFM audio spectrum data.

# Frequency bands

The display shows 11 bars, each representing a fixed audio frequency range:

| Bar | Range (Hz) | Character |
|-----|-----------|-----------|
| 1 | 0–375 | Deep bass, low rumble |
| 2 | 375–750 | Upper bass punch |
| 3 | 750–1500 | Lower midrange fullness |
| 4 | 1500–2250 | Midrange clarity |
| 5 | 2250–3375 | Upper midrange bite |
| 6 | 3375–4875 | Presence and edge |
| 7 | 4875–6750 | Lower brilliance |
| 8 | 6750–9375 | Brilliance and air |
| 9 | 9375–13125 | High treble sparkle |
| 10 | 13125–16875 | Upper treble airiness |
| 11 | 16875–24375 | Extreme treble / noise floor |

# Technical details

The app uses WFM demodulation with a **180 kHz** channel bandwidth at a 3.072 MHz sampling rate. Audio is output at 48 kHz. The modulation and bandwidth are fixed — this app is specifically intended for FM broadcast reception (87–108 MHz and above).

The frequency can also be set via the USB Serial Console using the standard `setfreq` command.

# Settings persistence

The selected frequency and colour theme are saved automatically and restored on next launch. Settings are stored in `SETTINGS/rx_gfx_eq.ini` on the SD card.