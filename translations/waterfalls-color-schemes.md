# Кольорові схеми водоспаду

Змінити кольорову схему водоспаду можна так: **Utilities → File Manager** → тека **WATERFALLS** → виберіть один із файлів центральною кнопкою.

Щоб повернути типову схему, застосуйте `default.txt` або видаліть файл `waterfall.txt` у корені SD-карти.

Власні схеми зручно створювати застосунком [Waterfall Designer](Waterfall-Designer).

## Схеми

**default** (типова)

![default](https://github.com/user-attachments/assets/7d8a52f1-5f4e-4a43-bc86-fdd8d170f847)

**aurora**

![aurora](https://github.com/user-attachments/assets/ae5b8ac0-d74b-4464-b563-bd7e21297478)

**flame**

![flame](https://github.com/user-attachments/assets/540de9ad-cbbd-4115-8483-cbac779c2a8a)

**matrix**

![matrix](https://github.com/user-attachments/assets/6ce3fb58-4665-4d6e-938c-1d0acb9d3bbb)

**sunset**

![sunset](https://github.com/user-attachments/assets/f8bcb92b-606e-4f6e-879a-cdc740707a82)

## Створення власної схеми

- Додайте новий файл у WATERFALLS.
- Додайте рядки кольорів у форматі `індекс,R,G,B`.
- Усі значення — від 0 до 255 (включно з індексом).
- Між рядками `індекс,R,G,B` кольори утворюють плавні переходи (градієнти).
- Рядки, що починаються з `#`, — коментарі.

Подивіться на наявні файли, особливо `default.txt` — він також містить опис формату.
