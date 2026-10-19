
At 26 June 2025 Great Scott Gadgets announced the 'HackRF Pro'. A long awaited upgrade of the 2014 HackRF One.  
Product Page: https://greatscottgadgets.com/hackrf/pro/
Although it got plenty of new features, the development take care of backwards compatibility. The main features are:

- 100 kHz to 6 GHz operating frequency
- Tunable from 0 Hz to 7.1 GHz
- Half-duplex transceiver
- Up to 20 million samples per second
- 8-bit quadrature samples (8-bit I and 8-bit Q)
- Compatible with GNU Radio, SDR#, and more
- Software-configurable RX and TX gain and baseband filter
- Software-controlled RF port power (50 mA at 3.3 V)
- SMA RF connector
- SMA clock input and output for synchronization and triggering
- Convenient buttons for programming
- Internal pin headers for expansion
- High-Speed USB 2.0 with Type-C connector
- USB-powered
- Open source hardware

Compared to [HackRF One](https://greatscottgadgets.com/hackrf/one), HackRF Pro introduces a host of new and updated features, including:

- Wider operating frequency range
- Improved RF performance with flatter frequency response
- Modern USB Type-C connector
- Built-in TCXO crystal oscillator for superior timing stability
- Logic upgrade from a CPLD to a power-efficient FPGA
- Elimination of the DC spike
- Extended-precision mode with 16-bit samples for low sample rates (typical ENOB: 9-11)
- Half-precision mode with 4-bit samples at up to 40 Msps
- More RAM and flash memory for custom firmware
- Installed shielding around the radio section
- Trigger input and output accessible through clock connectors
- Cutout in the PCB provides space for future add-ons
- Improved power management
- Enhanced RF port protection
- Facility to hardware-disable transmit mode

(Source: https://greatscottgadgets.com/hackrf/pro/)


### PortaPack with the HackRF One
Although 4 MB flash (upgraded from 1 MB) sounds great, it leads to some side effects.  

```
$ hackrf_spiflash -w git/mayhem-firmware/build/firmware/portapack-mayhem-firmware.bin 
File size 4194304 bytes.
Request exceeds size of flash memory.
[...]
```
This is most likely an indicator for old hackrf-tools, see:  
```
$ hackrf_info 
hackrf_info version: 2024.02.1+
libhackrf version: 2024.02.1+ (0.9.1)
No HackRF boards found.
```
it should show something like
```
hackrf_info version: git-afb42968
libhackrf version: git-afb42968 (0.9.2)
```

## Build the firmware
The development is still in progress, so no all features of the Mayhem Firmware are working at the moment.  
If you want to try it yourself, the process is pretty much the same, except you are telling the compiler to use the new board
```
$ git clone https://github.com/portapack-mayhem/mayhem-firmware/ --recursive
$ cd mayhem-firmware/
$ cmake .. -DBOARD="PRALINE"
```


## Upgrade the hackrf-tools
The newest HackRF Tools are supporting the HackRF Pro

### Linux

Get the latest hackrf-tools
```
$ git clone https://github.com/greatscottgadgets/hackrf
```
change in the working directory, and compile the binaries
```
mkdir hackrf/host/build; cd /hackrf/host/build
cmake ..
make
## install on the system
sudo make install
sudo ldconfig
```

### Windows
https://github.com/greatscottgadgets/hackrf/blob/main/host/README.md#how-to-build-host-software-on-windows

### MacOS
https://github.com/greatscottgadgets/hackrf/blob/main/host/README.md#how-to-build-the-host-software-on-macos


## DFU Mode (rescue)
THE GSG website says, you need to plug the USB out (unpower the HackRF), press DFU and hold it. Plug Power in. Hold the DFU button until the 3.3V LED lights up.  
The Process is the same for the OpenSourceSDRLabs version, however, the 3.3V LED won't lit. But you will see the device on the computer:
```
$ lsusb
[...]
Bus 001 Device 005: ID 1fc9:000c NXP Semiconductors LPC4330FET180 [ARM Cortex M4 + M0] (device firmware upgrade mode)
[...]
```

... from here you can flash the basic firmware to the RAM:
```
$ dfu-util --device 1fc9:000c --alt 0 --download FIRMWARE_hpro_mayhem_nightly_n_260219/utils/hackrf_one_usb.dfu
```
... and the regular Mayhem firmware over it:
```
$ hackrf_spiflash -w ~/git/sdr/mayhem-firmware/build/firmware/firmware_tar/FIRMWARE/portapack-mayhem_dev.bin   
```

## lsusb outputs
Mayhem Firmware loaded  
`Bus 001 Device 008: ID 1d50:6018 OpenMoko, Inc. Black Magic Debug Probe (Application)`  
Mayhem in HackRF Mode  
`Bus 001 Device 007: ID 1d50:6089 OpenMoko, Inc. Great Scott Gadgets HackRF One SDR`  
DFU Mode  
`Bus 001 Device 005: ID 1fc9:000c NXP Semiconductors LPC4330FET180 [ARM Cortex M4 + M0] (device firmware upgrade mode)`

