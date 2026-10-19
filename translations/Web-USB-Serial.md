# WebUSB serial не працює в Linux

Якщо WebUSB serial (наприклад, сайт [hackrf.app](https://hackrf.app/)) не працює в браузері Linux, перевірте такі поширені причини:

1. **Права доступу.** Linux за замовчуванням обмежує доступ до USB-пристроїв. Переконайтеся, що ваш користувач у групах `dialout` і `plugdev` (доступ до послідовних портів і USB). Додати користувача:
    ```
    sudo usermod -aG dialout $USER
    sudo usermod -aG plugdev $USER
    ```
    Після цього вийдіть із сеансу й увійдіть знову.
2. **Правила udev.** Деяким USB-пристроям потрібні власні правила udev для правильних прав. Створіть у `/etc/udev/rules.d/` файл `53-hackrf.rules` з таким вмістом:
    ```
    ATTR{idVendor}=="1d50", ATTR{idProduct}=="604b", SYMLINK+="hackrf-jawbreaker-%k", MODE="660", GROUP="plugdev"
    ATTR{idVendor}=="1d50", ATTR{idProduct}=="6089", SYMLINK+="hackrf-one-%k", MODE="660", GROUP="plugdev"
    ATTR{idVendor}=="1d50", ATTR{idProduct}=="cc15", SYMLINK+="rad1o-%k", MODE="660", GROUP="plugdev"
    ATTR{idVendor}=="1fc9", ATTR{idProduct}=="000c", SYMLINK+="nxp-dfu-%k", MODE="660", GROUP="plugdev"
    ```
    Потім перезавантажте правила: `sudo udevadm control --reload-rules && sudo udevadm trigger`.
3. **Сумісність браузера.** Не всі браузери Linux повністю підтримують WebUSB. Найстабільніша підтримка — у Chrome (або браузерах на основі Chromium). Використовуйте актуальну версію Chrome чи Edge.
4. **Версія ОС.** Підтримка WebUSB залежить від дистрибутива й версії ядра. Оновлення до останньої стабільної версії може розв'язати проблеми сумісності.
5. **Дозволи в Chrome.** Chrome може вимагати явного дозволу на доступ до USB-пристроїв. Перевірте: `chrome://settings/content/usbDevices`.
6. **Налаштування безпеки браузера.** Розширення чи налаштування приватності можуть блокувати WebUSB. Вимкніть розширення або спробуйте вікно інкогніто.
7. **Кабель чи порт.** Перевірте USB-кабель і порт на іншому пристрої або з іншим кабелем.
