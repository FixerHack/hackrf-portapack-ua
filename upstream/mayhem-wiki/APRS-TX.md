[Automatic Packet Reporting System] The APRS TX App sends messages on the selected frequency. The App allows the configuration of the APRS stream.
The App is marked as Beta, but it does send decodable messages in AFSK in the correct AX.25 format.

> [!NOTE]
> This is an [external app](External-apps-informations) and must be present on the SD card in the `APPS/` folder.

## Fields

**Source:**
Your own licensed amateur radio callsign (e.g. W1ABC). The field accepts up to 6 alphanumeric characters. Move the cursor to the right side of the label using the arrow buttons and select each character. Then move to "SSID:" and select a number from 0–15. The most common SSID for a PortaPack is 0.

**Dest.:**
This is **not** the callsign of a receiving station. In APRS, this field must contain a valid APRS destination address. The recommended value for general use is **APRS** (which falls under the generic AP* wildcard accepted by all APRS decoders). For experimental or custom software, **APZNNN** (where NNN is a version number) is the correct choice per the APRS Protocol Reference. Entering a random callsign or leaving this field empty will cause APRS decoders (such as OpenWebRX, Direwolf, or aprs.fi) to ignore or incorrectly parse the packet. Set SSID to 0.

**Path:**
The digipeater path tells the network how far to relay your packet.
- WIDE1-1 — single hop, recommended for most mobile and portable use
- WIDE1-1,WIDE2-1 — two hops, wider area coverage
- Leave empty for direct RF only (no digipeating)

**Info field:**
The message content. Select the "Set" button to enter text (maximum 30 characters). **Important:** The very first character of the Info field must be a valid APRS Data Type Identifier (DTI). Without it, APRS decoders cannot determine the packet type and will not display the content correctly.

Note: The ! DTI is an exception — it may appear anywhere up to the 40th character position. All other DTIs must be the first character.

## APRS Data Type Identifiers

The first character of the Info field defines what kind of data follows. Source: APRS Protocol Reference v1.0, Chapter 5.

| Character | Type | Messaging | Example Info field |
|-----------|------|-----------|-------------------|
| > | Status — simplest, no coordinates needed | No | >Hello from PortaPack |
| ! | Position without timestamp | No | !4071.27N/07400.59W-Hello from NYC |
| = | Position without timestamp | Yes | =4071.27N/07400.59W-Hello from NYC |
| / | Position with timestamp | No | /181654z4071.27N/07400.59W-Hello |
| @ | Position with timestamp | Yes | @181654z4071.27N/07400.59W-Hello |
| : | Message to a specific station | Yes | :W1XYZ    :Hello there |
| ; | Object report | No | ;OBJECT   *181654z4071.27N/07400.59W/ |
| _ | Weather report (no position) | No | _10092345c000s000g000t068 |
| T | Telemetry | No | T#001,100,200,300,400,500,00000000 |

**"Messaging"** means the packet signals that the station is capable of receiving and acknowledging APRS messages. Use = or @ if you want two-way messaging; use ! or / for position-only beacons.

**For beginners, start with > (status).** It requires no coordinates, no timestamp, and is decoded by all APRS software.

The ?GPS? placeholder in the Info field is automatically replaced by the current GPS coordinates if a GPS module is active or Manual GPS has been set. Example: !?GPS?-Hello from PortaPack

## Timestamp formats

Timestamps appear inside position packets that use the / or @ DTI. The format is always 7 characters.

| Format | Example | Meaning |
|--------|---------|---------|
| DDHHMMz | 181654z | Day 18, 16:54 UTC — recommended |
| DDHHMM/ | 181654/ | Day 18, 16:54 local time |
| HHMMSSh | 165400h | 16:54:00 UTC (hours/minutes/seconds) |

The APRS Protocol Reference recommends always using zulu (z) format for on-air transmissions.

Note: The MDHM format (Month/Day/Hours/Minutes) seen in some older examples is only valid for positionless weather station reports and must not be used in position packets.

## Position coordinate format

Latitude: DDmm.hhN or DDmm.hhS (8 characters)
Longitude: DDDmm.hhE or DDDmm.hhW (9 characters — always 3 digits for degrees, with leading zero if needed)

Example: 4071.27N/07400.59W = New York City area
- 40 degrees 71.27 minutes North
- 074 degrees 00.59 minutes West (note the leading zero)

