For this we are using clang format version 18. All the config for this is in the .clang-format file.

## Formatting the whole project

Pre-built clang-format 18 binaries are provided for all platforms. To indent the entire project, run the appropriate script from the root of the repository:

**Linux/Mac:**
```bash
./format-code.sh
```

**Windows (PowerShell):**
```powershell
.\format-code.ps1
```

> ⚠️ **Before pushing**, always run the provided script above. IDE-integrated clang-format (VS Code, CLion, etc.) may produce different formatting results even at the same version and with the same `.clang-format` file, which can cause the GitHub format-check pipeline to fail.

## VS Code
Make sure you have C/C++ extension by Microsoft installed and it should automatically pick up your .clang-format file. You can use the IDE's auto-indent while developing, but **do not rely on it as a substitute for the provided script before committing**.

## CLion
CLion has built in clang-format, just press Ctrl + Shift + L (Windows and Linux) to auto-indent while developing with the `.clang-format` configure file within project directory. However, **do not rely on it as a substitute for the provided script before committing**.
Note: KDE default keymap is Alt + Shift + L

# Maintainer: Managing and Updating clang-format Binaries

The pre-built binaries are stored under `tools/clang-format-bin/<version>/` with one subdirectory per supported platform:
```
tools/clang-format-bin/
└── 18.1.8/
    ├── linux-x86_64/
    │   ├── clang-format
    │   └── lib/libtinfo.so.5
    ├── linux-arm64/
    │   ├── clang-format
    │   └── lib/libtinfo.so.5
    ├── macos-arm64/
    │   └── clang-format
    └── windows-x86_64/
        └── clang-format.exe
```

The root `format-code.sh` and `format-code.ps1` scripts delegate to `tools/clang-format.sh` and `tools/clang-format.ps1` respectively, which automatically select the correct binary for the current OS and architecture.

### Updating the clang-format version

1. Edit `tools/fetch-clang-format.sh` and update the version number.
2. Run the script, it will download the binaries and create the appropriate versioned directories under `tools/clang-format-bin/`. **Note that downloading from the LLVM project servers can take a while.**
3. Test each downloaded binary. Some platforms may require additional libraries (e.g. `libtinfo.so.5` for Linux). If so, provide the library in a `lib/` subdirectory alongside the binary. `tools/get_libtinfo_linux_x86_64_arm64.sh` has been left as a reference example, you can copy and adjust it for any future library needs.
4. Edit `tools/clang-format.sh` and `tools/clang-format.ps1` and set the version to the newly downloaded one.

> Multiple versions of the binaries can coexist under `tools/clang-format-bin/`. The active version is whichever is set in `tools/clang-format.sh` and `tools/clang-format.ps1`, making it easy to switch between versions as needed.