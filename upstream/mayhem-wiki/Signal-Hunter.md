# Signal Hunter

**Signal Hunter** is an external app that automatically detects RF energy above a configurable threshold and captures the signal to the SD card as a `.C16` file. It supports monitoring a single fixed frequency or hopping through a list of frequencies loaded from a freqman file.

This is an [external app](External-apps-informations) and must be present on the SD card in the `APPS/` folder.

# Features

* Energy-based signal detection using a sliding-window power measurement
* 8 ms pre-trigger IQ ring buffer — captures signal preamble before threshold crossing
* Automatic `.C16` capture to SD card on trigger
* Configurable energy threshold, hang time, and hop dwell time
* Single-frequency and frequency-hopping modes
* Hit counter tracks how many trigger events occurred in the current session

# User Guide

## Top bar

* **LNA / VGA / AMP** — Gain controls, shared across all tabs.
* **RSSI bar** — Live signal strength indicator.

## Tab 1 — Main

The main status and control screen.

* **Frequency display** — Shows the frequency currently being monitored in large digits. Turns red while a capture is in progress.
* **Status** — Shows `IDLE` when stopped, `HUNTING...` (green) while active.
* **START / STOP** — Begins or halts the hunt. In HOP mode the first frequency in the loaded list is selected automatically on start.
* **Hits** — Running count of trigger events since the last START.

## Tab 2 — Freqs

Frequency list management for HOP mode.

* **LOAD FILE** — Opens the file browser to select a freqman `.TXT` file. All frequencies in the file are loaded and HOP mode is activated automatically.
* **CLEAR** — Clears the loaded frequency list and returns to SINGLE mode.
* **Dwell Time (ms)** — How long (in milliseconds) the app stays on each frequency before hopping to the next. Range: 10–9999 ms, default: 200 ms.
* **Loaded info** — Shows the number of frequencies currently loaded.

## Tab 3 — Config

Detection parameters and mode selection.

* **MODE button** — Displays the current mode (`SINGLE` or `HOP`). Switches between modes. In SINGLE mode, one fixed frequency is monitored. In HOP mode, the app cycles through the loaded frequency list.
* **Frequency field** *(SINGLE mode only)* — The frequency to monitor. Default: 433.920 MHz.
* **Energy Threshold** — Minimum sliding-window power level required to trigger a capture. Range: 100–99999, default: 5000. Lower values trigger on weaker signals; raise it to ignore noise.
* **Hang Time (ms)** — How long after signal energy drops below the threshold before the capture is closed. Range: 10–5000 ms, default: 500 ms.

> [!NOTE]
> Changes to Config settings take effect only after stopping and restarting the hunt ("Restart HUNT after change").

# How it works

The baseband processor samples at 2 MHz and decimates by 8 to 250 kHz. A 64-sample sliding window continuously measures signal energy. When the window sum exceeds the **Energy Threshold**, a trigger fires:

1. The pre-trigger ring buffer (~8 ms of IQ data) is flushed first, capturing the signal preamble.
2. Capture continues until the signal falls below threshold and the **Hang Time** elapses.
3. The `.C16` file is saved to the `CAPTURES/` folder on the SD card.
4. The hit counter increments and the frequency display returns to its normal color.

In HOP mode the receiver steps to the next frequency after each dwell period, regardless of whether a signal was detected.

# File format

Captures are saved as standard `.C16` IQ files in the `CAPTURES/` folder and can be replayed using the [Replay](Replay) app.

Frequency lists for HOP mode use the standard freqman `.TXT` format, the same files used by the [Scanner](Scanner) and [Recon](Recon) apps. Files are typically stored in the `FREQMAN/` folder.