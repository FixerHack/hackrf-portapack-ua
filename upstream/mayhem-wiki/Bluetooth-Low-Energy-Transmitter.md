BLE TX transmits Bluetooth Low Energy advertisement packets loaded from a .TXT file. It supports two modes: single transmit (sends each packet once) and loop mode (repeats continuously for the number of repeats specified in the file). A file must be loaded before transmitting — unless arriving directly from the BLE RX app, which transfers the captured packet automatically.

## Settings

**Open file:** Select a .TXT packet file from the SD card. Files are stored in the BLETX/ directory by default.

**?? Mac:** When checked, a randomised MAC address is used instead of the one defined in the file.

**Loop:** When checked, the app transmits the full packet file repeatedly until stopped. The progress bar and Packets Left indicator show how many packets remain in the current pass.

**Speed:** Controls the transmit interval between packets, based on display frame timer ticks (≈16 ms each):

* 1 — 2 ticks (~32 ms per packet)
* 2 — 4 ticks (~64 ms per packet)
* 3 — 6 ticks (~96 ms per packet)
* 4 — 8 ticks (~128 ms per packet)
* 5 — 12 ticks (~192 ms per packet)

**Channel:** BLE channel selection:

* **Ch.37, Ch.38, Ch.39** — individual BLE advertising channels
* **Ch.00–Ch.36** — individual BLE data channels
* **Auto** — cycles through the three advertising channels (Ch.37, Ch.38, Ch.39)
* **All** — cycles through all 40 BLE channels (Ch.00–Ch.39)

**Advertisement PDU Type:** The BLE packet type to transmit — set in the UI, not read from the file: DISCOVERY, ADV_IND, ADV_DIRECT, ADV_NONCONN, ADV_SCAN_IND, SCAN_REQ, SCAN_RSP, CONNECT_REQ. To make a packet visible on a BLE scanner app, use ADV_NONCONN.

**Marked Data sequence:** When bytes are marked in the data editor, controls how they change between transmissions — Ascend, Descend, or Random.

**Long-press on packet data:** Hold a value in the data packet display to edit it in real time using the encoder knob and buttons.

**Clear Marked:** Removes all marked bytes from the data editor.

**Save Packet:** Saves the current packet list to a new file in BLETX/ named BLETX_XXXX.TXT.

**Switch to Rx:** Switches directly to the BLE RX app.

## File Format

Each line in the .TXT file defines one packet with three space-separated fields. All fields must be separated by a single space.

* **MAC:** Exactly 12 hex characters, no separators (e.g. 010203040506)
* **AdvertisementData:** Up to 62 hex characters of raw advertisement payload (max 31 bytes per BLE spec)
* **RepeatCount:** Number of times to transmit this packet (integer)

Up to 32 packets per file are supported. Each packet goes on its own line.

Example — two packets, 500 repeats each:
```
010203040506 190953445220426c7565746f6f7468204c6f7720456e65726779 500
010203040507 190953445220426c7565746f6f7468204c6f7720456e65726779 500
```

The advertisement data in this example decodes to the ASCII string SDR Bluetooth Low Energy.

Files captured by the BLE RX app are already in this format and can be loaded directly.

## Settings Persistence

Settings are saved to tx_ble.ini.