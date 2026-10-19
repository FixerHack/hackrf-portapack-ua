The **Wipe SD Card** app overwrites the FAT (File Allocation Table) region of the SD card with pseudo-random data, destroying the filesystem structure. This makes the card appear blank and unreadable without reformatting.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).


> [!WARNING]
> **This is not a secure data erasure tool.** Only the FAT area (~256 KB) is overwritten — the actual file data on the card remains physically intact and may be recoverable with data recovery software. Do not rely on this tool to securely destroy sensitive captures or recordings.

> [!WARNING]
> **After wiping, the SD card must be reformatted on a PC** before it can be used again. The PortaPack itself cannot reformat the card.

## What it does

When launched, a confirmation dialog appears:

> *"Wipe FAT of SD card?"*

Selecting **Yes** starts the wipe. The app writes 512 blocks of pseudo-random data (512 bytes each = 256 KB total) over the FAT base sectors of the filesystem. A progress bar is shown during the process. The app exits automatically when done.

Selecting **No** returns to the menu without making any changes.

## When to use it

This tool is useful when you want to quickly render the card's contents unnavigable — for example, to prevent casual browsing of captures and recordings. It is **not** suitable as a privacy or security measure if the data must not be recoverable.

## After wiping

The SD card will need to be reformatted (FAT32) on a computer before the PortaPack can use it again. See [[How-to-Format-SDCard]] for instructions.