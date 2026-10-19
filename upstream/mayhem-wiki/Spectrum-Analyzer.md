# Spectrum Analyzer

<img width="320" height="480" alt="image" src="https://github.com/user-attachments/assets/dc92c346-a2d1-4a53-b8ad-f0fce516da9c" />

<img width="320" height="480" alt="image" src="https://github.com/user-attachments/assets/fe75ae10-a1bb-4b81-b830-49ea3faa89a1" />



A swept spectrum analyzer that works like a bench instrument. It runs in landscape and covers anything from a 10 kHz span up to the whole 1 MHz – 6 GHz range. It has three traces, four markers, a waterfall, and controls modelled on the softkey menus of a benchtop analyzer.

**Location:** `Receive` → `Spectrum` (external app, green icon)

> [!NOTE]
> Level readings are **relative, not calibrated**. The app converts dBFS into an input-referred level by subtracting the LNA, VGA and amp gain. To read absolute dBm, measure a known source and set **AMPT → Offst** (reference offset) so the reading matches.

---

## Holding the device

The app turns the screen to **landscape**. By default, hold the PortaPack turned 90° **anticlockwise** from its normal position. The D-pad turns with the screen, so "left" is always left on the screen as you see it.

If you'd rather hold it the other way, use **DISP → Flip** to rotate the picture 180°. The keys and touch input follow.

When you leave the app, the screen goes back to portrait.

---

## Screen layout

```
┌──────────────────────────────────────────────────────────────┐
│ Ref -40.0dB 10dB/ LNA24 VGA20 AMP-               CONT 12.3ms │  status line
│ M1 433.92MHz -52.31dB  D2 +25kHz -18.40dB                    │  marker readout
├──────────────────────────────────────────────────────────────┤
│                                                              │
│                spectrum graticule (10 × 10 div)              │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                         waterfall                            │  (optional)
├──────────────────────────────────────────────────────────────┤
│ CF 433.92MHz  Span 20MHz  RBW 156.2kHz  VBW 156.2kHz   1tune │  annotation
│ Center                                  433.920 000 MHz      │  active function
│ < │FREQ │SPAN │AMPT │ BW  │TRACE│ MKR │DISP │                │  softkeys
└──────────────────────────────────────────────────────────────┘
```

| Area | Contents |
|---|---|
| **Status line** | Reference level, dB/div scale, LNA/VGA gain, amp on/off, reference offset (if not zero). On the right: sweep state (`CONT` continuous, `SGL` single sweep in progress, `HOLD` stopped) and the time one sweep takes. |
| **Marker readout** | The selected marker, plus the next one that is on. Shows `Mn freq level` for a normal marker, or `Dn ±Δf ±ΔdB` for a delta marker. |
| **Graticule** | 10 vertical divisions (dB/div), 10 horizontal divisions (span/10), one display point per pixel column (320 points). |
| **Waterfall** | History of past sweeps, newest at the top. Colours run from black (bottom of screen) through blue, cyan, yellow and red to white (at the reference level). |
| **Annotation** | Center frequency, span, RBW, VBW, and how many tunes one sweep needs. `SETTLE LOW` appears in orange if the settle time is below the safe minimum for your hardware. |
| **Active function** | The parameter the encoder and Up/Down keys change right now: its name on the left, its value on the right. |
| **Softkeys** | `<` (back) followed by the current menu. |

---

## Controls

The app uses the usual analyzer model: you pick a **softkey**, and it becomes the **active function**. You then change its value with the encoder or the arrow keys.

| Input | Action |
|---|---|
| **Left / Right** | Move the softkey cursor (yellow highlight). |
| **Select** | Press the highlighted softkey. |
| **Encoder** | Change the active function in **fine** steps. |
| **Up / Down** | Change the active function in **coarse** steps (usually one division). |
| **Back** | Go back to the top menu; from the top menu, exit the app. |
| `<` softkey | Same as Back. |

### Softkey behaviour

- **Menu keys** (FREQ, SPAN, …) open their submenu.
- **Value keys** (Centr, Span, Ref, RBW, …): the first press makes the key the active function, shown with a blue background. For frequencies, a second press opens the **frequency keypad**. For list settings (dB/div, RBW, Window, …), a second press steps to the next value. That way you can use the app with touch alone.
- **Toggle keys** (Amp, Fill, Wfall, Flip, …) turn on and off right away. A green label means on.
- **Action keys** (Peak, Zoom+, >CF, …) run right away.

### Touch

- **Tap a softkey** to press it.
- **Tap or drag on the graticule** to move the selected marker to that spot. If the marker was off, this turns it on.
- **Tap the active-function line** while Center, Start, Stop or Span is active to open the frequency keypad.

