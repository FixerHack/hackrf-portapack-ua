# Flex TX
## Overview

<img width="240" height="320" alt="SCR_0000" src="https://github.com/user-attachments/assets/547774aa-d7d5-4579-9a0e-83f3d69d8e11" />

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Introduction

This application transmits pager messages using the [FLEX](https://en.wikipedia.org/wiki/FLEX_(protocol)) protocol. FLEX is a one-way paging protocol developed by Motorola that supports higher throughput than POCSAG through multi-level modulation and multiple phases.

The transmitter generates a complete FLEX frame including sync patterns, FIW (Frame Information Word), BIW (Block Information Words) with optional network metadata, address encoding, and message payload. It supports short and long addresses, multiple message types, and configurable network parameters.

It is intended for testing, experimentation, and educational use with licensed equipment or on frequencies for which you hold appropriate authorization.

## Controls

### Capcode

The destination pager address (capcode). Enter using the on-screen digit field (0-4297068542).

An info line below the capcode field shows the address type and computed frame/phase:

| Range | Type |
|-------|------|
| 1 - 1,933,312 | Short address |
| 2,058,240 - 2,062,335 | Network address |
| 2,041,856 - 2,058,239 | Info service |
| 2,062,336 - 2,062,351 | Temporary group #0-15 |
| 2,062,352 - 2,062,367 | Operator message |
| 2,101,249 - 4,297,068,542 | Long address (2-word encoding) |

The address type, frame number, and phase (A/B/C/D) are decoded from the capcode and shown for information only. In a real network, the infrastructure drives phase assignment and collapse values - these computed values may not reflect what a live network would use.

Only short and long addresses are valid for normal message transmission. Other address types (network, info service, temporary group, operator) may require different vector types or special payload formats. The app does not prevent sending to these addresses, but pagers will ignore messages with an invalid payload format for the address type.

### Speed

Currently supports **1600/2FSK** only (1600 baud, 2-level FSK, phase A). This is the baseline FLEX mode supported by all FLEX pagers.

| Mode | Baud Rate | Modulation | Phases | Bit Rate | TX Support |
|------|-----------|------------|--------|----------|------------|
| 1600/2FSK | 1600 baud | 2-FSK | A | 1600 bps | Yes |
| 3200/2FSK | 3200 baud | 2-FSK | A, C | 3200 bps | No |
| 3200/4FSK | 1600 baud | 4-FSK | A, C | 3200 bps | No |
| 6400/4FSK | 3200 baud | 4-FSK | A, B, C, D | 6400 bps | No |

### Type

Message type to transmit:

| Type | Description |
|------|-------------|
| Alphanumeric | Free-text ASCII message (up to 240 characters) |
| Numeric | BCD-encoded digits using a numeric vector word, with message words for the payload. Valid BCD characters: `0-9 U - ] [ space` and `.` (reserved, rendered as period for clarity) |
| Short/tone | Short numeric vector with an empty payload - the pager typically decodes this as a tone-only alert. This is not a true "address-only" page (which would be an address word with no vector at all); it is a short numeric vector where all digit positions are filled with spaces. |
| Short numeric | Short numeric vector with BCD digits encoded directly in the vector word(s). Short addresses carry up to 3 digits; long addresses carry up to 8 digits (3 in the vector word + 5 in a second word). Every pager that supports numeric vectors also supports short numeric vectors. |

> **Note:** True tone-only pages (address without any vector word) are not implemented here and are not supported by most alphanumeric pagers in practice.

### Message

The text payload. Press **Set message** to enter text using the on-screen keyboard. Maximum length is 240 characters.

For **Numeric** and **Short numeric** types, only valid BCD characters are accepted: `0-9 U - ] [ space` and `.` (reserved BCD symbol, rendered as period). Invalid characters will trigger an error.

### Set Params

Opens the FLEX Parameters configuration screen (see below).

## FLEX Parameters

The **Set params** button opens a configuration screen for the BIW (Block Information Word) fields included in the transmitted frame. These fields carry network metadata that real FLEX transmitters broadcast alongside messages.

### Date

When enabled, includes a BIW date word in the frame. Fields: Year (1994-2025), Month, Day.

> **Note:** The FLEX protocol encodes years as a 5-bit offset from 1994, giving a valid range of 1994-2025. For years beyond 2025, the app can automatically find a calendar-equivalent year (same leap year status and day-of-week alignment) within the valid range. Some newer pagers treat year 0 as 2026 (an epoch rollover similar to how GPS or Unix time handles wraparound), but this behavior is pager-dependent.

Date and time fields are pre-populated from the PortaPack's RTC clock when the app opens, but you can change them or disable them with the checkboxes before transmitting.

### Time

When enabled, includes a BIW time word. Fields: Hour, Minute, Second. The second value is quantized to 7.5-second steps per the FLEX specification.

The app uses standard mode: BIW TIME encodes the time at Frame 0 of the current cycle (`minute = cycle*4, second = 0`, hour from the RTC). The pager adds `frame*1.875s` internally to recover the real current time.

### TZ / DST / ExtSec

When enabled, includes a timezone BIW sysinfo word. Select from a list of UTC offsets. The DST checkbox indicates whether daylight saving time is active (pre-populated from the PortaPack's DST setting).

**ExtSec** (0-7, default 0): extended seconds trim in 0.9375s steps. Used by real infrastructure to compensate for clock/frame-grid misalignment. Leave at 0 for normal use.

### LocID / CovZone

When enabled, includes a SSID1 BIW word with:
* **Local ID** (0-511): Identifies the local transmitter site
* **Coverage Zone** (0-31): Geographic coverage area identifier

### Country Code

When enabled, includes a SSID2 BIW word with the country code (0-1023).

### Roam

When enabled, sets the roaming flag in the FIW, which tells pagers that this network supports roaming and they may join even if it is not their home network. Enabling roaming automatically enables both LocID and CountryCode fields.

> **Note:** LocID, CovZone, CountryCode, and Roam should all be left disabled unless the target pager's home country and network are known. This transmitter does not implement a proper carousel to broadcast all the BIW words required for correct multi-network operation. By default, pagers treat whatever frequency they are configured on as their home network, so these options are for experimentation only.

### Msg#

Message sequence number (0-63). Incremented automatically after each successful transmission. Initialized from the RTC on app launch. Pagers can use this to detect duplicate messages as part of the FLEX extended network feature, but not all pagers implement it - some simply deduplicate based on message content.

### ERS

When enabled, transmits ERS (Emergency Re-Sync) signal cycles before the message frame. In a FLEX network with collapse > 0, pagers periodically go to sleep to save battery and only wake up during their assigned frames. The ERS signal must be at least one collapse cycle in length so that any sleeping pager has a chance to wake up and see the re-sync alert before the message frame arrives.
* **Count** (1-10): Number of ERS burst groups to transmit.

## Transmission

### Transmit Controls (Bottom Bar)

* **Frequency**: Transmission frequency. Default is 931.74 MHz.
* **Gain** (0-47 dB): TX IF gain.
* **AMP** (0 or 1): RF amplifier (+14 dB when enabled).

Press **START** to begin transmitting. The progress bar shows transmission progress through the multi-step sequence:

1. **ERS bursts** (if enabled) -- one step per ERS count
2. **Frame 1/2 (new)** -- small ERS preamble + message frame with retrieve=1 (new message)
3. **Frame 2/2 (dup)** -- small ERS preamble + message frame with retrieve=0 (retransmit, don't alert if already seen)

Each frame transmission is sent as a single package: a short ERS preamble (8 cycles, 96 bytes) followed by the frame data (379 bytes), totaling about 475 bytes. 

The shared memory buffer used to pass data to the baseband processor is 512 bytes, so there is only room for one frame at a time. A real FLEX network transmits a continuous time-synchronized signal - 15 cycles per hour, 128 frames per cycle (each 1.875 seconds), with frame 0 of cycle 0 aligned to the top of each hour. The PortaPack cannot maintain such a signal because the baseband buffer is too small to hold more than one frame, and there is no GPS time reference or real-time frame scheduler. Instead, it transmits individual frames as one-shot bursts, with the carrier dropping between steps. The FIW carries the real FLEX cycle and frame number derived from the RTC at the moment of transmission, so a standard pager reconstructs the correct current time as `BIW TIME + frame*1.875s`. Because of this, it sends two copies of the message frame with small ERS preamble: the first message with the retrieve bit set (new message, pager alerts) and the second without it (retransmit, pager stores but does not alert again if it already received the first). This improves the chance of successful delivery. Transmission stops automatically when complete.

## USB Serial

The Flex TX app can be triggered remotely via USB serial using the `FlexTosend` message type. When a serial message is received, the capcode, type, and message fields are updated in the UI and transmission starts automatically.

## Settings Persistence

Capcode and BIW parameter selections are saved automatically and restored on next launch. Settings are stored in `SETTINGS/tx_flex.ini` on the SD card.

## Legal Notice

FLEX operates on licensed frequencies. Transmitting on commercial paging frequencies without authorization is illegal in all jurisdictions. The HackRF One is a test and development device. The licensed operator is responsible for ensuring compliance with local regulations.

## Further Reading

* [Flex RX](Flex-RX) - receive and decode FLEX pager messages
* [FLEX protocol - Wikipedia](https://en.wikipedia.org/wiki/FLEX_(protocol))
* [POCSAG TX](POCSAG-Tx) - transmit using the POCSAG protocol
