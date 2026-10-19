# Режим HackRF

Пункт **HackRF** у головному меню перемикає пристрій із прошивки Mayhem у стандартний режим HackRF. У цьому режимі PortaPack працює як звичайний HackRF One, повністю сумісний з GNU Radio, GQRX, SDR# та будь-яким іншим програмним забезпеченням, що підтримує HackRF через USB, — без додаткового перепрошивання чи модифікацій.

## Перехід у режим HackRF

Виберіть **HackRF** у головному меню. З'явиться діалог підтвердження:

> *«This mode enables HackRF functionality. To return, press the reset button.»*
> (Цей режим вмикає функціональність HackRF. Щоб повернутися, натисніть кнопку reset.)

Виберіть **Yes**, щоб підтвердити. Інтерфейс Mayhem завершить роботу, а керування перейме прошивка HackRF.

> [!NOTE]
> У режимі HackRF усі органи керування PortaPack — диск енкодера, кнопки та сенсорний екран — неактивні. Під час запуску дисплей показує статичну блок-схему, а після підключення SDR-застосунку через USB додає значення в реальному часі.

## Версія прошивки в режимі HackRF

У режимі HackRF `hackrf_info` усе одно повідомляє версію прошивки Mayhem, наприклад:

```
─$ hackrf_info
hackrf_info version: 2024.02.1
libhackrf version: 2024.02.1 (0.9)
Found HackRF
Index: 0
Serial number: 00000000000000009xxxxxxxxxxxxxx3
Board ID Number: 2 (HackRF One)
Firmware Version: n_250606 (API:1.08)
Part ID Number: 0xa000cb3c 0x0066476c
Hardware Revision: r10
Hardware does not appear to have been manufactured by Great Scott Gadgets.
Hardware supported by installed firmware:
    HackRF One
```

Це очікувана поведінка: USB-інтерфейс HackRF надається образом прошивки Mayhem, тому рядок версії відображає Mayhem, а не оригінальну прошивку HackRF.

## Вимоги до драйверів

**Linux / macOS:** HackRF підтримується «з коробки» пакетом `libhackrf`. Встановіть його через менеджер пакунків (наприклад, `sudo apt install hackrf`, `brew install hackrf`), і пристрій буде розпізнано автоматично.

**Windows:** Windows за замовчуванням не містить драйвера HackRF. Потрібно встановити драйвер WinUSB за допомогою Zadig:

1. Завантажте й запустіть Zadig з https://zadig.akeo.ie.
2. Виберіть **Options → List All Devices**.
3. Виберіть **HackRF One** у випадному списку.
4. Виберіть драйвер **WinUSB** і натисніть **Install Driver** або **Replace Driver**.

Після встановлення HackRF розпізнаватимуть GQRX (через GNU Radio), SDR# та `hackrf_transfer`.

> [!NOTE]
> Якщо ви раніше використовували PortaPack із застосунком [SD Over USB](SD-Over-USB) у Windows, пристрою вже може бути призначено інший драйвер. Zadig дозволяє його замінити.

## Повернення до Mayhem

Щоб повернутися до прошивки Mayhem, натисніть кнопку **RESET** — вона розташована зверху на PortaPack, крайня (права). Її точне розташування дивіться в розділі [Огляд апаратної частини](Hardware-overview).

> [!NOTE]
> Програмного способу вийти з режиму HackRF немає. Повернути пристрій у Mayhem може лише кнопка RESET.

## Сфери застосування

Режим HackRF корисний, коли потрібно користуватися HackRF безпосередньо з SDR-програмами на ПК — наприклад, GQRX або SDR# для широкосмугового моніторингу, потокових схем GNU Radio або `hackrf_transfer` для необробленого запису та відтворення з командного рядка.

| PortaPack у режимі HackRF | Режим HackRF, підключений до gqrx |
| --- | --- |
| ![hackrf_mode_1_basic_small](https://github.com/user-attachments/assets/fa02f7db-c505-40ce-8fed-f62cd8b5348d) | ![hackrf_mode_2_gqrx_small](https://github.com/user-attachments/assets/535f4e09-debe-48c2-8571-21e37825b66f) |
