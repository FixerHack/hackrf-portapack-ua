<img width="239" height="320" alt="image" src="https://github.com/user-attachments/assets/719dc1d4-9eda-44f7-94d1-02b7daf1bb8d" />

Receives and decodes Radio Teletype (RTTY) transmissions using Baudot/ITA2 5-bit encoding over FSK (frequency-shift keying). The decoder produces live text output and supports automatic baud rate detection.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Settings

* **Frequency**: The center frequency to receive on. Frequency step is 100 Hz. Adjustable via the encoder knob or on-screen numpad.
* **RF Amp** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0–40): Low-noise amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **VGA gain** (0–62): Variable-gain amplifier gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings).
* **RSSI**: Signal strength indicator.
* **Volume**: Audio output volume. The received audio (mark/space tones) is passed to the speaker or headphone output.
* **Baud**: Sets the expected symbol rate. Options: `Auto`, `45`, `45.45`, `50`, `75`, `100`, `110`, `150`, `200` bps. See [Auto-Baud](#auto-baud) below.

## Decoded Text Area

The main body of the screen is a scrolling text console that displays decoded Baudot/ITA2 characters in real time. Both letter and figure shift states are handled automatically. The console does not auto-scroll — new text appends at the current position.

## Shift

The frequency shift between mark and space is fixed at **170 Hz**. This is the standard narrow shift used by most amateur radio RTTY and many commercial RTTY stations. The shift is not user-configurable in this app.

## Auto-Baud

When **Baud** is set to `Auto`, the decoder measures incoming pulse widths and continuously refines its estimate of the symbol rate. It starts with a default of approximately **45.45 baud** (the most common RTTY rate) and updates as more signal is received.

The auto-baud algorithm uses a fast-lock approach: a new baud estimate is accepted after 3 consecutive pulses agree with a candidate width. If no signal is detected for approximately 0.5 seconds (12,000 samples at 24 kHz), the baud estimate resets to the 45.45 baud default.

When a specific baud rate is selected, baud detection is bypassed and the decoder locks immediately to the configured rate. This results in faster and more reliable locking when the transmission rate is known in advance.

## Squelch and Polarity

Squelch is automatic and based on the measured spread between the mark and space signal levels. It opens when spread exceeds a threshold and closes when the signal fades — there is no manual squelch control.

Polarity (which tone is mark and which is space) is also detected and corrected automatically. If only one tone is received continuously for more than ~0.3 seconds, the decoder flips polarity and resets the UART state machine.

## Signal Processing

The baseband runs at 3.072 MHz and passes through three decimation stages to reach a final demodulation rate of 24 kHz (3.072 MHz → 384 kHz → 48 kHz → 24 kHz). FM demodulation is used to discriminate between the mark and space frequencies, followed by envelope tracking, a Schmitt trigger slicer, and a 5-bit asynchronous UART state machine to extract Baudot characters.

## Settings Persistence

The selected baud rate is saved to `rx_rtty.ini` on the SD card when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.