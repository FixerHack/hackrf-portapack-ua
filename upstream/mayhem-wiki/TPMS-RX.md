![image](https://github.com/user-attachments/assets/43efc797-9278-4e6b-945b-7fa71547d7da)

Tire Pressure Monitoring System (TPMS) sensors transmit in licence-free ISM bands — 315 MHz in North America and 433.92 MHz in Europe and most of the rest of the world. This app decodes TPMS transmissions and displays tyre pressure, temperature, sensor ID, and status flags in a live list.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Settings

* **Frequency**: Three options are available — **314.9 MHz**, **315.0 MHz**, and **433.9 MHz**. Both 314.9 and 315.0 are provided because "315 MHz" sensors may actually transmit at either frequency; the default is 314.9 MHz.
* **Pressure unit**: **kPa**, **PSI**, or **BAR**. Selectable inline; applies to both the list view and detail view.
* **Temperature unit**: **°C** or **°F**. Selectable inline.
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).

# Decoded Signal List

Each row in the list represents one unique sensor (identified by type + ID). The columns are:

* **Tp**: Sensor type number (shown as a 2-digit number in the list; the detail view also shows the name). Currently decoded types:
  + `0` = None
  + `1` = FLM_64
  + `2` = FLM_72
  + `3` = FLM_80
  + `4` = Schrader
  + `5` = GMC_96
  + `9` = Renault
  + `10` = Hyundai-VDO

  Renault and Hyundai-VDO are decoded from the same FSK 19k2 Schrader baseband path as the FLM types — no extra baseband signal path is needed for them.

  The firmware also contains CRC-verified decoders for further sensor types (Toyota, Ford, Citroen, Nissan, Kia, Abarth124, Jansite, Jansite-Solar, Elantra2012, PMV-107J, Renault-0435R, AVE). These are present in the code but are **not yet wired into the active decode path**, so they do not currently appear in the list — most of them require additional baseband signal paths (other modulations/baud rates) that are not implemented yet.
* **ID**: The 8-digit hexadecimal sensor ID. Note: some sensors print their ID in decimal on the housing.
* **Pres**: Tyre pressure in the selected unit (kPa, PSI, or BAR).
* **Temp**: Temperature in the selected unit (°C or °F). Spurious readings can occur due to receive errors, unsupported sensor models, or failing sensors — compare against the vehicle's dashboard reading where possible.
* **Cnt**: Number of packets received from this sensor since the app was opened.
* **Fl**: Sensor flags as a 2-digit hexadecimal value. The meaning of individual flag bits varies by sensor manufacturer and model.

Selecting a row opens a detail view with all fields expanded. A **Save** button in the detail view writes the sensor data to `TPMS/TPMS_.TXT` in a format compatible with the TPMS TX app.

# Transmission Behaviour

Each sensor transmits at intervals that vary from a few seconds to several minutes, depending on the vehicle and sensor model. Transmission is typically triggered by wheel movement or by a rapid pressure change. Most sensors can also be triggered immediately using a TPMS activation tool operating at 125 kHz.

# Logging

When an SD card is present on app startup, received packets are automatically logged to `LOGS/TPMS.TXT`. Each log entry contains a timestamp in `YYYYMMDDHHMMSS` format, followed by the receiver frequency, signal type (`FSK 38400 19200 Schrader`, `OOK - 8192 Schrader`, or `OOK - 8400 Schrader`), the raw Manchester-decoded hex data, a `/` separator, and a per-bit Manchester coding error indicator.

# Settings Persistence

The selected pressure unit and temperature unit are saved to `rx_tpms.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.