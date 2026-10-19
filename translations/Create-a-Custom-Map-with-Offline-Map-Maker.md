# Створення власної карти через Offline Map Maker

Це посібник зі створення власної карти для PortaPack, а **не** карти з особливими деталями.

## Для кого це

Може бути корисним, якщо ваш регіон на стандартній карті замалий чи нечіткий.

## Кроки (Offline Map Maker)

1. Завантажте Offline Map Maker з [офіційного сайту](https://www.allmapsoft.com/omm/index.html) або [напряму](https://www.allmapsoft.com/omm/download/omm_setup.exe).
2. Після встановлення:
   1. Виберіть тип карт у лівому дереві (лише карти з тайлами 256 px; якщо розмір не вказано — зазвичай він 256 за замовчуванням; перевірити можна [тут](https://www.allmapsoft.com/tilesample.html)).
   2. Введіть назву завдання, наприклад `newtask.omm`.
   3. Задайте діапазон рівнів масштабу. Для найкращої чіткості беріть найвищий (у безкоштовній версії 13, у платній 19). Вищий масштаб = більший файл.
   4. Введіть 4 параметри області (Left Longitude, Right Longitude, Top Latitude, Bottom Latitude) або [завантажте KML](https://www.allmapsoft.com/omm/support.htm#kml).
   5. Виберіть шлях для збереження проєкту й зображень.
   6. Натисніть «Start».

### Об'єднання завантажених тайлів

7. Після успішного завантаження перейдіть у «Tools» → «Map Combiner»:
   1. Відкрийте теку з завантаженням (переконайтеся, що позначено «Create a JPEG file» і обрано ваш масштаб).
   2. Натисніть «Combine».

Детальніші інструкції — на [офіційному сайті](https://www.allmapsoft.com/omm/support.htm).

## Нарешті

1. Перейменуйте об'єднане зображення на `world_map.jpg`.
2. Покладіть його в `sdcard/ADSB/world_map.jpg`.
3. Запустіть `firmware/tools/generate_world_map.bin.py` — карта згенерується як `sdcard/ADSB/world_map.bin`.
4. Покладіть `.bin` у теку `ADSB/` на SD-картці.

## Важливо

- Встановіть Python (автор використовував 3.10).
- Встановіть Pillow: `pip install Pillow`.

[Відео: заміна карти світу на H4M](https://youtu.be/J1_U-G8m0Sk) ⚠️ воно **не** охоплює локальні/власні карти. Для власної (локальної) карти також потрібна зміна у `ui_geomap.cpp` (`/firmware/application/ui/`) і перезбирання проєкту.

## Код

Щоб побачити свою власну карту, треба змінити код — функцію `void GeoMap::move(const float lon, const float lat)` (приблизно рядок 197 `ui_geomap.cpp`). Замініть її на варіант, що враховує координати вашої карти:

```cpp
void GeoMap::move(const float lon, const float lat) {
    lon_ = lon;
    lat_ = lat;

    // Введіть координати вашої карти
    double mapLeftLon = 79.14;
    double mapRightLon = 81.89;
    double mapLonDelta = mapRightLon - mapLeftLon;
    double mapBottomLat = 5.86;
    double mapBottomLatDegree = mapBottomLat * pi / 180;

    Rect map_rect = screen_rect();

    // Проєкція WGS 84 / Pseudo-Mercator
    x_pos = (lon_ - mapLeftLon) * (map_width / mapLonDelta) - (map_rect.width() / 2);

    double lat_rad = lat_ * pi / 180;
    double map_world_lon = ((map_width / mapLonDelta) * 360) / (2 * pi);
    double map_offset = (map_world_lon / 2 * log((1 + sin(mapBottomLatDegree)) / (1 - sin(mapBottomLatDegree))));
    y_pos = map_height - ((map_world_lon / 2 * log((1 + sin(lat_rad)) / (1 - sin(lat_rad)))) - map_offset);

    // Обмеження позиції
    if (x_pos > (map_width - map_rect.width())) x_pos = map_width - map_rect.width();
    if (y_pos > (map_height + map_rect.height())) y_pos = map_height - map_rect.height();
}
```

У тесті автора проєкції зміщені приблизно на 60–90 м — непогано.

## Пояснення коду

Усе, що потрібно:
1. Введіть `mapLeftLon` — «Left Longitude».
2. Введіть `mapRightLon` — «Right Longitude».
3. Введіть `mapBottomLat` — «Bottom Latitude».

Це ті значення, які ви вводили / завантажували через KML на кроці 4. Якщо у вашому KML багато знаків після коми — вводьте їх точно.
