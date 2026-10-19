# Sleep Mode

Sleep mode turns off the screen backlight and puts the LCD controller into a low-power state. The device continues operating normally — all signal processing, audio output, and receiving continue without interruption. Only the display is affected.

## Activating sleep mode

**Manually:** Tap the sleep icon (moon) in the [[Title-Bar|title bar]]. The backlight turns off immediately.

**Automatically:** A backlight auto-timeout can be configured under **Settings → Display**. When enabled, the backlight turns off after a period of inactivity. Available timeout values are: 5 s, 15 s, 30 s, 1 min, 3 min, 5 min, 10 min, 1 h. The timeout is disabled by default.

The sleep icon can be hidden from the title bar via **Settings → User Interface**.

## Waking the display

Press any hardware button or turn the encoder dial. The first input wakes the display — it does not trigger any other action. Touching the touchscreen does not wake the display.

## What sleep mode does and does not do

| | Status during sleep |
|---|---|
| Backlight | **Off** |
| LCD controller | **Suspended** |
| Baseband (M4 core) | **Running** — signal processing continues |
| Audio output | **Active** — audio continues playing |
| Receiving / transmitting | **Active** — unaffected |

> [!NOTE]
> Sleep mode is purely a display power-saving feature. It is not a standby or low-power mode for the radio hardware. If you need to stop radio activity, exit the current app or power off the device.