---

## Menus

### FREQ

| Key | Function | Fine (encoder) | Coarse (Up/Down) |
|---|---|---|---|
| **Centr** | Center frequency | ~span/100 (rounded to 1-2-5) | span/10 (one division) |
| **Start** | Start frequency (span changes, stop stays put) | same | same |
| **Stop** | Stop frequency (span changes, start stays put) | same | same |
| **Keys** | Opens the frequency keypad for Start, Stop or Span if one of those is active; otherwise for Center | | |

The tuning range is 0 – 7.25 GHz. How well the hardware performs at the very ends of that range depends on your device.

### SPAN

| Key | Function |
|---|---|
| **Span** | Sets the span in 1-2-5 steps (10 kHz minimum). Press again to type a value on the keypad. |
| **Full** | Sweeps 1 MHz – 6 GHz. |
| **Zoom+** | Halves the span around the center. |
| **Zoom-** | Doubles the span around the center. |
| **Last** | Returns to the previous span. |

### AMPT (amplitude)

| Key | Function | Range / step |
|---|---|---|
| **Ref** | Reference level (top line of the graticule) | −150 … +30 dB; fine 0.1 dB, coarse one division |
| **dB/dv** | Vertical scale | 1, 2, 5, 10, 20 dB/div |
| **LNA** | RF LNA gain | 0 … 40 dB, 8 dB steps |
| **VGA** | Baseband VGA gain | 0 … 62 dB, 2 dB steps |
| **Amp** | RF amp (+14 dB) on/off | toggle |
| **Offst** | Reference offset added to every reading (for calibration or external attenuators and preamps) | ±100 dB; fine 0.1 dB, coarse 10 dB |
| **AutoR** | Sets the reference level so the highest point of trace 1 sits just under the top line (next 5 dB step at least 5 dB above the peak). | action |

Changing a gain clears the traces, because old data would be at the wrong level. The displayed level already takes LNA, VGA and amp gain into account, so changing a gain moves the noise floor, not the signals.

> [!TIP]
> If strong signals show **spurs or a raised noise floor** across the band, the front end is overloaded. Lower the LNA gain or turn the Amp off.

### BW (bandwidth and sweep)

