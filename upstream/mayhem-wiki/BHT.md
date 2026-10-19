BHT TX transmits remote streetlight management messages using two protocols — **Xylos** and **EPAR** — developed by BH-Technologies for public lighting control in France and some other European cities. The two protocols are selected via tabs and differ in their encoding and address structure. Settings are saved to `tx_bht.ini`.

> **Note:** Transmission on the frequencies used by these systems requires authorisation. Use only in a closed RF environment or with explicit permission from the network operator.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Xylos Tab

Xylos encodes commands as a sequence of 20 CCIR tones (100 ms per tone, 400 ms silence). Each field in the address hierarchy narrows which receivers respond.

* **Header A / Header B**: Two 2-digit numeric codes (0–99 each). These form the protocol header identifying the network.
* **City code**: Numeric code identifying the municipality. Range: 0–99.
* **Family**: Receiver family number. Range: 0–9.
* **Subfamily**: Receiver sub-group. Range: 0–9. The **All** checkbox sends a wildcard that matches all subfamilies in the selected family.
* **Receiver ID**: Individual receiver address. Range: 0–99. The **All** checkbox sends a wildcard that addresses all receivers in the selected subfamily.
* **Relay 1–4**: Four independent relay states. Each relay can be set to **Ignore** (no change), **Off**, or **On**, shown as bulb icons.

## EPAR Tab

EPAR (also called EP) uses OOK encoding at approximately 580 baud. Each transmission is repeated 26 times.

* **City code**: Municipality code. Range: 0–255.
* **Group**: Receiver group on the installation. Options: **A**, **B**, **C**, or **TP** (test point).
* **Relay 1–2**: Two relay states, each **Off** or **On**.

## Common Controls

* **Scan**: When checked, the app steps through the address range automatically after each transmission, incrementing the receiver address until the full range is covered. A progress bar tracks scan progress.
* **Flashing**: After each transmission, the app waits the number of seconds set in the speed field, flips all relay states to the opposite, then retransmits. This creates a flashing/toggling effect on the controlled lights.
* **Speed**: Interval in seconds between flashing toggles. Range: 1–99 s. Default: 1 s.
* **Frequency**: Editable via the keypad. The Xylos protocol operates in the 31–32 MHz band; EPAR deployments vary by installation.
* **LNA gain** (0–47 dB) and **RF Amp** (0 or 14 dB): Standard TX gain controls.
* **TX / Stop**: Starts or stops the transmission.