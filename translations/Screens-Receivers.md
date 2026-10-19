<!-- згенеровано scripts/gen_app_pages.py з scripts/apps_data.py — правте дані там -->
# Приймачі: огляд застосунків

!!! info "Скріншоти з вашого пристрою"
    Усі знімки зроблено на HackRF One + PortaPack H2 з прошивкою Mayhem v2.4.0. Більшість застосунків показано у стані «за замовчуванням», до приймання чи передавання. Опис складено за вікі Mayhem та екранами; дрібні відмінності залежать від версії прошивки.

У меню **Receive** — застосунки для приймання й декодування сигналів. Поля `0 32 32` у верхній частині екрана — це **AMP / LNA / VGA** (ВЧ-підсилювач, малошумний підсилювач і підсилювач основної смуги), див. [Основні елементи керування](Main-Controls).

## Меню Receive

### Receive — сторінка 1 {#shot-002}

<div class="app" markdown>
<div class="shot" markdown>
![Receive — сторінка 1](screens/002.jpg)
</div>
<div class="txt" markdown>

Пункти меню: ADS-B, AIS Boats, APRS, Audio, BLE Rx, POCSAG, Radiosonde, TPMS RX, Search, SubGhzD, Weather, Level, WeFax, Time Sink, SubCar, SSTV RX, Scanner, RTTY.


</div>
</div>

### Receive — сторінка 2 {#shot-003}

<div class="app" markdown>
<div class="shot" markdown>
![Receive — сторінка 2](screens/003.jpg)
</div>
<div class="txt" markdown>

Пункти меню: SSTV RX, Scanner, RTTY, ProtoView, NRF, NOAA APT, Morse, ACARS, gfxEQ, FPV Detect, Fox Hunt, Radio, FLEX RX, ERT Meter, EPIRB RX, Detector, Analog TV, AFSK.


</div>
</div>

## Застосунки

### ADS-B RX {#shot-017}

<div class="app" markdown>
<div class="shot" markdown>
![ADS-B RX](screens/017.jpg)
</div>
<div class="txt" markdown>

Приймає сигнали транспондерів літаків ADS-B на 1090 МГц і показує список повітряних суден.

- Стовпці списку: **ICAO/Call** (адреса/позивний), **Lvl** (рівень сигналу), **Spd** (швидкість), **Amp**, **Hit** (кількість прийнятих пакетів), **Age** (час від останнього пакета).
- Вибравши літак, можна відкрити деталі та показати його на карті (потрібна карта світу на SD-карті).
- Навіть коротка антена приймає ADS-B, якщо ввімкнено ВЧ-підсилювач (AMP = 1).

[Докладніше на сторінці застосунку](<Automatic-dependent-surveillance–broadcast-(ADS-B)>)

</div>
</div>

### AIS RX (кораблі) {#shot-018}

<div class="app" markdown>
<div class="shot" markdown>
![AIS RX (кораблі)](screens/018.jpg)
</div>
<div class="txt" markdown>

Декодує дані морських суден системи AIS на VHF 161,975 МГц (канал 87B) або 162,025 МГц (канал 88B).

- **Ch** — вибір каналу, **MMSI** і **Name/Call** — колонки списку суден.

[Докладніше на сторінці застосунку](<AIS-Boats>)

</div>
</div>

### APRS RX {#shot-019}

<div class="app" markdown>
<div class="shot" markdown>
![APRS RX](screens/019.jpg)
</div>
<div class="txt" markdown>

Приймає й показує пакети APRS (позиційні звіти й повідомлення радіоаматорів).

- Дві вкладки: **Stream** (потік) і **List** (список станцій); частота на скріншоті — 144,3900 МГц (США); у Європі — 144,800 МГц.

[Докладніше на сторінці застосунку](<APRS-RX>)

</div>
</div>

### Audio RX {#shot-020}

<div class="app" markdown>
<div class="shot" markdown>
![Audio RX](screens/020.jpg)
</div>
<div class="txt" markdown>

Універсальний аудіоприймач: AM, NFM, WFM, SSB, а також режим **SPEC** (спектр). Основний застосунок для прослуховування сигналів.