| Key | Function |
|---|---|
| **RBW** | Resolution bandwidth. **Auto** picks the smallest FFT whose bins are no wider than one display point. You can also force an FFT size of N = 256, 512, 1024 or 2048. The readout shows the effective RBW (including the window's noise bandwidth) and N. |
| **VBW** | Video bandwidth: how many FFTs are averaged per tune (1, 2, 4, 8, 16, 32). Higher values give a smoother noise floor but a slower sweep. VBW is shown as RBW ÷ averages. |
| **Windw** | FFT window: **Rectangular**, **Hann**, **Blackman-Harris** (default), or **Flat top**. Use Flat top for accurate amplitude readings and Blackman-Harris for good dynamic range. |
| **Detct** | How several FFT bins are combined into one display point when the span is wide: **Peak** (default, never misses a narrow carrier), **Average**, **Sample**, or **Neg peak**. |
| **Bins** | Which FFT bins each tune uses. See [Bins layout](#bins-layout). |
| **Settl** | Settle time after each retune before samples are used. 0 … 5000 µs; fine 50 µs, coarse 500 µs. Shows `<min` in orange if set below the safe minimum. |

#### Bins layout

- **Upper sideband**: uses only the bins above the LO and keeps away from the anti-alias filter edge. This keeps the DC/LO spike and the image of strong signals off the trace. It is the right choice for a standard zero-IF HackRF One, and the default there.
- **Both sidebands**: uses bins on both sides of the LO. Each tune covers about 2.2× more spectrum, so the sweep is much faster. Use it on hardware that already keeps DC and the image out of band (**PRALINE**, where it is the default). On a HackRF One it shows a spike at every tune's LO and image signals.

#### Settle time

The tuner needs a short time to settle after each retune. If samples are taken too early, a clean carrier shows up smeared across part of the screen.

| Hardware | Default | Safe minimum |
|---|---|---|
| HackRF One | 400 µs | 350 µs |
| PRALINE | 100 µs | 0 µs |

Settle time only matters when one sweep needs more than one tune (see the `tunes` count in the annotation line). Narrow spans that fit in a single tune never retune between sweeps.

### TRACE

There are three independent traces: **Tr 1** yellow, **Tr 2** cyan, **Tr 3** magenta. By default Tr 1 is Clear/Write and Tr 2 and Tr 3 are Blank.

| Key | Function |
|---|---|
| **Tr n** | Selects which trace the other keys act on. |
| *mode* | Trace mode of the selected trace (the label shows the current mode). |
| **AvgN** | Number of sweeps the Average mode averages over: 2 … 128 in powers of two (default 8). |
| **Fill** | Fills the area under trace 1. |
| **Clear** | Clears the selected trace and restarts its hold/average. |

Trace modes:

| Mode | Label | Behaviour |
|---|---|---|
| Clear/Write | `ClrW` | Shows the latest sweep. |
| Max hold | `MaxH` | Keeps the highest level seen at each point. Good for catching bursts and hoppers. |
| Min hold | `MinH` | Keeps the lowest level seen at each point. |
| Average | `Avg` | Exponential average in dB over *AvgN* sweeps. It settles quickly after a clear. |
| View | `View` | Freezes the trace as it is. Handy for comparing against a live trace. |
| Blank | `Blnk` | Hidden and not updated. |

Changing the mode clears the trace. View is the exception: it keeps what is already there.

### MKR (markers)

There are four markers, **M1 … M4**, drawn as small coloured arrows on their trace. When the menu opens, the cursor is on **Peak**.

| Key | Function |
|---|---|
| **Mkr n** | Makes the selected marker the active function, so the encoder moves it one point and Up/Down move it one division. Press again to select the next marker. Selecting a marker that is off runs a peak search to place it. |
| *mode* | Steps through **Off → Norm → Delta**. Delta reads frequency and level **relative to M1**. M1 has no delta mode. A marker sits on the trace that is selected when you turn it on. |
| **Peak** | Moves the selected marker to the highest point of its trace. |
| **NxtPk** | Moves to the next lower peak. A peak only counts if it rises at least 3 dB above the valley between it and the current marker, so noise is skipped. |
| **>CF** | Sets the center frequency to the marker frequency. |
| **>Ref** | Sets the reference level to the marker level. |
| **AllOf** | Turns all markers off. |

### DISP (display and sweep)

| Key | Function |
|---|---|
| **Wfall** | Turns the waterfall under the spectrum on or off. With the waterfall off, the spectrum uses the full height. |
| **DLine** | Display line: a dashed horizontal reference line. Press once to turn it on and make it active, then set its level with the encoder (0.1 dB) or Up/Down (one division). Press again while it is active to turn it off. |
| **Cont / Singl** | Switches between continuous sweeping and single sweep. |
| **Run** | Restarts the sweep. In single mode, it takes one new sweep. |
| **Flip** | Rotates the picture 180° so you can hold the device the other way round. |

The waterfall adds at most about 30 lines per second. When the sweep is faster than that, the sweeps in between are **peak-held** into one line, so short bursts still show up.

---

## Typical workflows

**Find and measure a signal**
1. Go to **SPAN → Full** for an overview, or **FREQ → Centr** and type a frequency.
2. Go to **MKR → Peak** to jump to the strongest signal, then **>CF** to center it.
3. Go to **SPAN → Zoom+** a few times to look closer. RBW gets narrower on its own.
4. Go to **AMPT → AutoR** to bring the peak near the top line.

**Catch intermittent or hopping signals**
1. **TRACE**: set Tr 1 to `MaxH`.
2. Leave it running. Watch the waterfall for when the signal appears.
3. Press **Clear** to start over.

**Compare before and after**
1. **TRACE**: with Tr 1 in `ClrW`, select **Tr 2**, set it to `ClrW`, wait one sweep, then switch it to `View`.
2. Tr 2 now holds a reference copy, and Tr 1 keeps updating live.

**Measure an offset between two signals**
1. **MKR**: put M1 on the first signal (**Peak**).
2. Select **Mkr2**, set its mode to **Delta**, then move it to the second signal with **NxtPk**, the encoder, or a tap.
3. The readout shows `D2 ±Δf ±ΔdB`.

**Calibrate the level readout**
1. Connect a source of known level.
2. Use **MKR → Peak** to read its level.
3. Go to **AMPT → Offst** and adjust until the marker reads the true level. The offset is saved.

---

## Tips

- **Slow sweep?** Wide spans with a narrow RBW need many tunes. To speed up: use **RBW Auto**, lower **VBW** averaging, or switch **Bins** to *Both sidebands* if your hardware supports it. The status line shows the sweep time and the annotation line shows the tune count.
- **Spike at center on HackRF One?** That is LO feedthrough. Keep **Bins** on *Upper sideband* so it stays off the trace.
- **Smeared carriers or "ghost" humps between tunes?** The settle time is too short. Raise **Settl** until they go away.
- **Settings are saved.** Frequency, span, levels, gains, bandwidths, trace modes, markers and display options are kept between sessions (settings file `rx_specan`).
