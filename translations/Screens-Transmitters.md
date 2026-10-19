<!-- згенеровано scripts/gen_app_pages.py з scripts/apps_data.py — правте дані там -->
# Передавачі: огляд застосунків

!!! info "Скріншоти з вашого пристрою"
    Усі знімки зроблено на HackRF One + PortaPack H2 з прошивкою Mayhem v2.4.0. Більшість застосунків показано у стані «за замовчуванням», до приймання чи передавання. Опис складено за вікі Mayhem та екранами; дрібні відмінності залежать від версії прошивки.

!!! danger "Передавайте відповідально"
    Передавання радіосигналів без дозволу, глушіння, підміна GPS, підроблені сигнали лиха та аварійні оповіщення незаконні в більшості країн. Тестуйте лише на власному обладнанні, на еквіваленті навантаження або в екранованому середовищі. Див. [Призначення та законність використання](Intended-Use-and-Legality).

У меню **Transmit** — застосунки для передавання. Внизу екрана передавача є стандартна панель: частота, крок, смуга, **Gain**, **Amp** і кнопка **START**.

## Меню Transmit

### Transmit — сторінка 1 {#shot-004}

<div class="app" markdown>
<div class="shot" markdown>
![Transmit — сторінка 1](screens/004.jpg)
</div>
<div class="txt" markdown>

Пункти меню: APRS TX, BLE Tx, OOK, RDS, TouchTunes, Adult Toys, TPMS TX, SSTV, Spectrum Painter, Soundboard, Signal gen, SAME TX, RTTY, POCSAG TX, P25 TX, OOKEditor, OOKBrute, Morse TX.


</div>
</div>

### Transmit — сторінка 2 {#shot-005}

<div class="app" markdown>
<div class="shot" markdown>
![Transmit — сторінка 2](screens/005.jpg)
</div>
<div class="txt" markdown>

Пункти меню: OOKEditor, OOKBrute, Morse TX, MDC-1200, LGE, TEDI/LCR, Keyfob, KeeLoq TX, Jammer, Hopper, GPSSim, FlipperTx, EPIRB TX, CVS Spam, BurgerPgr, BLESpam, BHT TX, ADSB-TX.


</div>
</div>

## Застосунки

### APRS TX {#shot-053}

<div class="app" markdown>
<div class="shot" markdown>
![APRS TX](screens/053.jpg)
</div>
<div class="txt" markdown>

Передає позиційні звіти й повідомлення APRS (Bell 202 AFSK, 1200 бод).

- Поля **Source**, **Dest.**, **Path**, кнопки **Set Path**, **Set**, **Manual GPS**.

[Докладніше на сторінці застосунку](<APRS-TX>)

</div>
</div>

### BLE TX {#shot-054}

<div class="app" markdown>
<div class="shot" markdown>
![BLE TX](screens/054.jpg)
</div>
<div class="txt" markdown>

Передає рекламні пакети Bluetooth Low Energy на 2,4 ГГц.

- Кнопки **Open file**, **Clear Marked**, **Save Packet**, **Switch to Rx**.

[Докладніше на сторінці застосунку](<Bluetooth-Low-Energy-Transmitter>)

</div>
</div>

### OOK {#shot-055}

<div class="app" markdown>
<div class="shot" markdown>
![OOK](screens/055.jpg)
</div>
<div class="txt" markdown>

Передає сирі OOK/ASK-шаблони для пультів нижче 1 ГГц.

- Параметри: тип сигналу, тактова частота, повтор; відображення форми сигналу (**Waveform**).

[Докладніше на сторінці застосунку](<OOK>)

</div>
</div>

### Adult Toys {#shot-056}

<div class="app" markdown>
<div class="shot" markdown>
![Adult Toys](screens/056.jpg)
</div>
<div class="txt" markdown>

Передає BLE-керувальні пакети, сумісні з Bluetooth-пристроями бренду Love Spouse.

- Вибір режиму, пакета та прапорці.

[Докладніше на сторінці застосунку](<Adult-Toys>)

</div>
</div>

### TouchTunes {#shot-057}

<div class="app" markdown>
<div class="shot" markdown>
![TouchTunes](screens/057.jpg)
</div>
<div class="txt" markdown>

Передає сигнали ІЧ-через-ВЧ дистанційного керування музичних автоматів TouchTunes.

