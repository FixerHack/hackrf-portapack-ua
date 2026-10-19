## About Widgets

Widgets are elements to compose the UI of your custom app. Widgets are defined in [`firmware\common\ui_widget.hpp`](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/common/ui_widget.hpp) and widget functions can be found in [`firmware\common\ui_widget.cpp`](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/common/ui_widget.cpp). To use them, you must add the line `#include "ui_widget.hpp"` into your app .hpp file.  
There are different types of widgets. Here you will find a list of available widgets, with their constructor. For all methods available, you should check the [ui_widget.hpp](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/common/ui_widget.hpp) file.  


## Attach a generic Widget to your Application

To display a widget in your app, you can use the functions `add_child()` for a single widget or `add_children()` to add an undefined number of widgets.  
Both functions shall be called within the code of the `NewAppGameView(NavigationView &nav){}` constructor.  
Widgets must be passed as pointers to the functions.  

**Declaration and prototype**  
```
add_child(&my_widget);
```
or  
```
add_children({
    &widget_1,
    &widget_2
});
```

## Available widgets

There are several widgets available and more might be added. You should always check [ui_widget.hpp](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/common/ui_widget.hpp) if new widgets have been added.  
In this document you will find a list of most basic widgets.  


***
### Text

The text widget add a simple text area widget in the app.  

**Declaration and prototype**  
```
Text my_text_widget{
    Rect parent_rect,
    std::string text
};

```
**Note:** `Rect parent_rect` has it's own definition inside another file.  

**Example**  
Add a text widget with the content "Hello World" positioned at 10x10 px from the top left corner with width 100 and height 24.  
```
Text hello_world_text_widget(
  {10, 10, 100, 24},          // Coordinates are: int:x (px), int:y (px), int:width (px), int:height (px)
  "Hello world!"
);
```

***
### Button

Buttons allows to do something when you press it.  

**Declaration and prototype**  
```
Button my_button_widget{
    Rect parent_rect,
    std::string text
};
```
**Note:** Every time you create a button, you have to implement the method `my_button_widget.on_select = [&nav](Button &){}`. It could be empty (even though it shouldn't, as here you define the action for a button), but it must be present in the code.  

**Example**  
A button called `my_button`, with the same dimensions as the previous widget.  
```
Button my_button(
   {10, 10, 100, 24}, // Coordinates are: int:x (px), int:y (px), int:width (px), int:height (px)
   "my_button_text"
);
```

***
### Labels

Labels are a text element that can be used to describe other widgets.  

**Declaration and prototype**  
```
Labels my_label_widget{
    std::initializer_list<Label> labels
};
```

**Example**  
A label called `my_label`. Because the constructor is looking for a list you'll need to add brackets `{}` around each label.  
Add this to `apps/ui_newapp.hpp`:
```
Labels my_label{
    {{10, 10},            // Coordinates are: int:x (px), int:y (px)
    "my_label_text:",     // Label text
    Color::light_grey()}, // Label color
};
```
**Note:** Colors are defined in [`firmware/common/ui.hpp`](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/common/ui.hpp).  

In `apps/ui_newapp.cpp` add the `my_label` pointer to `add_child()` or `add_children()`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_label,
    });

}
```

***
### LiveDateTime

LiveDateTime gives the dynamic date and time.  

**Declaration and prototype**  
```
LiveDateTime my_liveDateTime_widget{
    Rect parent_rect
};
```

**Example**  
For a label called `my_liveDateTime` add the folowing code to `apps/ui_newapp.hpp`:  
```
LiveDateTime my_liveDateTime {
    { 2, 10, 19*8, 16 },       // Coordinates are: int:x (px), int:y (px), int:width (px), int:height (px)
};
```

In `apps/ui_newapp.cpp` add the `my_liveDateTime` pointer to `add_child()` or `add_children()`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_liveDateTime,
    });

}
```

