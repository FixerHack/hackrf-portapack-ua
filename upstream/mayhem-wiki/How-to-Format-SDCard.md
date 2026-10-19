PortaPack NEEDS FAT32 or exFAT format for SDCard! Here's how you can format them with your PC.
# Linux
Usually all the Desktop Environment provide it's own GUI partition tool. for example GPartition or KDE Partition Manager. If you wanna use CLI way:
1. Identify the SD card device with `sudo fdisk -l`.

2. Unmount the SD card with `sudo umount /dev/sdX1`.

3. Format the SD card with `sudo mkfs.vfat -F 32 /dev/sdX1`.
   * if `mkfs.vfat: command not found` install dosfstools dependency (eg: `sudo pacman -S dosfstools`)

4. (Optional) Label the SD card with `sudo mkfs.vfat -F 32 -n "SDCARD" /dev/sdX1`.

5. Mount the SD card with `sudo mount /dev/sdX1 /mnt`.

# macOS
Just use Disk Utility app.

# Windows
- If your sdcard capacity is smaller or equal than/to 32G, just right-click the sdcard driver in Explorer
- If your sdcard capacity is greater than 32G, Download a free partition manager (for example Disk Genius) and format with it.

# I DON'T KNOW WHAT ARE Windows/Linux/macOS
Just follow the Windows chapter.