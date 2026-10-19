![SCR_0072](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/ae2c1434-93a0-4ddc-b45e-a8803f544601)


IQ Trim allows you to trim "radio silence" from the beginning and end of a C16, C8, or CU8 capture file.

## UI Components

| Field | Description |
|-------|-------------|
| **Capture File** | Tap to open a `.C16`, `.C8`, or `.CU8` file from the `CAPTURES/` folder. |
| **IQ Display** | Shows the signal power across 240 buckets. The green line marks the Start position, the red line marks the End position. |
| **Start** | Starting sample of the trim region. Adjustable manually. Step size scales with file length. |
| **End** | Ending sample of the trim region. Adjustable manually. Step size scales with file length. |
| **Samples** | Total number of samples in the capture file. |
| **Max Pwr** | Power (complex magnitude) of the strongest sample in the capture file, after amplification. Shown in **red** if the amplification setting would cause clipping. |
| **Cutoff** | Signal-to-noise cutoff as a percentage of Max Pwr (1–100%). Default: **7%**. Used to automatically determine the Start/End trim points. |
| **Amplify** | Amplification factor applied to the trimmed file (1–9×). Default: **1×** (no amplification). Useful if the captured signal was weak. |
| **Trim** | Applies the trim (and amplification) to the file. **Overwrites the file in place — no backup is made.** |

## Trimming Capture Files

1. Open a capture file by tapping the file path field. You should see the signal power displayed in the IQ Display.
   - If the display shows no visible block, the captured signal was too weak for the tool to detect automatically.
2. Either adjust **Cutoff %** to automatically set Start/End, or set **Start** and **End** manually.
3. Optionally increase **Amplify** if the signal was weak. Watch the **Max Pwr** field — it turns red if clipping would occur.
4. Press **Trim**. The file will be edited in place.

> [!WARNING]
> Trim overwrites the original file without making a backup. Use the [[File-manager|File Manager]] to make a copy first if you want to preserve the original.

## Splitting Capture Files

Capture files can be split into multiple files by combining File Manager and IQ Trim:

1. Use [[File-manager|File Manager]] to make copies of the original capture file.
2. Open each copy in IQ Trim and trim to the desired Start/End range.
3. The resulting files can be trimmed further if needed.