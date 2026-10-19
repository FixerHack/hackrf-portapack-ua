The **HackRF** entry in the main menu switches the device from Mayhem firmware into standard HackRF mode. In this mode the PortaPack operates as a plain HackRF One, fully compatible with GNU Radio, GQRX, SDR#, and any other software that supports the HackRF via USB — without any additional flashing or modification.

## Switching to HackRF mode

Select **HackRF** from the main menu. A confirmation dialog appears:

> *"This mode enables HackRF functionality. To return, press the reset button."*

Select **Yes** to confirm. The Mayhem UI shuts down and the HackRF firmware takes over.

> [!NOTE]
> All PortaPack inputs — the encoder dial, buttons, and touchscreen — are inactive in HackRF mode. The display shows a static block diagram at startup, and adds live values once an SDR application connects via USB.

## Firmware version in HackRF mode

When in HackRF mode, `hackrf_info` still reports the Mayhem firmware version, for example:
```
─$ hackrf_info
hackrf_info version: 2024.02.1
libhackrf version: 2024.02.1 (0.9)
Found HackRF
Index: 0
Serial number: 00000000000000009xxxxxxxxxxxxxx3
Board ID Number: 2 (HackRF One)
Firmware Version: n_250606 (API:1.08)
Part ID Number: 0xa000cb3c 0x0066476c
Hardware Revision: r10
Hardware does not appear to have been manufactured by Great Scott Gadgets.
Hardware supported by installed firmware:
    HackRF One
```

This is expected — the HackRF USB interface is provided by the Mayhem firmware image, so the version string reflects Mayhem, not the original HackRF firmware.

## Driver requirements

**Linux / macOS:** The HackRF is supported natively by the `libhackrf` package. Install it via your package manager (e.g. `sudo apt install hackrf`, `brew install hackrf`) and the device will be recognized automatically.

**Windows:** Windows does not include a HackRF driver by default. You need to install the WinUSB driver using Zadig:

1. Download and run Zadig from https://zadig.akeo.ie
2. Select **Options → List All Devices**.
3. Select **HackRF One** from the dropdown.
4. Select **WinUSB** as the driver and click **Install Driver** or **Replace Driver**.

Once installed, the HackRF will be recognized by GQRX (via GNU Radio), SDR#, and `hackrf_transfer`.

> [!NOTE]
> If you previously used the PortaPack with the [[SD-Over-USB|SD Over USB]] app on Windows, a different driver may already be assigned to the device. Zadig will let you replace it.

## Returning to Mayhem

To return to Mayhem firmware, press the **RESET button** — it is on the top of the PortaPack, the outer (right) one. See [[Hardware-overview]] for its exact location.

> [!NOTE]
> There is no software way to exit HackRF mode. Only the RESET button will return the device to Mayhem.

## Use cases

HackRF mode is useful when you need to use the HackRF with PC-based SDR software directly — for example to use GQRX or SDR# for wideband monitoring, run GNU Radio flowgraphs, or use `hackrf_transfer` for raw capture and replay from the command line.

To leave this mode, press the [reset button](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Hardware-overview). It is on the top of the PortaPack the outer (right) one.


| PortaPack in HackRF Mode | HackRF Mode connected to gqrx |
| --- | --- |
| ![hackrf_mode_1_basic_small](https://github.com/user-attachments/assets/fa02f7db-c505-40ce-8fed-f62cd8b5348d) | ![hackrf_mode_2_gqrx_small](https://github.com/user-attachments/assets/535f4e09-debe-48c2-8571-21e37825b66f) |
