# SD-картка (для розробника)

## Про що це

Читання й запис SD-картки — чудовий спосіб зберігати прогрес застосунку чи довідкові дані, завеликі для прошивки. Нижче — приклади роботи з SD-карткою в кодовій базі Mayhem.

## Клас File

Основну роботу з файлами виконує клас `File` — обгортка над FatFs (`firmware/chibios-portapack/ext/fatfs/src/ff.c`). Продовжуючи [Створення простого застосунку](Create-a-simple-app), додайте в `.hpp` застосунку:

```cpp
#include "file.hpp"
#include "sd_card.hpp"
```

> У всіх прикладах шлях — це `std::filesystem::path`, який може бути UTF-16-літералом. Корінь SD-картки — `u""`, будь-яка тека далі — `u"DIRECTORY/SUB_DIRECTORY"`.

### Перевірка SD-картки

Перед читанням/записом бажано швидко перевірити, чи картка змонтована. У фоні є обробка помилок, що запобігає збоям, але так користувач краще зрозуміє, чи є проблема. Статуси визначені в `firmware/application/sd_card.hpp`.

```cpp
bool NewAppView::check_sd_card() {
    return (sd_card::status() == sd_card::Status::Mounted) ? true : false;
}
```

### Перелік вмісту теки

Структура з інформацією про запис (шлях, розмір, чи це тека):

```cpp
struct file_entry {
    std::filesystem::path entry_path { };
    uint32_t size { };
    bool is_directory { };
};
```

Функція повертає вектор `file_entry` (теки — на початку, файли — в кінці; пропускає приховані файли, що починаються з `.`):

```cpp
std::vector<file_entry> NewAppView::list_dir(const std::filesystem::path& path) {
    std::vector<file_entry> entry_list { };
    for (const auto& entry : std::filesystem::directory_iterator(path, u"*")) {
        if (entry.path().string().length() && entry.path().filename().string()[0] != '.') {
            if (std::filesystem::is_regular_file(entry.status())) {
                entry_list.push_back({ entry.path(), (uint32_t)entry.size(), false });
            } else if (std::filesystem::is_directory(entry.status())) {
                entry_list.insert(entry_list.begin(), { entry.path(), 0, true });
            } else {
                continue;
            }
        }
    }
    return entry_list;
}
```

### Створення теки

`make_new_directory()` повертає 0 при успіху (інше — помилка), тож допоміжна функція інвертує результат:

```cpp
bool NewAppView::create_dir(const std::filesystem::path& path, std::string name) {
    return !(make_new_directory(path.string() + "/" + name));
}
```

### Створення файлу

```cpp
bool NewAppView::create_file(const std::filesystem::path& path, std::string name) {
    File file = { };
    Optional<File::Error> success = file.create(path.string() + "/" + name);
    return !(success.is_valid()); // 0 = успіх
}
```

## Про читання й запис

