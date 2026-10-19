Since HackRF Version 2021.03.1, the CPLD will be upgraded within the SPI and DFU firmware upgrade process. For older versions you have to, and now you can, update the CPLD manually:

- Clone the original HackRF project to your computer:
  - `git clone https://github.com/greatscottgadgets/hackrf`
- If not present, install the HackRF tools.
  - See [here](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Update-firmware#using-firmware-file-from-github-release-page-and-the-classic-hackrf_spiflash-tool) how, at the example `hackrf_spiflash`. The Process installs all necessary tools.
- Connect your PortaPack into your Computer, put it into [HackRF](https://github.com/portapack-mayhem/mayhem-firmware/wiki/HackRF) mode and use the following command to update the CPLD:
  - `hackrf_cpldjtag -x hackrf/firmware/cpld/sgpio_if/default.xsvf`

**LED1/2/3 blinking means CPLD program success.**
LED3/RED steady means error.
Wait for the message 'Write finished' and power OFF / Disconnect your PortaPack from your machine.
