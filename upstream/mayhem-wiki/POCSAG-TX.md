## Overview

<img width="238" height="324" alt="POCSAG TX app screenshot" src="https://github.com/user-attachments/assets/c4d86a38-dfc8-432e-ac96-eb28fb79dafb" />

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Introduction

This application allows you to transmit messages using the **POCSAG** protocol with the PortaPack running **Mayhem** firmware. POCSAG (Post Office Code Standardisation Advisory Group) is a one-way paging protocol that uses 2-FSK modulation on narrowband FM channels.

It is intended for testing, experimentation, and educational use with licensed amateur radio equipment or on frequencies for which you hold the appropriate authorization.

## Frequency

The default frequency is **466.175 MHz**, which is a commercial paging frequency used in some regions. This must be changed to match your intended use:

| Frequency | Use |
|-----------|-----|
| 439.9875 MHz | Amateur Radio DAPNET (worldwide) |
| 466.075 MHz | Commercial paging (region-dependent) |
| 466.175 MHz | Commercial paging (default, region-dependent) |
| Other | Varies by country and operator |

For Amateur Radio use with DAPNET, use **439.9875 MHz** at **1200 bps**. See [DAPNET](https://hampager.de) for registration details.

## Message Controls

These settings define the content and format of the POCSAG message:

### Bitrate

Select the transmission bitrate:
- **512 bps** — older pagers, longer range
- **1200 bps** — most common, used by DAPNET and most commercial systems
- **2400 bps** — faster, shorter range, fewer compatible pagers

### Address

The destination pager address. This is a 7-digit decimal field (0000000 – 9999999). The POCSAG protocol supports 21-bit addresses (maximum 2,097,151). Values above this are outside the protocol specification. Address 0 is a broadcast address received by all pagers.

### Type

The message type determines how the payload is encoded:

| Type | Description |
|------|-------------|
| Address only | No message payload — sends address and function code only. Used to trigger tone-only pagers. |
| Numeric only | Numeric characters only. Valid characters: `0–9`, `S`, `U`, `]`, `[`, `-`, space. |
| Alphanumeric | Full ASCII text message, up to 80 characters. |

### Function

The function code is a 2-bit field (A–D) transmitted with every POCSAG message. Its meaning is defined by the receiving pager and operator, but conventional usage is:

| Code | Conventional meaning |
|------|----------------------|
| A | Tone only / alert |
| B | Numeric message |
| C | Alphanumeric message |
| D | Voice call / operator-defined |

Most modern pagers accept any function code for alphanumeric messages. When in doubt, use **A**.

### Phase

Selects the signal polarity of the transmitted bitstream:

- **P (Positive)** — bits are inverted before transmission (`~codeword`). Some pager systems expect this polarity.
- **N (Normal)** — bits are transmitted as-is. This is the standard POCSAG polarity per the specification.

If a pager does not respond to transmission with one phase setting, try the other.

### Message

The text payload to transmit. Maximum length is **80 characters**.

- For **Numeric only**, only `0–9 S U ] [ -` and space are valid. Other characters will trigger an error.
- For **Alphanumeric**, standard printable ASCII is supported.
- Use the **Set message** button to enter the text.

## Transmit Controls (Lower Bar)

### First Line

- **Frequency** — Transmission frequency. Adjust with the encoder wheel, on-screen keypad, or load from SD card.
- **Frequency Step** — Step size when adjusting frequency with the encoder.
- **Channel Bandwidth** — RF bandwidth. Fixed at 1.75 MHz (narrowband FM, suitable for 12.5 kHz and 25 kHz POCSAG channels).

### Second Line

- **Gain (IF)** — TX gain in dB (0–47). See [Description of gain settings](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Main-Controls) for details.
- **AMP** — RF amplifier: `1` = enabled (+14 dB), `0` = disabled.

## Transmission

Press the **START** button to begin transmitting. A progress bar shows transmission progress. Transmission stops automatically when the message is complete.

## USB Serial Console

The POCSAG TX app can be triggered remotely via the USB serial console using the `sendpocsag` command:

```
sendpocsag   [baud] [type] [function] [phase]
```

| Parameter | Values | Description |
|-----------|--------|-------------|
| addr | 0–2097151 | Destination pager address |
| msglen | 0–80 | Message length in bytes. Use 0 for address-only. |
| baud | 512, 1200, 2400 | Bitrate (optional, default 1200) |
| type | 0, 1, 2 | 0=ADDRESS_ONLY, 1=NUMERIC_ONLY, 2=ALPHANUMERIC |
| function | A, B, C, D | Function code |
| phase | P, N | Signal polarity |

After sending the command, the console will prompt: `send  bytes`. Send exactly that number of bytes as the message payload. If `msglen` is 0, transmission starts immediately without a message.

Example — send alphanumeric message to address 1234567 at 1200 bps:
```
sendpocsag 1234567 12 1200 2 A N
```
Then send: `Hello World!`

See the [USB Serial Console](https://github.com/portapack-mayhem/mayhem-firmware/wiki/USB-Serial-Console) page for connection instructions.

## Testing

A reliable way to verify your transmission is to use the [POCSAG Receiver](https://github.com/portapack-mayhem/mayhem-firmware/wiki/POCSAG-Receiver) app on a second PortaPack, or use an SDR receiver with software such as [PDW](http://www.discriminator.nl/pdw/index-en.html) (Windows) or [multimon-ng](https://github.com/EliasOenal/multimon-ng) (Linux).

## Legal notice

POCSAG operates on licensed frequencies. Transmitting on commercial paging frequencies without authorization is illegal in all jurisdictions. Transmitting on amateur radio frequencies (such as 439.9875 MHz for DAPNET) requires a valid amateur radio license.

The HackRF One is a test and development device. The licensed operator is responsible for ensuring that all transmissions comply with local regulations regarding frequency, power, and authorized use.

## Further reading

- [POCSAG Receiver](https://github.com/portapack-mayhem/mayhem-firmware/wiki/POCSAG-Receiver)
- [POCSAG protocol overview](https://github.com/portapack-mayhem/mayhem-firmware/wiki/POCSAG)
- [USB Serial Console — sendpocsag command](https://github.com/portapack-mayhem/mayhem-firmware/wiki/USB-Serial-Console)
- [DAPNET Amateur Radio Paging Network](https://hampager.de)
- [multimon-ng POCSAG decoder](https://github.com/EliasOenal/multimon-ng)