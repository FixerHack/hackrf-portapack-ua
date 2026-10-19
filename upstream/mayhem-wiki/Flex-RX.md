<img width="239" height="321" alt="image" src="https://github.com/user-attachments/assets/2a025b86-02cd-4966-91cb-436faca46257" />

# Introduction

[FLEX](https://en.wikipedia.org/wiki/FLEX_(protocol)) is a one-way paging protocol developed by Motorola in the 1990s, used by commercial paging networks to deliver messages to pagers. It supports multiple baud rates and modulation schemes, allowing higher capacity than its predecessor POCSAG. FLEX paging networks were widely deployed across North America, Europe, and Asia, and some systems remain in operation today.

The Flex RX app receives and decodes FLEX pager messages, displaying the capcode (pager address) and message content on screen.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

The key items that can be selected with the cursor and changed with the encoder knob are:

* **Title bar:** The usual items may be changed and displayed.
* **Frequency:** The default frequency is 931.74 MHz. Adjust to match the local paging network channel.
* **AMP / LNA / VGA:** Gain controls. Start with AMP off, LNA 24, VGA 24 and adjust based on received signal strength shown in the RSSI indicator.

## Common frequencies

FLEX paging frequencies vary by country and operator. Some examples:

| Region | Frequency |
|--------|-----------|
| USA (primary) | 931.8125 MHz |
| USA (secondary) | 929.7125 MHz, 931.7375 MHz |
| USA (various) | 929.0375 – 932.0 MHz band |
| UK / Europe | 153.025 MHz, 466 MHz band |
| Australia | 148.0125 MHz |

> **Note:** The app default (931.74 MHz) approximates the US 931.7375 MHz channel. Local frequencies depend on the operator and region. Scanning across known paging bands with Looking Glass or Scanner may help identify active channels.

# Protocol details

FLEX uses FM modulation with automatic detection of baud rate and modulation level from the sync codeword. The following modes are supported by the Mayhem decoder:

| Mode | Baud rate | Modulation | Phases |
|------|-----------|------------|--------|
| 1600/2 | 1600 baud | 2-FSK | A |
| 1600/4 | 1600 baud | 4-FSK | A, B |
| 3200/2 | 3200 baud | 2-FSK | A, C |
| 3200/4 | 3200 baud | 4-FSK | A, B, C, D |

The app demodulates at a sample rate of 3.072 MHz (decimated to 24 kHz for symbol detection) with a channel bandwidth of 1.75 MHz.

# Display

Received messages are shown in a scrolling console. Each decoded message entry shows:

* **Capcode** — the numeric pager address (up to 10 digits)
* **Message text** — decoded content (alphanumeric, numeric, or "Tone Only")

Up to 20 messages are stored in the display buffer. When the buffer is full, the oldest messages are removed to make room for new ones. A blank line separates each message entry.

## Message types

The following message types can be decoded:

| Type | Description |
|------|-------------|
| Alphanumeric | Free-text message (7-bit ASCII) |
| Numeric | Digits only, using BCD encoding |
| Tone Only | Alert to the pager, no message text |
| Secure | Encrypted alphanumeric (content not decoded) |
| Binary | Raw binary data (not decoded) |

Numbered Numeric and Special Numeric variants are also supported.

# Status bar

The top two rows of the screen show network metadata decoded from BIW words:

**Row 1:** `C<cycle>/F<frame> <bitrate> <polarity>  HH:MM:SS UTC+N`

Time is reconstructed from BIW TIME as `Frame-0 time + frame*1.875s + ext_sec*0.9375s`. If the transmitter sends an ExtSec value it is shown as `UTC+N es=N`.

**Row 2:** Local ID, coverage zone, country code from SSID BIWs. R flag = roaming supported.

# Settings persistence

The selected frequency is saved automatically and restored the next time the app is opened. Settings are stored in `SETTINGS/rx_flex.ini` on the SD card.

# Legal notice

Receiving pager transmissions may be restricted in your country. In many jurisdictions, intercepting communications intended for others — even if unencrypted — is regulated under telecommunications or wiretapping law. Check local regulations before use. Transmitting on paging frequencies without authorization is illegal.

# Further reading

* [FLEX protocol — Wikipedia](https://en.wikipedia.org/wiki/FLEX_(protocol))
* [FLEX paging frequencies — RadioReference](https://www.radioreference.com/)