- Зверху — режим (**NFM**), частота, підсилення, смужка рівня й гучність.
- **Step 25kHz** — крок налаштування; нижче — водоспад із шкалою смуги (±20 кГц).
- Червоне коло зліва — кнопка запису звуку.

[Докладніше на сторінці застосунку](<Audio-Receivers>)

</div>
</div>

### BLE RX {#shot-021}

<div class="app" markdown>
<div class="shot" markdown>
![BLE RX](screens/021.jpg)
</div>
<div class="txt" markdown>

Сканує рекламні пакети Bluetooth Low Energy (2,4 ГГц) і показує список пристроїв за MAC-адресами.

- Кнопки **Clear**, **Export CSV**, **Tx**; прапорці **Name**, **Log**, **USB Log**, **Duplicate**; сортування й фільтр за вмістом пакета.
- Вибрав запис — відкриється детальний вигляд останнього пакета.

[Докладніше на сторінці застосунку](<Bluetooth-Low-Energy-Receiver>)

</div>
</div>

### POCSAG RX {#shot-022}

<div class="app" markdown>
<div class="shot" markdown>
![POCSAG RX](screens/022.jpg)
</div>
<div class="txt" markdown>

Приймає повідомлення пейджерів POCSAG (512/1200/2400 бод).

- Типова частота — 466,1750 МГц (на скріншоті); у радіоаматорів поширена 439,9875 МГц.
- Кнопки **Filter**, **Last**, **Config** (налаштування модему та фільтрів).

[Докладніше на сторінці застосунку](<POCSAG-Receiver>)

</div>
</div>

### Radiosonde {#shot-023}

<div class="app" markdown>
<div class="shot" markdown>
![Radiosonde](screens/023.jpg)
</div>
<div class="txt" markdown>

Декодує телеметрію метеозондів (RS41, M10, M20, M2K2): ідентифікатор, температура, вологість, тиск, висота, координати GPS.

- Типова частота — 402,7 МГц.
- Поля **Type**, **ID**, **Temp**, **Humidity**, **Pressure**, **Lat/Lon** заповнюються після прийому зонда; є прапорці **Log** і **CRC**.

[Докладніше на сторінці застосунку](<Radiosonde>)

</div>
</div>

### TPMS RX {#shot-024}

<div class="app" markdown>
<div class="shot" markdown>
![TPMS RX](screens/024.jpg)
</div>
<div class="txt" markdown>

Приймає й декодує датчики тиску в шинах (TPMS) на 315/433,9 МГц.

- Колонки: **Tp** (тип датчика), **ID**, **Pres** (тиск), **Temp**, **Cnt**, **Fl** (прапорці).
- Одиниці тиску: kPa, PSI, BAR.

[Докладніше на сторінці застосунку](<TPMS-RX>)

</div>
</div>

### Search {#shot-025}

<div class="app" markdown>
<div class="shot" markdown>
![Search](screens/025.jpg)
</div>
<div class="txt" markdown>

Безперервно скануює діапазон частот за допомогою ШПФ і зупиняється на сигналах, що перевищують поріг. Звук не демодулює, лише реєструє частоту й тривалість.

- **Min/Max** — діапазон пошуку, **Trig** — поріг виявлення (Mean + Trig), **Snap to** — округлення знайденої частоти до кроку.
- Прапорець **LOG** записує CSV на SD-карту.

[Докладніше на сторінці застосунку](<Search>)

</div>
</div>

### Level {#shot-026}

<div class="app" markdown>
<div class="shot" markdown>
![Level](screens/026.jpg)
</div>
<div class="txt" markdown>

Вимірювач рівня сигналу: RSSI, потужність у дБ, показник насичення та графік історії.

- Режими AM / NFM / WFM / SPEC, налаштовувана смуга **BW**.

[Докладніше на сторінці застосунку](<Level>)

</div>
</div>

### Weather {#shot-027}

<div class="app" markdown>
<div class="shot" markdown>
![Weather](screens/027.jpg)
</div>
<div class="txt" markdown>

Декодує безпроводові датчики метеостанцій (температура, вологість) у ISM-діапазонах.

- Типова частота 433,920 МГц; колонки **Type**, **Temp**, **Hum**, **Ch**, **Age**.
- Підказка: для початку спробуйте AMP 0, LNA 32, VGA 20.

