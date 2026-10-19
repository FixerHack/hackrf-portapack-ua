> [!WARNING]
> Using this app to disrupt or crash other people's devices without their consent may be illegal in your jurisdiction. The **iOs crash** mode explicitly crashes nearby unpatched iOS devices. Use responsibly and only on devices you own or have permission to test.

BLESpam continuously transmits spoofed Bluetooth Low Energy advertisement packets to trigger pairing popups, notifications, or instability on nearby devices. The MAC address and BLE channel (37, 38, or 39) are randomised automatically with each new packet. Each packet is transmitted 4 times before the app moves to the next one.

The protocol implementations are ported from the [Flipper Zero Xtreme-Apps](https://github.com/Flipper-XFW/Xtreme-Apps) BLE spam module.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Attack Mode

Select the target platform or behaviour from the dropdown:

* **Android** — Sends Google FastPair advertisement packets. Triggers a pairing popup on nearby Android phones. Android applies a per-device cooldown of approximately 15 minutes before showing the popup again.
* **iOs** — Sends Apple Continuity packets (Proximity Pair or Nearby Action type, chosen randomly). Triggers device suggestion notifications on nearby iOS devices. Effect depends on iOS version.
* **iOs crash** — Sends a specially crafted Apple Continuity packet. Causes unpatched iOS devices to crash after approximately one minute. A power cycle recovers the device.
* **Windows** — Sends Swift Pair packets. Triggers a device popup on nearby Windows machines. Behaviour depends on patch level and supported hardware.
* **Samsung** — Sends Samsung EasySetup packets (Galaxy Buds or Galaxy Watch models, chosen randomly). Triggers a pairing popup on nearby Samsung devices.
* **NameSpam** — Broadcasts one of 9 fixed device names as a generic HID device advertisement: `PortaHack`, `PwnBt`, `iSpam`, `GenericFoodVagon`, `SignalSnoop`, `ByteBandit`, `RadioRogue`, `RadioRebel`, `ByteBlast`. The name is chosen randomly each cycle.
* **NameRandom** — Broadcasts a randomly generated 9-character alphanumeric string as the device name. A new name is generated each cycle.
* **NameCustom** — Broadcasts names read line by line from `/BLESPAM/NAME.txt` on the SD card (one name per line, max 19 characters each). The file is cycled continuously. Falls back to **NameSpam** behaviour if the file is missing or unreadable.
* **All-Safe** — Cycles randomly through all modes except **iOs crash**.
* **All** — Cycles randomly through all modes including **iOs crash**.

# Controls

* **Start / Stop**: Begins or halts transmission.
* **Rnd device** (checkbox, default: on): When enabled, the device model or payload is randomised with each packet change. When disabled, the same payload is retransmitted repeatedly (MAC and channel are still randomised).

# Display

The console area shows the raw advertisement data hex of the current packet, updated approximately every 25 packet changes.

# Settings Persistence

Settings are saved to `tx_blespam.ini`.