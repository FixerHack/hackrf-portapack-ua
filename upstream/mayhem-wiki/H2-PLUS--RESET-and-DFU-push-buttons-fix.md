# Fixing RESET & DFU issues on old PortaPack H2+ PCB v3.6

This procedure fixes two issues found on some old **PortaPack H2+ PCB v3.6** units:

- The **RESET** push button freezes the device instead of resetting it.
- The **DFU** push button does not work correctly with current Mayhem firmware.

The problem can be fixed by updating the PortaPack CPLD firmware.

> **IMPORTANT:** This procedure has been validated only on the specific hardware configuration described below.
>
> Do not use it on other PortaPack revisions unless they have been independently verified as compatible.

---
## 1. Firmware prerequisite

Before starting this procedure, make sure your PortaPack is running a **recent Mayhem firmware version** that provides the USB serial console CPLD commands used in this guide.

You can do it , connecting your device to Mayhem Hub through USB  ,https://hackrf.app/
 just updating your  Mayhem fw with latest available nightly .

<img width="706" height="366" alt="image" src="https://github.com/user-attachments/assets/31d7e8d8-51f2-4f1d-8a86-4a793c0fef86" />


## 2. Check that your hardware matches

Before doing anything, visually check that your PortaPack is:

- **PortaPack H2+**
- **PCB version 3.6**
- CPLD package: **QFP100**

<img width="588" height="356" alt="image" src="https://github.com/user-attachments/assets/84c175f0-b8f0-45f3-9445-beecaf226cc9" />

Then connect the PortaPack to **Mayhem Hub** and open the USB serial console.

Run:

```text
cpld_info portapack
```
<img width="794" height="120" alt="image" src="https://github.com/user-attachments/assets/a211b5d9-f3f6-4123-8529-91184676d2d3" />

The affected units validated with this procedure reported:

```text
CPLD IDCODE: 0x00025610
CPLD Model: AGM AG256SL100
CPLD firmware checksum: 0x17DDE5B1
```

Proceed only if **ALL** of the following conditions match:

**PortaPack H2+ → PCB v3.6 → AGM AG256SL100 (QFP100) → original CPLD checksum `0x17DDE5B1`**

If any of these conditions do not match, **do not use this procedure**.

---

## 3. Get the CPLD programming file

Use the official Mayhem CPLD programming file (in the official remote Mayhem GitHub or in your local fork repo):

```text
hardware/portapack_h4m/CPLD/Supra/portapack_h4m_cpld.prg
```

File name:

```text
portapack_h4m_cpld.prg
```

### Verify the file on your computer

Before uploading it to the PortaPack SD card, verify its SHA256, (using any of those below three options).

1-) Linux:

```bash
sha256sum portapack_h4m_cpld.prg
```

2-) Windows PowerShell:

```powershell
Get-FileHash .\portapack_h4m_cpld.prg -Algorithm SHA256
```
3-) Windows Bash Shell:

```Bash Shell
sha256sum portapack_h4m_cpld.prg
```
Expected SHA256:

```text
210c891c0207ea705fce6282c592d91f421c18e306aa91d8bd3af57d41cc0977
```

**Do not continue if the SHA256 does not exactly match.**

---

## 4. Upload the PRG file to the SD card

Using **Mayhem Hub**, upload (clicking second icon starting from left) :

<img width="475" height="163" alt="image" src="https://github.com/user-attachments/assets/561c0aa3-203e-4fa7-8d31-be54665b44dd" />

```text
portapack_h4m_cpld.prg
```

to the **root directory of the PortaPack SD card**.

After uploading, verify that the file is present:

```text
ls /
```

You should see:

```text
portapack_h4m_cpld.prg
```

### Verify the SD uploaded file (that it was correctly uploaded without any corruption)

Use the Mayhem Hub serial command:

```text
crc32 /portapack_h4m_cpld.prg
```

Expected CRC32:

```text
0x050D8A24
```

**Do not continue if this value does not exactly match.**

