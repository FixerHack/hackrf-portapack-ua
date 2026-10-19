# Automatic Packet Reporting System

> [!NOTE]
> This is an [external app](External-apps-informations) and must be present on the SD card in the `APPS/` folder.

![image](https://github.com/user-attachments/assets/78607967-ed3b-455d-9c0c-87af5b171dc9)

The APRS RX app receives and displays messages transmitted using the APRS (Automatic Packet Reporting System) protocol. It shows a live list of received stations including callsign, position (if available), hit count, and last received time.

## Pre-configured Regions

Select a region to automatically tune to the correct APRS frequency for that area:

| Code | Frequency | Region |
|------|-----------|--------|
| MAN | user-defined | Manual — frequency set manually |
| NA | 144.390 MHz | North America |
| NZ | 144.575 MHz | New Zealand |
| JAP | 144.640 MHz | Japan |
| PHI | 144.740 MHz | Philippines |
| EUR | 144.800 MHz | Europe / UK |
| THA | 144.900 MHz | Thailand |
| AUS | 145.175 MHz | Australia |
| BR | 145.570 MHz | Brazil |
| ISS | 145.825 MHz | International Space Station |

When a region is selected, the frequency field updates automatically. If you change the frequency manually afterwards, the region selector switches to **MAN**.

Frequencies not in the preset list can be tuned manually (MAN), for example **432.500 MHz** (Europe, UHF).

## Controls

### Frequency

- Use the rotary encoder over the frequency field to adjust in steps
- Press the middle button over the frequency field to enter a frequency manually via keypad
- Load a frequency from SD card using the frequency manager

### Radio Settings

From left to right:

- **AMP** — RF amplifier: `0` = off, `1` = on (+14 dB). Enable if signal is weak.
- **LNA** — IF gain (0–40 dB in 8 dB steps)
- **VGA** — Baseband gain (0–62 dB in 2 dB steps)

See [Description of gain settings](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Main-Controls) for more details.

### Volume

Audio volume is shown after the signal strength bars. Use the rotary encoder when focused on it.

## Station List

The main screen shows a list of recently received APRS stations with the following columns:

| Column | Description |
|--------|-------------|
| Source | Callsign of the transmitting station (with SSID if present) |
| Location | GPS coordinates if the packet contained a position report |
| Hits | Number of times this station has been received |
| Time | Time of last received packet |

Tap or select an entry to open the **Detail View**.

## Detail View

Selecting a station from the list opens a detail screen showing the full decoded APRS packet information including the raw info field content. Two buttons are available:

- **Done** — return to the station list
- **See Map** — opens the map view centered on the station's position. This button is only visible if the station transmitted a valid GPS position.

## Logging

Received packets are automatically logged to the SD card at:

```
LOGS/APRS.TXT
```

Each line contains the raw decoded APRS stream data. Logging is active as long as the app is running and a writable SD card is present.

## Important Notes

- APRS RX on the HackRF is relatively insensitive. Enable **AMP** if you are not receiving stations that are clearly audible on a dedicated receiver.

⚠️ Be careful not to connect strong signals directly — the HackRF has no input protection.

- Some stations transmit with a bandwidth wider than the default 8.5 kHz. If you are missing packets, increase the reception bandwidth by editing the settings file on the SD card:
  1. Navigate to `SETTINGS/rx_aprs.ini` using the File Manager app
  2. Select the file, press down to select the pen icon, press OK
  3. Find the line starting with `nbfm_config_index` and change the value:
     - `0` = 8.5 kHz (default)
     - `1` = 11 kHz
     - `2` = 16 kHz

## Protocol

APRS is transported over **AX.25** using a **Bell 202** modem at **1200 bit/s** (AFSK): a **1200 Hz** tone for *mark* (binary 1) and **2200 Hz** for *space* (binary 0).

## SSID (Secondary Station ID)

The SSID is a numeric suffix added to a callsign to tell apart multiple stations under one call. APRS allows 16 SSIDs (0–15); the commonly recommended meanings:

| SSID | Typical use |
|------|-------------|
| 0 | Primary station, usually fixed and message-capable |
| 1–4 | Generic additional station (digi, mobile, wx, etc.) |
| 5 | Other networks (D-STAR, smartphones, etc.) |
| 6 | Special activity, satellite ops, etc. |
| 7 | Handheld transceivers / human-portable |
| 8 | Boats, sailboats, RVs, or second main mobile |
| 9 | Mobiles or trackers |
| 10 | Internet, iGates, Echolink, Winlink, AVRS, APRN, etc. |
| 11 | Balloons, aircraft, spacecraft, etc. |
| 12 | APRStt, DTMF, RFID devices, one-way trackers, etc. |
| 13 | Weather stations |
| 14 | Truckers / full-time drivers |
| 15 | Generic additional station (digi, mobile, wx, etc.) |

## Further Reading

- [APRS TX](https://github.com/portapack-mayhem/mayhem-firmware/wiki/APRS-TX) — transmit APRS packets
- [APRS Protocol Reference Manual](http://www.aprs.org/doc/APRS101.PDF)
- [aprs.fi — Live APRS map](https://aprs.fi)