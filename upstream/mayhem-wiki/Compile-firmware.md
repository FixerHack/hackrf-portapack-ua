There are severals ways to compile the firmware. As the traditional way, check the original [Building from Source](https://github.com/furrtek/portapack-havoc/wiki/Building-from-source) document, however, Docker is recommended because it provides a very clean way to go from source to a `.bin` file.

[Using Docker and Kitematic](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Compile-firmware#using-docker-hub-and-kitematic)

[Docker command-line reference](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Compile-firmware#docker---command-line-reference)

[Using Buddyworks and other CI platforms](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Compile-firmware#using-buddyworks-and-other-ci-platforms)

[Notes for Buddy.Works (and other CI platforms)](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Compile-firmware#notes-for-buddyworks-and-other-ci-platforms)

[Using ARM on Debian host](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Compile-firmware#using-arm-on-debian)

[All in one script for ARM on Debian host](https://github.com/portapack-mayhem/mayhem-firmware/wiki/Compile-firmware#all-in-one-script-for-arm-on-debian-host)

# Using Docker Hub and Kitematic

## Step 1: Prepare environment
1. Install [Docker](https://docs.docker.com/get-docker/)
2. Get [Kitematic](https://github.com/docker/kitematic/releases/)
3. Install [GitHub Desktop](https://desktop.github.com/)

## Step 2: Clone the repository

If you are using Windows, line endings may produce some errors. For example: `'python/r' not found` messages are product of a problem with the line endings. This must be done prior to cloning the repository for compilation to succeed. To prevent this, configure git to not manipulate these line endings, open a terminal and execute:
y
`git config --global core.autocrlf false`

You can also check the current configuration by omitting the `false` at the end of the command.

[[img/git_linefeed.png|600px]]

**Important:** If you want to collaborate to the project, [Fork the repository](How-to-collaborate#fork-the-repository) to your own account and continue this instructions from your own fork.

Open Github Desktop, and click "Open with Github Desktop" from the main page of the repository (or your fork), under the button "Code". 

[[img/github_clone.png|400px]]

Finally, create a `build` folder inside of the repository. From Github Desktop, just click "Repository / Show in Explorer" and create an empty folder named `build`. This folder will be used for the compilation output.

## Step 3: Prepare the Docker container
_Note: You need to make sure you have also cloned the hackrf folder. to do that run: ```git submodule update --init --recursive```_


Open up a terminal in the root of the cloned git repo and run: ```docker build -t portapack-dev -f dockerfile-nogit . ```

_(the image only works on x86 systems, if you are running docker on an arm system, as a workaround, you can get it build and run an amd64 image but it will run in x86 emulation and will be slow. To make the amd64 image use: ```docker build --platform linux/amd64 -t portapack-dev -f dockerfile-nogit . ```)_

After its built the docker image, go back to docker and you should see this screen under images
![image](https://user-images.githubusercontent.com/4393979/159808543-bac63e5f-8fe3-48af-a469-f940e4690767.png)

Click on the blue run button and then click the dropdown to expand Optional Settings.

Make sure they look like this:

![image](https://user-images.githubusercontent.com/4393979/159808716-b9956308-5f76-4efa-bc89-8fc6f79752b8.png)

`Host path` is the root of your repo.

After that click run!

_Note: Come across a `/usr/bin/env: ‘python\r’: No such file or directory` error? RTFM and go back to step 2 https://github.com/portapack-mayhem/mayhem-firmware/wiki/Compile-firmware#step-2-clone-the-repository_


## Step 4: Compile!

Everytime you run the container you prepared in the previous step, it will compile the source and (if successful) leave the results in `build/firmware/`  
Note: The *.bin file is just the firmware. The *.ppfw.tar file also contains the apps.

[[img/Kitematic_uvIvGXRbFR.png|600px]]

If you have additional questions, please check [this guide](Using-MAC-OS).

# Docker - Command line reference

If you are inclined for using the command line, you can try the following:
* Clone the repository and submodules:
```
git clone https://github.com/portapack-mayhem/mayhem-firmware.git
cd mayhem-firmware
git submodule update --init --recursive
```
* For building the docker image:
`docker build -t portapackccache -f dockerfile-nogit .`  
On an system with an ARM processor: `docker build --platform linux/amd64 -t portapack-dev -f dockerfile-nogit .`

* For running the image to build firmware (in the root of the repo):
`docker run -it --rm -v ${PWD}:/havoc portapackccache` \
This runs and then immediatelly deletes the container, so that they arent pile up in your docker instance.

  * You can specify the number of jobs to run in parallel during compilation. 
    To speed up the build specify the number of cores available: ```docker run -it --rm -v ${PWD}:/havoc portapackccache -j4```

  * Alternatively if you want to have a single persistent container, and just execute it when necessary

    * Create the persistent container (it will also build the firmware once): ```docker run --name portapackbuild -it -v ${PWD}:/havoc portapackccache -j4```

    * Run the existing container: ```docker start portapackbuild```

_You no longer have to create a `build` folder before running the image._

# Using Buddy.Works (and other CI platforms)

You can use the following _yml _as your template for your CI platform (pipeline export from [buddy.works](https://buddy.works/)):

```
- pipeline: "Build firmware"`
  `trigger_mode: "ON_EVERY_PUSH"`
  `ref_name: "master"`
  `ref_type: "BRANCH"`
  `auto_clear_cache: true`
  `trigger_condition: "ALWAYS"`
  `actions:`
  `- action: "Build Docker image"`
    `type: "DOCKERFILE"`
    `dockerfile_path: "dockerfile-nogit"`
    `do_not_prune_images: true`
    `trigger_condition: "ALWAYS"`
  `- action: "Execute: mkdir build"`
    `type: "BUILD"`
    `working_directory: "/buddy/portapack-havoc"`
    `docker_image_name: "library/ubuntu"`
    `docker_image_tag: "18.04"`
    `execute_commands:`
    `- "mkdir -p build"`
    `volume_mappings:`
    `- "/:/buddy/portapack-havoc"`
    `trigger_condition: "ALWAYS"`
    `shell: "BASH"`
  `- action: "Run Docker Image"`
    `type: "RUN_DOCKER_CONTAINER"`
    `use_image_from_action: true`
    `volume_mappings:`
    `- "/:/havoc"`
    `trigger_condition: "ALWAYS"`
    `shell: "SH"
```

## Notes for Buddy.Works (and other CI platforms)

If you decide to [ignore this guide](https://github.com/portapack-mayhem/mayhem-firmware/issues/75) and use the command line instead, you will need to include submodules

    git clone --recurse-submodules --remote-submodules <url>



# Using ARM on Debian

* Untested on other linux flavors

* Thanks to @aj#3566 from discord for it 

* For convenience the compiler will be installed to /opt/build

* Needed steps
1. Update a Debian based OS
2. Install the necessary ARM compiler to /opt/armbin (if not done before)
3. Link ARM compiler to your bash environment
4. Clone Mayhem repository from GitHub (if not done before)
5. Giver user permission to the Mayhem repository
6. Create makefile through cmake and compile
7. Flash the firmware

* Once done you only need to call 'make' in the /opt/portapack-mayhem/firmware/build directory

* You can speed up the building process by calling 'make -j 8' instead, where 8 is the number of physical CPU cores (if you have 
some compiling errors to check it's better to call it without '-j 8')

* **Use the following commands while logged into your every day user profile. :)**

## 1. Update a Debian based OS, install cmake, python, pyyaml

    sudo apt-get update
    sudo apt-get install -y git tar wget dfu-util cmake python3 bzip2 lz4 curl hackrf python3-distutils python3-setuptools
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; python3 get-pip.py
    pip install pyyaml

## 2. Install the necessary ARM compiler to /opt/armbin (if not done before)

    sudo mkdir /opt/build
    cd /opt/build
    sudo wget -O gcc-arm-none-eabi.tar.bz2 'https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2020q2/gcc-arm-none-eabi-9-2020-q2-update-x86_64-linux.tar.bz2?revision=05382cca-1721-44e1-ae19-1e7c3dc96118&la=en&hash=D7C9D18FCA2DD9F894FD9F3C3DC9228498FA281A'
    sudo mkdir armbin
    sudo tar --strip=1 -xjvf gcc-arm-none-eabi.tar.bz2 -C armbin

_Download an up to date version here if you want to try: https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads_
_The nightly build/release system is using version 9.2.1, known as 9-2019-q4-major, found here: https://developer.arm.com/downloads/-/gnu-rm_
_Don't forget to change the paths or filenames accordingly _

## 3. Link ARM compiler to your bash environment

    echo 'PATH=/opt/build/armbin/bin:/opt/build/armbin/lib:$PATH' >> ~/.bashrc
    source ~/.bashrc

## 4. Clone the eried's mayhem repository from GitHub (if not done before) into /opt

    cd /opt
    sudo git clone --recurse-submodules https://github.com/portapack-mayhem/mayhem-firmware.git

## 5. Give permission for the portapack-mayhem directory to your user 

    sudo chown -R my_user:my_usergroup /opt/mayhem-firmware

## 6. Create makefile through cmake and compile (it's important to call the PATH cmd in step 3 just before making the cmake)
    
    cd /opt/mayhem-firmware
    mkdir build
    cd build
    cmake ..
    make

If you want, use -j argument to increase the compile speed, for example `make -j` to auto decide the numbers of threads to compile, or manually set the thread numbers, for example `make -j4`

Developers wishing to test selected functions in the firmware code by running them on their linux PC can also use the command `make build_tests` and then `ctest --output-on-failure` to run the tests.

## 7. Flash the firmware to HackRF

    hackrf_spiflash -w /opt/portapack-mayhem/build/firmware/portapack-h1_h2-mayhem.bin

# All in one script for ARM on Debian host

If you want to have all these commands in one go, go to https://github.com/GullCode/compile-flash-mayhem and download compile-flash-mayhem.sh  and adjust it to fit your needs 

# Other Toolsets
- [Linux Aarch64 gcc-arm-none-eabi-9-2020-q2-update-aarch64-linux.tar.bz2](https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2020q2/gcc-arm-none-eabi-9-2020-q2-update-aarch64-linux.tar.bz2?revision=7166404a-b4f5-4598-ac75-e5f8b90abb09&rev=7166404ab4f54598ac75e5f8b90abb09&hash=07EE5CACCCE77E97A1A8C049179D77EACA5AD4E5)
- [Toolsets archive](https://developer.arm.com/downloads/-/gnu-rm)
- [Compilation error after changing toolsets](https://github.com/portapack-mayhem/mayhem-firmware/issues/420)


# Compiling Mayhem Firmware on Kali Linux
Tested at 21. Sept. 2024 on Kali 2024.3 kali-rolling  
Should work for any Debian based Distribution, see comments.  

## Download and install dependencies
```
sudo apt update
sudo apt install git tar bzip2 lz4 wget curl cmake python3 python3-setuptools python3-distutils-extra python3-yaml dfu-util hackrf
```

In many distributions the tool `hackrf` is provided, but outdated because of the release policy. Kali is rolling release, so does not follow this restrictions.  
If you have a R9 or newer HackRF and need a newer version, I recommended to download and compile it by yourself. Source: https://github.com/greatscottgadgets/hackrf

## Download and install the ARM toolchain
If you use another Version as 9.2.1, the mayham cmake warns you:
> WARNING: Compiler version mismatch, please use the official compiler version 9.2.1 when sharing builds! Current compiler version: 13.2.1

It might compile. From other projects, as Proxmark3 or Chameleon Ultra, we know the gcc-arm-none-eabi in version 13 (provided by various distributions) creates a bigger firmware image, which won't fit into the memory. Even if it compiles without error, the firmware file is useless.

```
sudo mkdir /opt/build
sudo chown $USER:$(id -gn $USER) /opt/build
cd /opt/build
wget https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019q4/gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2
mkdir armbin
tar --strip=1 -xjvf gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2 -C armbin
```

I recommend to adjust the user rights at the first possible moment. Work as root as less as possible.   
If more than one person works in the system, feel free to set the group to something more generic. For example `src` or `staff`.

Source for the newest toolcain: https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads  
Source for deprecated toolchain: https://developer.arm.com/downloads/-/gnu-rm


### Set toolchain as default
```
echo 'PATH=/opt/build/armbin/bin:/opt/build/armbin/lib:$PATH' >> ~/.zshrc
source ~/.zshrc
```

Kali Linux uses [ZSH](https://en.wikipedia.org/wiki/Z_shell) as default shell. On [Debian](https://wiki.debian.org/Shell) is Bash the default shell, so if you are using Debian or changed the default shell, you need to pipe the echo into ~/.bashrc (or the related [rc file](https://en.wikipedia.org/wiki/Configuration_file))

## Get the Firmware from Github
```
cd ~
mkdir git
cd git
git clone https://github.com/portapack-mayhem/mayhem-firmware/ --recurse-submodules
```

Personal Note:
> You could work at any place, for example `/opt`. The [FHS](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) says `/usr/src` would be the right place for source codes. But this would be in `/` and most systems I know got roundabout 20 to 50 GB for `/` and several 100 GB for `/home`, so I decide to work with git in /home.


## Build the firmware
```
cd ~/git/mayhem-firmware
mkdir build
cd build
cmake ..
make clean && make
```

For the first compile `make clean &&` is not necessary. But if the compilation stops of any reason, you need to use clean. If nothing is there, it won't hurt.


# Compiling Mayhem Firmware on macOS

Tested on macOS Sequoia (March 2025)

## Install dependencies

```bash
# Install required packages via Homebrew
brew update
brew install git cmake python3 ninja dfu-util binutils hackrf lz4

# Set up Python environment
python3 -m venv ~/portapack_env
source ~/portapack_env/bin/activate
pip install pyyaml

# Add binutils to your PATH
echo 'export PATH="/opt/homebrew/opt/binutils/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## Download and install the ARM GCC toolchain

```bash
# Download the ARM GCC toolchain
cd ~/Downloads
curl -L -o gcc-arm-none-eabi-9-2019-q4-major-mac.tar.bz2 "https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major-mac.tar.bz2"

# Extract and install the toolchain
tar -xjf gcc-arm-none-eabi-9-2019-q4-major-mac.tar.bz2
sudo mkdir -p /usr/local/arm
sudo mv gcc-arm-none-eabi-9-2019-q4-major /usr/local/arm/

# Add the toolchain to your PATH
echo 'export PATH="/usr/local/arm/gcc-arm-none-eabi-9-2019-q4-major/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Verify installation
arm-none-eabi-gcc --version
```

## Clone the repository

```bash
# Create directory and clone the repository
sudo mkdir -p /opt
cd /opt
sudo git clone --recurse-submodules https://github.com/portapack-mayhem/mayhem-firmware.git

# Set ownership
sudo chown -R $(whoami):staff /opt/mayhem-firmware
```

## Modify script for macOS compatibility

You'll need to modify a Python script to work with macOS:

```bash
cd /opt/mayhem-firmware/firmware/tools
cp make_spi_image.py make_spi_image.py.bak
```

Open `make_spi_image.py` in your text editor and locate line 134, which should contain:
```python
output = subprocess.check_output(['readelf', '-p', '.comment', elf_file])
```

Change it to:
```python
output = subprocess.check_output(['/opt/homebrew/opt/binutils/bin/greadelf', '-p', '.comment', elf_file])
```

## Build the firmware with Ninja

```bash
cd /opt/mayhem-firmware
mkdir -p build
cd build
cmake -G Ninja ..
ninja
```

## Flash the firmware to HackRF
Note, https://hackrf.app WILL NOT WORK on macOS. You must flash manually. 

## Troubleshooting

- If you encounter "Apple could not verify..." warnings, go to System Preferences > Security & Privacy and click "Allow Anyway"
- If you experience build errors, try using the regular make system with `cmake .. && make` instead of Ninja
