![image](https://github.com/user-attachments/assets/f221dff8-07cf-41ca-be20-0e25b6a16e0f)

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Introduction

The Radio app is a general-purpose audio receiver with 10 quick-access favourite slots. It supports AM, NFM (Narrow FM), WFM (Wide FM), USB and LSB demodulation modes and is primarily intended for listening to broadcast FM, amateur radio, and other audio transmissions. Switching between presets requires only a single button press or touch, making it convenient for scanning across known frequencies.

# Controls

**Top row (always visible):**

* **Frequency:** The tuned frequency. Use the rotary encoder to step in 25 kHz increments (suitable for FM broadcast), or click to open the numeric keypad. The default frequency is 87.0 MHz.
* **AMP:** RF preamplifier — 0 = off, 1 = on (+14 dB). Avoid enabling AMP on strong local signals as it will cause overload.
* **LNA:** Low Noise Amplifier gain (0–40 dB). Use the rotary encoder to adjust.
* **VGA:** Variable Gain Amplifier / baseband gain (0–62 dB). Use the rotary encoder to adjust.
* **Volume:** Audio output level. Use the rotary encoder to adjust.

**Waveform / Spectrum display:**

Below the top row, an audio spectrum waveform is shown during reception. In WFM mode only, clicking on the waveform toggles between the waveform view and a graphic equalizer (GraphEq) display. Clicking the GraphEq cycles through 20 built-in colour themes.

**Favourite buttons (middle):**

Ten buttons arranged in two columns show the frequency of each saved preset. Clicking a button immediately loads that preset (frequency, modulation, and bandwidth). Buttons show the frequency in MHz format (e.g., `87.0`). Unassigned slots default to 87.0 MHz / WFM.

**Bottom row:**

* **Save:** Activates save mode. The label "Select slot" appears above the favourite buttons. Click any favourite button to save the current frequency, modulation, and bandwidth to that slot. Save mode is cancelled automatically after saving or by pressing Save again.
* **BW (Bandwidth):** Adjusts the demodulation bandwidth. Available options depend on the selected modulation mode (see table below).
* **MODE:** Selects the demodulation mode. Available modes: `AM`, `NFM`, `WFM`, `USB`, `LSB`.

## Modulation modes

| Mode | Description | Audio rate | Default BW |
|------|-------------|------------|------------|
| WFM | Wideband FM — broadcast FM radio (87–108 MHz) | 48 kHz | 200 kHz |
| NFM | Narrowband FM — PMR, amateur VHF/UHF | 24 kHz | 16 kHz |
| AM | Amplitude Modulation — MW, shortwave | 24 kHz | DSB |
| USB | Upper Sideband — HF amateur bands | 24 kHz | (AM baseband) |
| LSB | Lower Sideband — HF amateur bands | 24 kHz | (AM baseband) |

> **Note:** USB and LSB use the AM baseband processor internally with the sideband filter applied. The BW selector changes the AM configuration accordingly.

## Saving a favourite

1. Tune to the desired frequency and select the correct modulation and bandwidth.
2. Press **Save**. The text "Select slot" appears.
3. Press any of the 10 favourite buttons to store the current settings.

The slot is immediately updated and the new frequency label appears on the button. All slots are saved persistently to the SD card.

# Settings persistence

All 10 favourite slots (frequency, modulation, bandwidth) and the current colour theme for the GraphEq are saved automatically and restored on next launch. Settings are stored in `SETTINGS/rx_fmradio.ini` on the SD card.

## What this app does not support

### DAB and DAB+

DAB (Digital Audio Broadcasting) and DAB+ cannot be received or decoded by this app or any other app in Mayhem. DAB/DAB+ is a digital standard that uses OFDM modulation across a 1.536 MHz channel, with audio encoded in MPEG-4 HE-AAC (DAB+) or MPEG-1 Layer II (DAB). Decoding requires significant DSP processing for OFDM demodulation, channel correction, Viterbi decoding, and audio codec processing — well beyond what the HackRF's M4 baseband processor can handle standalone.

DAB/DAB+ is therefore only receivable with a dedicated DAB receiver or a PC-based SDR solution (e.g. Welle.io or a hardware DAB stick). The PortaPack with Mayhem cannot substitute for these.

> [!NOTE]
> **FM broadcast (WFM) worldwide:** The Radio app receives FM broadcast normally wherever it is available:
> - **Europe / most of the world:** 87.5–108 MHz
> - **USA / Canada:** 87.9–107.9 MHz (same band, fully compatible)
> - **Japan:** 76–95 MHz — note the different lower band edge; tune accordingly
> - **Regions with DAB+ rollout (Germany, UK, Norway, Switzerland, Australia etc.):** FM and DAB+ often run in parallel. FM remains receivable with WFM; DAB+ is not.
> - **Regions where FM is still dominant (most of Africa, South/Central America, Southeast Asia):** WFM works as expected with no DAB interference to consider.
>
> **DAB/DAB+ via PC:** When the PortaPack is switched to [[HackRF]] and connected to a PC via USB, DAB/DAB+ reception becomes possible using PC-based SDR software such as **Welle.io** (Windows/Linux/macOS, supports HackRF natively). The HackRF has more than enough bandwidth for a full DAB multiplex (1.536 MHz channel). In this case the PC handles all demodulation and decoding — the PortaPack itself does nothing beyond acting as an RF frontend.

### Other unsupported digital audio standards

Similarly, **HD Radio** (USA), **DRM** (Digital Radio Mondiale, HF), and **ISDB-Tsb** (Japan/Brazil) are not supported for the same reasons — all require complex digital demodulation and audio decoding that exceeds the hardware's processing capacity.