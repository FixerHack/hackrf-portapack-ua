![image](https://github.com/user-attachments/assets/90050229-4aab-4fa6-a69f-af23de4c52d6)

# Important

**This App Does not work as a general-purpose AFSK decoder.** The app is hardcoded at startup to the modem settings and default frequency of the [LCR/TEDI](LCR) app (467.225 MHz, Bell 202, 7-bit Even parity, LSB first). This means it produces a constant stream of random characters on any other frequency or signal type. For LCR reception use the dedicated [LCR/TEDI](LCR) app instead.

This is an [external app](External-apps-informations) and must be present on the SD card in the `APPS/` folder.

## Context

AFSK stands for **A**udio **F**requency-**S**hift **K**eying, and is a protocol for encoding digital information into audio for transmission over radio frequencies. Its use exists within many technologies, including in a few apps in the mayhem-firmware such as [APRS-RX](APRS-RX).

This app was (until now) poorly documented and has remained in _beta_ for a significant amount of time, relegating it to an external app to free up space in the core firmware. It is believed by most to not work at all, and some to not work as well as it should.

### Main Page

The top bar of the main page of the app has configurable items that are common to many other apps, including frequency selector, AMP, LNA, VGA, and Volume. It also has a toggle for outputting data to a log file writing to `AFSK.TXT` in the logs directory, as well as [Modem Setup](#Modem-Setup).

Finally, it has a section labelled as Debug. Here the user is presented with an ever-scrolling dump of what may appear to be random characters, but are the applications attempt to decode audio frequencies into textual output using UTF8 <sup>[1](#1)</sup>.

Each time the app processes a new message <sup>[2](#2)</sup> it will change the colour of this output cycling through `Red`, `Blue`, `Green`, and then `Light Blue`. In the log file, these are simply split by new lines.
 
### Modem Setup

This page allows for the selection of a number of presets for processing AFSK
1. Bell202
2. Bell103
3. V21
4. V23 M1
5. V23 M2

These can be selected by scrolling the selection wheel to the desired option, and then pressing the SET button. It is also possible to manually set the `Baudrate`, `Mark`, `Space`, `Repeat`, and `Serial Format`. Once the user has the desired settings selected, pressing the `Save` button at the bottom of the screen will bring them back to the [Main Page](#Main-Page). Note: due to the hardcoded startup configuration, modem settings changed here do not take effect correctly.


<sub><a name="1"></a>[1] At least, I think it's UTF-8. The printed characters of UTF-8 line up with the values that the C++ code is reading and declaring as a printed character, but at time of writing I am not familiar enough with C++ to know if it would be UTF-8 or another encoding type that has an overlap with UTF-8 such as windows 1252/latin1/etc. </sub>

<sub><a name="2"></a>[2] This is based on the code attempting to decode the audio into a byte(s) value between `DEC 32`/`HEX 0x20`/`UTF-8 (SPACE)` and `DEC 126`/`HEX 0x7e`/`UTF-8 ~(TILDE)`, and printing out the corresponding UTF-8 character. Any values outside of this range (with exception to below) are placed between square brackets and printed in their HEX form. </sub>

<sub><a name="3"></a>[3] If the decoded value is `DEC 127`/`HEX 0x7f`/`UTF-8(Control Character)` then this is treated as the end of a message, changing the colour of the text where displayed on the main page, or breaking onto a new line in the log file.</sub>