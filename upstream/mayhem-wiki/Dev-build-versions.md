We are trying to work out what is the most recent version we can update to while making it so all devs can still develop using the version on their OS/distro.

Developer testing with various GCC compiler and hardware versions demonstrates code stability, and helps suss out intermittent issues such as timing issues or uninitialized memory.  But, particularly if the nightly build system uses a different GCC version from most developers, a developer-testing phase may be needed for future firmware release candidates before the worldwide release announcement.

Note that higher GCC versions contain larger libraries that consume more of our limited ROM space.

| Dev      | GCC Version | Platform     | Issues|
|----------|-------------|--------------|--------------|
| Stable/nightly | 9.2.1       | ubuntu:20.04 | ADSB fails in v1.8.0 (some claim other versions too TBD) |
| @jlynx   | 9.4.0       | Ubuntu (WSL) | None (That I am aware of) |
| @u-foka | 13.2.1       | M1 Mac | File size too big |
| @notherngineer | 9.3.1       | Debian 11 | None |
| @bernd-herzog | 9.2.1 | ubuntu:22 | None |
| @zxkmm |13.2.0|Arch Linux on X86_64 PC (Intel Core i7-8Gen*h)| Image size too big |
| @zxkmm |13.2.0|Manjaro Linux on X86_64 PC (Intel Core i3-3Gen)| Image size too big|
| @zxkmm |10.3-2021.10-aarch64|Armbian on Amlogic S905D Cortex-A53 microchip|Image size too big|
