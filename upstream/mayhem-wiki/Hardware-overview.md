# External

<img src="img/hw_overview_h2_front.png" height="500"> <img src="img/hw_overview_h2_back.png" height="500">

1. [Antenna](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Antennas#types-of-antenna) (the connector is a _female SMA_, so the antenna needs to be _male SMA_, and not _RPSMA_)
2. Encoder thumb wheel (on the H1 has a different layout, but the same functionality). Pushing the wheel down once to turn ON, or twice quickly to turn OFF.
3. Directional pushbuttons and Enter/Select in the center
4. [CLK IN](https://hackrf.readthedocs.io/en/latest/external_clock_interface.html)
5. [CLK OUT](https://hackrf.readthedocs.io/en/latest/external_clock_interface.html)
6. Micro usb port and next to it, charging led indicator (in the H2, this might flicker while charging but will _mostly_ turn off when the battery is full)
7. Headset/Microphone (standard smartphone 4 segment 3.5mm connector)
8. Receive and transmit leds (indicates the current operation, since the HackRF is half-duplex, only one of this will be lit at every moment)
9. Other status leds (1.8V: rail status, RF: internal power supply, USB: connection to host is active)

> **Note:** In normal operation, 3.3V, 1.8V, RF lights will be ON. 

10. DFU mode button (check the [firmware update procedure](Update-firmware) for details)
11. 3.3V rail status led
12. Reset button

Check [care of PortaPack/HackRF](Care) for general guidelines of how to take care of your device.

# PortaPack internals

<img src="img/hw_overview_h2_inside.png" height="500">

1. MicroSD card slot (insert the card with the contacts looking to the same direction as the screen)
2. GPS module option (has not been implemented)
3. Memory backup coin cell (compatible with CR1225 or CR1220 in the H2, and with the CR2032 or CR2025 in the H1)
4. [Speaker connector](Internal-speaker) (yellow and red go to the speaker coil, black is ground and can be left disconnected)
5. Battery connector
6. TCXO clock (it might be populated with SMD components like in the upper image, unpopulated or populated with a shielded module)
7. Headset/Microphone jack (In case of the H2 the internal speaker switches automatically when the headset is plugged)
8. USB charging circuitry (only the units with battery; this is a standard power bank chipset)
9. Audio amp circuitry

> [!TIP]  
>Adding a small bead of hot-glue on the top of the SD card slot, as shown here, will prevent the SD card from falling down inside the case when it's being inserted.
>
> <img src="https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/ef125782-51f7-4451-951a-126208307c69" height="200">
