> **Legal warning:** Brute-forcing remote control codes to operate devices you do not own or are not authorised to control is illegal in most jurisdictions. This includes garage doors, gates, barriers, and building access systems belonging to others. Use only on your own equipment for legitimate security testing.

OOK Brute sequentially transmits all OOK remote control codes within a configurable range for a selected protocol. It is intended for testing the code space of fixed-code OOK remote systems — for example, verifying that your own receiver responds to the correct code, or auditing the security of a system you own.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Settings

* **Protocol**: The OOK encoding standard to brute-force:
  + **Came12** — CAME 12-bit fixed code
  + **Came24** — CAME 24-bit fixed code
  + **Nice12** — Nice 12-bit fixed code
  + **Nice24** — Nice 24-bit fixed code
  + **Holtek12** — Holtek HT12E 12-bit fixed code
  + **Princeton24** — Princeton PT2262 24-bit fixed code
* **Start**: First code to transmit (decimal). Can be entered via the on-screen keypad button.
* **Stop**: Last code to transmit (decimal). The app iterates from Start to Stop inclusive.
* **Frequency**: Default 433.920 MHz. Editable.
* **Start / Stop button**: Begins or halts the brute-force sequence.

# Settings Persistence

Settings are saved to `tx_ookbrute.ini`.