> [!WARNING]
> This application transmits RF signals that may cause interference. Use only for authorised testing on equipment you own or have explicit permission to test. Jamming is illegal in most jurisdictions.

Hopper transmits on a user-defined list of frequencies, cycling through all of them using the jammer baseband. All listed channels are active simultaneously within the baseband; the "hop" interval controls how long each transmission burst lasts before moving to the next channel. It is designed for testing multi-channel interference resilience on systems you own.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# SD Card Setup

Frequency lists are stored as `.PHOP` files in the `HOPPER/` directory at the root of the SD card. Each line in the file contains one frequency in Hz. Lines starting with `#` are treated as comments and skipped.

**Example file (`HOPPER/mylist.PHOP`):**
```
# My test frequencies
433920000
315000000
868000000
```

Up to **80 frequencies** can be loaded. Additional entries beyond the limit are ignored.

# Controls

* **📁 (Load)**: Opens a file browser in `HOPPER/`, filtered to `.PHOP` files. Replaces the current list.
* **💾 (Save)**: Prompts for a filename and saves the current frequency list as a `.PHOP` file in `HOPPER/`.
* **➕ (Add)**: Opens the frequency keypad to add a single frequency to the current list.
* **🗑 (Delete)**: Removes the currently highlighted frequency from the list.
* **🧹 (Clear)**: Clears the entire frequency list after confirmation.
* **START / STOP**: Begins or ends transmission.

# Settings

* **Type**: Signal type generated on each channel. Options (with defaults in bold):
  * `Rand FSK` — Random FSK noise
  * `FM tone` — FM-modulated tone
  * `CW sweep` — Continuous wave sweep
  * **`Rand CW`** — Random amplitude CW (default)
  * `Sine` — Sine wave
  * `Square` — Square wave
  * `Sawtooth` — Sawtooth wave
  * `Triangle` — Triangle wave
  * `Chirp` — Linear frequency chirp
  * `Gauss` — Gaussian noise
  * `Brute` — Broadband noise

* **Speed**: Modulation speed / symbol rate within each channel:
  * `10 Hz`, `100 Hz`, `1 kHz`, **`10 kHz`** (default), `100 kHz`

* **Hop**: Dwell time per channel before switching:
  * **`0ms !!`** — Fastest possible; **causes the HackRF UI to freeze**. Press the hardware RESET button to recover.
  * `1ms`, `10ms`, **`50ms`** (default), `100ms`, `1s`, `2s`, `5s`, `10s`

* **TX** (1–180 seconds): How long the app transmits before entering the sleep/pause period.

* **Sle3p** (1–60 seconds): Duration of the pause (cooldown) between TX bursts. During the pause the transmitter is disabled. This TX→pause cycle repeats continuously while running.

* **Jitter** (1–60, unit: /60 seconds): A random offset applied to the TX and pause timers using an LFSR sequence, preventing a perfectly regular duty cycle. Higher values mean more timing variation.

* **Gain** (0–47): TX gain.
* **A** (0/1): RF amplifier on/off.

# Frequency Counter

The display shows the current channel number and total number of active channels (e.g. `03/05`) as the baseband cycles through them.

> [!NOTE]
> Hopper has no settings persistence — frequency lists must be reloaded from SD card after each app launch.