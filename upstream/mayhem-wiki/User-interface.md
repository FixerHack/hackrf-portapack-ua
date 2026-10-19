
# User Interface

<img width="240" height="320" alt="SCR_0002" src="https://github.com/user-attachments/assets/f331e242-0a77-42ba-8eaa-ffa34de3b464" />




The PortaPack display is 240×320 pixels. The screen is divided into three horizontal bands that are always present:
```
┌─────────────────────────────┐  ← 16 px  Title bar
│                             │
│       App content area      │  ← 288 px
│                             │
├─────────────────────────────┤  ← 16 px  Information bar
```

## Title bar

The top 16 pixels form the [[Title-Bar|title bar]]. It contains:
- Navigation controls (back arrow, app name) on the left
- Configurable status icons and quick-action buttons on the right

## App content area

The middle 288 pixels are used by the currently running app. On the [[main-menu|main menu]] this shows the 2-column button grid. Inside apps it shows the app's own controls and display.

## Information bar

The bottom 16 pixels always show:
- **Left:** Firmware version string (e.g. `n_250606`). If a firmware checksum error is detected at boot, this shows `FLASH ERR` in red instead.
- **Right:** Live UTC clock, updated every second. Date display can be enabled via **Settings → User Interface**.

## Splash screen

A splash screen is shown on each boot before the main menu appears. Tap the screen or press any button to skip it immediately.

By default a random image is selected from the `SPLASH/` folder on the SD card. If a file named `splash.bmp` exists in the SD card root, that file is used instead and the random selection is skipped.

Splash display can be enabled or disabled under **Settings → Display**. See [[Create-a-custom-splash-screen]] for image format requirements.

## Sub-pages

- [[Title-Bar]] — all title bar icons, their functions and active colours
- [[Main-Menu]] — main menu layout and available entries
- [[Main-Controls]] — common controls: frequency field, step size, bandwidth, gain
- [[Text-Entry]] — the on-screen keyboard used for text input
- [[Screenshots]] — how to capture and save screenshots
- [[Create-a-custom-splash-screen]] — boot splash screen image and format requirements
- [[Sleep-mode]] — display sleep and backlight auto-timeout
- [[Stealth-Mode]] — automatic backlight-off during transmission
- [[SD-Card-Content]] — SD card folder structure used by the firmware