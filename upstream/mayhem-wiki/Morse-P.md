<img width="241" height="323" alt="image" src="https://github.com/user-attachments/assets/926a928f-e8d3-446b-81f9-5c8350821a8c" />

Morse Practice is a Morse code keying trainer. It lets you practise sending Morse code by pressing and holding a key button, then decodes what you entered and displays the corresponding character. Audio feedback plays a tone through the speaker while the key is held down.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

* **KEY button** (centre of screen): Hold to key — release to decode. Works with both the touchscreen and the Select hardware button.
* **CLR button**: Clears the decoded text display.
* **Volume**: Audio output level for the keying tone.

# How it works

The app measures the duration of each key press and gap:

* A short press is decoded as a **dit (·)**
* A long press is decoded as a **dah (−)**
* A gap between presses ends the current symbol and looks it up in the Morse table
* The dot/dash threshold is determined automatically from your keying rhythm using a statistical split of recent pulse durations

The current dot-dash sequence is shown on screen, and the decoded character appears below it when the inter-character gap is detected. Decoded characters accumulate in the scrolling text area below.