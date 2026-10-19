# Introduction
_Are you bored of the standard power on screen? Do you want your own image at power up to personalize your device? You can!_

Save a **240x304 24-bit BMP file** named `splash.bmp` in the root of the SD card, and it will be used as a starting up splash screen !

For PortaRf the resolution is **320x464**.

Beginning in firmware version 1.7.4, the splash screen BMP files stored on the SD card can be viewed in the File Manager application and set to be the current splash screen with a single click.  

You can share and get ready to use images in the `#splash-screens` channel over our [Discord](https://discord.gg/tuwVMv3) group.

There is also https://ppsplash.creativo.hu/ where you can choose and download splash screens from a curated selection

You can of course use https://hackrf.app/ to upload them directly to SPLASH directory (firmware version >= 2.0.1 is needed)

> [!TIP]  
> If you enable the Splash screen in the settings, but don't provide /splash.bmp to the SD card, each boot will show a random one from the SPLASH folder.


> [!WARNING]  
> If your firmware is recent enough, it may support activation/deactivation of the splash screen via a checkbox in **Settings → Splash settings** [(Splash settings)](Settings#splash-settings). Don't forget to check it if the splash screen isn't displayed at startup!

## Example
![image](https://github.com/user-attachments/assets/ecdf315a-9e1d-4707-bb0d-a3ed728efc4e)

## Online converter
You can use this website, to create your splash from almost any image. [https://ppsplash.creativo.hu/editor.html](https://ppsplash.creativo.hu/editor.html)

## Tools / How-to
Use your favorite picture editor to adjust size, or use "convert" from [ImageMagick](https://imagemagick.org), which is a powerful image manipulation tool. It is open source and available for all common operating systems.  

> [!NOTE]  
> From version 7 of [ImageMagick](https://imagemagick.org) you will get a warning when running with `convert` or `magick convert` saying that the command is depricated and you should now use `magick` only.
```
$ convert source.jpg -resize 240x304 destination.bmp
```

### If you see and don't want a frame left and right, you can adjust the convert with:
```
$ convert source.jpg -resize 240x304 -gravity center -extent 240x304 destination.bmp
```

### To choose the filling color when resizing/extending the image, add '-background color' after 'source.jpg':
```
$ convert source.jpg -background "#000000" -resize 240x304 -gravity center -extent 240x304 destination.bmp
```
or 
```
$ convert source.jpg -background black -resize 240x304 -gravity center -extent 240x304 destination.bmp
```
The list of predefined colors can be obtained with ```convert -list color```

### To check if the splash got the required parameter, check:
```
$ identify destination.bmp     
destination.bmp BMP3 240x300 240x304+0+0 8-bit sRGB 216054B 0.000u 0:00.000
```
If it is saying '8-bit', you're good. It's the number of bits by color components. For sRGB, 8+8+8 = 24-bit

> [!TIP]  
> If you have save the image via a different program and it looks right when using the `identify` command above, try to convert it again  with [ImageMagick](https://imagemagick.org) following the instructions above.
## Limitations
- image have to be a 24 bits bitmap.
- width have to be exactly 240 pixels wide.
- height have to be in the [ 1 , 304 ] range. Any additional lines will be cut.