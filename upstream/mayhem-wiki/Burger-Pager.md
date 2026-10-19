> [!NOTE]
> This is an [external app](External-apps-informations) and must be present on the SD card in the `APPS/` folder.

Burger Pager transmits FSK paging signals compatible with restaurant coaster pager systems. It allows sending a page to a specific pager unit by address, or scanning through a range of addresses automatically.

The default frequency is **433.920 MHz**. Actual pager system frequencies vary by hardware — adjust the frequency field to match the target system before transmitting.

# Settings

* **Data** (16 hex digits): The full 8-byte payload to transmit. The lower 16 bits (last 4 hex digits) represent the pager address. Default value: `44013B30303034BC`.
* **Scan** (checkbox): When enabled, the app increments the pager address by 1 after each successful transmission and immediately retransmits, stepping through addresses continuously. When disabled, the frame is transmitted once and stops.

# Frame Format

Each transmission consists of a fixed 19-byte FSK frame:

| Bytes | Content |
|-------|---------|
| 0–7 | Preamble: `55 55 55 55 55 55 55 55` |
| 8–9 | Sync word: `2D D4` |
| 10 | Data length: `08` |
| 11–18 | Data payload (8 bytes, from the Data field) |

Modulation is FSK with a deviation of 5 kHz. Each frame is transmitted 32 times per press.

# Settings Persistence

Settings are saved to `tx_burger.ini`.