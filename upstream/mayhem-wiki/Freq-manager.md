The **Freq Manager** (Freqman) is a frequency database manager. It lets you browse, create, edit, and delete frequency entries organized into named lists (categories). These lists are shared with other apps such as [[Recon]], [[Scanner]], and the [[Audio-Receivers|Audio]] receiver, which can load them directly.

## SD Card location

Freqman files are stored in the `FREQMAN/` folder on the SD card as plain `.TXT` files. Each file is one category.

## Using the app

The top bar shows the current category (file). Use the encoder to cycle through categories.

| Button | Action |
|--------|--------|
| 📄 (new file icon) | Create a new category |
| 🗑 (red trash icon) | Delete the current category |
| **Edit** | Open the full edit screen for the selected entry |
| **Frequency** | Quick-edit just the frequency of the selected entry |
| **Description** | Quick-edit just the description of the selected entry |
| ➕ (add icon) | Add a new entry to the current category |
| 🗑 (red delete icon) | Delete the selected entry |
| **Exit** | Exit the app |

The edit screen lets you set: Entry Type, Frequency A, Frequency B, Modulation, Bandwidth, Step, Tone (CTCSS), and Description.

## Freqman file format

Files are plain text, one entry per line. Fields are comma-separated `key=value` pairs.

- Empty lines are ignored
- Lines starting with `#` are comments and are ignored
- Maximum description length: 30 characters
- Maximum entries per file: 150 (file is truncated if exceeded)

> [!WARNING]
> Any content that does not match a recognized field is silently ignored.

### Entry type fields

Every entry must begin with one of these type-defining key pairs:

| Keys | Type | Description |
|------|------|-------------|
| `f=freq` | Single | One frequency |
| `a=start,b=end` | Range | Frequency range to scan |
| `r=rx_freq,t=tx_freq` | HamRadio | Ham relay: RX and TX frequencies. TX is scanned as a single frequency in scanner mode. |
| `l=listen_freq,t=tx_freq` | Repeater | Repeater: listen frequency (also used as single freq when repeater mode is inactive) and TX offset |

### Optional fields

| Key | Description |
|-----|-------------|
| `m=modulation` | Modulation mode |
| `bw=bandwidth` | Bandwidth (must appear **after** `m=` in the line) |
| `s=step` | Frequency step — only meaningful for Range entries |
| `c=tone` | CTCSS tone frequency — only meaningful for HamRadio entries |
| `d=description` | Free-text description (max 30 characters) |

### Possible values for modulation

| Value | Notes |
|-------|-------|
| `AM` | |
| `NFM` | |
| `WFM` | |
| `SPEC` | Spectrum / raw IQ |
| `AMFM` | Special: AM+FM demod for HF WeatherFax (used by [[WeatherFax]] app) |
| `FMAM` | Special: FM+AM demod for NOAA 137 MHz APT (used by [[NOAA]] app) |

### Possible values for bandwidth

**AM:** `DSB 9k`, `DSB 6k`, `USB+3k`, `LSB-3k`, `CW`

**NFM:** `8k5`, `11k`, `12k5`, `16k`

**WFM:** `80k`, `180k`, `200k`

**SPEC:** `12k5`, `16k`, `25k`, `32k`, `50k`, `75k`, `100k`, `150k`, `250k`, `500k`, `600k`, `750k`, `1000k`, `1250k`, `1500k`, `1750k`, `2000k`, `2250k`, `2500k`, `3000k`, `3500k`, `4000k`, `4500k`, `5000k`, `5500k`

### Possible values for step

`10Hz`, `50Hz`, `0.1kHz`, `1kHz`, `5kHz`, `6.25kHz`, `8.33kHz`, `9kHz`, `10kHz`, `12.5kHz`, `15kHz`, `25kHz`, `30kHz`, `50kHz`, `100kHz`, `250kHz`, `500kHz`, `1MHz`

## Example file
```
# My frequency list
f=468000000,d=Single Freq
f=468000000,m=AM,d=Single Freq AM
f=468000000,m=NFM,bw=12k5,d=Single Freq NFM
f=468000000,m=WFM,bw=200k,d=Single Freq WFM
f=468000000,m=AM,bw=USB+3k,d=Single Freq AM USB
a=87000000,b=110000000,m=WFM,bw=200k,s=50kHz,d=WFM radio search
r=430150000,t=430550000,d=HAM relay
r=430150000,t=430550000,m=NFM,bw=12k5,c=88.5,d=HAM with CTCSS
l=430150000,t=431150000,m=SPEC,bw=1000k,d=1MHz repeat txoffset
```

## Additional freqman files

Community-maintained and country-specific freqman files are available at:
https://github.com/portapack-mayhem/mayhem-freqman-files