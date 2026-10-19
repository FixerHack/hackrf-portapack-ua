If the SD card is not recognized by your PC after starting [[SD-Over-USB|SD Over USB]], the cause is usually a wrong or missing USB driver on Windows, or simply not waiting long enough for the drive to appear.

## First: wait up to 20 seconds

After pressing **Run** in the SD Over USB app, it can take **up to 20 seconds** for the drive to appear on the PC. Wait before assuming something is wrong.

## Windows: wrong driver assigned

Windows sometimes assigns the HackRF's USB serial driver instead of the USB Mass Storage driver when the device switches modes. To fix this:

1. Open **Device Manager** (right-click the Start button → Device Manager).
2. Under **Universal Serial Bus devices** or **Other devices**, find the HackRF One entry.
3. Right-click it and select **Update driver**.
4. Select **Browse my computer for drivers**.
5. Select **Let me pick from a list of available drivers on my computer**.
6. Select **USB Mass Storage Device** from the list.
7. Click **Next** and confirm.

The SD card should now appear as a removable drive in File Explorer.

> [!NOTE]
> You may need to repeat this step after rebooting or reconnecting the device, as Windows may revert to the previous driver assignment.

## Linux and macOS

On Linux and macOS, USB Mass Storage is handled natively by the kernel and no driver installation is needed. If the drive does not appear, check that the SD card is properly inserted in the PortaPack and is not corrupted. If the SD card has filesystem errors, the host OS may fail to mount it — try formatting the card as FAT32 and restoring the SD card contents from a fresh release package.

## General checks

- Make sure the SD card is inserted in the PortaPack before starting the app.
- Use a USB cable that supports data transfer, not a charge-only cable.
- Try a different USB port, preferably directly on the PC rather than through a hub.
- If the drive appears but shows errors, the SD card filesystem may be corrupted — see [[How-to-Format-SDCard]].