<!-- Optional: add a screenshot after first stable release -->

<img width="800" height="564" alt="meteor-m2en" src="https://github.com/user-attachments/assets/6e6710e5-e036-4a98-98cd-fea26e48b5d5" />

**Meteor LRPT** is an **external receive app** for **Meteor M2-series** satellites that transmit **LRPT** (Low Rate Picture Transmission) near **137 MHz**. It runs the radio in a **wideband capture–style** configuration, decodes the LRPT bitstream on the **M4 baseband** processor, and can **record** decoded data to the SD card. Optional **MSU-MR** processing (visible imaging) runs on the **M0** application core and can write **BMP** files and a small **LCD preview**.

# Where to find it

**Receive → Meteor LRPT**


> [!NOTE]
> **Pull** : https://github.com/portapack-mayhem/mayhem-firmware/pull/3175
> **Tools** : https://github.com/user-attachments/files/27760145/tools_meteor_lrpt.zip
> **Binaries** : https://github.com/user-attachments/files/27731032/hackrf_usb.zip

# Antenna and frequency

* **Meteor M2-3 / M2-4** LRPT is commonly received near **137.9 MHz** (primary). A **backup** downlink near **137.1 MHz** may appear on some passes; check current satellite information for your pass.
* The repository includes a Freqman preset file you can copy to the SD card: `sdcard/FREQMAN/METEOR_LRPT.TXT`. See [Freqman manager](Freq-manager) and [SD Card Content](SD-Card-Content).
* **these might help 👇🏻**

<img width="1707" height="459" alt="antennas" src="https://github.com/user-attachments/assets/29289c6c-a9f3-47b2-8d7e-e12ac5a4c5b7" />
<img width="2048" height="380" alt="sawfilters" src="https://github.com/user-attachments/assets/f6385419-66c4-4f33-89ee-d58753d6b283" />

# Main controls

* **Frequency:** Centre frequency for LRPT (keypad or encoder; stored with app settings if enabled globally).
* **RF Amp / LNA / VGA:** Same idea as other receivers. If nothing decodes, avoid overdriving the front end. See [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues) for gain behaviour.
* **Volume:** Audio level for the receiver UI (same pattern as other RX apps).

# Troubleshooting

* **No decode / flat waterfall:** Check frequency for the **current** satellite, **RHCP** antenna, **gain** (not clipped), and **M2-x / Interlv / 80k** toggles vs the pass you are actually receiving.
* **Recording drops / yellow REC:** Reduce SPEC bandwidth, use a faster SD card, shorten cable, or record **C8** instead of wider IQ where applicable (see [Capture](Capture)).
* **Interleaved pass but garbage CADU:** Confirm whether the pass is truly **interleaved**; confirm SOFT block size matches mode (**8192** vs **16384**). When in doubt, archive **IQ** with [Capture](Capture) and compare offline using repo tools under `tools/meteor_lrpt/`.
* **MSU-MR never writes BMP:** Confirm **CADU** file path, that CADU ASM/lock is sane, and that JPEG is **baseline** (not progressive). Inspect `drop_bits` per `G4_PRODUCT.md` in the repo.

# Decoder options (checkboxes)

* **M2-x:** Select when receiving **Meteor M2-x** style LRPT .
* **Interlv (interleaved):** **M2-x interleaved** mode. When enabled together with a working **M0 deinterleave** path, the firmware uses the dual-stream deinterleave + dual Viterbi pipeline.
* **Diff:** NRZ-M / differential decoding option (matches the SatDump “diff” style path for the selected mode).
* **Leg.corr:** Legacy correlator path (for non–M2-x style receptions).
* **80k sym:** Use only when you intentionally capture **80 ksymbol/s** test modes. Leave **off** for normal **72 ksymbol/s** passes.
* **BMP:** Saves a **thin grayscale strip** driven by **JPEG preview heuristics** on M4 — **not** a full MSU-MR colour product. For real images, use **MSU-MR** below.

# Waterfall / bandwidth

The app expects a **SPEC**-style bandwidth suitable for LRPT (commonly **150 kHz** or **250 kHz**). Very wide bandwidths increase CPU and **SD** load; if recording glitches, reduce bandwidth or use a faster SD card (same idea as [Capture](Capture) yellow **REC** warnings).

# Recording — CADU and SOFT

Two **record** rows may appear (similar pattern to other apps using [Capture](Capture) / record views):

* **CADU row:** Records **post–Reed–Solomon** **1020-byte** CADU frames (logical frame length used by the decoder). Raw bytes use extension **`.C8`** on SD (aligned with Mayhem **raw S8** recording conventions).
* **SOFT row:** Records **signed 8-bit soft symbols** (I/Q pairs) for offline comparison or advanced debugging.

**Critical:** Do **not** enable **CADU** and **SOFT** recording at the same time. The baseband exposes **only one** capture stream at a time; enabling both can conflict.

**Block sizes for SOFT files**

* **16384 bytes** per write: legacy / M2-x **non-interleaved** soft path.
* **8192 bytes** per write: **M2-x + Interleaved** when the M0 IPC + deinterleave path is active.

# SD card layout

* Recordings and products default under folder **`/LRPT`** on the SD card.
* Ensure the card is formatted and has free space before long passes. See [How to Format SDCard](How-to-Format-SDCard) if needed.

# MSU-MR (G4) — images on SD

When **MSU-MR** is enabled, an **M0 worker** scans CADU data, extracts **MSU-MR** JPEG payloads where possible, decodes **baseline JPEG** with embedded **TJpgDec**, and writes **24-bit BMP** files such as:

` /LRPT/msumr_<apid>_<timestamp>.bmp `

**Operator workflow (short)**

1. Record **CADU** with the **CADU** record row during the pass (recommended for a clean archive).
2. Default **tail file** path for the worker is **`/LRPT/g4_cadu.C8`** — point it at your CADU capture (same **`.C8`** convention as the CADU recorder), or adjust the **Path** in the app if your filename differs.
3. Enable **MSU-MR** and watch the status line counters (`c` / `j` / `b`, drops, optional **`ro`** ring overflow count when **Live** is on).
4. **Live:** Optional path where **post-RS CADU** is pushed from M4 into a **small fixed RAM ring** for near–real-time decode. If M0 cannot keep up, **overflow** is counted and some CADUs are **dropped** by design (lossless archival still prefers **record to SD first**).
5. **Img** and **^** / **v:** Optional paging viewer over the **last** decoded BMP (read-only file access).

Progressive JPEG is **not** supported (decoder limitation).

# Related wiki pages

* [Capture](Capture) — IQ recording, bandwidth, **REC** colour warnings, `.C16` / `.C8` context  
* [C16 format](C16-format) — complex sample file layout when you also archive IQ  
* [Freqman manager](Freq-manager) — loading `METEOR_LRPT.TXT` 
* [Receive Quality Issues](Help!-Im-not-receiving-anything!---Receive-Quality-Issues) — gain and overload  
* [SD Card Content](SD-Card-Content) — folder layout on SD  
* [External apps informations](External-apps-informations) — how external apps load baseband images  