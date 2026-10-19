![image](https://github.com/user-attachments/assets/2f10ba8b-c085-4085-b5fc-8cbc7dcdf8d8)

> [!WARNING]
> Transmitting signals that trigger retail store assistance systems without authorisation may be illegal in your jurisdiction. Use only for research on systems you own or have explicit permission to test.

CVS Spam replays pre-recorded IQ capture files to trigger wireless customer assistance call buttons, as found in retail environments (CVS Pharmacy and similar). It operates as a raw IQ replay transmitter — it does not generate signals in software, but plays back `.c16` or `.cu8` capture files from the SD card.

The transmit frequency is fixed at **433.920 MHz** and cannot be changed from the UI.

App credit: RocketGod ([@rocketgod-git](https://github.com/rocketgod-git)). Original capture files: [@jimilinuxguy](https://github.com/jimilinuxguy/customer-assistance-buttons-sdr).

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# SD Card Setup

Place `.c16` or `.cu8` IQ capture files in the `CVSFILES/` directory on the SD card. The app lists all files found there. Up to 50 files are shown per page.

If the directory is empty or no supported files are found, the app displays `Empty directory!`.

# Controls

* **File list**: Scroll through available capture files. The currently highlighted file is the one that will be transmitted with **CALL**.
* **`<` / `>`**: Navigate between pages when more than 50 files are present.
* **CALL**: Transmits the currently selected file once, then stops. Selecting the same file while transmitting stops the transmission immediately.
* **CHAOS**: Starts continuous random playback — after each file finishes, a new file is chosen using an LFSR pseudo-random sequence and transmitted after a 100 ms pause. Pressing **CHAOS** again while active stops playback.
* **STOP**: Stops any active transmission immediately.

# Transmission Parameters

These values are set by the app and cannot be adjusted from the UI:

| Parameter | Value |
|-----------|-------|
| Frequency | 433.920 MHz |
| Sample rate | 250,000 Hz |
| RF Amp | Enabled |
| TX Gain | 47 |
| Bandwidth | 1,750,000 Hz |

# Progress Bar

The red progress bar updates continuously during playback to show approximate progress through the current file.