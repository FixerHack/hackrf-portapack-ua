# Receive Quality Issues

## Not receiving anything / Noisy waterfall

### Antenna

Is the correct antenna connected, and plugged in securely? An incorrect or missing antenna is the most common cause of poor reception. See [[Antennas]] for guidance on antenna selection and matching.

### Gain settings

Gain controls appear in the same layout across all receiver apps: **LNA** on the left, **VGA** on the right.

![Receiver gain controls](https://github.com/portapack-mayhem/mayhem-firmware/wiki/img/screenshots/Receive_Audio.png)

**LNA (Low Noise Amplifier):** Adjusts the front-end gain before the signal is mixed down. Valid values are `0, 8, 16, 24, 32, 40` dB (steps of 8). The LNA attempts to improve signal-to-noise ratio; values of 24–32 are a good starting point for most signals.

**VGA (Variable Gain Amplifier):** Adjusts the baseband gain after mixing. Valid values are `0` to `62` dB in **steps of 2** (even values only). It amplifies the entire received signal including noise; values between 8–20 are typical for most use cases.

> [!NOTE]
> Setting gain too high causes the ADC to clip, which introduces noise and distortion across the entire waterfall — the same effect as audio overload. If the waterfall looks uniformly noisy or "washed out", try reducing both LNA and VGA.

### RX amp

The hardware RX pre-amplifier (AMP button) adds approximately 14 dB of additional gain ahead of the LNA. It is useful for very weak signals but is easy to overdrive and can be damaged if a strong signal is present on the antenna while active. Use it with caution.

### Frequency correction

If you can see a signal on the waterfall but it appears offset from where it should be, check **Settings → Radio → Freq. Correct** (correction in PPB). Most clone HackRF/PortaPack units have a small frequency offset. The [[Tuner]] app can help you measure this offset against a known-accurate reference.

### Software filters

Mayhem's receiver apps include selectable IF bandwidth filters (the bandwidth field next to the modulation selector). Choosing a bandwidth that matches your signal reduces adjacent-channel interference and noise. Using too wide a bandwidth lets in more noise than necessary.

External hardware filters placed between the antenna and the SMA port can also help significantly:

- **Band-pass filters** pass only a specific frequency range and reject everything outside it. Useful when you want to isolate a specific band.
- **Low-pass filters** reject high-frequency signals and harmonics above a cutoff frequency.
- **High-pass filters** reject low-frequency signals and DC components below a cutoff.
- **Notch filters** (band-stop) reject a specific narrow frequency — useful for eliminating strong local interference such as an FM broadcast station.

## Noise sources

### Nearby strong transmitters

High-powered transmitters nearby — FM broadcast stations, trunking repeaters, pager networks — can overload the HackRF's RF front end and create broadband noise across the entire waterfall. An FM-band block filter (88–108 MHz) is a common and inexpensive fix if FM overload is suspected.

### Local interference sources

Many common devices generate wideband noise: computer monitors and screens, USB hubs, switching power supplies, poorly shielded cables, and faulty wiring. To isolate the cause, try unplugging devices one at a time, or simply step outside — outdoor reception is often noticeably cleaner.

### Power banks

Many USB power banks generate significant RF noise. If you are using one, try a different power bank or a direct mains adapter.

### H2 internal battery charger

Some H2 model PortaPacks have been reported to generate noise when the USB cable is connected, caused by the internal battery charger circuit. This is a hardware issue specific to certain H2 units. If you suspect this, try operating on battery only (no USB connected) and compare the waterfall.

> [!NOTE]
> This issue applies to the H2 model specifically. It is not known to affect H1, H2+, or H4M models.

### Cables and grounding

Use well-shielded coax cables. Poorly shielded cables can act as antennas for local noise. Ensure the device and any connected equipment share a common ground where appropriate.

## Intermittent signal loss or noise

### Loose connections

Wiggle the antenna and any coax connectors while watching the waterfall. A dramatic change in the noise floor or signal level indicates a loose or failing connection.

### Nearby intermittent transmitters

Pager networks in particular transmit intermittently and at high power, which can cause brief overloads. Nearby trunking repeaters can have the same effect.

### H2 internal battery charger (intermittent)

The same H2 charger noise issue described above can also occur intermittently, appearing only when the charging circuit is active. See the section above for details.

## Broken RF chain

If none of the above steps help and the device receives nothing at all, the RF front end may be damaged — typically the TX amplifier (a component easily damaged by transmitting into an open or mismatched antenna). The best course of action is to open an issue on the [HackRF GitHub](https://github.com/greatscottgadgets/hackrf) with a description of the problem. If you have a genuine Great Scott Gadgets HackRF One, a replacement may be possible.