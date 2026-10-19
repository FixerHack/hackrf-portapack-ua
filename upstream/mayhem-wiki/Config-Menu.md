The Config Menu is a minimal pre-boot configuration interface that runs before the main firmware loads. It uses only the hardware buttons and LEDs — **the LCD screen is not used**.

## Entering the Config Menu

The Config Menu activates automatically after **3 consecutive failed boot attempts** (crashes or resets before the firmware fully loads). To enter it intentionally, press the RESET button 3 times in quick succession — each time before the firmware finishes loading.

> [!NOTE]
> Some PortaPack models do not have a working RESET button. On those, unplugging and replugging the USB cable counts as a reset, and doing so 3 times quickly enough will trigger the Config Menu.

> [!NOTE]
> The Config Menu can be disabled entirely via **Settings → Config Mode**. If disabled, it will never activate automatically or manually.

When entered successfully, all three LEDs (TX, RX, USB) will blink rapidly (~8 times per second). At this point, press the DFU button once to display the currently active settings.

## Available settings

Settings are displayed via the TX and RX LEDs. The USB LED is only used during the initial waiting phase and goes dark once the DFU button is pressed.

### LCD driver (TX LED)

| TX LED | Setting |
|--------|---------|
| Off | Option 1: Automatic detection (default) |
| On | Option 2: LCD driver 1 |
| Blinking fast | Option 3: LCD driver 2 |
| Blinking slow | Option 4: LCD driver 2 QFP100 chip |
| Inverse blink slow | Option 5: LCD driver 1 QFP100 chip |

> [!NOTE]
> The LCD driver can also be set at power-on using the directional buttons. See [[Won't-boot]] for details.

### Disable external TCXO (RX LED)

| RX LED | Setting |
|--------|---------|
| Off | External TCXO enabled / autodetect (default) |
| On | External TCXO disabled |

> [!NOTE]
> This setting can also be changed via **Settings → Radio**.

> [!NOTE]
> On HackRF R9 hardware, if the Config Menu is entered automatically due to boot failures, the external TCXO is temporarily disabled for the duration of the Config Menu session. This is because the TCXO is the most likely cause of the crash. The original setting is restored when you exit.

## Switching between settings

Each press of the DFU button advances to the next combination of settings. Both the LCD driver and TCXO settings are cycled together — after **10 presses** you return to the original active combination.

> [!WARNING]
> Do not press the DFU button too quickly. Hold it down for at least **200ms** or the press may be ignored.

Each new selection is saved immediately to persistent memory. The device can be restarted at any time and the selected settings will be active.

## Unwanted Config Menu activation

In some cases a PortaPack may enter Config Menu mode unexpectedly — for example when the power button is pressed rapidly multiple times, or if electrical noise occurs when a USB cable is attached (causing false resets). If this happens frequently (dark screen with blinking LEDs), the Config Menu can be permanently disabled via **Settings → Config Mode**, which sets a flag in persistent memory to skip the Config Menu entirely on all future boots.