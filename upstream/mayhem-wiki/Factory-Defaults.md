# Factory Defaults

## Why reset to factory defaults

After a firmware update, some settings may be stored in an incompatible format, causing apps to malfunction or the device to behave unexpectedly. Resetting to factory defaults clears these settings and returns the device to a known-good state.

There are two separate stores that may need to be reset:

- **Persistent memory (P.Mem):** Stores device-wide settings such as frequency, corrections, UI options, and radio configuration. Held in battery-backed RAM (requires a working coin cell battery).
- **SETTINGS directory on SD card:** Stores per-app settings saved by the "App Load and Save" feature.

## Resetting persistent memory (P.Mem)

### Via the Settings menu

Navigate to **Settings → P.Memory Mgmt**. The following options are available:

| Button / Control | Function |
|---|---|
| Use SD card for P.Mem | Store P.Mem on SD card instead of coin-cell-backed RAM (useful if coin cell is dead or missing) |
| Save P.Mem to SD card | Back up current P.Mem contents to SD card |
| Load P.Mem from SD Card | Restore P.Mem from a previously saved SD card backup |
| Reset P.Mem to defaults | Reset all persistent memory settings to factory defaults |

Pressing **Reset P.Mem to defaults** opens a confirmation dialog:

> *"This will reset the P.Mem to default settings."*

Confirm with **Yes** to apply the reset. The status bar refreshes immediately.

:warning: ! if you are using "Use SD card for P.Mem" option because your coin battery is dead or absent, don't forget to hit "Save P.Mem to SD card" after clicking on "Reset P.Mem to defaults", else you are going to have old settings at reboot ! :warning: 

### Via button combination at boot

If the device is in a state where it cannot be navigated normally, persistent memory can be bypassed at startup. Hold the **Left** and **Right** buttons simultaneously while powering on or pressing reset. The device will boot as if P.Mem is empty, loading factory defaults without modifying the stored contents.

> [!NOTE]
> This bypass is temporary — P.Mem is not permanently cleared by this method. To permanently reset, use the Settings menu as described above.

### Automatic reset

P.Mem is reset to defaults automatically in two cases:
- After a firmware upgrade or downgrade that changes the P.Mem data structure version
- When the coin cell battery is discharged (P.Mem loses power and becomes invalid)

## Resetting SD card settings

### SETTINGS directory

Delete all files under the `SETTINGS/` directory on the SD card. This resets all per-app settings saved via "App Load and Save", as well as the P.Memory Mgmt configuration (e.g. the SD pmem flag file). It does **not** reset the persistent memory itself.

> [!NOTE]
> Updating the SD card content to the latest release is a good opportunity to do this cleanup. The firmware does not automatically remove old or incompatible settings files.

## Full reset procedure

For a complete reset (both P.Mem and SD card settings):

1. Remove the SD card and connect it to a computer.
2. Delete all files under `SETTINGS/`.
3. Optionally update the SD card content to the latest release.
4. Reinsert the SD card.
5. Boot the device without the SD card first (hold the boot key if required), go to **Settings → P.Memory Mgmt**, and press **Reset P.Mem to defaults**.
6. Shut down, reinsert the SD card, and boot normally.

The device will now behave as if freshly set up.

> [!NOTE]
> The "Debug Dump" app (under **Settings → Debug → Debug Dump**) can generate a file listing all current persistent memory settings — useful for diagnosing issues before resetting.