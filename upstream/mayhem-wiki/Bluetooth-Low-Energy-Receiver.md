![image](https://github.com/user-attachments/assets/02c4dfef-a0b7-4d78-a7ba-50128b6cb813)

# Introduction 
As of 10/31/23, the previous BLE implementation has been updated, and improved to correct some of the issues in the previous BTLE app. This BLE app has several features which I will highlight in a brief overview.

# Main Menu:

This is the main view which provides the user with incoming packet entries captured by the BLE Scanning.

1. The BLE app upon entry will scan for **only** BLE advertisement packets, and report them on the screen. The **Channel** knob can be used to select which advertisement channel to listen on. There is an Auto feature which will switch channels incrementally in 25ms steps.
2. Once found the user can then select an individual MAC Address entry to pull up a more detailed view of most recently captured data packet from this MAC Address.
3. The **Sort Knob** will sort the list of MAC indices by either Ascending MAC Address, device name, number of hits, dB, or by most recently updated entry.
4. The **Filter** button allows the user to filter based on the hex data of each packet. It also allows for filtering based on the ASCII name of the device (if found). More on that below.
5. The **Name** toggle allows the user to toggle off and on name display, if there is a name associated with the device. Not all devices have a name string. This name string is being parse from the Shortened and Complete Local Name packet type. See BLE Spec for information on packet types.
6. The **Log** toggle allows BLE app to write all filtered packet data into SD card under `/BLERX/Logs`. Each log entry contains timestamp, packet type, length of the packet, MAC address, and packet data.
7. The **USB Log** toggle allows BLE app to write all filtered packet data to serial over USB. Messages can be viewed by any serial terminal client (eg: PuTTY) by opening the port (eg: '/dev/ttyACM0') with a baud rate of 9600.
8. The **Clear** button allows the user to clear entries as they fill up the screen.
9. The **Export CSV** file allows the user to export the current list of packet entries into a csv style file. Upon resaving the file, the file will update the existing entries with new data, as well as append new entries to the existing file.
10. The **Tx** button allows the user to switch to the BLE Tx app. See BLETX for more information.

**Note:** The dBm displayed on the list of devices is an estimated receive power, relative to the Tx power of the device. Estimation takes into account the LNA/VGA/AMP when determining the dBm value.

# Packet Detail Menu:

This menu is a more single detailed view on a specific entry selected by the Main Menu. More specific packet information is laid out here such as:

1. The **MAC Address**
2. The **PDU Type** which displays the last received PDU packet type as noted here:

| Type | Name | Description |
| :--- | --- | --- |
| `00` | `ADV_IND` | Scannable advertising indication for all devices |
| `01` | `ADV_DIRECT_IND` | Directed advertising to a specific device indicating that only that device can connect |
| `02` | `ADV_NONCONN_IND` | Advertising indication but not accepting connections or scans |
| `03` | `SCAN_REQ` | Sent by a device to receive more info from scannable advertisers |
| `04` | `SCAN_RSP` | Response to 03 containing more info |
| `05` | `CONNECT_REQ` | Sent to an advertiser to initiate a connection |
| `06` | `ADV_SCAN_IND` | Scannable advertising indication but not accepting connections |
| `07` | `ADV_EXT_IND` | BT 5.0, points to additional data on secondary channels |
| `09` | `AUX_ADV_IND` | BT 5.0, scannable advertising indication for all devices on secondary channels |
| `0A` | `AUX_SCAN_REQ` | BT 5.0, sent by a device to receive more info from scannable advertisers on secondary channels |
| `0B` | `AUX_SCAN_RSP` | BT 5.0, response to 0A containing more info |
| `0C `| `AUX_CONNECT_REQ` | BT 5.0, sent to an advertiser to initiate a connection |
| `0D` | `AUX_CHAIN_IND` | BT 5.0, chains advertising packets together when they get too big |
| `0E` | `AUX_CONNECT_RSP` | BT 5.0, response to 0C |
| `10-26` | Link Layer | Link layer setup and operation |
| `26-FF` | Data | General data and proprietary |

3. The last packets received for each data type, their length, and their contents.

1. The **Send** button immediately moves the user to the BLE TX app and allows the user to transmit the selected packet data.
2. The **Save** button allows the user to save packets in the format used by the BLE TX app.
3. The **Done** button brings the user back to the Main Menu.

# Video:

Below short example on using the BLE Rx App.

https://vimeo.com/886881206?share=copy

# References:
BLE Tx App: [Bluetooth Low Energy Transmitter](../wiki/Bluetooth-Low-Energy-Transmitter)

BLE Packet Types: https://www.bluetooth.com/wp-content/uploads/Files/Specification/Assigned_Numbers.pdf?id=3

Reference Code Used in Porting Protocol: https://github.com/JiaoXianjun/BTLE
