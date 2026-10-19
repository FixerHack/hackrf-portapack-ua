# HackRF Hardware

The HackRF is the SDR board that the PortaPack connects to. Multiple versions are supported by Mayhem.

## HackRF One (R1–R9)

The HackRF One is the original board created by Michael Ossmann at Great Scott Gadgets. It has been manufactured in multiple hardware revisions (R1 through R9), all fully supported by Mayhem.

| Specification | Value |
|---|---|
| Transceiver | Half-duplex |
| Operating frequency | 1 MHz to 6 GHz |
| Sample rates | 2 to 20 Msps (quadrature) |
| Resolution | 8 bits |
| Max RX power | −5 dBm (exceeding this risks permanent damage; up to 10 dBm is safe with the RX amp disabled) |
| USB | High-Speed USB 2.0, Type-A or Micro-B |

### Max TX power (HackRF One)

| Frequency range | Approximate TX power |
|---|---|
| 10 – 2150 MHz | 5 to 15 dBm (increases as frequency decreases) |
| 2150 – 2750 MHz | 13 to 15 dBm |
| 2750 – 4000 MHz | 0 to 5 dBm (increases as frequency decreases) |
| 4000 – 6000 MHz | −10 to 0 dBm (increases as frequency decreases) |

For measured values see: [empirical TX power measurement](https://www.reddit.com/r/hackrf/comments/hi8275/measurement_of_the_hackrf_one_output_power/)

### CLKout / CLKin (HackRF One)

| Hardware revision | Behaviour |
|---|---|
| R1–R8 (OG, Si5351C) | User-configurable 4 kHz–60 MHz via Settings → Radio |
| R9 (Si5351A) | Fixed 10 MHz, software-gated on/off only |

Signal level is 0 V to 3 V into a high-impedance load (square wave).

---

## HackRF One R10C

The R10C is a HackRF One variant manufactured by OpenSourceSDRLab, sold bundled with the H4M PortaPack. It uses the same chipset and hardware architecture as the R9 (Si5351A clock generator) and is treated identically by the Mayhem firmware. The only hardware difference from R9 is the **USB-C connector** instead of Micro-B.

| Specification | Value |
|---|---|
| Based on | HackRF One R9 |
| USB | High-Speed USB 2.0, **Type-C** |
| CLKout | Fixed 10 MHz (same as R9) |
| Firmware compatibility | Full Mayhem support (detected as R9) |

> [!NOTE]
> Despite the "R10" in its name, the R10C is not related to the HackRF Pro. It is a HackRF One with a USB-C connector, manufactured by a third party.

---

## HackRF Pro

The HackRF Pro was announced by Great Scott Gadgets on 26 June 2025. It is a major upgrade of the HackRF One while maintaining backward compatibility. Mayhem supports it via the PRALINE build target.

| Specification | Value |
|---|---|
| Transceiver | Half-duplex |
| Operating frequency | 100 kHz to 6 GHz |
| Tunable range | 0 Hz to 7.1 GHz |
| Sample rates | Up to 20 Msps (standard); up to 40 Msps (4-bit half-precision) |
| Resolution | 8-bit standard; 16-bit extended precision at low sample rates (typical ENOB 9–11); 4-bit half-precision |
| Clock reference | Built-in TCXO (no GP_CLKIN dependency) |
| Logic | iCE40 FPGA (replaces the CPLD of HackRF One) |
| USB | High-Speed USB 2.0, Type-C |

### CLKout / CLKin (HackRF Pro)

User-configurable 4 kHz–60 MHz via Settings → Radio (same range as HackRF One R1–R8).

---

# PortaPack Hardware

The PortaPack is an add-on board that attaches to the HackRF and provides a standalone user interface. Multiple versions exist. For a full comparison see [PortaPack Versions](PortaPack-Versions).

| Feature | Details |
|---|---|
| Display | 320 × 240 px color LCD (ILI9341), 2.4" (H1) or 3.2" (H2/H4M) |
| Touchscreen | Resistive touch, configurable threshold |
| Controls | Encoder dial + 5 directional buttons (up/down/left/right/select) |
| Storage | microSD card slot (FAT32) |
| Audio out | 3.5 mm headphone/speaker jack |
| Microphone | Built-in (H2M, H4M only) |
| Battery management IC | Yes (H4M only) |
| GPIO port | Expansion header (H4M only) |
| GPS | External GPS module supported (NMEA over UART) |

---

# Mayhem Firmware

Mayhem is a community firmware for HackRF + PortaPack that greatly extends the capabilities of the Havoc firmware it was forked from.

## App categories

| Category | Description |
|---|---|
| [Receivers](Receivers) | Decode and display signals: ADS-B, AIS, APRS, POCSAG, ACARS, EPIRB, and many more |
| [Transmitters](Transmitters) | Transmit a wide range of signals and protocols |
| [Transceivers](Transceivers) | Full send/receive apps: Microphone, KISS TNC |
| [Recon](Recon) | Frequency scanner and signal hunter |
| [Capture](Capture) | Record IQ data to microSD as .C16 or .C8 |
| [Replay](Replay) | Play back captured IQ files |
| [Remote](Remote) | Remote control via USB |
| [Looking Glass](Looking-Glass) | Wideband spectrum overview |
| [Utilities](Utilities) | Tools: antenna calculator, file manager, IQ trim, notepad, and more |
| [Settings](Settings) | Device configuration, radio parameters, display, themes |
| [Games](Games) | Included games: Tetris, Doom, Pac-Man, and more |
| [Debug](Debug) | Hardware diagnostics and developer tools |
| [External Apps](External-apps-informations) | Loadable .ppma apps from the SD card |

## Key firmware features

- **External apps**: Load additional apps from the SD card without reflashing
- **Screenshots**: Capture the display to a PNG file on the SD card
- **Stealth mode**: Disable backlight during TX
- **Sleep mode**: Turn off display while keeping radio running
- **Custom splash screen**: Load a user-supplied BMP image on boot
- **Themes**: Multiple color themes for the UI
- **GPS integration**: Apps can use position data from an attached GPS module
- **App Settings persistence**: Per-app settings saved to SD card
- **Frequency manager**: Store and recall named frequencies
- **Playlist/Replay editor**: Sequence multiple captures for playback

## Notes

- Half-duplex means the device can transmit or receive, but not both simultaneously.
- The operating frequency range (1 MHz–6 GHz for HackRF One) covers most common radio services. See [Wikipedia: Frequency allocation](https://en.wikipedia.org/wiki/Frequency_allocation) for a detailed breakdown.
- Always consult [Intended Use and Legality](Intended-Use-and-Legality) and your local regulations before transmitting.
