Spectrum Painter transmits an image or text in a way that makes it visible as a pattern on a waterfall display. The image or text is encoded as the instantaneous frequency of the signal over time, painting each row of pixels as a horizontal line in the spectrum.

The app has two tabs: **Image** and **Text**.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls (common to both tabs)

* **Frequency** — Center frequency of the transmission.
* **GAIN** — TX gain, 0–47 dB. Default: 47.
* **A:** — RF amplifier, 0 or 14 dB. Default: off (0).
* **Loop** (checkbox, default: on) — Repeats the transmission continuously. When active, the Pause field sets a gap between repetitions.
* **BW** — Transmission bandwidth. This determines how wide the painted spectrum appears. Options: 12k5, 16k, 25k, 32k, 50k, 75k, **100k** (good starting point), 150k, 250k, 500k, 600k, 750k, 1000k, 1250k, 1500k, 1750k, 2000k, 2250k, 2500k, 3000k. Default: 12k5. For visible results on a multi-MHz waterfall span, use at least 500k–2000k.
* **Du:** — Duration of each transmission in seconds (1–999). Default: 10.
* **P:** — Pause between transmissions in seconds when Loop is active (0–99). Default: 5.
* **▶ / ■** — Start or stop transmission. A progress bar shows the current position within the transmission.

The internal baseband bandwidth is fixed at 1.75 MHz regardless of the BW setting.

# Image Tab

Place `.BMP` files in the `SPECTRUM/` directory on the SD card. Press the file selector to choose a file — a scaled preview is shown on screen before transmission. The selected file is transmitted row by row, with each pixel row becoming one horizontal line in the spectrum.

**Supported formats:** 16-bit, 24-bit, and 32-bit uncompressed BMP (no compression, single plane). All three bit depths are fully supported.

For best results, use a high horizontal resolution. A width of 2048 pixels works well. Using a power of 2 for the width (512, 1024, 2048, …) gives optimal results.


![SCR_0000](https://github.com/portapack-mayhem/mayhem-firmware/assets/13151053/4f3ecb71-eb8f-4231-a0a5-21f593c43b8b)

![grafik](https://github.com/portapack-mayhem/mayhem-firmware/assets/13151053/0facc180-5474-4093-98a9-a983f8b93f43)

# Text Tab

Enter text using the **Set message** button (opens the keyboard). The message is displayed across up to 10 lines of 30 characters each on screen. Maximum message length is 300 characters.

![SCR_0003](https://github.com/portapack-mayhem/mayhem-firmware/assets/13151053/3ea539e7-baf7-4a77-8415-3aabe9bc6cea)

![Screenshot](https://github.com/portapack-mayhem/mayhem-firmware/assets/13151053/9b322883-6064-4b77-9a40-dcdf9098ee06)

# Settings Persistence

Settings are saved to `tx_painter.ini`.