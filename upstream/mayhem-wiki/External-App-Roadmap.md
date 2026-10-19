# Untitled

# Overview

More apps need to be moved from internal to external to make room for new features in the flash ROM.  Considerations regarding exactly *which* apps should be moved from internal to external include the following:

1. Some apps should remain internal for better user experience (screens with fewer menu icons, and warnings about missing apps, are not the best look at first power-on).
2. Some core apps should remain internal for functional reasons, including the capability to install the external apps on the SD card (including the Flash Utility, SD-over-USB, and some Settings apps).
3. Some apps require the SD card to be installed and often to contain specific data files (such as map data or C8/C16 files) so it may make sense to move the app itself to the SD card too; no loss of functionality.
4. External app code is loaded into RAM (like the baseband M4 code), so will have less free RAM space available to operate, so apps that require more memory (including those that allocate lots of memory or use File Manager to select files) should *not* be moved to external.
5. Running code from RAM, external apps may have slightly better performance than internal apps that run from ROM (although they will still make many calls into the ROM code).
6. We also need to devise a way to sort the apps on the screen by the user and for consistency, since the external apps are currently at the end of the list and their position in the menu is *randomly* determined by their position in the FAT directory.

‍

# Legend

✅: Fully

✔️: Partial

🚫: Not at all

# Apps Currently in SPI Flash

(THE TABLES BELOW ARE VERY INCOMPLETE)
|Catalog|App Name|Can work without sdcard?|Can work without correctly put sdcard content?|Importance|Current Suggest|
| ---------| ----------------------------------------| ---------------------| ---------------------| -------------| ---------------------|
|Home|Capture|🚫|✅|✅ Core app|Stay in SPI flash|
|/|Replay|🚫|✅|✅ Core app|Stay in SPI flash|
|/|Remote|🚫|✅|||
|/|Scanner|✅|✅|||
|/|Microphone|✅|✅|✅ Core app|Stay in SPI flash<br />|
|/|Looking Glass|✅|✅|✅ Core app|Stay in SPI flash<br />|
|Receive|ADS-B|✔️|✔️|||
|/|AIS Boats|✅|✅|||
|/|APRS|✅|✅|||
|/|Audio|✔️|✅|✅ Core app|Stay in SPI flash|
|/|BLE Rx|✔️|✅|||
|/|ERT Meter|✅|✅|||
|/|Level|✅|✅|||
|/|POCSAG|✅|✅|||
|/|Radiosnde|✅|✔️|||
|/|Recon|✅|✔️|||
|/|Search|||||
|/|TPMS|✅|✅|||
|/|Weather|✅|✅|||
|/|SubGhzD|✅|✅|||

# Apps Currently in sdcard

|Catalog|App Name|Can work without sdcard if moved to SPI flash?|Can work without correctly put sdcard content if moved to SPI flash?|Importance|Current Suggest|
| ------------------------| ---------------------| ------------------------------------------------| ----------------------------------------------------------------------| -----------------| -------------------------------|
|Receive|AFSK||||Stay in sdcard|
|Utilities|Pac-Man|✅|✅|Game|Stay in sdcard|
|Transmit|GPSSim|🚫|🚫||Stay in sdcard|