- Цифрова клавіатура, PIN, кнопки **PAUSE/POWER**, режими **Scan** та **EW Mode**.

[Докладніше на сторінці застосунку](<TouchTunes>)

</div>
</div>

### RDS TX {#shot-058}

<div class="app" markdown>
<div class="shot" markdown>
![RDS TX](screens/058.jpg)
</div>
<div class="txt" markdown>

Передає дані системи радіоданих (RDS), вбудовані в FM-несучу.

- Вкладки **Name**, **Text**, **Time**, **Audio**; тип програми, прапорці **TP**, **Stereo**, **Music**, **Traffic announcement**.

[Докладніше на сторінці застосунку](<RDS>)

</div>
</div>

### TPMS TX {#shot-059}

<div class="app" markdown>
<div class="shot" markdown>
![TPMS TX](screens/059.jpg)
</div>
<div class="txt" markdown>

Передає симульовані сигнали датчиків тиску в шинах.

- Поля **Freq**, **Type**, **ID**, **Pres**, **Temp**, кнопки **Load**, **Save**, **START TX**.

[Докладніше на сторінці застосунку](<TPMS-TX>)

</div>
</div>

### SSTV TX {#shot-060}

<div class="app" markdown>
<div class="shot" markdown>
![SSTV TX](screens/060.jpg)
</div>
<div class="txt" markdown>

Передає зображення SSTV (режими Scottie, Martin) з файлу BMP.

- **File** — файл зображення, **Mode** — режим (Scottie 2); показується попередній перегляд.

[Докладніше на сторінці застосунку](<SSTV>)

</div>
</div>

### Spectrum Painter {#shot-061}

<div class="app" markdown>
<div class="shot" markdown>
![Spectrum Painter](screens/061.jpg)
</div>
<div class="txt" markdown>

Передає сигнал, спектрограма якого «малює» зображення на аналізаторі спектра.

- Вкладки **Image** / **Text**, кнопка **Load Image …**.

[Докладніше на сторінці застосунку](<Spectrum-Painter>)

</div>
</div>

### SAME TX {#shot-062}

<div class="app" markdown>
<div class="shot" markdown>
![SAME TX](screens/062.jpg)
</div>
<div class="txt" markdown>

Передає заголовки аварійних сповіщень SAME/EAS (використовуйте лише для тестів у закритому середовищі).

- Поля **Org**, **Evt**, **FIPS**, **Dur**.

[Докладніше на сторінці застосунку](<SAME-TX>)

</div>
</div>

### Signal gen {#shot-063}

<div class="app" markdown>
<div class="shot" markdown>
![Signal gen](screens/063.jpg)
</div>
<div class="txt" markdown>

Генератор сигналу: несуча з опційною FM-модуляцією (тон, свіп, шум).

- **Modulation**, **Shape**, **Tone**, кнопка **Update**, **Auto**, **Stop after**.

[Докладніше на сторінці застосунку](<Signal-Generator>)

</div>
</div>

### Soundboard {#shot-064}

<div class="app" markdown>
<div class="shot" markdown>
![Soundboard](screens/064.jpg)
</div>
<div class="txt" markdown>

Передає FM-модульоване аудіо з файлів `.WAV` на SD-карті.

- Список файлів, **Loop**, **Random**, гучність, сторінки (**Page**, **Sounds**).

[Докладніше на сторінці застосунку](<Soundboard>)

</div>
</div>

### RTTY TX {#shot-065}

<div class="app" markdown>
<div class="shot" markdown>
![RTTY TX](screens/065.jpg)
</div>
<div class="txt" markdown>

Передає текст RTTY (Бодо/ITA2) зі стандартними швидкостями.

- **Baud**, **Shift**, **Inverted**, повідомлення (**Set message**).

[Докладніше на сторінці застосунку](<RTTY-TX>)

</div>
</div>

### POCSAG TX {#shot-066}

<div class="app" markdown>
<div class="shot" markdown>
![POCSAG TX](screens/066.jpg)
</div>
<div class="txt" markdown>

Передає повідомлення пейджерів POCSAG (цифрові та буквено-цифрові).

- Детальний розбір екрана — на анотованому зображенні в розділі [Інтерфейс](ui-guide.md).

[Докладніше на сторінці застосунку](<POCSAG-Tx>)

</div>
</div>

### P25 TX {#shot-067}

