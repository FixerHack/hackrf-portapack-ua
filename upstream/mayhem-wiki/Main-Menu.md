# Main Menu

The main menu is the first screen shown after boot. It is a 2-column button grid that provides access to all major areas of the firmware.

<img width="240" height="320" alt="SCR_0002" src="https://github.com/user-attachments/assets/eda7026d-a7fb-4276-98b7-4a734434fd80" />

## Menu items

| Entry | Color | Description |
|---|---|---|
| **Receive** | Cyan | Receiver applications — audio, ADS-B, AIS, APRS, BLE, POCSAG, and more |
| **Transmit** | Cyan | Transmitter applications — APRS TX, BLE TX, OOK, RDS, TouchTunes, and more |
| **Transceiver** | Cyan | Bidirectional apps — Microphone TX/RX and KISS TNC |
| **Recon** | Green | Automated frequency scanning and signal reconnaissance |
| **Capture** | Red | Raw IQ capture to SD card |
| **Replay** | Green | Playback of previously captured IQ files |
| **Looking Glass** | Green | Wideband spectrum sweep visualizer |
| **Utilities** | Cyan | Tools — File Manager, Freq. Manager, IQ Trim, Notepad, Flash Utility, Debug, and more |
| **Games** | Cyan | Built-in games |
| **Settings** | Cyan | Device configuration — radio, display, UI, P.Memory, and more |
| **HackRF** | Cyan | Switch to standard HackRF mode (USB SDR) |

> [!NOTE]
> **HackRF** always appears as the last item in the menu. It is not a navigation target but a mode switch — selecting it opens a confirmation dialog. See [[HackRF]] for details.

## External apps in the main menu

External apps (`.ppma` or `.ppmp` files in the `APPS/` folder on the SD card) can be configured to appear directly in the main menu rather than inside a submenu. Apps registered at the `HOME` location are inserted between **Settings** and **HackRF** in the order they appear in the `APPS/` directory.

See [[External-apps-informations]] for how to configure an external app's menu location.

## App Search

Tapping the **info bar** (the status bar at the top of the screen) opens an alphanumeric keyboard. Type part of an app name (up to 20 characters) and confirm to search across all built-in and external apps. A results list is shown with matching entries — select one to launch it directly. If no match is found a modal displays "No matching app found." Pressing back or submitting an empty query cancels the search.

## Navigation

From the main menu, pressing the **back button** (or the left hardware button on H1/H2, or navigating back on H4M) has no effect — the main menu is the root of the navigation stack.

The **title bar** at the top of every screen provides access to quick settings (converter, clock output, speaker, stealth mode) and shows the current UTC time, battery status, and SD card status. See [[Title-Bar]] for details.