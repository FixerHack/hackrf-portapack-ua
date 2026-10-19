> [!WARNING]
> This application is intended solely for experimental purposes on equipment you own or have permission to test. You are responsible for complying with all applicable laws.

OOK TX transmits On-Off Keying signals using pre-defined encoder chip protocols. It is commonly used for testing remote controls, gate openers, and similar 315 MHz / 433.92 MHz OAM devices. The app has two tabs: **Config** (manual frame construction) and **de Bruijn** (automated code scanning).

# Config Tab

* **Type**: Encoder chip protocol. 14 types are supported:

  | Name | Chip | Address symbols | Data symbols | Word length | Default clk |
  |------|------|----------------|-------------|------------|-------------|
  | 2260-R2 | PT2260-R2 | 0, 1, F | 0, 1 | 12 | 150 kHz |
  | 2260-R4 | PT2260-R4 | 0, 1, F | 0, 1 | 12 | 150 kHz |
  | 2262 | PT2262 | 0, 1, F | 0, 1, F | 12 | 20 kHz |
  | 16-bit | — | 0, 1 | 0, 1 | 16 | 25 kHz |
  | 1527 | RT1527 | 0, 1 | 0, 1 | 24 | 100 kHz |
  | 526E | HK526E | 0, 1 | 0, 1 | 12 | 20 kHz |
  | 12E | HT12E | 0, 1 | 0, 1 | 12 | 3 kHz |
  | 5026 | VD5026 | 0, 1, 2, 3 | 0, 1, 2, 3 | 12 | 100 kHz |
  | UM3750 | UM3750 | 0, 1 | 0, 1 | 12 | 100 kHz |
  | UM3758 | UM3758 | 0, 1, F | 0, 1 | 18 | 160 kHz |
  | BA5104 | BA5104 | 0, 1 | 0, 1 | 9 | 455 kHz |
  | 145026 | MC145026 | 0, 1, F | 0, 1 | 9 | 455 kHz |
  | HT6*** | HT6xxx | 0, 1, F | 0, 1 | 18 | 80 kHz |
  | TC9148 | TC9148 | 0, 1 | 0, 1 | 12 | 455 kHz |

* **Repeat** (1–99): Minimum number of times the frame is repeated per transmission. Automatically set to the encoder's default when the type changes.

* **Clk** (1–1000 kHz): Encoder oscillator clock frequency. Changing this updates **Frame** automatically. Step size is set by the adjacent **Step** selector (1 / 10 / 100 kHz).

* **Frame** (300–99,999 µs): Frame duration in microseconds. Changing this updates **Clk** automatically. Step size is set by its adjacent **Step** selector (1 / 10 / 100 / 1000 µs). Clock and frame are interlinked: `frame_µs = clk_period_µs × word_length`.

* **Symbols**: The bit pattern to transmit. Each position corresponds to a symbol in the word format shown on the line below (A = Address, D = Data, S = Sync). Symbols are selectable per encoder type — for example `0`, `1`, and `F` (float) for tri-state encoders.

* **Waveform**: Live preview of the generated OOK waveform for the current symbol pattern.

* **Progress bar / status**: Shows repeat count (`n/total`) and transmission progress.

# de Bruijn Tab

Transmits a de Bruijn sequence — a cyclic bit sequence that contains every possible n-bit combination exactly once. This is used to scan all possible codes for a given bit length without needing to enumerate them individually.

* **Length** (3–24 bits): The code word length `n`. A length-`n` de Bruijn sequence covers all `2ⁿ` combinations.

* **Bit length** (two fields): The duration of each bit in microseconds, entered as tens + units (e.g. `40` + `0` = 400 µs per bit). Range: 10–889 µs.

# Common Controls

* **Frequency / Gain / AMP**: Standard TX controls in the bottom bar. Default frequency: 433.920 MHz.
* **Start / Stop**: Begins or aborts transmission. When the de Bruijn tab is active, starts a scan; when the Config tab is active, transmits the configured frame.

# Settings Persistence

Settings are saved to `tx_ook.ini`.