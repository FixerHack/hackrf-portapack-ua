# My device wont start up

## White screen
If you device won't boot and leaves you on white screen, then you will need to power off the device and then holding the **UP** button while you power it on. This could take up to 10 seconds.

If this does not work, then try the same thing but this time holding the **DOWN** button (Remembering to wait up to 10 seconds).

What this is doing is loading a different LCD driver to get your devices screen to work.

Once that is done you should be able to reboot normally without any issues.

## Black screen
If you device won't boot and leaves you on a black screen, then you will need to power off the device and then hold down the **LEFT** button while you power it on. This could take up to 10 seconds.


# Description
* UP key = LCD driver 1
* DOWN key = LCD driver 2
* OK/SELECT key = Reset/Automatic detection
* LEFT key = LCD driver 2 QFP100 chip
* RIGHT key = LCD driver 1 QFP100 chip

> If you are having trouble understanding these procedures, here is a step-by-step instruction:  
>1. power off your device
>2. press and holding one of the buttons listed above. （**DO NOT RELEASE IT YET**）
>3. power on
>4. Wait for at least 10 seconds.
>5. if : you see the screen displaying any valid content*, release the button you have chosen.   
>else if : you still not seeing any valid content* displayed, choose another button and start again from step 1.
>6. power off, wait 5s, power on again **without** holding any buttons listed above, check if it boot successfully.  
>if : you see the screen display any valid content* : we are done.  
>else if : it boots successfully last round, but fail again this time : check the coin battery.

>p.s. ^valid content : either a splash screen or any of the interface

> [!NOTE]  
> H2+ usually require you to hold the **UP key** on the first boot to configure them.

_This is valid from nightly version **n_220412** and stable release version: **v1.5.1**_

## H2+ (and H1) not powering up, just black LCD (after flashing new Mayhem FW, and it is ignoring previous above key buttons init description):

If your device was working correctly before updating the firmware, and now you see a black screen after it's been flashed and it is ignoring the keyboard of the above instructions and looks like it's bricked (or also if the Mayhem menus appear but running any app causes an M0 guru fault indicating that the ROM may be partially flashed), then you have several options to try below depending the situation. Make sure the PortaPack is charged using a separate 5V USB power adapter (not connected to the PC).  After charging, connect the USB cable from your PC to the device and follow the steps below:

### (1) If your device is still detecting correctly the USB plug to your USB PC
(showing in the front of the HackRF board a green LED when plug in USB cable), then you are lucky; it means that your device is in “hackrf mode”, with good USB communication,
**then just follow the below process (I)**

### (2) If you have an H1 device (without integrated battery) that does not detect any USB communication
(usually no need to disassemble), try to set up it to DFU mode (by holding in the DFU button while turning on power or attaching the USB cable).  In DFU mode, the device will show up as an "NXP LPC" USB device.  While in DFU mode, execute the following command:

 `dfu-util --device 1fc9:000c --alt 0 --download hackrf_one_usb.dfu`

(Alternatively, run the `mayhem_flasher.bat` file and select flash DFU mode, which performs the command above.)

You will see from that point that the green USB LED from the Hackrf becomes active when the USB cable is connected, and the linux command lsusb should show a "Great Scott Gadgets HackRF One" device. If hackrf mode has been entered successfully, **then just follow the below process (I)**. 
If not, see more DFU information: [Update firmware troubleshooting](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Update-firmware-troubleshooting).

