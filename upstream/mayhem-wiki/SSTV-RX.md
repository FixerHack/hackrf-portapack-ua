<img width="239" height="321" alt="image" src="https://github.com/user-attachments/assets/24763486-fbc5-43d4-b212-30899861ae7b" />

Receives and decodes Slow Scan Television (SSTV) transmissions, displaying the incoming image in real time and saving it as a BMP file to the SD card.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Settings

* **Frequency**: The frequency to receive on. Adjustable via the encoder knob or on-screen numpad.
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **Volume**: Audio output volume.
* **Mode**: Selects the SSTV transmission mode. Default is **Scottie 2**. The six supported modes are:

| Mode | VIS Code | Pixels | Lines | ms/pixel |
|------|----------|--------|-------|----------|
| Scottie 1 | 60 | 320 | 256 | 0.432 |
| Scottie 2 | 56 | 320 | 256 | 0.275 |
| Scottie DX | 76 | 320 | 256 | 1.080 |
| Martin 1 | 44 | 320 | 256 | 0.458 |
| Martin 2 | 40 | 320 | 256 | 0.229 |
| SC2-180 | 55 | 320 | 256 | 0.734 |

* **Ph** (Phase, −50 to +50): Horizontal pixel offset to correct line start alignment. Adjust if the image has a horizontal shift or color misalignment. Applied immediately while receiving. Not saved between sessions.
* **Slnt** (Slant, −100 to +100): Timing drift correction in 0.1% steps. Adjust if the image appears diagonally tilted. Applied immediately while receiving. Not saved between sessions.

# Calibration Display

A **Calib** text field below the Mode selector shows sync detection status during reception — sync count and suggested phase/slant corrections are displayed here as they are computed from the incoming signal.

# Image Display

The received image is drawn line by line onto the screen in real time, scaled to fit the available display area below the controls. The internal image resolution is always 320 × 256 pixels regardless of screen scaling.

# Start / Stop

Press **Start RX** to begin reception. The button label changes to **Stop RX** while active. Each time Start RX is pressed, a new timestamped BMP file is created on the SD card. When Stop RX is pressed (or the app is closed), the current file is finalized and closed.

Images are saved to: `SSTV/RX/SSTV_YYYYMMDD_HHMMSS.BMP`

# Modulation Note

This app decodes SSTV signals transmitted using **FM modulation** only. SSB (USB/LSB) SSTV, which is the norm on HF amateur radio, is not supported. FM SSTV is used on VHF/UHF (e.g., 144.500 MHz in Europe) and via certain satellite downlinks.