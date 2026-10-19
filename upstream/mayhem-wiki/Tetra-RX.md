# Tetra RX

## Overview
The **Tetra RX** app allows you to receive, demodulate, and parse Terrestrial Trunked Radio (TETRA) downlink signals directly on your PortaPack. It decodes unencrypted network parameters, frame structure information, and live call control events from the base station in real-time. 

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

## User Interface

![Tetra RX App](https://private-user-images.githubusercontent.com/1985796/618255515-ae7fc206-677c-46d4-9b76-dab1b26ee2ae.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODM1OTAwNjEsIm5iZiI6MTc4MzU4OTc2MSwicGF0aCI6Ii8xOTg1Nzk2LzYxODI1NTUxNS1hZTdmYzIwNi02NzdjLTQ2ZDQtOWI3Ni1kYWIxYjI2ZWUyYWUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDcwOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA3MDlUMDkzNjAxWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MTZmMTJkNzYzYWFkMzc3MjE0NjYwNDRiMzAxNzZiYzVlOTlkZjA0ZmYzZGZjM2ZmOWZjMGRhZTNhYmM0MTEyZiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.jp36udqO4g_RSeNvLjbNRLLLKLn2zSZQ-fAo26uYJSY)

### Top Bar / RF Settings
*   **Frequency:** The downlink center frequency of the TETRA base station (e.g., `427.1625` MHz).
*   **Gain Controls:** Standard RX gain staging (e.g., `1 40 6` representing RF Amp, LNA, and VGA levels).
*   **Signal Meter:** Visual indicator showing signal strength and decoding quality.

### Network & Station Parameters
*   **MCC (Mobile Country Code):** Identifies the country of the network (e.g., `216`).
*   **MNC (Mobile Network Code):** Identifies the specific network operator (e.g., `2163`).
*   **BCC (Base Color Code):** Differentiates between nearby base stations utilizing the same frequency (values 0-63).
*   **LA (Location Area):** The current location area code of the cell (e.g., `1105`).

### Frame & Payload Data
*   **TS (Time Slot):** Current time slot being decoded (TETRA utilizes 4 time slots per TDMA frame).
*   **FN (Frame Number):** The current frame number within the TETRA multiframe hierarchy.
*   **ENC (Encryption):** Indicates the encryption state of the payload (e.g., `Clear` indicates an unencrypted control channel).
*   **PDU (Protocol Data Unit):** The most recent MAC block type decoded (e.g., `MAC-RESOUR`).

### Demodulator & Sync Stats
*   **Syn / V / H / E:** These are underlying demodulator and decoder metrics. They track synchronization locks (`Syn`), header error counts (`E`). Consistently low or zero error counts (like `E: 0`) indicate a clean, well-tuned signal.

### Call Event Log
The bottom section of the screen provides a real-time, scrolling log of the decoded network activity and call control events

## Usage Tips
*   **Tuning:** TETRA channels are spaced 25 kHz apart. Ensure your tuning is exact, as the $\pi$/4 DQPSK demodulator requires a centered signal to maintain a sync lock.
*   **Gain Adjustment:** Adjust your LNA and VGA to ensure a clean signal without overloading the RX chain. 
*   **Audio:** While the app can decode network parameters and subscriber IDs on unencrypted control channels, it cannot decode audio or payload data.