The **KISS TNC** app turns the PortaPack into a bidirectional **KISS TNC** (Terminal Node Controller) over the USB serial port. It receives APRS/AX.25 packets from radio and forwards them to a connected PC as KISS frames, and transmits KISS frames received from the PC over radio as AFSK 1200 baud AX.25.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).


## What is KISS TNC?

KISS (Keep It Simple, Stupid) is a protocol that allows a PC application to send and receive AX.25 packet radio frames through a TNC over a serial connection. With this app, the PortaPack acts as the TNC, and the USB serial port is the link to the host PC. Any APRS or packet radio software that supports a serial KISS TNC can be used — for example Direwolf (as a client), APRSISCE/32, APRSdroid, or custom scripts.

## Controls

| Field | Description |
|-------|-------------|
| **Frequency** | RX/TX frequency. Default: 144.390 MHz (APRS standard) |
| **RF Amp** | RF amplifier on/off |
| **LNA** | LNA gain |
| **VGA** | VGA gain |
| **RSSI** | Signal strength indicator |
| **USB** | Shows `Connected` or `Disconnected` — whether the PC has opened the USB serial port |
| **RX** | Count of AX.25 packets received from radio and forwarded to the PC |
| **TX** | Count of frames received from the PC and transmitted over radio |
| **Console** | Live log of received packets, shown as `SOURCE>DESTINATION` |

The status line at the top toggles between **Listening** (RX active) and **Transmitting** (TX in progress).

## Connecting a PC

Connect the PortaPack to the PC via USB. The USB serial port appears as a standard CDC serial device. Open it in your packet radio software and configure it as a KISS TNC at any baud rate (the USB CDC connection is not baud-rate limited).

> [!NOTE]
> On Linux the device typically appears as `/dev/ttyACM0`. On Windows it appears as a COM port. No driver installation is needed on Linux or macOS; Windows may require the standard CDC driver.

## Operation

- **RX**: The app continuously listens on the configured frequency. When a valid AX.25 packet is decoded, it is wrapped in a KISS frame and sent to the PC over USB serial. The RX counter increments and the packet's source and destination callsigns appear in the console.
- **TX**: When the PC sends a KISS data frame (command byte `0x00`) over USB serial, the app switches to transmit mode, sends the AX.25 frame as AFSK 1200 baud Bell 202, then automatically returns to RX mode. The TX counter increments for each transmitted frame.

> [!WARNING]
> The maximum transmittable frame payload is **200 bytes**. Frames larger than this are silently discarded.

## Technical details

| Parameter | Value |
|-----------|-------|
| Modulation | AFSK Bell 202 |
| Baud rate | 1200 baud |
| Mark / Space | 1200 Hz / 2200 Hz |
| Default frequency | 144.390 MHz |
| Max TX frame size | 200 bytes |
| KISS framing | Standard KISS (`0xC0` FEND, `0xDB` FESC escaping) |