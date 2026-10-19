# Створення простого зовнішнього застосунку

## Про що це

Цей посібник показує, як створити **зовнішній застосунок**: самостійний застосунок, який компілюється разом із прошивкою, але постачається окремим файлом `.ppma` на SD-картці, а не вбудовується в образ прошивки. Це **рекомендований** спосіб додати власний застосунок у Mayhem.

Якщо ви зовсім новачок у кодовій базі Mayhem, спершу пройдіть [Створення простого застосунку](Create-a-simple-app) — там простий «hello world», що знайомить з view, віджетами, підписами й кнопками; тут це вважається вже відомим.

## Перші кроки

Ви створите нову теку застосунку в `firmware/application/external/`, додасте потрібні файли, зареєструєте застосунок у збірці й скомпілюєте. Виконуйте кроки по порядку.

## Робочий процес

- Створіть підтеку з назвою застосунку в `firmware/application/external`, наприклад `firmware/application/external/new_external_app`.
- Створіть базову структуру з `.hpp`/`.cpp`. Має бути `main.cpp` і щонайменше ще два файли.

**main.cpp** (ключова частина — структура `application_information_t`):

```cpp
#include "ui.hpp"
#include "ui_new_external_app.hpp"
#include "ui_navigation.hpp"
#include "external_app.hpp"

namespace ui::external_app::ui_new_external_app {
void initialize_app(ui::NavigationView& nav) {
    nav.push<NewExternalAppView>();
}
}

extern "C" {
__attribute__((section(".external_app.app_ui_new_external_app.application_information"), used))
application_information_t _application_information_ui_new_external_app = {
    /*.memory_location = */ (uint8_t*)0x00000000,
    /*.externalAppEntry = */ ui::external_app::ui_new_external_app::initialize_app,
    /*.header_version = */ CURRENT_HEADER_VERSION,
    /*.app_version = */ VERSION_MD5,
    /*.app_name = */ "NewExternalApp",
    /*.bitmap_data = */ { /* 16x16 1-бітна іконка */ },
    /*.icon_color = */ ui::Color::cyan().v,
    /*.menu_location = */ app_location_t::DEBUG,
    /*.desired_menu_position = */ -1,
    /*.m4_app_tag = */ {0, 0, 0, 0},
    /*.m4_app_offset = */ 0x00000000,  // заповнюється під час компіляції
};
}
```

**new_external_app.hpp** — оголошення класу view (успадковує `View`, має `focus()`, `title()`, віджети).

**new_external_app.cpp** — реалізація конструктора: `add_children({...})`, `button_exit.on_select = [this](Button&){ nav_.pop(); }`.

### Важливі налаштування

- Замініть `app_location_t` у `main.cpp` на місце для застосунку: `RX`, `TX`, `DEBUG`, `UTILITIES`, `HOME`.
- Не забудьте узгодити header guard, назву класу й зовнішній namespace з назвою застосунку.
- Налаштуйте рядок `/*.m4_app_tag = */ {0, 0, 0, 0}` у `main.cpp` на потрібний baseband (список у `firmware/common/spi_image.hpp`). **Якщо застосунок використовує кілька baseband'ів, вкажіть тут найбільший (зазвичай NFM).**
- Замініть іконку: скопіюйте потрібну з `firmware/application/bitmap.hpp`.
- Якщо використали приклад, замініть усі входження `new_external_app` на назву свого застосунку, а `NewExternalAppView` — на свій клас.
- **Linker-скрипти редагувати вручну не треба.** Три скрипти `external_tier0.ld`, `external_tier1.ld`, `external_tier2.ld` генеруються автоматично з маркерів `tier.txt` застосунків скриптом `tools/update_external_tier_ld.py`, який CMake запускає щозбірки. Просто зберіть один раз і закомітьте перегенеровані `.ld`.
- За бажання додайте файл `tier.txt` з одним числом, що керує тим, коли застосунок вбудовується В прошивку, а не як зовнішній `.ppma`:
  - `0` (або немає `tier.txt`) — ніколи не внутрішній, зовнішній у кожній збірці (звичайний випадок);
  - `1` — вбудовується на пристроях 2 МБ (PortaRF) і більших (HackRF Pro);
  - `2` — вбудовується лише на пристроях >2 МБ (HackRF Pro);
  - `-1` — вимкнено, не входить у жодну збірку.
  - Для tier `1` чи `2` треба також `#include` заголовок у `firmware/application/ui_navigation.cpp` у блоці `#if FLASH_TIER >= N` (інакше збірка відмовить). Звичайному зовнішньому застосунку цього не треба.
- У `external.cmake` додайте блок свого коду в `EXTCPPSRC`:
  ```
  # new_external_app
  external/new_external_app/main.cpp
  external/new_external_app/new_external_app.cpp
  ```
- У `external.cmake` додайте назву застосунку в блок `EXTAPPLIST`.
- Готово — зберіть прошивку, і ваш зовнішній застосунок збереться разом із нею.
- Прошийте `ppfw` через сайт hackrf.app або скопіюйте файл на SD-картку й скористайтеся прошивачем на пристрої.

## Приклад онлайн

Користувач aquilestraigo, який зробив внесок у застосунок OOK Editor, також написав гарну сторінку про свою пригоду зі створенням зовнішнього застосунку: <https://blog.hawktesters.com/rookremote-on-off-keying-for-to-portapack-hackrf/>. Там досить докладно й, можливо, знайдуться пояснення, яких тут бракує.
