
![RemoteUI](https://github.com/portapack-mayhem/mayhem-firmware/assets/3761006/b0c2245b-d7bd-480e-973a-77b062ac6bfc)
![RemoteEdit](https://github.com/portapack-mayhem/mayhem-firmware/assets/3761006/86783dbe-c51a-44ab-942b-743b9cb3c4c8)

The Remote app lets you create a custom button panel and bind each button to a capture file for one-touch playback.

Remote files (`.REM`) are stored in the `REMOTES/` folder on the SD card. New remotes are automatically named `REMOTE_0001.REM`, `REMOTE_0002.REM`, etc.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Main UI

* **Title** — The top line shows the remote's name. Select it to rename it (max 30 characters).
* **Buttons** — Up to 12 customizable buttons arranged in a 4×3 grid. Select a button to transmit its capture file. Select the same button again to stop. Long-press Select to open the button edit screen.
* **Waterfall** — A small waterfall display shown between the button grid and the bottom bar while transmitting.
* **Gain / Amp** — Transmitter gain and amplifier control (via the TX bar at the bottom). The indicator color reflects transmitter power.
* **Loop** — When checked, continuously retransmits the capture until stopped.
* **Filename** — Shows the current remote filename (without extension). Select it to rename the file.
* **Add button (+ icon)** — Adds a new empty button to the grid. New buttons open in edit mode the first time they are selected.
* **New remote (new-file icon)** — Saves the current remote and starts a new empty one.
* **Open remote (folder icon)** — Saves the current remote and opens an existing `.REM` file from the `REMOTES/` folder.

Remotes are automatically saved when the app exits.

## Button Edit UI

* **Name** — The text label shown on the button (max 30 characters).
* **Path** — Select to pick a capture file (`.C16` / `.C8`) from the `CAPTURES/` folder.
* **Freq** — The center frequency to transmit on. Defaults to the capture file's metadata frequency if a `.met` file is found, otherwise falls back to the current TX frequency.
* **Rate** — The sample rate read from the capture file's metadata, or 500 ksps if no metadata is found. Display only — cannot be changed here.
* **Icon** — Selects an icon to show on the button (index 0 = no icon; indices 1–24 select from the available icon set).
* **FG Color** — Foreground (text/icon) color index (0–20).
* **BG Color** — Background color index (0–20).
* **Preview** — Live preview of the button as it will appear in the main UI.
* **Trash (red)** — Deletes this button after a confirmation prompt and returns to the main screen.
* **Done** — Saves changes and returns to the main screen.

### Available colors (index → name)

| Index | Color | Index | Color | Index | Color |
|-------|-------|-------|-------|-------|-------|
| 0 | Black | 7 | Orange | 14 | Dark orange |
| 1 | White | 8 | Yellow | 15 | Dark yellow |
| 2 | Darker grey | 9 | Green | 16 | Dark green |
| 3 | Dark grey | 10 | Blue | 17 | Dark blue |
| 4 | Grey | 11 | Cyan | 18 | Dark cyan |
| 5 | Light grey | 12 | Magenta | 19 | Dark magenta |
| 6 | Red | 13 | Dark red | 20 | Purple |

## Technical details

| Parameter | Value |
|-----------|-------|
| Baseband bandwidth | 2.5 MHz |
| Sample rate | From capture metadata (or 500 ksps fallback) |
| Metadata fallback frequency | Current TX frequency |
| Settings file | `tx_remote.ini` |

## REM file format

Remote files are plain text and can be edited in any text editor. Empty lines and lines beginning with `#` are ignored.

* The first non-ignored line is the remote **title**.
* Each subsequent line (up to 12) defines one button in this comma-separated format:

```
capture_path,button_name,icon_index,bg_color_index,fg_color_index,center_frequency_hz,sample_rate_sps
```

**Example:**
```
My Remote
CAPTURES/door.C16,Door,6,3,1,433920000,500000
CAPTURES/lock.C16,Lock,0,17,1,433920000,500000
```

The order of buttons on screen matches the order of lines in the file, so buttons can be rearranged by reordering lines.

## Tips

* Use the [IQ Trim](https://github.com/portapack-mayhem/mayhem-firmware/wiki/IQ-trim) utility to trim silence from captures so they start transmitting instantly.
* If a `.txt` metadata file exists alongside a capture, its frequency and sample rate are used automatically.
* Button positions can be rearranged by editing the `.REM` file directly.