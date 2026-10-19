# Screenshots

The camera icon in the [[Title-Bar|title bar]] takes a screenshot of the current display and saves it to the SD card.

## File details

Screenshots are saved as 24-bit RGB PNG files in the `SCREENSHOTS/` folder on the SD card:
```
SCREENSHOTS/SCR_0000.PNG
SCREENSHOTS/SCR_0001.PNG
...
```

The counter increments automatically based on the highest existing file. Numbering starts at `SCR_0000.PNG` when the folder is empty. Up to 10,000 screenshots (0000–9999) can be stored; once the counter is exhausted, no further screenshots are saved.

The display is 240×320 pixels. File sizes vary depending on screen content due to PNG compression — typically around 90–150 KB for most app screens.

## How to take a screenshot

**From the device:** Tap the camera icon in the title bar. The icon can be hidden via **Settings → User Interface** — if it is not visible, enable it there first.

**Via USB Serial Console:** The `screenshot` command saves a screenshot with the same naming scheme:
```
screenshot
```

See [[USB-Serial-Console]] for how to connect and use the serial shell.

> [!NOTE]
> The `SCREENSHOTS/` directory is created automatically on first use if it does not already exist.