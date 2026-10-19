
# Splash screen
For converting back and forth between the image and source you can use `xxd`. In a Windows environment you can use this command in the Linux Subsystem installing one of the versions available (i.e. [Ubuntu](https://ubuntu.com/tutorials/tutorial-ubuntu-on-windows#1-overview)). 

### From .bmp to .hpp
`xxd -i input_image.bmp output.hpp`

### From .hpp to .bmp
`xxd -r -p input.hpp output_image.bmp `

## Python converter for Splash Screen

There is also a python helper in [firmware/tools/bmp_tools](https://github.com/portapack-mayhem/mayhem-firmware/tree/next/firmware/tools/bmp_tools/) 

# Firmware icons

The special file `firmware/application/bitmap.hpp` contains all firmware icons.  
This file should not be edited directly! Instead, new icons should be copied in [firmware/graphics](https://github.com/portapack-mayhem/mayhem-firmware/tree/next/firmware/graphics) and then run `python [firmware/tools/bitmap_tools/pp_png2hpp.py](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/tools/bitmap_tools/pp_png2hpp.py) <DIRECTORY> bitmap.hpp` to create `bitmap.hpp`.

For operating that Python3 script, `Pillow` library is required: `pip install pillow`

## make_bitmap.py - Convert a folder contains one or more icon.png to one bitmap.hpp
The `make_bitmap.py` is the traditional helper, well tested. The folder with the icons is given as argument and generates the `bitmap.hpp`. This file needs to be copied to `mayhem-firmware/firmware/application/`. Starting from the `tools/ folder, the command is:  
```
python3 bitmap_tools/make_bitmap.py ../graphics/ && mv bitmap.hpp ../application/bitmap.hpp
```

The icon size needs to be a multiple of 8. The generated icon is black/white.  

## bitmap_arr_reverse_decode.py - Convert bitmap array to icon.png
The `bitmap_arr_reverse_decode.py` takes an array from the bitmap.hpp and convert it back to a png.  


## pp_png2hpp.py - Convert both ways
The `pp_png2hpp.py` is based on the previous scripts, as all in one solution.  

With the `--hpp bitmap.hpp` file and the `--graphics /folder_to/png_icons/` arguments, this script will generate a `bitmap.hpp`.  
Add the `--reverse` argument to generate png icons from a given `bitmap.hpp`.  

The reverse function got a parser, for automatic get the filename and size of the image.

#### Example
From the `tools/` folder:
```
$ ./bitmap_tools/pp_png2hpp.py ../application/bitmap.hpp ../graphics
Converting from png to hpp
From path ../graphics/ to file ../application/bitmap.hpp
Find your bitmap.hpp at ../application/bitmap.hpp
```

To reverse the icons from the .hpp to png icons use the parameter `--reverse`. Default is only the mayhem logo, named `titlebar_image`:
```
$ ./bitmap_tools/pp_png2hpp.py ../application/bitmap.hpp /home/lupus/work/hackrf/tmp/ --reverse 
Reverse: Converting from hpp to png
Converting icon titlebar_image
```

Add the parameter `--icon <icon name>` to convert another icon or `all` to convert all available icons at once:  
```
$ ./bitmap_tools/pp_png2hpp.py ../application/bitmap.hpp /home/lupus/work/hackrf/tmp/ --reverse --icon all
```

**Note**: It is not a recovery, the icons will be new generated. The new icons are black/white, even if the original icons where transparent.  

## Online editor

The current icons were designed on [Piskelapp](https://www.piskelapp.com/). To create or update icons, the current sources ([16x16](https://www.piskelapp.com/p/agxzfnBpc2tlbC1hcHByEwsSBlBpc2tlbBiAgKC9vPncCww/view) or [8x8](https://www.piskelapp.com/p/agxzfnBpc2tlbC1hcHByEwsSBlBpc2tlbBiAgKC9vPncCww/view)) can be used.
