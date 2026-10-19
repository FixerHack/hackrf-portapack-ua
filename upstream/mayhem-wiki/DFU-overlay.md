While Mayhem firmware is running, a short press of the DFU button cycles through two diagnostic overlays and then hides them again:

| DFU press | Result |
|-----------|--------|
| 1st | Show **Performance** overlay |
| 2nd | Show **Radio Settings** overlay |
| 3rd | Hide overlay |

The overlay is drawn on top of the current screen without leaving the active app. Values update approximately once per second.

> [!NOTE]
> The fields shown in both overlays are defined directly in the firmware source (`ui_dfu_menu.hpp`) and depend on the shared memory structure between the two processors (`portapack_shared_memory.hpp`). They may change between firmware versions if either file is modified. The table below reflects the current source code.

## Overlay 1 — Performance

Displays CPU and memory diagnostics for both processors.

| Field | Description |
|-------|-------------|
| M0 core | M0 free core memory (bytes) |
| M0 heap | M0 free heap memory (bytes) |
| M0 frags | M0 heap fragment count |
| M0 stack | M0 free stack space (bytes) |
| M0 cpu % | M0 CPU utilisation (%) |
| M4 heap | M4 heap usage (bytes) |
| M4 stack | M4 stack usage (bytes) |
| M4 cpu % | M4 CPU utilisation (%) |
| M4 miss | M4 baseband buffer miss count |
| Uptime | Device uptime (seconds) |

## Overlay 2 — Radio Settings

Displays the current live radio configuration for both receiver and transmitter models.

| Field | Description |
|-------|-------------|
| RX Freq | Receiver target frequency (Hz) |
| RX BW | Receiver baseband bandwidth (Hz) |
| RX SampR | Receiver sampling rate (Hz) |
| RX Satu% | M4 saturation percentage |
| Modulatn | Modulation index |
| AM cfg | AM configuration index |
| NBFM cfg | Narrowband FM configuration index |
| WFM cfg | Wideband FM configuration index |
| TX Freq | Transmitter target frequency (Hz) |
| TX BW | Transmitter baseband bandwidth (Hz) |
| TX SampR | Transmitter sampling rate (Hz) |

## Using the DFU button to flash firmware

The DFU button serves a second, separate purpose: entering DFU (Device Firmware Upgrade) mode for flashing the HackRF base firmware from a PC. This only works **before** the Mayhem firmware has fully loaded — pressing DFU while the firmware is already running will only toggle the overlay described above.

To enter DFU mode for flashing, try one of these methods while the device is not yet booted into Mayhem:

- Hold **DFU**, plug in the USB cable, then release **DFU**.
- Hold **DFU** and **RESET** simultaneously, release **RESET** first, then release **DFU**.
- Hold **DFU**, power on the device (press the knob on H1/H2, or use the power switch on H4M), release **DFU**, then plug in USB.

When in DFU mode, the LEDs will be on and the screen will remain blank.

See [[Full-reset]] and [[Update-firmware-troubleshooting]] for full flashing instructions.