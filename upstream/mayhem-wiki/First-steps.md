# Identify your device

There are many different versions of the PortaPack. It is important that you identify the correct version as this can affect how you install the firmware and device initial start-up. It is recommended you read the description of versions [here](PortaPack-Versions). The H2 and H2+ versions are a slightly improved version, but the people making these copies never published the circuit diagrams or Code, hence breaking the license terms. 

The main difference are the controls and the screen size, along with the codec and processor chip. The H2 / H2+ has extra circuitry to manage the battery charging and powering on/off. In this document, there is a brief description about the details. Check a more technical comparison [here](Differences-Between-H1-and-H2-models).

# Up to date information
There is a Discord server ["HackRF PortaPack Mayhem"](https://discord.gg/tuwVMv3). This has all the current talk and information.

# Power on/off
The original H1 powers instantly when you plug a power supply into the USB port. To turn it off, just unplug it. Similar to the issues with some USB cables while [upgrading the firmware](Update-firmware), the quality of your cable might affect the performance. 

To power on/off the H2, you need to hold the middle button (knob or pushbutton) for few seconds. See more details [here](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Powering-the-PortaPack).

For most H2+ models, click the knob to power on, double-click the knob to power off. 

# Extra functionality (H2 and H2+)
## Charging
This version can charge the internal lipo battery via the USB. There is a led indicator that turns off when the charging is done, but it might flicker. On some models (H2+) there are 4 leds below the knob that represent the state of the battery charge: 25%, 50%, 75%, 100%. When charging, one will flash dependent on the current charge state of the battery. See more details [here](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Powering-the-PortaPack). 

## Charging indications on screen (H4M)
This version can charge the internal lipo battery via the USB. There is an on screen indicator of the level of charge. The icons can be a level on a battery, or a percentage.

## Battery life
An internal battery between 1000 and 2500 mAh should last for several hours of use, depending on use of apps. The standby consumption is [very low](https://github.com/eried/Research/blob/master/HackRF/PortaPack/h2_standby_consumption.jpg), around 52 µA, so you do not need to worry about having to remove/disconnect the battery in normal circumstances.