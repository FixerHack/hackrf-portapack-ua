> [!WARNING]
> P25 TX transmits a simulated trunked radio control channel. Transmitting on frequencies you are not licensed for is illegal and may interfere with public safety communications. Use only on licensed frequencies, in RF-shielded environments, or with a dummy load.

P25 TX generates a continuous P25 Phase 1 trunked control channel (TSCC). It cycles through TSBK (Trunked System Block) packets that identify the network and assign voice channels to talkgroups, allowing P25 radios and decoders to lock onto and follow the simulated system. Frames are transmitted continuously in a loop until stopped.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Transmission Parameters

| Parameter | Value |
|-----------|-------|
| Default frequency | 155.000 MHz |
| Bandwidth | 12,500 Hz (12.5 kHz) |
| Sample rate | 2,400,000 Hz |
| Modulation | C4FM, 9600 baud |
| Frame type | TSBK (DUID 0x07) |

# Controls

All fields are hexadecimal.

| Field | Digits | Description | Default |
|-------|--------|-------------|---------|
| **NAC** | 3 hex | Network Access Code | `293` |
| **SYS** | 3 hex | System ID | `001` |
| **WACN** | 5 hex | Wide Area Communication Network ID | `BEEF0` |
| **RFSS** | 2 hex | RF Subsystem ID | `01` |
| **SITE** | 2 hex | Site ID | `01` |
| **TG** | 4 hex | Talkgroup ID included in voice channel grant messages | `0001` |
| **VCH** | 3 hex | Voice Channel number assigned in group voice grant messages | `001` |

* **Frequency / Gain / AMP**: Standard TX controls. The configured frequency is also embedded into the IDEN\_UP TSBK packet as the channel centre frequency.
* **Start / Stop**: Begins or halts continuous TSBK transmission. Status shows `TX TSCC` while running.

# TSBK Sequence

The app transmits a repeating 5-packet cycle:

1. `IDEN_UP` (0x3D) — Channel identifier with frequency
2. `NET_STATUS` (0x3B) — WACN and System ID
3. `RFSS_STATUS` (0x3A) — RFSS and Site identification
4. `GRP_V_GRANT` (0x00) — Group voice channel grant for the configured TG / VCH
5. `NET_STATUS` (0x3B) — repeated

Each packet is BCH(63,16)-encoded, 1/2-rate trellis-encoded, interleaved, and status-symbol-inserted per the P25 Phase 1 standard before transmission.

# Settings Persistence

Settings are saved to `tx_p25_tx.ini`.