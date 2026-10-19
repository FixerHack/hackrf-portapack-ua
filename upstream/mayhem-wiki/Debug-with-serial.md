You can only print things to debug for this.
If you wanna set break point, checking registers etc, use another debug method.

ref. and code: https://github.com/portapack-mayhem/mayhem-firmware/pull/2111/files

# usage
1. Include the async msg header in your file
``` 

#include "usb_serial_asyncmsg.hpp"

``` 
if err happend after including it, maybe try not to include it but still using it (we are trying to settle the headers to prevent circuit including but it need sometime)

2 print things in your code and it will appear on serial.
``` 
void FileManBaseView::push_dir(const fs::path& path) {
    std::string test_string = "test string:";
    UsbSerialAsyncmsg::asyncmsg(test_string);
    std::string test_string111 = "abcdefghi";
    UsbSerialAsyncmsg::asyncmsg(test_string111);

    std::string test_path_label = "test_path:";
    UsbSerialAsyncmsg::asyncmsg(test_path_label);
    UsbSerialAsyncmsg::asyncmsg(path);

    std::string test_vec_label = "test_vector:";
    UsbSerialAsyncmsg::asyncmsg(test_vec_label);

    std::vector<uint32_t> test_vector;
    test_vector.push_back(1);
    test_vector.push_back(2);
    test_vector.push_back(3);
    UsbSerialAsyncmsg::asyncmsg(test_vector);

    std::string test_num_label = "test_num:";
    UsbSerialAsyncmsg::asyncmsg(test_num_label);

    uint8_t test = 254;
    UsbSerialAsyncmsg::asyncmsg(test);

    if (path == parent_dir_path) {
        pop_dir();
    } else {
        current_path /= path;
        saved_index_stack.push_back(menu_view.highlighted_index());
        menu_view.set_highlighted(0);
        reload_current(true);
    }
}
``` 

# why not printing anything?
* make sure async msg lock is disabled.
``` 
asyncmsg enable
``` 
* make sure serial connected
``` 
help
``` 
* MayhemHub currently not support real-time serial command communication. Use others.

# linking error
It’s possible that the object you are printing isn’t implemented yet (e.g. color obj). If you would like, feel free to implement it by editing usb_serial_asyncsg.cpp and hpp files.