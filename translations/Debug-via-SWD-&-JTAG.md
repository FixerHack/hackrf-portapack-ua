# Налагодження через SWD і JTAG

> Якщо вам потрібне просте налагодження (лише вивід змінних/векторів/символів, без точок зупину й перегляду регістрів), скористайтеся [Налагодженням через послідовний порт](Debug-with-serial) — для початківців воно, _можливо_, простіше.

## (1) Налагодження через SWD

Писати код без можливості налагодження дуже затратно за часом — ви майже наосліп. PortaPack — вбудована система, і для зручності потрібна певна підготовка.

### Arm Debug Interface (ADI)

ADI — специфікація і апаратного, і логічного інтерфейсу налагодження між хостом і пристроями. Більшість сучасних процесорів реалізує ADIv5. ADI визначає порт доступу до налагодження (DAP), що складається з порту налагодження (DP) і портів доступу (AP). DP включає фізичне з'єднання (JTAG, SWD) і вбудовані регістри; кожен AP має свої з'єднання із системою й власні регістри.

### LPC43xx

Наш двоядерний мікроконтролер LPC4320 підтримує JTAG і Serial Wire Debug (SWD), послідовне трасування, вісім точок зупину й чотири точки спостереження.

Щодо Black Magic Probe автор зазначає: «Можна під'єднатися до M0 замість M4, якщо використати `jtag_scan` замість `swdp_scan`, але минулого разу BMP мав помилки при роботі з M0».

### Що потрібно

