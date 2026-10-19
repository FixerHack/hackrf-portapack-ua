![image](https://github.com/user-attachments/assets/37807945-cfc5-4608-9d97-9f1e8d858962)

SubGhzD (Sub-GHz Decoder) is a passive receiver app for decoding OOK/AM sub-GHz remote control signals from gate remotes, garage door openers, doorbells, home automation devices, and similar ISM-band transmitters. It identifies the protocol and displays decoded data in a scrolling list.

# Settings

* **Frequency**: Default is **433.92 MHz**. Adjustable via the encoder knob or on-screen numpad for other ISM bands (e.g., 315 MHz, 868 MHz).
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier. Use with care on strong signals.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **Clear**: Clears the decoded signal list from the screen. Does not affect the log file.
* **Log**: When checked, decoded packets are written to a timestamped CSV file on the SD card: `LOGS/SUBGHZDLOG_YYYYMMDD_HHMMSS.CSV`. The file header is `; Type; Bits; Data;`.

# Decoded Signal List

Each decoded packet appears as a row with three columns: **Type** (protocol name), **Bits** (frame bit length), and **Age** (seconds since last received). The list deduplicates by signal content — repeated transmissions from the same remote update the age counter rather than adding new rows.

Selecting a row opens a detail view showing the protocol type, serial number, button code, counter value, and any additional decoded fields for that protocol.

For **KeeLoq** and **Superrollo** signals the detail view always shows the Fix code and the Encrypted hop value. The decrypted **Hop** value and the **Save** button are only shown when a matching manufacturer key is found in `KEELOQKEYS/MFCODES`. Without the key, the signal is received and displayed but cannot be decrypted and cannot be saved for retransmission.

When the Save button is available, it saves the decoded remote data to `KEELOQREMOTES/<name>.KEELOQ` on the SD card for use with the [KeeLoq TX](KeeLoq-TX) app.

# Supported Protocols

45 protocols are currently implemented, covering fixed-code and some rolling-code (KeeLoq) systems across the 300–868 MHz ISM bands:

Princeton, Bett, CAME, CAME Atomo, CAME Twee, Chamberlain Code, Clemsa, Doitrand, Dooya, FAAC, Gate TX, Holtek, Holtek HT12X, Holtek HT6P20B, Honeywell, Honeywell WDB, Hörmann, IDO, Intertechno V3, KeeLoq, Kingates Stylo 4K, Linear, Linear Delta 3, Magellan, Marantec, Marantec24, Mastercode, Megacode, Nero Radio, Nero Sketch, Nice FLO, Nice FLO RS, Phoenix V2, Power Smart, Security+ V1, Security+ V2, SMC5326, Somify Keytis, Somify Telis, Star Line, X10, Legrand, Gangqi, Restaurant Pager, Superrollo (GW60/HCS361).

> Note: Hörmann BiSecure (FM-based) is recognized but not implemented in this app as it requires FM demodulation.

# Superrollo (GW60/HCS361)

Superrollo GW60 remotes use the HCS361 rolling-code chip with a 67-bit OOK frame at Te=450 µs. SubGhzD decodes these signals and displays them as protocol type **Superrollo**.

Full workflow:
1. Tune to 433.92 MHz and press the Superrollo remote button.
2. The signal appears in the list as **Superrollo**, 67 bits.
3. Open the detail view — Fix code and Encrypted hop are always shown.
4. If a `Superrollo` entry exists in `KEELOQKEYS/MFCODES`, the decrypted Hop value and the **Save** button also appear.
5. Press Save, enter a filename — the decoded remote is saved to `KEELOQREMOTES/<name>.KEELOQ`.
6. Open [KeeLoq TX](KeeLoq-TX), load the file, and transmit.

Without a valid manufacturer key in MFCODES, steps 4–6 are not available. See [KeeLoq TX](KeeLoq-TX) for the MFCODES file format.

# Settings Persistence

The Log checkbox state is saved to `rx_subghzd.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.