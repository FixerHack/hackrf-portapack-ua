> **Before you transmit, know your local laws. HackRF One has not been tested for compliance with regulations governing the transmission of radio signals. You are responsible for using your HackRF One legally.**

Transmitter apps generate and broadcast RF signals. The list below covers all transmitter apps currently in Mayhem.

## Transmitter Apps

| App | Description |
|-----|-------------|
| [2-Tone-TX](2-Tone-TX) | Transmits a Motorola / QCII style two-tone page with configurable Tone A, Tone B |
| [ADS-B(S) TX](ADS-B(S)) | Transmits ADS-B Mode S aircraft transponder frames — for simulation and testing only |
| [Adult Toys](Adult-Toys) | Transmits BLE control packets compatible with Love Spouse brand Bluetooth devices |
| [APRS TX](APRS-TX) | Transmits APRS position reports and messages using Bell 202 AFSK at 1200 baud |
| [BHT Xy/EP](BHT) | Transmits BHT streetlight management protocol (Xylos and EPAR variants) |
| [BLE TX](Bluetooth-Low-Energy-Transmitter) | Transmits Bluetooth Low Energy 2.4 GHz advertisement packets |
| [BLESpam](BLESpam) | Transmits spoofed BLE advertisement packets (Apple, Google, Samsung pairing popups) |
| [Burger Pager](Burger-Pager) | Transmits signals for restaurant guest pager systems |
| [CVS Spam](CVS-Spam) | Transmits CVS pharmacy pager / call system signals |
| [EPIRB TX](EPIRB-TX) | Transmits 406 MHz EPIRB distress beacon test signals |
| [Flex TX](FLEX-TX) | Transmits FLEX paging protocol messages (1600 / 3200 / 6400 baud) |
| [FlipperTX](FlipperTX) | Transmits sub-GHz signals from Flipper Zero `.sub` capture files |
| [GPS Sim](GPS-Sim) | Transmits a simulated GPS L1 C/A signal to spoof GPS receiver position |
| [Hopper](Hopper) | Frequency hopper: transmits a carrier that sweeps across a configurable frequency list |
| [Jammer](Jammer) | Transmits noise across a frequency range to disrupt communications — use responsibly and legally |
| [KeeLoq TX](KeeLoq-TX) | Retransmits KeeLoq rolling-code signals loaded from `.keeloq` capture files |
| [Key fob TX](Key-fob-TX) | Transmits fixed-code remote keyless entry signals (currently Subaru only) |
| [LGE Tool](LGE-Tool) | Transmits LG Electronics service signals |
| [MDC 1200 TX](MDC-1200-TX) | Transmits MDC-1200 ANI/PTT ID bursts used in analogue radio systems |
| [Morse TX](Morse-TX) | Encodes text to Morse code (CW) and transmits it as a keyed carrier |
| [OOK](OOK) | Transmits raw On-Off Keying (OOK/ASK) patterns for sub-GHz remote control signals |
| [OOK Brute](OOK-Brute) | Sequentially brute-forces OOK remote control code spaces (CAME, Nice, Holtek, Princeton) |
| [OOK Editor](OOK-Editor) | Graphical editor for composing and transmitting custom OOK bit patterns |
| [P25 TX](P25-Tx) | Transmits Project 25 (APCO P25) Phase 1 FDMA digital voice frames |
| [POCSAG TX](POCSAG-Tx) | Transmits POCSAG pager messages (numeric and alphanumeric) at 512 / 1200 / 2400 baud |
| [RDS](RDS) | Transmits Radio Data System (RDS) data embedded in an FM carrier |
| [RTTY TX](RTTY-TX) | Transmits RTTY (Baudot/ITA2) text at standard baud rates |
| [SAME TX](SAME-TX) | Transmits Specific Area Message Encoding (SAME/EAS) emergency alert headers |
| [Security+ TX](Security-Plus-TX) | Transmits Security+ 2.0 rolling-code signals for Chamberlain, LiftMaster, and Craftsman garage door openers at 315 MHz |
| [Signal gen](Signal-Generator) | Generates a carrier with optional FM modulation (CW, tones, sweep, noise); also available under Utilities |
| [Soundboard](Soundboard) | Transmits FM-modulated audio from `.WAV` files stored on the SD card |
| [Spectrum Painter](Spectrum-Painter) | Transmits a signal whose spectrogram draws an image visible on a spectrum analyser |
| [SSTV](SSTV) | Transmits Slow Scan Television (SSTV) image transmissions (Scottie, Martin modes) |
| [TEDI/LCR](LCR) | Transmits TEDI/LCR train identification and signalling protocol messages |
| [TouchTunes](TouchTunes) | Transmits TouchTunes jukebox IR-over-RF remote control signals |
| [TPMS TX](TPMS-TX) | Transmits simulated TPMS tyre pressure sensor signals at 315 / 433.9 MHz |
| [VOR TX](VOR-TX) | Transmits a simulated VOR aviation navigation beacon for a user-programmable radial (DSB-AM + 9960 Hz subcarrier + optional Morse ID) |

## HackRF Transmit Power

HackRF One output power varies significantly across its frequency range:

| Frequency range | Approximate TX power |
|-----------------|----------------------|
| 1 MHz – 10 MHz | 5 to 15 dBm, increasing with frequency |
| 10 MHz – 2150 MHz | 5 to 15 dBm, decreasing with frequency |
| 2150 MHz – 2750 MHz | 13 to 15 dBm (best performance region) |
| 2750 MHz – 4000 MHz | 0 to 5 dBm, decreasing with frequency |
| 4000 MHz – 6000 MHz | −10 to 0 dBm, decreasing with frequency |

Through most of the range below 4 GHz the output power falls between 0 and 10 dBm. The 2150–2750 MHz band delivers the highest and most consistent output.

## TX Gain Controls

HackRF provides two TX gain stages: the **LNA (IF) gain** (0 to 47 dB in 1 dB steps) and the **RF amplifier** (0 dB or 14 dB). Both are adjustable in Mayhem's transmitter apps via the Amp and LNA fields.

The output power is sufficient for close-range over-the-air experiments and for driving an external power amplifier. If you add an external amplifier, also add an external bandpass filter matched to your operating frequency — HackRF has no built-in filtering and will otherwise radiate harmonics and spurious emissions.