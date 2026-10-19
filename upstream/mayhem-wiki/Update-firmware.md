## Common workflow
> Note: The TLDR guide is for experts. Please try to read the full guide before asking in the community, if you are having trouble understanding the TLDR guide.

1. Update your SD card content 
2. Connect USB cable
3. Use **ONE OF** the following methods:
    * (Method1) Enter HackRF mode, flash with hackrf_spiflash
    * (Method2) Stay in Mayhem mode, use [hackrf.app](https://hackrf.app/) website 
    * (Method3) Copy firmware all in one tar package into SD card, and offline update with Flash Utility app in portapack 
        * (Method3-1) Use the filename that ends with `.bin` => only update flash
        * (Method3-2) Use the filename that ends with `.ppfw.tar` => update both flash and external SD card apps
        * The `.bin` is useful when you need to make a first flash or a recovery flash because you lost mayhem. If possible, you always want to update using the `.ppfw.tar`



```
citations:
- method 2 and 3 would automatically update external apps too;
- you don't have to update the entire sdcard content everytime, however it is recommended to do so, since every update mostly have new sdcard content;
- YOU WILL NEED A WORKING DEVICE WITH MAYHEM FIRMWARE TO USE METHOD 2 and 3.
```

### Detailed video guide

If you prefer watching a video guide, check [this](https://www.youtube.com/watch?v=qM7Q9IidK2o).

# Detailed Firmware Update procedures

## Using firmware file from github release page and the [Flash Utility](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Flash-Utility)

- Get the latest firmware from the [![GitHub release (latest by date)](https://img.shields.io/github/v/release/portapack-mayhem/mayhem-firmware?label=Releases&style=social)](https://github.com/portapack-mayhem/mayhem-firmware/releases/latest) page 

- Copy it to your SDCARD, put it back in your PortaPack 
- Flash it via the [Flash Utility](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Flash-Utility) in "Utilities" menu on your PortaPack
> [!Note] 
>- If you don't see the Flash Utility app, try using other methods to update to latest version
>- The [Flash Utility](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Flash-Utility) can also be used to program new firmware from a bin file stored on a MicroSD card 

## Using firmware file from github release page and the classic hackrf_spiflash tool
> [!Note]
> :warning: Using that method, you NEED to update the SDCARD content accordingly to the release you choose, else the external apps will not work !

### Windows
1. Connect the device via USB.
2. Switch to HackRF mode via the on-screen option. (In the PortaPack)
3. Double click `mayhem_flasher.bat` and follow the instructions.
4. Reboot the device.

### Linux
1. Connect the device via USB
2. Switch to HackRF mode via the on-screen option. (In the PortaPack)
3. Upload the firmware with `hackrf_spiflash -w new_firmware_file.bin` (eg. portapack-h1_h2-mayhem.bin for mayhem firmware or hackrf_one_usb.bin for stock HackRF firmware)
4. Reboot the device
> [!NOTE] 
>- To Ubuntu and Mint user: Ubuntu based distro never maintains their repo for HackRF host (cli client) package. You’ll face a lot of weird problems if your HackRF is R9. To resolve these, please compile the HackRF package yourself, or use another distro.

### MacOS
1. If necessary, install the HackRF tools: `brew install hackrf`
2. Connect the device via USB
3. Switch to HackRF mode via the on-screen option (in the PortaPack)
4. Upload the firmware with `hackrf_spiflash -w new_firmware_file.bin` 
5. Reboot the device

### Update SDCARD files
You need to provide a MicroSD with enough space, 16g is good enough unless you have a bunch of record file. This is necessary for certain functionality, like the world map, GPS simulator, external apps, and others. 

Get the latest files from the [![GitHub release (latest by date)](https://img.shields.io/github/v/release/portapack-mayhem/mayhem-firmware?label=Releases&style=social)](https://github.com/portapack-mayhem/mayhem-firmware/releases/latest) page. You need to uncompress (using [7-zip](https://www.7-zip.org/download.html)) the files from `mayhem_vX.Y.Z_COPY_TO_SDCARD.7z` to a FAT32 formatted MicroSD card. 

> [!NOTE] 
> How to put into SD card?  
> Extract the root directory of the 7z archive into the root directory of your SD card. 
>  - Don't put the 7z archive file directly into your SD card.
>  - Don't extract into any sub-folder of SD card.
>  - Don't use unbranded SD card.  
> ![Screenshot_20240121_101958](https://github.com/portapack-mayhem/mayhem-firmware/assets/24917424/e14a2ef7-37bd-4a00-b19f-101235093e01)

### Details about the SD card contents
Please go and read the [SD card Content](https://github.com/portapack-mayhem/mayhem-firmware/wiki/SD-Card-Content) article.

## Using the hackrf.app website
- You need to use a browser compatible with Web USB Serial
- The update using the website is only updating the firmware and external apps on the sdcard. If you want/need a full sdcard content update, please follow first the [Update SDCARD files](#update-sdcard-files) article, then update using the website

### Procedure
- Connect portapack using an USB cable with DATA enabled
- Navigate to https://hackrf.app/
- If never done, click on "Connect Device"

![image](https://github.com/user-attachments/assets/8d1d333d-a6b4-4651-867a-03e06a849b70)

- On the little pop up, select your Portapack, click 'Connect'

![IMG_20241118_103143](https://github.com/user-attachments/assets/a08f5499-d0d2-404d-b442-246bc3de6757)

- You should see "HackRF Connected" on top of the page, and the Live Screen will load the first screenshot
- Scroll down to "Manage Firmware", and click it

![image](https://github.com/user-attachments/assets/56a62da3-ce63-4eb6-83a2-00fe8069fcde)

- Choose the firmware version to install (stable, nightly, or from a custom ppfw file)

![image](https://github.com/user-attachments/assets/f761d1e5-65c5-4869-a0ad-15cb97626c4d)

- Wait for the file to be uploaded, and for your device to automatically reboot
- Done !

# Troubleshooting

- Please check [this guide](Update-firmware-troubleshooting)
- External apps (.ppma files in the APPS folder) will only function if their version matches the firmware version
- Please check the [FAQ](https://github.com/portapack-mayhem/mayhem-firmware#frequently-asked-questions)
- If your fimware version is lower or equal to v2.0.0 or nightly n_240114, you can only update firmware in HackRF mode with classic procedure
- Updating using the hackrf.app website is only working for stable version bigger or equal to v2.0.1, nightly version newer than n_240114
- When downgrading, please make sure SD card content versions match.
- Mayhem firmware contains HackRF firmware. You DO NOT need to flash HackRF firmware.
- In theory, it is impossible to brick the device, since you can always try the DFU recovery procedure. However, the updating might become fiddly in certain conditions. So you probably need basic computer usage knowledge (running/installing software, read documents, knowing USB ports, adjust system settings, reading English, etc.) if you don't, you probably should ask your friends or someone who knows these things to do it for you.