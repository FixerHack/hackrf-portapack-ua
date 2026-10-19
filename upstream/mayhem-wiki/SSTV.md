SSTV TX transmits Slow Scan Television images from `.BMP` files stored on the SD card. The signal is transmitted as FM audio tones in the standard SSTV frequency range (1,500–2,300 Hz).

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

* **File** — Selects the `.BMP` file to transmit from the `SSTV/` directory on the SD card.
* **Mode** — Selects the SSTV transmission mode. Default: Scottie 2.
* **Frequency, Gain, AMP** — Standard RF controls. Default gain: 12 dB.
* **▶** — Starts transmission. A progress bar shows the current scanline.

# Supported Modes

| Mode | VIS Code | Lines | µs/pixel |
|---|---|---|---|
| Scottie 1 | 60 | 256 | 432.0 |
| **Scottie 2** (default) | 56 | 256 | 275.2 |
| Scottie DX | 76 | 256 | 1080.0 |
| Martin 1 | 44 | 256 | 457.6 |
| Martin 2 | 40 | 256 | 228.8 |
| SC2-180 | 55 | 256 | 734.4 |

All modes transmit 320 pixels per line and 256 lines (320×256 total).

# Image Requirements

* Format: 24-bit uncompressed BMP (`.bmp`)
* Size: exactly **320×256 pixels**
* Location: `SSTV/` directory on the SD card

Images that do not match the required resolution will produce incorrect output.

# RF Parameters

| Parameter | Value |
|---|---|
| Sample rate | 3.072 MSps |
| Baseband bandwidth | 1.75 MHz (fixed) |
| Frequency step | 10 kHz |

# Settings Persistence

Settings are saved to `tx_sstv.ini`.