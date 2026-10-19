The Debug menu provides hardware diagnostics, memory inspection tools, and developer utilities. Some items are built-in; others are external apps (`.ppma`) that load dynamically from the SD card and appear in the Debug menu automatically when the SD card is present.

## Audio Test


> [!NOTE]
> This is an [external app](External-apps-informations). It requires the `audio_test.ppma` file to be present on the SD card.

Generates a sine wave tone of a configurable frequency and duration to test the audio output chain. Duration of 0 plays the tone continuously. The sample rate and frequency step can also be adjusted. A speaker toggle controls whether the built-in speaker (if present) is used.

## Battery

> [!NOTE]
> Only shown when a MAX17055 battery management IC is detected (H4M hardware only).

Displays the raw register contents of the MAX17055 fuel gauge IC, including voltage, current, capacity, state of charge, and other battery parameters. Values are shown in decoded form with units. Use the encoder dial to scroll through pages of registers.

## Buttons Test

Shows real-time input from all hardware controls: directional buttons, encoder dial, and touchscreen. Useful for verifying that buttons register correctly and that the encoder steps cleanly without skipping or double-stepping. The test screen also includes a long-press test for the directional keys and the DFU switch.

![SCR_0013](https://github.com/portapack-mayhem/mayhem-firmware/assets/125336/1415257f-e322-428c-801d-71977603640e)

## Debug Dump

> [!NOTE]
> This is an [external app](External-apps-informations). It requires the `debug_pmem.ppma` file to be present on the SD card.

Writes a file containing debug information (persistent memory contents, firmware version, hardware info) to the `DEBUG/` folder on the SD card. Useful for reporting bugs or diagnosing configuration issues.

## Ext Module

Displays information about a connected PortaPack expansion module (PPMod) communicating over I2C. Shows the module name, firmware version, and a list of apps provided by the module. If no module is connected, the screen shows "No module connected". The display updates once per second.

## ExtSensor

> [!NOTE]
> This is an [external app](External-apps-informations). It requires the `extsensors.ppma` file to be present on the SD card.

Scans for I2C-connected external sensors and displays their readings. Supports environmental sensors that report temperature, humidity, and pressure (e.g. BME280). Found I2C device addresses are listed on startup.

## Font Viewer

> [!NOTE]
> This is an [external app](External-apps-informations). It requires the `font_viewer.ppma` file to be present on the SD card.

Displays the built-in 5×8 and 8×16 font character sets used by the Mayhem UI.

![SCR_0055](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/3772de42-41af-4c5d-815d-390a7a43a4da)

## M0 Stack Dump

Writes a file containing the M0 core stack contents to the `DEBUG/` folder on the SD card. Used for diagnosing crashes or stack overflows in the M0 processor.

## Memory Dump

Allows a region of memory to be saved to a file in the `DEBUG/` folder in hexadecimal ASCII format. Also allows direct read and write access to specific memory addresses for debugging purposes.

> [!WARNING]
> Memory addresses must be multiples of 4 to avoid causing a fault. Writing to some addresses may cause hardware damage. Use with care.

![SCR_0049](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/049f7939-1638-44a3-9991-c7f809812890)

## Peripherals

Displays the raw register contents of the HackRF radio hardware ICs, which vary by hardware revision:

| Hardware | ICs shown |
|---|---|
| R1–R8 (OG) | RFFC5072, MAX2837, Si5351C, audio codec, SGPIO |
| R9 / R10C | RFFC5072, MAX2839, Si5351A, audio codec, SGPIO |
| HackRF Pro | RFFC5072, MAX2831, Si5351A, iCE40 FPGA, audio codec, SGPIO |

If a MAX17055 battery IC is detected (H4M), it also appears here.

Individual registers can be read or written. If more registers exist than fit on the screen, turn the encoder dial when the Update button is highlighted to scroll through them.

> [!WARNING]
> Writing to some registers may cause hardware damage. Use with care.

![DD1FEF74-140D-4B9E-B86C-B658B035919D](https://github.com/portapack-mayhem/mayhem-firmware/assets/86470699/272500d6-413d-4fcb-9bd6-73b44caa7f1d)

![00403D10-E202-4014-A4C5-B36A216AC548](https://github.com/portapack-mayhem/mayhem-firmware/assets/86470699/a3d9529f-d379-46d0-b326-7cbc020a62a4)

Starting with HackRF One r6, hardware revisions are detected by firmware and reported by `hackrf_info`. The R9 board can be identified without disassembly via the Peripherals view:

![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/86470699/7a1c98ce-8f88-4305-bb51-620a2e8add93)

![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/86470699/49b1d3f2-d7c7-4940-8d18-c49293f2b8ab)

![SCR_0050](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/2faa8689-fc5e-46ed-9f30-c53e4fbf9296)
![SCR_0051](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/c608fc98-8183-4f0a-9298-f4f674a62743)

## Persistent Memory

Displays the 256-byte persistent memory (p.mem) area as a hex dump, split across pages. Use the encoder dial to scroll between pages. The current byte offset from the start of p.mem is shown in the left column.

At the bottom, the current size of the `data_t` struct and the stored checksum are displayed. The checksum is calculated from the first 252 bytes and stored in the last 4 bytes. The config version is visible as the first 4 bytes of the dump.

![SCR_0053](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/6bcef480-b536-4971-b89a-acae1a72b93b)

## Pro Debug

> Only shown on HackRF **Pro** hardware (PRALINE build). It does not appear on H1/H2/H4/H4M.

A submenu of low-level diagnostics for the HackRF Pro's radio front-end and clocking. Intended for developers and hardware bring-up, not everyday use.

| Tool | Purpose |
|---|---|
| WFM Audio | WFM audio-path debug view |
| Clocks | Pro clock-domain status |
| MSynth | Si5351 MultiSynth debug |
| Radio Diag | Radio diagnostics overview |
| Radio Debug | Pro radio register/debug |
| Signal Path | RX/TX signal-path status |
| System Diag | System diagnostics |
| PLL A | Si5351 PLL A debug |
| PLL B | Si5351 PLL B debug |
| GPIO | GPIO state debug |
| RFFC Status | RFFC5072 mixer/synth status |
| RFFC Tuning | RFFC5072 tuning debug |
| MAX2831 | MAX2831 transceiver registers |
| Si5351 | Si5351 clock-generator registers |
| SGPIO Clk | SGPIO clock detector |
| Baseband | Baseband status |
| SGPIO Live | Live SGPIO monitor |
| RX Test | Radio RX test |

## Reboot

Immediately reboots the device.

## SD Card

Displays information about the inserted SD card and allows it to be tested for read/write integrity.

![SCR_0085](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/a1276f7b-1e17-4d02-b49d-0ff63b08cf5f)

## Temperature

> [!NOTE]
> This is an [external app](External-apps-informations). It requires the `mcu_temperature.ppma` file to be present on the SD card.

Displays the current temperature as reported by the on-chip digital temperature sensor of the MAX2837 (R1–R8) or MAX2839 (R9/R10C). Accuracy is approximately ±4.33 °C per step.

![SCR_0052](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/1223b68a-b28b-4dd2-983d-cbba82b99ba9)

## Touch Test

Allows drawing on the screen with a stylus to test touchscreen calibration and accuracy.

![SCR_0058](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/db7c3011-aad7-455f-9301-b8d7468948d1)

Controls:
* **Select** — return to the Debug menu
* **Left** — change the pen to a random color (hold to cycle faster)
* **Down** — clear the screen to a random color
* **Encoder dial** — change the pen size

The screenshot icon remains functional but is hidden; press the exact spot on the title bar to activate it. For improving touchscreen calibration, see Settings → Calibration.
