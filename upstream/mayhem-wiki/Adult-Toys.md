> **Consent warning:** This app can send control signals to compatible Bluetooth devices within radio range — including devices belonging to other people. Using this app to operate, interfere with, or control any device without the explicit consent of its owner is a serious violation of personal boundaries and privacy, and may be illegal under harassment, stalking, or communications interference laws in your jurisdiction. **Only use this app on your own devices.**

Adult Toys TX transmits Bluetooth Low Energy (BLE) control packets compatible with **Love Spouse** brand Bluetooth-connected devices. The protocol is based on the Lovespouse implementation from the Flipper Zero Momentum project. The app operates on BLE advertising channels in the 2.4 GHz band.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Settings

* **Frequency**: BLE channel frequency (2.4 GHz band). The app cycles through BLE advertising channels 37, 38, and 39 automatically.
* **Start / Stop**: Begins or halts the continuous transmission of control packets.

# Notes

* The device must be in range and in a connectable/advertisable state to respond.
* Currently only the Love Spouse protocol is implemented. Other brands are not supported.
* Settings are saved to `tx_adult_toys.ini`.