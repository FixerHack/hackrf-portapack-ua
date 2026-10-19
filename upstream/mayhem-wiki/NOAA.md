![image](https://github.com/user-attachments/assets/9e6273a2-4b50-4deb-b073-4d70548f9c67)

# Update regarding decommissioning of all NOAA POES satellites
**All three NOAA POES satellites have been decommissioned and are no longer available for receiving.**

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## Decommissioning Timeline
**NOAA-18:** Decommissioned on June 6, 2025 at 17:40 UTC due to an unrecoverable S-Band transmitter failure.

**NOAA-19:** Decommissioned on August 13, 2025 at 16:55 UTC due to a battery failure on August 9, 2025 that threatened safe spacecraft operations. This occurred earlier than the planned August 19 date.

**NOAA-15:** Decommissioned on August 19, 2025 at 20:37 UTC (postponed from the original August 12 date).


# Update regarding decommissioning of NOAA-18
NOAA-18 was decommissioned on June 6, 2025 and is no longer available for receiving.  This is due to a failing S-Band transmitter used in the control of the satellite.  At the time of this update both NOAA-15 and NOAA-19 continue to remain operational

https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes/2025-notice-of-changes/decommissioning-of-noaa-18-scheduled-june-6-2025-1733-1749-utc

# Introduction
That  Rx NOAA App, allows us to receive any of the 3 current operating NOAA weather satellites that are transmitting analogue [APT](https://en.wikipedia.org/wiki/Automatic_picture_transmission) maps in the 137 MHz band .
Currently, they are using those frequencies, (but in future they may change them, then , better time to time, double check it ) 
![image](https://github.com/user-attachments/assets/85e9e32f-7c69-44a6-aaeb-5695161beeca)


NOAA Polar Operational Environmental Satellites (POES) have an orbital period of approximately 102 minutes, approximately 520 miles (800 kms)  above Earth, meaning they circle the Earth in about that time.The Earth's rotation allows the satellite to see a different view with each orbit, and each satellite provides two complete views of weather around the world each day. This allows them to complete about 14 orbits per day, passing over the same location twice daily, once during daylight and once at night.Example of the 14 orbits , in 24h (Image from NOAA):

![image](https://github.com/user-attachments/assets/cf50aacf-6e41-414e-8a8b-8ed57ed9bf7d)



The [APT signal](https://www.sigidwiki.com/wiki/Automatic_Picture_Transmission_%28APT%29#Frequencies) is a 256-level amplitude-modulated 2400 Hz subcarrier, which is then frequency modulated onto the 137 MHz-band RF carrier. The satellite is broadcasting it with an effective radiated power of approximately 5 watts (37 dBm) at 800 kms from the ground earth . These signals are frequency modulated (FM) and carry low-resolution weather imagery. 

The analogue APT weather map transmission was invented in the 60's 
![image](https://github.com/user-attachments/assets/433e3db3-e541-42e4-bd0f-57ed64aed841)

It has a resolución of  4 Kms/pixel.
 Mínimum , 2 passes / day 
 Continuos signal in the visual satellite range time.

The maximum pass duration for NOAA satellites, when receiving signals from them using ground equipment, can be around 10 to 15 minutes. This duration refers to the time the satellite is visible and within signal range at a given location, from its initial rise above the horizon to its descent below the horizon on the other side.  (If you have a pass just above of your (zenith = visual satellite max. elevation = 90º) , you can record the max.  long pass, till around 1800 lines with  max 15 min time aprox)

![image](https://github.com/user-attachments/assets/2abb8dfb-d6e6-4bd3-bc5d-600929d36543)
![image](https://github.com/user-attachments/assets/be9279e1-a0a6-4747-ae56-f9bc858e9f1d)

![image](https://github.com/user-attachments/assets/97116ed9-1b42-4773-96b1-9520216b60fc)
![image](https://github.com/user-attachments/assets/bc7d2365-924f-49b3-a69c-73f8ab248697)

APT signal format : 120 lines / minute ,  sending two pictures at the same time (visible / infrared ) 
8 bits/pixel.The signal amplitude represents the brightness of each pixel. Two lines per second, 4160 pixels per second.
2080 pixels per line, each channel has 909 useful pixels per line.

![image](https://github.com/user-attachments/assets/c17d63f1-d898-4672-aedf-fe0bb4d1a45a)

![image](https://github.com/user-attachments/assets/a5edc905-8d6c-465b-bd8c-09d2908dbe48)

![image](https://github.com/user-attachments/assets/f6eb6af2-f00c-4814-b8c2-b18d2719d5d6)

# Usage

Hackrf, like the rest of SDR receivers,  have not enough sensitivity to receive directly those NOAA APT maps with the stock rod antenna. To receive those signals , the best would be to use an  omnidirectional QFH 137 Mhz antenna band ,or a proper 137 Mhz  dipole  + bandpass amplifier (if you have  noisy strong adjacent channels, it will help to improve the reception). 

The most simple antenna you can use is a [V-dipole antenna](https://lna4all.blogspot.com/2017/02/diy-137-mhz-wx-sat-v-dipole-antenna.html), consists of two wires or rods of 52cm, spread apart by 120 degrees. Instead of using a protactor you can use trigonometry, the distance between the tips of each rod should be around 90cm.

![image](https://github.com/user-attachments/assets/ffb0e67b-f52b-4a9d-bd29-69681e38fc17)

You can tune , inputting directly any of the 3 x above current  NOAA Satellite frequencies (NOAA 15: 137.62MHz. NOAA 18: 137.9125MHz. NOAA 19: 137.1MHz) ,and check at what exact time , the satellite will be visible in his orbital pass. (there are many programms and web links to check the exact local time pass to your ground station place ) . 
Here you have,  some predict and tracking web links examples  : 

To check [NOAA 15](https://www.n2yo.com/satellite/?s=25338), [NOAA 18](https://www.n2yo.com/satellite/?s=28654), [NOAA 19](https://www.n2yo.com/satellite/?s=33591) real time tracking position or next 10 day prediction passes to your location (based on your IP).

You need to adjust proper LNA , RF GAIN , VGA till getting proper signal (not weak, not saturating) , and you can adjust the audio volume till recognizing the usual beep , beep sound indicating frame A, frame B every 0.25 segs.Once you confirmed all those above points optimizing the gain levels for best LCD screen map decoding. you can press START , and it will start to  record the map into SD/BMP folder ,in high resolution. Once you lose the satellite signal , you can press the STOP button , and you can check the recorded image into that SD/BMP folter . The file name will start by "noaa_year-month-date-time.bmp"

![image](https://github.com/user-attachments/assets/b1758def-6b6f-43fb-a317-2ac1bc928f54)


![image](https://github.com/user-attachments/assets/c3f5ac4b-e1b7-49a7-8793-4c0a95d78905)


Here some example of local test replay  decoded maps from that Mayhem NOAA Application , that we can record in .bmp image format  

![image](https://github.com/user-attachments/assets/2eedb52f-791e-4525-9510-f7217bd51ebc)

![image](https://github.com/user-attachments/assets/59c1d670-e271-4042-8a83-d13814cdb908)

Previous pictures was from local Replay , when debugging and developping. 
Here I can share a real captured picture , NOAA 19 pass, with max. elevation of 83º . The satellite came from North (that is why picture appeared with direct proper North on top ). I recorded using new binary after  [#2654 PR ](https://github.com/portapack-mayhem/mayhem-firmware/pull/2654) ,using QFH 137 Mhz antenna with cheap pre-amplifier. And  PP settings :  
LNA = 1 ,  GAIN = 32 , VGA (not relevant 30 or 40) + a direct cheap pre-amplifier to the PP, and short antenna cable . (It was just quick hand made testing) .

![image](https://github.com/user-attachments/assets/02d0a36a-f1fb-411f-8262-e60e78ef921c)
 

