
# The UI

![Playlist](https://github.com/portapack-mayhem/mayhem-firmware/assets/3761006/8e494c6a-bed6-43f8-8af0-aca58f7958ff)

Replay transmits captured IQ files (`.C16` or `.C8` or `.CU8`) over the air. Files can be played individually or organized into a playlist (`.PPL`) for sequential playback with optional delays between entries.

# Display

* **Line 1**: Name of the currently loaded capture file.
* **Line 2**: Frequency (editable) and sample rate of the current track. Two stacked progress bars on the right — the top shows position within the playlist, the bottom shows transmit progress of the current file.
* **Line 3**: Duration of the current track in seconds. TX gain (0–47), TX amp (0/14), Loop checkbox (default: on), and the play/stop button.
* **Line 4**: Current track number / total tracks (e.g. `1/2`) on the left, current playlist filename on the right.

A live waterfall is displayed below the controls during transmission.

# Controls

* **◄ / ►**: Navigate to the previous or next track in the playlist.
* **📄 (Add file)**: Opens the file picker to select a `.C16` or `.C8` or `.CU8` capture file and append it to the end of the playlist.
* **🗑 (Delete)**: Removes the currently selected track from the playlist.
* **📂 (Open)**: Opens the file picker to load a `.PPL` playlist file. This replaces the current playlist.
* **💾 (Save)**: Saves the current playlist to the active `.PPL` file.
* **Loop** (checkbox, default: on): When enabled, the playlist restarts from the beginning after the last track finishes.
* **▶ / ■**: Start or stop playback.

The frequency field is editable per-track and is not saved to the playlist file.

# Playing a Single File

When the app opens with an empty playlist, the Add file button is automatically focused. Press it, select a `.C16` or `.C8` or `.CU8` file, and the play button receives focus immediately — allowing fast two-button playback.

You can also open a capture or playlist file directly from the File Manager app, which will launch Replay with that file pre-loaded.

# Playlist Files

Playlist files use the extension `.PPL` and are stored in the `PLAYLIST/` directory on the SD card. They are plain text, comma-delimited files.

**Format:**
```
ABSOLUTE_PATH_TO_FILE,DELAY_MS
# Comment lines starting with # are ignored
```

The delay (in milliseconds) is optional. If omitted, no pause is inserted between tracks.

> [!WARNING]
> The pre-delay is implemented as a blocking sleep on the UI thread. Setting a long delay will cause the device to appear frozen for that duration. There is no way to interrupt it other than resetting the device.

**Example:**
```
# Playlist file
/SAMPLES/TeslaChargePort_US.C16
/SAMPLES/TeslaChargePort_EU_AU.C16,100
```

This plays the US file, then pauses 100 ms, then plays the EU/AU file.

When a new capture file is added to an empty playlist, a new playlist file is created automatically with the name `PLAY_XXXX.PPL` in `PLAYLIST/`. The playlist is not saved to disk until you press the Save button.

**Metadata fallback:** If a capture file has no matching `.TXT` metadata file, the current transmit frequency and a sample rate of 500,000 Hz are assumed.

# Settings Persistence

Settings are saved to `tx_replay.ini`.