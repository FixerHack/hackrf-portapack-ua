![image](https://github.com/user-attachments/assets/f1efc269-566f-4b67-be42-1c820bb39cc4)

The Weather app decodes wireless temperature and humidity transmissions from consumer weather stations operating in the ISM licence-free bands. It receives AM-mode OOK signals and presents a live list of decoded sensor readings, updated in real time.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Settings

* **Frequency**: Default 433.920 MHz. Adjustable in 10 kHz steps using the encoder knob, or tap to open the keypad. Common frequencies are listed below.
* **Temperature unit**: **°C** or **°F**. Applies to both the list view and detail view.
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier. Use with caution on strong nearby signals.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain.
* **Volume**: Volume for packet beep tones. Only active when **Beep on packets** is enabled in the global [Settings](Settings#audio).
* **Clear**: Clears the in-memory sensor list. Does not affect any log file.
* **Log**: Checkbox to enable CSV logging. When checked, a new log file is created immediately. The log state is saved to `rx_weather.ini` and restored on next launch — if it was enabled when you last left the app, logging resumes automatically on the next startup.

> **Gain tip:** This app is sensitive to signal strength. If nothing decodes, try starting with AMP 0, LNA 32, VGA 20, and adjust from there. Both over-amplification and under-amplification will prevent decoding.

# Common Frequencies

* **433.92 MHz** — Europe, most of the world
* **315 MHz** — North America, Japan
* **868 MHz** — Europe and others
* **915 MHz** — North America, Japan

# Sensor List

Each row represents one unique sensor. Entries are kept for up to 64 sensors at a time. Columns:

* **Type**: Sensor protocol name (see Supported Protocols below).
* **Temp**: Temperature in the selected unit.
* **Hum**: Relative humidity in percent, or `–` if the sensor does not transmit humidity.
* **Ch**: Channel number reported by the sensor, or `–` if not applicable.
* **Age**: Seconds since the last packet was received from this sensor. Resets to 0 on each new reception.

Selecting a row opens a **detail view** with all fields expanded: Type, Id (hexadecimal), Temperature, Humidity, Channel, Battery status (OK / LOW), and Age. Press **Done** to return to the list.

# Logging

When the **Log** checkbox is enabled, received sensor data is written to `LOGS/WEATHERLOG_.CSV` on the SD card. The file starts with the header line:

```
;Type; id; Temp; Hum; CH; Batt
```

Each subsequent line contains one decoded sensor reading in the same column order.

# Supported Protocols

26 protocols are decoded:

Acurite592TXR, Acurite5in1, Acurite606TX, Acurite609TX, Acurite986, Ambient, AuriolAhfl, AuriolTH, Bresser3CH, EmosE601x, GT-WT02, GT-WT03, InFactory, Kedsum, LaCrosse TX, LaCrosse TX141THBv2, NexusTH, Oregon2, Oregon2B, Oregon3, OregonV1, SolightTE44, ThermoPro TX4, TX 8300, Vauno EN8822, Wendox W6726

# Settings Persistence

The temperature unit and log state are saved to `rx_weather.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.