<!-- згенеровано scripts/gen_app_pages.py з scripts/apps_data.py — правте дані там -->
# Трансівери, Recon, Capture, Replay та утиліти

!!! info "Скріншоти з вашого пристрою"
    Усі знімки зроблено на HackRF One + PortaPack H2 з прошивкою Mayhem v2.4.0. Більшість застосунків показано у стані «за замовчуванням», до приймання чи передавання. Опис складено за вікі Mayhem та екранами; дрібні відмінності залежать від версії прошивки.

Інші розділи головного меню: **Transceiver**, **Recon**, **Capture**, **Replay**, **Remote**, **Looking Glass**, **Utilities** (з меню **Debug**) і **Games**.

## Меню розділів

### Transceiver {#shot-006}

<div class="app" markdown>
<div class="shot" markdown>
![Transceiver](screens/006.jpg)
</div>
<div class="txt" markdown>

Пункти меню: Mic, KISS TNC.


</div>
</div>

### Utilities — сторінка 1 {#shot-012}

<div class="app" markdown>
<div class="shot" markdown>
![Utilities — сторінка 1](screens/012.jpg)
</div>
<div class="txt" markdown>

Пункти меню: File Manager, Freq. Manager, IQ Trim, Notepad, Debug, Flash Utility, Antenna Length, Calculator, Metronome, PlaylistEdit, Rand Pwd, SD Over USB.


</div>
</div>

### Utilities — сторінка 2 {#shot-013}

<div class="app" markdown>
<div class="shot" markdown>
![Utilities — сторінка 2](screens/013.jpg)
</div>
<div class="txt" markdown>

Пункти меню: Calculator, Metronome, PlaylistEdit, Rand Pwd, SD Over USB, Wipe SD card, Cart Lock, Stopwatch, Tuner, WAV Viewer, WardriveMap, Wt Design (Waterfall Designer).


</div>
</div>

### Games {#shot-014}

<div class="app" markdown>
<div class="shot" markdown>
![Games](screens/014.jpg)
</div>
<div class="txt" markdown>

Пункти меню: Battleship, Blackjack, Breakout, Dino Game, Doom, 2048, Morse P, Snake, Space Invaders, Tetris, DigitalRain, Pac-Man.


</div>
</div>

## Трансівери

### Microphone (трансівер) {#shot-086}

<div class="app" markdown>
<div class="shot" markdown>
![Microphone (трансівер)](screens/086.jpg)
</div>
<div class="txt" markdown>

Напівдуплексний голосовий трансівер: NFM, WFM, AM, USB, LSB, DSB-SC; PTT і VOX, CTCSS, Roger beep, окремі частоти TX/RX.

- Кнопка **PTT TX**, **TX-IQ-CAL**, прапорці **Roger beep**, **Hear Mic**, **RX audio**.

[Докладніше на сторінці застосунку](<Microphone-Transceiver>)

</div>
</div>

### KISS TNC {#shot-087}

<div class="app" markdown>
<div class="shot" markdown>
![KISS TNC](screens/087.jpg)
</div>
<div class="txt" markdown>

Контролер вузла терміналу в режимі KISS для пакетного радіозв'язку / APRS (AX.25).

- Статус USB (**Disconnected**), лічильники **RX/TX**.

[Докладніше на сторінці застосунку](<KISS-TNC>)

</div>
</div>

## Recon, Capture, Replay, Remote, Looking Glass

### Recon {#shot-007}

<div class="app" markdown>
<div class="shot" markdown>
![Recon](screens/007.jpg)
</div>
<div class="txt" markdown>

Сканер частот і «мисливець за сигналами»: сканує списки частот та діапазони, реєструє знайдені сигнали.

- Кнопки **PAUSE**, **AUDIO**, **STORE**, **CONFIG**, **SEARCH**, **RECON**.

[Докладніше на сторінці застосунку](<Recon>)

</div>
</div>

### Replay {#shot-008}

<div class="app" markdown>
<div class="shot" markdown>
![Replay](screens/008.jpg)
</div>
<div class="txt" markdown>

Передає записані файли IQ (`.C16`/`.C8`/`.CU8`) або плейлисти `.PPL`.

- Кнопки навігації між треками, додавання/видалення файлу, відкриття й збереження плейлиста; прапорець **Loop**.

[Докладніше на сторінці застосунку](<Replay>)

</div>
</div>

### Capture {#shot-009}

<div class="app" markdown>
<div class="shot" markdown>
![Capture](screens/009.jpg)
</div>
<div class="txt" markdown>

Записує IQ-дані на SD-карту у форматі `.C16` (або `.C8`) разом з метаданими.

- **Rate** — частота дискретизації (рекомендовано ≤ 500 кГц), **Format** (C16/C8), **Trim** — автообрізання; червона кнопка запускає запис, нижче — водоспад.

[Докладніше на сторінці застосунку](<Capture>)

</div>
</div>

### Remote {#shot-010}

<div class="app" markdown>
<div class="shot" markdown>
![Remote](screens/010.jpg)
</div>
<div class="txt" markdown>

