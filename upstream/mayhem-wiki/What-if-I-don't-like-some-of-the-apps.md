Mayhem firmware comes with a large collection of apps. There are three ways to manage apps you don't want to see.

## Option 1: Hide apps with the App Manager (recommended)

Go to **Settings → App Manager** to hide individual apps from the menu. Hidden apps remain on the SD card and can be re-enabled at any time. This is the easiest and fully reversible method.

Alternatively, you can directly edit the blacklist config file — see [[Settings#blacklist]].

> [!NOTE]
> Hidden apps take up no RAM or CPU while not in use. External apps stored on the SD card each occupy less than 10 KB of storage, so there is no meaningful space benefit to deleting them. Games and other non-radio apps have no impact on core radio functionality — if you don't want to see them, simply hide or delete them.

## Option 2: Delete the app file from the SD card

If you want to remove an app entirely, delete its file from the `APPS/` folder on the SD card. External apps use two file extensions:

- `.ppma` — standard external apps (must match the current firmware version)
- `.ppmp` — standalone external apps (version-independent)

You can access the SD card by physically removing it, or via the [[SD-Over-USB|SD Over USB]] app.

> [!WARNING]
> Deleted app files are not restored by firmware updates. To get a deleted app back, you will need to copy it from a fresh release package.

## Note on built-in apps

Some apps — particularly the built-in ones compiled directly into the firmware — cannot be removed without recompiling the firmware. However, all of them can be hidden via the App Manager.