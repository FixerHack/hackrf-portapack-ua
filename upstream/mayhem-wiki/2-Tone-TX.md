## Introduction

Transmits a Motorola / QCII style two-tone page with configurable Tone A, Tone B, durations, optional gap, and optional CTCSS. It can be used for bench testing, interoperability checks, or generating known paging sequences for decoder testing.

This is an external app. The `.ppma` file must match the currently running firmware version.

## Controls

* CTCSS: Selects the CTCSS tone mixed with the transmitted page. Set it to `None` to send the page tones without CTCSS.
* A: Selects Tone A from the Motorola / QCII frequency table, or `Custom`.
* B: Selects Tone B from the Motorola / QCII frequency table, or `Custom`.
* ADur: Sets Tone A duration in milliseconds.
* BDur: Sets Tone B duration in milliseconds.
* Gap: Sets an optional silent gap between Tone A and Tone B.
* Timing: Selects a timing preset such as `Moto Std`, `Short Alert`, `Fire Std`, `Long Alert`, or `Custom`.
* Slot: Selects one of five preset storage slots.
* Save: Saves the current tone and timing settings into the selected slot.
* Load: Loads the selected preset slot.
* AHz / BHz: Used when Tone A or Tone B is set to `Custom`. This allows direct entry of a custom frequency in whole Hz.

* The TX time line shows the total transmit duration and the selected tone names.
* The status line reports actions such as preset save/load, `Stopped`, or `Done`.
* The progress bar shows the transmission progress while the page is being transmitted.

## Presets

Each preset slot stores:

* CTCSS selection
* Tone A selection
* Tone B selection
* Tone A duration
* Tone B duration
* Gap duration
* Custom A/B frequency values

Preset slots also have a short display name shown on screen.

## Notes

* The app uses the existing Mayhem tone transmit path and does not require a special receive-side detector.
* With CTCSS enabled, the CTCSS tone is mixed simultaneously with the main paging tones.
* When `Moto Std` is selected, the app uses the usual 1000 ms Tone A and 3000 ms Tone B timing.

## Practical Tips

* Use only frequencies and modulation settings that are legal in your region.
* Keep deviation and gain settings conservative when testing with another receiver to avoid distortion or clipped tones.
* If you are testing a decoder, a `0 ms` gap most closely matches standard back-to-back two-tone paging.