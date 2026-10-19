![image](https://github.com/user-attachments/assets/d6e775b3-04c7-4651-ae37-73958e7769a5)

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Introduction

That Wefax App, 
allows to  receive any HF Weather Station Brodcasting (Wefax, https://www.sigidwiki.com/wiki/WEFAX) , and decode its analogue weather fax maps transmissions . 

Here is the list of current Wefax stations and its frequencies,and the exact GMT map transmission time  https://weatherfax.com/stations/.
To save RF spectrum , and optimize the range , all those broadcasting are transmitting in USB .
Some example of the spectrum frequencies are the following ones , 

![image](https://github.com/user-attachments/assets/a47935e7-c08c-4d05-9137-a006764b894d)

For better usability , we are internally applying that tune-offset . Therefore you just need to tune the official published WeatherFax frequency transmitter. (3.855 Khz in that example,  or 7.880 Khz , 8.040 Khz ,...)  

That Wefax App is combining two consecutive demodulations. First RF USB audio baseband demodulation , and later demodulating the FM subcarrier audio baseband tones. (Audio Baseband with centered  f_subcarrier fsc (1900Hz), and modulated in  FSK +-400Hz ; Shift White pixel +400 Hz = 2.300 Hz, and  Shift Black pixel -400 Hz = 1.500 Hz).  

That analogue AM-FM modulation , it is commonly used in Wefax (HF Weather Fax transmissions) . 
It demodulates APT signal of the HF weather fax maps. , and sends the demodulated low scan map APT signal in parallel to the speaker (just for our audio tuning reference ) and to the LCD display in low resolution. And it allows to the user , been able to RECORD (with START / STOP)  that map in full resolution to the SD/BMP folder.
  
# Usage

Hackrf has poor sensitivity to receive directly those HF Wefax signals, (mainly broadcasted in HF band : 3 Mhz to 16 Mhz) Normally we should better add a front up-converter with better HF filtered pre-amplifiers,  and a reasonable good enough HF antenna. WEFAX's format is a derivative of the [Automatic Picture Transmission (APT)] originally developed for transmission from the polar satellites of the USA. WEFAX has 60, 90, 100, 120, 180 and 240 LPM (Lines per minute) speeds, and two IOC (Index of Cooperation) modes, IOC 576 (1200 line maps)  and IOC 288 (600 line maps). Most weather forecasts are sent in IOC 576, 120 lpm (make sure to select those 120 lpm . Our initial target would be , WEFAX-IOC576 standard.


You can tune , inputting directly the Wefax broadcast frequency Station or pressing LOAD WeatherFax pre-setting stations , in the (tune menu). 

![image](https://github.com/user-attachments/assets/42b7e157-0d0b-4d95-abd2-6108f98cc365)



The application is in continuous display mode (trying to plot 2 lines / sec - if you select 120 lpm IOC 576 -the most common-) , and once you input the correct station frequency , you need to adjust the gain reception to the best point (through LNA :0/1, AMP , VGA) , to  not saturate and not get too weak signal. If you don't amplify enough  it could be darker image, or if you amplify too much, there could be much more whites. So it needs some tweaking too. Looking the screen and hearing the sound you should be able to find a good compromise tuning reception. In good setting conditions , you will start to recognise some part of the map in the screen , (like this below one)

![image](https://github.com/user-attachments/assets/8b3806c1-5979-4948-ac80-bc98b24815b3)

If needed , you can also check the waterfall signal Spectrum (and adjacent channels, interferences,...)  using the other [Audio App , with AMFM demod. mode](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Audio-Receivers) in ZOOM x2 (for better view)  ,and you can confirm ,  
* that the frequency is the correct one (well tuned when top FM +deviation (white map pixels) are aligned to the border of the right yellow mark) 
* and the waterfall signal has also some -deviation (black map pixels) left peaks (as in the below picture)  .
* that you can confirm , that you have adjusted the best overall gain (proper LNA_AMP / GAIN / VGA)  .  

![image](https://github.com/user-attachments/assets/fd578f6f-79cc-4b51-87f2-0f2ac4c78e66)



Once you confirmed all those above points from Audio App or directly from the Wefax App (optimizing the gain levels for best LCD screen map decoding.  you can press START from the Wefax App ,and it will record into SD/BMP , related decoded maps , in high resolution.
![image](https://github.com/user-attachments/assets/8d2fa901-5095-4aca-8b81-af5483d5d3bf)


Pls. find attached some captured examples, 

![image](https://github.com/user-attachments/assets/6e3a58ad-cec4-4bbf-976b-d1185baa3fcb)
![image](https://github.com/user-attachments/assets/4feced1f-7ec0-4cb5-816a-b80bfeb7580f)

Receiving & Decoding WeatherFax: https://youtu.be/KJ7u5V44u2o
The video starts by showing where the preconfigured WeatherFax frequencies are located in the Portapack menu, making it easy to start receiving weather fax transmissions.
You will then see live WeatherFax signal reception, followed by automatic decoding of the signal into weather map images directly on the device.
The video also shows where decoded WeatherFax images are stored on the H4M Portapack Mayhem, and includes three real WeatherFax images received with this device.





