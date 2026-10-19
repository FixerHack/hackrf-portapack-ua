# Main Controls

This page describes the common controls that appear across most receiver and transmitter apps.

## Frequency

When the frequency field is selected, the frequency can be changed in three ways:

- **Encoder dial:** Adjusts the frequency by the currently set step size.
- **Short press of Select:** Opens the direct frequency entry screen, where a frequency can be typed in.
- **Long press of Select:** Toggles *digit mode*. In digit mode, the cursor highlights a single digit of the frequency. Left/Right move the cursor between digit positions; Up/Down (or the encoder) adjust the value of the selected digit. Long press again to exit digit mode.

The nine digit positions represent: 1 GHz, 100 MHz, 10 MHz, 1 MHz, **·** (decimal), 100 kHz, 10 kHz, 1 kHz, 100 Hz.

## Step size

The step size used when turning the encoder dial can be changed as a secondary option when the frequency field is focused. The available steps are:

`10Hz` · `50Hz` · `0.1kHz` · `1kHz` · `5kHz (SA AM)` · `6.25kHz (NFM)` · `8.33kHz (AIR)` · `9kHz (EU AM)` · `10kHz (US AM)` · `12.5kHz (NFM)` · `15kHz (HFM)` · `25kHz (N1)` · `30kHz (OIRT)` · `50kHz (FM1)` · `100kHz (FM2)` · `250kHz (N2)` · `500kHz (WFM)` · `1MHz`

## Bandwidth

The IF filter bandwidth selects which FIR filter is applied to the received signal. Available options depend on the modulation mode:

**AM:** `DSB 9k` · `DSB 6k` · `USB+3k` · `LSB-3k` · `CW`

- `DSB 9k` and `DSB 6k` are standard double-sideband AM (9K00A3E and 6K00A3E).
- `USB+3k` and `LSB-3k` are single-sideband (2K80J3E), upper and lower respectively.
- `CW` uses a 200 Hz filter centred at 700 Hz.

**NFM:** `8k5` · `11k` · `12k5` · `16k`

- `16k` (16KF3E) is for 25 kHz channel spacing.
- `12k5` is standard for 12.5 kHz channels; overmodulated systems may benefit from `11k`.
- `8k5` (8K5F3E) is for narrow 12.5 kHz spacing where tighter filtering is needed.

**WFM:** `80k` · `180k` · `200k`

- `200k` covers a full stereo FM broadcast signal.
- `80k` is a narrower option useful for weaker stations or reduced bandwidth.

## Gain controls

The HackRF has three independent RX gain stages and two TX gain stages. The image below shows their position in the Audio receiver app — the layout is the same across all receiver apps.

![Gain controls in the Audio receiver app](https://github.com/portapack-mayhem/mayhem-firmware/assets/13151053/d0eea0c2-097f-4a71-a498-4ceb03bdaa67)

### RX gain

| Label in UI | Stage | Range | Step |
|---|---|---|---|
| **AMP** | RF amplifier (at antenna port) | 0 dB or +14 dB | on/off |
| **LNA** | IF / low-noise amplifier | 0 – 40 dB | 8 dB |
| **VGA** | Baseband variable gain amplifier | 0 – 62 dB | 2 dB |

The RF amp is shown as `0`/`1` in most RX apps. In the Audio app, it appears as `Amp` on the line below LNA/VGA when one of those fields is selected.

A good starting point for most signals is: **AMP off, LNA 16, VGA 16**. Increase LNA and VGA roughly equally until the signal is clear. Enable AMP only for very weak signals — it can degrade SNR if the noise floor is already high, or if a strong signal is present.

> [!NOTE]
> Setting gain too high causes ADC saturation, which appears as broadband noise or spurious signals across the waterfall. The **Satu%** field in the [[DFU-overlay]] shows the current saturation percentage in real time and helps dial in the optimal setting.

### TX gain

| Label in UI | Stage | Range | Step |
|---|---|---|---|
| **AMP** | RF amplifier (at antenna port) | 0 dB or +14 dB | on/off |
| **Gain** | TX VGA | 0 – 47 dB | 1 dB |

The TX amp is shown as `0` or `14` in TX apps.