# I2C external device driver integration

> [!IMPORTANT]  
Always check the wiring, because you can kill your devices!

## How the I2CManager works
On boot, the system will do a full I2C bus scan, and try to find each device it's driver. If a driver is not found, it won't look for it again. The scan is repeated only on main screen and by any app that requests it. If your app requires the periodical scan for new devices you can enable it but disable it in the destructor! These scans will detect new devices and device removals. Devices will be removed when the I2C communication to it's address fails multiple times in a row. If the device is removed, but found again (like plugged in again) the driver will be started again for it.
Any app can get a pointer for any driver, and call it's public functions, so it is not forced to just use the update() polling method. But for this, you should write it's own app. The app is preferred to be external app.

## Basics
The namespace is i2cdev, there is everything you'll need. Currently all drivers are under the firmware/common folder. You can take the i2cdev_bmx280 as an example. It has tons of comments that will help you.
Important files:
 - i2cdevmanager.hpp  - the core of everything. It describes the I2cDev, and the I2CDevManager.
 - i2cdevlist.hpp     - here you must put your new driver.
 - i2cdev_xxxxxx.hpp + cpp  - the driver itself.
 
## Steps needed
1. Get a good name for your module. From now we will use I2CDEVMDL_EXAMPLEDEV
2. Insert a new enum element into the i2cdevlist.hpp at the END of the enum I2C_DEVMDL. Also create define for the dev's I2C address (for all if it has multiple).  This should be I2CDEV_EXAMPLEDEV_ADDR_1 , I2CDEV_EXAMPLEDEV_ADDR_2, ...
3. Create the new i2cdev_exampledev.hpp and i2cdev_exampledev.cpp files. Use the namespace i2cdev!
4. Create the class for the device named I2cDev_ExampleDev, and derive it from I2cDev.
5. Override the bool init(uint8_t addr) function. This function must check the address it got if the module uses it. If yes, then try to init the device. Query for any special registers that you can identify the dev, to make sure it is THAT  device you are writing the driver for (since different devices share the same address sometimes). If THAT is your device, then set it up and get it ready to go. Also you must return true if the driver is ok. If there is ANY error, you must return false. In this function you MUST set the variable addr to the given address (addr = addr_;). You MUST set the model variable to the new enum you just created. Also you need to set the query_interval value, how often does your device needs to be polled for new data. Don't put here too small value, since it'll slow down the whole system. The value is in seconds. You can use the I2cDev::i2c_read() and i2c_write() functions or one of the helper functions to read / write from the bus. init() must be as fast as possible.
6. Override the void update() function. Here you query your device for new data. If you got any value, then you broadcast it system wide. (see next step). update() must be as fast as possible. Try not to delay there. So please don't run calibration code that took 1000 samples and 10 seconds.
7. Select the message you want to use. The current system wide messages are in the message.hpp. If you don't find any that fits your need, you can create a new one. (try to avoid that).
8. In your update() code just create a new message variable you have selected, take for example the EnvironmentDataMessage msg{temp, hum, pressure}; fill it with your data, and send it to the system with the EventDispatcher::send_message(msg); function.
9. Include your hpp file (i2cdev_exampledev.hpp) in the i2cdevmanager.cpp. Then add it to the found() function. There check if the currently found device's address matches any you can handle, and it yes, create an instance of your class (item.dev = std::make_unique<I2cDev_ExampleDev>()) , and try to call init(). If it fails, set the item.dev = nullptr so other drivers can try to work with it.
10. Update apps / create apps to handle your data.
11. Test, test and test.
12. Clean up your code. Remove any unneeded things, use the less needed variable sizes. Try to use the less FW space and RAM. There is not so much ram assigned to this task.

## Debug
You can use the Debug / ExtSensor app to see what I2C devices are found by the system. You can use the usb_serial_asyncmsg.hpp to send debug messages to USB serial. (before you must send "asyncmsg enable").

## App development for devices
I2CDevManager::manual_scan() will start an one time scan for new (or removed) devices.
I2CDevManager::set_autoscan_interval() will start a periodic search for new devices. DON'T FORGET TO SET IT TO 0 when you finished or your app is closed!
I2CDevManager::get_dev_by_addr(), I2CDevManager::get_dev_by_model() will give you a pointer to the device. Preferred to use the get_dev_by_model(), since with that you'll know what that pointer needs to be casted (it'll return a generic I2cDev, that you derived your driver from).
I2CDevManager::get_dev_list_by_model() and I2CDevManager::get_gev_list_by_addr() returns a vector of the models it discovered (that HAS WORKING DRIVER) and all the addresses it sees on the bus (even those without a driver).
When the scan detects any change in the device list it'll send a "I2CDevListChangedMessage" system wide message. 

