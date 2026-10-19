## About

This guide shows how to create an **external app**: a standalone app that is compiled alongside the firmware but shipped as a separate `.ppma` file on the SD card, instead of being baked into the firmware image. This is the recommended way to add your own app to Mayhem.

If you are completely new to the Mayhem code base, start with [Create a Simple App](Create-a-Simple-App) first. That page is a plain "hello world" that introduces views, widgets, labels and buttons: the UI basics this guide assumes you already know.

## First steps

You will create a new app folder under `firmware/application/external/`, add the required source files, register the app in the build, and compile. Follow the steps below in order.

# Workflow

- create a new subdir with your app name in firmware/applications/external, like firmware/applications/new_external_app
- create your empty hpp and cpp basic structure. It must contain a main.cpp and at least two other files, example:

**main.cpp:**
````
/*
 * Copyright (C) 2023 Bernd Herzog
 *
 * This file is part of PortaPack.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#include "ui.hpp"
#include "ui_new_external_app.hpp"
#include "ui_navigation.hpp"
#include "external_app.hpp"

namespace ui::external_app::ui_new_external_app {
void initialize_app(ui::NavigationView& nav) {
    nav.push<NewExternalAppView>();
}
}  // namespace ui::external_app::ui_new_external_app

extern "C" {

__attribute__((section(".external_app.app_ui_new_external_app.application_information"), used)) application_information_t _application_information_ui_new_external_app = {
    /*.memory_location = */ (uint8_t*)0x00000000,
    /*.externalAppEntry = */ ui::external_app::ui_new_external_app::initialize_app,
    /*.header_version = */ CURRENT_HEADER_VERSION,
    /*.app_version = */ VERSION_MD5,
    /*.app_name = */ "NewExternalApp",
    /*.bitmap_data = */ {
        0x54,
        0x15,
        0x54,
        0x15,
        0xFF,
        0x7F,
        0xFC,
        0x1F,
        0xFF,
        0x7F,
        0xCC,
        0x19,
        0xAF,
        0x7A,
        0x6C,
        0x1B,
        0xEF,
        0x7B,
        0xEC,
        0x1B,
        0xFF,
        0x7F,
        0xFC,
        0x1F,
        0xFF,
        0x7F,
        0x54,
        0x15,
        0x54,
        0x15,
        0x00,
        0x00,
    },
    /*.icon_color = */ ui::Color::cyan().v,
    /*.menu_location = */ app_location_t::DEBUG,
    /*.desired_menu_position = */ -1,
    /*.m4_app_tag = portapack::spi_flash::image_tag_none */ {0, 0, 0, 0},
    /*.m4_app_offset = */ 0x00000000,  // will be filled at compile time
};
}
````

**new_external_app.hpp:**
````
/*
 * Copyright (C) 2015 Jared Boone, ShareBrained Technology, Inc.
 * Copyright (C) 2018 Furrtek
 *
 * This file is part of PortaPack.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef __UI_NEW_EXTERNAL_APP_H__
#define __UI_NEW_EXTERNAL_APP_H__

namespace ui::external_app::new_external_app {

class NewExternalAppView : public View {
   public:
    NewExternalAppView(NavigationView& nav);

    void focus() override;

    std::string title() const override { return "NEwExternalApp"; };

   private:
    NavigationView& nav_;

    Text text_widget{
        {0 * 8, 19 * 8, 30 * 8, 16},
        ""};

    Button button_exit{
        {22 * 8, 34 * 8, 8 * 8, 32},
        "Exit"};
};

}  // namespace ui::external_app::new_external_app

#endif /*__UI_NEW_EXTERNAL_APP_H__*/
````

**new_external_app.cpp:**
````
/*
 * Copyright (C) 2015 Jared Boone, ShareBrained Technology, Inc.
 * Copyright (C) 2018 Furrtek
 *
 * This file is part of PortaPack.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#include "ui_new_external_app.hpp"

namespace ui::external_app::new_external_app {

NewExternalAppView::NewExternalAppView(NavigationView& nav)
    : nav_{nav} {
    add_children({&dump_output,
                  &button_exit});

    button_exit.on_select = [this](Button&) {
        nav_.pop();
    };
}

void NewExternalAppView::focus() {
    button_exit.focus();
}

}  // namespace ui::external_app::new_external_app
````
- replace app_location_t in main.cpp by the place you want your app (RX, TX, DEBUG, UTILITIES, HOME)
- don't forget adjust header guard, class name, external namespace according to your new app name
- don't forget to adjust the /*.m4_app_tag = portapack::spi_flash::image_tag_none */ {0, 0, 0, 0}, line in main.cpp to use the needed baseband if ever. You can find the list in firmware/common/spi_image.hpp. **If your app is using multiple basebands, you have to put here the biggest possibe one (usually NFM)**
- change bitmap icon, copy the one you want from firmware/applications/bitmap.hpp 
- if you used the example files, replace all occurrences of new_external_app by your new app name and NewExternalAppView by your new class name
- (You no longer edit the linker script by hand.) The three linker scripts `external_tier0.ld`, `external_tier1.ld` and `external_tier2.ld` are generated automatically from the apps' `tier.txt` markers by `tools/update_external_tier_ld.py`, which CMake runs on every build. Just build once and commit the regenerated `.ld` files.
- Optionally add a `tier.txt` file in your app folder containing a single number that controls when your app is built INTO the firmware instead of as an external `.ppma`:
  - `0` (or no `tier.txt`) – never internal, external in every build (the normal case)
  - `1` – built in on 2 MB devices (PortaRF) and larger (HackRF Pro)
  - `2` – built in only on >2 MB devices (HackRF Pro)
  - `-1` – disabled, left out of every build
  - If you give your app tier `1` or `2`, you must also `#include` its header in `firmware/application/ui_navigation.cpp` inside a `#if FLASH_TIER >= N` block (the build will refuse otherwise). A plain external app needs none of this.
- in external.cmake, add a block to EXTCPPSRC with your source, example:

````
# new_external_app
external/new_external_app/main.cpp
external/new_external_app/new_external_app.cpp
````
- in external.cmake, add a line with your app name in the EXTAPPLIST block, example:

````new_external_app```
- done, you can now build the firmware and your new external app will be built along with it
- flash the ppfw via the hackrf.app website or copy it to the sdcard and use the on device flasher

# Online example

User aquilestraigo who contributed the OOK Editor app also made a nice page on his adventure creating an external app.

You can check it here: https://blog.hawktesters.com/rookremote-on-off-keying-for-to-portapack-hackrf/

It's pretty explanatory, and you will maybe find there some explanations you missed here.
````
