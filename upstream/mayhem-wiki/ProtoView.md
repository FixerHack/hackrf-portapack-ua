
![image](https://github.com/user-attachments/assets/35732df7-91ac-4312-9673-cdb02a226870)

ProtoView is a raw signal visualizer that displays received OOK/ASK pulses as a waveform. It does not attempt to decode protocols — it shows the raw on/off timing of any signal, making it useful for inspecting unknown or custom transmissions that other decoders do not recognize.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Settings

* **Frequency**: The frequency to monitor. Adjustable via the encoder knob, on-screen numpad, or a saved freqman entry. Frequency step is 100 Hz.
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **RSSI**: Signal strength indicator in the title bar.
* **Volume**: Audio output volume for monitoring the raw signal.

## Controls

* **Zoom**: Sets the time scale of the waveform display. The value is the number of microseconds (µs) per display pixel. Available steps: 1, 2, 5, 15, 30, 50, 100, 200, 500, 1000. Lower values show finer detail over a shorter time window; higher values compress the signal to show longer bursts.
* **Reset**: Clears the signal buffer and restarts live capture. Also exits pause mode and resets the shift position.
* **Pause / Resume**: Freezes the display to inspect the captured waveform. When paused, the **Shift** field appears (see below). The button label changes to **Resume** while paused.

## Waveform Display

The signal is displayed as four stacked waveform rows, each rendered in yellow. Together they represent up to 600 display columns of pulse data. High signal (above threshold) is shown as a raised level; low signal as a flat baseline.

The display is derived from a buffer of up to 400 pulse-timing entries. Each entry stores the duration in microseconds of one continuous high or low state. The threshold between high and low is determined automatically by the baseband processor and adapts continuously to the received signal level.

Pulses longer than 30,000 µs are treated as gap/idle markers and are not rendered.

## Pause Mode and Shift

When paused, a **Shift** field appears between the Zoom control and the waveform. Turning the encoder knob while the Shift field is focused scrolls the waveform left or right through the captured buffer:

* Positive shift values move the display window to the right (skip earlier samples).
* Negative shift values insert blank padding on the left, moving the signal toward the right of the display.

The shift range is −400 to +400 samples. Use this to align specific pulses or transitions in the center of the screen for easier inspection.

## Signal Processing

The baseband processor samples at 4 MHz and decimates by 8, producing an effective analysis rate of 500 kHz. Signal presence is determined by comparing the instantaneous IQ magnitude against an adaptive threshold, which is recalculated every 90,000 samples and clamped to the range 50–1700. This allows the app to work across a wide range of signal strengths without manual squelch adjustment.

## Settings Persistence

App settings (frequency, gain, zoom) are saved to `rx_protoview.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.