To enable seconds use the function `set_seconds_enabled(bool new_value)`:  
```
my_liveDateTime.set_seconds_enabled(true);
```

***
### BigFrequency

BigFrequency is used for displaying a radio frequency.  

**Declaration and prototype**  
```
BigFrequency my_bigFrequency_widget{
    Rect parent_rect, 
    rf::Frequency frequency
};
```

**Example**  
For a big frequency widget called `my_bigFrequency` add the following code to `apps/ui_newapp.hpp`:  
```
BigFrequency my_bigFrequency(
    {10, 10, 28*8, 52}, // Coordinates are: int:x (px), int:y (px), int:width (px), int:height (px)
    0                   // Beginning frequency in hz
);
```

In `apps/ui_newapp.cpp` add the `my_bigFrequency` pointer to `add_child()` or `add_children()`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_bigFrequency,
    });

}
```

To set a frequency use the function `set(const rf::Frequency frequency)`:  
```
my_bigFrequency.set(433000000); // 433MHz
```

***
### ProgressBar

Progress bars are a visual representation of the progress of a task.  

**Declaration and prototype**  
```
Labels my_progressBar_widget{
    Rect parent_recthttps://github.com/portapack-mayhem/mayhem-firmware.wiki.git
};
```

**Example**  
For a label called `my_progressBar` add the following code to `apps/ui_newapp.hpp`:  
```
ProgressBar my_progressBar {
    { 2, 10, 208, 16 },      // Coordinates are: int:x (px), int:y (px), int:width (px), int:height (px)
};
```

In `apps/ui_newapp.cpp` add the `my_progressBar` pointer to `add_child()` or `add_children()`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_progressBar,
    });

}
```

Set the maximum value for the progress bar with the function `set_max(const uint32_t max)`:  
```
my_progressBar.set_max(10); // 10 is 100%
```

Change the value of progress for the progress bar with the function `set_value(const uint32_t value)`:  
```
my_progressBar.set_value(5); // 50% Complete
```

***
### Console

Console can be used as large text field where you can output mutable lines of text.  

**Declaration and prototype**  
```
Console my_console_widget{
    Rect parent_rect
};
```

**Example**  
For a label called `my_console` add the following code to `apps/ui_newapp.hpp`:  
```
Console my_console {
    { 2*8, 10, 208, 200 },    // Coordinates are: int:x (px), int:y (px), int:width (px), int:height (px)
};
```

In `apps/ui_newapp.cpp` add the `my_console` pointer to `add_child()` or `add_children()`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_console,
    });

}
```

To write to 'my_console' use the function `write(std::string message)`:  
```
my_console.write("Hello World");
```

For automatic new line use the function `writeln(std::string message)`. It will add `\n` at the end of every string:  
```
my_console.writeln("Hello World but on a new line!");
```

To enable scrolling use the function `enable_scrolling(bool enable)`:  
```
my_console.enable_scrolling(true);
```

**Note:** The buffer size is limited to 256 char

***
### Checkbox

Checkbox is a boolean (true/false) widget, that allows you to chose between two options. The Checkbox is displayed as a rectangle with a green check mark (true) or a red cross (false).  

**Declaration and prototype**  
```
Checkbox my_checkbox_widget{
    Point parent_pos,
    size_t length,
    std::string text,
    bool small
};
```

**Example**  
For a checkbox called `my_checkbox` add the following code to `apps/ui_newapp.hpp`:  
```
Checkbox my_checkbox(
    {10, 20},           // Coordinates are: int:x (px), int:y (px)
    4,                  // Length
    "my_checkbox_text", // Title
    false               // Checkbox Size: true == small(16X16px), false == regular(24X24px) 
);
```

In `apps/ui_newapp.cpp` add the `my_checkbox` pointer to `add_child()` or `add_children()`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_checkbox,
    });

}
```

