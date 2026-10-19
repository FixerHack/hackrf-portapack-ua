<img width="239" height="320" alt="image" src="https://github.com/user-attachments/assets/7e730aa9-7e87-4eee-8b17-7162403bf3b7" />

SubCar is a receiver app for decoding automotive remote keyless entry (RKE) signals from car key fobs. It passively listens on a configurable frequency and attempts to match incoming signals against a library of known manufacturer protocols, displaying decoded results in a scrolling list.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Settings

* **Frequency**: Default is **433.92 MHz**, the standard European RKE band. Adjustable via the encoder knob or on-screen numpad for other regional bands (e.g., 315 MHz in North America).
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **Mode**: Selects the demodulation mode — **AM** (default) or **FM**. Most car key fob protocols operate with AM (OOK) modulation; FM mode may be needed for some regional or newer implementations.
* **Clear**: Clears the decoded signal list from the display (does not affect the log file).
* **Log**: When checked, decoded packets are written to a timestamped CSV file on the SD card: `LOGS/SubCarLOG_YYYYMMDD_HHMMSS.CSV`. The file header is `; Type; Bits; Data;`.

# Decoded Signal List

Each decoded packet is shown as a row with three columns: **Type** (protocol name), **Bits** (bit length of the decoded frame), and **Age** (seconds since last received). The list is deduplicated by signal content — repeated presses of the same fob button update the age counter rather than adding a new row.

Selecting an entry opens a detail view showing the protocol type, serial number, button code, and additional decoded fields where available for that protocol.

# Supported Protocols

The following car key fob protocols are currently implemented:

| Protocol | Manufacturer |
|----------|-------------|
| Suzuki | Suzuki |
| VW | Volkswagen (button IDs: Lock, Unlock, Trunk, Panic, combinations) |
| Subaru | Subaru |
| Kia V0–V5 | KIA |
| Ford V0 | Ford |
| Fiat V0 | Fiat |
| BMW V0 | BMW |

> Note: Some protocols with full rolling-code encryption (Kia V6, PSA/Peugeot-Citroën) are recognized but not decoded, as the payload is entirely encrypted.

# Settings Persistence

The modulation mode and Log checkbox state are saved to `rx_subcar.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu