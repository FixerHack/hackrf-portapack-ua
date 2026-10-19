# Title Bar


<img width="173" height="22" alt="Unbenannt" src="https://github.com/user-attachments/assets/6e89b8e7-e5bb-40e0-8778-cf5b9da5b5de" />

The title bar appears at the top of every screen and contains navigation controls, quick-action buttons, and status indicators. It is 16 pixels tall and is always visible.

## Navigation

The left side of the title bar contains two fixed elements:

- **Back arrow** — returns to the previous screen or main menu. Also functions as a back button when tapped.
- **App name / title** — displays the current application name. Tapping it has the same effect as the back arrow.

## Status icons

The right side contains a configurable set of icons, added left to right in this order. Most can be individually hidden via **Settings → User Interface**.

| Icon | What it shows | When tapped | Active colour |
|---|---|---|---|
| **Camera** | — | Takes a [[Screenshots\|screenshots]] | — |
| **Sleep** (moon) | — | Activates [[Sleep-mode\|sleep mode]] | — |
| **Stealth** | Stealth mode on/off | Toggles [[Stealth-Mode\|stealth mode]] | Green |
| **Converter** (up/down arrow) | Up- or down-converter selected | Toggles converter on/off | **Red** when active |
| **Bias Tee** | DC power on antenna port on/off | Toggles antenna bias with confirmation | **Yellow** when active |
| **Clock** (int/ext icon) | Current clock reference source (internal or external) | Toggles clock output (CLKOUT) on/off | Green when CLKOUT is enabled |
| **Mute** (speaker/headphone) | Audio mute on/off | Toggles audio mute | Green when muted |
| **Speaker** | Speaker output on/off | Toggles speaker output | Green when enabled |
| **Battery icon** | Battery level and charging status | Opens battery details | — |
| **Battery %** | Numeric battery percentage | Opens battery details | — |
| **SD card** | SD card present/absent | Opens SD card info screen | Green when card is detected |

> [!NOTE]
> The **Speaker** icon only appears on PortaPack models with an AK4951 audio codec where the speaker can be independently controlled. Do not enable it if the speaker already works without it enabled — on some OpenSourceSDRLab H2 models this can cause a conflict.

> [!WARNING]
> The **Bias Tee** supplies DC voltage on the SMA antenna port. Only enable it if your antenna or LNA is designed to accept DC power via the coax. Applying DC to unprepared equipment can cause damage.

## Converter icon detail

The converter icon switches between an up-arrow (`icon_upconvert`) and a down-arrow (`icon_downconvert`) based on the up/down converter setting in **Settings → Converter**. The icon turns **red** when the converter is enabled, regardless of direction.

## Clock icon detail

The clock icon switches between `icon_clk_int` (internal reference) and `icon_clk_ext` (external reference) based on the currently active clock source. The icon turns **green** when the clock output (CLKOUT on the expansion port) is enabled. Tapping it toggles CLKOUT on/off — it does not switch between internal and external clock sources.

## Navigating the title bar with hardware buttons

On H1/H2 models, pressing **Up** while the focus is on the main menu area moves the highlight into the title bar. Icons can then be selected using the directional buttons. On H4M, the touchscreen is the primary method.

## Hiding icons

All status icons can be individually shown or hidden via **Settings → User Interface**. This is useful for decluttering the title bar on small screens or hiding features that are not needed.
