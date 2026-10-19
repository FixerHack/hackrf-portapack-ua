# Looking Glass
<img width="240" height="320" alt="image" src="https://github.com/user-attachments/assets/6e1bdbab-a672-4323-8f43-eccce99cad90" />
<img width="240" height="320" alt="image" src="https://github.com/user-attachments/assets/bcc394a8-2780-4f35-bc74-2573b4332c5a" />
<img width="240" height="320" alt="image" src="https://github.com/user-attachments/assets/d3702a95-89ad-4675-b06e-5cf956c8d1e0" />


# Introduction

Looking Glass provides a wide-band spectrum waterfall view covering a large frequency range in a single scrolling display. The HackRF steps through the configured range in slices, and each completed full sweep updates the waterfall with a new row.

For wide scan ranges the sweep time is long and the display may appear frozen — this is normal. Keep the scan range as small as practical to get fast, responsive updates. Despite the HackRF's modest sensitivity, Looking Glass is a useful tool for spotting local RF activity across a broad span when paired with an appropriate antenna.

Frequency presets are loaded from all `.TXT` files in the `LOOKINGGLASS/` folder on the SD card. Multiple preset files are supported — all valid entries across all files are merged into the preset list. Keep preset ranges small to limit memory usage.

# Controls

* **MIN / MAX:** Place the cursor on the `MIN` or `MAX` field and use the rotary encoder to adjust the lower or upper scan frequency in steps of the selected step size. The `RANGE` label shows the total scan span.

* **Range lock:** Click on the range value label to lock or unlock the range width when adjusting MIN/MAX. When locked, moving MIN also moves MAX so the span stays fixed.

* **PRESET:** Move the cursor to the `PRESET:` field to select one of the pre-set frequency ranges from `LOOKINGGLASS/PRESETS.TXT` on the SD card.

* **LNA / VGA / AMP:** Gain controls. LNA (IF) adjustable 0–40 dB; VGA (baseband) 0–62 dB; AMP 0 = off, 1 = on (+14 dB).

* **FILTER:** Selects a display smoothing filter — `OFF`, `MID`, or `HIGH`. The filter affects the visual contrast of detected signals. Adjust to get the best contrast for the signals you are trying to see; the optimal setting depends on scan speed and gain.

* **F- / S-:** Scan mode — `F-` is fast but less accurate; `S-` is slow but more accurate.

* **SPECTR / LIVE-V / PEAK-V:** Selects the display mode:
  - `SPECTR` — scrolling waterfall (default)
  - `LIVE-V` — live frequency power level bars
  - `PEAK-V` — peak frequency power level bars

* **RES:** Resolution (FFT trigger point), adjustable 2–128. Default is 32. Increase for finer frequency resolution; decrease for faster updates. Adjust together with gain and FILTER for best results.

* **MARKER:** Rotate the encoder while the cursor is on this field to move a red frequency marker arrow across the waterfall display. The marker's frequency and the per-pixel frequency step are shown. Pressing the encoder knob or the button jumps to the Audio app at the marker frequency with 1 MHz steps and a 10 MHz view. Note: returning from the Audio app resets Looking Glass to its default settings.

* **BEEP:** Click to enable or disable the audio squelch beep. When enabled, a beep is emitted whenever signal power at the marker exceeds the configured squelch threshold (adjustable from −100 to +20 dB; default is 20, which disables it).

* **VOL:** Controls the volume of the beep when beep is enabled.

## LIVE-V and PEAK-V additional controls

When LIVE-V or PEAK-V mode is selected, additional UI elements appear:

* **x0 – x9** *(LIVE-V only)*: Integration multiplier. `x0` gives the fastest response with more noise; `x9` gives the slowest, smoothest response with fewer spikes.

* **▶/■ (Play/Pause)** Toggle button. When the sweep is running the button shows a stop icon (■) in green. Pressing it pauses the sweep — the display freezes and the button turns red showing a play icon (▶). Pressing again resumes. Useful for inspecting a snapshot of the spectrum without the display updating.

* **RSSI** Toggle button. When active (shown in green), two horizontal lines are drawn across the display indicating the current min and max RSSI power levels. When inactive (shown in dark), the lines are hidden. Disabled by default.

* **MAX: VALUE** Displays the frequency with the highest reception power.

* **RST** Resets the max-hold value and clears the display.

* **JMP** Jumps to the Audio app at the frequency shown in `MAX`.