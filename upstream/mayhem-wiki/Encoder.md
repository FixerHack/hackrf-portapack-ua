> [!NOTE]  
> This section is mostly talking about H2

Encoder for H2/H2+ uses a [30-step EC11 encoder](https://www.aliexpress.com/i/1005002905424756.html) with push button and shaft length of 12.5mm.  
(For H4M click wheel, try [ANO Directional Navigation and Scroll Wheel Rotary Encoder](https://www.adafruit.com/product/5001))

A short press of the push button turns on the PortaPack; a long press or two short presses turns off the PortaPack.  If no click is felt when the knob is pressed, there may be insufficient clearance between the knob and the case, in which case some padding may be added inside the knob shaft.

A malfunctioning rotary encoder may sometimes work better if the knob is pressed slightly to the left when rotating.  Make sure that the Portapack is running firmware version 1.7.1. or later, which improves handling of glitchy switch contacts.  Encoder dial sensitivity can also be modified in Settings.

## Plastic knob

Depending on the shaft of your encoder, you can use [diverse knobs](https://www.aliexpress.com/item/1652540985.html):

![image](https://github.com/user-attachments/assets/cd117b4e-ba62-4515-8b44-4b492b917e67)

## Encoder Replacement on PortaPack H2

### Disassemble the device
1. Unscrew the screws and SMA connector rings.
2. Pull apart the case and carefully separate the PortaPack from the HackRF by gently pulling upwards to disconnect the pins.
3. Disconnect the speaker and battery.

### Removing the Encoder
![image](https://github.com/user-attachments/assets/dc82574a-1c6c-4c69-84f0-0f0b6f5060c1)

The encoder is mounted in a way that makes it difficult to desolder due to pin placement. 
If you are having trouble with this, try the following technique:

1. Use a pair of tin snips to cut the encoder’s leads and remove the encoder.
2. Apply flux to the solder pads.
3. Carefully heat each pad with a soldering iron, one by one, to remove the clipped leads. This approach reduces strain on the pads and lowers the risk of tearing up the traces.
> [!WARNING]  
> The upper-most pin is close to the screen, take care not to scorch it with your soldering iron.

### Installing the Replacement Encoder

The replacement rotary encoder will likely have long leads designed for through-hole mounting. However, the PortaPack uses surface mounting for this component, so the leads will need to be trimmed down. Here’s how to do it:
> [!NOTE]  
> Correct lead length is important to avoid clearance issues when reassembling the case.

1. **Trim the Leads:** Shorten the encoder leads so that they are approximately flush with the body of the encoder. This will ensure that the encoder sits stably and doesn’t increase the height of the assembly.
2. After trimming, solder the encoder on the PCB, taking care to align it correctly before soldering.
3. After soldering each pin, do a visual inspection to ensure there is good electrical contact.

### Reassembly

Once the new encoder is in place, follow the disassembly steps in reverse to reassemble your PortaPack.
