ACARS (Aircraft Communications Addressing and Reporting System) is a digital data link protocol used to exchange short messages between aircraft and ground stations over VHF radio. This app decodes ACARS frames and displays the extracted fields in a scrolling console.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Settings

* **Frequency**: Default **131.825 MHz** (primary ACARS VHF frequency in Europe and globally). Adjustable via encoder knob or tap for keypad. Other common frequencies include 129.125 MHz and 130.025 MHz depending on region and airline.
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain.
* **LOG**: Checkbox to enable logging to file. When checked, decoded messages are written to `LOGS/ACARS.TXT`. The log file is opened automatically on startup; the checkbox controls whether entries are written.

# Decoded Message Fields

Each received and CRC-verified ACARS frame is decoded into the following fields, displayed in the console:

* **CRC**: `OK` if the CRC-16/CCITT checksum over the frame matches the two trailing CRC bytes; `FAIL` otherwise. Frames with CRC failures are still displayed but should be treated as potentially corrupt.
* **Registration**: 7-character aircraft registration (tail number), e.g. `D-ABCD` or `N12345`.
* **Label**: 2-character message type code identifying the category of message (e.g. flight plan update, ATIS, position report).
* **BlockID**: 1-character sequence counter for multi-block messages.
* **MsgNum**: 3-character message number within the current session.
* **FlightID**: 6-character flight identifier, typically the IATA flight number.
* **Message**: Free-text payload of variable length. Content depends on the label type and airline ground system.

A minimum valid frame must be at least 23 bytes (21-byte fixed header + 2 CRC bytes). Frames shorter than this are shown with an error message in the text field instead of decoded content.

# Logging

When **LOG** is enabled, each decoded message is written as a single timestamped entry to `LOGS/ACARS.TXT`. The file is always opened on launch; entries are only written when the checkbox is active. Settings are saved to `rx_acars.ini`.