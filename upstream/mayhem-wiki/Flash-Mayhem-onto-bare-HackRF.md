## Using firmware file from github release page and the classic hackrf_spiflash tool
> [!Note]
> :warning: This guide works for bare HackRF instead of HackRF with a PortaPack.

- Get the latest firmware from the [![GitHub release (latest by date)](https://img.shields.io/github/v/release/portapack-mayhem/mayhem-firmware?label=Releases&style=social)](https://github.com/portapack-mayhem/mayhem-firmware/releases/latest) page 

### Windows
1. Connect the device via USB.
2. Double click `mayhem_flasher.bat` and follow the instructions.
3. Reboot the device.

### Linux
1. Connect the device via USB
2. Upload the firmware with `hackrf_spiflash -w new_firmware_file.bin` (eg. portapack-h1_h2-mayhem.bin for mayhem firmware or hackrf_one_usb.bin for stock HackRF firmware)
3. Reboot the device
> [!NOTE] 
>- To Ubuntu and Mint user: Ubuntu based distro never maintains their repo for HackRF host (cli client) package. You’ll face a lot of weird problems if your HackRF is R9. To resolve these, please compile the HackRF package yourself, or use another distro.

### MacOS
1. If necessary, install the HackRF tools: `brew install hackrf`
2. Connect the device via USB
3. Upload the firmware with `hackrf_spiflash -w new_firmware_file.bin` 
4. Reboot the device