# 🎯 Overview
**EPIRB TX** application simulates an **ELT/EPIRB/PLB** [COSPAS/SARSAT](https://www.sarsat.noaa.gov/cospas-sarsat-system-overview/) emergency beacon.

<img height="360" alt="image" src="https://github.com/user-attachments/assets/b9e7a682-1fb9-4837-8588-0949720eb493" />&nbsp;&nbsp;&nbsp;&nbsp;[![Demo vidéo](https://img.youtube.com/vi/fgVSkCUypg8/0.jpg)](https://www.youtube.com/watch?v=fgVSkCUypg8)

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## 📡 Beacons
COSPAS/SARSAT [emergency beacons](https://www.sarsat.noaa.gov/emergency-406-beacons/) are used in boats (**EPIRB**), planes (**ELT**) or by individuals (**PLB**) to facilitate Search And Rescue (**SAR**) missions by helping to locate accident sites.<br>
This application is intended for testing COSPAS SARSAT [406 decoding devices](https://github.com/fredzo/SarsatJRX) used by **HAM radio Civil Security SAR teams** around the world.

There are two generation of 406 MHz beacons:
* First Generation Beacons (FGB) use a **Manchester encoded BPSK signal**,
* Second Generation Beacons (SGB) use **DSSS-OQPSK modulation**.

## :warning: **Warning** :warning:
This application only transmits **"Self-Test"** beacon frames.<br>
It **MUST NOT** be used to send real (non test) beacon data, as it could initiate a **Search And Rescue alert**.

# 🎁 Features
The application features two transmission modes:
* A **406 MHz signal** (Manchester encoded BPSK for FGB or DSSS-OQPSK modulation for SGB) containing beacon data,
* A **127.5 MHz AM distress audio signal**.

Beacon data can be selected from two different sources:
* A set of **test beacons** stored in the `BEACONS.TXT` file in `EPIRB` directory of the SD card,
* A **manual beacon editor** integrated in the application, allowing selection of beacon type and location.

Beacon frames can be sent periodically (using the `Resend` checkbox) every **50 seconds** (adjustable).<br>
If `AM signal` checkbox is enabled, the transmission will automatically switch to **121.5 MHz AM emergency signal** at the end of the BPSK/OQPSK frame.<br>
If the `Send on change` checkbox is enabled, a new frame will be sent each time a beacon parameter is modified.

# 📶 Protocol
First Generation Beacon frame data is encoded using **Manchester BPSK modulation** at **400 bits per second**, with a phase of **±63°**, in accordance with COSPAS/SARSAT specifications.
Second Generation Beacon frame data is encoded using *OQPSK** at **300 bits per second** with DSSS spreading.

# 📻 Baseband
A dedicated proc_epirb_tx **baseband processor** is used for:
- BPSK/OQPSK data transmission,
- AM emergency signal generation.

The **121.5 MHz AM emergency signal** is an audio signal using a **3Hz frequency sweep from 300 Hz to 1600 Hz** reproducing the typical ELT distress sound.

# ❓ User Guide
### 📝 Beacon Editor Mode
<table>
  <tbody>
    <tr>
      <td style="border: none" width="270">
<img width="247" height="330" alt="image" src="https://github.com/user-attachments/assets/abea66d6-3368-4c03-b523-60d574b1f61b" />
</td>
      <td style="border: none">
<u>Manual (Editor) mode:</u><br>
- Select beacon type (<code>ELT</code> / <code>EPIRB</code> / <code>PLB</code>)<br>
- Select location protocol (<code>Standard</code> / <code>User</code> / <code>National</code>)<br>
- Select beacon format (<code>FGB</code> / <code>SGB</code>)<br>
- Select beacon country<br>
- Enable <code>Internal</code> checkbox to indicate that the beacon uses an internal positioning device<br>
- Set beacon location using <b>Maidenhead Locator</b> or the <b>Map View</b>(<code>Set pos.</code> button)
      </td>
    </tr>
  </tbody>
</table>

### 🗺️ Map View
<table>
  <tbody>
    <tr>
      <td style="border: none" width="270"><img width="240" height="320" alt="image" src="https://github.com/user-attachments/assets/e3508345-9adc-46af-a090-44ea5c98d531" /></td>
      <td style="border: none">
<u>Map View:</u><br>
- In Manual mode, beacon location can be set using the <code>Set pos.</code> button<br>
- Map View is then displayed to allow beacon location adjustment<br>
- Edit coordinates or move the cursor on the map<br>
- Press the <code>OK</code> button to validate coordinates and return to the main screen<br>
      </td>
    </tr>
  </tbody>
</table>

### 📄 Beacon File Mode

<table>
  <tbody>
    <tr>
      <td style="border: none" width="270">
<img width="247" height="330" alt="image" src="https://github.com/user-attachments/assets/96ea7dd8-9003-4d56-bc70-2b9a12cfd70e" />
</td>
      <td style="border: none">
<u>File (<code>BEACONS.TXT</code>) mode:</u><br>
- Select a beacon from the samples stored in <code>EPIRB/BEACONS.TXT</code> file on the SD card<br>
- Enable <code>Slideshow</code> checkbox to have the application automatically move to the next beacon in <code>BEACONS.TXT</code> file after each send<br> 
<br>
<u><code>BEACONS.TXT</code> file format:</u><br>
- <b>3-columns CSV file</b> using <code>;</code> as separator<br>
- Lines starting with <code>#</code> are treaed as comments<br>
Columns:<br>
-1. Beacon title (displayed in the UI Options list)<br>
-2. Beacon description (displayed in the UI description field)<br>
-3. Beacon data, as:<br>
&nbsp;&nbsp;&nbsp;&nbsp;o a <b>36-character hexadecimal string</b> (2 HEX characters per byte), including <code>FFFED0</code> synchronization header for FGB format<br>
&nbsp;&nbsp;&nbsp;&nbsp;o a <b>63-character hexadecimal string</b> (250 bits, padded right) for SGB format<br>
      </td>
    </tr>
  </tbody>
</table>

### 📡 Transmission block

<table>
  <tbody>
    <tr>
      <td style="border: none" width="270">
<img width="247" height="330" alt="image" src="https://github.com/user-attachments/assets/20fa33a9-74aa-4678-a321-c3aa759c774b" />
</td>
      <td style="border: none">
<u>Transmission controls:</u><br>
- Enable <code>Resend every xx s.</code> checkbox to periodically retransmit the frame<br>
- Adjust the resend period using the delay value<br>
- Enable <code>AM signal</code> checkbox to transmit the <b>121 MHz emergency signal</b> between frames<br>
- Set the emergency signal frequency using the <code>AM frequency</code> input (Manual channel)<br>
- Enable <code>Send on change</code> checkbox to automatically retransmit when frame content is modified<br>
- Use the <code>Start</code>/<code>Stop</code> button to activate/deactivate the beacon simulation<br>
- Use <code>AM chan</code> to select the channel for AM signal<br>
- Use <code>BPSK chan</code> to select the channel for BPSK/OQPSK signal<br>
      </td>
    </tr>
  </tbody>
</table>

### 📻 Transmitter View

<table>
  <tbody>
    <tr>
      <td style="border: none" width="270">
<img width="247" height="330" alt="image" src="https://github.com/user-attachments/assets/fd2f49c8-a2cd-44d7-afb2-07952267001c" />
</td>
      <td style="border: none">
<u>This is the <b>generic PortaPack Transmitter view</b>, used to configure:</u><br>
- BPSK/OQPSK transmission frequency (Manual channel)<br>
- Frequency step<br>
- Transmitter bandwidth (N/A in this direct IQ PSK mod. scheme)<br>
- Transmitter GAIN-TX dB control ,step 1 dB , (<b>0 to +47 dB</b>)<br>
- Transmitter RF-AMP  gain , OFF-ON , (<b>0 or +14 dB</b>)<br>
      </td>
    </tr>
  </tbody>
</table>
