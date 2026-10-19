# HackRF Pro

26 червня 2025 року Great Scott Gadgets анонсували **HackRF Pro** — довгоочікуване оновлення HackRF One 2014 року. Сторінка продукту: <https://greatscottgadgets.com/hackrf/pro/>

Попри багато нових можливостей, розробники подбали про зворотну сумісність. Основні характеристики:

- робоча частота від 100 кГц до 6 ГГц;
- налаштування від 0 Гц до 7,1 ГГц;
- напівдуплексний трансівер;
- до 20 мільйонів відліків за секунду;
- 8-бітові квадратурні відліки;
- сумісність з GNU Radio, SDR# та іншими;
- програмно налаштовувані підсилення RX/TX та фільтр основної смуги;
- ВЧ-роз'єм SMA, входи/виходи тактового сигналу SMA;
- High-Speed USB 2.0 з роз'ємом Type-C;
- живлення від USB, апаратне забезпечення з відкритим кодом.

Порівняно з [HackRF One](Original-GSG-HackRF-One), HackRF Pro має: ширший діапазон частот, рівнішу частотну характеристику, роз'єм USB Type-C, вбудований TCXO, логіку на енергоефективній FPGA замість CPLD, усунення DC-сплеску, режим розширеної точності з 16-бітовими відліками, режим половинної точності з 4-бітовими відліками до 40 Мвибірок/с, більше RAM і флеш-пам'яті, встановлене екранування, входи/виходи запуску (trigger), покращене керування живленням і захист ВЧ-порту, можливість апаратно вимкнути передавання.

Загальний опис — у розділі [Можливості та характеристики](Features).

## PortaPack з HackRF Pro

Хоча 4 МБ флеш-пам'яті (замість 1 МБ) звучить чудово, це дає побічні ефекти. Помилка `Request exceeds size of flash memory` при прошиванні, найімовірніше, означає застарілі hackrf-tools:

```
$ hackrf_info
hackrf_info version: 2024.02.1+
No HackRF boards found.
```

Має бути щось на кшталт `hackrf_info version: git-afb42968`. Оновіть hackrf-tools.

## Збирання прошивки

Розробка ще триває, тож не всі функції Mayhem працюють. Якщо хочете спробувати, процес майже такий самий, лише компілятору вказується нова плата:

```
git clone https://github.com/portapack-mayhem/mayhem-firmware/ --recursive
cd mayhem-firmware/
cmake .. -DBOARD="PRALINE"
```

Докладніше про збирання — [Збирання прошивки](Compile-firmware).

## Оновлення hackrf-tools

Найновіші HackRF Tools підтримують HackRF Pro. У Linux:

```
git clone https://github.com/greatscottgadgets/hackrf
mkdir hackrf/host/build; cd hackrf/host/build
cmake ..
make
sudo make install
sudo ldconfig
```

Для Windows і macOS — див. [інструкції GSG](https://github.com/greatscottgadgets/hackrf/blob/main/host/README.md).

## Режим DFU (відновлення)

За інструкцією GSG: від'єднайте USB (знеструмте HackRF), натисніть і утримуйте DFU, підключіть живлення, тримайте DFU, доки не засвітиться світлодіод 3.3V. Для версії OpenSourceSDRLab процес той самий, але світлодіод 3.3V не засвітиться — проте пристрій буде видно на комп'ютері як `1fc9:000c NXP Semiconductors LPC4330FET180 ... (device firmware upgrade mode)`.

Далі можна прошити базову прошивку в RAM через `dfu-util` і поверх — звичайну Mayhem через `hackrf_spiflash`.
