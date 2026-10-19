
If you bought a standalone HackRF, it probably came with the GSG firmware flashed onto it. This enables usage over USB from a computer.

When buying pre-assembled HackRF + PortaPack bundles, they typically come with some version of the Mayhem firmware. One important thing to understand is that the firmware is always flashed onto the HackRF board; the PortaPack has no flash nor CPU. It is basically an interface module that enables standalone usage without a computer. It provides an LCD screen, buttons, an audio codec IC, an SD card slot, a coin cell battery to preserve settings and time between uses, and in some versions, a high-precision clock signal and a battery.

Although the Mayhem firmware allows you to directly use many functions in the field, standalone without a computer, it also provides a “HackRF mode,” which enables the user to start a version of the original GSG firmware and use your HackRF via USB, controlled by a computer. However, if you separate the two boards, you won’t be able to use the menu GUI and enable “HackRF mode.” So, if you want to use your HackRF board alone (detached), you’ll need to flash it with the GSG firmware.

In case you bought a PortaPack separately or want to upgrade your firmware, check out our Update Firmware page! [Update firmware](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Update-firmware)