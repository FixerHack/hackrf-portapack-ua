![image](https://github.com/user-attachments/assets/c4aa3bf3-0ea2-4573-8de2-9aea4dcfcede)

# Introduction

The Audio App is the main way that signals can be heard and seen in detail. Three types of decoders are provided for audio modulated signals and a spectrum view of the signals. The user interface has the ability to view and change:
 
## Controls 

* **SPEC:** Display a Spectrum of the received signal and allow viewing of 10MHz of RF Spectrum, centered on a configurable frequency, with 5MHz above the frequency and 5MHz below.

* **AM:** Demodulate and Record RF Signals modulated using the Amplitude Modulation scheme. It can demodulate Double-Sideband AM (ITU Designation: A3E) and both Lower-Sideband and Upper-Sideband Single-Sideband AM (ITU Classification: R2E, H3E, J3E) signals.

* **NFM:** The Narrow Band Frequency Modulation decoding ITU Classification: FM3

* **WFM:** The Wide FM Receiver is a Sub-Application of the Audio Receiver Application. Its purpose is to Demodulate and Record RF Signals modulated using the Frequency Modulation scheme. It can demodulate mono and stereo Wide FM signals of 200KHz bandwidth. Such signals are commonly used for VHF FM Broadcast services.

* **AMFM:** Here in that Audio App we can tune , and RECORD the APT signal from a HF-Weather Fax map Broadcasting Station into audio_format_APT_file.wav ,mainly for investigation , debugging , and check signal  levels (signal strenght , saturation , filters check ,...). But we have also in Mayhem fw ,  another external receiver [Wefax App](https://github.com/portapack-mayhem/mayhem-firmware/wiki/WeatherFax) (based on that AMFM demodulation engine) , more convenient to the user, because it combines both things : (that APT demodulation and the additional  display weather map to the LCD (in low resolution) able to record the decoded weather map into a bmp file (in full received resolution. -much better than the displayed in the low resolution screen) 
We are combining in that demodulation , two consecutive demodulations. First RF USB audio baseband demodulation , and later demodulating the FM subcarrier audio baseband  tones.That modulation , it is commonly used in Wefax (HF Weather Fax transmissions) . It demodulates APT signal of the HF weather fax maps.  , and  sends the demodulated  low scan map  APT signal in parallel to the speaker (just for our audio tuning reference ) and it can be also  RECORDED to the SD card , through audio.wav file (SR =12KHZ, audio mono track). 
Inside audio baseband spectrum , there is a sub-carrier audio tone , modulated in FM with the low scan APT image map signal .
(Audio Baseband with f_subcarrier fsc (1900Hz)  FSK mod +-400Hz ; Shift  White pixel  +400 Hz = 2.300 Hz , Shift  Black pixel -400 Hz  = 1.500 Hz). For better usability , in both Applications (this Audio App AMFM mode, and Wefax App) we are internally applying a proper tune-offset . Therefore you just need to tune the official published Weather Fax frequency transmitter. (example 3.855 Khz ,7.880 Khz , 8.040 Khz ,...). 

* **FMAM:** Here in that Audio App we can tune , and RECORD the APT signal 137 Mhz , from the discontinued NOAA Analog saltellite weather image service. Fax image Broadcasting Station into audio_format_APT_file.wav ,mainly for investigation , debugging , and check signal  levels (signal strenght , saturation , filters check ,...). But we have also in Mayhem fw ,  another external receiver [NOAA APT App](https://github.com/portapack-mayhem/mayhem-firmware/wiki/NOAA)

Hackrf has poor sensitivity to receive directly those HF Wefax signals, (mainly broadcasted in HF band : 3 Mhz to 16 Mhz)
Normally we should add to the Hackrf receiver a front up-converter with better HF filtered pre-amplifiers, and a reasonable good enough HF antenna.
WEFAX's format is a derivative of the [Automatic Picture Transmission (APT)](https://www.sigidwiki.com/wiki/Automatic_Picture_Transmission_(APT)) originally developed for transmission from the polar satellites of the USA.
WEFAX has 60, 90, 100, 120, 180 and 240 LPM (Lines per minute) speeds, and two IOC (Index of Cooperation) modes, IOC 576 and IOC 288. Most weather forecasts are sent in IOC 576 , 120 LPM . Our initial target is WEFAX-IOC576 standard. https://www.sigidwiki.com/wiki/WEFAX.
Here you can see the actual Worldwide Weather fax HF Stations with his frequencies , and exact GMT map transmission time . 
https://weatherfax.com/stations/


The Key Items on the App that can be seen or selected with the cursor and changed with the encoder knob are:

* **Title bar:** The usual Items may be changed and displayed.

* **Mode:** On the line below title bar is the demodulation mode AM, NFM, WFM, SPEC. When either of these are selected it will bring up a secondary set of relevant items on the line below. These are discussed in secondary items below.

* **Frequency:** The Centre frequency of the demodulation band.

   > Note 1 : From Frequency field, you can move down to the below Step field , to adjust your best suitable Freq-step, according to your
 needs.

   > Note 2 : If you have load/save App Settings from SD card enabled, it will continue to use what it was last set at. And you can always edit the file in the SD  card, /SETTINGS/rx_audio
.ini and edit the step size there, according to your needs in that App.

   > Note 3 : Additionally , to be more user friendly ,  from version 1.7.4+ holding  in the Select button on the Frequency field for a second until a digit turns blue, then you can use Left/Right select which digit you'd like to adjust, and then you can use the Encoder Dial to adjust any digit up/down by 1 to tune more precisely. (Press Select again to exit this tuning mode. 
  
* **Gain:** Settings are shown in order of LNA(IF) (0-40) and VGA (Baseband Gain) (0-62). When either of these are selected in the secondary line the AMP setting is shown and can be as either set to  0=0db or 1=14dB.

* **Signal Display:** The three coloured displays are top to bottom RSSI(Red/Blue) with an average marker in the line. Next is the Baseband signal and last the Audio level.

* **Volume:** The Last item on this line is the audio volume control (O-99) that is used with either headphone or speaker if fitted.

* **Secondary Information:** This line provides associated information for the following items these are:

    * **AM:** Bandwidth settings of DSB 9k, DSB 6k, USB+3k, LSB-3k, CW. The Spectrum view can go from  +/-90khz till +-11k25 depending on the selected zoom (x1,x2,x3,x4). It has also applied the Sliding frequency feature . There is also an **SQ** field, shown as `SQ  /99`, for an optional channel-power squelch (range 0-99, **default 0 = off**). This is separate from the NFM squelch. When set above 0, the audio is muted while the channel power stays below the threshold (about -80 dBFS at 1, rising to about -20 dBFS at 99), which silences an idle AM channel between transmissions.
    * **NFM:** Bandwidth Settings of 16k,11k,8k5. Note there is no setting for the more common 6k5 used in European Spectrum plans. Next item is SQ: which is shown in the format of 40/99 allow the noise squelch point to be set Between 0-99. Typically, around 40-50 is a good threshold. It has also applied the Sliding frequency feature .
    * **Gain:** The RF Amp settings. The Spectrum view is +/-20k.
    * **USB+FM:** It is usually  used to demodulate Wefax (HF Weather fax transmissions) , demodulating the signal in two steps,  first demodulating the tuned  RF signal in USB , extracting audio tones. And then demodulating again those FM modulated subcarrier audio tones,  to extract APT low scan weather fax map signal. (that signal can be recorded into audio.wav file ).
For a correct demodulation ,currently  we need to tune that published frequency , (in our application , you do not need to apply any usual  - 1.900Khz offset . The -tuning offset ,  is already applied internally). So we have to just tune the  (published) Wefax Station frequency directly . 
    * **FM-AM:** It was used to demodulate NOAA analog APT  Weather Image satellite in 137 Mhz band, demodulating the signal in two steps,  first demodulating the tuned  RF signal in WFM (38KHZ BW aprox)   , extracting AM carrier modulated with APT (2khz BW aprox)  .  And then demodulating again this AM modulated subcarrier  to extract APT low scan Image weather satellite signal. (that signal can be recorded into audio.wav file ).

* **Record button:** press to record a file, press one more time to stop the record.

* **Marker Frequency** Just below REC Icon we have a marker Frequency field input (0 Hz) , that we can adjust from 0..48kHz range with the knob rotary encoder, with 200 Hz step jumps. It will move a short vertical red line pointer cursor across the Multiplex FM demodulated baseband  FFT spectrum graphic. It could be useful to see and confirm the exact frequency of those spectrum peaks, like the below picture , showing 19Khz pilot carrier tone from a usual Stereo FM Broadcasting.

* **Waveform display** if you get down the marker frequency and put focus on the wafeform display, you can disable it with a single click

* **Frequency shift** if you get down the Waveform display or just touch the screen, you'll enter in the frequency shift mode. A flashing red dot will indicate the next position. Use rotary encoder or click on the screen, and press enter to set the new frequency.


Note : All AM modes (DSB 9K, DSB 6K, USB, LSB, CW) and AMFM mode has the option to expand the waterfall, selecting **ZOOM x1** / **ZOOM x2** / **ZOOM x3** / **ZOOM x4**  , but in addition,  AM modes has also implemented Slider Frequency feature.

AM MODES

<img width="928" height="289" alt="image" src="https://github.com/user-attachments/assets/00711f36-d1a7-41d5-bbd0-4e42a1e0628e" />

AMFM (Wefax)

<img width="855" height="286" alt="image" src="https://github.com/user-attachments/assets/f36cd642-492c-4a2a-923c-730b325c74ee" />


Here in that Audio App we can tune , and RECORD the APT signal into file.wav ,mainly for investigation and check signal  levels (signal strenght , saturation , filters check ,  debugging). 
      
![image](https://github.com/user-attachments/assets/6fa91268-405c-46bd-9a7a-ed1dff001ef5)

(as example, that weather map, was decoded directly from a weather HF Broadcasting station,  by the other Wefax App)
![image](https://github.com/user-attachments/assets/58acad5c-5abe-4b2b-858f-eb8aed06a228)

### **WFM**

There are three option filters in that Secondary settings: 
1. 200k ,the original filter for commercial FM stations with soft transition, 
2. 180k with sharp transition, for also commercial FM broadcast station, specially useful to improve demodulated S/N in around 6 to 8 dB in weak signals.
3. 40k with also sharp transition, for supporting NOAA APT weather satellite reception in 137 MHz . (that filter is too narrow for WFM with 75khz delta deviation and can produce audio distortion in the demodulated sound). The Spectrum view is +/-100k with a marker That may be changed (though seem the incorrect value).
 
> ![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/86470699/88ef7389-d7c0-47a8-84ed-05d836879af5)

### **SPEC**

The spectrum Secondary Items allows the view of the RF spectrum with different setting for maximum bandwidth shown:
            
1. 20M with markers at +/- 5M
2. 10M with markers at +/- 3M
3. 5M with markers at +/- 2M
4. 2M with markers at +/- 500k
5. 1M with markers at +/- 300k
6. 500k with markers at +/-200k

The next item is the setting of the bin sizes used for the waterfall (0-63) with “0” being the minimum information being the fastest display and “63” the maximum information collected the slowest display. Adjust to give a balance of speed and information seen. 

#### Calibration

And next right to that field ,while you are still in SPEC mode,  you will see the Rx_IQ_CAL field. It actually can improve (8 to 10 dB's from worse CAL point to the best one ) the receiver Image Reject Ratio (IRR) only in the Receiver Applications that are using Zero IF-frequency tuning ,like this SPECTRUM mode.  This calibrated value will be stored in the SD card , /settings/rx_audio.ini .

To calibrate it , you will need to try to find some clean isolated continuous air carrier signal (please make sure that it is a real air signal, not internal harmonic residual interference clock beats)  , and try to tune it , (for example,  to the right of the positive frequencies ). Select properly the SPEC BW to try to isolate that air carrier signal (in below example , I selected BW = 2 Mhz).
 Then, to make slightly more visible the bare Image mirror frequency -that appears in the other symetric  left part screen.-, you will need to start set up CAL to 0 (min). Then , you will need to adjust AMP , LNA and GAIN to receive strong enough signal to the right part  (but at the same time , not so strong to not produce intermodulations , otherwise re-adjust again decreasing AMP, LNA, GAIN) , and not so weak , till just getting the carrier +freq. clean (desired carrier signal) , and its bare visible Image mirror Signal (in the other symetrical -xx mirror freq . (unwanted Image signal to be minimized) .  Then, when you got similar situation as left below picture, you can start  adjusting  Rx IQ phase CAL till minimizing the received Image "mirror" signal (as in the middle  below picture).

That below example is calibrating H2+ old r6 version (max2837) that has 31 steps ,(Note , using Hackrf r9 (max2839 ,you will have 64 steps)

![image](https://github.com/portapack-mayhem/mayhem-firmware/assets/86470699/84dc2b51-e265-40aa-a0b8-fb8d9270e6b3)

### NFM

* **CTCSS:** This Continuous Tone Coded Squelch System is a display at the end of the secondary information line. It is used by many systems and standardised by EIA/TIA, with a description [here.](https://en.wikipedia.org/wiki/Continuous_Tone-Coded_Squelch_System ) In the NFM mode in Audio app, the tone field is increased from 11 to 14 characters.
Now , the CTCSS tone frequency and CTCSS code numbers are displayed at once (if a matching freq was found in the tone_key table). See the Annex to this document below. It should be noted that most of the time the display is jumping around and only clearly displays the received tone when there is a gap in the voice and the Signal is of good quality. 

* **Record:** The record button if selected will show the record file name, % of the SD Card used, and at the end of the line is the total recording time available left on the SD card and this decrements when recording. The file name of the recorded 16-bit mono WAV file includes the date, time, and radio tuning frequency.  The WAV file sampling rate depends on the receiver mode; 48KHz for WFM, 24KHz for NFM, or 12KHz for AM.

## CTCSS Tone List

	None      0.0 
	0 XZ      67.000 
	1 WZ      69.400 
	2 XA      71.900 
	3 WA      74.400 
	4 XB      77.000 
	5 WB      79.700 
	6 YZ      82.500 
	7 YA      85.400 
	8 YB      88.500 
	9 ZZ      91.500 
	10 ZA      94.800 
	11 1ZB      97.400 
	12 21Z      100.000 
	13 1A      103.500 
	14 1B      107.200 
	15 2Z      110.900 
	16 2Z      114.800 
	17 2B      118.800 
	18 3Z      123.000 
	19 3A      127.300 
	20 3B      131.800 
	21 4Z      136.500 
	22 4A      141.300 
	23 4B      146.200 
	24 5Z      151.400 
	25 5A      156.700 
	40 --      159.800 
	26 5B      162.200 
	41 --      165.500 
	27 6Z      167.900 
	42 --      171.300 
	28 6A      173.800 
	43 --      177.300 
	29 6B      179.900 
	44 --      183.500 
	30 7Z      186.200 
	45 --      189.900 
	31 7A      192.800 
	46 --      196.600 
	47 --      199.500 
	32 M1      203.500 
	48 8Z      206.500 
	33 M2      210.700 
	34 M3      218.100 
	35 M4      225.700 
	49 9Z      229.100 
	36 --      233.600 
	37 --      241.800 
	38 --      250.300 
	50 0Z      254.100 
	Axient 28kHz      28000.0 
	Senn. 32.768k      32768.0 
	Senn. 32.000k      32000.0 
	Sony 32.382k      32382.0 
	Shure 19kHz      19000.0 
