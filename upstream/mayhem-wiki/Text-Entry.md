# Text Entry

The text entry screen (title: **Text entry**) is used whenever an app needs free-text input — for example entering a callsign, filename, or label. It is opened automatically by apps that require it; it cannot be accessed directly from the menu.

## Layout

The keyboard is a 5-column grid of 29 character buttons. Below the grid are four action controls:

| Control | Function |
|---|---|
| **Shift** (icon) | Cycle shift state: off → on (once) → locked → off |
| **`<DEL`** | Delete the character before (to the left of) the cursor |
| **Mode button** (e.g. `123`) | Switch to the next character set (UPPER / lower-case letters, digits and marks) |
| **`OK`** | Confirm entry and send the string back to the calling app |

Above the grid, the current text is shown with a cursor. Below the grid are two helper fields:

- **Raw:** — a number field (1–255) for inserting a character directly by its ASCII code. Use it for special characters that are not on any keyboard page: rotate the encoder to set the value, check the resulting character in the **AKA:** field, then press the center button to insert it.
- **AKA:** — shows the character corresponding to the current Raw value.

## Character sets

The keyboard cycles through three sets using the Mode button. The button always shows the *next* set's name:

### `abc` — Letters
- Normal: `a b c d e f g h i j k l m n o p q r s t u v w x y z , . `
- Shifted (once or locked): same in uppercase `A B C … Z , . `

### `123` — Digits and punctuation
- Normal: `` 1 2 3 4 5 6 7 8 9 0 ( ) ' ` " + - * / = < > _ \ ! ? , . ``
- Shifted (locked only): `` ! @ # $ % ^ & * ( ) [ ] ' ` " { } | : ; < > - _ ~ ? , . ``

> [!NOTE]
> In `123` mode, the Shift button skips the one-time shift state and goes directly to ShiftLock. Single-character capitalisation is only available in `abc` mode.

### `hex` — Hexadecimal
- `1 2 3 4 5 6 7 8 9 0 A B C D E F ` (space)
- Shift has no effect in this mode.

## Shift states

The Shift button cycles through three states:

| State | Shift button colour | Effect |
|---|---|---|
| Off | Dark (default) | Normal characters |
| On (once) | Darker | Next character typed is uppercase/shifted; then resets to off automatically |
| Locked | Blue | All characters are uppercase/shifted until unlocked |

## Navigation

- **Encoder dial:** moves the highlight through all 29 character buttons in order.
- **Touchscreen:** tap any button directly.
- **Hardware buttons (D-pad):** navigate between buttons.

The cursor position in the text preview can be set by tapping a position in the text field if supported by the calling app.