---

## 5. Important checksum clarification

Do not confuse these three different checksum values:

| Check | Expected value |
|---|---|
| PRG file SHA256 | `210c891c0207ea705fce6282c592d91f421c18e306aa91d8bd3af57d41cc0977` |
| Uploaded PRG file CRC32 | `0x050D8A24` |
| CPLD checksum after programming | `0x20F48814` |

> **WARNING:** The original factory CPLD firmware with checksum `0x17DDE5B1` cannot currently be restored from a simple CPLD readback/dump.
>
> Do not continue unless the board revision, CPLD model/IDCODE, original CPLD checksum, PRG SHA256 and uploaded-file CRC32 all exactly match the values documented above.

---

## 6. Program the CPLD

Run:

```text
cpld_write portapack eeprom portapack_h4m_cpld.prg
```

The programming process should report:

```text
CPLD IDCODE: 0x00025610
CPLD Model: AGM AG256SL100
Reading file...
Magic found: 3397A006
Writing data to CPLD...
New CPLD firmware checksum: 0x20F48814
```

> **WARNING:** Do not disconnect USB power, press RESET/DFU, remove the SD card, or otherwise interrupt the device while CPLD programming is in progress.

---

## 7. Reconnect Mayhem Hub and verify the CPLD

After CPLD programming has completed, **reconnect Mayhem Hub to the device** before issuing further serial commands.

Then run:

```text
cpld_info portapack
```

Verify:

```text
CPLD IDCODE: 0x00025610
CPLD Model: AGM AG256SL100
CPLD firmware checksum: 0x20F48814
```

The CPLD update is now complete.

---

## 8. Test RESET and DFU

### RESET

Press the RESET push button.

The PortaPack should now reset and boot normally instead of freezing.

A short visual delay before the boot sequence is normal. The LCD retains its previous screen contents while the MCU resets; the display changes once the MCU initializes the LCD again.

### DFU

Test the DFU push button using current Mayhem firmware.

The DFU procedure should now operate normally without requiring USB power to be disconnected.

---

## Results

Before the CPLD update:

```text
CPLD checksum: 0x17DDE5B1

RESET: FAIL
DFU:   FAIL
```

After the CPLD update:

```text
CPLD checksum: 0x20F48814
Magic:         0x3397A006

RESET: PASS
DFU:   PASS
```

The DFU signal was also electrically checked before and after the update.

Before the update, the released DFU signal showed an incorrect/marginal LOW level of approximately **1.1–1.2 V**.

After the update, clean logic levels of approximately **0 V LOW / 3.2 V HIGH** were measured, with no abnormal continuous current through R30.

---

## Validation

This procedure was independently tested and validated on **two PortaPack H2+ PCB v3.6 units**, both equipped with:

```text
AGM AG256SL100 (QFP100)
Original CPLD checksum: 0x17DDE5B1
```

The two PortaPacks were installed on:

- HackRF One **r6**
- HackRF One **r9**

After updating both units to CPLD checksum `0x20F48814`:

- RESET works correctly.
- DFU works correctly.
- General PortaPack functionality was tested.
- No functional or RF degradation was observed.

---

## Background

This CPLD image and programming method were previously developed and tested by Bernd Herzog and JLynx on an older H2/H2M as part of the CPLD reset fix.

See **[Mayhem PR #2401](https://github.com/portapack-mayhem/mayhem-firmware/pull/2401)** for the original Bernd development/reference.

Bernd has subsequently reconfirmed that his unit still contains CPLD checksum `0x20F48814` and that RESET and DFU work correctly with current Mayhem firmware.

Additional technical investigation, oscilloscope measurements and before/after electrical results are documented in **[Mayhem issue #3289](https://github.com/portapack-mayhem/mayhem-firmware/issues/3289)**.

---

Special thanks to **JLynx and Bernd Herzog** for their invaluable technical support, and to **ChatGPT** for assisting throughout the investigation, analysis and validation process.