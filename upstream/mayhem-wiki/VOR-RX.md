# VOR RX

A **VOR** (VHF Omnidirectional Range) ground station lets an aircraft determine its bearing (radial) to or from the station. The station radiates two 30 Hz signals: a reference phase (FM-modulated onto a 9960 Hz subcarrier) and a variable phase (AM). The phase difference between them equals the receiver's bearing from the station, so every direction around the beacon has a unique phase relationship.

**VOR RX** tunes the VOR band (108–117.95 MHz, AM) and recovers both 30 Hz tones to decode that bearing. To do this it keeps the channel at 48 kHz rather than applying the usual AM decimation, which would otherwise filter out the 9960 Hz subcarrier and destroy the reference phase. The decoded radial, a selectable course (OBS) and a course-deviation indicator are shown so the app works like a basic aircraft VOR instrument.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card). It was introduced in [#3244](https://github.com/portapack-mayhem/mayhem-firmware/pull/3244).

New to VOR navigation? These videos explain the concept well:
- [VOR Explained Simply by FlightInsight](https://youtu.be/uqGvbVDp5Jk) (recommended for beginners)
- [How to navigate using VOR by FlightInsight](https://www.youtube.com/watch?v=RTxW1VB_Qog)

<img width="240" height="320" alt="VOR RX" src="https://github.com/user-attachments/assets/1c6b37dd-68c2-4e7f-a530-de57f46c23f8" />

## Values

- **Status** (read): displays whether the app is actively searching for VOR data or idle. Status can be changed by pressing the **Start** or **Stop** button at the bottom of the interface.
- **VOR Band** (read): the typical range for VOR beacons
- **Decoder** (read): the status of the VOR decoder, either:
  - **Searching**: no VOR signal has been found yet
  - **Locked**: VOR signal is steady and valid data is being decoded
- **Course (OBS)** (write): Omni Bearing Selector - the heading the user wants to navigate to (target)
- **Received Radial** (read): the receiver's radial as seen from the VOR beacon (the bearing to reach the VOR)
- **Flag** (read): if the instrument is navigating **TO** or **FROM** the VOR. There's a dead zone where the instrument will display **---** and it is displayed when the user is within the dead band between the **TO** and **FROM** directions.
  - See the videos above to better understand this flag
- **Calibration** (write): this field allows manual compensation of the decoder algorithm, useful if you're using devices that might alter the phase of the received signals (like external filters or different firmwares).
- **Course Deviation Indicator** (read): this gauge shows how far off you are from the selected OBS. The center of the instrument is 0° meaning you're on the exact route, each tick to the left or right indicates a 5° offset from the selected course. Scale ranges from -10° to +10°.
- **LOG to SD Card** (write): allows the user to collect diagnostic information for manual processing (records the heading, obs, status, and timestamp)

## Usage

1. Tune the VOR frequency of the nearest airport (e.g: 115.800MHz for VRN airport)
   - If the correct frequency was tuned and the VOR is within range, you should hear the Morse identifier of the VOR every 10 seconds.
2. Set the OBS to the course you want to navigate (e.g: 050°)
3. Observe the received radial and navigate accordingly

## See also

- [VOR TX](VOR-TX) — transmit a programmable VOR signal