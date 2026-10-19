# Прошивка Mayhem на «голий» HackRF

## Файл прошивки зі сторінки релізів GitHub і класична утиліта hackrf_spiflash

> [!Note]
> ⚠️ Цей посібник стосується «голого» HackRF, а не HackRF із PortaPack.

Завантажте останню прошивку зі сторінки [релізів](https://github.com/portapack-mayhem/mayhem-firmware/releases/latest).

### Windows

1. Підключіть пристрій через USB.
2. Двічі клацніть `mayhem_flasher.bat` і дотримуйтесь інструкцій.
3. Перезавантажте пристрій.

### Linux

1. Підключіть пристрій через USB.
2. Завантажте прошивку командою `hackrf_spiflash -w new_firmware_file.bin` (наприклад, `portapack-h1_h2-mayhem.bin` для прошивки Mayhem або `hackrf_one_usb.bin` для стокової прошивки HackRF).
3. Перезавантажте пристрій.

> [!NOTE]
> Користувачам Ubuntu та Mint: дистрибутиви на основі Ubuntu ніколи не підтримують свій репозиторій із пакетом хост-клієнта HackRF (CLI) в актуальному стані. Ви зіткнетеся з безліччю дивних проблем, якщо ваш HackRF має ревізію R9. Щоб їх розв'язати, зберіть пакет HackRF самостійно або скористайтеся іншим дистрибутивом.

### macOS

1. За потреби встановіть інструменти HackRF: `brew install hackrf`
2. Підключіть пристрій через USB.
3. Завантажте прошивку командою `hackrf_spiflash -w new_firmware_file.bin`.
4. Перезавантажте пристрій.
