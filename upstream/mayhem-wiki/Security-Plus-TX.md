# Security+ TX

Transmits **Security+ 2.0** rolling-code signals used by Chamberlain, LiftMaster, and Craftsman garage door openers and gate operators.

This is an [external app](External-apps-informations) and must be present on the SD card in the `APPS/` folder.

# 🎁 Features

* Encodes and transmits Security+ 2.0 rolling-code packets (two-packet frame, Manchester OOK)
* Rolling code auto-increments after each transmission to stay in sync with the receiver
* Optional data payload field for openers that require it
* Learn mode for pairing without advancing the rolling code
* Save/load remote configurations from `.SECPLUS` files
* Autosave after each successful transmission

# 📶 Protocol

Security+ 2.0 uses **OOK (On-Off Keying)** with **Manchester encoding** at **4000 bps** on **315 MHz**.

Each transmission consists of two packets sent sequentially:
- **Packet 1** (indicator `0b00`) — encodes the first half of the rolling and fixed codes
- **Packet 2** (indicator `0b01`) — encodes the second half

The full transmission is repeated **3 times**.

The rolling code is a 28-bit counter. The fixed code is a 40-bit device identifier. Together they form a cryptographically scrambled frame that the receiver validates. The rolling code must stay within the receiver's synchronisation window (typically ±256 counts of the last accepted value) to be accepted.

# ❓ User Guide

## Controls

| Control | Description |
|---|---|
| **Open** | Open a `.SECPLUS` file from the `SECPLUS/` folder |
| **Save** | Save current data to the current file immediately |
| **Name** | Remote name (tap to edit via keyboard) |
| **Fixed** | 40-bit fixed code in hex (10 digits) — permanent device identifier |
| **Rolling** | 28-bit rolling code in hex (7 digits) — increments after each TX |
| **Data** | Optional 32-bit payload in hex (8 digits). Enable with the **Data** checkbox. Greyed out when disabled. |
| **Learn** | When checked, the rolling code does **not** increment after TX. Use this when pairing with a receiver or replaying a known code. |
| **Autosave** | When checked (default), the file is saved automatically after each transmission. Keeps the rolling code on disk in sync. |
| Progress bar | Shows transmission progress across the 3 repeat cycles. |

Standard transmitter controls (frequency, LNA, VGA, AMP, TX button) are shown at the bottom.

## Workflow

**Transmitting a known remote:**
1. Press **Open** and select the `.SECPLUS` file for the remote.
2. Verify the Fixed and Rolling codes match your remote.
3. Press **TX**. The rolling code increments automatically and the file is saved.

**Creating a new remote entry:**
1. Enter the Fixed and Rolling code values from your remote (e.g. read via SDR capture and decode).
2. Set a name and optionally enable the Data field.
3. Press **Save** or let Autosave handle it after the first TX.

**Pairing / learning mode:**
1. Enable the **Learn** checkbox.
2. Transmit — the rolling code stays fixed, allowing you to transmit the same code repeatedly.

# 📁 File Format

Remote configurations are stored as `.SECPLUS` files in the `SECPLUS/` folder on the SD card.

The file is a single CSV line:

```
version;name;has_data;fixed_code;rolling_code;data
```

Example:
```
2;MyGarage;0;1A2B3C4D5E;0001F4;00000000
```

| Field | Description |
|---|---|
| `version` | Protocol version — always `2` for Security+ 2.0 |
| `name` | Remote name (display only) |
| `has_data` | `1` if data field is used, `0` otherwise |
| `fixed_code` | 40-bit fixed code in hex |
| `rolling_code` | 28-bit rolling code in hex |
| `data` | 32-bit optional data payload in hex |

The default file `SECPLUS/DEFAULT.SECPLUS` is created automatically on first launch if it does not exist.