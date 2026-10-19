Waterfall Designer is a utility for creating and editing custom waterfall colour palettes. A live waterfall display is shown while editing so you can see the effect of your changes in real time. Profiles are saved as files in the `WATERFALLS/` directory on the SD card and can be applied to replace the active waterfall colour scheme.

> **Note:** Changes made while editing are previewed live but are automatically reverted when you leave the app — unless you explicitly press **Apply**. Only after pressing Apply is the palette permanently set as the active colour scheme.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Workflow

1. Press **New** to start a fresh profile, or **Open** to load an existing one from `WATERFALLS/`.
2. Select a signal level entry from the list (0–255, representing signal strength).
3. Press **Edit color** to open the colour picker and assign an RGB colour to that level.
4. Use **Add level** / **Remove level** to insert or delete colour stops in the palette.
5. Press **Save** to write the current profile back to its file in `WATERFALLS/`.
6. Press **Apply** to set this profile as the active waterfall colour scheme and exit.

# Controls

* **New**: Creates a new empty profile.
* **Open**: Opens the file manager to load a profile from `WATERFALLS/`.
* **Save**: Saves the current profile to disk. The filename is shown after saving.
* **Add level** (+): Adds a new colour stop to the palette.
* **Remove level** (−): Removes the currently selected colour stop.
* **Edit color**: Opens the colour picker sub-view for the selected level.
* **Apply**: Applies the current profile as the active waterfall palette and exits the app.

# Colour Picker

When editing a colour stop the following fields are available:

* **Index**: The signal level this colour applies to (0–255). 0 = weakest signal (background), 255 = strongest.
* **R / G / B**: Red, Green, Blue components, each 0–255.
* **Step**: Increment size for encoder knob adjustments on the R/G/B fields.
* **Save**: Confirms the colour and returns to the main view.

# RF Settings

The live waterfall display is fully functional while editing — you can tune to a real signal to judge how your palette looks on actual data.

* **Frequency** and **frequency step**: Standard RX frequency controls.
* **RF Amp**, **LNA**, **VGA**: Standard gain controls.

# Files

Profile files are stored in `WATERFALLS/` on the SD card. Settings are saved to `rx_wtf_designer.ini`.