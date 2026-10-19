Receives and decodes telemetry from meteorological radiosondes — weather balloons that transmit GPS position, temperature, humidity, and other atmospheric data as they ascend.

# UI Overview

![image](https://github.com/user-attachments/assets/22ba8419-4d88-41a8-a9ad-0a9092142af1)

## Settings

* **Frequency**: The frequency to monitor. Default is **402.7 MHz**, which is the primary international radiosonde downlink band. Adjustable via the encoder knob or on-screen numpad.
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **RSSI**: Signal strength indicator.
* **Volume**: Audio output volume.

## Decoded Fields

The app displays a common set of fields for all sonde types. Fields that are not available for a given sonde type are shown as `...`. Vertical speed is calculated by the app from successive GPS altitude readings and packet timestamps.

| Field | Meteomodem M10 | Meteomodem M20 | Meteomodem M2K2 | Vaisala RS41-SG |
|-------|:--------------:|:--------------:|:---------------:|:---------------:|
| Type | ✓ | ✓ | ✓ | ✓ |
| ID / Serial | ✓ | ✓ | — | ✓ |
| DateTime | ✓ | ✓ | ✓ | ✓ |
| Battery voltage | ✓ | ✓ | ✓ | ✓ |
| Frame number | — | ✓ | — | ✓ |
| Temperature | ✓ | ✓ | — | ✓ |
| Humidity | ✓ | ✓ | — | ✓ |
| Pressure | — | ✓ | — | — |
| GPS (Lat / Lon / Alt) | ✓ | ✓ | ✓ | ✓ |
| Vertical speed | ✓ | ✓ | ✓ | ✓ |

## Checkboxes

* **Log**: Logs received packets to the SD card. A new timestamped file is created each time the app is opened: `LOGS/SONDE_YYYYMMDD_HHMMSS.TXT`. The log contains raw packet bit data and a reception timestamp.
* **CRC**: Enables CRC checking. When active, packets that fail their checksum are discarded rather than displayed. CRC is supported for M10, M20, and RS41-SG; M2K2 does not have a CRC implementation.

## Beep on Packet

The app emits an RSSI-level-dependent audio beep when a packet is received. The beep pitch corresponds to signal strength. This behaviour is controlled by the global **Beep on packets** setting in [Settings → Radio](Settings#radio), not by a per-app checkbox.

## Map Buttons

* **See QR**: Generates a `geo:latitude,longitude` QR code for the last received GPS fix. Scanning the code on a smartphone opens its map application at those coordinates.
* **See on map**: Opens the built-in world map view centred on the last received GPS fix. Requires `world_map.bin` to be present in the `/ADSB/` folder on the SD card.

## Settings Persistence

The Log and CRC checkbox states are saved to `rx_sonde.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.