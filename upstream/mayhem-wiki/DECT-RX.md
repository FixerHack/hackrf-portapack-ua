DECT RX tunes the 10 US/EU DECT carriers, demodulates the GFSK bursts, CRC-checks the A-field, and tracks RFP (base) and PP (handset) parts, showing their RFPI/IPUI, timeslot, and Qt multiframe sync. Bearers that advertise voice (`BA == 0`) are flagged in the part list and status line. Decoding to audible audio is **not** included.

> [!WARNING]
> DECT carries cordless-telephone traffic. Intercepting communications you are not authorised to receive may be illegal in your jurisdiction and violates the privacy of the parties on the call. Use only on systems you own or have explicit permission to monitor.


# Receiver Parameters

| Parameter | Value |
|-----------|-------|
| Default frequency | 1921.536000 MHz (US Ch0) |
| Frequency step | 1 kHz |
| Bandwidth | 3,500,000 Hz |
| Sample rate | 4,608,000 Hz (4× symbol rate) |
| Symbol rate | 1.152 Mbaud (GFSK) |
| Channel spacing | 1.728 MHz |
| Bands | US, EU |
| Channels per band | 10 |
| Hidden LO offset | sample_rate/4 + 20,000 Hz (≈1.172 MHz) |
| Frame structure | 24 slots × 480 symbols (10 ms frame) |
| A-field CRC | RCRC-16 (CCITT/HDLC variant), XOR 0x0001 |

# Controls

* **Band** (US / EU): Selects the DECT band. Changing it re-applies the selected channel and retunes.

* **Channel** (Ch0–Ch9): Selects the carrier within the band.

* **Frequency**: Displays the tuned carrier. Step is 1 kHz; updated whenever the band or channel changes.

* **RSSI / Channel meter**: Signal strength and channel level (top right).

* **RF amp / LNA / VGA**: Standard RX gain controls.

* **Status bar**: Shows `N part(s)  voice:M`, `not configured`, or `starting`.

* **Console**: Logs one line per newly-seen part ID (de-duplicated per receiver slot). Format:

  ```
  RFP sNN AABBCCDDEE qt voice
  ```

  * type: `RFP` (base) or `PP ` (portable/handset)
  * `sNN`: DECT timeslot, 0–23
  * `AABBCCDDEE`: 5-byte RFPI (RFP) or IPUI (PP) in hex
  * `qt`: Qt multiframe sync seen, otherwise `--`
  * `voice`: voice/traffic bearer present, otherwise `-----`

# Bands and Channels

| Ch | US (MHz) | EU (MHz) |
|----|----------|----------|
| 0 | 1921.536 | 1897.344 |
| 1 | 1923.264 | 1895.616 |
| 2 | 1924.992 | 1893.888 |
| 3 | 1926.720 | 1892.160 |
| 4 | 1928.448 | 1890.432 |
| 5 | 1930.176 | 1888.704 |
| 6 | 1931.904 | 1886.976 |
| 7 | 1933.632 | 1885.248 |
| 8 | 1935.360 | 1883.520 |
| 9 | 1937.088 | 1881.792 |

US follows DECT 6.0 (FCC Part 15 Subpart D); EU follows ETSI EN 300 175.

# Decode Pipeline

The M4 baseband decodes at 4× the DECT symbol rate so there is exactly one bit decision per 4 IQ samples, with no resampler.

1. **DC blocker**: The LO is parked ~20 kHz off-channel so the front-end LO-leakage spike falls in the blocker's narrow notch while the carrier stays in its passband (this measurably lowers the A-field error rate).
2. **Phase-difference demod**: `atan2`-based phase difference drives the bit decision (positive phase → `0`, negative → `1`).
3. **Sync**: Detects the RFP sync word `0xAAAAE98A`; PP bursts use the bitwise complement. After sync, 388 bits are captured: 64-bit A-field + 320-bit B-field + 4-bit X-CRC.
4. **A-field decode**: The first 6 bytes are CRC-checked (RCRC-16). Header fields:
   * `TA == 3` → Identification: 5-byte RFPI (base) / IPUI (portable)
   * `TA == 4` → Qt: multiframe sync / system info (frame 8 of 16)
   * `BA == 0` → traffic bearer carrying voice
5. **Part tracking**: Up to 8 concurrent parts. A burst is matched to an existing part by 24-slot timing, or a new part is allocated. A part is dropped after 16 frames (~160 ms) with no activity. RFP and PP entries are paired when their IDs match; an RFP's Qt marker is lent to its paired PP.

# Settings Persistence

None. DECT RX does not save settings to an `.ini` file; the selected band and channel reset on exit.
