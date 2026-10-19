The **Antenna Length** calculator computes the optimal antenna length for any given frequency, displayed in both metric and imperial units. It also shows how many elements to extend for each of your saved telescopic antennas.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

> [!WARNING]
> Selecting the right ("tuned" or "matched") antenna for each frequency is of paramount importance — otherwise RX or TX will be less than optimal. Under some circumstances, such as a grossly mismatched antenna during high power TX, you could end up damaging your equipment. This applies to all radio TX equipment.

## Controls

| Field | Description |
|-------|-------------|
| **Frequency** | Target frequency. Adjust with the encoder; step size is 1 MHz. |
| **Wave** | Antenna type / fraction of a wavelength to calculate. |
| **Metric** | Calculated length in meters and centimeters. |
| **Imperial** | Calculated length in feet and inches. |

## Wave Type Options

| Option | Fraction | Notes |
|--------|----------|-------|
| Full | 1 | Full wavelength |
| Half | 1/2 | Common dipole |
| Quarter | 1/4 | **Default** — common whip/monopole |
| 3/4 | 3/4 | |
| 1/8 | 1/8 | |
| 3/8 | 3/8 | |
| 5/8 | 5/8 | Popular for VHF/UHF gain |
| 7/8 | 7/8 | |

## Telescopic Antenna Guidance

Below the calculated length, the app shows how many **elements** to extend on each of your saved telescopic antennas to reach the target length.

For example: `ANT500: 3 1/4 elements` means extend 3 full sections plus roughly a quarter of the next.

When the target length falls outside an antenna's physical range, the app reports it instead of a section count: **`retracted`** when the required length is shorter than the fully-collapsed antenna (frequency above the antenna's range), and **`fully ext.`** when it is longer than the fully-extended antenna (frequency below the antenna's range).

If no `ANTENNAS.TXT` file is found on the SD card, the app falls back to the built-in **ANT500** antenna only.

## Adding Your Own Antennas

Place a file at `WHIPCALC/ANTENNAS.TXT` on the SD card. Lines starting with `#` are comments.

**Format:** `label,element1_mm,element2_mm,...`

Each element value is the total extended length in millimeters when that section is fully extended.

### Example ANTENNAS.TXT
```
#antenna label,elements length in mm, separated by commas
ANT700,95,134,175,206,230,245
ANT500,185,315,450,586,724,862
TELESCOPIC,118,183,253,326,399,476
Cheap 11cm,118,183,253,326,399,476
Comet W100RX,200,300,400,510,615,800,986
```

The SD card image ships with a ready-made `ANTENNAS.TXT` that includes several presets such as the **Comet W100RX**.

# References
Episode 44: telescopic antenna of the HackRF (The RF Noob)
https://www.youtube.com/watch?v=MzbAEBghcPM