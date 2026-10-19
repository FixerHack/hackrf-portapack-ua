![cart-lock](https://github.com/user-attachments/assets/8023f40f-309c-4a1c-b52d-c2b4016f903f)

Shopping Cart lock/unlock app by RocketGod ([@rocketgod-git](https://betaskynet.com)).

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).


> [!WARNING]
> This app plays audio at **maximum volume** automatically.

## Requirements

Two WAV files must be placed in the `WAV/` folder on the SD card:

| Filename | Function |
|----------|----------|
| `shopping_cart_lock.wav` | Played when pressing Lock |
| `shopping_cart_unlock.wav` | Played when pressing Unlock |

If either file is missing, the Lock and Unlock buttons will not appear.

## Usage

| Button | Action |
|--------|--------|
| **Lock** | Plays the lock WAV file on loop |
| **Unlock** | Plays the unlock WAV file on loop |
| **Stop** | Stops playback |

The audio loops continuously until **Stop** is pressed or the app is closed.

The log panel at the top shows diagnostic output: file scan results, playback state, and any errors.

## Notes

- Original `.cu8` signal files by [@jimilinuxguy](https://github.com/jimilinuxguy/customer-assistance-buttons-sdr)
- Audio is output through the headphone jack or internal speaker at maximum volume
- The app requires WAV files to be present — it does **not** generate tones internally