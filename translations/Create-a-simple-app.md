# Створення простого застосунку

> **Попередні слова.** Цей метод — лише демонстрація для початку. Це **не** прийнятий спосіб робити готові до продакшену застосунки. Для свого застосунку використовуйте метод [зовнішнього застосунку](Create-a-simple-external-app).

## Про що це

Ця сторінка показує, як створити простий застосунок, і знайомить з основами кодової бази Mayhem. Вважайте це застосунком «hello world». Ми створимо кілька простих елементів керування й під'єднаємо застосунок до головного меню. Мета — познайомитися з тим, як усе влаштовано.

## Перші кроки

Гнучкості багато, але поки що дотримуймося патернів, уже наявних у коді: назви файлів і класів надихатимемося наявним кодом.

## Код застосунку

Наведена структура — основа будь-якого застосунку. За загальною структурою ці файли в прикладі створюються в `firmware/application/apps/`.

### ui_newapp.hpp

```cpp
#include "ui.hpp"
#include "ui_widget.hpp"
#include "ui_navigation.hpp"
#include "string_format.hpp"

namespace ui
{
    class NewAppView : public View                                // оголошення класу застосунку
    {
    public:
        NewAppView(NavigationView &nav);                          // оголошення функції ініціалізації
        std::string title() const override { return "New App"; }; // заголовок застосунку

    private:
        void update();                                            // оголошення функції
        MessageHandlerRegistration message_handler_update{        // приклад (не обов'язково)
            Message::ID::DisplayFrameSync,                        // передає повідомлення від baseband; щоразу при
            [this](const Message *const) {                        // DisplayFrameSync викликається update()
                this->update();
            }};
    };
}
```

### ui_newapp.cpp

```cpp
#include "ui_newapp.hpp"
#include "portapack.hpp"
#include <cstring>

using namespace portapack;

namespace ui
{
    NewAppView::NewAppView(NavigationView &nav) // головна функція застосунку
    {
         // код застосунку
    }

    void NewAppView::update()                   // виконується при кожному DisplayFrameSync
    {
         // код обробки повідомлення
    }
}
```

## Запис у головне меню

Щоб запускати ваш застосунок, додайте пункт у головне меню. Воно — у `firmware/application/ui_navigation.cpp`. Перегляньте наявні пункти й додайте новий у відповідну секцію.

```cpp
// вгорі — підключіть заголовок свого застосунку
#include "ui_newapp.hpp"
...
// додаємо NewApp у меню Transmitters
const NavigationView::AppList NavigationView::appList = {
    add_items({
        ...
        {"newapp", "NewApp", TX, Color::red(), &bitmap_icon_remote, new ViewFactory<NewAppView>()},
    });
}
```

## Ранній тест

Не забудьте додати `apps/ui_newapp.cpp` у `firmware/application/CMakeLists.txt`:

```cmake
set(CPPSRC
    main.cpp
    ...
    apps/ui_newapp.cpp
)
```

Тепер застосунок можна скомпілювати й протестувати на пристрої (див. [Збирання прошивки](Compile-firmware)). Новий застосунок має з'явитися в обраному меню.

## Додавання віджетів і базової функціональності

Віджети — це елементи, з яких складається UI. Вони визначені в `firmware/common/ui_widget.hpp`, функції — у `firmware/common/ui_widget.cpp`. Щоб ними користуватися, додайте `#include "ui_widget.hpp"` у `.hpp` свого застосунку. Повний список методів — у `ui_widget.hpp`. Детальний перелік віджетів — на сторінці [Віджети](Widgets).

### Під'єднання віджета

Щоб показати віджет, викличте `add_child()` (один віджет) або `add_children()` (кілька) усередині конструктора. Віджети передаються як вказівники:

```cpp
add_child(&my_widget);
// або
add_children({ &widget_1, &widget_2 });
```

Приклади основних віджетів — Button (кнопка; обов'язково реалізуйте `on_select`), Labels (підписи), LiveDateTime (живі дата/час), ProgressBar (смуга прогресу; `set_max`, `set_value`), NumberField (числове поле; значення через колесо, `value()`, `on_change`). Повні конструктори й приклади — на сторінці [Віджети](Widgets).

## Підсумок

Нижче — приклад застосунку «Hello World», що демонструє кілька віджетів і логіку керування ними.

### ui_newapp.hpp

```cpp
#include "ui.hpp"
#include "ui_widget.hpp"
#include "ui_navigation.hpp"
#include "string_format.hpp"

#define PROGRESS_MAX 100

namespace ui
{
    class NewAppView : public View
    {
    public:
        void focus() override;
        NewAppView(NavigationView &nav);
        std::string title() const override { return "New App"; };

    private:
        void update();
        MessageHandlerRegistration message_handler_update{
            Message::ID::DisplayFrameSync,
            [this](const Message *const) { this->update(); }};

        uint32_t progress = 0;

        // Примітка: корисний простір екрана — 240x304 px.
        // Кожен символ — 8x8 px, тож множте кількість символів/рядків на 8 (30x38 символів).
        Button button_helloWorld{ {70, 128, 100, 24}, "Hello World!" };
        LiveDateTime timestamp { {6*8, 22*8, 19*8, 20 } };
        Labels label_progress { {{8*8, 33*8}, "Progress:     %", Color::light_grey()} };
        NumberField numberField_progress { {18*8, 33*8}, 3, {0,PROGRESS_MAX}, 1, '0', false };
        ProgressBar progressBar_progress { {2*8, 35*8, 208, 16 } };
    };
}
```

### ui_newapp.cpp

```cpp
#include "ui_newapp.hpp"
#include "portapack.hpp"
#include <cstring>

using namespace portapack;

namespace ui
{
    void NewAppView::focus() { button_helloWorld.focus(); } // фокус за замовчуванням

    NewAppView::NewAppView(NavigationView &nav)
    {
        add_children({
            &button_helloWorld, &label_progress,
            &numberField_progress, &progressBar_progress, &timestamp,
        });

        progressBar_progress.set_max(PROGRESS_MAX);

        button_helloWorld.on_select = [this](Button &){
            if(progress < 100) { numberField_progress.set_value(100); }
            else { numberField_progress.set_value(0); }
        };

        numberField_progress.on_change = [this](int32_t v) {
            progress = v;
            progressBar_progress.set_value(progress);
        };

        timestamp.set_seconds_enabled(true);
    }

    void NewAppView::update() { /* код обробки повідомлення */ }
}
```
