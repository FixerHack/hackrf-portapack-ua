![image](https://github.com/user-attachments/assets/ca6b0359-6e42-4930-b2d0-cd0b0a183ee8)

FlipperTX transmits signals from Flipper Zero `.sub` capture files directly from the PortaPack. It reads the file's encoded protocol timing data and replays it over the air at the configured frequency using the modulation preset defined in the file itself.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# SD Card Setup

Place `.sub` files in the `SUBGHZ/` directory at the root of the SD card. The Browse button opens a file selector starting in this directory, filtered to `.sub` files.

# Supported File Formats

FlipperTX only supports a subset of the Flipper Zero `.sub` file format:

**Protocols:**

| Protocol | Support |
|----------|---------|
| `RAW` | ✅ Supported |
| `BinRAW` | ✅ Supported |
| All others | ❌ Not supported |

**Presets (modulation):**

| Preset | Modulation | Support |
|--------|-----------|---------|
| OOK | On-Off Keying | ✅ Supported |
| 2FSK | 2-level FSK | ✅ Supported |
| `Custom` or unknown | — | ❌ Not supported |

If the file uses an unsupported protocol or preset, the filename field shows an error message and transmission is blocked:

* `File: err, bad file` — file could not be parsed
* `File: err, not supp. proto` — protocol not RAW or BinRAW
* `File: err, not supp. preset` — preset not OOK or 2FSK

# Controls

* **Frequency**: Transmit frequency. Defaults to **433.920 MHz**. Must be set manually to match the frequency in the `.sub` file — the app does not read frequency from file metadata automatically.
* **Gain / AMP**: TX gain and RF amplifier toggle.
* **Browse**: Opens the file selector in `SUBGHZ/`. After a valid file is selected, the full path is shown in the filename field.
* **Start / Stop**: Begins or aborts transmission. The file is transmitted once and stops automatically at end of file. There is no loop mode.

# Transmission Parameters

These values are fixed and cannot be changed from the UI:

| Parameter | Value |
|-----------|-------|
| Sample rate | 2,280,000 Hz |
| Bandwidth | 1,750,000 Hz |
| FM deviation (2FSK only) | 60,000 Hz |

# Settings Persistence

Settings are saved to `tx_flippertx.ini`.