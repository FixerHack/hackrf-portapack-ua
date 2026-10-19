
TouchTunes is a jukebox platform found in bars, pubs, and restaurants across North America. TouchTunes jukeboxes (Gen 2 and above) use a wireless remote that transmits NEC-encoded messages via ASK/OOK at 433.92 MHz. These remotes are used for basic jukebox functions such as power, skip, volume, etc. The wireless messages are addressed using PINs 000–255 to prevent multiple units from interfering with each other. **The default PIN is 000 in most deployments.**

This app emulates TouchTunes wireless remotes (Gen 2 and newer) and supports both single-address and brute-force (scan) modes.

# How To Use

![](/portapack-mayhem/mayhem-firmware/wiki/img/screenshots/Transmit_TouchTune.png)

* **Transmit a command:** Press any button on the touchscreen, or highlight and select with the physical controls. Each command is transmitted 4 times automatically.
* **Change the PIN:** Adjust the 3-digit PIN field in the top-left using the encoder knob. Default is 000. Range: 000–255.
* **Brute force (Scan mode):** Enable the **Scan** checkbox, then press any button. The selected command will be transmitted 4 times for each PIN from 000 to 255 in sequence, covering all 256 possible addresses.
* **EW Mode (Electronic Warfare, Experimental):** Transmits a continuous CW carrier at 433.92 MHz to jam the jukebox's receiver, preventing others from sending commands. You retain control — the jamming signal automatically pauses when you transmit a command, then resumes. Enable with the **EW Mode** checkbox.

# Message Structure

### Basic Info

* **Frequency:** 433.92 MHz
* **Modulation:** ASK/OOK
* **Protocol:** NEC (without address complement)
* **Sample rate:** 2.28 MSps
* **Symbol rate:** 1766 baud (measured; nominal NEC rate is 1786 baud)
* **Symbol period:** 566 µs
* **Repeats per command:** 4

### NEC Symbol Encoding

* **Short (0):** `10` (OOK: ON OFF)
* **Long (1):** `1000` (OOK: ON OFF OFF OFF)

### Frame Structure

```
{PREAMBLE} {SYNC} {PIN} {COMMAND} {TAIL}
```

* **Preamble (literal symbols):** `0xFFFF00`
* **Sync (decoded NEC):** `0x5D`
* **PIN 000–255 (decoded NEC):** `0x00–0xFF` (LSB first)
* **Tail (literal symbols):** `0x8`

### Commands (pre-NEC encode)

Each command byte is doubled with the second half bit-reversed before NEC encoding. For example, Pause (`0x32`) becomes `0x3223` before encoding.

| Code | Button |
|---|---|
| `0x32` | Pause |
| `0x78` | On/Off (Power) |
| `0x70` | P1 |
| `0x60` | P2 Edit Queue |
| `0xCA` | P3 |
| `0x20` | F1 Restart |
| `0xF2` | Up (^) |
| `0xA0` | F2 Key |
| `0x84` | Left (<) |
| `0x44` | OK |
| `0xC4` | Right (>) |
| `0x30` | F3 Mic A Mute |
| `0x80` | Down (V) |
| `0xB0` | F4 Mic B Mute |
| `0xF0` | 1 |
| `0x08` | 2 |
| `0x88` | 3 |
| `0x48` | 4 |
| `0xC8` | 5 |
| `0x28` | 6 |
| `0xA8` | 7 |
| `0x68` | 8 |
| `0xE8` | 9 |
| `0x18` | * (Music / Karaoke) |
| `0x98` | 0 |
| `0x58` | # (Lock Queue) |
| `0xD0` | Zone 1 Vol+ |
| `0x90` | Zone 2 Vol+ |
| `0xC0` | Zone 3 Vol+ |
| `0x50` | Zone 1 Vol- |
| `0x10` | Zone 2 Vol- |
| `0x40` | Zone 3 Vol- |

### Example

**Command:** PIN 000 – On/Off  
**Literal symbols (hex):** `ffff00 a2888a2aaaa8888aa2aa2220`  
(PREAMBLE SYNC PIN COMMAND TAIL)