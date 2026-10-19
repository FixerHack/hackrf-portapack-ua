> [!NOTE]  
> ccache is default disabled because it creats issues in particular situation.  
> If you are aware its pros and cons and you insist enable it, following this guide: https://github.com/portapack-mayhem/mayhem-firmware/wiki/Notes-About-ccache  
> If you don't know what's this, just use default.

1. Update your system:

```sh
   sudo apt-get update
   sudo apt-get upgrade
```

2. Install dependencies:

```sh
   sudo apt-get install -y git tar wget dfu-util cmake python3 ccache bzip2 liblz4-tool curl ninja-build python3-pip
```

3. Install pip and pyyaml:

```sh
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py --break-system-packages
   sudo python3 get-pip.py
   pip install pyyaml --break-system-packages
```

4. Set up environment variables:

```sh
   export LANG=C.UTF-8
   export LC_ALL=C.UTF-8
```

5. Download and install the ARM toolchain:

```sh
   mkdir -p /opt/build
   cd /opt/build
   wget -O gcc-arm-none-eabi.tar.bz2 "https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019q4/gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2?revision=108bd959-44bd-4619-9c19-26187abf5225&la=en&hash=E788CE92E5DFD64B2A8C246BBA91A249CB8E2D2D"
   sudo mkdir armbin
   sudo tar --strip=1 -xjvf gcc-arm-none-eabi.tar.bz2 -C armbin
```

6. Add the ARM toolchain to your PATH:

```sh
   echo 'export PATH=$PATH:/opt/build/armbin/bin' >> ~/.bashrc
   source ~/.bashrc
```

7. Clone the PortaPack Mayhem repository (if you haven't already):

```sh
   sudo git clone --recurse-submodules https://github.com/portapack-mayhem/mayhem-firmware.git
   cd mayhem-firmware
   sudo chmod -R 777 ~/mayhem-firmware
```

8. Create a build directory and run CMake:

```sh
   mkdir build
   cd build
   cmake -G Ninja ..
```

9. Build the firmware:

```sh
   ninja
```
