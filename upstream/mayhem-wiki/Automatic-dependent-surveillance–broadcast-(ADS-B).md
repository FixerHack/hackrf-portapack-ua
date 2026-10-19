![Main View of ADS-B](https://i.ibb.co/ZN5vhN1/SCR-0005.png)

> [!NOTE]
> This is an [external app](External-apps-informations) and must be present on the SD card in the `APPS/` folder.

# Introduction 
With this app you can receive real-time ADS-B used for air traffic control.

# Functionality
Select a received aircraft and more detail will be shown. Select "Show on map" to see the aircraft location. ADS-B operates on 978 to 1090 MHz. Even a short antenna attached directly to the Portapack will receive ADS-B when the receive preamp is enabled ("1" displayed).

## Map
For map functionality a world map must be loaded on the SD card. The map image and other SD card content is available from the portapack-mayhem github download page.  The map can be zoomed in or out by moving the cursor down to the map region and turning the encoder dial (resolution is still limited by the map file, but zooming in helps to separate overlapping plane icons, and zooming out may help if you have really good reception).  The map position can also be changed by modifying the latitude and longitude values.

## Airlines

### Log into microSD
The ADSB RX app will log each frame including the following columns:

* **(YEAR MONTH DAY HOUR MIN SEC)**
* **(RAW PACKET IN HEX)**
* ICAO: **(ICAO)**
* **(CALLSIGN)**
* Alt: **(ALTITUDE)**
* Lat: **(LATITUDE)**
* Lon: **(LONGITUDE)**

Example:

`20171103100227 8DADBEEFDEADBEEFDEADBEEFDEADBEEF ICAO:nnnnnn callsign Alt:nnnnnn Latnnn.nn Lonnnn.nn`

## Screenshots
Main ADS-B View.  In the columns, the ICAO/Call column will show the Callsign if known, otherwise the ICAO.  The Lvl field is the Altitude in 100's of feet.  Spd is the speed in mph.  Amp is the signal strength, which may be increasing/decreasing depending on whether the plane is getting closer.  Hit is the number of packets received from the same plane, and age is the number of seconds since the last packet was received.

![Main View of ADS-B](https://i.ibb.co/ZN5vhN1/SCR-0005.png)

Aircraft View.  The altitude is in feet, and the speed is in mph.

![Aircraft View](https://i.ibb.co/pwzdgD0/SCR-0006.png)

Map View.  The map can be zoomed in or out by moving the cursor down to the map area and then turning the encoder dial.

![Map View](https://i.ibb.co/SrD1gbv/SCR-0007.png)

A/C Details

![A/C Details](https://i.ibb.co/SRq38gJ/SCR-0008.png)
