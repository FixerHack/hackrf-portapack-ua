# Level App
![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/3157857/42ff454a-7b7e-451f-9474-58b57b1e1937)

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).


# Introduction

The Level app provides a comprehensive single-screen signal monitoring view combining RSSI meters, a power level readout, receiver saturation indicator, a scrolling history graph, and optionally audio output and an audio squelch beep. It is designed for signal level measurement and monitoring across AM, NFM, WFM, and spectrum (capture) modes.

# Controls

**Row 1 — gain:**

* **LNA:** Low Noise Amplifier gain (0–40 dB).
* **VGA:** Variable Gain Amplifier / baseband gain (0–62 dB).
* **AMP:** RF preamplifier — 0 = off, 1 = on (+14 dB).
* **VOL:** Audio output volume (only relevant when audio is on).

**Row 2 — reception parameters:**

* **BW:** Bandwidth selector. Options depend on the selected modulation mode (AM: DSB/USB/LSB/CW variants; NFM: various kHz widths; WFM: 200k/180k/80k; SPEC: various sampling rates from 12.5k to 20M).
* **MODE:** Demodulation mode — AM, NFM, WFM, or SPEC. SPEC (spectrum/capture) mode uses the IQ capture baseband and shows signal power without audio demodulation. Cycling past WFM wraps to SPEC, cycling past SPEC wraps back to AM.
* **S (Step):** Frequency tuning step size for the encoder. A short list of standard step sizes from 100 Hz upward.

**Row 3 — frequency:**

* **Frequency button** (labelled ``): click to open the numeric keypad for direct entry. Use the rotary encoder while focused to step in the selected step size.
* The frequency persists from the last used receiver state.

**Row 3 (right) — audio:**

* **AUDIO:** `audio off` / `audio on` — enables or disables audio output. Audio is not available in SPEC mode even if set to on; in SPEC mode the beep function takes over instead when a signal is above the squelch level.

**Row 4 — squelch and display:**

* **Bip> / beep squelch field:** Threshold in dBm (−100 to +20) above which an audio beep is emitted. The beep pitch scales with signal strength: −100 dBm maps to 400 Hz, +20 dBm maps to 2600 Hz, duration 150 ms. The beep fires on every statistics update while the signal exceeds this threshold.
* **RSSI: min/avg/max** — current RSSI values from the scrolling graph.
* **peak:** Sets peak hold time for the right vertical RSSI bar — none, 0.25 s, 0.5 s, 1 s, 3 s, 5 s, or 10 s. Default: 0.5 s.
* **History columns:** Number of columns in the scrolling RSSI/power graph — 16, 32, 64, 128, or 240. Default: 32.

**Row 5:**

* **Power: X db** — peak channel power in dB (range −100 to +20).
* **RxSat: X%** — receiver saturation percentage (see below). Displayed with a colour gradient. Shows `RxSat off` in WFM+audio mode or SPEC mode where saturation measurement is not available.
* **CTCSS tone** — in NFM mode, the detected CTCSS/DCS sub-tone or code is shown to the right of RxSat if one is present on the received signal.

# Displays

## Right vertical level meter

A narrow vertical bar on the right edge of the screen:

* **Blue fill** — RSSI minimum
* **White horizontal bar** — RSSI average
* **Red fill** — RSSI maximum
* **Green marker** — peak hold (when peak hold is enabled and a peak has been captured)

## Scrolling history graph

The main graph area below row 5 shows four overlaid traces over a scrollable history:

* **Blue line** — RSSI minimum (clipped to RSSI range 31–170, scaled to graph height)
* **White line** — RSSI average (same range)
* **Red line** — RSSI maximum (same range)
* **Green line** — channel power in dB (clipped to −100 to +20 dB, scaled to graph height)

The number of visible history columns is set by the **history columns** selector.

## RxSat colour coding

The RxSat indicator uses a colour gradient to show how hard the receiver front-end is working:

| Range | Colour | Meaning |
|-------|--------|---------|
| 0–80% | Blue → green | Normal — increasing as signal strength grows |
| 80% | Green | Ideal operating point |
| 80–100% | Green → red | Overloading — reduce LNA/VGA gain |

RxSat is calculated from the M4 baseband performance counter. It is **not available** in SPEC mode or in WFM mode with audio enabled.

# Modulation modes

| Mode | Audio rate | Notes |
|------|-----------|-------|
| AM | 12 kHz | DSB default. BW selector changes AM configuration (DSB/USB/LSB/CW). |
| NFM | 24 kHz | 16 kHz bandwidth default. CTCSS/DCS detection active. |
| WFM | 48 kHz | 200 kHz bandwidth default. RxSat not shown when audio is on. |
| SPEC | 24 kHz | IQ capture mode. BW sets the baseband sampling rate. Beep squelch active. No audio. |

# Settings persistence

The beep squelch threshold, audio on/off state, modulation mode, and bandwidth selection are saved automatically and restored on next launch. Settings are stored in `SETTINGS/rx_level.ini` on the SD card.

The frequency is not saved in the app's own settings — it follows the global receiver frequency. scaled along the height of the RSSIGraph widget