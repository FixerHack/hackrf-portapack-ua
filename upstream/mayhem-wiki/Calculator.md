The **Calculator** is a FORTH-programmable scientific RPN (Reverse Polish Notation) calculator based on the [IVT (IVEE-TINY)](https://github.com/zooxo/ivee) engine by zooxo/deetee.

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).


## What is RPN?

In RPN, operands are entered before the operator. Instead of `3 + 4`, you enter `3`, then `4`, then `+`. Numbers are pushed onto a stack; operations consume values from the top of the stack and push the result.

- **D** (DUP) pushes/duplicates the current number onto the stack, or confirms number entry.
- **C** (DROP) removes the top of stack, or clears the current number entry.

## Keyboard Layout

The keypad has two modes. Press **F** to toggle the shifted layer.

### Normal mode

| Col 1 | Col 2 | Col 3 | Col 4 |
|-------|-------|-------|-------|
| **F** (shift) | **7** | **8** | **9** |
| **E** (10^x) | **4** | **5** | **6** |
| **N** (negate) | **1** | **2** | **3** |
| **C** (DROP/clear) | **0** | **.** (decimal) | **D** (DUP/enter) |

### F-shifted mode (press F first)

| Col 1 | Col 2 | Col 3 | Col 4 |
|-------|-------|-------|-------|
| **MENU** | **SUM+** | **PRG** | **/** |
| **SWAP** | **DICT** | **USR** | **\*** |
| **ROT** | **RCL** | **STO** | **-** |
| **CA** | **PI** | **INT** | **+** |

## Key Reference

| Key | Description |
|-----|-------------|
| **0–9, .** | Enter digits and decimal point |
| **E** | Scientific notation exponent (Y × 10^X) |
| **N** | Negate (change sign) |
| **D** | DUP — duplicate top of stack / confirm number entry |
| **C** | DROP — remove top of stack / clear current entry |
| **F** | Shift to function layer; double-press opens user MENU |
| **+  −  ×  ÷** | Basic arithmetic |
| **SWAP** | Swap top two stack values (1 2 → 2 1) |
| **ROT** | Rotate stack (1 2 3 → 2 3 1) |
| **STO / RCL** | Store/recall a number to memory slot 0–9 (enter slot number first) |
| **CA** | Clear all — clears stack and statistics memories |
| **PI** | Push π onto the stack |
| **INT** | Integer part of top value |
| **SUM+** | Add X (or X,Y) data point for statistics / linear regression |
| **DICT** | Browse the full dictionary of all commands |
| **USR** | Assign a dictionary entry to the user menu |
| **MENU** | Open the user-defined menu |
| **PRG** | Edit a user program (enter program number 0–15 first) |

## Dictionary Functions

Access all commands via **DICT** (F+4). Functions include:

**Math:** `SQRT`, `POW` (y^x), `INV` (1/x), `EXP`, `LN`, `SIN`, `COS`, `TAN`, `ASIN`, `ACOS`, `ATAN`, `GAMMA` (ln Γ)

**Stack:** `DUP`, `DROP`, `SWAP`, `ROT`, `OVER`

**Statistics:** `SUM+`, `SUMclr`, `MEAN/STDEV`, `LR` (linear regression)

**Other:** `PV` (present value), `ND` (normal distribution PDF/CDF), `P>R` / `R>P` (polar/rectangular), `nPr`, `nCr`, `SOLVE` (root finder)

**Control flow (for programs):** `IF`, `ELSE`, `THEN`, `BEGIN`, `UNTIL`, `<`, `=`, `<>`, `>`

## Programming

IVT supports up to **16 user programs** (numbered 00–15) with up to 440 total steps.

To edit a program:
1. Enter the program number (e.g. `0`, `5`)
2. Press **F + PRG**
3. Navigate steps with **E** (up) and **N** (down)
4. Insert steps by pressing a key or selecting from DICT
5. Delete a step with **.**
6. Save and exit with **C**

> [!NOTE]
> User program **00** is reserved for the **SOLVE** (root finder) function.

## Limits

| Item | Limit |
|------|-------|
| Stack depth | 24 |
| Significant digits | 7 |
| Memory slots (STO/RCL) | 10 (0–9) |
| User programs | 16 |
| Total program steps | 440 |
| User menu slots | 32 |
| Number precision | IEEE 754 32-bit float (~6–7 decimal digits) |

## Example Programs
```
ABS:    DUP 0 > IF THEN NEG
SINH:   EXP DUP INV NEG + 2 /
LOG:    LN 1 0 LN /
%:      OVER / 1 0 0 *
C<>F:   DUP 1 . 8 * 3 2 + SWAP 3 2 - 1 . 8 /
```