[Докладніше на сторінці застосунку](<Weather>)

</div>
</div>

### SubGhzD {#shot-028}

<div class="app" markdown>
<div class="shot" markdown>
![SubGhzD](screens/028.jpg)
</div>
<div class="txt" markdown>

Пасивний декодер OOK/AM-пультів (ворота, гаражні двері, дверні дзвінки) нижче 1 ГГц — розпізнає понад 40 протоколів.

- Частота за замовчуванням — 433,92 МГц.
- Список: **Type** (протокол), **Bits** (довжина кадру), **Age** (секунд від останнього прийому).
- **Clear** очищає список, **Log** записує CSV на SD-карту.

[Докладніше на сторінці застосунку](<SubGhzD>)

</div>
</div>

### WeFax (WeatherFax) {#shot-029}

<div class="app" markdown>
<div class="shot" markdown>
![WeFax (WeatherFax)](screens/029.jpg)
</div>
<div class="txt" markdown>

Приймає КХ-метеофакс (радіофакс) — картки погоди, які передаються аналоговим способом.

- Поля **LPM** (рядків за хвилину) та **IOC**; кнопка **Start** запускає запис зображення у BMP на SD-карту.
- HackRF слабо приймає КХ напряму — краще використовувати апконвертер і хорошу КХ-антену.

[Докладніше на сторінці застосунку](<WeatherFax>)

</div>
</div>

### Time Sink {#shot-030}

<div class="app" markdown>
<div class="shot" markdown>
![Time Sink](screens/030.jpg)
</div>
<div class="txt" markdown>

«Осцилограф» для радіо: показує компоненту I сигналу IQ у часовій області.

