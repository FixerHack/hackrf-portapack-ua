Receives pager messages using the POCSAG protocol.

This protocol operates in the VHF/UHF bands using FSK modulation.

# UI Overview

![POCSAG_UI](https://github.com/portapack-mayhem/mayhem-firmware/assets/3761006/bb4795e7-1b1f-4b31-8663-ddc71d1535d4)

![POCSAG_UI_Detail](https://github.com/portapack-mayhem/mayhem-firmware/assets/3761006/1c0faccf-aec3-4a44-b183-8731d24642f1)

### Settings

* **Frequency**: Sets the frequency to receive pager messages on. Can be adjusted with the encoder knob, on-screen numpad, or loaded from frequencies saved on an SD card. 439.9875 MHz is the most popular worldwide frequency used by amateur radio for POCSAG. Amateur radio POCSAG uses 1200 bps.
* **RF amplifier** (0 or 1): Enables/disables the internal RF amplifier.
* **LNA gain** (0, 8, 16, 24, 32, 40): Sets the LNA gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings) for details.
* **VGA gain** (0 to 62): Sets the VGA gain. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues#gain-settings) for details.
* **RSSI/Audio**: Top bar indicates signal strength. Bottom bar indicates the audio level. The audio bar can be useful for tuning settings without headphones or a speaker.
* **Squelch** (0–99): Sets the minimum signal level required to start decoding. 0 disables squelch (all signals decoded regardless of strength). Higher values require a stronger signal — use this to avoid decoding weak or noisy signals that would produce garbled output.
* **Volume**: Output volume for the received audio.

### Information

* **Decoder Status**: Indicates the status of the decoder state machine. White: Idle, Cyan: Clear, Yellow: Waiting for message start, Green: Waiting for rest of message.
* **Batch Count**: Number of message batches received. A batch has 16 codewords.
* **Bits**: Displays the bits being decoded into codewords.
* **Sync**: Green when the frame decoder has received a sync frame. Messages are not decoded unless a sync frame is found.
* **Codewords**: Shows the number of codewords in the current batch. When the bar fills, the batch is complete and processed.
* **Baud Rate**: The detected rate of the current message. `05`: 512 bps, `12`: 1200 bps, `24`: 2400 bps.

### Buttons

* **Ignore Last**: Sets the filter to drop messages sent to the last received address.
* **Config**: Opens the settings page

## Config

![POCSAG_Config](https://github.com/portapack-mayhem/mayhem-firmware/assets/3761006/96ca160b-5672-4169-b90d-85a433cbb39d)

* **Enable Log**: Logs decoded messages to `LOGS/POCSAG.TXT` on the SD card.
* **Log Raw Data**: Also logs the batch codewords as hexadecimal. Useful for debugging decoder issues.
* **Use Small Font**: Uses a smaller font in the UI to show more messages on screen at once.
* **Hide Bad Data**: Do not show (or log) codewords that fail checksum validation.
* **Hide Addr Only**: Do not show (or log) codewords that contain an address but no message payload.
* **Filter Mode** / **Filter Address**: Controls address filtering. `None` disables filtering. `Drop` hides messages sent to the specified address. `Keep` shows only messages sent to the specified address and hides all others.
* **Beta**: Enables the newer POCSAG baseband processor. The app must be restarted after changing this option.
* **Save**: Saves the current settings changes.

> **Note:** Settings are only saved and restored if **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.

## Message Display

Typical message:

```
12:34 1200 #432123 F2
This is a test message
```

Description (from top-left):

* `12:34` — **Time**: When the message was received (PortaPack clock time).
* `1200` — **Data rate**: The baud rate used to receive the message.
* `#432123` — **Address**: The pager address the message was sent to.
* `F2` — **Function**: A value 0–3 indicating the message type or source category.
* `This is a test message` — **Message**: The decoded message text.

Messages displayed in **magenta** contain a high number of decoding errors and may be unreliable.