Створює власну панель кнопок, прив'язаних до файлів запису для одним дотиком.

- Файли `.REM` у теці `REMOTES/`; кнопки **+** (додати), **Новий**, **Відкрити**; прапорець **Loop**.

[Докладніше на сторінці застосунку](<Remote>)

</div>
</div>

### Looking Glass {#shot-011}

<div class="app" markdown>
<div class="shot" markdown>
![Looking Glass](screens/011.jpg)
</div>
<div class="txt" markdown>

Широкосмуговий спектр-водоспад по великому діапазону частот.

- **MIN/MAX/RANGE** — межі діапазону, **FILTER**, **PRESET**, режими відображення **SPECTR/LIVE-V/PEAK-V**, **F-/S-** (швидко/точно).

[Докладніше на сторінці застосунку](<Looking-Glass>)

</div>
</div>

## Утиліти

### File Manager {#shot-088}

<div class="app" markdown>
<div class="shot" markdown>
![File Manager](screens/088.jpg)
</div>
<div class="txt" markdown>

Файловий менеджер SD-карти: перегляд тек, копіювання, перейменування, видалення.

- Показано кореневий каталог SD-карти (`AIS`, `APPS`, `AUDIO`, `CAPTURES` тощо) і кількість файлів у теках.

[Докладніше на сторінці застосунку](<File-manager>)

</div>
</div>

### Freq. Manager {#shot-089}

<div class="app" markdown>
<div class="shot" markdown>
![Freq. Manager](screens/089.jpg)
</div>
<div class="txt" markdown>

Менеджер збережених частот (списки freqman): редагування частоти й опису.

- Кнопки **Edit**, **Frequency**, **Description**, **+**, **Exit**.

[Докладніше на сторінці застосунку](<Freq-manager>)

</div>
</div>

### IQ Trim {#shot-090}

<div class="app" markdown>
<div class="shot" markdown>
![IQ Trim](screens/090.jpg)
</div>
<div class="txt" markdown>

Обрізає записаний файл IQ, залишаючи лише корисну частину сигналу.

- **Capture File** — файл, **Start/End/Samples/Max Pwr/Cutoff/Amplify**, кнопка **Trim**.

[Докладніше на сторінці застосунку](<IQ-trim>)

</div>
</div>

### Notepad {#shot-091}

<div class="app" markdown>
<div class="shot" markdown>
![Notepad](screens/091.jpg)
</div>
<div class="txt" markdown>

Простий текстовий блокнот (наприклад, для файлу `blacklist` у `SETTINGS`).


[Докладніше на сторінці застосунку](<Notepad>)

</div>
</div>

### Flash Utility {#shot-092}

<div class="app" markdown>
<div class="shot" markdown>
![Flash Utility](screens/092.jpg)
</div>
<div class="txt" markdown>

Оновлення прошивки з файлу на SD-карті (`.bin` або `.ppfw.tar`).

- Показано вибір файлу прошивки; повний порядок дій — у розділі [Оновлення прошивки](update-firmware.md).

[Докладніше на сторінці застосунку](<Flash-Utility>)

</div>
</div>

### Antenna Length {#shot-096}

<div class="app" markdown>
<div class="shot" markdown>
![Antenna Length](screens/096.jpg)
</div>
<div class="txt" markdown>

Калькулятор довжини антени за частотою (чверть хвилі, метрика й дюйми).

- Приклад: 100 МГц → чверть хвилі ≈ 74,9 см; підказки для антен ANT500/ANT700.

[Докладніше на сторінці застосунку](<antennas>)

</div>
</div>

### Calculator {#shot-097}

<div class="app" markdown>
<div class="shot" markdown>
![Calculator](screens/097.jpg)
</div>
<div class="txt" markdown>

Калькулятор (з шістнадцятковими цифрами A–F).


[Докладніше на сторінці застосунку](<Calculator>)

</div>
</div>

### Metronome {#shot-098}

<div class="app" markdown>
<div class="shot" markdown>
![Metronome](screens/098.jpg)
</div>
<div class="txt" markdown>

Метроном: BPM, тони акцентованих і слабких ударів, розмір, тривалість спалаху.

- Кнопка **Tap Tempo** задає темп дотиками.

[Докладніше на сторінці застосунку](<Metronome>)

</div>
</div>

### Playlist Editor {#shot-099}

<div class="app" markdown>
<div class="shot" markdown>
![Playlist Editor](screens/099.jpg)
</div>
<div class="txt" markdown>

Редактор плейлистів `.PPL` для застосунку Replay.

- Кнопки відкриття, додавання/видалення записів і збереження.

[Докладніше на сторінці застосунку](<Playlist-Editor>)

</div>
</div>

### SD Over USB {#shot-100}

<div class="app" markdown>
<div class="shot" markdown>
![SD Over USB](screens/100.jpg)
</div>
<div class="txt" markdown>

Режим USB-накопичувача: SD-карта PortaPack стає диском на комп'ютері.

- Натисніть **Run** і зачекайте до 20 с, поки диск з'явиться.

