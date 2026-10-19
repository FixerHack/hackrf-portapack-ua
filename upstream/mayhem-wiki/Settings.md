This section provides a set of utilities that can be used to configure some aspects of the PortaPack and are described below. Settings are saved in persistent memory.

## AppManager
Allow you to hide/unhide application, and set/unset the autostart application.

![image](https://github.com/user-attachments/assets/d176fcb9-976e-4b4a-b934-a3cd734831ee)

## App Settings
Settings for each app are saved in corresponding .ini files in the /SETTINGS folder to maintain persistence, if a formatted SD card is installed. An updated .ini file is saved whenever the app is closed. To reset an app to default settings, the corresponding .ini file may be safely deleted and a new file will be created automatically when the app is subsequently executed. Alternatively, individual lines in the file may be deleted to reset only a subset of application settings. For debug purposes, note that some additional configuration settings may be found in the .ini file that are not configurable in the app itself.

![SCR_0043](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/45f0ac0b-d822-44f8-a643-9cf54c017c84)
![SCR_0046](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/06c05ef9-d599-49c0-8c7c-9afd2a1c4a70)
![SCR_0048](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/e101d06c-7f5e-4112-a635-cbbf8c6d9bea)

### Blacklist
To disable specific apps completely, a text file named "blacklist" can be created manually in the SETTINGS folder using the Notepad application.
Unwanted applications should be listed in this file using their case-sensitive application name (text that appears under the app's screen icon), and they will be disabled (hidden) effective on the next boot.
List one application per line. (Requires 1.8.0+ firmware and an SD card)

![SCR_0044](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/9687c092-6c7d-42bd-b075-bb81b3871245)
![SCR_0045](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/876df1ef-2faa-4051-9e8c-475337b584b4)

## Audio
This setting allows adjustment of the following audio parameters:

* Tone Key (CTCSS) mixer setting when transmitting in Soundboard or Mic apps, as a percent of the audio level (range: 10–99%).
* Audio Beep on speaker/headphone in certain apps when receiving a data packet (not all apps support this).

![SCR_0092](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/9ba259a4-ed18-4083-8c04-ec96fa7edda7)

## Battery
This settings only affect how the battery status will be displayed, it won't affect the charging behavior.
The Battery menu is only shown when a battery management IC is detected (e.g. on H4M and devices with compatible hardware).

In this menu, you can choose the battery calculation method or reset values.

Override:
- checked = voltage based
- unchecked = ic based

In newer firmware versions, there is also the checkbox 'Charge hint', which shows a blue battery icon at the top menu bar, if the battery is charging.
- checked = show blue battery icon on top, while charging
- unchecked = don't show extra indicator while charging

The IC 'learns' when the battery is full or empty and provides the % based on the former charging cycles. If the value is unreasonable or the battery is replaced, use the 'Reset' button. This will set the history to 0 and let the IC start to learn again.

<img width="240" height="320" alt="SCR_0006" src="https://github.com/user-attachments/assets/8c3101ba-e7d2-4a03-a4c8-5bec3db06b40" />

## Button Speed

<img width="240" height="320" alt="SCR_0007" src="https://github.com/user-attachments/assets/85467b55-3367-4aa9-b9e6-8fd07076d2be" />

Adjusts the response time when a button is held down. Three options can each be set to Normal or Fast:
* Repeat delay — how long before a held button starts repeating
* Repeat speed — how quickly the held button repeats
* Long press delay — how long a button must be held to trigger a long-press action

## Calibration
![SCR_0036](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/8ffcbfde-6261-4d64-a1ce-5704f8f8b741)

This provides an app for the calibration of the touch screen and alignment by following on screen instruction.

You have to keep pressed for at least a second on each target for the app to guess the touch area correctly and show next target on release.


## Config Mode
In some cases a PortaPack may start up intermittently in Config Menu mode, such as when the power button is pressed twice rapidly, or if a little electrical noise occurs when a USB cable is attached. If this occurs frequently (dark screen and blinking LEDs), the Config Menu code can be disabled using the Settings -> Config Mode app (which sets a flag in persistent memory to disable Config Menu activation).

![SCR_0037](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/28b4fd52-ec77-4f14-9b56-300ef2ce75c1)

## Converter
Set up convert or down convert mode.

![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/3157857/d64cb3b2-a9f1-4f1d-bde8-9cab3f0c8b34)

Widgets:
 * show / hide icon, hiding will also disable any up / down conversion
 * enable / disable converter
 * (+) or (-) set the offset sign
 * set the offset

When using an upconverter it's common to use an offset to access the correct frequency. As an example, if you want to use a HamItUp which is designed to listen from 60KHz to 30MHz, you'll need to tune your PortaPack to 125 MHz (or any other frequency used in the upconverter local oscillator) + the frequency you need.

Doing the calculation and tuning while adding the frequencies can be a bit tedious. Don't worry: just got into your PortaPack's settings, Radio menu, and set the shifting you need. You can set up conversion (+) or down conversion (-) in the Settings/Converter menu.

When the option is on, the displayed frequency is the one you want to tune in, and the real tuned frequency is displayed frequency plus or minus offset.
When the option is off, the displayed frequency is the one you want to tune in, and the real tuned frequency is the displayed frequency.

You can turn it on and off using the checkbox while in Radio menu, or using the top bar icon 'Freq', with an arrow telling you if it's up or down conversion.

Note: This has the same effect as using the top bar 'Freq' icon. While in the radio menu, the synchronization of the top bar 'Freq' status and the checkbox is not implemented when toggling the top bar 'up' icon. The status is saved, and the last to talk is setting the status.

## Date/Time
Set the date and time which will appear on the home screen (if enabled), in log entries, and file time stamps. A coin cell is required to keep the time updated when the PortaPack is off. If the coin cell battery is dead/missing but there is an SD card, the date will be advanced by 1 day every time the Portapack is rebooted, so that log entries/files will be in chronologically ascending order.

![SCR_0034](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/22e1660a-ef1e-429b-af6d-81a8f612b893)

If Daylight Savings Time (DST) is enabled, the time is advanced by one hour during the indicated date range specified as the Nth Day-of-Week in Nth Month (note that the time displayed on this screen is assumed to already be corrected for DST so the time entered should be the same as appears on other clocks). To learn the Daylight Savings Time date range for your area, see [Wikipedia Daylight Savings Time By Country](https://en.wikipedia.org/wiki/Daylight_saving_time_by_country). The precise _hour_ of the time change is as shown on the screen and is not configurable.

Note that it takes about a second to save the time when the Save button is pressed. Daylight Savings Time is supported in firmware version 2.0.0 or higher.

## Display
<img width="240" height="320" alt="SCR_0043" src="https://github.com/user-attachments/assets/ae0edabb-c407-4b48-b02e-67661435b665" />


An IPS Screen checkbox is available — enable this if your PortaPack has an IPS display panel, and reboot to apply.


## Encoder Dial
Allows the sensitivity of the encoder dial position between Low, Normal, and High (this adjusts the number of steps for a full rotation). The rotation rate multiplier adjusts the number of steps that occur when the dial is rotated faster, for faster scrolling through frequencies, file lists, volume setting, etc. The direction can also be set to Normal or Reverse.

![SCR_0067](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/fcfb7208-32ce-4e06-a2cb-07b238425f2b)

## FreqCorrect
Set TX and/or RX Frequency correction in Hz.

![PORTAPACK_FREQCORRECTION](https://github.com/portapack-mayhem/mayhem-firmware/assets/3157857/4c313bb6-1125-4b43-8b1b-c3721f3041b1)

A value between [-4,+4] MHz of correction is accepted, else it's truncated due to the variable used in persistent memory.

Use the '+' or '-' field to change to correction mode (addition or subtraction).

Use the MHz RX and MHz TX field to set the correction in each mode.

Settings are automatically saved in persistent memory.

## Hard Reset

Resets selected parts of the PortaPack back to a clean state. 

This is an [external app](External-apps-informations) (`.ppma` file on the SD card) and appears in the Settings menu.

Three options can be selected independently with checkboxes (all enabled by default); the number next to the first two shows how many items would be affected:

* **Settings file** — deletes the app settings (`.ini`) files from the `SETTINGS/` folder. The count shows how many `.ini` files are currently present.
* **Bad apps** — deletes incompatible external apps from the `APPS/` folder (apps whose version does not match the running firmware). The count shows how many such apps were found.
* **P.mem reset** — resets persistent memory to defaults. After this, the app launches the touchscreen calibration screen, since the calibration data is part of persistent memory.

Press **Erase sel.** to carry out the selected actions, or **No** to cancel and leave without changes.

> [!WARNING]
> This permanently deletes the selected files and settings. Use it when apps misbehave after a firmware update (for example, external apps that no longer match the firmware version).

## Menu Color
The Menu Color app can be used to change the background color scheme of the app menu buttons from the default grey to suit your preference.

![SCR_0080](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/502ad48c-c6a5-40d7-ac06-ea6193303864)
![SCR_0081](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/45ceb64e-7dcc-40b1-b832-0d428ea02e42)

## P.Memory Mgmt
Set persistent memory options.

![SCR_0039](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/7abd585c-1eaa-45b5-beb7-c7da27ddaa5d)

There are 256 bytes of persistent memory where settings are saved when there is a working coin battery. Note that a dead/missing coin battery will not prevent startup or display any messages, but settings will be lost after a power cycle. To prevent this, settings may be stored in a file on the SD card versus in the persistent memory, if enabled.

Widgets:
 * Use SD card for P.Mem: if checked the firmware will try to load last saved settings at startup. The checkbox is configuring a flag file under SETTINGS for it to work without coin battery.
 * Save P.Mem to SD card: save actual persistent memory onto the SD card
 * Load P.Mem from SD Card: manually load persistent memory from SD card
 * Reset P.Mem to defaults: reset the persistent memory to factory defaults

## Radio
In the radio section there are three options,

1. Enable/disable the Clock Output. (it can be activated / deactivated by top title bar (CLKout icon) or through that radio menu (check-box)

> Note 1 : In r9 Hackrf platform , due to our complex fw Architecture and usage of Si5351A , we have fixed the synthetized CLK out freq to 10Mhz.

> Note 2 : In all previous r1 to r8 Hackrf platforms , as we are using Si5351C, we do not have that limitation , and user can change the CLKOUT frequency between 4 kHz to 60000 kHz; press OK when the frequency is highlighted to select which digit position to modify and then use the encoder to scroll through the digit values. (it works with both clock references, the internal Hackrf (25Mhz) and the external -when available- from Portapack (TCXO 10Mhz ). Once enabled the CLK\_out , the new introduced frequency will be updated to the CLK\_out port, as soon as you press below SAVE button.

> ![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/86470699/5c44e075-cf84-4f8f-8ca6-a7979c1bf4aa)

> Note 3 : Zooming previous picture , when the unit detects that external CLOCK\_in -usually 10Mhz reference- (from Portapack or from external source) , it is indicated in the top title CLK\_in icon
> with some top arrow below the icon (right picture) . In case of no detection , it is indicated with some "X" below the icon (left picture),and in that case, the system takes the internal 25Mhz Hackrf clock reference.

> ![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/86470699/820c12d9-c724-48ed-ba1d-f3c31e096a07)

> Warning note : be awared that some of current market Portapack boards may have an integrated low ppm TCXO 10Mhz clock generator mounted, and when it is built in, it is connected in parallel to the external Hackrf CLK\_in port connector. So in that special case , that internal PP clock signal is present always in the SMA CLK\_in connector (this s a strange case, because in those devices, CLK\_in is behaving as real embedded ref. output of internal TCXO 10Mhz clock) , and you should better not connect any other external signal generator there (unless you dissassembly the Portapack from Hackrf) , because otherwise, you will connect two clock signal generators in parallel -the embedded one to the external one -, and you may damage that Portapack TCXO clock IC circuit.

> Here below , you can see two different examples of the embedded TCXO 10Mhz ref. clock,
> in a PP H1 brd (left side ) , PP H2 brd (right side) boards :

> ![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/86470699/ad83b637-4532-4ea8-994b-4372a38f9d15)

2. Enable/disable the Antenna Bias voltage. (it can be activated / deactivated by top title bar (DC bias icon) : **yellow** icon means activated, or through that radio menu (check-box). If enabled, ensure that all devices attached to the antenna connector can accept a DC bias voltage.

3. Enable/disable the External TCXO Clock input. (it can be activated / deactivated by that radio menu (check-box).
   Sometimes, in low battery charge voltage, or other low output TCXO voltage amplitude (much lower than the expected 3.3V pk-pk
   from ground) , we may have some boot problems with that
   external TCXO signal and in that case, we may want to deactivate it.

## SD Card
Enables higher speed access to the SD card (only works on higher-speed SD card models).

![SCR_0040](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/ec2409fc-f830-4a48-8328-8e386e131491)

Use the Test button to try it before saving this setting in persistent memory.
Files may not be read or written properly if this is enabled on a slower SD card.

## Splash settings
Configures the splash screen shown at power-up.

<img width="240" height="320" alt="SCR_0003" src="https://github.com/user-attachments/assets/2c57f656-4d39-4eca-b9d3-0443b04e94e6" />

* Show splash — enable or disable the splash screen at boot.
* Random splash on boot — if enabled, a random image from the SPLASH/ folder on the SD card is shown at each boot. If a fixed `splash.bmp` file is selected, random mode is disabled.
* Select picture — browse the SPLASH/ folder on the SD card to pick a specific splash image.

## Theme
- Choose the global theme color, that will also be applied to apps. Available themes: Default (Grey), Yellow, Aqua, Green, Red, Dark. A restart is required to fully apply the new theme.
- Override "Menu Color" with the theme one, or keep the one selected in "Menu Color"

![image](https://github.com/user-attachments/assets/cc46c4df-53a7-402e-96c8-7ee3befda184)


## Touchscreen Threshold

<img width="240" height="320" alt="SCR_0008" src="https://github.com/user-attachments/assets/e92dd5c5-ba58-4601-91d9-7660afd3f925" />

The touchscreen's resistance detection layer can be eventually wore out (it's inside the soft layer so use screen protector won't slow it down) by using it, or it's originally bad quality, so you maybe need to tune the threshold if you can't touch an area, or some region are kept pressing even if you are not pressing it (which causes the back light keeps on forever because the device think you are keep touching the screen)

In the best case the threshold should be 1, but considering the most case that the layer already kind of damaged, we default it to 32. The threshold value range is 1 to 1023.

If you are having issues listed above, just press Auto detect, and follow the guide, and it will automatically tune to a value that good for your device.

When auto detecting, don't touch the screen, until count down finished. otherwise it will give you a bad value. But don't worry if you mistakenly touched, just need to start over and nothing bad would happen.

## TX Limit
Limits the RF transmit gain globally across all applications.

<img width="240" height="320" alt="SCR_0004" src="https://github.com/user-attachments/assets/bbac886d-0df8-41d6-9e34-d833a9054563" />

* Disable TX — disables all transmit functionality. When active, the TX Gain and TX Amp fields in all transmitter apps become non-focusable and are shown in grey with a value of 0.
* Disable TX Amp — disables the TX amplifier stage. When active, the TX Amp field in all transmitter apps becomes non-focusable and is shown in grey with a value of 0.
* TX Max Gain — sets the maximum allowed TX gain (range: 0–47 dB). The gain is capped at this value across all apps. When the TX gain reaches the configured maximum, the gain field is highlighted in cyan to indicate the limit has been reached.

## User Interface

<img width="240" height="320" alt="SCR_0044" src="https://github.com/user-attachments/assets/90c0ff7c-23bb-45eb-af92-6986987f1009" />

The UI interface setting for the following can be Enabled (tick) or Disabled (x) or selected value for the backlight timeout:

* Touchscreen can be enabled or disabled.
* Backlight off after 5, 15, 30 seconds, 1, 3, 5, 10 minutes, or 1 hour; or never (default).
* Show the clock — selects whether to display the clock on the home screen, and whether to show time only or time and date.
* Back button in menu — Enables a "Back" button on all menu screens.
* Show/Hide Status Icons — Select which status bar icons are visible or hidden. Available icons: Camera (screenshot), Sleep, Stealth, Converter, Bias Tee, Clock, Mute, SD Card. Speaker is only shown on devices with AK4951 codec; Battery Icon and Battery Text are only shown when a battery management IC is detected.

> Note: The splash screen is configured separately under Settings → Splash settings.