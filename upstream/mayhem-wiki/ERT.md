![image](https://github.com/user-attachments/assets/c0120d8a-d081-4301-8a0b-28402b771727)

# Introduction

[Encoder receiver transmitter](https://en.wikipedia.org/wiki/Encoder_receiver_transmitter) (ERT) is a packet radio protocol developed by Itron for automatic meter reading of water, gas and electricity. The system uses OOK short range radio which is transmitted in the unlicensed 902-928 MHz ISM band, so that meters can be read from a passing vehicle. This is mainly used in USA. The data is not encrypted, and does not have functions to enable full control. The system is not as advanced as a smart meter and lacks the control or security in the data transferred. Supported message protocols are IDM, SCM, and SCM+.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

# Controls

The Key Items on the App that can be selected with the cursor and changed with the encoder knob are:

* **Title bar:** The usual Items may be changed and displayed.
* **Frequency:** The default frequency of 911.6 MHz can be modified in newer firmware (the ISM band is commonly ~902 MHz to 928 MHz).
* **Gain:** Setting are shown in order of AMP 0=0db or 1=14dB, LNA(IF) (0-40) and VGA (Baseband Gain) (0-62).

# Indications

Fields displayed in the App are as follows:

* **ID:** The meter ID in decimal format. Should match the number or barcode printed on the physical meter.
* **Ty:** The packet type — one of `IDM`, `SCM`, or `SCM+`.
* **Consumpt:** The meter consumption reading value.
* **Tamp:** Tamper flags. For SCM type meters the tamper flags are shown as two single-digit values (physical/encoder tamper flags respectively). For SCM+ or IDM type meters the tamper flags are shown as a 4-digit hexadecimal value. Note: for IDM packets, bits 32–47 of the tamper flags are not displayed due to screen width limitations.
* **Ct:** The count of the number of readings received with the same meter ID. Displayed as `++` if the count exceeds the field width.

The PortaPack ERT receiver monitors approximately 2.5 MHz centered around 911.6 MHz. It does not implement channel filters, so sensitivity is reduced in exchange for monitoring more simultaneous "channels".

# Logging

If a FAT-formatted micro SD card is present when this mode is entered, the receiver will log received packets to a file named `LOGS/ERT.TXT`.

Each log entry is one line with the following format:

```
YYYYMMDDHHMMSS FREQUENCY TYPE data/errors ID:meterID
```

* `YYYYMMDDHHMMSS` — timestamp in sortable format
* `FREQUENCY` — the tuned frequency in Hz at the time of reception
* `TYPE` — packet type: `IDM`, `SCM`, or `SCM+`
* `data/errors` — Manchester-decoded data bits, a `/`, and a per-bit Manchester coding error indicator (`1` = error on that bit)
* `ID:meterID` — the decoded meter ID in decimal

Received data that looks like it might be a packet (based on the sync bits) but has an invalid checksum will not be shown on screen, but will still be written to the log file for debugging purposes. Adjusting the gain values may help reduce these invalid packets.