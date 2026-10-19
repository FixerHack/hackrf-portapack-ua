
   [[img/screenshots/Calls.png]]

The Search app continuously sweeps a defined frequency range using FFT spectrum analysis and locks onto any signal that rises above a configurable power threshold. It is designed for passive signal detection — it does not demodulate audio during scanning, but logs the frequency, time, and duration of each detected signal.

# UI Overview

## Settings

* **Min / Max**: The frequency range to search. Default is 100 MHz to 400 MHz. Settings are saved per app (see [Settings Persistence](#settings-persistence)).
* **LNA** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA** (0–62): Variable-gain amplifier gain. There is no RF amplifier control in this app; the amp is always off.
* **Trig** (5–255, step 5, default 80): Power threshold for signal detection. A signal is detected when its FFT bin power exceeds `Mean + Trig`. Set this higher to ignore weaker signals and reduce false triggers; lower to catch weaker signals.
* **Snap to**: When enabled, the detected frequency is rounded to the nearest step before being displayed and logged. Available snap steps: 25 kHz, 12.5 kHz, 8.33 kHz, 2.5 kHz, 500 Hz. Default is 12.5 kHz (enabled).
* **LOG**: When checked, creates a timestamped CSV log file on the SD card each time it is enabled (see [Logging](#logging)).

## Status Indicators

* **Mean**: The average FFT power across all bins in the current scan, shown as a value from 0–255. The detection threshold is `Mean + Trig`. Setting Trig above the noise floor is the primary tuning task for this app.
* **Slices**: The number of 2.5 MHz slices the scan range has been divided into, shown as `X / 32`. Each slice is one FFT capture. The maximum supported span is 80 MHz (32 slices).
* **Rate**: The detection update rate in Hz, indicating how many full scan sweeps are completed per second.
* **VU meter**: Displays the peak FFT power across all bins. The marker line indicates the current detection threshold (`Mean + Trig`).
* **Timer**: A progress bar showing the detect or release countdown (see [Detection Timing](#detection-timing)).
* **Status text**: Shows the current state — `Listening`, `Locked!`, or `Out of range`.

## Big Frequency Display

Shows the frequency of the currently detected or locked signal. When a signal is found outside the configured Min/Max range, it is shown as `Out of range` and displayed in grey.

## Spectrum Display

A colored gradient spectrum bar is shown across the screen, representing the FFT power across the entire scanned range. This provides a visual overview of band activity.

## Frequency Log Table

The lower portion of the screen is a running log of all signals that were locked during the session, showing frequency, time of detection, and duration (in 100 ms units). Selecting an entry from the log opens the frequency entry screen, where the frequency can be saved to a freqman file on the SD card.

# Detection Timing

The app operates in 100 ms timing units:

* **Detection**: A signal must remain above the threshold for **500 ms** (5 × 100 ms) before it is locked. This prevents single-frame noise spikes from being logged.
* **Release**: Once locked, a signal is released **600 ms** (6 × 100 ms) after it drops below the threshold. The duration logged is the time from lock to release.

# Frequency Accuracy

Each FFT bin covers approximately 9.8 kHz (2.5 MHz ÷ 256 bins). The raw frequency resolution is therefore **±4.9 kHz**. Enabling **Snap to** rounds the result to a grid, which can improve readability for known channel plans.

# Logging

When **LOG** is enabled, a new CSV file is created at the start of the session: `LOGS/SEARCH_YYYYMMDD_HHMMSS.CSV`. The format is semicolon-delimited: `Time;Freq;Duration;`. A new file is created each time LOG is toggled on; existing files are not appended to.

A beep is emitted on signal lock if **Beep on packets** is enabled in the global [Settings → Radio](Settings#radio) menu.

# Settings Persistence

The power threshold, Min/Max frequencies, and Snap settings are saved to `rx_search.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.