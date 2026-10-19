This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

> **Legal warning:** Transmitting KeeLoq signals to garage doors, gates, or vehicles you do not own or have no authorisation to access is illegal in most jurisdictions. This app is intended for testing your own equipment and for security research on systems you are authorised to evaluate.

![alt](https://img.lightshot.app/-YmBUwtjTx2rfEhDnZmPtQ.png)

KeeLoq TX retransmits KeeLoq rolling-code signals loaded from `.keeloq` capture files. These files are created by the [SubGhzD](SubGhzD) receiver app when the Save button is used on a received KeeLoq or Superrollo packet. The app reconstructs and transmits the encrypted rolling-code payload based on the captured serial number, counter value, button code, and the KeeLoq learning variant used by the target device.

Supported transmission modes:
* **KeeLoq simple learning** — standard 64-bit OOK frame at Te=400 µs
* **KeeLoq normal learning** — standard 64-bit OOK frame at Te=400 µs
* **Superrollo (GW60/HCS361)** — 67-bit OOK frame at Te=450 µs, automatically selected when a file with `mf_name=Superrollo` is loaded

For all modes, the correct manufacturer key must be present in `KEELOQKEYS/MFCODES` to reconstruct the encrypted rolling-code payload. Without the key the transmission cannot be generated correctly.

# Settings

* **Open file**: Opens the file manager to select a `.keeloq` file from the `KEELOQREMOTES/` directory on the SD card.
* **Serial**: Displays the 28-bit serial number read from the loaded file.
* **Counter**: The 16-bit synchronisation counter. Editable — incrementing this value moves the counter forward in the rolling-code sequence.
* **Button**: The button code (0–15) to encode in the transmission.
* **Repeat**: Number of transmission repetitions. Default: 4.
* **Payload**: Live preview of the resulting encrypted frame in hexadecimal.
* **Transmit / Stop**: Starts or stops the transmission.

# Manufacturer Key File (MFCODES)

KeeLoq encryption requires a 64-bit manufacturer key specific to the device brand. Keys are loaded from `KEELOQKEYS/MFCODES` on the SD card. The file is not included in the firmware — it must be created manually.

File format — one entry per line, semicolon-delimited:

`mf_name;key_hex;type`

| Field | Description |
|---|---|
| `mf_name` | Manufacturer name as recognised by SubGhzD (e.g. `Superrollo`) |
| `key_hex` | 64-bit manufacturer key in hexadecimal (16 characters) |
| `type` | Learning mode: `1` = simple, `2` = normal |

Example: `Superrollo;XXXXXXXXXXXXXXXX;1`

Replace `XXXXXXXXXXXXXXXX` with the actual 64-bit key for your device. The key is not publicly distributed and must be obtained independently (e.g. via hardware analysis of the transmitter IC).

# Settings Persistence

Settings are saved to `tx_keeloq.ini`.