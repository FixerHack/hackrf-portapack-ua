There is a Theme system in PP, so each app can use the same color scheme, that can be changed by the user.

## Using theme system

It is important to use this system to give users consistent UI. Have to mention there are use cases when you must use specific colors, like in a waterfall, then do it.

To use the theme system, just include **theme.hpp**, and instead of using Color::grey() or similar colors, use the corresponding theme object.
For example the labels usually used LightGrey color. Now you can use the template's light foreground color. 
``` Theme::getInstance()->fg_light ```


The theme system uses (mostly) styles, that starts with fg_ or bg_ . 
These can be light, medium, dark, darker, darkest.
FG stands for foreground, BG stands for background. This is to specify if the foreground is important to you, or the background. So if it is important, that the foreground of a button be light, then use the fg_light. then the foreground will be light colored (like light grey) but the background for it will be something that has good readability.

There are specific colors to indicate "error", "warning", or "ok". These are: error_dark; warning_dark; ok_dark;
There are also specific color styles, like fg_red, fg_green, fg_yellow, fg_orange, ....
Use these, because theme can override the color of the red, so within a "red theme" (where the backgrounds are red too) the 255,0,0 color could be different for better contrast. But if you use Color::red() it may not be as readable as the theme's fg_red.

Also if you use theme specific colors, like fg_red->foreground, you should use it's background counterpart. (in the example it would be fg_red->background).


The app's background is usually bg_darkest->background.


You don't need to use the styles as a style object! For labels you can specify the foreground color only. 
``` Theme::getInstance()->fg_light->foreground ```  or for the app or widget's background you can use ``` Theme::getInstance()->bg_darkest->background ```


## Creating a new theme
Step 1: open theme.hpp and add a new class derived from ThemeTemplate:
``` 
class ThemeMyNewTheme : public ThemeTemplate {
   public:
    ThemeMyNewTheme ();
};
```

Step 2: add it to the enum (ThemeId) within the Theme class, BEFORE MAX.
``` 
enum ThemeId {
        DefaultGrey = 0,
        Yellow = 1,
        Aqua = 2,
        Green = 3,
        Red = 4,
        MyNewTheme = 5,
        MAX
    };
```
Step 3: In the theme.cpp create a case block for your new enum and class in the Theme::SetTheme() function.
```
void Theme::SetTheme(ThemeId theme) {
    if (current != nullptr) delete current;
    switch (theme) {
        case MyNewTheme :
            current = new ThemeMyNewTheme ();
            break;
        ....
        case DefaultGrey:
        default:
            current = new ThemeDefault();
            break;
    }
}
```
Step 4: Implement your class's constructor, and create each element! If you forget one, then your theme will crash the PP!
Best practice is to copy an exists one and modify the color defined in it.


Step 5: Always check your theme everywhere. Open each app, and look for missing or unreadable texts. 