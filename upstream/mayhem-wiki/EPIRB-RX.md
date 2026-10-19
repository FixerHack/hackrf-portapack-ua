# 🎯 Overview
The **EPIRB RX** application receives and decodes **ELT/EPIRB/PLB** [COSPAS/SARSAT](https://www.sarsat.noaa.gov/cospas-sarsat-system-overview/) emergency beacon frames.

<img height="360" alt="image" src="https://github.com/user-attachments/assets/5f740f62-1994-4a5b-9312-b2d4295238d9" />

<!--
<img height="360" alt="image" src="https://github.com/user-attachments/assets/b9e7a682-1fb9-4837-8588-0949720eb493" />&nbsp;&nbsp;&nbsp;&nbsp;[![Demo vidéo](https://img.youtube.com/vi/fgVSkCUypg8/0.jpg)](https://www.youtube.com/watch?v=fgVSkCUypg8)
-->

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## 🆘 Beacons
The **EPIRB RX** application decodes 406 MHz distress beacon transmissions from EPIRBs (Emergency Position-Indicating Radio Beacons), PLBs (Personal Locator Beacons), and ELTs (Emergency Locator Transmitters).

COSPAS/SARSAT [emergency beacons](https://www.sarsat.noaa.gov/emergency-406-beacons/) are used in boats (**EPIRB**), planes (**ELT**) or by individuals (**PLB**) to support Search And Rescue (**SAR**) operations by helping to locate accident sites.<br>

## 🦺 Error Correction
Received beacons are decoded using BCH error detection and single-bit correction. Each beacon state is color-coded:
* **Green** = valid packet
* **Yellow** = corrected (1-bit error fixed)
* **Red** = unrecoverable error

# 🎁 Features
RX parameters can be configured using standard RF settings: RF amplifier, LNA gain, and VGA gain.

Frequencies can be selected from a predefined list stored in the <code>EPIRB/FREQ.TXT</code> file.

The **EPIRB RX** application also outputs audio of the monitored frequency, with adjustable squelch and volume settings.

The application status header displays:
* A time counter showing seconds since startup, or a 50-second countdown after each frame
* The total number of received beacon frames
* Statistics for valid, corrected, and invalid frames
* The currently selected beacon information

The application uses a 4-tab layout:
* List Tab: displays a summary of recently received beacons
* Detail tab: shows detailed information about the selected beacon
* Map tab: displays the beacon's location
* QR tab: shows a QR code linking to the beacon location or details from [SARSAT Beacon Hex Decoder service](https://decoder2.herokuapp.com/decode)

The **EPIRB RX** application decoding algorithm is very sensitive to frequency alignment.
Due to size limitation of Mayhem applications, the **EPIRB RX** application does not provide a spectrum waterfall view.
Hearing a beacon frame does not necessarily mean you are tuned to the correct frequency, as COSPAS/SARSAT channels are very close to each other.
If decoding fails, it is recommended to use the [Audio](Audio-Receivers) application's waterfall view to verify frequency alignment.

# 📶 Protocol
Beacon frame data is encoded using **Manchester BPSK modulation** at **400 bits per second**, with a phase of **±63°**, in accordance with COSPAS/SARSAT specifications.

Each frame is preceded by a 160 ms carrier.

# 📻 Baseband
A dedicated proc_epirb **baseband processor** has been implemented using a state machine to:
- Detect the 160 ms carrier
- Detect the first phase transition and start Manchester decoding at each phase change
- Read packets using a dedicated PacketBuilder

An **Automatic Frequency Correction (AFC)** loop continuously tracks the carrier offset in the idle state, allowing the decoder to acquire signals up to **±5 kHz** off the nominal frequency before carrier lock. This eliminates the need for manual frequency fine-tuning in most cases and makes the decoder tolerant of oscillator drift and Doppler shift.

# ❓ User Guide
### 📡 Receiver section
This section is used to adjust receiver parameters for optimal decoding.
<table>
  <tbody>
    <tr>
      <td style="border: none" width="360">
      <img width="350" alt="image" src="https://github.com/user-attachments/assets/a5f10895-5594-4554-a214-cb3e602f744c" />
      </td>
      <td style="border: none">
<u>Receiver parameters:</u><br>
- <code>RFA</code>: <b>RF Amplifier</b> (0 or 1)<br>
- <code>LNA</code>: <b>LNA gain</b> (0–40)<br>
- <code>VGA</code>: <b>VGA gain</b> (0–62)<br>
- <code>SQL</code>: <b>Squelch</b> level for audio output (0-99)<br>
- <code>Audio</code>: <b>Audio output level</b> (0-99)<br>
<br>
The channel power bar turns <b>red</b> when the received signal approaches ADC full scale (overload threshold: −3 dBFS). This indicates front-end clipping which distorts the constant-envelope carrier and degrades decoding. Reduce <code>RFA</code>, <code>LNA</code>, or <code>VGA</code> gain until the bar returns to its normal color.<br>
      </td>
    </tr>
  </tbody>
</table>

### ℹ️ Application status
This section displays the current application status.
<table>
  <tbody>
    <tr>
      <td style="border: none" width="400">
<img width="390" alt="image" src="https://github.com/user-attachments/assets/c223a44b-459b-4c48-b7b3-413b6768f721" />
      </td>
      <td style="border: none">
<u>Application status:</u><br>
- <code>TIME</code>: shows seconds since startup or the countdown to the next beacon (50 s)<br>
- <code>COUNT</code>: index of the selected beacon <b>/</b> total received beacons<br>
- <code>STATS</code>: number of valid / corrected / invalid beacons<br>
- <code>ID</code>: short ID of the selected beacon<br>
- <code>TYPE</code>: type of the selected beacon<br>
- <code>LOC</code>: Maidenhead Locator of the selected beacon<br>
- <code>STATE</code>: satus (OK/KO) of the selected beacon<br>
      </td>
    </tr>
  </tbody>
</table>

### 📓 List Tab
The first tab displays a list of recently received beacons.<br> 
<table>
  <tbody>
    <tr>
      <td style="border: none" width="270">
<img width="240" height="320" alt="image" src="https://github.com/user-attachments/assets/7619d128-936d-452f-8b66-109c82ccaf89" />
</td>
      <td style="border: none">
<u>Each entry gives:</u><br>
- Reception time<br>
- Beacon short ID<br>
- Beacon type<br>
- Location (if available): Maidenhead locator<br>
- Status (<code>OK</code> if BCH1 and BCH2 codes are valid, <code>KO</code> otherwise ; if <code>OK</code> is displayed in yellow, it means that the frame has been corrected to match BCH1 and/or BCH2 code)
      </td>
    </tr>
  </tbody>
</table>

**Note** : In case that you are not decoding any received audible EPIRB burst signal , and you have selected a correct tuning frequency,  please make sure if your system is using an external portapack built-in , 10 Mhz TCXO reference clock or not. You can see it , just going to menu , Settings / Radio you can see in the top of the picture if your system is using external 10 Mhz TCXO or internal 25Mhz Hackrf xtall.<br> 

<img width="591" height="334" alt="image" src="https://github.com/user-attachments/assets/9fa0df3b-d9a0-49fe-a127-ac80029d80b3" />


In case that your system is using the internal (non TCXO)  25Mhz Hackrf xtall, you can confirm that possible freq. offset  using some good external  PLL digital receiver (HF, of FM ,VHF, or UHF)  and use any TX App (like example MIC App) and check and eventually compensate the potential  +/- frequency drift through the menu Settings / Radio / Frequency correction , example -05 PPM, as above right picture  (save that PPM compensation and from now on it will be automatically applied to both TX and RX App's . 

### 🔍 Detail Tab
This tab provides detailed information about the selected beacon.
<table>
  <tbody>
    <tr>
      <td style="border: none" width="270">
<img width="240" height="320" alt="image" src="https://github.com/user-attachments/assets/195c336e-225c-4639-81fe-7cdbef8b8016" />
</td>
      <td style="border: none">
<u>Controls:</u><br>
The encoder can be used to change the selected beacon.<br>
<u>Beacon details:</u><br>
- Beacon type (EPIRB/ELT/PLB etc), mode (real/test) and reception time<br>
- Protocol (Standard/User/National etc), Protocol description, and additional data<br>
- Emergency type (if available): distress reason encoded in the message (Fire, Flooding, Collision, Grounding, Sinking, Disabled etc.)<br>
- Country of origin<br>
- Location (if available) in 3 formats<br>
&nbsp;&nbsp;&nbsp;&nbsp;o Maidenhead Locator,<br>
&nbsp;&nbsp;&nbsp;&nbsp;o DMS coordinates,<br>
&nbsp;&nbsp;&nbsp;&nbsp;o Decimal coordinates.<br>
- BCH1 et BCH2 control code status (if in yellow, it means that the frame has been corrected to match BCH1/BCH2 code)<br>
- Beacon Hex ID<br>
- Beacon Serial Number (if available)<br>
- Main location device<br>
- Auxiliary location device<br>
      </td>
    </tr>
  </tbody>
</table>

### 🗺️ Map Tab
Displays the selected beacon on a map.
Other beacons within the visible map area are also displayed.
<table>
  <tbody>
    <tr>
      <td style="border: none" width="270">
<img width="240" height="320" alt="image" src="https://github.com/user-attachments/assets/9d608cfd-50d3-4af6-bc36-605e8466f13c" />
</td>
      <td style="border: none">
<u>Controls:</u><br>
- Arrow keys to move the map<br>
- Encoder to adjust zoom<br>
      </td>
    </tr>
  </tbody>
</table>

### 🔗 QR Tab
Display QR codes that can be scanned to access location or details from [SARSAT Beacon Hex Decoder service](https://decoder2.herokuapp.com/decode)
<table>
  <tbody>
    <tr>
      <td style="border: none" width="270">
<img width="240" height="320" alt="image" src="https://github.com/user-attachments/assets/11ce1e35-374b-436f-a44e-7a4b85be086f" />
</td>
      <td style="border: none">
<u>QR Tab:</u><br>
- QR option field can be used to chose between <code>Map</code> and <code>Detail</code> QR code:<br>
&nbsp;&nbsp;&nbsp;&nbsp;o <code>Map</code> QR code can be scanned to link to the beacon's coordinates in Maps<br>
&nbsp;&nbsp;&nbsp;&nbsp;o <code>Detail</code> QR code can be scanned to link to the beacon's details in  <a href="https://decoder2.herokuapp.com/decode">SARSAT Beacon Hex Decoder service</a><br>
- <code>Data</code> shows raw beacon frame data<br>
      </td>
    </tr>
  </tbody>
</table>

# ⚙️ Settings
### 📝 <code>SETTINGS/rx_epirb.ini</code> file
In addition to receiver settings, that are available from the UI, other settings can accessed by editing `SETTINGS/rx_epirb.ini` file when **App Settings** is enabled in the global [Settings](Settings#app-settings) menu.

This settings include:
* <code>countdown</code>: duration (in seconds) of the countdown that starts after receiving a frame

### 📝 <code>EPIRB/FREQ.TXT</code> file
The list of frequencies available from the frequency selector comes from <code>EPIRB/FREQ.TXT</code> file.

You can edit this file to add custom frequencies.

Default frequencies:
+ **406.025 MHz** (406025000)
+ **406.028 MHz** (406028000)
+ **406.037 MHz** (406037000)
+ **406.040 MHz** (406040000)
+ **406.049 MHz** (406049000)
+ **406.052 MHz** (406052000)
+ **406.061 MHz** (406061000)
+ **406.064 MHz** (406064000)
+ **433.025 MHz** (433025000)
+ **144.875 MHz** (144875000)
+ **406.022 MHz** (406022000)
