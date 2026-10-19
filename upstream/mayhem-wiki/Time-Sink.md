Time Sink is a time-domain waveform viewer — an oscilloscope for RF. It plots the I (in-phase) component of the received IQ stream as an amplitude-vs-time trace across the screen. Apps like [Looking Glass](Looking-Glass) display the frequency domain (spectrum); Time Sink displays the time domain (signal shape over time).

The equivalent GNU Radio block is the **Time Sink** source block:

<img alt="image" src="https://github.com/user-attachments/assets/7dcbc8dc-39fd-4a1f-a421-769958f51915" />

# Display

The waveform area covers the lower portion of the screen (below the 3-row header). Each horizontal pixel corresponds to one of **240 data points** sampled from the received baseband buffer. The vertical axis represents amplitude, with the centre line at zero. Only the I (real) component is shown.

# Settings

## Row 0 — Frequency and Gain

* **Frequency**: Default 433.920 MHz. Use the encoder knob or tap to open the keypad.
* **Frequency step**: Step size for encoder tuning.
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain.

## Row 1 — Sample Rate and Decimation

* **SR (Sample Rate)**: Baseband sampling rate. Options: **1.0 MHz, 2.0 MHz, 5.0 MHz, 10.0 MHz, 20.0 MHz**. Default: 2.0 MHz. Higher rates capture faster signal edges; lower rates give a slower, more zoomed-in time base.
* **DEC (Decimation)**: Range 0–128. Controls how many baseband buffers are skipped between display updates. Each buffer is ~2048 samples. At DEC=0, the display updates every buffer; at DEC=128, it updates every 129th buffer. Increase DEC to slow down the trace refresh on slow or periodic signals.

## Row 2 — Persistence and Trigger

* **PST (Persistence)**: Number of past waveform frames to keep visible on screen simultaneously. Options: **1, 2, 4, 8, 16**. At PST=1 only the current trace is shown; higher values overlay multiple recent traces, similar to the persistence mode of a digital oscilloscope. Maximum is 16 frames due to memory constraints in the external app format.

* **TRM (Trigger Mode)**: Controls waveform synchronisation.
  + `Off` — free-running, no synchronisation
  + `Rise` — triggers on a rising edge crossing the trigger level
  + `Fall` — triggers on a falling edge crossing the trigger level

  When triggered, the app finds the crossing point in each frame and aligns the display to that position, stabilising the waveform. A ±2 hysteresis band is applied to prevent false triggers. The trigger locks to the nearest crossing to the previous one for frame-to-frame stability.

* **LVL (Trigger Level)**: Range −127 to +127. Sets the amplitude threshold for trigger detection relative to the signal midpoint (0 = centre). Has no effect when TRM is set to Off.

# Settings Persistence

All settings (sampling rate, DEC, persistence, trigger mode, trigger level) are saved to `rx_time_sink.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.