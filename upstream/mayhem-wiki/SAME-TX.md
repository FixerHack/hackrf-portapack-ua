SAME TX generates and transmits Specific Area Message Encoding (SAME) digital headers — the protocol used by the US Emergency Alert System (EAS) and NOAA Weather Radio. SAME-capable receivers use these headers to selectively activate for alerts targeting their programmed county.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

| Field | Description | Range / Options | Default |
|---|---|---|---|
| **Org** | Originator code | WXR, EAS, CIV, PEP | WXR |
| **Evt** | Event type (index 0–25) | See table below | RWT (index 0) |
| **FIPS State** | 2-digit US state FIPS code | 00–99 | 39 (Ohio) |
| **FIPS County** | 3-digit county FIPS code | 000–999 | 007 (Ashtabula) |
| **Dur H** | Alert duration — hours | 00–99 | 00 |
| **Dur M** | Alert duration — minutes | 00–59 | 30 |

A live preview of the message string updates on screen as fields are changed.

# Originator Codes

| Code | Meaning |
|---|---|
| **WXR** | National Weather Service |
| **EAS** | EAS Participant (broadcaster or cable system) |
| **CIV** | Civil Authorities |
| **PEP** | Primary Entry Point System (presidential-level) |

# Event Codes

| # | Code | Event |
|---|---|---|
| 0 | RWT | Required Weekly Test |
| 1 | RMT | Required Monthly Test |
| 2 | NPT | National Periodic Test |
| 3 | NST | National Silent Test |
| 4 | NMT | National Periodic Test |
| 5 | EAN | Emergency Action Notification |
| 6 | EAT | Emergency Action Termination |
| 7 | NIC | National Information Center |
| 8 | ADR | Administrative Message |
| 9 | AVA | Avalanche Watch |
| 10 | AVW | Avalanche Warning |
| 11 | BZW | Blizzard Warning |
| 12 | CFW | Coastal Flood Watch |
| 13 | CFS | Coastal Flood Statement |
| 14 | DSW | Dust Storm Warning |
| 15 | EQW | Earthquake Warning |
| 16 | EVI | Evacuation Immediate |
| 17 | FFW | Flash Flood Warning |
| 18 | FFS | Flash Flood Statement |
| 19 | FFH | Flash Flood Watch |
| 20 | FRW | Fire Warning |
| 21 | HLS | Hurricane Statement |
| 22 | HUW | Hurricane Warning |
| 23 | HUH | Hurricane Watch |
| 24 | SVR | Severe Thunderstorm Warning |
| 25 | TOR | Tornado Warning |

# Message Format

The transmitted header has the form:

```
ZCZC-ORG-EVT-SS0CCC+HHMM-0010000-SAMETX--
```

where `SS` is the state FIPS, `0CCC` is the county FIPS (the leading `0` is literal, part of the SAME county encoding), `HHMM` is the duration, and `-0010000-SAMETX-` are fixed placeholder fields for issue time and station ID. The full message is preceded by 16 preamble bytes and transmitted **3 times** automatically, as required by the SAME standard.

# RF Parameters

| Parameter | Value |
|---|---|
| Default frequency | 162.550 MHz (NOAA Weather Radio) |
| Bandwidth | 1.75 MHz |
| Sample rate | 1.536 MSps |
| Modulation | AFSK / FM |
| Mark tone | 2083 Hz |
| Space tone | 1563 Hz |
| Baud rate | ~520.83 bps |
| FM deviation | 5 kHz |
| Repeats | 3× |

# Settings Persistence

Settings are saved to `tx_same.ini`.