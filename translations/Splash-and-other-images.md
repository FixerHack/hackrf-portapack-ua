# Конвертери зображень (заставка та іконки)

## Заставка (splash screen)

Для конвертації між зображенням і джерелом можна використати `xxd`. У Windows це робиться в підсистемі Linux (WSL), наприклад з Ubuntu.

- **З .bmp у .hpp:** `xxd -i input_image.bmp output.hpp`
- **З .hpp у .bmp:** `xxd -r -p input.hpp output_image.bmp`

Є також python-помічник у `firmware/tools/bmp_tools`.

## Іконки прошивки

Спеціальний файл `firmware/application/bitmap.hpp` містить усі іконки прошивки. **Його не можна редагувати напряму!** Натомість нові іконки копіюють у `firmware/graphics`, а потім запускають `pp_png2hpp.py`, щоб створити `bitmap.hpp`. Для python-скриптів потрібна бібліотека Pillow: `pip install pillow`.

### make_bitmap.py — тека з icon.png → bitmap.hpp

Традиційний, добре перевірений помічник. Тека з іконками передається аргументом; результат `bitmap.hpp` копіюється в `firmware/application/`. З теки `tools/`:

```
python3 bitmap_tools/make_bitmap.py ../graphics/ && mv bitmap.hpp ../application/bitmap.hpp
```

Розмір іконки має бути кратним 8. Згенерована іконка — чорно-біла.

### bitmap_arr_reverse_decode.py — масив bitmap → icon.png

Бере масив із `bitmap.hpp` і конвертує назад у png.

### pp_png2hpp.py — в обидва боки

Рішення «все в одному». З аргументами `--hpp bitmap.hpp` і `--graphics /folder_to/png_icons/` генерує `bitmap.hpp`. Додайте `--reverse`, щоб згенерувати png-іконки з наявного `bitmap.hpp` (зворотна функція має парсер, що автоматично бере ім'я й розмір зображення).

```
# png → hpp
./bitmap_tools/pp_png2hpp.py ../application/bitmap.hpp ../graphics

# hpp → png (лише логотип titlebar_image за замовчуванням)
./bitmap_tools/pp_png2hpp.py ../application/bitmap.hpp /tmp/ --reverse

# конкретна іконка або всі
./bitmap_tools/pp_png2hpp.py ../application/bitmap.hpp /tmp/ --reverse --icon all
```

> **Примітка:** це не відновлення — іконки генеруються заново, чорно-білими, навіть якщо оригінали були прозорими.

## Онлайн-редактор

Поточні іконки створено на [Piskelapp](https://www.piskelapp.com/). Для створення чи оновлення можна використати наявні джерела (16×16 або 8×8).
