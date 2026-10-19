# Analog TV Receiver

![Analog TV Receiver](https://github.com/portapack-mayhem/mayhem-firmware/assets/3157857/d01129b5-026c-4002-b860-e8d1d147b97b)

> [!NOTE]
> This is an external app. It requires the corresponding `.ppma` file in the `APPS/` folder on the SD card.

The Analog TV Receiver app decodes wideband AM-modulated **PAL** signals in black and white. PAL was the dominant analog television broadcast standard across Europe and much of the world before the switchover to digital broadcasting.

## How it works

Standard PAL video is 768 pixels wide × 625 lines at approximately 6 MHz bandwidth. The HackRF samples at **2 MHz** with 2 MHz baseband bandwidth, which reduces the horizontal resolution to 128 pixels. The app processes 256 samples per callback, yielding 2 lines per call. After 52 callbacks, a full frame of **104 lines × 128 pixels** is assembled in memory. Each of the 104 source lines is then painted twice to produce a **208-line × 128-pixel** image on screen, stretching the image vertically for better proportions.

The resulting image is displayed starting at pixel row 100 on the 240×320 PortaPack screen.

Because only the top half of the original 625 lines are retained (anything above line 312 triggers a new frame), the image represents roughly the top half of the original PAL frame.

## Supported standards

The app supports **PAL** with AM-modulated video only (as used in terrestrial analog broadcasts). NTSC and SECAM are not supported.

> [!NOTE]
> Digital television (DVB-T, DVB-T2, ATSC, ISDB-T) cannot be received with this app. Digital TV standards use OFDM modulation with QAM/QPSK and require complex channel coding (Reed-Solomon, LDPC) and Transport Stream parsing — this far exceeds the processing capacity of the HackRF's M4 baseband processor. The app is designed exclusively for analog AM video.

## Where to find analog TV signals today

Terrestrial analog TV broadcasts have been switched off in most countries (Europe mostly between 2007 and 2012, USA in 2009). The app is therefore primarily relevant for the following use cases today:

- **Amateur TV (ATV):** Radio amateurs operate analog image transmissions on UHF and microwave bands (e.g. 70 cm, 23 cm). This is the most common use case for this app.
- **Analog CCTV cameras:** Older surveillance systems frequently still transmit in analog PAL format, sometimes wirelessly in unlicensed bands.
- **FPV drones and industrial cameras:** Some inexpensive FPV drone cameras transmit analog PAL video on 5.8 GHz or 1.2 GHz.
- **Cable TV:** In some regions outside Europe, analog cable TV still runs alongside digital offerings.
- **Experiments and retro reception:** Test signals, self-built PAL transmitters (e.g. Raspberry Pi composite video via SMA adapter), or historic recordings replayed over RF.

## Known limitations

- **No sync detection.** The app does not detect horizontal or vertical sync pulses, so the image can be misaligned both horizontally and vertically and will drift over time.
- **Black and white only.** PAL color information (the 4.43 MHz color subcarrier) is received but not decoded; the image is displayed in greyscale.
- **No AGC.** There is no automatic gain control. LNA and VGA gain must be adjusted manually to get adequate contrast — this is especially important for AM video since the signal amplitude carries the picture information directly.
- **NTSC and SECAM not supported.**

## Controls

| Control | Function |
|---|---|
| Frequency | Tune to the video carrier frequency |
| LNA / VGA | Gain — adjust manually for best picture contrast |
| X-corr (0–128, default 10) | Horizontal offset correction — adjust to re-align the image left/right when it appears shifted |

The X-corr field is navigated to with the directional buttons and adjusted with the encoder dial.

## Gain advice

Because this is an amplitude-modulated signal, gain is critical. If gain is too low the image appears very dark; if too high it clips and the image washes out. Start with LNA 24, VGA 16 and adjust both until the picture has visible contrast.