# Послідовна консоль USB

Прошивка PortaPack Mayhem надає послідовну консоль через USB при підключенні до комп'ютера.

Підключитися можна будь-яким терміналом: PuTTY, minicom, screen, [HTerm](https://www.der-hammer.info/). Є навіть вебтермінали (Chrome і Edge, не Firefox): <https://www.serialterminal.com/> або **<https://hackrf.app/>**.

Термінал надає оболонку ChibiOS/RT Shell.

> [!WARNING]
> **НЕ** входьте в режим HackRF (із синім екраном) під час роботи з консоллю (ні через hackrf.app, ні через інші інструменти). Пристрій має бути ввімкнений, але в звичайному режимі.

## Доступні команди

- `help` — список усіх команд.
- `exit` — завершити консоль.
- `info` — відомості про систему ChibiOS/RT.
- `systime` — час роботи в мс.
- `reboot` — перезавантажити PortaPack (працює навіть якщо кнопка reset несправна).
- `dfu` — перезавантажити в режим оновлення прошивки DFU.
- `hackrf` — запустити оригінальну прошивку HackRF (режим HackRF).
- `sd_over_usb` — запустити режим [SD Over USB](SD-Over-USB).
- `flash` — [Flash Utility](Flash-Utility).
- `screenshot` — зробити знімок екрана.
- `screenframe` — повертає вміст екрана (1 рядок / рядок екрана, кожен піксель у HEX у порядку R,G,B).
- `screenframeshort` — вміст екрана, 1 символ на піксель (формат `00RRGGBB` + 32).
- `write_memory <адреса> <значення>` — записати значення за адресою пам'яті.
- `read_memory <адреса>` — прочитати пам'ять.
- `button <N>` — симулювати натискання кнопки: 1 — вправо, 2 — вліво, 3 — вниз, 4 — вгору, 5 — Select, 6 — DFU, 7 — енкодер вліво, 8 — енкодер вправо.
- `touch <x> <y>` — емулювати дотик (0 < x < ширина, 0 < y < висота).
- `keyboard <HEX>` — емулювати натискання клавіш. Параметр — HEX-представлення клавіш. Наприклад, «Hello world»: `keyboard 48656C6C6F20776F726C64`.
- `ls` — список файлів і тек.
- `unlink` — видалити файл.
- `mkdir` — створити теку.
- `filesize` — розмір файлу.
- `fopen` — відкрити файл для читання й зміни (позиція ставиться в кінець; `fseek 0` — на початок).
- `fseek` — встановити позицію у відкритому файлі.
- `fclose` — закрити файл.
- `ftruncate` — видалити вміст після поточної позиції.
- `ftell` — показати поточну позицію.
- `fread` — прочитати n байтів (швидший двійковий варіант — `frb`).
- `fwrite` — записати байти (швидший двійковий варіант — `fwb`).
- `crc32` — CRC32 файлу.
- `rtcget` — поточні дата й час.
- `rtcset [рік] [місяць] [день] [година] [хвилина] [секунда]` — встановити дату й час (усі поля обов'язкові).
- `cpld_info <device>` — інформація про CPLD (device: `hackrf` або `portapack`).
- `cpld_read <device> <target>` — прочитати CPLD (target: `sram` лише hackrf, `eeprom`).
- `cpld_write <device> <target> <file>` — записати CPLD (підтримується лише `cpld_write portapack eeprom <file>`).
- `accessibility_readall` — текстовий список усіх віджетів на екрані (елемент у фокусі має `*`).
- `accessibility_readcurr` — опис лише віджета у фокусі.
- `applist` — застосунки, які можна запустити через `appstart` (коротка назва, повна назва, категорія).
- `appstart <коротка_назва>` — запустити застосунок (зупиняє поточні).
- `gotgps <lat> <lon> <alt> <speed> <satinuse>` — надіслати застосункам позицію (lat, lon обов'язкові, роздільник `.`).
- `gotorientation <angle>` — надіслати орієнтацію (0 — північ, 90 — схід, 400 — не задано).
- `gotenv <temperature> [humidity] [pressure] [light]` — значення датчиків середовища.
- `gotlight <light_lux>` — значення освітленості.
- `pmemreset yes` — скинути всю PMEM до типових значень.
- `sysinfo` — апаратна інформація системи.
- `radioinfo` — налаштування радіо.
- `settingsreset yes` — видалити всі INI-файли з теки налаштувань.
- `sendpocsag <addr> <msglen> [baud] [type] [function] [phase]` — відкрити POCSAG TX і надіслати повідомлення (див. [POCSAG TX](POCSAG-Tx)).
- `asyncmsg <enable|disable>` — асинхронне журналювання налагодження.
- `setfreq <Hz>` — встановити частоту радіо. Працює лише в RX-застосунках: Audio, Capture, ERT, POCSAG, APRS, Level, Looking Glass, Sonde, SubGhzD, Weather.

### Приклад sysinfo

```
ch>sysinfo
M0 heap: 32400
M0 stack: 407
M0 cpu%: 0
M4 heap: 0
M4 stack: 0
M4 miss: 0
uptime: 15
ch>
```
