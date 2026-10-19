# VOR TX

A **VOR** (VHF Omnidirectional Range) ground station lets a receiver determine its bearing (radial) from the station by comparing two 30 Hz signals: a reference phase and a variable phase that is offset by the bearing angle.

**VOR TX** generates such a signal. It transmits a DSB-AM carrier carrying a 30 Hz reference tone and a 30 Hz variable tone offset by the chosen radial, a 9960 Hz subcarrier FM-modulated ±480 Hz by the reference tone, and an optional 1020 Hz Morse identifier. In effect the app emulates a VOR beacon transmitting a user-programmable radial.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card). It was introduced in [#3244](https://github.com/portapack-mayhem/mayhem-firmware/pull/3244).

New to VOR navigation? These videos explain the concept well:
- [VOR Explained Simply by FlightInsight](https://youtu.be/uqGvbVDp5Jk) (recommended for beginners)
- [How to navigate using VOR by FlightInsight](https://www.youtube.com/watch?v=RTxW1VB_Qog)

> [!WARNING]
> Disturbing the air band is one of the most illegal things you could do. This is not a joke - you can get into serious legal trouble very quickly.
>
> Neither the developers, the Mayhem team, nor anyone else except you is responsible for any fines, imprisonment, or other consequences resulting from interfering with aircraft communications, air navigation, or any other radio service while using this app. You alone are responsible for how you use this app.

<img width="240" height="320" alt="VOR TX" src="https://github.com/user-attachments/assets/db81e640-6e6b-4dee-9734-95312c344436" />

## Values

- **Radial** (write): the radial that should be transmitted
  - Please note: the value can be changed at any time but the change takes effect only after the transmission is restarted. To transmit a new radial, the user must stop and then start the transmission.
- **CW Identifier** (write): enables the Morse code transmission that identifies the VOR
- **Ident** (write): the string (7 characters at most) to be transmitted as VOR identifier
- **Status** (read): the current status of the app, either **Idle** or **TX radial XX** where **XX** is the radial selected before enabling the transmission

The bottom part of the application controls the transmitter settings, such as the frequency to use, the frequency step and the TX gain. To start and stop the transmitter, use the **Start** or **Stop** buttons. Before starting any transmission, a dialog is displayed informing the user that this app should only be used in a lab environment while transmitting into a dummy load.

## See also

- [VOR RX](VOR-RX) — receive and decode a VOR signal