- **SR** — частота дискретизації, **DEC** — децимація (швидкість оновлення), **TRIG**/**LVL** — тригер.

[Докладніше на сторінці застосунку](<Time-Sink>)

</div>
</div>

### SubCar {#shot-031}

<div class="app" markdown>
<div class="shot" markdown>
![SubCar](screens/031.jpg)
</div>
<div class="txt" markdown>

Декодує сигнали автомобільних брелоків безключового доступу (Suzuki, VW, Subaru, Kia, Ford, Fiat, BMW).

- Режим демодуляції: **AM** (за замовчуванням) або **FM**; частота 433,92 МГц (Європа).

[Докладніше на сторінці застосунку](<SubCar>)

</div>
</div>

### RTTY RX {#shot-032}

<div class="app" markdown>
<div class="shot" markdown>
![RTTY RX](screens/032.jpg)
</div>
<div class="txt" markdown>

Декодує радіотелетайп (RTTY, код Бодо/ITA2) і виводить текст у реальному часі.

- Швидкість передавання (**Baud**) визначається автоматично або вручну.

[Докладніше на сторінці застосунку](<RTTY-RX>)

</div>
</div>

### Scanner (за списком) {#shot-033}

<div class="app" markdown>
<div class="shot" markdown>
![Scanner (за списком)](screens/033.jpg)
</div>
<div class="txt" markdown>

Сканер частот за списком із блокуванням на каналі, де є сигнал.

- Режим **SCAN** (список частот) / **SRCH** (пошук між початком і кінцем), великі цифри частоти змінюють колір: сірий — сканування, жовтий — перевірка, зелений — захоплено.
- Детальний розбір екрана — на анотованому зображенні в розділі [Інтерфейс](ui-guide.md).

[Докладніше на сторінці застосунку](<Scanner>)

</div>
</div>

### Scanner (пошук) {#shot-034}

<div class="app" markdown>
<div class="shot" markdown>
![Scanner (пошук)](screens/034.jpg)
</div>
<div class="txt" markdown>

Той самий Scanner, але в режимі пошуку між початковою й кінцевою частотою з вибраним кроком.

- Кнопка **SWITCH** перемикає між режимами; **AUDIO** вмикає звук; **ADD FQ/DEL FQ** додає/видаляє частоту зі списку.

[Докладніше на сторінці застосунку](<Scanner>)

</div>
</div>

### SSTV RX {#shot-035}

<div class="app" markdown>
<div class="shot" markdown>
![SSTV RX](screens/035.jpg)
</div>
<div class="txt" markdown>

Приймає зображення SSTV (телебачення з повільним скануванням) і зберігає його у BMP на SD-карті.

- Режим (на екрані — **Scottie 2**), кнопка **Start RX**.

[Докладніше на сторінці застосунку](<SSTV-RX>)

</div>
</div>

### ProtoView {#shot-036}

<div class="app" markdown>
<div class="shot" markdown>
![ProtoView](screens/036.jpg)
</div>
<div class="txt" markdown>

Візуалізатор «сирих» OOK/ASK-імпульсів у вигляді графіка; корисний для невідомих сигналів.

- **Zoom** — масштаб за часом (мкс на піксель), **Reset** — скинути буфер, **Pause/Resume** — заморозити та роздивитися сигнал.

[Докладніше на сторінці застосунку](<ProtoView>)

</div>
</div>

### NRF RX {#shot-037}

<div class="app" markdown>
<div class="shot" markdown>
![NRF RX](screens/037.jpg)
</div>
<div class="txt" markdown>

Декодує пакети чипів nRF24L01+ на 2,4 ГГц (бездротові клавіатури, миші, пульти). Підтримує лише режим 250 кбіт/с.

- Частота = 2400 + номер каналу МГц (за замовчуванням 2480 МГц); кнопка **Modem setup**.

[Докладніше на сторінці застосунку](<decoder-for-NRF24L01>)

</div>
</div>

### NRF RX (прийняті дані) {#shot-038}

<div class="app" markdown>
<div class="shot" markdown>
![NRF RX (прийняті дані)](screens/038.jpg)
</div>
<div class="txt" markdown>

Той самий застосунок: приклад прийнятого пакета — адреса (**addr**) і дані (**data**) у шістнадцятковому вигляді.


[Докладніше на сторінці застосунку](<decoder-for-NRF24L01>)

</div>
</div>

### NOAA APT {#shot-039}

<div class="app" markdown>
<div class="shot" markdown>
![NOAA APT](screens/039.jpg)
</div>
<div class="txt" markdown>

Приймає аналогові зображення APT із метеосупутників NOAA (137 МГц). *Усі три супутники NOAA POES виведено з експлуатації у 2025 році, тож сигналу вже немає.*

- Кнопка **Start**; напис *Image arriving* означає очікування зображення.

[Докладніше на сторінці застосунку](<NOAA>)

</div>
</div>

### gfxEQ {#shot-040}

<div class="app" markdown>
<div class="shot" markdown>
![gfxEQ](screens/040.jpg)
</div>
<div class="txt" markdown>

Широкосмуговий FM-приймач із графічним еквалайзером на весь екран (11 смуг, 20 кольорових тем).

- Кнопка **MOOD** перемикає тему; частота за замовчуванням — 93,1 МГц.

[Докладніше на сторінці застосунку](<gfxEQ>)

</div>
</div>

### ACARS {#shot-041}

<div class="app" markdown>
<div class="shot" markdown>
![ACARS](screens/041.jpg)
</div>
<div class="txt" markdown>

Декодує повідомлення авіаційної лінії передавання даних ACARS на VHF (131,825 МГц) і виводить їх у консоль.

- Прапорець **LOG** записує повідомлення в `LOGS/ACARS.TXT`.

[Докладніше на сторінці застосунку](<ACARS>)

</div>
</div>

### Morse RX {#shot-042}

<div class="app" markdown>
<div class="shot" markdown>
![Morse RX](screens/042.jpg)
</div>
<div class="txt" markdown>

Автоматично визначає тон і швидкість та декодує азбуку Морзе (CW) у текст.

- Поля **Squelch**, **Speed (wpm)**, **Tone**, **Log**.

[Докладніше на сторінці застосунку](<Morse-RX>)

</div>
</div>

### FPV Detect {#shot-043}

<div class="app" markdown>
<div class="shot" markdown>
![FPV Detect](screens/043.jpg)
</div>
<div class="txt" markdown>

Виявляє аналогові FPV-відеопередавачі дронів на 5,8 ГГц у діапазонах A, B, E, F, R і визначає канал.

- Режими **AutoScan** та ручний; показує RSSI/SNR і перевіряє знайдені канали.

[Докладніше на сторінці застосунку](<FPV-Detect>)

</div>
</div>

### Fox Hunt {#shot-044}

<div class="app" markdown>
<div class="shot" markdown>
![Fox Hunt](screens/044.jpg)
</div>
<div class="txt" markdown>

Допомога в «полюванні на лисиць» (радіопеленгація AM-джерела): графік рівня сигналу в реальному часі.

- Кнопки **Mark** (поставити маркер із GPS/компасом) і **Clear**; частота змінюється кроком 100 Гц.

[Докладніше на сторінці застосунку](<Fox-Hunt>)

</div>
</div>

### Radio {#shot-045}

<div class="app" markdown>
<div class="shot" markdown>
![Radio](screens/045.jpg)
</div>
<div class="txt" markdown>

Мовний приймач AM/NFM/WFM із 10 швидкими слотами обраних частот.

- Кнопки-слоти (на скріншоті порожні — 87,0 МГц), **Save** зберігає поточну частоту в слот, **MODE: WFM**, смуга **200k**.

[Докладніше на сторінці застосунку](<Radio>)

</div>
</div>

### Radio (інший знімок) {#shot-046}

<div class="app" markdown>
<div class="shot" markdown>
![Radio (інший знімок)](screens/046.jpg)
</div>
<div class="txt" markdown>

Той самий застосунок Radio; зверху видно звукову хвилю приймання.


[Докладніше на сторінці застосунку](<Radio>)

</div>
</div>

### EPIRB RX {#shot-047}

<div class="app" markdown>
<div class="shot" markdown>
![EPIRB RX](screens/047.jpg)
</div>
<div class="txt" markdown>

Декодує аварійні маяки COSPAS-SARSAT 406 МГц (EPIRB, PLB, ELT) із виправленням помилок BCH.

- Кнопки **Map**, **Clear**, **Log**; статус — «Listening… Beacons: 0».

[Докладніше на сторінці застосунку](<EPIRB-RX>)

</div>
</div>

### ERT Meter {#shot-048}

<div class="app" markdown>
<div class="shot" markdown>
![ERT Meter](screens/048.jpg)
</div>
<div class="txt" markdown>

Декодує показання комунальних лічильників за протоколом ERT (діапазон 902–928 МГц).

- Частота за замовчуванням — 911,6 МГц; колонки списку: **ID**, **Tp**, **Consumpt**, **Temp**, **Ct**.

[Докладніше на сторінці застосунку](<ERT>)

</div>
</div>

### FLEX RX {#shot-049}

<div class="app" markdown>
<div class="shot" markdown>
![FLEX RX](screens/049.jpg)
</div>
<div class="txt" markdown>

Декодує пейджинговий протокол FLEX (1600/3200/6400 бод): адреса пейджера (capcode) і текст повідомлення.


[Докладніше на сторінці застосунку](<Flex-Rx>)

</div>
</div>

### Detector {#shot-050}

<div class="app" markdown>
<div class="shot" markdown>
![Detector](screens/050.jpg)
</div>
<div class="txt" markdown>

Швидке виявлення сигналів за списками частот: LoRa, пульти, аплінк TETRA. Подає звуковий сигнал при перевищенні порогу.

- Пресет (на екрані — TETRA UP 380–390 МГц), графік потужності, RSSI.

[Докладніше на сторінці застосунку](<Detector>)

</div>
</div>

### Analog TV {#shot-051}

<div class="app" markdown>
<div class="shot" markdown>
![Analog TV](screens/051.jpg)
</div>
<div class="txt" markdown>

Приймає чорно-біле аналогове відео PAL (AM). Цифрове ТБ не підтримується.

- Крок налаштування **Step 25kHz**.

[Докладніше на сторінці застосунку](<Analog-TV-Receiver>)

</div>
</div>

### AFSK RX {#shot-052}

<div class="app" markdown>
<div class="shot" markdown>
![AFSK RX](screens/052.jpg)
</div>
<div class="txt" markdown>

Експериментальний AFSK-декодер. Жорстко налаштований на модем LCR/TEDI (467,225 МГц, Bell 202), на інших сигналах виводить випадкові символи.

- Прапорець **Log**, кнопка **Modem setup**, внизу — налагоджувальний потік символів.

[Докладніше на сторінці застосунку](<AFSK>)

</div>
</div>

