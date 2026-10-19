> **Legal warning:** Transmitting remote keyless entry signals to vehicles you do not own is illegal in most jurisdictions and may constitute attempted vehicle theft or unlawful interference with a radio device. Use only on your own vehicle for testing and research purposes.

Key fob TX transmits fixed-code remote keyless entry (RKE) signals for compatible vehicle remotes. Currently only **Subaru** is supported. The transmitted frame is a fixed OOK-encoded signal — it does not use rolling codes (KeeLoq). It is transmitted 4 times in sequence at 433.920 MHz.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Settings

* **Make**: Vehicle manufacturer. Currently: **Subaru** only.
* **Command**: The remote command to transmit:
  + **Lock**
  + **Unlock**
  + **Trunk**
* **Payload A / Payload B**: The raw hexadecimal frame bytes, updated automatically when Make or Command is changed. Can also be edited manually for experimentation.
* **Transmit / Stop**: Starts or stops the 4-repeat transmission sequence.

# Settings Persistence

Settings are saved to `tx_keyfob.ini`.