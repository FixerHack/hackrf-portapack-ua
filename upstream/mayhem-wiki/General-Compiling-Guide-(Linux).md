# Notes
- This guide is for in case you are using some sort of not so common Linux distro, and you are expert, and you wanna compile on your Linux machine.
- This guide is only for experts, it won't offer any step by step instructions. 
- If you are using any Debian or Debian based distro, or you are using Arch Linux, use it's dedicated guide.

# Core Concepts
- This program using cmake as building system
- cmake scripts called arm-none-eabi-gcc toolchain (note that it's called "gcc" but it contains the whole c/cpp toolchain).
- cmake scripts called some linker scripts to implement the external app feature
- cmake scripts called some python scripts during building to generate some not so regular file structure.

# "Steps"
1. make sure you satisfied git submodule
2. make sure you got the correct arm-none-eabi-gcc toolchain from arm website or your package manager (it's a group of executable) and you are allowed to use any methods you want to have the system environment (and cmake) to be able to run it
3. We already supported Ninja and ccache, if you want use them.
4. finally just simply use the regular compile way for regular cmake project: `mkdir build && cd build && cmake .. && make`
