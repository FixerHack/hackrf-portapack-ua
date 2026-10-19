RDS TX transmits Radio Data System (RDS) data on the 57 kHz subcarrier of an FM broadcast signal. It allows broadcasting of station name, program type, program ID, traffic flags, and scrolling text to RDS-capable FM receivers.

The app uses 4 tabs: **Name**, **Text**, **Time**, and **Audio**. Only the Name and Text tabs are currently functional; Time and Audio display "Not yet implemented."

# RF Parameters

| Parameter | Value |
|---|---|
| Default frequency | Stored in persistent memory |
| Frequency step | 50 kHz |
| Bandwidth | 1.75 MHz |
| Sample rate | 2.28 MSps |
| TX gain | 0–47 dB (LNA), 0/14 dB (AMP) |

Settings are saved to `tx_rds.ini`.

# Common Controls (all tabs)

These controls appear at the top of the screen regardless of the active tab:

* **Program type (PTY):** Dropdown with 32 options (codes 0–31): None, News, Affairs, Info, Sport, Educate, Drama, Culture, Science, Varied, Pop, Rock, Easy, Light, Classics, Other, Weather, Finance, Children, Social, Religion, PhoneIn, Travel, Leisure, Jazz, Country, National, Oldies, Folk, Docs, AlarmTst, Alarm.
* **Program ID (PI):** 4-digit hex value (0000–FFFF). Identifies the station globally.
* **TP (Traffic Program):** Checkbox — signals that the station regularly broadcasts traffic information.

# Name Tab

* **Transmit PSN** (checkbox): Enables transmission of the Program Service Name.
* **PSN:** The station name shown on FM receivers. Maximum 8 characters. Default: `TEST1234`. Press **Set** to open the text entry keyboard.
* **Stereo:** Checkbox — sets the DI (Decoder Identification) bit to indicate stereo audio.
* **Music:** Checkbox — sets the MS (Music/Speech) bit.
* **Traffic announcement (TA):** Checkbox — signals an active traffic announcement on this channel.

# Text Tab

* **Transmit Radiotext** (checkbox): Enables transmission of the RadioText (RT) message.
* **Text:** Free-form scrolling text displayed on receivers. Maximum 28 characters in this implementation. Default: `Radiotext test ABCD1234`. Press **Set** to open the text entry keyboard.

# Time Tab

Displays "Not yet implemented." Date and time transmission (RDS group type 4A / CT) is not functional.

# Audio Tab

Displays "Not yet implemented." Audio-related RDS data transmission is not functional.

# Starting Transmission

Press **Start** at the bottom of the screen to begin transmitting. Press it again to stop. All enabled tabs (PSN and/or Radiotext) are transmitted in rotation.