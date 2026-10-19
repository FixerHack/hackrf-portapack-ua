![](https://github.com/htotoo/ESP32-Portapack/blob/main/ScreenShots/foxhunt.png?raw=true)

The Fox Hunt app is designed to help with [transmitter hunting](https://en.wikipedia.org/wiki/Transmitter_hunting) (also known as fox hunting). Its use is not limited to the game — it can be used to locate any AM signal source.

The receiver demodulates in **AM mode only** and outputs audio through the speaker. Fox hunt transmitters typically send [Morse code](https://en.wikipedia.org/wiki/Morse_code), which can be heard directly. A real-time RSSI graph and power level display help judge signal strength changes as you move toward or away from the source.

The app integrates with external GPS and orientation (compass) modules to show your current position and heading on a built-in map, and allows you to drop markers at bearing positions to triangulate the transmitter's location.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

**Top row:**

* **Frequency:** The frequency to monitor. Use the rotary encoder to step in **100 Hz increments** (very fine tuning, useful for centering on a weak AM carrier), or click to open the numeric keypad.
* **AMP:** RF preamplifier — 0 = off, 1 = on (+14 dB). Use with caution near strong signals.
* **LNA:** Low Noise Amplifier gain (0–40 dB).
* **VGA:** Variable Gain Amplifier / baseband gain (0–62 dB).
* **Volume:** Audio output level.

**Below frequency row:**

* **Power: X db** — Displays the current peak channel power in dB. Updates in real time.
* **Mark** — Drops a marker at your current GPS position and compass bearing. Use this when the signal peaks in a particular direction, then move to a new position and mark again.
* **Clear** — Removes all previously placed markers from the map.

**RSSI graph:**

A scrolling bar graph (64 columns) showing the history of minimum, average, and maximum RSSI values alongside the peak power. This gives a visual trend of signal strength over time, helping identify whether you are approaching or moving away from the transmitter.

**Map:**

The lower portion of the screen shows a geographical map. The map auto-follows your GPS position — it is not manually scrollable. If an orientation module is connected, a directional arrow shows your current heading. Dropped markers (from the **Mark** button) appear on the map and remain until **Clear** is pressed.

Zooming in the map helps significantly when navigating to a nearby transmitter — use the encoder or touch to zoom.

# External modules

The app benefits from two optional external modules connected via the PortaPack's I²C/GPIO expansion port:

* **GPS module** — Provides real-time position updates. The map centres on your location and tracks movement automatically.
* **Orientation / compass module** — Provides a bearing angle. The map displays a heading arrow. Each marker stores the bearing at the moment it was dropped, which is useful for triangulation (two or more bearings from different positions narrow down the transmitter's location).

Without these modules the map is static and markers cannot be placed.

# Typical usage

1. Tune to the known fox hunt frequency.
2. Adjust LNA and VGA so the signal is audible but not overloaded.
3. Move to an open area and rotate — the RSSI graph and Power indicator will peak when pointing toward the source.
4. Press **Mark** to record your bearing and position.
5. Move to a second location at least 50–100 m away, repeat, and press **Mark** again.
6. The intersection of the two bearing lines (visible on the map) indicates the transmitter's approximate position.

# Settings persistence

The last used frequency and gain settings are saved automatically and restored on next launch. Settings are stored in `SETTINGS/rx_foxhunt.ini` on the SD card.