> [!WARNING]
> This application is intended solely for experimental and educational purposes. Broadcasting GPS signals may be illegal in your jurisdiction and can interfere with navigation systems. You are solely responsible for ensuring compliance with all applicable laws before use.

GPS Sim replays pre-generated GPS baseband signal files (`.C8` format) to simulate GPS satellite signals. It can be used to feed a fixed or moving position to GPS receivers for testing and research.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# SD Card Setup

Place `.C8` data files and their corresponding `.TXT` metadata files in the `GPS/` directory at the root of the SD card. Both files must share the same base name (e.g. `gpssim.C8` and `gpssim.TXT`).

When a `.C8` file is opened, the app automatically reads the matching `.TXT` file and sets the transmit frequency and sample rate accordingly.

# Metadata File Format

Create a `.TXT` file with the same name as the `.C8` file containing:

```
center_frequency=1575420000
sample_rate=SAMPLE_RATE
```

`center_frequency` is the GPS L1 carrier frequency and should always be `1575420000`. If the metadata file is missing, or if either value is zero, the app falls back to its defaults (1575.420 MHz, 2,600,000 Hz sample rate).

Known working sample rate values:

* `2600000`
* `2500000`
* `1250000`

# Generating C8 Files

Use the `gps-sdr-sim` tool to generate `.C8` files. It requires a RINEX navigation file (GPS ephemeris data) as input.

**Fixed position:**
```
gps-sdr-sim -e BRDC_FILE.n -l LAT,LON,HEIGHT -b 8 -s 2600000 -o gpssim.C8
```

**Moving position from NMEA file:**
```
gps-sdr-sim -e BRDC_FILE.n -g NMEA_FILE.txt -b 8 -o gpssim.C8
```

RINEX navigation files (`.n` / `.20n` etc.) can be downloaded from public GNSS data archives such as NASA CDDIS or IGS. Use the file dated closest to your intended simulation date.

**Example metadata file for the above:**
```
center_frequency=1575420000
sample_rate=2600000
```

# Controls

* **Open file**: Opens a file browser in `GPS/`, filtered to `.C8` files. After selection, the filename, sample rate, and estimated duration are shown.
* **Frequency / Gain / AMP**: Transmit frequency, gain, and RF amplifier. Automatically set from the `.TXT` file when a capture is loaded.
* **Loop** (checkbox, default: on): When enabled, the file restarts automatically at end of file and transmits continuously.
* **▶ / ■**: Start or stop transmission.

The progress bar shows playback position through the file. A live waterfall is displayed during transmission.

# Default Transmission Parameters

| Parameter | Default value |
|-----------|--------------|
| Frequency | 1,575.420 MHz (GPS L1) |
| Bandwidth | 15,000,000 Hz |
| Sample rate | 2,600,000 Hz (overridden by .TXT file) |

# Improving Reception on Target Devices

Modern devices use multiple positioning sources and may reject spoofed GPS. To improve the chance of a lock:

* Enable airplane mode (disables Wi-Fi, Bluetooth, and cellular assisted positioning)
* Test indoors where real GPS signal is weak
* Reboot the device after enabling airplane mode

# Known Device Results

> [!NOTE]
> Newer devices increasingly use sensor fusion and network-based positioning. Results may vary by firmware version.

| Type | Make | Model | Locks on spoofed GPS? | GPS acts "jammed"? | Notes |
|------|------|-------|----------------------|-------------------|-------|
| Tablet | Samsung | Note 7 | No | Yes | |
| Phone | Samsung | S8 | Yes | No | Wi-Fi must be off |
| Phone | Huawei | P30 lite | No | Yes | |
| Phone | Huawei | Mate 10 Pro | No | No | 6–7 satellites: no fix |
| Smartwatch | Huawei | Amazfit Bip | Yes | No | |
| Phone | Apple | iPhone 6 | Yes | No | Works with Wi-Fi on |
| Phone | ZTE | Axon 7 | Yes | No | Works with Wi-Fi on |
| Phone | Xiaomi | Mi5 | Yes | No | Works with Wi-Fi on |
| Phone | Samsung | S20+ 4G | Yes | No | Wi-Fi must be off |
| Smartwatch | Samsung | Gear S3 WiFi | Yes | No | Location over GPS only |
| Phone | OnePlus | 7 Pro | No | No | No effect observed |
| Phone | OnePlus | 5 | Yes | No | 3D fix |
| Phone | Samsung | S21 Ultra | Yes | No | |

# Settings Persistence

Settings are saved to `tx_gps.ini`.