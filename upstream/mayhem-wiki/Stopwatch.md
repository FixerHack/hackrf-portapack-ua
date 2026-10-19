The **Stopwatch** is a utility app for measuring elapsed time with lap support and configurable millisecond precision display.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Display

The stopwatch shows two rows in large digits:

| Row | Label | Color |
|-----|-------|-------|
| **TOTAL** | Total elapsed time since last reset | Minutes: 🔴 red, Seconds: 🟢 green, Milliseconds: 🟡 yellow |
| **LAP** | Time of the last lap mark | White |

Time is displayed in the format: `MM:SS.mmm`

## Buttons

| Button | While stopped | While running |
|--------|--------------|---------------|
| **START / STOP** | Starts the timer | Stops (pauses) the timer |
| **RESET / LAP** | Resets the timer to zero | Records a lap time |
| **EXIT** | Exits the app | Exits the app |

## Milliseconds Display Level

When the timer is stopped, an option field in the top right controls how many millisecond digits are shown:

| Setting | Digits shown |
|---------|-------------|
| `& - -` | 1 digit (hundreds) |
| `& & -` | 2 digits (hundreds + tens) |
| `& & &` | 3 digits (full milliseconds) |

This option is hidden while the timer is running to prevent accidental changes.

## Notes

- The timer continues accumulating time correctly after a pause — resuming does not reset the elapsed time.
- Lap time is fixed at the moment the **LAP** button is pressed; the TOTAL counter keeps running.
- Only one lap time is displayed at a time; pressing **LAP** again overwrites the previous lap.