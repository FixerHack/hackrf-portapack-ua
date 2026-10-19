TEDI/LCR TX generates and transmits LCR (Langage de Commande Routier — Road Command Language) frames, a French protocol used to control dynamic road equipment: variable message signs (PMV), tunnel systems, traffic cameras, emergency phones, weather stations, and related infrastructure. It uses AFSK modulation (Bell 202-compatible) over FM.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

**EC** — Éclairage (lighting) mode. Options: Auto (`A`), Jour/Day (`J`), Nuit/Night (`N`), S? (`S`).

**RGSB** — The 4-character destination address code (e.g. `AI10`). Press the **RGSB** button to enter a custom address via the keyboard. In scan mode, this is overridden by the selected address list.

**AM1–AM5** — Up to 5 address message slots. Each slot has a checkbox (to include it in the frame) and a **Set** button to enter the 7-character payload text. Only checked slots are included in the transmitted frame.

**Modem Setup** — Opens the modem configuration screen where you set the baudrate and repeat count. These settings are shared with other AFSK apps and persist in memory.

**Scan** (checkbox) — When enabled, automatically cycles through all RGSB addresses in the selected list, transmitting the configured frame to each address in sequence.

**List** — Selects the preconfigured RGSB address list used in scan mode. Contains a list of known addresses for the Lille road network (36 entries).

**Clear** — Clears all AM slot content and unchecks all checkboxes.

**START / STOP** — Starts or stops transmission. A progress bar and status line show repeat and scan progress (`repeat/total scan_index/total`).

# Message Format

The transmitted LCR frame has the following structure:

```
<7 sync bytes> RGSB AM=1 [AM=2 ...] EC=  
```

Text in each AM slot is padded to 7 characters. The checksum is an XOR of all characters from the RGSB field to the EOM byte, masked to 7 bits. The complete frame is transmitted the number of times set in Modem Setup.

# Preconfigured RGSB Lists

**Lille** (36 addresses): AI10–AI70, AJ10–AJ70, AK10, EAA0–EAD0, EbA0–EbS0

**Reims** (20 addresses): AI10–AI70, AJ10–AJ70, AK10–AK70 (selected), AP10

# RF Parameters

| Parameter | Value |
|---|---|
| Modulation | AFSK / FM (Bell 202-compatible) |
| Mark frequency | 1200 Hz |
| Space frequency | 2200 Hz |
| Baud rate | Configurable via Modem Setup (default: 1200 bps) |
| Bandwidth | 1.75 MHz |
| Sample rate | 1.536 MSps |
| Frequency step | 10 kHz |

# Settings Persistence

Settings are saved to `tx_lcr.ini`. Baudrate and repeat count are stored in shared persistent memory via Modem Setup.