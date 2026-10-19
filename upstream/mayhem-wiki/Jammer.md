> [!WARNING]
> Intentional radio jamming is illegal in most countries, including all EU member states and the United States. Use only for authorised testing on equipment you own in a shielded environment. You are solely responsible for compliance with all applicable laws.

Jammer TX transmits interference signals across up to three independently configured frequency ranges simultaneously. Each range is split into 1 MHz segments (hops), and the jammer cycles through them sequentially. All three ranges are active at the same time when enabled.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Range Tabs (Range 1 / Range 2 / Range 3)

Each tab configures one independent frequency range. The three ranges operate together when transmitting.

* **Enable range** (checkbox): Activates this range. At least one range must be enabled to start.
* **Load range**: Opens the Freqman frequency manager to load a saved range from the `FREQMAN/` directory on the SD card.
* **Start / Stop buttons**: Set the lower and upper bound of the range directly. Can also be set by loading a range.
* **Center / Width buttons**: Alternative way to define the range by center frequency and bandwidth.

The combined bandwidth across all enabled ranges must not exceed **80 MHz** in total (80 × 1 MHz segments). Exceeding this limit shows an error and prevents transmission from starting.

The hop counter (e.g. `03/12`) next to the Type field shows which 1 MHz segment is currently being transmitted and the total number of segments across all active ranges.

# Settings

* **Type**: Signal type generated in each hop segment:

  | Option | Description |
  |--------|-------------|
  | `Rand FSK` | Random FSK noise |
  | `FM tone` | FM-modulated tone |
  | `CW sweep` | Continuous wave sweep |
  | `Noise` | Random amplitude noise |
  | `Sine` | Sine wave |
  | `Square` | Square wave |
  | `Sawtooth` | Sawtooth wave |
  | `Triangle` | Triangle wave |
  | `Chirp` | Linear frequency chirp |
  | `Gauss` | Gaussian noise |
  | `Brute` | Broadband noise |

* **Speed**: Modulation rate within each hop segment: `10 Hz`, `100 Hz`, `1 kHz`, `10 kHz`, `100 kHz`

* **Hop**: Dwell time per 1 MHz segment before moving to the next:
  `Off`, `10ms`, `50ms`, `100ms`, `1s`, `2s`, `5s`, `10s`
  — `Off` disables segment hopping; the jammer stays on each segment indefinitely.

* **TX** (1–180 seconds): How long the jammer transmits before entering the sleep pause.

* **Sleep** (0–60 seconds): Pause duration between TX bursts. When **Sleep = 0**, the TX/pause cycle is disabled entirely and the jammer transmits continuously without stopping. When Sleep > 0, the jammer alternates between TX and pause, with the button label changing to `PAUSED` during the sleep period.

* **Jitter** (0–60, unit: /60 seconds): Adds a random LFSR-based offset to the TX and sleep timers to prevent a perfectly periodic duty cycle. `0` = no jitter.

* **Gain** (0–47): TX gain.
* **A** (0/1): RF amplifier on/off.

# Transmission Parameters

| Parameter | Value |
|-----------|-------|
| Baseband bandwidth | 28,000,000 Hz (max TX LPF) |
| Sampling rate | 3,072,000 Hz |

# Example Configuration (2.4 GHz Wi-Fi)

To target Wi-Fi channels 1, 6, and 11 (2.400–2.483 GHz):

* Range 1: Start `2400000000`, Stop `2483000000`
* Type: `Noise`
* Speed: `10 kHz`
* Hop: `10ms`
* TX: 30 Secs, Sleep: 0 (continuous)
* Jitter: 0

Note that the HackRF's low transmit power (~5–10 dBm) limits effective jamming range to a few metres without an external amplifier.

> [!NOTE]
> Jammer TX has no settings persistence — all settings reset when the app is closed.