<div class="app" markdown>
<div class="shot" markdown>
![P25 TX](screens/067.jpg)
</div>
<div class="txt" markdown>

Передає цифрові голосові кадри P25 Phase 1.

- Параметри **NAC**, **SYS**, **WACN**, **RFSS**, **SITE**, **TG**, **VCH**.

[Докладніше на сторінці застосунку](<P25-Tx>)

</div>
</div>

### Morse TX {#shot-068}

<div class="app" markdown>
<div class="shot" markdown>
![Morse TX](screens/068.jpg)
</div>
<div class="txt" markdown>

Кодує текст у азбуку Морзе (CW) та передає як маніпульовану несучу.

- **Mode**, **Tone**, **WPM**, **Message**, **Call sign**.

[Докладніше на сторінці застосунку](<Morse-TX>)

</div>
</div>

### OOK Brute {#shot-069}

<div class="app" markdown>
<div class="shot" markdown>
![OOK Brute](screens/069.jpg)
</div>
<div class="txt" markdown>

Послідовний перебір кодових просторів OOK-пультів. Призначений для власного обладнання й тестів.

- Початкова й кінцева позиція, тип кодувальника (**Encoder Type**), кнопка **Start**.

[Докладніше на сторінці застосунку](<OOK-Brute>)

</div>
</div>

### OOK Editor {#shot-070}

<div class="app" markdown>
<div class="shot" markdown>
![OOK Editor](screens/070.jpg)
</div>
<div class="txt" markdown>

Графічний редактор для створення й передавання власних бітових шаблонів OOK.

- **SampleRate**, **SymbolRate**, **Repeat**, **Payload**, кнопки **Set**, **Open File**, **Save File**, **Send**.

[Докладніше на сторінці застосунку](<OOK-Editor>)

</div>
</div>

### MDC-1200 TX {#shot-071}

<div class="app" markdown>
<div class="shot" markdown>
![MDC-1200 TX](screens/071.jpg)
</div>
<div class="txt" markdown>

Передає пакети ANI/PTT ID MDC-1200, які використовують в аналогових радіосистемах.

- **Op**, **ID**, **Src**, **Arg**.

[Докладніше на сторінці застосунку](<MDC-1200-TX>)

</div>
</div>

### LGE Tool {#shot-072}

<div class="app" markdown>
<div class="shot" markdown>
![LGE Tool](screens/072.jpg)
</div>
<div class="txt" markdown>

Передає сервісні сигнали LG Electronics.

- Поля **Frame**, **Room**, **Team**, **Player**, **Vest** та ін.

[Докладніше на сторінці застосунку](<LGE-Tool>)

</div>
</div>

### TEDI/LCR TX {#shot-073}

<div class="app" markdown>
<div class="shot" markdown>
![TEDI/LCR TX](screens/073.jpg)
</div>
<div class="txt" markdown>

Передає повідомлення протоколу ідентифікації та сигналізації TEDI/LCR.

- Список полів AM 1–5, кнопки **Modem setup**, **Clear**.

[Докладніше на сторінці застосунку](<LCR>)

</div>
</div>

### Jammer {#shot-074}

<div class="app" markdown>
<div class="shot" markdown>
![Jammer](screens/074.jpg)
</div>
<div class="txt" markdown>

Передає шум у вибраних діапазонах частот. **Використання глушіння радіозв'язку в більшості країн заборонене** — застосовуйте лише в екранованому середовищі.

- Вкладки **Range 1–3**, **Start/Stop/Center/Width**, тип шуму, швидкість.

[Докладніше на сторінці застосунку](<Jammer>)

</div>
</div>

### KeeLoq TX {#shot-075}

<div class="app" markdown>
<div class="shot" markdown>
![KeeLoq TX](screens/075.jpg)
</div>
<div class="txt" markdown>

Повторно передає сигнали KeeLoq з файлів запису `.keeloq`.

- Поля **Manufacturer**, **Serial**, **Fix**, **Hop**, **Counter**, **Button**, **Repeat**; кнопка **Open file**.

[Докладніше на сторінці застосунку](<KeeLoq-TX>)

</div>
</div>

### Key fob TX {#shot-076}

<div class="app" markdown>
<div class="shot" markdown>
![Key fob TX](screens/076.jpg)
</div>
<div class="txt" markdown>

Передає сигнали безключового доступу з фіксованим кодом (поки лише Subaru).

