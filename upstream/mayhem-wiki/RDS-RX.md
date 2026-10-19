# RDS RX

Decodes **RDS** (Radio Data System) data carried alongside the audio of FM broadcast stations and shows the station's identity and text in real time.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Overview

RDS is the digital data stream that FM stations broadcast on a subcarrier next to their audio. It carries the station identity, programme type, a traffic flag and scrolling text. The app FM-demodulates the selected station, recovers the RDS subcarrier at **57 kHz**, decodes the biphase-coded groups and displays the fields below.

Tune the frequency field to an FM broadcast station (87.5–108 MHz). A strong, clean FM signal is needed for stable decoding.

## Controls

| Control | Description |
|---|---|
| **Frequency** | Tune to an FM station (100 kHz steps). |
| **RF Amp** | RF amplifier: `0` = off, `1` = on (+14 dB). |
| **LNA** | IF gain (0–40 dB). See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings). |
| **VGA** | Baseband gain (0–62 dB). |
| RSSI / Channel | Signal strength and channel power meters. |

## Decoded fields

| Field | Meaning |
|---|---|
| **PI** | Programme Identification code (hex) — uniquely identifies the station / network |
| **TP** | Traffic Programme flag (Yes / No) — station carries traffic announcements |
| **PTY** | Programme Type as number + name (e.g. News, Pop, Rock, Classics, Weather, Sport) |
| **PS** | Programme Service name — the 8-character station name, built up from type 0A/0B groups |
| **Radio Text** | Free-text message from the station (up to 64 characters, type 2A/2B groups), shown on three lines |

Below the fields a **diagnostic console** prints each received group as its four raw blocks `[A B C D]` followed by the group type (e.g. `G:0A`, `G:2A`). Blocks that failed the error check are shown as `----`.

## Protocol

RDS is transmitted on a **57 kHz** subcarrier (the third harmonic of the 19 kHz FM stereo pilot), biphase-coded at **1187.5 bit/s** and arranged in groups of four blocks, each protected by an error-correcting checkword.

## See also

- [RDS](RDS) — transmit RDS data with the RDS TX app