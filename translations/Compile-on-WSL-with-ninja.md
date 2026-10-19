# Збирання на WSL з ninja

> [!NOTE]
> ccache за замовчуванням вимкнено, бо в окремих ситуаціях він спричиняє проблеми. Якщо ви розумієте плюси й мінуси й усе одно хочете його ввімкнути — див. [Нотатки про ccache](Notes-About-ccache). Якщо не знаєте, що це, — лишіть за замовчуванням.

1. Оновіть систему:
    ```sh
    sudo apt-get update
    sudo apt-get upgrade
    ```
2. Встановіть залежності:
    ```sh
    sudo apt-get install -y git tar wget dfu-util cmake python3 ccache bzip2 liblz4-tool curl ninja-build python3-pip
    ```
3. Встановіть pip і pyyaml:
    ```sh
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py --break-system-packages
    sudo python3 get-pip.py
    pip install pyyaml --break-system-packages
    ```
4. Встановіть змінні середовища:
    ```sh
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
    ```
5. Завантажте й встановіть ARM-toolchain:
    ```sh
    mkdir -p /opt/build
    cd /opt/build
    wget -O gcc-arm-none-eabi.tar.bz2 "https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019q4/gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2"
    sudo mkdir armbin
    sudo tar --strip=1 -xjvf gcc-arm-none-eabi.tar.bz2 -C armbin
    ```
6. Додайте toolchain у PATH:
    ```sh
    echo 'export PATH=$PATH:/opt/build/armbin/bin' >> ~/.bashrc
    source ~/.bashrc
    ```
7. Клонуйте репозиторій:
    ```sh
    sudo git clone --recurse-submodules https://github.com/portapack-mayhem/mayhem-firmware.git
    cd mayhem-firmware
    sudo chmod -R 777 ~/mayhem-firmware
    ```
8. Створіть теку build і запустіть CMake:
    ```sh
    mkdir build
    cd build
    cmake -G Ninja ..
    ```
9. Зберіть прошивку:
    ```sh
    ninja
    ```