### (3) If you have an H2+ (with integrated battery) device that does not detect any USB communication,
first try the steps under (2) above.  If that does not work, then disassembling the HackRF from the PortaPack will be necessary to get the device into DFU mode.
In that case, Dissassemble carefully both boards from the metal case box.
Separate with maximum care to not bend / force so much the PCB's and the LCD Panel , both boards (Hackrf - Portapack) , It is a matter of patience , step by step from both connectors , trying to keep coplanarity of both boards ,
![image](https://user-images.githubusercontent.com/86470699/227355755-a0213c19-31e9-42d1-beb4-f58e04bad355.png)



(A) Once disassembled, pick up your hackrf board,
![image](https://user-images.githubusercontent.com/86470699/227356035-3dd044f0-dfb1-4bfe-b780-6c05fa038770.png)

 and connect it to USB.
 If it's not bricked, you will have a green LED when plugging USB (indicating HackRF mode is enabled). 
 if it is bricked you will need to enter DFU mode (by holding in the DFU button while turning on power or attaching the USB cable).
In DFU mode, the device will show up as an "NXP LPC" USB device. Execute the following command to get the device into HackRF mode:

 `dfu-util --device 1fc9:000c --alt 0 --download hackrf_one_usb.dfu`

(Alternatively, run the `mayhem_flasher.bat` file file and select flash DFU mode, which performs the command above.)

You will see from that point that the green USB LED from the Hackrf becomes active when the USB cable is connected, and the linux command lsusb should show a "Great Scott Gadgets HackRF One" device. If hackrf mode has been entered successfully, **then just follow the below process (I)**. 
If not, see more DFU information: [Update firmware troubleshooting](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Update-firmware-troubleshooting).


## Special Step process (I) to recover it (usually only needs to be done just once)

Assuming that you are here, with already in correct Hackrf mode (with green LED when connecting USB cable to the USB).  If you have already done the steps below in the past, you can skip to just flashing the firmware to the latest version using HackRF mode; see [Update firmware](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Update-firmware).

**In case that you have H2+ Portapack with big CPLD QFP100:**
     flash it with special fw jumbo77 1.43 first 

**In case that you have H1/H2+ Portapack with standard small CPLD QFP64:**
     flash it with official Mayhem fw 1.43 first 
     
If you came from case (3) above, assemble both boards again.

Then , 
(a) Confirm correct boot up of fw version 1.43 (special jumbo 1.4.3 for big CPLD QFP100, or official 1.4.3 for std CPLD QFP64)  

(b) From that 1.43 fw ,with correct boot, put the device in “hackRF mode” and flash it again, but now with latest Mayhem firmware.

(c) At first power up, keep pressing the appropriate button for your unit for more than 2 secs, until getting correct LCD display, and it should work all correctly ! 


## Explanation
Firmware starting at version 1.5.4 and onward contain the <a href="https://github.com/portapack-mayhem/mayhem-firmware/pull/662">Pull Request 662</a> that uses the persistent memory to test and store the hardware and LCD config settings . That memory uses the same back up voltage than the Real Time Clock calendar, both needs a healthy cell battery button voltage. Sometimes, in a re flashing process , although we got good battery cell button voltage, the unit seems to be badly initializing those persistent bytes and we got strange black screen. Doing those above steps probably reset the persistent memory. That's just a guess.

### Additional notes : 
I used to have many frequent “black LCD boot brick” when exchanging binaries compiled with different gcc-arm… version , from 9.4 to 10.3 or 12 . But thanks to @u–foka‘s PR fix pmem -> make backup_ram_t data members volatile [#1135](https://github.com/portapack-mayhem/mayhem-firmware/pull/1135), all those problems are gone , and now I do not have any persistent memory boot problems , so I do not need to go back to any old version 1.4.3 anymore. 


## H4 users
If you got any addon plugged in, try to remove it, and power off, wait a bit, and power on your device. If the addon board / module has problems, it can extremely slow down the boot, and the working. (usually happens when the I2C line goes wrong, and each operation have to wait for the timeout)

## HackRF does not boot with sd-card inserted.
When turning on the HackRF with the sd-card inserted, it does not fully boot into the Mayhem firmware and is stuck on the following screen: ![HackRF Stuck on boot](https://i.imgur.com/X5ECGuX.jpeg) 
When removing the sd-card, the HackRF does fully boot into the Mayhem firmware.

Try a persistent memory reset (SETTINGS, P.Mem Mgmt, reset, reboot device) and check if SETTINGS/SD Card is not having "enable high speed IO enabled". This will fix the problem.