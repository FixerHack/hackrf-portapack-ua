

![SCR_0011](https://user-images.githubusercontent.com/13151053/229307637-792795d4-c403-46eb-a619-b06fff2f33d4.PNG)
![SCR_0013](https://user-images.githubusercontent.com/13151053/229307644-ea556a0c-094f-4e92-9ae3-ea606adf2cc2.PNG)


![Screenshot 2023-04-01 193341](https://user-images.githubusercontent.com/13151053/229307649-d243f926-20a4-4f12-aa40-cfdbf010d1ba.jpg)

The **SD Over USB** app exposes the SD card as a USB Mass Storage device, allowing a connected PC to read and write files directly — without physically removing the card.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

> [!NOTE]
> When SD Over USB is active, normal PortaPack operation is completely suspended. The device runs a dedicated USB Mass Storage firmware — no other apps or functions are available until the PortaPack is restarted.

## Usage

1. Connect the PortaPack to a PC via USB.
2. Open **SD Over USB** from the Utilities menu.
3. Press the **Run** button.
4. The screen clears and the HackRF icon appears on a black background — this indicates USB Mass Storage mode is active.
5. It can take **up to 20 seconds** for the drive to appear on the PC.
6. Use the SD card as you would any external drive — copy, delete, or modify files freely.

## Exiting USB Mass Storage mode

There is no exit button. To return to normal PortaPack operation, first **safely eject / unmount** the drive on your PC, then **power cycle the device**. On the H4M use the power switch; on older models (H1, H2) double-press the encoder knob to turn off, then press once to turn on.

> [!WARNING]
> Always unmount the drive on your PC before power cycling — failing to do so may cause filesystem corruption on the SD card.

## Performance

Transfer speed is approximately **400–500 KB/s**. This is a hardware limitation of the USB connection. For large file transfers, physically removing the SD card and using a card reader may be significantly faster.

For example, copying the 2 GB `world_map.bin` file to the SD card via SD Over USB can take up to 2 hours. Using a card reader directly is much faster.