The character between latitude and longitude is the Symbol Table Identifier (/ = primary table, \ = alternate table). The character immediately after the longitude is the Symbol Code. Common symbol codes: - = house, > = car, [ = jogger, / = dot/waypoint. See the [APRS Symbol Tables](http://www.aprs.org/symbols.html) for the full list.

## Altitude

When a real position is present (from a GPS module or the manual position picker), the station's altitude is transmitted as the standard APRS comment extension **`/A=aaaaaa`**, appended after the position. Altitude is entered in **metres** in the position picker and converted to **feet** for the six-digit `/A=` field. An altitude of zero is a valid value and is sent as `/A=000000` rather than being dropped. The last altitude is saved to `tx_aprs.ini`.

## Frequency

APRS operates on dedicated frequencies per region. Transmitting on the wrong frequency means nobody will receive your packets.

| Frequency | Region |
|-----------|--------|
| 144.390 MHz | North America (USA, Canada, Mexico), Colombia, Chile, Indonesia, Thailand |
| 144.800 MHz | Europe, Africa, Russia, Middle East |
| 144.575 MHz | New Zealand |
| 144.640 MHz | Japan, Eastern Asia |
| 145.175 MHz | Australia |
| 145.825 MHz | ISS (International Space Station) — worldwide, only when ISS is in range (~10 min passes) |
| 432.500 MHz | Europe (UHF) |

The default frequency in the app is 144.390 MHz. Change it using the on-screen keypad at the bottom of the screen.

**ISS note:** Packets sent to 145.825 MHz during an ISS pass are relayed by the onboard APRS digipeater and can be received worldwide. Use ARISS as the path instead of WIDE1-1. Check current ISS pass times for your location before attempting.

⚠️ Transmitting to the ISS requires the same valid amateur radio license as any other APRS operation. Using the ISS digipeater with a fictional callsign is a violation of both national regulations and ITU Radio Regulations Article 25. The ARISS organization monitors activity on 145.825 MHz. See the [ARISS website](https://www.ariss.org) for schedules and guidelines.

## Gain settings

At the bottom of the screen:
- **Frequency step:** select step size with cursor, adjust with rotary encoder (e.g. 12k5)
- **Deviation:** select with cursor, adjust with rotary encoder (e.g. 5 kHz)
- **Gain IF:** range 0–47. Color indicates combined output power (IF + AMP): 0–17 green, 18–38 yellow, 39–47 orange, 48–61 red
- **Amp:** 0 dB or 14 dB (on/off)

Transmission starts with the "Start" button and stops automatically after the packet is sent.

## Complete working examples

Some example message formats are as follows. Many more are in the [APRS Protocol Reference Manual](http://www.aprs.org/doc/APRS101.PDF).

**Simplest packet — status message:**
- Source: W1ABC, SSID: 0
- Dest.: APRS, SSID: 0
- Path: WIDE1-1
- Info field: >Hello from PortaPack
- Frequency: 144.390 MHz (North America)

**Position without timestamp (no messaging):**
- Info field: !4071.27N/07400.59W-Hello from NYC
- The - after the longitude is the Symbol Code for a house

**Position without timestamp (with messaging enabled):**
- Info field: =4071.27N/07400.59W-Hello from NYC

**Position with UTC timestamp (no messaging):**
- Info field: /181654z4071.27N/07400.59W-Hello from NYC
- Format: /DDHHMMzDDmm.hhN/DDDmm.hhW[symbol][comment]

**Position with UTC timestamp (with messaging):**
- Info field: @181654z4071.27N/07400.59W-Hello from NYC

**Position with GPS placeholder:**
- Info field: !?GPS?-Hello from PortaPack
- Requires GPS module active or Manual GPS set

**Position with altitude:**
- Info field: !4071.27N/07400.59W-Hello from NYC /A=105
- Altitude /A= is always in feet per APRS Protocol Reference

**Putting it all together — position, UTC timestamp, altitude and comment:**
- Info field: @181654z4071.27N/07400.59W-Hello from NYC /A=105
- April 18th at 16:54 UTC, New York City area, 105 feet altitude

## Testing your transmission

A reliable way to verify your packets are correctly decoded is to use a second SDR receiver (e.g. RTL-SDR) with SDR++ and the QTMM AFSK1200 Decoder software, both free. You can also use an online WebSDR or a local OpenWebRX instance. Note that aprs.fi and similar internet-connected receivers will only show your packet if an iGate is within RF range of your transmission.

## Legal notice — amateur radio license required

APRS operates on amateur radio frequencies. Transmitting on these frequencies requires a valid amateur radio license in virtually every country.

| Country / Region | Governing body | Regulation | License required |
|------------------|----------------|------------|------------------|
| USA | FCC | [Part 97](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97) | Technician class or higher |
| Europe (ITU Region 1) | National authority (e.g. BNetzA, Ofcom, ANFR) | [ITU Radio Regulations Art. 25](https://www.itu.int/pub/R-REG-RR) | National amateur license |
| Australia | ACMA | [Radiocommunications Act 1992](https://www.legislation.gov.au/Details/C2022C00097) | Foundation class or higher |
| Japan | MIC | [Radio Law of Japan](https://www.tele.soumu.go.jp/e/adm/freq/search/index.htm) | Operator license + equipment type approval |
| Canada | ISED | [RBR-4](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/standards/radio-standards/rbr-4-standards-operation-radio-stations-amateur-radio-service) | Amateur radio operator certificate |
| Worldwide | ITU | [ITU Radio Regulations](https://www.itu.int/pub/R-REG-RR) | National amateur license |

**The Source callsign must be your own licensed callsign.** Using a fictional, unassigned, or third-party callsign is illegal in all jurisdictions and may result in fines, license revocation, or criminal prosecution depending on local law.

**The HackRF One is a test and development device, not a certified amateur radio transceiver.** In the USA (FCC Part 97), no equipment certification is required for amateur radio — the licensed operator bears full responsibility for the quality and legality of the transmission. In most European countries, the transmitting equipment must additionally meet national technical requirements (spurious emissions, bandwidth). Ensure your transmission complies with the regulations of your country before transmitting on any amateur frequency.

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

## Further reading

- [APRS Protocol Reference Manual](http://www.aprs.org/doc/APRS101.PDF)
- [FCC Part 97 — Amateur Radio Service](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97)
- [ARRL guide to Part 97](https://www.arrl.org/part-97-text)
- [ARISS — Amateur Radio on the International Space Station](https://www.ariss.org)
- [ITU Radio Regulations](https://www.itu.int/pub/R-REG-RR)
- [aprs.fi — Live APRS map](https://aprs.fi)
- [APRS Symbol Tables](http://www.aprs.org/symbols.html)