Thank you for considering a contribution! As an embedded project with limited resources, we balance new features against flash/RAM usage and CPU overhead.

## Quick Decision Framework

*   **Bug Fixes** → **Highly Welcome**
    *   Security fixes, crash fixes, or correctness improvements
    *   Should include minimal reproduction steps or regression tests

*   **External/Standalone Apps** → **Very Welcome**
    *   Code that runs without consuming internal flash space
    *   Must not modify core system APIs (add only, don't break)

*   **Core System Modifications** → **Discussion Required First**
    *   Architecture changes (Radio related, compile routine, filesystem architecture, etc...)
    *   Navigation & UI (menu systems, navigation system, UI design concept...)
    *   Core system functionality (serial port, file management, text editor, frequency management, setting & debugging options, persistent memory usage, etc... )
    
    **Required:** Open an **Issue** or ask on **Discord** before writing code. We may reject modifications that consume significant RAM/flash for edge-case use cases. Early feedback prevents wasted effort.

# Once your pull request has been merged

Add a wiki article: 
- Create or new page or update existing page in the project wiki documenting your change (improvement, new app).
- If needed, update the sidebar menu to include a link to your new article in the appropriate section.

This helps keep our documentation up to date and makes it easier for other contributors to understand the project.

## AI-Assisted Coding Policy

*   **Welcomed** with conditions:
    *   You must verify the code works on **actual hardware** (not just compiles or even not compiling)
    *   You must be willing to iterate based on review feedback

## General Requirements

*   Match existing code style (run `clang-format`)
*   Include `static` for internal linkage; minimize global symbols

By contributing, you agree to [the license](https://github.com/portapack-mayhem/mayhem-firmware?tab=GPL-3.0-1-ov-file#readme).