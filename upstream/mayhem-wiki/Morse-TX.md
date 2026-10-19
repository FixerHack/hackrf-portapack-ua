<img width="239" height="323" alt="image" src="https://github.com/user-attachments/assets/4d3b5bee-8c9b-40d4-8d76-f520e07778dd" />

Morse TX encodes a text message into Morse code and transmits it in either CW (carrier on/off keying) or FM (tone-modulated) mode.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

* **Foxhunt** (checkbox): When enabled, disables the custom message field and instead uses one of 11 pre-defined fox hunt identification codes, selected with the adjacent number field (1–11). The codes are standard ARDF (Amateur Radio Direction Finding) sequences:

  | # | Code | Pattern |
  |---|------|---------|
  | 1 | MOE | – – – – – · |
  | 2 | MOI | – – – – – · · |
  | 3 | MOS | – – – – – · · · |
  | 4 | MOH | – – – – – · · · · |
  | 5 | MO5 | – – – – – · · · · · |
  | 6 | MON | – – – – – – · |
  | 7 | MOD | – – – – – – · · |
  | 8 | MOB | – – – – – – · · · |
  | 9 | MO6 | – – – – – – · · · · |
  | 10 | MO | – – – – – |
  | 11 | S | · · · |

* **Speed** (10–45 wpm): Transmission speed in words per minute. The time unit per dot/dash is calculated as `1200 ÷ wpm` ms. Default: 15 wpm.

* **Tone** (100–9999 Hz, step 20): The audio tone frequency used in FM mode. In CW mode the tone determines the sidetone pitch only. Default: 700 Hz.

* **Modulation**: `CW` (carrier keying, default) or `FM` (tone-modulated carrier).

* **Loop**: Automatically retransmits the message after the selected interval:
  `Off`, `5 sec`, `10 sec`, `30 sec`, `1 min`, `3 min`, `5 min`

* **Set message**: Opens the text keyboard to enter a custom message. The message is shown on the line above. Default message: `PORTAPACK`.

* **Frequency / Gain / AMP**: Standard TX controls in the bottom bar. Frequency is stored in persistent memory.

* **TX will last**: Displays the calculated transmission duration in seconds based on the current message, speed, and tone settings, updated live.

* **Progress bar**: Shows transmission progress. When Loop is active, shows the countdown to the next retransmission.

* **Start / Stop**: Starts transmission. Press again to abort.

# Known Issue

Due to a timing issue in the transmitter, the first 1–2 characters of a message may be clipped or not transmitted correctly. As a workaround, prefix the message with two short characters, for example `E ` (letter E followed by a space), before the actual content.

# Settings Persistence

Settings are saved to `tx_morse.ini`, including message text, foxhunt selection, speed, tone, modulation, and loop interval.