Functions within `apps/ui_newapp.cpp` can lookup the value of `my_checkbox` with Checkbox's `value()` function:  
```
if(my_checkbox.value()) {
    do_a();                // If checkbox is selected (green check mark)
} else {
    do_b();                // If checkbox is NOT selected (red X)
}
```

Set the value for `my_checkbox` with the function `set_value(const bool value)`:  
```
my_checkbox.set_value(true);  // Checkbox selected (green check mark)
my_checkbox.set_value(false); // Checkbox deselected (red X)
```

To automatically perform an action when the checkbox is toggled, add [Lambda](https://www.geeksforgeeks.org/lambda-expression-in-c/) to `apps/ui_newapp.cpp`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Add widget pointers
    add_children({
        &my_checkbox,
    });

    // When checkbox is toggled do...
    my_checkbox.on_select = [this](Checkbox&, bool v) {
        if(v){
            do_a();                                      // If checkbox is selected (green check mark) 
        } else {
            do_b();                                      // If checkbox is NOT selected (red X)  
        }
    };

}
```

***
### Image

Images can be displayed within your app.  

**Declaration and prototype**  
```
Image my_Image_widget{
    Rect parent_rect,
    Bitmap* bitmap,
    Color foreground,
    Color background
};
```

Images need to be a Bitmap object before they can be displayed. Below is an example of the code needed to create a Bitmap from [`firmware/application/bitmap.hpp`](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/application/bitmap.hpp).
```
static constexpr uint8_t bitmap_stripes_data[] = {
	0xFF, 0x03, 0xC0, 
	0xFF, 0x01, 0xE0, 
	0xFF, 0x00, 0xF0, 
	0x7F, 0x00, 0xF8, 
	0x3F, 0x00, 0xFC, 
	0x1F, 0x00, 0xFE, 
	0x0F, 0x00, 0xFF, 
	0x07, 0x80, 0xFF, 
};
static constexpr Bitmap bitmap_stripes {
	{ 24, 8 }, bitmap_stripes_data
};
```

**Example**  
With the Bitmap object created we can define the image `my_image`. Add the following code to `apps/ui_newapp.hpp`:  
```
Image my_image(
    {10, 10, 24, 8},    // Coordinates are: int:x (px), int:y (px), int:width (px), int:height (px)
    &Bitmap,            // Pointer to your bitmap
    Color::white(),     // Color Foreground
    Color::black()      // Color Background
);
```
**Note:** Colors are defined in [`firmware/common/ui.hpp`](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/common/ui.hpp)


In `apps/ui_newapp.cpp` add the `my_image` pointer to `add_child()` or `add_children()`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_image,
    });

}
```

***
### OptionsField

OptionsField is a widget to create a field, in which you can change its value with the wheel on your PortaPack.

**Declaration and prototype**  
```
 OptionsField my_OptionsField_widget{
   Point parent_pos, 
   int length, 
   options_t options,
   bool centered,
};
```
`parent_pos` is an array of two integer, represents where the top left corner of the widget should be positioned. The length is an integer which tells how many options you have into your options parameter. The options_t field is an array of options in which your portapack can choose to display.  

Centered is a bool that if you true it, you can make all the text in it in the center. It’s originally init-ed, so if you don’t define it, it will be default false.

**Example**  
An OptionsField called `my_optionsField`, with 3 options positioned at 10 from top and 10 from left:  
```
OptionsField my_optionsField{
    {10,10},                   // Coordinates are: int:x (px), int:y (px)
    7,                         // Char length for option title
    {
      {"option1",0},  
      {"option2",1},           // Options {"KEY", int VALUE}
      {"option3",2}
    }
};
```
**Note:** The number following the `option_n` string value, should be the value that could be retrieved from the OptionsField with the function `my_optionsField.selected_index_value();`

***
### NumberField

NumberField is similar to the OptionsField widget except that it only deals with numbers. You can change its value with the wheel on your portapack.  

