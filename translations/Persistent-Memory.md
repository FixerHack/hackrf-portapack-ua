# Постійна пам'ять

Це частина **підсистеми RTC (годинника реального часу)** всередині чипа LPC43xx на платі PortaPack.

## Підсистема RTC

Підсистема RTC підтримує хід годинника (дата/час) від резервної монетної батарейки (яку потрібно [встановити](Hardware-overview#portapack-internals) на платі PortaPack), навіть коли пристрій не під'єднаний до USB-живлення. Окрім RTC, та сама батарейка тримає постійною невелику область SRAM на живленні VBAT (0x40041000, 256 байтів) для збереження налаштувань стану системи при вимкненні.

Карта постійної пам'яті визначена в `/firmware/chibios-portapack/os/hal/platforms/LPC43xx/lpc43xx.inc`:

```
LPC_RTC_DOMAIN_BASE       (0x40040000)
LPC_ALARM_TIMER_BASE      (+ 0x0000)
LPC_BACKUP_REG_BASE       (+ 0x1000) <- область backup_ram!
LPC_POWER_MODE_CTRL_BASE  (+ 0x2000)
LPC_CREG_BASE             (+ 0x3000)
LPC_EVENT_ROUTER_BASE     (+ 0x4000)
LPC_OTP_CTRL_BASE         (+ 0x5000)
LPC_RTC_BASE              (+ 0x6000)
```

## Область backup_ram

**backup_ram** — невеликий обсяг RAM (лише 256 байтів), визначений у `/firmware/common/memory_map.hpp` через мітку **LPC_BACKUP_REG_BASE**, тобто починається з адреси **0x40041000**.

### Структура data_t

Прошивка PortaPack зберігає в backup_ram кілька змінних uint32_t (і одну uint64_t) всередині структури `data_t`, оголошеної в `/firmware/common/portapack_persistent_memory.cpp`.

### Змінні в постійній пам'яті

В **оригінальному PortaPack** зберігалося лише кілька конфігураційних змінних; пізніше версія **HAVOC** від furrtek розширила це кількома новими параметрами. Серед них — `uint32_t config_t`, що зберігає кілька булевих прапорців.

У версії **MAYHEM** додано два нових булевих параметри, особливо корисних для користувачів H1: «**Speaker is present**» (наявність динаміка) і «**Back Buttons on menus**» (кнопка «назад» у меню). Їх реалізовано як два нових чекбокси в OPTIONS → UI.

Ці два параметри додано до змінної `uint32_t ui_config`, яка тепер розкладена так:

### Позиції бітів ui_config

- 31 (HAVOC) заставка (splash screen)
- 30 (HAVOC) логін
- 29 (HAVOC) старт у прихованому режимі (stealth)
- 28 (**гілка MAYHEM H1**) кнопка «..» (назад) у кожному меню
- 27 (**гілка MAYHEM H1**) вивід на динамік (модель H1 приймає динамік)

### Використання двох нових булевих значень

Доступ з будь-якого місця — додайте (якщо ще немає) include:

```cpp
#include "portapack_persistent_memory.hpp"
```

а потім перевіряйте стан:

```cpp
portapack::persistent_memory::config_backbutton()
portapack::persistent_memory::config_speaker()
```

Вони повертають TRUE або FALSE залежно від налаштування.
