## Introduction

Receives Motorola / QCII style two-tone paging sequences from FM voice channels and logs detected tone pairs on screen. The app can optionally require a matching CTCSS tone before detection starts, which helps reduce false detections on shared or noisy channels.

This is an external app. The `.ppma` file must match the currently running firmware version.

## Controls

* Frequency: Sets the receive frequency. It can be adjusted with the encoder, entered directly, or loaded from saved frequencies in the normal Mayhem way.
* RF amplifier (0 or 1): Enables or disables the internal RF amplifier.
* LNA gain: Sets the LNA gain.
* VGA gain: Sets the VGA gain.
* Volume: Sets the audio output volume.
* CTCSS: Selects a required CTCSS tone. Set it to `None` to detect pages without CTCSS gating.
* Sq: Sets the squelch level used by the app.
* Start / Stop: Starts or stops the receiver and tone detector.
* Clr: Clears the detected tone pair history shown on screen.
* Bias-T: Enables Bias-T power for an external LNA while the app is running, then restores the previous antenna bias state when the app stops.

The status line shows the current detection phase:

* `T1 ...` means the app is currently collecting the first tone.
* `T1:xxxx.xHz xxxxms T2...` means the first tone has been accepted and the app is collecting the second tone.
* `T1:xxxx.xHz xxxxms T2 ?` can briefly appear when the second tone has a weak or noisy dropout window.

The tone log stores completed tone pairs in the order they were received. New entries are added below older ones. If more entries are collected than fit on screen, the list can be scrolled.

Each line shows:

* Tone A frequency and duration
* Tone B frequency and duration

Example:

`584.8Hz 1000ms 810.2Hz 3040ms`

## Notes

* This app is designed for Motorola / QCII style pages, commonly using approximately 1 second for Tone A and 3 seconds for Tone B.
* The app finalizes a page either when the tone detector reports the end of the tone sequence, or when a valid long Tone B transitions directly into dispatch voice audio without the RF carrier dropping.
* For debugging, the app can write detailed trace output to `DEBUG/TWOTONERX.TXT` on the SD card, but the normal UI log only shows completed tone pairs.

## Practical Tips

* Real-world paging channels are often weak or noisy. Best results usually come from using the correct antenna, appropriate gain settings, and any needed external filtering.
* If the monitored system uses CTCSS, selecting the correct tone can reduce false detections significantly.
* External apps in Mayhem are version-sensitive. If the app hard faults or behaves strangely after an update, make sure the firmware and the `2-Tone RX.ppma` were built from the same firmware version.