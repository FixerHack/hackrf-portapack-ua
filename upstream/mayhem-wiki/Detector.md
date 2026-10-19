![image](https://github.com/user-attachments/assets/02253903-2099-44c2-8b58-1f2cfce76af5)

# Introduction

The Detector app is based on the Level app and allows quick signal detection across preset frequency lists for LoRa, remote controls, and TETRA uplink. It scans through all frequencies in the selected preset automatically, and produces an audible beep whenever a signal exceeds the configured threshold.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

## First line — Gain and Volume

- **LNA** — IF gain (0–40 dB). Adjust with rotary encoder when focused.
- **VGA** — Baseband gain (0–62 dB). Adjust with rotary encoder when focused.
- **AMP** — RF amplifier: `0` = off, `1` = on (+14 dB).
- **VOL** — Beep volume (0–99).

## Second line — Preset selection

Select the signal type to monitor:

| Preset | Frequency range | Description |
|--------|----------------|-------------|
| TETRA UP | 380–390 MHz | TETRA uplink band (emergency services, Europe) |
| Lora | 433, 868, 915 MHz | LoRaWAN EU433, EU868 and US915 bands |
| Remotes | 315, 433.92 MHz | Common remote control and key fob frequencies |

The current frequency being scanned is displayed on the right side of this line.

## Third line — Beep threshold and signal display

- **Bip** — Detection threshold in dBm (-100 to +20). When the received signal power exceeds this value, a beep is triggered. Lower values = more sensitive. The beep pitch scales with signal strength: a weak signal at threshold produces a 400 Hz tone, a maximum strength signal (+20 dBm) produces a 2600 Hz tone. Beep duration is 150 ms.
- **RSSI: min/avg/max** — Raw RSSI values (min/average/max) from the RSSI graph over recent history.
- **Power: -XX db** — Current received signal power in dBm.

# How scanning works

The app cycles through all frequencies in the selected preset on every display frame (~16 ms per frequency step). Each scan window has a bandwidth of **750 kHz**. If the signal level on any frequency exceeds the threshold during its scan window, a beep is produced.

# Signal display

The main area shows two displays:
- **RSSI graph** — scrolling history of min/avg/max RSSI values and signal power
- **RSSI bar** — current instantaneous RSSI level on the right side

# Preset frequencies

## Remotes

| Center frequency | Coverage |
|-----------------|----------|
| 315.000 MHz | 314.625 – 315.375 MHz |
| 433.920 MHz | 433.545 – 434.295 MHz |

## LoRa

| Center frequency | Coverage | Band |
|-----------------|----------|------|
| 433.375 MHz | 433.000 – 433.750 MHz | EU433 |
| 434.125 MHz | 433.750 – 434.500 MHz | EU433 |
| 434.875 MHz | 434.500 – 435.250 MHz | EU433 |
| 867.375 MHz | 867.000 – 867.750 MHz | EU868 |
| 868.125 MHz | 867.750 – 868.500 MHz | EU868 |
| 868.875 MHz | 868.500 – 869.250 MHz | EU868 |
| 914.250 MHz | 913.875 – 914.625 MHz | US915 |
| 915.000 MHz | 914.625 – 915.375 MHz | US915 |
| 915.750 MHz | 915.375 – 916.125 MHz | US915 |

## TETRA Uplink

| Center frequency | Coverage |
|-----------------|----------|
| 380.375 MHz | 380.000 – 380.750 MHz |
| 381.125 MHz | 380.750 – 381.500 MHz |
| 381.875 MHz | 381.500 – 382.250 MHz |
| 382.625 MHz | 382.250 – 383.000 MHz |
| 383.375 MHz | 383.000 – 383.750 MHz |
| 384.125 MHz | 383.750 – 384.500 MHz |
| 384.875 MHz | 384.500 – 385.250 MHz |
| 385.625 MHz | 385.250 – 386.000 MHz |
| 386.375 MHz | 386.000 – 386.750 MHz |
| 387.125 MHz | 386.750 – 387.500 MHz |
| 387.875 MHz | 387.500 – 388.250 MHz |
| 388.625 MHz | 388.250 – 389.000 MHz |
| 389.375 MHz | 389.000 – 389.750 MHz |
| 390.125 MHz | 389.750 – 390.500 MHz |

# Settings

The beep threshold is saved automatically to `SETTINGS/rx_detector.ini` on the SD card when the app is closed (requires Load App Settings to be enabled in the Settings menu).