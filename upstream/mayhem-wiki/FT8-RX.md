<img width="240" height="314" alt="FT8 RX on 40 m" src="https://github.com/user-attachments/assets/87c42d6b-5321-4251-a34f-446ed75e4d1f" />

Receives and decodes FT8, the 15-second digital mode used on the HF amateur bands, and prints each decoded message with the audio frequency it was found on. The decoder is [ft8_lib](https://github.com/kgoba/ft8_lib) running on the baseband core. No time source is needed: the receiver finds the slot boundary from the signals on the band.

This is an [external app](External-apps-informations) and must be present on the SD card in the `APPS/` folder.

## Settings

* **Frequency**: The dial frequency, as WSJT-X shows it. Frequency step is 100 Hz.
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **RSSI / Channel**: Two bars. The upper one is the RF level in front of the demodulator. The lower one is the peak level in the channel filter and turns red at -3 dBFS, where the decoder starts losing signals. See [Gain](#gain).
* **Volume**: Audio output volume. The SSB audio the decoder listens to goes to the speaker or headphone output, so the band can be heard.
* **Band**: Presets for the standard FT8 dial frequencies, 160 m to 6 m: 1.840, 3.573, 5.357, 7.074, 10.136, 14.074, 18.100, 21.074, 24.915, 28.074 and 50.313 MHz. Tuning by hand to any other frequency shows `---`.

## Status Line

The second line shows the band, the state of the slot synchroniser and the number of messages decoded since the app was opened.

* **Searching** (red): nothing usable in the passband yet.
* **Heard, no decode** (yellow): an FT8 transmission is in the passband, but no message has passed its CRC yet. Usually the capture window is not aligned with the slot.
* **Syncing** (yellow): a message decoded, and the receiver is refining the window to a fraction of a symbol.
* **Locked** (green): the window follows the slot. Decodes now arrive every 15 seconds while the band is active.

A cold start walks the 15-second slot in four steps, so the first decode can take up to about two minutes. Two minutes of an empty band return the receiver to **Searching**.

## Decoded Text Area

One line per decoded message: the message text on the left and its audio frequency on the right. The frequency is the offset from the dial, 200–2500 Hz, which is where the station sits in the passband. Two stations on 7.074 MHz at 837 Hz and 1312 Hz are two signals, and WSJT-X lists them the same way.

Lines that start with `CQ` are green.

FT8 sends a callsign as a hash once both stations have exchanged it in full. A hashed callsign shows as `<...>` until the receiver has heard its owner, then as `<CALLSIGN>`. The receiver keeps the 32 most recent callsigns for this.

The console holds 17 lines. Older lines scroll off and are not kept; there is no log file.

## Gain

The receiver has no AGC, because the decoder needs linear amplitude. Too much gain flattens the waterfall the decoder builds, and messages that are plainly audible stop decoding. The lower bar under RSSI is the check: red means the input clips, and LNA or VGA should come down until it is blue again. On HF the bar reads well above half even at zero gain; red is the signal to act on.

## Signal Processing

The baseband runs at 3.072 MHz and decimates through 384 kHz, 48 kHz and 24 kHz to 12 kHz, demodulates SSB and feeds the audio to a bank of 368 Goertzel filters spaced 6.25 Hz apart across the passband, one FT8 tone per bin. Each of the 79 symbols is 1920 samples. The waterfall of one slot goes through Costas sync, LDPC decoding with 10 iterations and a CRC check; up to 10 messages come out of one slot.

The Goertzel bank takes almost all of the baseband core: the CPU counter reads about 99 %, and some sample buffers are dropped. A slot that loses samples decodes fewer messages than WSJT-X would on the same antenna.

## Settings Persistence

Frequency and gains are saved to `rx_ft8.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.
