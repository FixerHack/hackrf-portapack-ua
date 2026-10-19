# Оновлення Xilinx CPLD на платі HackRF

Починаючи з версії HackRF 2021.03.1, CPLD оновлюється разом із процесом оновлення прошивки через SPI і DFU. Для старіших версій CPLD потрібно (і тепер можна) оновити вручну:

1. Клонуйте оригінальний проєкт HackRF на комп'ютер:
    ```
    git clone https://github.com/greatscottgadgets/hackrf
    ```
2. Якщо їх немає, встановіть інструменти HackRF — див. [Оновлення прошивки](Update-firmware) (розділ про `hackrf_spiflash`) або [Встановлення ПЗ HackRF](hackrf/installing_hackrf_software). Процес встановлює всі потрібні інструменти.
3. Підключіть PortaPack до комп'ютера, переведіть його в [режим HackRF](HackRF) і виконайте команду оновлення CPLD:
    ```
    hackrf_cpldjtag -x hackrf/firmware/cpld/sgpio_if/default.xsvf
    ```

**Блимання світлодіодів LED1/2/3 означає, що CPLD запрограмовано успішно.** Постійне світіння LED3 (червоного) — помилка.

Дочекайтеся повідомлення «Write finished», після чого вимкніть / від'єднайте PortaPack від комп'ютера.
