# Introduction

Morse RX is a Morse code receiver that automatically detects and decodes incoming CW signals. Tune to the signal frequency and wait for clear audio — the app handles tone frequency detection, WPM estimation, and character decoding without manual configuration.

The decoder uses automatic tone and speed detection, which may take a few moments to lock onto a signal. Decoding quality depends heavily on signal clarity.

# Controls

**Top row:**

* **Frequency:** Click to open the numeric keypad, or use the rotary encoder for fine tuning.
* **AMP:** RF preamplifier — 0 = off, 1 = on (+14 dB). Avoid enabling near strong signals.
* **LNA:** Low Noise Amplifier gain (0–40 dB).
* **VGA:** Variable Gain Amplifier / baseband gain (0–62 dB).
* **Volume:** Audio output level.

**Second row:**

* **Squelch (0–99):** Sets the squelch level. Signals below this threshold are ignored. Adjust to suppress background noise without cutting off the desired signal.
* **Mode:** Selects the demodulation mode — `AM/CW`, `NFM`, `AM/DSB`, `AM/USB`, or `AM/LSB`. Use `AM/CW` for standard HF CW, `NFM` for VHF/UHF Morse beacons.
* **Speed: XX wpm:** Displays the estimated receive speed in words per minute. This is calculated automatically from the detected dit/dah timing. If decoding goes wrong the value will visibly adapt as the algorithm self-corrects.

**Third row:**

* **Log checkbox:** Enables logging to a daily file in the `LOGS/` directory on the SD card. Each log session is stamped with a timestamp header and the selected mode.
* **Tone: XXXX Hz:** Displays the detected audio tone frequency of the incoming Morse signal. The colour indicates whether the tone is in a good range for decoding:
  - **Green** — 580–1220 Hz: optimal range
  - **Yellow** — 400–580 Hz or 1220–1400 Hz: acceptable but at the edge
  - **Red** — below 400 Hz or above 1400 Hz: outside the reliable decoding range; results will be poor

**Fourth row:**

* **Last seq.:** Shows the most recently detected dit/dah pattern before it was decoded into a character, useful for debugging weak or noisy signals.

**Decoded text console:**

The large area in the lower half of the screen shows the decoded characters. The colour of each character indicates the decoder's confidence:

* **Green** — confidence ≥ 90%: high confidence
* **Yellow** — confidence 80–90%: moderate confidence
* **Red** — confidence < 80%: low confidence, likely incorrect
* **White** — spaces and unmatched sequences

**Bottom:**

* **CLR:** Clears the decoded text console.

# Tips for best results

The decoder requires a clean, steady audio tone in the 400–1400 Hz range. Before starting:

* Adjust frequency so the signal produces a clear audio tone — listen with the speaker enabled.
* Use a narrowband mode (`AM/CW` or `NFM`) and set gain so the signal is strong but not clipping (a `clipping` warning appears on screen if the input is saturated).
* Keep the scan range small and avoid strong nearby interferers.
* If the tone frequency display shows red and jumps around, there is too much noise or the wrong mode is selected.

# Settings persistence

The selected demodulation mode is saved automatically and restored on next launch. Settings are stored in `SETTINGS/rx_morse_radio.ini` on the SD card.