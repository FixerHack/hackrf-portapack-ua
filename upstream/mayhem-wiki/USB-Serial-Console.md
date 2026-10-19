The PortaPack Mayhem firmware exposes a serial console via USB when connected to a computer.

![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/1091420/2caf6ccf-0ee2-4bad-8a19-a140ee856c84)

![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/1091420/ca238acd-f09e-4153-a96a-36a48ff92428)

Any serial terminal client can be used to connect like PuTTY, minicom, screen, [HTerm](https://www.der-hammer.info/). There are even web based ones (Chrome&Edge, no Firefox): https://www.serialterminal.com/ or **https://hackrf.app/**

The terminal exposes the ChibiOS/RT Shell:

![grafik](https://github.com/portapack-mayhem/mayhem-firmware/assets/13151053/0642485a-ff13-4386-a1f4-4516d654d8dc)

You SHOULD NOT enter HackRF mode (AKA the mode with blue screen) when using the serial console, whether with PWA app (hackrf.app) or other serial tools. That saying, you need to keep your portapack on but in normal mode (instead of entering hackrf mode) to use it.

# Available Commands
* `help`: lists all available commands.
![grafik](https://github.com/user-attachments/assets/4ee7fe24-377b-4b0f-a70c-141d8dc816af)
* `exit`: shutdown the serial console
* `info`: shows the ChibiOS/RT system details.
* `systime`: shows the uptime in ms.
* `reboot`: reboots the PortaPack. This will also work on devices where the reset button is not working.
* `dfu`: reboots the PortaPack into DFU firmware upgrade mode.
* `hackrf`: Starts the original HackHF firmware to use the PortaPack as HackHF.
* `sd_over_usb`: Starts the [SD Over USB](SD-Over-USB) mode.
* `flash`: This is the [Flash Utility](Flash-Utility).
* `screenshot`: Takes a screenshot.

  ![grafik](https://github.com/portapack-mayhem/mayhem-firmware/assets/13151053/1c5278a9-3977-4bf7-8043-44cc524e8b83)
* `screenframe`: Replies with the screen's content. Format is 1 line / screen line, and for each pixel HEX (2 char) in the R,G,B order. So one line will be 720 + newline.
* `screenframeshort`: Replies with the screen's content. Format is 1 line / screen line, and for each pixel you'll get 1 character. Format is '00RRGGBB' + 32. So for black you'll get 32 (' '). For white 95 ('_').
* `write_memory`: manually write values at specific memory locations. Usage: ```write_memory <address> <value (1 or 4 bytes)>```
  ![grafik](https://github.com/portapack-mayhem/mayhem-firmware/assets/13151053/6d655d31-8de4-4c70-aa30-e0540583c236)
* `read_memory`: Reads memory at specific location. Usage: ```read_memory <address>``` 
* `button`: Simulates a button press
    * button 1: Right
    * button 2: Left
    * button 3: Down
    * button 4: Up
    * button 5: Select/Enter
    * button 6: DFU
    * button 7: Rotary Left
    * button 8: Rotary Right
* `touch`: Emulates touch event (press + release). Need to pass the x y coordinates of the event, and 0 < x < screen_width, 0 < y < screen_height must be met.
* `keyboard`: Emulates keypress event for the supported widgets. One parameter must be a string that has the HEX (2 char) representation of the desired key. You can send multiple characters at once. Backspace is 08. "Hello world" sent in one command: `keyboard 48656C6C6F20776F726C64`.
* `ls`: Lists files and directories.
* `unlink`: Deletes a file.
* `mkdir`: Creates a directory.
* `filesize`: Return the size of a specific file. 
* `fopen`: Opens a file for reading and modification.
> [!NOTE]
> The current position will be set to the end of the file. Use `fseek 0` to move to the start of the file.
* `fseek`: Sets the current position inside the currently opened file.
* `fclose`: Closes the currently opened file.
* `ftruncate`: Removes all content in the file behind the current position.
* `ftell`: Shows the current position is the file.
* `fread`: Reads n bytes from the currently opened file.
> [!TIP]
> there is a faster binary read option: `frb`
* `fwrite`: Writes bytes from the currently opened file.

 ![291070841-9e4ecef9-89bb-4a47-be0c-710384a84a22](https://github.com/portapack-mayhem/mayhem-firmware/assets/13151053/b7156f62-537a-4a7b-9d76-0c197992a040)
> [!TIP]
> there is a faster binary write option: `fwb`
* `crc32`: Get the CRC32 of a specific file.
* `rtcget`: Get the portapack current date and time.
* `rtcset`: Set the portapack current date and time. Usage: ```rtcset [year] [month] [day] [hour] [minute] [second]```. All fields are required, milliseconds are reset when the function is called (fractional seconds are not supported)
* `cpld_info`: Display information about the CPLD. Usage: ```cpld_info <device>```. Device should be 'hackrf' or 'portapack'
* `cpld_read`: Read the CPLD. Usage: ```cpld_read <device> <target>```. Device can be: hackrf, portapack. Target can be: sram (hackrf only), eeprom.
* `cpld_write`: Write the CPLD. Usage: ```cpld_write <device> <target> <file>```. Device can be: hackrf, portapack. Target can be: sram (hackrf only), eeprom. Currently only "cpld_write portapack eeprom <file>" is supported.
* `accessibility_readall`: return a textual list of all widget on screen. The item with focus will have it's type end with a '*', like in ```[NewButton*] Receive```.
* `accessibility_readcurr`: return a textual description of the focused widget only.
* `applist`: Shows the apps that can be started with `appstart` command. You'll get 3 parameters per line: app short name (you'll need to use this with appstart), app's full name, and app category.
* `appstart`: You can start apps from the list given by the `applist` command. 1 paremeter needed, the app's short name. It'll stop any running apps.
* `gotgps`: You can send apps your current position. Format `gotgps lat lon <alt> <speed> <satinuse>`. Lat, lon is mandantory with '.' as a decimal separator.
* `gotorientation`: You can send apps your current orientation. Format `gotorientation angle`. Send only integer, where 0 mean North, 90 East, 400 mean 'not set'.
* `gotenv`: Set environnement sensors value. Usage: ```gotenv <temperature> [humidity] [pressure] [light]```
* `gotlight`: Set environnement light value. Usage: ```gotlight <light_lux>```
* `pmemreset`: Sets all values in PMEM to default. Pass the "yes" as a parameter, that indicates you know what are you doing.
* `sysinfo`: show system hardware informations.
```
ch>sysinfo
M0 heap: 32400
M0 stack: 407
M0 cpu%: 0
M4 heap: 0
M4 stack: 0
M0 cpu%: 0
M4 miss: 0
uptime: 15
ch>
```
* `radioinfo`: show radio settings.
```
ch>radioinfo
receiver_model.target_frequency: 1090000000
receiver_model.baseband_bandwidth: 1750000
receiver_model.sampling_rate: 3072000
receiver_model.modulation: 1
receiver_model.am_configuration: 0
receiver_model.nbfm_configuration: 0
receiver_model.wfm_configuration: 0
transmitter_model.target_frequency: 1090000000
transmitter_model.baseband_bandwidth: 1750000
transmitter_model.sampling_rate: 3072000
ch>
```
* `settingsreset`: Deletes all INI files from settings folder, resetting app settings. Pass the "yes" as a parameter, that indicates you know what are you doing.
* `sendpocsag`: Opens the Pocsag TX app, and sends a message defined in the command.
```
Usage: sendpocsag <addr> <msglen> [baud] [type] [function] [phase] 
addr: 0 or the destination address
msglen: 0, max is 80
baud: 512, 1200 or 2400
type: 0 (ADDRESS_ONLY) 1 (NUMERIC_ONLY) 2 (ALPHANUMERIC)
function: A, B, C or D
phase: P or N
```
After you send this message, there will be a prompt `send <mgslen> bytes`. then you need to send JUST that amount of bytes that will be the message. If msglen is 0, the TX is direct and without a message.
The Pocsag TX app will start, set the desired options, and send the message. 

* `asyncmsg`: turn on of off the asynchronous debug message logging. Usage: ```asyncmsg <status>```. Status can be 'enable' or 'disable'.

* `setfreq`: Set the radio frequency. Parameter: target frequency in HZ. Only works in the following RX apps: Audio, Capture, ERT, Pocsag, APRS, Level, Looking Glass, Sonde, SubGHZd, Weather. Not supported in other apps that are using frequency range, or automatically set / hopping frequencies.
