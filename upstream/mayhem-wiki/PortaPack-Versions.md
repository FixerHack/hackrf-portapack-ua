> [!IMPORTANT]  
Mayhem does not manufacture or sell any devices, nor does it profit from designing the software and hardware. No contributors got paid writing codes or desiging hardware. Please be cautious of those who steal code or steal hardware design from here and profit from it by selling modified versions.

## Introduction

PortaPack is an add-on for the HackRF Software Defined Radio (SDR) platform that adds a touchscreen display, buttons, and additional functionality to transform it into a portable SDR device. There are many versions of PortaPack available on the market, created by different manufacturers, often with varying features such as larger screens, added charging capabilities, or different main chips due to price and availability.

This guide provides an overview of various PortaPack versions, their compatibility with Mayhem, and key differences between models. Please ensure you verify hardware compatibility with the vendor before purchasing, as manufacturers frequently change components without notice.

## Table of Contents

1. [PortaPack Versions Comparison](#portapack-versions-comparison)
2. [HackRF Information](#hackrf)
3. [Frequently Asked Questions](#faq)
4. [Detailed PortaPack Version Descriptions](#detailed-portapack-version-descriptions)


***

# Portapack Versions Comparison

There are many different versions of PortaPack, mainly due to Chinese companies putting their own take of the design such as adding a larger screen, adding charging or changing the main chip due to price and availability.  

**Most manufactures changes components frequently without notifying anyone, thus you should always ask the vendor the compatibility of their hardware before you buy, even if a specific vendor/store/seller already has a lot of positive reviews.**  

Asking which one to buy in the community is welcomed, however it could be not helping since things changing fast and no one can guarantee you that something will be 100% working.  
    
The current list is:

 Version|Compatible|Screen Size|Onboard Mic|Battery IC|GPIO Port| AK4951 Codec| WM8731 SSOP Codec| WM8731L QFN Codec| CPLD| INS 8002E Audio Amp| LTK 8002D Audio Amp| CS 8122S Audio Amp|
|-------|----------|-----------|-----------|----------|----------|-------------|-------------------|-------------------|------|---------------------|---------------------|-------------------|
|[H1 R1](#h1r1r2)|:+1:|2.4"|:x:|:x:|:x:||:heavy_check_mark:||QFP64||||
|[H1 R2](#h1r1r2)|:+1:|2.4"|:x:|:x:|:x:|:heavy_check_mark:|||QFP64||||
|[H2M (Mayhem edition)](#h2m-mayhem-edition)|:+1:|3.2"|:heavy_check_mark:|:x:|:x:|||:heavy_check_mark:|QFP100||||
|[H2 (H2 R1)](#h2)|:+1:|3.2"|:x:|:x:|:x:|:heavy_check_mark:|||QFP64||||
|[H2 (maxgeek)](#maxgeek-h2)|:question:|3.2"|:x:|:x:|:x:||||QFP64||||
|[H2 (old OpenSource SDRLab version)](#h2)|:+1:|3.2"|:x:|:x:|:x:|:heavy_check_mark:|||QFP64|||:heavy_check_mark:|
|[H2+ R2](#h2r2)|:+1:|3.2"|:x:|:x:|:x:||:heavy_check_mark:||QFP64||||
|[H2+ R3](#h2r3)|:+1:|3.2"|:x:|:x:|:x:||:heavy_check_mark:||QFP100|:heavy_check_mark:|||
|[H2+ R4](#h2r4)|:+1:|3.2"|:x:|:x:|:x:|||:heavy_check_mark:|QFP100||:heavy_check_mark:||
|[H2+ R5](#h2-r5)|:+1:|3.2"|:x:|:x:|:x:||||||||
|[H3](#h3)|:shit:|2.4"|:question:|:x:|:x:|:heavy_check_mark:|||QFP64||||
|[H3 mini/ H2 Plus](#h3)|:shit:|3.2"|:question:|:x:|:x:|:heavy_check_mark:|||QFP100||||
|[H4](#h4)|:+1:|3.2"|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|||:heavy_check_mark:|QFP100||||
|[H4M (Mayhem edition)](#new-h4m-mayhem-edition)|:heart::+1:|3.2"|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|||:heavy_check_mark:|QFP100||||
|[H4M Pro (Mayhem edition)](#new-h4m-pro-mayhem-edition)|:heart::+1:|3.2"|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|||:heavy_check_mark:|QFP100||||


> [!NOTE]  
> * **Any** versions of H3 are **incompatible** (we will never do support of this hardware), do not buy them as they're scam.  
> * "H2+" and "H2 Plus" are different devices, even if their names sounds similar.


### Legend
- 👍 Compatible
- ❓ Compatibility unknown
- ✔️ Included
- 🚫 Not compatible
- ❤️ Recommended

# HackRF
If you want to support the original creators of the HackRF, we would highly recommend purchasing a GSG HackRF though one of their resellers listed here.
https://greatscottgadgets.com/hackrf/one/

[<img src="https://github.com/user-attachments/assets/a8c4dfe7-6a24-4b9d-beed-34ee9acfd298">](https://greatscottgadgets.com/hackrf/one/)


## FAQ

**Q: Which one should I buy?**  
A: Please refer to the comparison table above.

**Q: Should I buy a pre-assembled unit or buy parts separately and assemble it myself?**  
A: It depends on your skills. If it’s your first time assembling a device, there might be challenges. However, if you want an original/genuine HackRF, buying the parts separately is your only choice.

**Q: How do I know if the device from a specific vendor/store/seller works or is compatible?**  
A: Check the hints at the top of this page and always verify compatibility with the vendor. 


***

## Detailed PortaPack Version Descriptions 
Below are a more detailed look at the different variations of PortaPacks

## H1(R1/R2)
<img src="https://user-images.githubusercontent.com/4393979/162888735-083d4fb5-dfd5-499c-94b1-c0fbbec0fda2.png" height="300">
<img src="https://user-images.githubusercontent.com/4393979/162888869-cc9a45ed-170f-435c-a3c1-43076d0035b2.png" height="300">

### Differences:
* The H1R1 has a WM8731 audio chip
* The H1R2 has a AK4951 audio chip
* Some versions have a touch screen while a lot of the clones do not

## H2
<img src="https://user-images.githubusercontent.com/4393979/162888315-85e7c7da-8bcd-4578-9195-93dd96118560.png" height="300">
<img src="https://user-images.githubusercontent.com/4393979/162888233-c773743c-3231-4b06-b2f1-a5bb9988c66e.png" height="300">


### Differences:
* Bigger touch screen
* Different control/button layout
* Built in battery

## H2M (Mayhem Edition)
[<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/4393979/295532718-8e5b661c-f946-4cee-8b2d-0a615f7715f4.png" height="300">](https://github.com/portapack-mayhem/mayhem-firmware/assets/4393979/8e5b661c-f946-4cee-8b2d-0a615f7715f4)
[<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/4393979/295532482-c4366743-d46a-4155-9758-e99bef734ed6.png" height="300">](https://github.com/portapack-mayhem/mayhem-firmware/assets/4393979/c4366743-d46a-4155-9758-e99bef734ed6)

> [!TIP]
> *Click the images to see them on their full glory*

### Differences:
* Custom PCB built specifically for Mayhem with all the top contributors names silkscreened on the back of it and the Mayhem logo on the front.
* This usually comes with a new crystal clear case so you can see all the beautiful silkscreen art.
* Comes with a built in microphone.
* Has new CPLD code so the reboot button doesn't freeze the device unlike some of the other H2's on the market.

## H2 (old OpenSourceSDRLab version)
![261866889-6a4c7de5-15f2-4119-9329-db76917f9466-b](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/7078c63c-cc35-4636-946c-6f944171d455)
![261866887-e3d853ec-9cc2-4884-aecd-d6697331839f-b](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/316283e6-6696-499b-9da7-54c6cb06c214)


### Differences:
* AK4951 with 3W CS8122S Amplifier chip (INS8002e clone) -- speaker shuts off automatically when headphones plugged in
* NOTE:  Do not enable AK4951 Speaker Output icon on title bar on this model or the AK4951 IC may overheat (CS8122S and AK4951 speaker outputs seem to be tied together on PCB)

## H2+ Unbranded board (circa 2020)


<img src="https://lh3.googleusercontent.com/pw/AP1GczMTY3h3jl70jM_maDYd9bqYAG2PIwyV0TTyHeYI6qf2NILrJOOSzBowBTZQF4xTjsJhweX-dmFsXMRmMuJactgSobWHyz1Ze9s3VWlP3c-g1CxCBzGWSvxXbUXyGeHmqTAKnNWzaLfFh5egdkqJ-jUT_g=w562-h911-s-no-gm?authuser=0" height="300">


<img src="https://lh3.googleusercontent.com/pw/AP1GczP_IAfd4ldbVOOyaeggmbMTRjbzYh7TkSWJH7IEbXJwBfTnbXsHwtvPsKmAlUJ33gekXkIOzYS5czL5HDZOG2rIHlB882J80meLAuzOcfNM7eL0osvw4a6AW4vzDlHQnCj5LC4aNBAdHI8qFqp31lKxIQ=w564-h911-s-no-gm?authuser=0" height="300">

### Differences:

* Different encoder and button layout in front side
* Encoder works in opposite direction
* Other differences yet to be established after further investigation

## H2+ R1


<img src="https://user-images.githubusercontent.com/4393979/162888499-4d780cd0-2ddd-47f0-b465-2c29238af6ad.png" height="300">

### Differences:
* Similar to  H2 in early versions except claim for better TXCO spec(questionable) and board marked as H2+.
* Battery state indicator with 4 leds under Encoder Knob for 25%,50%,75%,100%,flashing while charging, steady when that level full. 

## H2+ R2

<img src="https://user-images.githubusercontent.com/32274981/163668781-3f9beec7-b670-43dd-aa97-b01a63343157.JPG" height="300">


### Differences:
* Similar to  H2+R1 except using the WM8731 Codec and  has an added audio power amp INS8002E. The front face of the board is marked as H2+ as in H2+R1 above.

## H2+ R3

<img src="https://user-images.githubusercontent.com/32274981/163668864-cfddc191-cdf5-418c-b8fd-7d7b16937c02.jpg" height="300">


### Differences
* Similar to  H2+R2 except
* This versions the standard CPLD 5M40ZE64CN5 was  replaced with EPM240T100C5N ( due to cost and supply issues by supplier "OpenSourceSDR Lab") which has caused some issues ( they issued their work around fixes in a version 1.4.3)  and resolved in version 1.5.x due to a lot of hard work.


## H2+ R4

<img src="https://user-images.githubusercontent.com/4393979/170891015-6c9517bf-ee0b-49b9-b7bf-8d9f4049c721.png" height="300">

![IMG_0100](https://github.com/portapack-mayhem/mayhem-firmware/assets/129641948/86ba5a3c-ecdd-485b-b230-16ca1f3ac1cc)

### Differences
* Similar to the H2+R3 except it now uses the AG256SL100 IC as well as the 28 pin QFN WM8731L instead of the 38 pin QFN AK4951. Marked as "PCB v3.6 mmdvm.club". 
* 3W LTK8002D SOP8 Class D amplifier for the speaker (INS8002e clone).
* Power IC IP5306 SOP8.
* Inserting headphone plug doesn't [disable the speaker](https://github.com/portapack-mayhem/mayhem-firmware/wiki/H2-Plus-speaker-modifications).

## H2+ R5
Bascially H2 with internal microphone and a independent power switch (but only pad/hole exist in some of the boards.)  
Community reported it works (including the internal microphone), but other infomation are unknown.

## H3
Uses custom close source firmware. **Not compatible with Mayhem. Do not buy or support as it's a scam**

<img src="https://user-images.githubusercontent.com/1091420/214587249-48608cf2-195e-47a9-aa31-3dd2feb2abea.png" height="300">

This also exists as H2 Plus. Uses custom close source firmware ([Ref.](https://user-images.githubusercontent.com/24917424/198536040-e573b98c-e327-4e69-9448-83cea52b02e3.jpg)). **Not compatible with Mayhem([Ref.](https://user-images.githubusercontent.com/24917424/198536040-e573b98c-e327-4e69-9448-83cea52b02e3.jpg)).

## [H4M (Mayhem Edition)](https://share.hackrf.app/3OFS3N)

[<img src="https://github.com/user-attachments/assets/b393c64a-932b-4e33-818b-3927900c2c71" height="300">](https://github.com/user-attachments/assets/857ba4c0-558b-4f21-bce2-144a4c3bf66d)
[<img src="https://github.com/user-attachments/assets/3ef88b57-28e9-493d-a27f-457746a45e81" height="300">](https://github.com/user-attachments/assets/3ef88b57-28e9-493d-a27f-457746a45e81)




> [!TIP]
> *Click the images to see them on their full glory*

### Differences:
* 🔌 GPIO port! The H4M adds a GPIO port so users can make their own add-ons for the H4M, just like the flipper.
* 🔋 Advanced battery management IC (battery %, voltage, current/draw, etc...)
* 🕹️ Single power on/off switch.
* 🚫 When powered off, the battery will no longer phantom drain.
* 📱 flat design, going back to the iPod style click wheel. (so no more broken buttons and encoders!)
* ⚡ Improved charge speeds.
* 🎙️ Built in mic (and mic switch between internal and external).
* 🖥️ Matte screen.
* 💎 This usually comes with a new crystal clear case so you can see all the beautiful silkscreen art.
* 🛠️ Custom PCB built specifically for Mayhem with all the top contributors names silkscreened on the back of it and the Mayhem logo on the front.

### Where to buy?
[Directly from the manufacturer OpenSourcesSDRLab](https://opensourcesdrlab.com/search/?Keyword=h4m)

**Worldwide - OpenSourcesSDRLab**
* [H4M & HackRF With Type C (R10C)](https://opensourcesdrlab.com/products/h4m-receiver-and-spectrum-analyzer)
* [H4M (with case, speaker and battery)](https://opensourcesdrlab.com/products/mayhem-signature-edition-h4m-portapack-and-transparent-shell-with-speaker-and-2500-mah-lithium-battery)

**Worldwide - AliExpress**
* [H4M & HackRF With Type C (R10C)](https://share.hackrf.app/80OD1K)
* [H4M (with case, speaker and battery)](https://share.hackrf.app/R3DROK)

**US and EU - AliExpress**
* [H4M & HackRF With Type C (R10C)](https://opensourcesdrlab.com/products/h4m-receiver-and-spectrum-analyzer)
* [H4M (with case, speaker and battery)](https://share.hackrf.app/W38X9V)

## _(NEW)_ [H4M Pro (Mayhem Edition)](https://opensourcesdrlab.com/products/hackrf-pro-h4m-pro?VariantsId=10426)

<!-- Temporary: H4M images are used until H4M Pro images are available. -->
[<img src="https://github.com/user-attachments/assets/e443f471-e569-40c8-996b-34b9d99ea6ae" height="300">](https://github.com/user-attachments/assets/e443f471-e569-40c8-996b-34b9d99ea6ae)


### Differences:
* ✨ Includes all the features and improvements of the H4M Mayhem Edition:
  * 🔌 GPIO port for add-ons.
  * 🔋 Advanced battery management.
  * 🕹️ Single power on/off switch with no phantom battery drain when off.
  * ⚡ Improved charging speeds.
  * 🎙️ Built-in microphone with internal/external mic switch.
  * 🖥️ Matte screen.
  * 🛠️ Custom Mayhem PCB with contributor names and Mayhem logo.
* 🔋 Uses a standard, user-replaceable 18650 battery instead of the H4M's 104050 pouch battery.
* 🔊 Speaker and microSD-card slot have been repositioned for easier access.
* 📡 Includes the HackRF Pro, which improves on the standard HackRF One with:
  * 📻 Wider frequency range: 100 kHz–6 GHz.
  * ⏱️ Built-in 25 MHz, 0.5 ppm TCXO.
  * 🔌 USB-C connection.
  * 🛡️ Improved RF shielding and antenna-port surge protection.
  * ⚙️ LPC4330 MCU, iCE40 UltraPlus FPGA, and 32 Mbit flash memory.

### Where to buy?
[Directly from OpenSourceSDRLab](https://opensourcesdrlab.com/products/hackrf-pro-h4m-pro?VariantsId=10426)
