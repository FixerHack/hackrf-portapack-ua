The **WardriveMap** displays geotagged RF captures and Flipper Zero `.sub` files on a map. If a GPS module is attached, the map follows your position live.

You can also pan manually by changing the Lat / Lon fields — once you do, GPS will no longer auto-move the map.

Each marker on the map shows the filename of the capture above it.

> [!NOTE]
> Maximum 30 captures can be viewed at once. Use the `<-` / `->` buttons to page through all geotagged files, or pan/zoom the map to see captures in a different area.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).


## Requirements

- A world map installed on the SD card (see [[Create-a-Custom-Map-with-Offline-Map-Maker]]).
- Geotagged capture files in the `CAPTURES/` folder, **or** Flipper Zero `.sub` files with GPS coordinates in the `subghz/` folder.

## Supported File Formats

| Format | Folder | Description |
|--------|--------|-------------|
| `.txt` metadata | `CAPTURES/` | Created automatically by the [[Capture]] app when GPS data is present |
| `.sub` Flipper Zero | `subghz/` | Flipper Zero sub-GHz captures with embedded GPS coordinates |

## Controls

| Control | Description |
|---------|-------------|
| **`<-`** | Page to the previous set of markers |
| **`->`** | Page to the next set of markers |
| **Lat / Lon fields** | Manually pan the map to a specific coordinate |

The `<-` and `->` buttons are hidden when there is nothing further to page to.

## Notes

- Only files with valid, non-zero GPS coordinates are shown as markers.
- The map automatically centers on the first geotagged file found when opening the app.
- If a GPS and orientation sensor are connected, your current position and heading are shown on the map.