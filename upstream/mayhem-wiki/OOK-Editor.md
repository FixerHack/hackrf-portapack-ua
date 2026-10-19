
![image](https://github.com/user-attachments/assets/b1cfb099-ef6e-456a-8456-c91df88e55a4)
![image](https://github.com/user-attachments/assets/88715817-7f37-4cbe-b771-89873a61517c)
![image](https://github.com/user-attachments/assets/9af89119-cf14-469c-8b00-e79e0bcd1dff)

OOK Editor is a free-form On-Off Keying transmitter. Unlike the [OOK TX](OOK) app, it does not use predefined encoder chip protocols — instead you define the payload bit-by-bit, either by typing it directly, using the Bug Key composer, or loading a `.OOK` file from the SD card.

This app is a lightly enhanced version of the ROOK application by @sasaga.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

* **Frequency / Gain / AMP**: Standard TX controls. Default frequency: **433.920 MHz**.

* **SampleRate**: The baseband sample rate used for transmission. Options: `250k`, `1M`, `2M`, `5M`, `10M`, `20M` Hz.

* **Step**: Increment used when adjusting **SymbolRate** and **PauseSymbol** fields with the encoder. Options: `1`, `10`, `100`.

* **SymbolRate** (0–9999): Number of symbols per second.

* **Repeat** (1–999): Number of times the payload is repeated per transmission.

* **PauseSymbol** (0–9999 µs): Pause duration between repetitions.

* **Payload**: Displays the current bit string to be transmitted (`0` = carrier off, `1` = carrier on).

* **Set**: Opens the text keyboard to type a payload manually.

* **Open File**: Opens a file browser in `OOKFILES/` to load a `.OOK` configuration file.

* **Save File**: Saves the current settings to a `.OOK` file in `OOKFILES/`.

* **Bug Key**: Opens the Bug Key composer view (see below).

* **Waveform**: Live preview of the current payload's OOK waveform.

* **Send / Stop**: Starts or stops transmission.

# Bug Key

The Bug Key is a quick pattern composer. It appends repeated `0` or `1` bits to the payload using configurable step sizes.

* **Primary Step** (0–550): Number of bits appended by the short buttons (`0` and `1`).
* **Secondary Step** (0–550): Number of bits appended by the long buttons (`00` and `11`).

| Button | Action |
|--------|--------|
| `0` | Appends Primary Step × `0` bits (carrier off) |
| `00` | Appends Secondary Step × `0` bits (carrier off) |
| `1` | Appends Primary Step × `1` bits (carrier on) |
| `11` | Appends Secondary Step × `1` bits (carrier on) |
| `
