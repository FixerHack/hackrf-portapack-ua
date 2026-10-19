![image](https://github.com/user-attachments/assets/c7d63705-f6f0-4cda-b63d-e245ebfb164a)

# Introduction

The NRF receiver app decodes packets from [nRF24L01+](https://www.nordicsemi.com/Products/2-4-GHz-proprietary) transceivers made by Nordic Semiconductor. These are low-cost, low-power 2.4 GHz devices widely used in wireless keyboards, mice, game controllers, mini-drone remotes, and general hobbyist projects. They communicate using Nordic's proprietary Enhanced ShockBurst (ESB) protocol.

The app currently supports **250 kbps mode only**. 1 Mbps and 2 Mbps modes are not yet implemented.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Protocol background

The nRF24L01+ operates in the 2.4 GHz ISM band on 128 channels spaced 1 MHz apart (channel 0 = 2400 MHz, channel 127 = 2527 MHz). Each packet consists of a preamble, a 5-byte address, a 9-bit Packet Control Field (PCF, containing payload length and packet ID), the payload (0–32 bytes), and a 2-byte CRC. The decoder verifies the CRC before displaying a packet — only packets with a valid CRC are shown.

# Controls

* **Frequency:** The default is **2480 MHz** (channel 80). Use the rotary encoder to step in 100 Hz increments, or click to open the numeric keypad. To scan a specific device, set the frequency to the channel it is using: `2400 + channel_number` MHz. Many devices hop across multiple channels; scanning manually or sweeping with Looking Glass first can help identify active channels.
* **AMP:** RF preamplifier — 0 = off, 1 = on (+14 dB).
* **LNA:** Low Noise Amplifier gain (0–40 dB).
* **VGA:** Variable Gain Amplifier / baseband gain (0–62 dB).
* **Modem setup:** Opens the modem configuration screen. The app auto-configures the modem on launch; this button is available for manual adjustments.

# Display

Decoded packets are shown in the console area as hex bytes, formatted as:

```
addr: AA BB CC DD EE  data: XX XX XX XX ...
```

Each line represents one received packet that passed the CRC check. The address field is always 5 bytes. The data bytes that follow are the payload content.

# Limitations

* Only **250 kbps** data rate is supported. Devices transmitting at 1 Mbps or 2 Mbps will not be decoded.
* No channel hopping — the receiver listens on a single fixed frequency. Devices that use frequency hopping must be caught on the right channel.
* The HackRF's 2.4 GHz sensitivity is limited. Passive reception is possible but range is short compared to dedicated 2.4 GHz receivers. Placing the antenna close to the transmitter improves results significantly.