> **Note (firmware ≥ Oct 2025):** the single `external.ld` file was split into `external_tier0.ld`, `external_tier1.ld` and `external_tier2.ld` (one per device flash-size tier) and these are now generated automatically from each app's `tier.txt` marker by `tools/update_external_tier_ld.py`. Where this page says `external.ld`, read it as `external_tier0.ld` (the tier-0 file still lists every app). Don't edit these files by hand: change the app's `tier.txt` and rebuild. See [Create a Simple External App](Create-a-simple-external-app) for the tier values.

External apps are similar to internal apps in that they are compiled and linked with the rest of the firmware, but at the link stage a fake memory address range is specified for each external app in the "external.ld" file.  After linking, the external apps are removed from the firmware image and extracted to separate files.  This is quite different from baseband modules that are each compiled and linked separately, run on a different CPU (the M4), and communicate with the main firmware via a message protocol.  Note that LTO optimization cannot be used when linking the external apps, to prevent the linker from attempting to share code between external apps.

## export_external_apps.py
The export_external_app python script edits each external app image to (1) replace the fake memory addresses used during the linker stage with actual RAM addresses where the external app will be loaded to be executed, (2) append any needed baseband image, and (3) adds a file checksum to verify integrity during the untar process.

### External App Address Replacement
As example, if the fake address range of an app is 0xADC00000 to 0xADC07FFF, this python script will search the external app file for values in this range and replace them; it _assumes_ that they are pointers to memory addresses within this app.  If the app image contains a value where the high byte is 0xAD but the next most significant byte is potentially an address within a different app, a warning message is displayed such as the following.  This message implies that code within the indicated app may be attempting to use code within another app (but since the LTO optimization is disabled, it is most likely that this warning message is a false positive and the value found could just be a code instruction or raw data):

`    WARNING: External code address 0xadb01234 at offset 0x1000 in tetris.himg`

Note that the fake 0xADxxxxxx address range was selected for external apps based on few data values in this range in the firmware image, and because any firmware attempts to access this fake memory address range will trigger a GURU meditation fault.

### External App Baseband Images
Baseband modules for external apps are created exactly the same as baseband images for internal apps, are compressed, and execute from RAM on the M4 processor as all baseband modules do.  But, external app baseband images are omitted from the firmware ROM and are instead appended to the external app image using the python script mentioned above.

### External App Checksum
The checksum used for external app image files is simply a uint32 sum of all 32-bit values in the image file, with the sign finally inverted such that the total (including checksum) will sum to 0 if it's a valid image.  This simple checksum method is used for speed (CRC32 would be slower).

## make_spi_image.py
The make_spi_image python script creates the firmware ROM image by appending the baseband images and a simple checksum, and also checks to make sure there are no references to the "fake" memory address regions used for external apps mentioned above.  The checksum algorithm is the same as used for external apps, above.  A warning message similar to the one below may be displayed if data values are found in the firmware image that _might_ be an attempt to access a "fake" memory address region:

`    WARNING: Possible external code address 0xadb96ef0 at offset 0xb24a4 in portapack-h1_h2-mayhem.bin`

To determine if a warning message such as that above is real or a false positive, search for the mentioned external code address within the memory regions indicated in the external.ld file.  In this example, you might find a line in external.ld like this, which implies that firmware might possibly be trying to access memory in the LCR app:

`    ram_external_app_lcr(rwx) : org = 0xADB90000, len = 32k`

To determine if it's real or a false positive, edit this line of the external.ld file to change the LCR app's address to another range that is unused such as "org = 0xADFF0000" and rebuild firmware.  IF the address in the warning message changes to the new address range, then firmware really is trying to access code or data within that external app.  If the address in the warning message stays the same, then it's a false positive and can safely be ignored.  (Future updates to the python script will hopefully eliminate the bogus warnings.)