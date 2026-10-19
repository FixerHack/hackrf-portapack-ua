# Збирання прошивки

Є кілька способів зібрати прошивку. Класичний спосіб описано в оригінальному документі [Building from Source](https://github.com/furrtek/portapack-havoc/wiki/Building-from-source). Проте рекомендовано **Docker** — він дає дуже чистий шлях від вихідного коду до файлу `.bin`.

У цьому розділі: [Docker і Kitematic](#using-docker-hub-and-kitematic), [командний рядок Docker](#docker-command-line-reference), [CI-платформи](#using-buddyworks-and-other-ci-platforms), [ARM на Debian](#using-arm-on-debian), [Kali Linux](#compiling-mayhem-firmware-on-kali-linux), [macOS (Homebrew)](#compiling-mayhem-firmware-on-macos).

Швидший спосіб із WSL 2 — [Як швидше компілювати у Windows з WSL 2](How-to-compile-faster-with-WSL-2). Компіляція на macOS через Docker — [Using MAC OS](Using-MAC-OS). На WSL з ninja — [Compile on WSL with ninja](Compile-on-WSL-with-ninja).

## Docker і Kitematic {#using-docker-hub-and-kitematic}

### Крок 1: підготовка середовища

1. Встановіть [Docker](https://docs.docker.com/get-docker/).
2. Отримайте [Kitematic](https://github.com/docker/kitematic/releases/).
3. Встановіть [GitHub Desktop](https://desktop.github.com/).

### Крок 2: клонування репозиторію

У Windows закінчення рядків можуть спричиняти помилки (наприклад, `'python/r' not found`). Це треба зробити **до** клонування. Налаштуйте git не змінювати закінчення рядків:

```
git config --global core.autocrlf false
```

**Важливо:** якщо хочете долучитися до проєкту, [зробіть форк репозиторію](How-to-collaborate) у свій акаунт і продовжуйте з власного форку.

Відкрийте GitHub Desktop і натисніть «Open with Github Desktop» на головній сторінці репозиторію (під кнопкою «Code»). Нарешті створіть теку `build` усередині репозиторію — у неї потраплятиме результат компіляції.

### Крок 3: підготовка контейнера Docker

> Примітка: переконайтеся, що клоновано й теку hackrf: `git submodule update --init --recursive`.

Відкрийте термінал у корені клонованого репозиторію й виконайте:

```
docker build -t portapack-dev -f dockerfile-nogit .
```

> Образ працює лише на системах x86. На ARM як обхід можна зібрати й запустити образ amd64, але він працюватиме в емуляції x86 і буде повільним: `docker build --platform linux/amd64 -t portapack-dev -f dockerfile-nogit .`

Після збирання образу поверніться в Docker, знайдіть образ у розділі Images, натисніть синю кнопку Run, розгорніть Optional Settings. `Host path` — корінь вашого репозиторію. Натисніть Run.

### Крок 4: компіляція

Щоразу при запуску підготовленого контейнера він компілює код і (у разі успіху) лишає результати в `build/firmware/`.

> Файл `*.bin` — це лише прошивка. Файл `*.ppfw.tar` містить також застосунки.

## Командний рядок Docker {#docker-command-line-reference}

Клонування:

```
git clone https://github.com/portapack-mayhem/mayhem-firmware.git
cd mayhem-firmware
git submodule update --init --recursive
```

Збирання образу:

```
docker build -t portapackccache -f dockerfile-nogit .
```

На ARM: `docker build --platform linux/amd64 -t portapack-dev -f dockerfile-nogit .`

Запуск образу для збирання прошивки (у корені репозиторію):

```
docker run -it --rm -v ${PWD}:/havoc portapackccache
```

Це запускає й одразу видаляє контейнер, щоб вони не накопичувалися. Кількість паралельних завдань: `docker run -it --rm -v ${PWD}:/havoc portapackccache -j4`.

Постійний контейнер: `docker run --name portapackbuild -it -v ${PWD}:/havoc portapackccache -j4`, потім `docker start portapackbuild`.

## CI-платформи (Buddy.Works тощо) {#using-buddyworks-and-other-ci-platforms}

Можна використати YAML-шаблон (експорт пайплайна з buddy.works) з оригінальної вікі. Якщо використовуєте командний рядок, включайте підмодулі: `git clone --recurse-submodules --remote-submodules <url>`.

## ARM на Debian {#using-arm-on-debian}

> Не перевірено на інших дистрибутивах Linux. Для зручності компілятор встановлюється в `/opt/build`.

### 1. Оновіть ОС, встановіть cmake, python, pyyaml

```
sudo apt-get update
sudo apt-get install -y git tar wget dfu-util cmake python3 bzip2 lz4 curl hackrf python3-distutils python3-setuptools
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; python3 get-pip.py
pip install pyyaml
```

### 2. Встановіть ARM-компілятор у /opt/armbin

```
sudo mkdir /opt/build
cd /opt/build
sudo wget -O gcc-arm-none-eabi.tar.bz2 'https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2020q2/gcc-arm-none-eabi-9-2020-q2-update-x86_64-linux.tar.bz2?revision=05382cca-1721-44e1-ae19-1e7c3dc96118'
sudo mkdir armbin
sudo tar --strip=1 -xjvf gcc-arm-none-eabi.tar.bz2 -C armbin
```

> Нічна система збирання використовує версію 9.2.1 (9-2019-q4-major). Вищі версії GCC дають більший образ, що може не вміститися в пам'ять.

### 3. Додайте компілятор у середовище bash

```
echo 'PATH=/opt/build/armbin/bin:/opt/build/armbin/lib:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### 4. Клонуйте репозиторій у /opt

```
cd /opt
sudo git clone --recurse-submodules https://github.com/portapack-mayhem/mayhem-firmware.git
```

### 5. Надайте права користувачу

```
sudo chown -R my_user:my_usergroup /opt/mayhem-firmware
```

### 6. Створіть makefile через cmake і скомпілюйте

```
cd /opt/mayhem-firmware
mkdir build
cd build
cmake ..
make
```

Прискорити: `make -j` (автоматично) або `make -j4`. Для тестів функцій на ПК з Linux: `make build_tests`, потім `ctest --output-on-failure`.

### 7. Прошийте HackRF

```
hackrf_spiflash -w /opt/mayhem-firmware/build/firmware/portapack-h1_h2-mayhem.bin
```

## Усе в одному скрипті для ARM на Debian {#all-in-one-script-for-arm-on-debian-host}

Усі ці команди однією дією: завантажте `compile-flash-mayhem.sh` з <https://github.com/GullCode/compile-flash-mayhem> і налаштуйте під себе.

## Збирання на Kali Linux {#compiling-mayhem-firmware-on-kali-linux}

Перевірено 21.09.2024 на Kali 2024.3. Має працювати для будь-якого дистрибутива на основі Debian.

### Залежності

```
sudo apt update
sudo apt install git tar bzip2 lz4 wget curl cmake python3 python3-setuptools python3-distutils-extra python3-yaml dfu-util hackrf
```

### ARM-toolchain

Якщо версія не 9.2.1, cmake попередить про невідповідність компілятора. GCC 13 створює більший образ, який може не вміститися в пам'ять.

```
sudo mkdir /opt/build
sudo chown $USER:$(id -gn $USER) /opt/build
cd /opt/build
wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019q4/gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2
mkdir armbin
tar --strip=1 -xjvf gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2 -C armbin
```

Kali використовує ZSH. Додайте компілятор:

```
echo 'PATH=/opt/build/armbin/bin:/opt/build/armbin/lib:$PATH' >> ~/.zshrc
source ~/.zshrc
```

(На Debian за замовчуванням Bash — пишіть у `~/.bashrc`.)

### Клонування й збирання

```
cd ~; mkdir git; cd git
git clone https://github.com/portapack-mayhem/mayhem-firmware/ --recurse-submodules
cd mayhem-firmware
mkdir build; cd build
cmake ..
make clean && make
```

Для першого разу `make clean &&` не обов'язковий, але знадобиться, якщо компіляція перервалася.

## Збирання на macOS (Homebrew) {#compiling-mayhem-firmware-on-macos}

Перевірено на macOS Sequoia (березень 2025).

### Залежності

```bash
brew update
brew install git cmake python3 ninja dfu-util binutils hackrf lz4

python3 -m venv ~/portapack_env
source ~/portapack_env/bin/activate
pip install pyyaml

echo 'export PATH="/opt/homebrew/opt/binutils/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### ARM GCC toolchain

```bash
cd ~/Downloads
curl -L -o gcc-arm-none-eabi-9-2019-q4-major-mac.tar.bz2 "https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major-mac.tar.bz2"
tar -xjf gcc-arm-none-eabi-9-2019-q4-major-mac.tar.bz2
sudo mkdir -p /usr/local/arm
sudo mv gcc-arm-none-eabi-9-2019-q4-major /usr/local/arm/
echo 'export PATH="/usr/local/arm/gcc-arm-none-eabi-9-2019-q4-major/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
arm-none-eabi-gcc --version
```

### Клонування

```bash
sudo mkdir -p /opt
cd /opt
sudo git clone --recurse-submodules https://github.com/portapack-mayhem/mayhem-firmware.git
sudo chown -R $(whoami):staff /opt/mayhem-firmware
```

### Зміна скрипта для сумісності з macOS

```bash
cd /opt/mayhem-firmware/firmware/tools
cp make_spi_image.py make_spi_image.py.bak
```

У `make_spi_image.py` знайдіть рядок із `subprocess.check_output(['readelf', ...])` і замініть `readelf` на `/opt/homebrew/opt/binutils/bin/greadelf`.

### Збирання з Ninja

```bash
cd /opt/mayhem-firmware
mkdir -p build; cd build
cmake -G Ninja ..
ninja
```

### Прошивання

> hackrf.app **НЕ працює** на macOS — прошивайте вручну (`hackrf_spiflash`).

### Усунення несправностей

- Попередження «Apple could not verify…» — System Preferences → Security & Privacy → «Allow Anyway».
- Якщо помилки збирання — спробуйте звичайний make (`cmake .. && make`) замість Ninja.
