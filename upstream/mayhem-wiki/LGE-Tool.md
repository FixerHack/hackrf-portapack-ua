LGE Tool transmits proprietary RF control frames used by certain laser tag systems operating in the 868 MHz ISM band. The system uses RFM69-based FSK packets with a fixed network ID and sync word. The tool was originally written by Furrtek for the portapack-havoc project.

> [!WARNING]
> This tool is intended for research and testing on equipment you own or operate. Transmitting control commands on third-party systems without authorisation may be illegal in your jurisdiction.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Radio Parameters

The system uses three fixed channels in the 868 MHz band. The default frequency is **868.067 MHz**.

| Channel | Frequency |
|---------|-----------|
| 1 | 868.067 MHz |
| 2 | 868.183 MHz |
| 3 | 868.295 MHz |

| Parameter | Value |
|-----------|-------|
| Modulation | FSK |
| Baud rate | 9600 |
| Deviation | 4,000 Hz |
| Bandwidth | 2,500,000 Hz |
| Packet format | RFM69, Network ID 5, Sync `0x2DD4` |

# Controls

* **Frame**: Selects the type of command frame to transmit (see below).
* **All ch.** (checkbox, default: on): When enabled, the frame is transmitted sequentially on all three channels (868.067 → 868.183 → 868.295 MHz). When disabled, only the currently selected frequency is used.
* **Room** (1–2): Room/arena number.
* **Text**: Player or team nickname, up to 15 characters. Opens the alpha keyboard on press.
* **Team** (1–6): Team number.
* **Player** (1–50): Player number.

# Frame Types

| Frame | Description | Fields used |
|-------|-------------|-------------|
| **Key** | Simulates a hit/shot on the target player | Room, Player |
| **Set nickname** | Assigns a nickname to a player | Room, Player, Team, Text |
| **Set team** | Sets the name for a team | Team, Text |
| **Brdcst nick** | Broadcasts a player's nickname to all units | Player, Team, Text |
| **Start** | Sends a game start command | Room |
| **Game over** | Sends a game end command | Room |
| **Set vest** | Configures a vest/sensor unit | See below |

## Set vest (vest configuration)

The **Set vest** frame configures the behaviour of an individual vest unit:

* **ID** (1–2): Vest unit ID.
* **Pow** (1–10): Zap power level (duty cycle).
* **Time** (1–25, × 100 ms): Zap duration. A value of `2` = 200 ms.
* **Heartbeat** (checkbox, default: on): Enables heartbeat signal from vest.
* **RX tick** (checkbox, default: on): Enables RX tick signal from vest.

The console area below the controls shows the raw hex bytes of each generated frame.

# Settings Persistence

Settings are saved to `tx_lge.ini`.