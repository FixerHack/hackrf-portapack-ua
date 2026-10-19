# На перший погляд

## HackRF

**Оригінальний код HackRF** лежить у `/hackrf` — це підпроєкт усередині вихідного коду. Він вказує на <https://github.com/mossmann/hackrf>.

## PortaPack

Решта коду, зокрема **portapack** та надбудови **havoc/mayhem**, лежить у `/firmware`.

Функції інтерфейсу PortaPack ⇄ HackRF — у `/firmware/baseband`.

Нижче лежить фреймворк ОС **ChibiOS/RT**: абстрактна функціональність — у `/firmware/chibios`, а конкретні драйвери й конфігурації плати PortaPack — у `/firmware/chibios-portapack`.

### Тека застосунків

Програмне забезпечення застосунків PortaPack — у `/firmware/application`.

- Інтерфейс користувача: `/firmware/application/ui`
- Застосунки (пункти в кожному меню): `/firmware/application/apps`
- Інтерфейс IC / апаратних компонентів: `/firmware/application/hw`
- Спільна функціональність протоколів: `/firmware/application/protocols`

## Інтерфейс користувача

### Меню та віджети

**Більшість меню** (окрім OPTIONS і DEBUG, які насправді є застосунками) та **спливні вікна** (yes/no, yes/cancel, ok) визначені в `/firmware/application/ui_navigation.cpp`.

Меню **Options** — насправді «застосунок», визначений у `/firmware/application/apps/ui_settings.cpp`.

Меню **Debug** (теж застосунок) визначене в `/firmware/application/apps/ui_debug.cpp`.

Віджети інтерфейсу — **кнопки, тексти, чекбокси, поля вводу** тощо — у `/firmware/common/ui_widget.cpp`.
