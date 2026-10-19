![image](https://github.com/user-attachments/assets/be5064b5-c7c7-42de-b535-2b302b04072b)

The scanner steps through approximately 20 frequencies per second, pausing 50 ms per frequency to allow the receiver to stabilize after retuning.

When a signal above the squelch threshold is found, the scanner locks onto that frequency for up to 500 ms (10 × 50 ms cycles) to confirm the signal is still present before pausing — this avoids stopping on spurious peaks.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Big Numbers Frequency

The large frequency display uses a colour code to indicate scanning state:

* **Grey**: Scanning or idle
* **Yellow**: Analyzing — possible signal detected, confirming
* **Green**: Signal confirmed and locked; audio active if above squelch

## Scan vs Search Modes

The scanner operates in two modes, toggled with the `SRCH`/`SCAN` button (which shows the mode that will be switched *to* when pressed):

* **Scan mode**: Steps through a list of discrete frequencies loaded from a freqman file.
* **Search mode**: Steps sequentially through all frequencies between a start and end frequency at a chosen step size.

## Frequency List

On startup the app loads from `FREQMAN\SCANNER.TXT` by default. Use the `LOAD` button to select a different freqman file. If app settings are enabled, the last used file is restored on the next startup.

If the loaded file contains a frequency *range* entry (`a=`, `b=`, `s=`), the start, end, and step fields are populated from it. Only one search range per file is supported. You can also set the search range manually by editing the SRCH START and END fields and the STEP selector directly.

Use the [Freq manager](Freq-manager) app to create or edit freqman files.

### Manually Selecting Entries or Frequencies

Whenever the ``/`` button is highlighted, the encoder knob scrolls through the frequency list (Scan mode) or through the search range (Search mode), regardless of whether Pause is currently active. The current item field `X / Y` can also be focused and used with the encoder knob in the same way.

## Radio Settings

* **LNA / VGA / AMP**: Gain settings. AMP: 0 = 0 dB, 1 = 14 dB. LNA: 0–40. VGA: 0–62. These are preserved per app if **App Settings** is enabled.
* **VOL**: Audio output volume.
* **BW**: Signal bandwidth. Available values depend on the selected **MODE**.
* **SQ**: Squelch threshold in dBm (range −90 to +20, default −30). When scanning, the scanner pauses on any frequency whose signal level exceeds this value. When paused for any reason, audio is enabled or muted based on this threshold.
* **MODE**: Modulation mode — AM (DSB 9k, DSB 6k, USB+3k, LSB−3k, CW), NFM, or WFM.
* **STEP**: Frequency step used for sequential Search mode.

## Buttons

* `LOAD`: Loads a freqman file (from the `FREQMAN/` directory) into the scan list and/or search range fields.
* `MCLR`: Clears the in-memory frequency list. Does not modify any file on the SD card. Frequencies can be re-added using `ADD FQ` or `LOAD`.
* `SRCH`/`SCAN`: Toggles between Search mode and Scan mode.
* ``/``: Manually pauses or resumes scanning. When this button is highlighted, the encoder knob can be used to step through frequencies. The squelch threshold still controls audio output while paused.
* `FORWARD`/`REVERSE`: Changes scanning direction. The button label shows the direction that will be activated when pressed.
* `MIC TX`: Opens the Microphone Transceiver app for 2-way radio operation.
* `AUDIO`: Opens the Audio Receivers app for further signal analysis.
* `DEL FQ`: Removes the currently displayed frequency from the in-memory scan list. Does not modify the file on the SD card.
* `ADD FQ`: Appends the currently displayed frequency to the **currently loaded freqman file** on the SD card. If the frequency already exists in the file, an error is shown. The entry is also added to the in-memory list if it is below the per-file limit.

## Delay Settings

* **Wsa** (Wait while Signal Active, default 5 s, range 0–99): Time to stay on an active frequency before skipping to the next one, even if a signal is still present. Set to 0 to remain on the frequency indefinitely until the encoder knob is used or the signal drops. A non-zero Wsa is also called "Browse" mode.
* **Wsl** (Wait after Signal Loss, default 2 s, range 0–99): Time to remain on a frequency after the signal drops below the squelch threshold before moving on.

## Other Fields

The `X / Y` field shows the current frequency index and the total number of entries in the scan list. If the loaded file is at the maximum freqman entry limit, `(DB MAX!)` is shown. If a description is available for the current entry, it appears above the big frequency display; otherwise the loaded filename is shown, or `SEARCHING...` in Search mode.

## Freqman File Format

See [Freqman Manager](Freq-manager).

## Settings Persistence

Wsa, Wsl, squelch, search range, and the last-loaded freqman file are saved to `rx_scanner.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.

## Example: Using Scanner as a Broadcast FM Radio Tuner

1. Press `LOAD`, select `FM_STANDARD_BAND.TXT`, and confirm. This loads the FM search range, step, mode (WFM), and bandwidth.
2. Optionally adjust VOL, SQ, gain settings, and Wsa.
3. Press `` to stop automatic scanning.
4. Navigate focus to the ``/`` button. When highlighted, use the encoder knob to tune to an FM station.
5. Press `ADD FQ` to save the current frequency to the loaded file. Repeat to store additional stations.
6. In future sessions, load the same file and Scanner will cycle through the saved stations, spending Wsa seconds on each. Press `` to stop on a station; use the encoder knob to change stations manually.

## Also see: Recon app

The [Recon](Recon) app is a more fully-featured scanner application for advanced use cases.