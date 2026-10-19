
![SCR_0070](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/006888cf-8518-4253-b6a2-6a6d562668d0)

Soundboard transmits `.WAV` files from the SD card as FM audio. Select a file from the list and press START, or enable Random mode to play files in random order.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# File List

WAV files are loaded from the `WAV/` directory on the SD card. Up to 50 files are shown per page; use the `<=` and `=>` buttons to navigate between pages. The current page number and total files on that page are shown above the list.

Files must be mono and either 8-bit unsigned PCM or 16-bit signed PCM. The sample rate is read automatically from the WAV header — files sampled between 24,000 and 48,000 Hz work reliably. Stereo files and other bit depths are silently skipped.

# Controls

* **Loop** (checkbox) — Repeats the currently selected file continuously until stopped.
* **Random** (checkbox) — Plays a randomly chosen file from the list each time START is pressed. When the file ends, a new random file is selected and played automatically.
* **Key** — Selects a subaudible tone to encode on the carrier. The full list includes standard CTCSS tones (labeled by EIA code, e.g. "1 XZ" through "50 ZZ") followed by wireless microphone pilot tones: Shure 19 kHz, Axient 28 kHz, Sennheiser 32.000 kHz, Sony 32.382 kHz, and Sennheiser 32.768 kHz. Select **None** (default) to disable.
* **Vol** — Controls the audio output volume to the speaker. Disabled (shown as `--`) when a Key tone is active, since the pilot tone signal would be audible on the speaker.
* **START / STOP** — Starts or stops transmission.
* **Progress bar** — Shows playback position within the current file.

# RF Parameters

| Parameter | Value |
|---|---|
| Modulation | FM |
| Bandwidth | 1.75 MHz (baseband) |
| Sample rate | Read from WAV header |
| TX gain | 0–47 dB (LNA), 0/14 dB (AMP) |

The bandwidth field in the TX bar sets the FM channel bandwidth (deviation), not the WAV sample rate. The sample rate is applied automatically from the file header.

# Preparing WAV Files

Files must be mono, 8-bit unsigned or 16-bit signed PCM, sampled at 24,000–48,000 Hz. The included sample files are 48,000 Hz / 8-bit. A quick conversion with `sox`:

```
for f in ./*.wav; do sox "$f" -r 48000 -c 1 -b 8 --norm "conv/$f"; done
```

In Audacity: mix down to mono via **Tracks → Mix → Mix Stereo Down to Mono**, then export as **Other Uncompressed Files** with Header **WAV (Microsoft)** and Encoding **Unsigned 8-bit PCM**.

# Settings Persistence

Settings are saved to `tx_soundboard.ini`.