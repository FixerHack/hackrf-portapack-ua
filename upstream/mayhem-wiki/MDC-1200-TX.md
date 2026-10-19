MDC-1200 TX transmits MDC-1200 signaling packets, used in some two-way radio systems for unit identification, emergency signaling, selective calling, and remote control operations. The protocol is AFSK at 1200 baud transmitted as FM subaudible data.

> [!WARNING]
> Transmitting MDC-1200 commands on operational radio systems without authorisation is illegal and may interfere with radio communications. Use only on equipment you own or have explicit permission to test.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Transmission Parameters

| Parameter | Value |
|-----------|-------|
| Default frequency | 462.562500 MHz |
| AFSK Mark | 1800 Hz |
| AFSK Space | 1200 Hz |
| Baud rate | 1200 |
| FM deviation | 2500 Hz |
| Bandwidth | 1,750,000 Hz |
| Default TX gain | 30 |
| Encoding | NRZI + convolutional + bit interleaving |
| CRC | CRC-16 with bit reversal, XOR 0xFFFF |

# Controls

* **Op**: Operation type to transmit. Selecting an operation automatically sets the default **Arg** value where applicable (see table below).

* **ID** (two fields, 0–255 each): The 16-bit target unit ID, entered as two separate decimal bytes (high byte and low byte). For example, ID 256 is entered as `001` `000`.

* **Arg** (0–255): The argument byte for the operation. Automatically set when the Op is changed. Can be overridden manually.

* **Src** (two fields, 0–255 each): The 16-bit source unit ID, used only for double-packet operations (Call Alert, Sel Call 1, Sel Call 2). Entered the same way as the target ID.

* **Status bar**: Shows `Ready`, `TX...`, or `Done!` depending on transmission state.

* **Frequency / Gain / AMP**: Standard TX controls in the bottom bar.

* **Start / Stop**: Transmit the current frame. Single transmit only — no loop mode.

# Operations

| Operation | Op code | Default Arg | Packet type |
|-----------|---------|-------------|-------------|
| PTT ID | 0x01 | 0x00 | Single |
| Emergency | 0x00 | 0x00 | Single |
| Radio Check | 0x63 | 0x85 | Single |
| Stun | 0x2B | 0x00 | Single |
| Unstun | 0x2B | 0x0C | Single |
| Status Req | 0x22 | 0x00 | Single |
| Status Resp | 0x06 | 0x00 | Single |
| Rem Monitor | 0x11 | 0x8A | Single |
| Message | 0x07 | 0x00 | Single |
| Sel Call 1 | 0x80 | — | Double (uses Src) |
| Call Alert | 0x81 | — | Double (uses Src) |
| Sel Call 2 | 0x82 | — | Double (uses Src) |

Double-packet operations send two codewords. The first codeword contains the target ID; the second contains the source ID from the **Src** field.

# Frame Structure

Each transmission consists of: 3 × 7-byte preamble (`0xAA`) + 5-byte sync word + one or two 14-byte codewords.

Each codeword carries: Op, Arg, ID high byte, ID low byte, CRC (2 bytes), padding (1 byte), plus 7 bytes of convolutional-encoded and bit-interleaved data.

# Settings Persistence

Settings are saved to `tx_mdc_tx.ini`.