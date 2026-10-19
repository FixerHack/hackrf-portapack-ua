
![SCR_0069](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/7ed6853e-909b-4aff-80a0-c7f7c7dbe106)


# Wav Viewer

The Wav Viewer app can be used to view and play back 8-bit unsigned or 16-bit signed mono WAV files. Sample WAV files may be found in the `WAV/` folder of the SD card, and WAV files captured using the Audio app will be placed in the `AUDIO/` folder.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Creating Compatible WAV Files

Using a PC, WAV files can be converted from existing audio using Audacity or ffmpeg:
```bash
# 8-bit unsigned mono, 48000 Hz
ffmpeg -i lovely_music.mp3 -ar 48000 -ac 1 -acodec pcm_u8 lovely_music.wav

# 16-bit signed mono, 48000 Hz
ffmpeg -i lovely_music.mp3 -ar 48000 -ac 1 -acodec pcm_s16le lovely_music.wav
```

> [!NOTE]
> Only **mono** WAV files with **8-bit unsigned** or **16-bit signed** PCM encoding are supported. Stereo or other formats will show an error on load.

## File Information Displayed

Once a file is opened, the app shows:

| Field | Description |
|-------|-------------|
| **File** | Filename |
| **xx-bit mono** | Bit depth (8 or 16) and channel count |
| **Sample rate** | e.g. `48000Hz` |
| **Title** | Embedded title tag from the WAV file header (if present) |
| **Duration** | Total length in seconds |

## Waveform Display

- The main **waveform** panel shows the audio samples for the current view window.
- Below the waveform, a compressed **amplitude overview** bar shows the overall signal level across the entire file using a color spectrum (darker = quieter, brighter = louder).
- A small **window indicator** shows which portion of the full file is currently visible in the waveform.

## Controls

| Control | Description |
|---------|-------------|
| **Open** | Open a `.WAV` file from the SD card |
| **▶ / ■** | Start or stop audio playback |
| **Vol** | Audio output volume |
| **Position (s / ms)** | Navigate to a specific time position in the file |
| **Sample** | Navigate by sample number |
| **Scale** | Zoom the waveform view (1 = 1 sample per pixel, higher = zoomed out) |
| **Cursor A** | Position of cursor A (cyan) on the waveform (0–239 pixels) |
| **Cursor B** | Position of cursor B (magenta) on the waveform (0–239 pixels) |
| **Delta** | Time difference between Cursor A and Cursor B, shown as duration and equivalent frequency |

## Playback

Pressing ▶ starts audio playback from the current position. A progress bar tracks playback through the file. The position fields update live during playback. Waveform view changes made during playback are applied once playback finishes.