**Declaration and prototype**  
```
NumberField my_NumberField_widget{
    Point parent_pos, 
    int length, 
    range_t range, 
    int32_t step, 
    char fill_char, 
    bool can_loop
};
```

**Example**  
For a NumberField called `my_numberField` add the following code to `apps/ui_newapp.hpp`:  
```
// Example 3 digit number starting at "000", ends at "255"
NumberField my_numberField(
    {10, 10},          // Coordinates are: int:x (px), int:y (px)
    3,                 // Length
    {0, 255},          // MIN -> MAX Range
    1,                 // Step
    '0',               // Fill Char
    false              // Can Loop
);
```

In `apps/ui_newapp.cpp` add the `my_numberField` pointer to `add_child()` or `add_children()`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_numberField,
    });

}
```

Functions within `apps/ui_newapp.cpp` are able to lookup the value of `my_numberField` with NumberField's `value()` function:  
```
int number = my_numberField.value();
```

Set the value for `my_numberField` with the function `set_value(int32_t new_value, bool trigger_change)`:  
```
my_numberField.set_value(123);
```

If you want your NumberField to change a value (int number for example) you'll need to add [Lambda](https://www.geeksforgeeks.org/lambda-expression-in-c/) to `apps/ui_newapp.cpp`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Add widget pointers
    add_children({
        &my_numberField,
    });

    // When NumberField is changed
    my_numberField.on_change = [this](int32_t v) {
        number = v;
    };

}
```

***
### Waveform

Waveforms are used to display a sign wave from a signal source.  
**Note:** The X axis represents time while the Y axis represents amplitude.  

**Declaration and prototype**  
```
Labels my_waveform_widget{
    Rect parent_rect,
    int16_t * data,
    uint32_t length,
    int32_t offset,
    bool digital,
    Color color
};
```

**Example**  
For a waveform widget called `my_waveform` add the following code to `apps/ui_newapp.hpp`:  
```
Waveform my_waveform(
    {0, 5*16, 240, 64},  // Coordinates are: int:x (px), int:y (px), int:width (px), int:height (px)
    waveform_buffer,     // RX data
    128,                 // Length, how many elements in the waveform_buffer array
    0,                   // Offset
    false,               // Digital
    Color::white()       // Sine wave color
);
```
**Note:** Colors are defined in [`firmware/common/ui.hpp`](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/common/ui.hpp).

The data being displayed by `my_waveform` needs to be a `int16_t` array. Declare this variable in `apps/ui_newapp.hpp`:  
```
class NewAppView : public View
{
    public:

        ...

    private:
        int16_t waveform_buffer[128];  // Data for Waveform

        ...

};
```

In `apps/ui_newapp.cpp` add the `my_waveform` pointer to `add_child()` or `add_children()`:  
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_waveform,
    });

}
```

If the input data has a variable length, use the function `set_length(const uint32_t new_length)` to update the waveform:
```
my_waveform.set_length(9001) // THAT'S OVER 18KB!!
```

***
### VuMeter

VuMeter is used to visually represent the sound intensity of an audio source.  

**Declaration and prototype**  
```
Labels my_vuMeter_widget{
    Rect parent_rect,
    uint32_t LEDs,
    bool show_max
};
```

**Example**  
For a VuMeter called `my_vuMeter` add the following code to `apps/ui_newapp.hpp`:  
```
VuMeter my_vuMeter(
    { 0*8, 1*8, 2*8, 33*8}, // Coordinates are: int:x (px), int:y (px), int:width (px), int:height (px)
    12,                     // LEDs
    true                    // Show max
);
```

In `apps/ui_newapp.cpp` add the `my_vuMeter` pointer to `add_child()` or `add_children()`:
```
NewAppView::NewAppView(NavigationView &nav) {

    // Widget pointers
    add_children({
        &my_vuMeter,
    });

}
```

Set the value for `my_vuMeter` with the function `set_value(const uint32_t new_value)`:  
```
my_vuMeter.set_value(123); // Max is 255
```
