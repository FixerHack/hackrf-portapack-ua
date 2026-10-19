For those of you who are tired of having to get that Micro USB cable to charge your Portapack.
This simple modification will give you the ability to charge with a USB-C cable. The battery state and charging current will work the same way as before modification, the ON/OFF switch behavior when plugged in will be the same as before modification (only charge in ON position, run from usb power in OFF position)
 As a nice consequence of this mod, your portapack will be much easier to charge while its placed in a stand. And if you have removed your SMA plugs on the bottom, the Portapacak will be able to stand on its own while plugged in, which is nice.

![standing pp](https://github.com/user-attachments/assets/b2375c18-6ca3-434e-9ce7-9d9763cf5f41)


Anyway, what you need is some thin wire and a USB-C chrging module from AliExpress in my case, also some tools to make a hole for the charging cable.

This is the module i used:
![Charging module](https://github.com/user-attachments/assets/5d0ca413-b776-449e-9011-f872ac69e2a0)

The placement of the module is a bit important, you dont want any smd components under it, and you dont want any bare pads that can contact the charging module pcb, but that is less important, because you can insulate if you want to.

When soldering the wires to the module, do not stick them through the holes, place them flat on top of the pcb, otherwise they will damage the silkscreen and short something.

Do not use hotglue to hold the module, the module gets hot and the glue will melt, i speak from experience.
Make a hole in the speaker grill to fit.
(The picture shows data wires soldered on, it was a test and it didnt work, dont try that)

![close up module](https://github.com/user-attachments/assets/ceb5c57f-59f9-4d60-b2a4-512fede8ebff)


Connect + and - wires from the module to BAT+ and GND on GPIO header of H4M portapack, if you have other versions of Portapack, you will have to find another place to connect to the battery.
![module placement](https://github.com/user-attachments/assets/65431346-eb83-4fc9-ae53-06eac55bf192)


They way H4M is designed, there is a battery monitoring chip that is separate from the charging chip, this way we get full battery indication on the battery page, even when not using the charging chip on H4M board. 
The charging speed on my PP went from 800mA to 1A, and became more reliable.

![charge states](https://github.com/user-attachments/assets/74c44eee-d660-4382-bfc8-6f3c8e1e84c7)