- **Black Magic Probe** або щось подібне (bluepill STM32F103C8T6 теж працює — при збиранні blackmagic додайте `BLUEPILL=1`). [HackRF](https://hackrf.readthedocs.io/en/latest/LPC43XX_Debugging.html) має список сумісного обладнання. У прикладі використано [Jeff Probe](https://flirc.tv/products/flirc-jeffprobe) з PortaPack H2+ в алюмінієвому корпусі. BMP і Jeff Probe — це поєднані апаратно-програмні проєкти з відкритим кодом: на апаратному рівні — інтерфейси JTAG і SWD для ARM Cortex-A/M; на програмному — gdb-сервер і прошивач флешу.
- **Інструменти**: паяльник, пінцет, викрутки, дриль, [лещата](https://uk.wikipedia.org/wiki/Лещата), мультиметр, напилок, гострий зір, тверді руки, канцелярський ніж.
- Ваш PortaPack.
- **Pin header** 2×5 крок 1.27 мм.

### Під'єднання порту налагодження

Спершу розберіть PortaPack (багато гвинтів) і знайдіть порт налагодження `LPC_JTAG`.

> Стрілка на платі вказує на PIN 1. Завжди під'єднуйте кабель правильно: зіставляйте позначений на платі PIN 1 з червоною смужкою на кабелі.

- **PortaPack без батареї:** припаяйте 10-піновий JTAG-конектор з боку A й лишіть плаский FFC-кабель всередині.
- **Пристрій із вбудованою батареєю** (місця немає) — два варіанти:
  1. Припаяти pin header і вже ніколи не змогти закрити PortaPack.
  2. Припаяти з тильного боку (боку B).

### Піни тепер «задом наперед»

> Якщо pin header на тильному боці, кабель правильно під'єднати неможливо, бо піни перевернуті: замість 1,2,3,…,10 буде 2,1,4,3,6,5,8,7,10,9.

Розберіть стрічковий кабель і виправте перевернутість: тримайте пари проводів разом, вставте назад, перекрутивши кожну пару, і стисніть докупи лещатами (обережно). Зробіть [перевірку цілісності](https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-test-for-continuity) мультиметром.

### Перший тест

Коли pin header і кабель готові, під'єднайте HackRF і батарею, увімкніть PortaPack. Jeff Probe також засвітиться світлодіодами. Після цього можна зібрати PortaPack назад, окрім задньої кришки.

### Фінальний штрих

Два варіанти:
1. Лишити задню кришку знятою під час налагодження (між кришкою й пінами покладіть щось непровідне, наприклад [ізоляційну стрічку](https://uk.wikipedia.org/wiki/Ізоляційна_стрічка)).
2. Зробити порт завжди доступним, просвердливши отвір у задній кришці.

## Використання gdb (клієнт)

Коли все налаштовано, під'єднайте gdb до LPC4320:

1. Запустіть `arm-none-eabi-gdb`.
   > ЗАУВАЖЕННЯ: для роботи запустіть застосунок ADS-B RX на пристрої.
2. Під'єднайтеся до пробника:
   - `target extended-remote \\.\COM4` (Windows — потрібний COM-порт дивіться в диспетчері пристроїв);
   - `target extended-remote /dev/ttyACM0` (Linux — допоможуть `dmesg`/`lsusb`).
   > Після під'єднання BMP/Jeff Probe з'являються два віртуальні послідовні порти: один для gdbserver, інший — звичайний TTL-UART. Пристрої реалізують клас CDC, драйвери Linux вбудовані. Шляхи — `/dev/ttyACM*`.
3. Перевірте версію прошивки пробника: `monitor version`.
4. Проскануйте пристрої: `monitor swdp_scan`.
5. Під'єднайтеся: `attach 1`.
6. Завантажте символи: `file build/firmware/baseband/baseband_adsbrx.elf`.
7. Огляньтеся: `info threads`, `info registers`, `tui enable`, `continue`.

### Обмеження та проблеми

- M0, схоже, недоступний через SWD (для налагодження M0 потрібен JTAG).
- Інтеграція з VSCode досить «глючна».
- Після зупинки налагодження Jeff Probe треба вимкнути з живлення, щоб він знову запрацював.

## Інтеграція у VSCode

> ЗАУВАЖЕННЯ: WSL на Windows має проблеми з прокиданням USB-пристрою в linux-хост. Автор використовував VSCode на Windows із розширенням «Remote - SSH» до старого ноутбука з Ubuntu, куди Jeff Probe під'єднувався напряму.

Створіть `.vscode/launch.json`. У лівій панелі оберіть «Debug» → «create a launch.json file» і замініть вміст на:

```json
{
    "version": "0.2.0",
    "configurations": [
    {
        "name": "(gdb) JTAG probe",
        "type": "cppdbg",
        "request": "launch",
        "miDebuggerPath": "arm-none-eabi-gdb",
        "targetArchitecture": "arm",
        "program": "${workspaceRoot}/build/firmware/baseband/baseband_adsbrx.elf",
        "cwd": "${workspaceRoot}",
        "setupCommands": [
            {"text": "file '${workspaceRoot}/build/firmware/baseband/baseband_adsbrx.elf'"},
            {"text": "target extended-remote /dev/ttyACM0"},
            {"text": "monitor swdp_scan"},
            {"text": "attach 1"}
        ],
        "launchCompleteCommand": "None",
        "externalConsole": false
    }
    ]
}
```

> На Linux за помилки прав доступу з'ясуйте групу файлу (`ls -la /dev/ttyA*`) і додайте користувача в неї: `sudo gpasswd -a ваше_імя dialout`.

Налаштування точок зупину й під'єднання без них працюють погано, тож зробимо це вручну в коді. Додайте макрос десь у `firmware/baseband/proc_adsbrx.cpp`:

```c
#define HALT_IF_DEBUGGING()                              \
  do {                                                   \
    if ((*(volatile uint32_t *)0xE000EDF0) & (1 << 0)) { \
      __asm("bkpt 1");                                   \
    }                                                    \
} while (0)
```

і викликайте його всередині циклу. Потім: зберіть прошивку → прошийте → запустіть застосунок ADS-B RX → під'єднайте Jeff Probe → запустіть профіль налагодження. Воно має зупинитися на точці зупину; F10 — крок по коду.

## Нотатки про уніфікований JTAG / SWD

ARM надає SWJ-DP (serial wire/jtag debug port) через технологію CoreSight, що відображає піни SWD на лінії тактування й скидання JTAG. Це дозволяє використовувати обидва протоколи на одному фізичному з'єднанні (але не одночасно).

SWD — альтернатива JTAG для мікроконтролерів з малою кількістю пінів (частина ADIv5). На фізичному рівні потрібні щонайменше дві лінії (плюс земля), на відміну від п'яти для JTAG: тактування (SWCLK, керується пробником) і двонапрямлена лінія даних (SWDIO). Трасування йде окремою (опційною) лінією TRACESWO.

У SWD піни TDI й TDO з JTAG замінено одним двонапрямленим SWDIO; пін TMS прибрано; тактування (TCK) лишилося (перейменоване на SWCLK). Отже, SWD використовує лише два піни замість чотирьох. Є три фази зв'язку: запит пакета, підтвердження, передача даних. До запитів і передачі застосовується перевірка парності. Перед обслуговуванням потрібна послідовність ініціалізації, частина якої — перемикання протоколу з JTAG на SWD (вимагається навіть для Cortex, що не підтримують JTAG).

## (2) Налагодження через JTAG (M0/M4) з FT232H

### Обладнання

1. Купіть багатофункціональний модуль USB-to-UART **FT232H** (підтримує RS232/422/485, FIFO, FT1248, JTAG, SPI, I2C). Чип FT232H, швидкість UART до 12 Мбод, драйвери VCP/D2XX.
2. Підготуйте кабелі для під'єднання 4 проводів + GND від конектора HackRF до FT232H:
   - AD0 → TCK
   - AD1 → TDI
   - AD2 → TDO
   - AD3 → TMS
   - GND → GND

   Для зручності можна скористатися перехідним PCB. Альтернативно є готовий адаптер `hackrf_jtag_adapter_v01` (файли для JLCPCB і початковий проєкт KiCad є в англійській вікі).

### OpenOCD

3. Встановіть пакет OpenOCD. Щоб перевірити з'єднання, увімкніть HackRF, під'єднайте FT232H до USB і виконайте:
   ```
   openocd -f /usr/share/openocd/scripts/interface/ftdi/um232h.cfg -f target/lpc4350.cfg
   ```
   Має з'явитися вивід, де виявлено M4 і M0:
   ```
   Info : JTAG tap: lpc4350.m4 tap/device found: 0x4ba00477 (ARM Ltd)
   Info : JTAG tap: lpc4350.m0 tap/device found: 0x0ba01477 (ARM Ltd)
   Info : [lpc4350.m4] Cortex-M4 r0p1 detected — 6 breakpoints, 4 watchpoints
   Info : [lpc4350.m0] Cortex-M0 r0p0 detected — 2 breakpoints, 1 watchpoint
   Info : gdb server for lpc4350.m4 on 3333
   Info : gdb server for lpc4350.m0 on 3334
   ```

### VSCode

4. Додайте в `launch.json` конфігураційні блоки для M4 і M0 JTAG. Їх можна тримати поряд з блоком SWD Jeff Probe — щоразу перед налагодженням під'єднуйте потрібний пробник і обирайте відповідний блок.
   - **M4:** оновлюйте `.elf` відповідно до proc-файлу, який налагоджуєте (напр. `baseband_weather.elf`); максимум 6 точок зупину, 4 спостереження.
   - **M0:** `application.elf` оновлювати не треба — він спільний для всіх застосунків; максимум 2 точки зупину, 1 спостереження.

Порада Bernd: якщо оптимізатор «викидає» потрібне для діагностики, вимкніть його для однієї функції:

```c
void __attribute__((optimize("O0"))) foo(unsigned char data) {
    // код
}
```

### Приклад launch.json для OpenOCD з FT232H

```json
{
    "version": "0.2.0",
    "configurations": [
    {
        "name": "(gdb) OpenOCD m4 baseband",
        "type": "cppdbg",
        "request": "launch",
        "program": "${workspaceRoot}/build/firmware/baseband/baseband_sd_over_usb.elf",
        "cwd": "${workspaceRoot}",
        "externalConsole": false,
        "MIMode": "gdb",
        "miDebuggerPath": "arm-none-eabi-gdb",
        "targetArchitecture": "arm",
        "debugServerPath": "openocd",
        "debugServerArgs": "-f interface/ftdi/um232h.cfg  -f target/lpc4350.cfg -c \"gdb_breakpoint_override hard\"",
        "serverStarted": "Listening on port [0-9]+ for gdb connections",
        "launchCompleteCommand": "None",
        "postRemoteConnectCommands": [
            {"text": "target extended-remote :3333"},
            {"text": "set remote hardware-watchpoint-limit 2"},
            {"text": "set remote hardware-breakpoint-limit 4"},
            {"text": "monitor [target current] configure -event gdb-detach { shutdown }"}
        ],
        "stopAtConnect": false,
        "useExtendedRemote": true
    },
    {
        "name": "(gdb) OpenOCD m0 application",
        "type": "cppdbg",
        "request": "launch",
        "program": "${workspaceRoot}/build/firmware/application/application.elf",
        "cwd": "${workspaceRoot}",
        "externalConsole": false,
        "MIMode": "gdb",
        "miDebuggerPath": "arm-none-eabi-gdb",
        "targetArchitecture": "arm",
        "debugServerPath": "openocd",
        "debugServerArgs": "-f interface/ftdi/um232h.cfg  -f target/lpc4350.cfg -c \"gdb_breakpoint_override hard\"",
        "serverStarted": "Listening on port [0-9]+ for gdb connections",
        "launchCompleteCommand": "None",
        "postRemoteConnectCommands": [
            {"text": "target extended-remote :3334"},
            {"text": "set remote hardware-watchpoint-limit 1"},
            {"text": "set remote hardware-breakpoint-limit 2"},
            {"text": "monitor [target current] configure -event gdb-detach { shutdown }"}
        ],
        "stopAtConnect": false,
        "useExtendedRemote": true
    }
    ]
}
```
