TPMS TX transmits simulated Tire Pressure Monitoring System (TPMS) sensor signals. It is the companion transmitter to [TPMS Rx](TPMS-Rx) and can replay sensor data previously saved by the receiver app.

> **Note:** Transmitting fake TPMS signals in the 315 or 433 MHz band may interfere with vehicle dashboard readings. Use only on your own vehicles and equipment in a controlled environment.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Settings

* **Frequency**: **314.9 MHz**, **315.0 MHz**, or **433.9 MHz**. Default: 314.9 MHz.
* **Sensor type**: **Schrader**, **FLM_64**, **FLM_72**, **FLM_80**, or **GMC_96**. Determines the encoding and signal type used.
* **Pressure unit**: kPa, PSI, or BAR.
* **Temperature unit**: °C or °F.
* **Transponder ID**: 24-bit or 32-bit hexadecimal sensor ID depending on sensor type.
* **Pressure**: Pressure value to transmit. Maximum is 340 kPa for Schrader/FLM types, 701 kPa for GMC_96. A `!MAX` warning is shown if the value exceeds the type's encoding limit.
* **Temperature**: Temperature value to transmit.
* **Flags**: Additional status flags byte.
* **Repeat**: Number of transmission repetitions. Default: 5.
* **Load**: Load a previously saved sensor file from `TPMS/TPMS_.TXT` (files created by the TPMS RX app's Save button).
* **Save**: Save the current settings to a file in the `TPMS/` directory for later replay.
* **Transmit / Stop**: Starts or stops the transmission.

# Settings Persistence

Pressure unit and temperature unit are saved to `tx_tpms.ini`.