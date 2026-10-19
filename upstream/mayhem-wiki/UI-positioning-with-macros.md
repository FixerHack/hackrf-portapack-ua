# Portapack UI Positioning Helper Macros

This document outlines the mandatory usage of the UI positioning helper macros for all new application development on the Portapack. These macros are designed to simplify and standardize the placement of UI elements by using a character-based grid system instead of raw pixel coordinates.

## Core Concept

The fundamental principle is to position elements based on character cells, where the default font is **8 pixels wide** by **16 pixels high**. All position parameters for these macros should be provided in terms of character or line counts, not pixels.

**Key Rule:** All positioning is **zero-indexed**. This means the first character or line is at index `0`, the second is at index `1`, and so on. For example, to place an element at the second character from the left and the second line from the top, you would use `UI_POS_X(1)` and `UI_POS_Y(1)`.

## Constants

These macros define the standard dimensions of character cells.

* `#define UI_POS_DEFAULT_HEIGHT 16`

  * The default height of a single line in pixels.

* `#define UI_POS_DEFAULT_HEIGHT_SMALL 8`

  * The height for a smaller font size in pixels.

* `#define UI_POS_DEFAULT_WIDTH 8`

  * The default width of a single character in pixels.

## Y-Axis Positioning (Vertical)

These macros calculate vertical pixel positions based on line numbers.

* `#define UI_POS_Y(linenum)`

  * **Description:** Calculates the top Y-pixel coordinate for a given line number.

  * **Example:** To start drawing on the 3rd line from the top:

    ```
    int y_position = UI_POS_Y(2); // Result: 32
    
    ```

* `#define UI_POS_Y_BOTTOM(linenum)`

  * **Description:** Calculates the top Y-pixel coordinate relative to the bottom of the screen. `linenum=0` refers to the last line, so it'll be out of screen. `linenum=1` will be the 1 char tall before the bottom, BUT the top status bar takes 1 line from the to, so it will be off screen too if the top status bar is visible.

  * **Important:** You must manually account for the top status bar if it is visible.

  * **Example:** To position an element on the last line of the screen:

    ```
    // Assuming screen_height is 240 and top bar is NOT visible
    int y_position = UI_POS_Y_BOTTOM(2); // Result: 208 (240 - 2*16) //but need to consider, that the 0 point in apps is the screen's 16th pixel, so it will display 1 line heigth object at the bottom.
    
    ```

## X-Axis Positioning (Horizontal)

These macros calculate horizontal pixel positions based on character numbers.

* `#define UI_POS_X(charnum)`

  * **Description:** Calculates the left X-pixel coordinate for a given character number.

  * **Example:** To start drawing at the 5th character from the left:

    ```
    int x_position = UI_POS_X(4); // Result: 32
    
    ```

* `#define UI_POS_X_RIGHT(charnum)`

  * **Description:** Calculates the left X-pixel coordinate relative to the right edge of the screen. `charnum=0` aligns the start of the element with the screen's right edge.

  * **Example:** To position an element 5 characters from the right edge:

    ```
    // Assuming screen_width is 320
    int x_position = UI_POS_X_RIGHT(5); // Result: 280 (320 - 5*8)
    
    ```

* `#define UI_POS_X_CENTER(charnum)`

  * **Description:** Calculates the starting X-pixel coordinate to center a string of `charnum` characters horizontally.

  * **Example:** To center the text "Hello" (5 characters):

    ```
    int x_position = UI_POS_X_CENTER(5);
    
    ```

* `#define UI_POS_X_TABLE(colnum, currcol)`

  * **Description:** Divides the screen into `colnum` equal columns and returns the starting X-pixel coordinate for the `currcol` (current column, zero-indexed).

  * **Example:** To get the starting position for the 2nd column in a 3-column layout:

    ```
    int x_position = UI_POS_X_TABLE(3, 1);
    
    ```

## Sizing and Dimensions

These macros calculate the width and height of elements in pixels.

### Width

* `#define UI_POS_WIDTH(charnum)`

  * **Description:** Calculates the pixel width for a given number of characters.

  * **Example:** The pixel width of a 10-character string:

    ```
    int width = UI_POS_WIDTH(10); // Result: 80
    
    ```

* `#define UI_POS_WIDTH_PERCENT(percent)`

  * **Description:** Calculates a pixel width that is a percentage of the total screen width.

  * **Example:** To get a width that is 50% of the screen:

    ```
    int width = UI_POS_WIDTH_PERCENT(50);
    
    ```

* `#define UI_POS_WIDTH_REMAINING(charnum)`

  * **Description:** Calculates the remaining pixel width from the `charnum`-th character position to the right edge of the screen.

  * **Example:** To draw a rectangle from character 4 to the end of the screen:

    ```
    int x_start = UI_POS_X(4);
    int rect_width = UI_POS_WIDTH_REMAINING(4);
    
    ```

* `#define UI_POS_MAXWIDTH`

  * **Description:** A constant representing the full pixel width of the screen (`screen_width`).

### Height

* `#define UI_POS_HEIGHT(linecount)`

  * **Description:** Calculates the pixel height for a given number of lines.

  * **Example:** The pixel height of a 4-line text box:

    ```
    int height = UI_POS_HEIGHT(4); // Result: 64
    
    ```

* `#define UI_POS_HEIGHT_PERCENT(percent)`

  * **Description:** Calculates a pixel height that is a percentage of the total screen height.

  * **Example:** To get a height that is 25% of the screen:

    ```
    int height = UI_POS_HEIGHT_PERCENT(25);
    
    ```

* `#define UI_POS_HEIGHT_REMAINING(linenum)`

  * **Description:** Calculates the remaining pixel height from the `linenum`-th line to the bottom of the screen.

  * **Important:** You must manually account for the top status bar if it is visible.

  * **Example:** To create a view that fills the screen below line 2:

    ```
    int y_start = UI_POS_Y(2);
    int view_height = UI_POS_HEIGHT_REMAINING(2);
    
    ```

* `#define UI_POS_MAXHEIGHT`

  * **Description:** A constant representing the full pixel height of the screen (`screen_height`).

## Practical Examples

Here are some examples demonstrating how to convert hard-coded pixel values to the more readable and screen-size-independent helper macros.

### Example 1: Basic Label Positioning

This shows a simple text label at the top-left corner of the screen.

**Before (Hard-coded pixels):**

```
Text label_channel{
    {0, 0, 16, 16}, // {x, y, width, height} in pixels
    "Ch"
};

```

**After (Using Macros):**
The same positioning is achieved, but the intent is much clearer. We are positioning an element that is 2 characters wide and 1 line high at the very first character/line position.

```
Text label_channel{
    {UI_POS_X(0), UI_POS_Y(0), UI_POS_WIDTH(2), UI_POS_HEIGHT(1)},
    "Ch"
};

```

### Example 2: Relative and Dynamic Sizing

These examples showcase more advanced macros for positioning relative to screen edges or using remaining space.

**RSSI Bar:**
This positions an RSSI indicator starting at the 22nd character, taking up most of the remaining width of the top line, with a fixed height of 4 pixels.

```
RSSI rssi{
    {UI_POS_X(21), UI_POS_Y(0), UI_POS_WIDTH_REMAINING(23), 4},
};

```

**Exit Button:**
This places a button on the 2th line up from the bottom, and 14 characters in from the right edge. The button itself is 14 characters wide and 2 lines high. This is ideal for standard footers.

```
Button button_exit{
    {UI_POS_X_RIGHT(14), UI_POS_Y_BOTTOM(3), UI_POS_WIDTH(14), UI_POS_HEIGHT(2)},
    "Exit"
};
