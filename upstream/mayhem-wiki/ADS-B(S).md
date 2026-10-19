This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## WARNING

> **This is a potentially dangerous app. HackRF can generate valid ADS-B messages that, if radiated, can affect how real aircraft and navigation systems perceive each other. It must only be used in a completely closed RF environment with no live transmission into open air.**

* This application is intended solely for **experimental** purposes. It must not be used for any other reason.
* It is your responsibility to comply with all local, state, national, and international laws while using this application. Any illegal activities are strictly prohibited.
* This application is not suitable for use by individuals under the age of 18.
* All experiments conducted with this application are done entirely at your own risk. The developers are not liable for any damages or losses that may result.
* No form of assistance or support is provided for experiments conducted with this application. You are solely responsible for all outcomes and consequences.
* By using this application, you agree to indemnify and hold harmless the developers and all associated parties from any and all claims, damages, losses, liabilities, costs, and expenses arising from your use of this application or violation of these terms.
* This application is provided "as is" without warranty of any kind, express or implied.

---

ADS-B TX generates and transmits ADS-B Mode S messages at 1090 MHz, simulating an aircraft transponder. The transmitted frames can carry position, callsign, velocity, and squawk code data, which will be visible to ADS-B receivers and applications in range.

The ICAO24 address field is **shared across all four tabs** and is always active. The four tabs each add an independently toggleable message type to the transmission. Settings entered on each tab are **not saved to persistent memory** — only the TX frequency, gain, and RF amp settings are retained between sessions (via `tx_adsb.ini`).

## ICAO24 (All Tabs)

* **ICAO24**: The 6-digit **hexadecimal** address that uniquely identifies the transmitting aircraft (e.g. `4CA1E0`). This 24-bit code, sometimes called the Mode S address, is assigned to each registered aircraft. Enter using the encoder knob on each hex digit.

## Position Tab

Enable **Transmit position** to include airborne position messages (DF17 Type 9–18).

* **Alt**: Altitude in feet. Range: −1000 to 50000 ft.
* **Lat**: Latitude in Degrees° Minutes' Seconds". Degrees: −90 to +90; Minutes: 0–59; Seconds: 0–59. The decimal degree equivalent is displayed to the right.
* **Lon**: Longitude in Degrees° Minutes' Seconds". Degrees: −180 to +180; Minutes: 0–59; Seconds: 0–59. The decimal degree equivalent is displayed to the right.
* **Set from map**: Opens the map view. Tap the desired location on the touchscreen to transfer its coordinates into the Lat/Lon fields. An **OK** button confirms the selection — it is initially hidden behind the coordinate readout but appears when that area is tapped.

## Callsign Tab

Enable **Transmit callsign** to include aircraft identification messages (DF17 Type 1–4).

* **Callsign**: Up to 8 characters. Tap the callsign button to open the text entry pad. Default: `TEST1234`.

## Speed Tab

Enable **Transmit speed** to include airborne velocity messages (DF17 Type 19).

* **Speed**: Ground speed in knots. Range: 0–999 kn, step 5.
* **Bearing**: Ground track angle. Range: 0–359°, step 1. The compass rose in the upper-right corner shows the selected direction visually.
* **Vertical rate**: Climb/descent rate in feet per minute. Range: −4096 to +4096 ft/min, step 64 (per the ADS-B encoding standard). Positive values indicate climbing, negative values descending. The source is simulated as GNSS-derived.

## Squawk Tab

Enable **Transmit squawk** to include Mode A identity replies (DF17 squawk).

* **Squawk**: A 4-digit **octal** transponder code (each digit 0–7), giving 4096 possible codes (0000–7777). Certain codes carry standard meanings: 7700 = general emergency, 7600 = radio failure, 7500 = hijack.

## Common Controls (Bottom Bar)

* **Frequency**: Fixed at **1090.000 MHz** (the international ADS-B frequency). Editable but must not be changed for valid ADS-B simulation.
* **LNA gain** (0–47 dB) and **RF Amp** (0 or 14 dB): Standard TX gain controls.
* **Start / Stop**: Begins or ends the transmission. All enabled tabs transmit their frames in a repeating cycle.
 
![image](https://user-images.githubusercontent.com/86470699/210870176-ab71e12e-90ce-42a2-a90d-762e878aa835.png)
![image](https://user-images.githubusercontent.com/86470699/210870689-397eed6d-dba5-4664-bbd6-ca0afbba5e92.png)

