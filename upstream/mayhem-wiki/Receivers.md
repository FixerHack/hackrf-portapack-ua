Receiver apps decode, display, or log radio signals. The list below covers all receiver apps currently in Mayhem. For signal quality and gain guidance that applies to all receiver apps, see [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues).

## Receiver Apps

| App | Description |
|-----|-------------|
| [2-Tone-RX](2-Tone-RX) | Decodes Motorola/QCII style 2-tone paging frequencies. |
| [ACARS](ACARS) | Decodes ACARS aircraft data link messages on VHF (default 131.825 MHz): registration, flight ID, label, and free-text payload |
| [ADS-B](Automatic-dependent-surveillance–broadcast-(ADS-B)) | Decodes 1090 MHz ADS-B aircraft transponder broadcasts: callsign, position, altitude, speed |
| [AFSK](AFSK) | Decodes Audio Frequency Shift Keying (Bell 202 / 1200 baud) — used for APRS and similar packet radio |
| [AIS Boats](AIS-Boats) | Decodes Automatic Identification System (AIS) maritime vessel traffic on 161.975 / 162.025 MHz |
| [Analog TV](Analog-TV-Receiver) | Receives analogue television video (PAL/NTSC) |
| [APRS RX](APRS-RX) | Decodes APRS position reports and messages on 144.800 MHz (EU) / 144.390 MHz (US) |
| [Audio](Audio-Receivers) | General-purpose audio receiver: AM, NFM, WFM, DSB, LSB, USB |
| [BLE RX](Bluetooth-Low-Energy-Receiver) | Scans and decodes Bluetooth Low Energy 2.4 GHz advertisement packets |
| [Detector](Detector) | Wideband signal presence detector with configurable squelch |
| [EPIRB RX](EPIRB-RX) | Decodes 406 MHz distress beacon transmissions (EPIRB, PLB, ELT) with BCH error correction and map display |
| [ERT Meter](ERT) | Decodes Encoder Receiver Transmitter (ERT) utility meter transmissions (IDM/SCM) |
| [Flex RX](Flex-Rx) | Decodes FLEX paging protocol (1600 / 3200 / 6400 baud) |
| [Fox Hunt](Fox-Hunt) | Signal direction-finding aid: displays received signal level for manual fox-hunting / RDF |
| [FPV Detect](FPV-Detect) | Detects FPV drone video transmitters in the 5.8 GHz band |
| [FT8 RX](FT8-RX) | Decodes FT8 on the HF bands: callsigns, grid locators and reports, with the audio frequency of each decode |
| [gfxEQ](gfxEQ) | Graphic equaliser-style spectrum display for audio signals |
| [Level](Level) | Simple RSSI level meter for measuring received signal strength at a given frequency |
| [Looking Glass](Looking-Glass) | Wideband spectrum sweep: scans up to several hundred MHz and displays a waterfall |
| [Meteor LRPT](Meteor) | Decodes Meteor-M2 series weather satellite LRPT image transmissions near 137 MHz (external app) |
| [Morse RX](Morse-RX) | Decodes Morse code (CW) to text |
| [NOAA](NOAA) | Receives NOAA weather satellite APT audio for image reconstruction |
| [NRF](decoder-for-NRF24L01) | Decodes 2.4 GHz nRF24L01 wireless packets |
| [POCSAG](POCSAG-Receiver) | Decodes POCSAG numeric and alphanumeric pager messages (512 / 1200 / 2400 baud) |
| [ProtoView](ProtoView) | Generic OOK/ASK signal visualiser and protocol analyser with waveform zoom |
| [Radio](Radio) | FM/AM broadcast radio receiver with audio output |
| [Radiosonde](Radiosonde) | Decodes RS41, M10, M20, and M2K2 weather balloon telemetry (temperature, humidity, GPS) |
| [RDS RX](RDS-RX) | Decodes RDS (Radio Data System) data from FM broadcast stations: PI code, programme service name (PS), programme type (PTY), TP flag and radiotext |
| [RTTY RX](RTTY-RX) | Decodes RTTY (Baudot/ITA2) at standard baud rates (45–200 baud) |
| [Scanner](Scanner) | Frequency list scanner with squelch-based channel locking |
| [Search](Search) | Wideband FFT-based signal search across a configurable frequency range |
| [Signal Hunter](Signal-Hunter) | Energy-based signal detector and auto-capture: triggers IQ recording to SD card when signal power exceeds a configurable threshold |
| [Spectrum Analyzer](Spectrum-Analyzer) | Swept spectrum analyzer (10 kHz span up to 1 MHz – 6 GHz) with three traces, four markers, a waterfall and benchtop-style softkey menus |
| [SSTV RX](SSTV-Rx) | Decodes Slow Scan Television (SSTV) image transmissions (Scottie, Martin, SC2 modes) |
| [SubCar](SubCar) | Decodes sub-GHz car remote keyless entry signals (Suzuki, VW, Subaru, Kia, Ford, Fiat, BMW) |
| [SubGhzD](SubGhzD) | Decodes sub-GHz OOK/AM remote controls across 45 protocols |
| [Tetra RX](Tetra-RX) | Decodes TETRA (Terrestrial Trunked Radio) downlink: network parameters, frame structure and call-control events (external app) |
| [Time Sink](Time-Sink) | Time-domain waveform viewer (oscilloscope): plots the I component of the IQ stream |
| [TPMS RX](TPMS-Rx) | Decodes Tire Pressure Monitoring System (TPMS) sensor transmissions at 315 / 433.9 MHz |
| [VOR RX](VOR-RX) | Decodes VHF Omnidirectional Range (VOR) aviation navigation beacons (108–117.95 MHz) and shows the bearing to/from the station |
| [Weather](Weather) | Decodes wireless weather station sensors (26 protocols; temperature, humidity) |
| [WeatherFax (WeFax)](WeatherFax) | Receives HF weather fax (radiofax) image broadcasts |
| [WMBus RX](WMBus-RX) | Decodes Wireless M-Bus (wM-Bus) utility meter telemetry at 868 MHz (S / T / C modes) — water, gas, heat and electricity meters |

## HackRF Receive Power Limits

The maximum safe RX input power for HackRF One is **−5 dBm** with the internal front-end amplifier enabled. Exceeding this level can cause permanent damage to the preamplifier IC — see [Preamplifier IC replacement](Preamplifier-IC-replacement) for repair notes.

With the RF amplifier disabled, HackRF One can in principle accept up to 10 dBm. However, a software error or accidental amplifier enable could still cause damage at that level. Using an external attenuator is safer than relying on the amplifier being off.

## Receiver Sensitivity

HackRF is a general-purpose SDR platform, not an optimised narrowband receiver. Actual sensitivity depends on the modulation type and depth, the operating frequency, the software and app configuration, and the acceptable bit error rate. Because any of these variables affects the result, there is no single answer for minimum detectable signal level — it must be measured for each specific application.

Performance can typically be improved significantly by choosing an appropriate antenna, adding an external low-noise amplifier, or adding an external bandpass filter for the frequency of interest. HackRF has no built-in RF filtering, making it susceptible to out-of-band interference without external filtering.