> **!! Апаратне обмеження: буфер читання/запису не може перевищувати блоки по 512 байтів. Розмір буфера не повинен бути більшим за 512 !!** (див. обговорення issue #1103)

### Читання файлу

> **Примітка:** наведений приклад не обробляє великі файли — для них потрібне керування пам'яттю.

```cpp
std::string NewAppView::read_file(const std::filesystem::path& path, std::string name) {
    std::string return_string = "";
    File file;
    auto success = file.open(path.string() + "/" + name);
    if(!success.is_valid()) { // 0 = успіх
        char one_char[1];
        for(size_t pointer = 0; pointer < file.size(); pointer++) {
            file.seek(pointer);
            file.read(one_char, 1);
            return_string += one_char[0];
        }
    } else {
        return "0"; // проста обробка помилок
    }
    return return_string;
}
```

### Запис файлу

`append()` відкриває файл на дозапис; `write_line()` / `write()` записує дані:

```cpp
bool NewAppView::write_file(const std::filesystem::path& path, std::string name, std::string data) {
    File file;
    auto success = file.append(path.string() + "/" + name);
    if(!success.is_valid()) {
        file.write_line(data);
        return true;
    }
    return false;
}
```

### Перейменування файлу чи теки

```cpp
bool NewAppView::rename_dir_or_file(const std::filesystem::path& path, std::string old_name, std::string new_name) {
    return !(rename_file(path.string() + "/" + old_name, new_name)); // 0 = успіх
}
```

### Видалення файлу чи теки

```cpp
bool NewAppView::delete_dir_or_file(const std::filesystem::path& path, std::string name) {
    return !(delete_file(path.string() + "/" + name));
}
```

## Підсумок

Нижче — демо всіх базових CRUD-операцій для файлів і тек. Кожну операцію обгорнуто в перевірку `check_sd_card()`, а результати виводяться у віджет `Console`.

### ui_newapp.hpp

```cpp
#include "ui.hpp"
#include "ui_widget.hpp"
#include "ui_navigation.hpp"
#include "string_format.hpp"
#include "file.hpp"
#include "sd_card.hpp"

namespace ui
{
    struct file_entry {
        std::filesystem::path entry_path { };
        uint32_t size { };
        bool is_directory { };
    };

    class NewAppView : public View {
    public:
        void focus() override;
        NewAppView(NavigationView &nav);
        std::string title() const override { return "New App"; };
    private:
        bool check_sd_card();
        bool create_dir(const std::filesystem::path& path, std::string name);
        std::vector<file_entry> list_dir(const std::filesystem::path& path);
        bool create_file(const std::filesystem::path& path, std::string name);
        bool rename_dir_or_file(const std::filesystem::path& path, std::string old_name, std::string new_name);
        std::string read_file(const std::filesystem::path& path, std::string name);
        bool write_file(const std::filesystem::path& path, std::string name, std::string data);
        bool delete_dir_or_file(const std::filesystem::path& path, std::string name);

        Console my_console { { 1*8, 1*8, 224, 296 } };
    };
}
```

### ui_newapp.cpp (конструктор — послідовність демо)

```cpp
NewAppView::NewAppView(NavigationView &nav) {
    add_children({ &my_console });
    my_console.enable_scrolling(true);

    // Перевірка картки
    my_console.writeln(check_sd_card() ? "+ SD Card is Mounted" : "- SD Card is NOT Mounted");

    // Створення теки
    if(check_sd_card() && create_dir(u"", "NEW_DIR")) my_console.writeln("+ New directory created");
    else my_console.writeln("- New directory FAILED");

    // Перелік теки
    std::vector<file_entry> files = check_sd_card() ? list_dir(u"") : std::vector<file_entry>{};
    my_console.writeln("+ dir SD Card: " + std::to_string(files.size()) + " items");

    // Перейменування теки
    if(check_sd_card() && rename_dir_or_file(u"", "NEW_DIR", "NEWER_DIR")) my_console.writeln("+ Directory renamed");
    else my_console.writeln("- Directory renamed FAILED");

    // Видалення теки
    if(check_sd_card() && delete_dir_or_file(u"", "NEWER_DIR")) my_console.writeln("+ New directory deleted");
    else my_console.writeln("- New directory deleted FAILED");

    // Створення, перейменування, запис, читання, видалення файлу — за тим самим шаблоном:
    create_file(u"", "NEW_FILE.txt");
    rename_dir_or_file(u"", "NEW_FILE.txt", "NEWER_FILE.TXT");
    std::string data = "Your mother was a hamster!";
    write_file(u"", "NEWER_FILE.TXT", data);
    std::string read_back = read_file(u"", "NEWER_FILE.TXT");
    my_console.writeln("+ Read file: " + read_back);
    delete_dir_or_file(u"", "NEWER_FILE.TXT");

    my_console.writeln("+ Demo Complete");
}
```

(Повну, нескорочену версію конструктора з усіма гілками обробки помилок дивіться в англійській вікі; тут її ущільнено заради читабельності.)
