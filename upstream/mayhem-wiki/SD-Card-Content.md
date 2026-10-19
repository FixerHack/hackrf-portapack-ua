# SD Card Content in Portapack Mayhem

The **SD card** is an essential component of the **Portapack Mayhem** firmware, extending the capabilities of the device by providing additional storage for files, configurations, and user-generated data. While the Portapack itself contains built-in functionality, many features rely on an SD card to function optimally.

## Key Uses of the SD Card

- **Records** – Custom **IQ recordings** and pre-generated waveforms for replay attacks or signal analysis.
- **External Apps** – Applications stored in the `APPS` directory of the SD card.
- **Configuration Files** – User preferences, profiles, and settings that persist across sessions.
- **Firmware Updates** – Bootloader and firmware upgrade files stored and loaded from the SD card.
- **Captured Data** – Logs, frequency sweeps, and captured transmissions saved for later analysis.

## File System & Organization

- The SD card should be formatted in **FAT32** or **exFAT**.
- Specific folders and naming conventions are required for certain features.
- Maintaining a well-structured file hierarchy ensures seamless operation.
- Proper management of SD card content unlocks the full potential of the Portapack Mayhem firmware, enabling advanced signal processing, automation, and enhanced usability in the field.
- The SD card provides a flexible storage resource that can be tailored to the user's needs.

# Downloading and Installing SD Card Files for Portapack Mayhem

To fully utilize the Portapack Mayhem firmware, you need to prepare your SD card with the necessary files.

You can refer to the quick procedure below to know where to download the required content and how to install it properly, or have a look at the detailed SD card content update in the [Update firmware](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Update-firmware#update-sdcard-file) article.

The standard SD card image is provided as part of the firmware download in the assets list of [each release](https://github.com/portapack-mayhem/mayhem-firmware/releases).

## Procedure

1. Navigate to the [releases page](https://github.com/portapack-mayhem/mayhem-firmware/releases).
2. Select the version you want (nightly or stable).
3. Under assets, find the two files ending with `...COPY_TO_SDCARD.zip` and `...COPY_TO_SDCARD-no-world-map.zip`.
4. Download the appropriate file:
   - If you have already installed the SD card content once, you do not need the larger version containing the ADS-B world map.
5. Extract the contents of the ZIP **to the root of the SD card**.

The data structure **at the root of your SD card** must match the following example:

![image](https://github.com/user-attachments/assets/fa5a79b5-6083-42a5-8ad2-7ab1ebd8d515)

> [!IMPORTANT]
> The ZIP file **must** be extracted.

> [!IMPORTANT]
> The directories shown in the screenshot **must be at the root of your SD card**.

# SD Card Details

## SD Card Contents

The following folders on the SD card store various app-specific data. Some of these folders are included in the SD card image, while others may be created later by the firmware or the user:

- **ADSB** – Contains databases for airlines and ICAO. The world map is also stored here. See the documentation for generating a custom map.
- **AIS** – Stores the AIS database.
- **APPS** – Stores external applications (`.ppma` files) offloaded from the firmware flash ROM.
- **APRS** – Logs from the APRS RX app.
- **AUDIO** – WAV audio recordings from the Audio app.
- **BLERX** – Captures from the BLE RX app.
- **BLETX** – Packet files for the BLE TX app (`.TXT` format).
- **BMP** – BMP images saved by the NOAA APT app. Created automatically by the app on first use.
- **CAPTURES** – IQ capture files (`.C16`, `.C8`, `.CU8`, and metadata `.TXT`) from the Capture app.
- **CVSFILES** – Files for the CVS Spam app.
- **DEBUG** – Debug dump files created from the Debug Dump app.
- **EPIRB** – Files for the EPIRB RX and TX apps. EPIRB RX reads `FREQ.TXT` for the frequency selector. EPIRB TX reads `BEACONS.TXT` for beacon playback in file mode.
- **FIRMWARE** – Contains `.bin` files used to update the PortaPack firmware.
- **FREQMAN** – Stores frequency database files for loading in various apps.
- **GPS** – Stores information for generating GPS simulation files.
- **HOPPER** – Files for the Hopper app.
- **KEELOQKEYS** – Holds the `MFCODES` key file for the KeeLoq TX and SubGhzD apps. `MFCODES` is a plain text file with one entry per line in the format `mf_name;key_hex;type`. Without a matching entry, KeeLoq and Superrollo signals cannot be decrypted or retransmitted.
- **KEELOQREMOTES** – Holds `.KEELOQ` remote files created by SubGhzD when saving a decoded KeeLoq or Superrollo signal. These files are loaded by the KeeLoq TX app for retransmission.
- **LOGS** – Logs from various apps including ADSB RX, ERT, TPMS, POCSAG, Radiosonde, SubGhzD (`SUBGHZDLOG_*.CSV`), and SubCar (`SubCarLOG_*.CSV`).
- **LOOKINGGLASS** – Holds preset frequency ranges for the Looking Glass app. All `.TXT` files in this folder are loaded automatically.
- **MACADDRESS** – Holds MAC address files.
- **OOKFILES** – Signal files for the OOK Editor app.
- **PLAYLIST** – Stores `.PPL` playlist files for the Replay app.
- **REMOTES** – Stores remote files for the Remote app.
- **SAMPLES** – Contains example capture files.
- **SCREENSHOTS** – Stores screenshot files.
- **SECPLUS** – Holds `.SECPLUS` remote files for the Security+ TX app.
- **SETTINGS** – Stores application settings (`.ini` files). If an app malfunctions, deleting its settings file resets it. A blacklist file for disabling apps may also be stored here.
- **SPECTRUM** – Stores `.BMP` images for the Spectrum Painter app.
- **SPLASH** – Stores custom splash screen `.BMP` files (active splash screens must be in the root directory as `splash.bmp`).
- **SSTV** – Contains images for the SSTV app.
- **SUBGHZ** – Holds `.sub` signal files for the FlipperTX app.
- **TPMS** – Holds log files from the TPMS RX app.
- **WATERFALLS** – Holds preset files for the Waterfall Designer app.
- **WAV** – Stores sound files for the Soundboard app.
- **WHIPCALC** – Stores whip length calculation data. Additional whips can be added with specific details.

SD card contents can be managed using the File Manager application, the "SD over USB" app, or by removing the SD card and accessing it via a computer.

> [!WARNING]
> Improper reinsertion may cause the SD card to fall into the device, requiring disassembly to retrieve it.

## Technical Details

- Detailed technical specifications are available [here](https://github.com/portapack-mayhem/mayhem-firmware/wiki/SD-Card-(DEV)).

> [!WARNING]
> The File Manager app has a memory limitation: an "out of memory" error may occur if a folder contains too many files.