- **Make**, **Command**, **Payload**.

[Докладніше на сторінці застосунку](<Key-fob-TX>)

</div>
</div>

### Hopper {#shot-077}

<div class="app" markdown>
<div class="shot" markdown>
![Hopper](screens/077.jpg)
</div>
<div class="txt" markdown>

Перестроювання частоти: передає несучу, що перебирає список частот.

- Список частот, тип (**Rand CW**), швидкість, час перебування.

[Докладніше на сторінці застосунку](<Hopper>)

</div>
</div>

### GPS Sim {#shot-078}

<div class="app" markdown>
<div class="shot" markdown>
![GPS Sim](screens/078.jpg)
</div>
<div class="txt" markdown>

Передає симульований GPS-сигнал L1 C/A (1575,42 МГц). **Підміна GPS незаконна**; можна застосовувати лише в екранованому середовищі.

- Кнопка **Open file** і прапорець **Loop**.

[Докладніше на сторінці застосунку](<GPS-Sim>)

</div>
</div>

### FlipperTX {#shot-079}

<div class="app" markdown>
<div class="shot" markdown>
![FlipperTX](screens/079.jpg)
</div>
<div class="txt" markdown>

Передає сигнали нижче 1 ГГц із файлів запису Flipper Zero (`.sub`).

- Кнопки **Browse** (вибір файлу) та **Start**.

[Докладніше на сторінці застосунку](<FlipperTX>)

</div>
</div>

### Burger Pager {#shot-080}

<div class="app" markdown>
<div class="shot" markdown>
![Burger Pager](screens/080.jpg)
</div>
<div class="txt" markdown>

Передає сигнали пейджерів гостей ресторанів (Syscall pager).

- Поле **Data**, прапорець **Scan**.

[Докладніше на сторінці застосунку](<Burger-Pager>)

</div>
</div>

### CVS Spam {#shot-081}

<div class="app" markdown>
<div class="shot" markdown>
![CVS Spam](screens/081.jpg)
</div>
<div class="txt" markdown>

Передає сигнали системи викликів CVS із файлів записів `.C16`.

- Список файлів, сторінки, кнопки **Start/Stop**, **CHAOS**.

[Докладніше на сторінці застосунку](<CVS-Spam>)

</div>
</div>

### EPIRB TX {#shot-082}

<div class="app" markdown>
<div class="shot" markdown>
![EPIRB TX](screens/082.jpg)
</div>
<div class="txt" markdown>

Передає тестові сигнали аварійних маяків 406 МГц. **Хибні сигнали лиха незаконні** — лише в закритому екранованому середовищі.

- Джерело (**Source**), тип маяка, кадр, прапорці **Resend every 50s**, **AM signal**.

[Докладніше на сторінці застосунку](<EPIRB-TX>)

</div>
</div>

### BLESpam {#shot-083}

<div class="app" markdown>
<div class="shot" markdown>
![BLESpam](screens/083.jpg)
</div>
<div class="txt" markdown>

Передає підроблені BLE-пакети (спливні вікна сполучення Apple, Google, Samsung). Може заважати чужим пристроям — використовуйте лише на власних.

- Кнопка **Start**, режим атаки (Android, iOS …).

[Докладніше на сторінці застосунку](<BLESpam>)

</div>
</div>

### BHT Xy/EP {#shot-084}

<div class="app" markdown>
<div class="shot" markdown>
![BHT Xy/EP](screens/084.jpg)
</div>
<div class="txt" markdown>

Передає протокол керування вуличним освітленням BHT (варіанти Xylos та EPAR).

- Вкладки **Xylos** і **EPAR**, поля **Header**, **City code**, **Family**, **Subfamily**, **Receiver ID**, **Relay**.

[Докладніше на сторінці застосунку](<BHT>)

</div>
</div>

### ADS-B TX {#shot-085}

<div class="app" markdown>
<div class="shot" markdown>
![ADS-B TX](screens/085.jpg)
</div>
<div class="txt" markdown>

Передає кадри Mode S транспондера ADS-B лише для симуляції. **Дуже небезпечно:** це може вплинути на справжні літаки, тож використання допустиме лише в повністю закритому ВЧ-середовищі.

- Вкладки **Position**, **Callsign**, **Speed**, **Squawk**, поле **ICAO24**.

[Докладніше на сторінці застосунку](<ADS-B(S)>)

</div>
</div>

