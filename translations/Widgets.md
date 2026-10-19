# Віджети

## Про віджети

Віджети — це елементи, з яких складається UI вашого застосунку. Вони визначені в `firmware/common/ui_widget.hpp`, а функції — у `firmware/common/ui_widget.cpp`. Щоб ними користуватися, додайте `#include "ui_widget.hpp"` у `.hpp` свого застосунку. Типів віджетів кілька; нижче — список доступних з їхніми конструкторами. Повний перелік методів завжди дивіться у `ui_widget.hpp` (можуть додавати нові).

## Під'єднання віджета

Щоб показати віджет, викличте `add_child()` (один) або `add_children()` (кілька) усередині конструктора view. Віджети передаються як вказівники:

```cpp
add_child(&my_widget);
// або
add_children({ &widget_1, &widget_2 });
```

## Доступні віджети

### Text

Просте текстове поле.

```cpp
Text hello_world_text_widget(
  {10, 10, 100, 24}, // x, y, ширина, висота (px)
  "Hello world!"
);
```

### Button

Кнопка виконує дію при натисканні. Щоразу обов'язково реалізуйте `my_button.on_select = [&nav](Button &){}` — можна порожнім, але має бути присутнім.

```cpp
Button my_button( {10, 10, 100, 24}, "my_button_text" );
```

### Labels

Текстові підписи для опису інших віджетів. Конструктор очікує список, тож дужки `{}` навколо кожного підпису обов'язкові.

```cpp
Labels my_label{
    {{10, 10}, "my_label_text:", Color::light_grey()},
};
```

> Кольори визначені у `firmware/common/ui.hpp`.

### LiveDateTime

Динамічні дата й час.

```cpp
LiveDateTime my_liveDateTime { { 2, 10, 19*8, 16 } };
my_liveDateTime.set_seconds_enabled(true); // увімкнути секунди
```

### BigFrequency

Відображення радіочастоти великим шрифтом.

```cpp
BigFrequency my_bigFrequency( {10, 10, 28*8, 52}, 0 );
my_bigFrequency.set(433000000); // 433 МГц
```

### ProgressBar

Візуальне представлення прогресу завдання.

```cpp
ProgressBar my_progressBar { { 2, 10, 208, 16 } };
my_progressBar.set_max(10);   // 10 = 100%
my_progressBar.set_value(5);  // 50%
```

### Console

Велике текстове поле для виводу змінюваних рядків.

```cpp
Console my_console { { 2*8, 10, 208, 200 } };
my_console.write("Hello World");
my_console.writeln("…з нового рядка!"); // додає \n
my_console.enable_scrolling(true);
```

> Розмір буфера обмежено 256 символами.

### Checkbox

Булевий (true/false) віджет: прямокутник із зеленою галочкою (true) або червоним хрестиком (false).

```cpp
Checkbox my_checkbox(
    {10, 20}, 4, "my_checkbox_text",
    false // розмір: true == малий (16x16), false == звичайний (24x24)
);
// читання: my_checkbox.value(); запис: my_checkbox.set_value(true);
my_checkbox.on_select = [this](Checkbox&, bool v) { if(v) do_a(); else do_b(); };
```

### Image

Зображення в застосунку. Спершу треба створити об'єкт `Bitmap`:

```cpp
static constexpr uint8_t bitmap_stripes_data[] = { /* дані */ };
static constexpr Bitmap bitmap_stripes { { 24, 8 }, bitmap_stripes_data };

Image my_image(
    {10, 10, 24, 8}, &Bitmap,
    Color::white(), Color::black()
);
```

### OptionsField

Поле з переліком значень, яке змінюється колесом. `parent_pos` — позиція лівого верхнього кута, length — кількість опцій, options_t — масив опцій. `centered` (за замовчуванням false) центрує текст.

```cpp
OptionsField my_optionsField{
    {10,10}, 7,
    { {"option1",0}, {"option2",1}, {"option3",2} }
};
// значення: my_optionsField.selected_index_value();
```

### NumberField

Як OptionsField, але лише для чисел; значення — колесом.

```cpp
NumberField my_numberField( {10, 10}, 3, {0, 255}, 1, '0', false );
int number = my_numberField.value();
my_numberField.set_value(123);
my_numberField.on_change = [this](int32_t v) { number = v; };
```

### Waveform

Відображення форми хвилі з джерела сигналу (вісь X — час, Y — амплітуда). Дані — масив `int16_t`.

```cpp
Waveform my_waveform(
    {0, 5*16, 240, 64}, waveform_buffer, 128, 0, false, Color::white()
);
my_waveform.set_length(new_length); // для змінної довжини даних
```

### VuMeter

Візуальне представлення інтенсивності звуку аудіоджерела.

```cpp
VuMeter my_vuMeter( { 0*8, 1*8, 2*8, 33*8}, 12, true );
my_vuMeter.set_value(123); // максимум 255
```
