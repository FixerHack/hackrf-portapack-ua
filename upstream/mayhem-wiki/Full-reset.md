A full reset reflashes both the HackRF firmware and the Mayhem firmware from scratch, and reinstalls all SD card contents. Use this as a last resort when other troubleshooting steps have failed.

> [!WARNING]
> This process erases all settings and SD card contents. Back up any important files first.

## Steps

1. Back up any important files from your SD card to a computer.

2. Download the latest release from the [Releases page](https://github.com/portapack-mayhem/mayhem-firmware/releases). The `mayhem_vX.X.X.ppfw.tar` file contains both the firmware and all SD card contents in a single archive.

3. Remove the SD card and the coin cell battery from the PortaPack. Keep them somewhere safe and ensure they do not touch each other.

4. Enter DFU mode on the HackRF. Try each method in order until one works — the LEDs should light up and the screen will remain blank:
   - Hold RESET and DFU simultaneously, release RESET first, then release DFU.
   - Hold DFU, plug in the USB cable, then release DFU.
   - Hold DFU, power on the device (press the knob on H1/H2, or use the power switch on H4M), release DFU, then plug in USB.
   - Plug in USB, hold DFU and unplug USB, release DFU, plug USB back in.

5. Flash the HackRF base firmware using DFU:
   - **Windows:** Double-click `mayhem_flasher.bat` from the release package and follow the prompts. Do not disconnect or reset the device afterwards.
   - **Linux / macOS:**
     1. Install `dfu-util` via your package manager (e.g. `sudo apt install dfu-util`, `brew install dfu-util`, or `pacman -Sy dfu-util`).
     2. Extract the release package, open a terminal in that directory, and run:
```
        dfu-util --device 1fc9:000c --download hackrf_one_usb.dfu
```
     3. Do not disconnect or reset the device afterwards.

6. Flash the Mayhem firmware — **without disconnecting the device from step 5**:
   - **Windows:** Run `mayhem_flasher.bat` again and follow the prompts.
   - **Linux / macOS:**
     1. Install the `hackrf` host tools (e.g. `sudo apt install hackrf`, `brew install hackrf`, or `pacman -Sy hackrf`).

        > [!NOTE]
        > Ubuntu's stable repository may ship an outdated `hackrf` package. If you encounter errors, consider compiling the hackrf host tools from source or using a rolling-release distribution.

     2. Extract the firmware package and run (adjust the filename to match the version you downloaded):
```
        hackrf_spiflash -w portapack-h1_h2-mayhem.bin
```

7. Prepare the SD card:
   1. Format the SD card as FAT32 on your computer. See [[How-to-Format-SDCard]] for instructions.
   2. If you downloaded the `ppfw.tar` file, extract it and copy all contents onto the SD card. If you downloaded the separate `COPY_TO_SDCARD.zip`, extract and copy that instead.
   3. Do not insert the SD card yet.

8. If the device still fails to boot at this point, follow the [[Won't-boot]] steps.

9. Power off the device, wait at least 1 minute, then insert the SD card and reinstall the coin cell battery.

10. Power on the device, go to **Settings → P.Memory Mgmt → Reset P.Mem to defaults → YES**, then power off and wait at least 1 minute.

11. If the device still does not boot correctly, repeat the [[Won't-boot]] steps (the boot configuration requires both the SD card and coin cell battery to be present to save correctly).

12. Power on — the full reset is complete.

## Troubleshooting notes

- If the device is not recognized by your computer no matter what you try, try a different computer running Linux, and try at least 5 different USB cables.
- If DFU flashing fails on Linux, check that `dfu-util` is up to date.
- As an optional additional step, you can update the Xilinx CPLD on the HackRF board: [[Updating-the-Xilinx-CPLD-on-hackrf-board]].
- If the problem you were trying to resolve persists after a full reset, open a GitHub issue.