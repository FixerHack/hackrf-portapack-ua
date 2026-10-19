# WMBus RX

Receives and decodes **Wireless M-Bus** (wM-Bus) telemetry from utility meters — water, gas, heat and electricity meters that report over radio in the 868 MHz band.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Overview

Wireless M-Bus (EN 13757) is the European standard that smart utility meters use to transmit consumption and status data by radio. The app receives these packets, validates each one with the wM-Bus CRC, and decodes the meter's identity and — for unencrypted frames — the reported values.

Select the **mode** that matches the meter, tune to the matching frequency, and received packets appear in the console.

| Mode | Frequency | Notes |
|---|---|---|
| **T-Mode** | 868.95 MHz | 3-of-6 chip coding (default mode) |
| **C-Mode** | 868.95 MHz | compact mode |
| **S-Mode** | 868.3 MHz | slower, stationary mode |

> The app does not retune automatically — set the frequency field to the frequency shown above for the selected mode.

## Controls

| Control | Description |
|---|---|
| **Mode** | wM-Bus mode: T / C / S (see table above). |
| **Frequency** | Tune to the mode's frequency (10 kHz steps). |
| **RF Amp** | RF amplifier: `0` = off, `1` = on (+14 dB). |
| **LNA** | IF gain (0–40 dB). See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings). |
| **VGA** | Baseband gain (0–62 dB). |
| RSSI / Channel | Signal strength and channel power meters. |
| **Last Err** | Reason the last frame was rejected (CRC fail, length error, coding error …) or `None`. |

## Decoded fields

For each valid packet the console shows:

| Field | Meaning |
|---|---|
| **Mfr** | Manufacturer — 3-letter flag code decoded from the meter header |
| **ID** | Meter serial number (hex) |
| **Ver** | Device version byte |
| **Type** | Device / medium type — e.g. Water, Cold water, Hot water, Gas, Electricity, Heat, Heat cost allocator, Smoke detector |
| **CI / Enc** | Control-information byte and encryption status: `None`, `AES-128`, `DES` or `Mode n` |
| **V:** | Up to three decoded data values (shown only for unencrypted frames) |
| **Hex** | Raw hex dump of the frame |

Encrypted frames (AES-128 / DES) are identified but their values cannot be read without the key.

## Protocol

Wireless M-Bus (EN 13757-4) operates in the 868 MHz short-range band using FSK. **T-Mode** uses 3-of-6 chip coding, **C-Mode** is the newer compact mode, and **S-Mode** is the slower stationary mode. Each frame is verified with the wM-Bus CRC (polynomial `0x3D65`) before it is decoded.

## See also

- [ERT](ERT) — decodes North-American (ERT / IDM / SCM) utility-meter telemetry