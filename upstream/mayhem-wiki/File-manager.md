Used to manage files on the SD Card.

## Controls

- Use the encoder or up and down buttons to move between items.
- Use the select (center) key to enter a folder or to select an item to take an action on.
- Use the right button to select a folder to take an action on (e.g. rename a folder).
- Use the left button or select the ".." folder to go up a directory.
- Click on "-->" to get to next page, you will generally find it at the bottom of the list.
- Click on "<--" to get to previous page, you will generally find it at the top of the list.

A small, blinking arrow on the right indicates that there are more items if you scroll down.

Items with filenames longer than the display width will automatically scroll horizontally when highlighted.

## Pagination

When there are too many elements, the sorting is disabled (not enough memory to do it) but the pagination is turned on, allowing to view a lot more elements.

On pagination button lines and in place of the size, there will be a page number indicating to which page you will be going.

## File type handlers

Selecting certain types of files launches a viewer for the content. Use the right button to enter the toolbar for these file types. Exiting the viewer when launched this way will return back to Fileman.

- **BMP files** will open in the Splash viewer if located in the SPLASH folder (and can be set as the splash screen). BMP files in any other folder open in the BMP File Viewer.
- **TXT files** will open in Notepad. Exception: TXT files in the WATERFALLS folder open the waterfall copy dialog instead.
- **PPL, C8, CU8 and C16 files** will open in Replay in the correct mode.
- **PNG files** will open the Screenshot viewer (this can only view screenshots generated on the device). When viewing a screenshot, press any key to return back to Fileman.

## Buttons

![Tools_File manager](https://github.com/user-attachments/assets/81cb210f-34b6-49bc-8d38-c85892bd681a)

When an item has been selected, the following commands are available in the toolbar.

- **Rename** — rename the file or folder.
- **Timestamp Rename** — rename the file or folder with the date appended.
- **Cut** — add the selected file or folder to the clipboard to be moved (by using Paste).
- **Copy** — add the selected item to the clipboard to be copied.
- **Paste** — move/copy the content of the clipboard into the current folder.
- **New Folder** — create a new folder in the current folder.
- **New File** — create an empty file in the current folder.
- **Notepad** — open the file in the text editor.
- **Trim** — open a capture file in the IQ Trim app.
- **Delete** — delete the file or folder.
- **Clean** — erase all the files in the folder.
- **Show Hidden** — shows hidden files.
- **Exit** — exit the file manager.

## Partner files

Capture files (.C8, .CU8 or .C16) will have a "partner" .TXT file containing metadata. Renaming or deleting one of the pair will prompt the same action to be applied to the other.

## Known folders

- **/ (root)** — holds the current splash screen file (splash.bmp), and the folders below.

- **ADSB** — holds map and airline data for the ADSB RX app.

- **AIS** — holds data for the AIS app.

- **APPS** — holds external apps such as PacMan and Calculator (app version on SD card must exactly match firmware version or it cannot be executed).

- **APRS** — holds captures from the APRS app.

- **AUDIO** — holds captures from the Audio app.

- **BLERX** — holds captures from the BLE RX app.

- **BLETX** — holds packet files for the BLE TX app (.TXT format).

- **BMP** — holds `.BMP` images saved by the NOAA APT app (`noaa_YYYYMMDDHHMMSS.bmp`). This folder is created automatically by the app if it does not exist.

- **CAPTURES** — holds captures from the Capture app.

- **CVSFILES** — holds files for the CVS Spam app.

- **DEBUG** — holds debug dump files created from the Debug Dump app.

- **EPIRB** — holds files for the EPIRB RX and TX apps. EPIRB RX reads `FREQ.TXT` for the frequency selector. EPIRB TX reads `BEACONS.TXT` for beacon playback in file mode.

- **FIRMWARE** — recommended directory to store alternate Mayhem firmware images.

- **FREQMAN** — holds frequency list files for the Freqman, Scanner, Recon, and Looking Glass apps.

- **GPS** — holds data for the GPS Sim app.

- **HOPPER** — holds files for the Hopper app.

- **KEELOQKEYS** — holds the `MFCODES` key file for the KeeLoq TX and SubGhzD apps. `MFCODES` is a plain text file with one entry per line in the format `mf_name;key_hex;type` (e.g. `Superrollo;XXXXXXXXXXXXXXXX;1`). Without a matching entry, KeeLoq and Superrollo signals cannot be decrypted or retransmitted.

- **KEELOQREMOTES** — holds `.KEELOQ` remote files created by SubGhzD when saving a decoded KeeLoq or Superrollo signal. These files are loaded by the KeeLoq TX app for retransmission.

- **LOGS** — holds logs from various apps including ADSB RX, ERT, TPMS, POCSAG, Radiosonde, SubGhzD (`SUBGHZDLOG_*.CSV`), and SubCar (`SubCarLOG_*.CSV`).

- **LOOKINGGLASS** — holds preset frequency ranges for the Looking Glass app. All `.TXT` files in this folder are loaded automatically.

- **MACADDRESS** — holds MAC address files.

- **OOKFILES** — holds signal files for the OOK Editor app.

- **PLAYLIST** — holds playlist files (.PPL) for the Replay app.

- **REMOTES** — holds remote files for the Remote app.

- **SAMPLES** — holds example capture files.

- **SCREENSHOTS** — holds screenshots.

- **SECPLUS** — holds `.SECPLUS` remote files for the Security+ TX app.

- **SETTINGS** — holds saved App Settings (.ini files), PMEM_FILEFLAG and pmem_settings (only if persistent memory is being saved on the SD card), DATE_FILEFLAG (for incrementing pseudo-date only when coin cell battery is dead), and blacklist (list of apps to be disabled).

- **SPECTRUM** — holds files for the Spectrum Painter app.

- **SPLASH** — holds example splash screen files. To select a new splash screen, open a BMP file with FileMan and press the Right button to copy it to the root directory as your new splash.bmp file ("Show Splash" also needs to be enabled on the Settings → User Interface page).

  ![image](https://github.com/user-attachments/assets/bf09723e-3922-4b76-8d6f-f950f76f8b05)
  ![image](https://github.com/user-attachments/assets/15320f59-f8fb-4dcc-89f9-9b3faac50870)

- **SSTV** — holds images for the SSTV app.

- **SUBGHZ** — holds `.sub` signal files for the FlipperTX app.

- **TPMS** — holds log files from the TPMS RX app.

- **WATERFALLS** — holds preset files for the Waterfall Designer app. TXT files in this folder open the waterfall copy dialog instead of Notepad.

- **WAV** — holds WAV audio files for the Soundboard app.

- **WHIPCALC** — holds data for the Antenna Length calculator.

## Known Issues

- Items are listed unsorted after a fixed number of elements (hardware limitation, not enough memory to sort all the files).
- Copy & Paste does not work on folders. (Note that Cut & Paste *is* now supported on folders.)
- Folders must be empty in order to be deleted (use the Clean button to empty a folder first).
- Cut/Copy/Paste does not work with "partner" files.

Tip: Use the SD-over-USB utility for more advanced file and folder editing via an attached computer.