[Докладніше на сторінці застосунку](<SD-Over-USB>)

</div>
</div>

### Random Password {#shot-101}

<div class="app" markdown>
<div class="shot" markdown>
![Random Password](screens/101.jpg)
</div>
<div class="txt" markdown>

Генератор випадкових паролів із ентропії радіошуму.

- Опції: довжина (**digits**), набори символів (123, abc, ABC, спецсимволи), **Generate**, **Show QR**.

[Докладніше на сторінці застосунку](<Random-password>)

</div>
</div>

### Wipe SD card {#shot-102}

<div class="app" markdown>
<div class="shot" markdown>
![Wipe SD card](screens/102.jpg)
</div>
<div class="txt" markdown>

**Форматує FAT SD-карти — усі дані буде втрачено.** Червоний значок означає руйнівну утиліту.

- Запит «Wipe FAT of SD card?» — **YES / NO**.

[Докладніше на сторінці застосунку](<Wipe-SD-Card>)

</div>
</div>

### Cart Lock {#shot-103}

<div class="app" markdown>
<div class="shot" markdown>
![Cart Lock](screens/103.jpg)
</div>
<div class="txt" markdown>

Утиліта блокування візків (**Lock/Unlock/Stop**).

- Журнал: перевірка файлів, ініціалізація, статус READY.

[Докладніше на сторінці застосунку](<Cart-Lock>)

</div>
</div>

### Tuner {#shot-104}

<div class="app" markdown>
<div class="shot" markdown>
![Tuner](screens/104.jpg)
</div>
<div class="txt" markdown>

Тюнер-підказка: програє еталонну ноту для налаштування інструмента.

- Вибір інструмента (**Guitar**), ноти, частоти, гучність.

[Докладніше на сторінці застосунку](<Tuner>)

</div>
</div>

### Stopwatch {#shot-105}

<div class="app" markdown>
<div class="shot" markdown>
![Stopwatch](screens/105.jpg)
</div>
<div class="txt" markdown>

Секундомір із колами.

- Кнопки **START**, **RESET**, **EXIT**.

[Докладніше на сторінці застосунку](<Stopwatch>)

</div>
</div>

### WAV Viewer {#shot-106}

<div class="app" markdown>
<div class="shot" markdown>
![WAV Viewer](screens/106.jpg)
</div>
<div class="txt" markdown>

Переглядач форми сигналу WAV-файлів із курсорами A/B.

- **Open** — відкрити файл; **Position**, **Scale**, **Cursor A/B**, **Delta**.

[Докладніше на сторінці застосунку](<Wav-viewer>)

</div>
</div>

### WAV Viewer (інший знімок) {#shot-107}

<div class="app" markdown>
<div class="shot" markdown>
![WAV Viewer (інший знімок)](screens/107.jpg)
</div>
<div class="txt" markdown>

Той самий застосунок.


[Докладніше на сторінці застосунку](<Wav-viewer>)

</div>
</div>

### WardriveMap {#shot-108}

<div class="app" markdown>
<div class="shot" markdown>
![WardriveMap](screens/108.jpg)
</div>
<div class="txt" markdown>

Показує на карті захоплення з прив'язкою до GPS.

- Повідомлення «No GeoTagged captures found» — записів з координатами ще немає.

[Докладніше на сторінці застосунку](<WardriveMap>)

</div>
</div>

### Waterfall Designer {#shot-109}

<div class="app" markdown>
<div class="shot" markdown>
![Waterfall Designer](screens/109.jpg)
</div>
<div class="txt" markdown>

Налаштування кольорових схем водоспаду.

- Кнопки відкриття/збереження схеми, шкала частот.

[Докладніше на сторінці застосунку](<Waterfall-Designer>)

</div>
</div>

## Debug

### Debug — меню (1) {#shot-093}

<div class="app" markdown>
<div class="shot" markdown>
![Debug — меню (1)](screens/093.jpg)
</div>
<div class="txt" markdown>

Діагностичні інструменти: Buttons Test, M0 Stack Dump, Memory Dump, Peripherals, Pers. Memory, SD Card, Touch Test, Reboot, Ext Module, Audio Test, DebugPMem, ExtSensor.


[Докладніше на сторінці застосунку](<Debug>)

</div>
</div>

### Debug — меню (2) {#shot-094}

<div class="app" markdown>
<div class="shot" markdown>
![Debug — меню (2)](screens/094.jpg)
</div>
<div class="txt" markdown>

Продовження меню Debug: Font Viewer, Temperature та інші.


[Докладніше на сторінці застосунку](<Debug>)

</div>
</div>

### Debug — Buttons Test {#shot-095}

<div class="app" markdown>
<div class="shot" markdown>
![Debug — Buttons Test](screens/095.jpg)
</div>
<div class="txt" markdown>

Тест кнопок: показує стан D-pad, обертання енкодера (**Dial**) і режим довгого натискання.

- Корисно для перевірки несправних кнопок і енкодера.

[Докладніше на сторінці застосунку](<Debug>)

</div>
</div>

