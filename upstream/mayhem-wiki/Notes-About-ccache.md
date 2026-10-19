# background
ccache is a nice tool, but we certainly realized some issue of its behavior in this project, that could waste your time instead of save your time. So it's **default off** now, unless you manually enable it. 

# issue that could appear if you enable it
Just keep in mind that these issues could be made:
- When you compiled with ccache enabled, and use git to merge/pull new changes, it can only detect a part of your change, and would compile fail. It cannot be fixed by `make clean`, you hvae to delete the build dir and start over.
- Sometimes ccache cause linking stage took extremely long.
- Unknown linking error until you `make clean` and start over again.

# I want enable it anyway
If you are aware of these issue and you are sure you are able to realized them, when they appear, follow this to enable ccache:

## for make: 
### turn on
```
#(...other steps that in compile guide...)
mkdir build
cd build
cmake -DUSE_CCACHE=ON ..   
make -j
#(...other steps that in compile guide...)
```
### turn off
```
#(...other steps that in compile guide...)
mkdir build
cd build
cmake -DUSE_CCACHE=OFF ..   
make -j
#(...other steps that in compile guide...)
```
### default behavior (off) (if you turned it on, this will became on until you turn it off again)
```
#(...other steps that in compile guide...)
mkdir build
cd build
cmake ..   
make -j
#(...other steps that in compile guide...)
```

## for ninja:
### turn on
```
#(...other steps that in compile guide...)
mkdir build
cd build
cmake -G Ninja -DUSE_CCACHE=ON .. 
ninja
#(...other steps that in compile guide...)
```
### turn off
```
#(...other steps that in compile guide...)
mkdir build
cd build
cmake -G Ninja -DUSE_CCACHE=OFF .. 
ninja
#(...other steps that in compile guide...)
```
### default behavior (off) (if you turned it on, this will became on until you turn it off again)
```
#(...other steps that in compile guide...)
mkdir build
cd build
cmake -G Ninja .. 
ninja
#(...other steps that in compile guide...)
```