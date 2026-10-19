# Збирання на macOS (Docker)

> Це тимчасова стаття. Сучасніший спосіб через Homebrew — у [Збиранні прошивки](Compile-firmware#compiling-mayhem-firmware-on-macos).

1. На **github.com** (створіть акаунт, якщо немає) зробіть власний форк **portapack-mayhem/mayhem-firmware**.
2. Завантажте й встановіть [GitHub Desktop](https://desktop.github.com).
3. Запустіть GitHub Desktop, увійдіть і клонуйте свій форк у локальну теку.
4. Завантажте й встановіть Docker Desktop для Mac.
5. Запустіть Docker Dashboard.
6. Увійдіть у Docker Hub (створіть акаунт на hub.docker.com).
7. У терміналі перейдіть у теку з клонованим репозиторієм.
8. Виконайте: `docker pull eried/portapack`.
9. Створіть теку build: `mkdir build`.

## Збирання

У командному рядку: `docker build -t portapackccache -f dockerfile-nogit .`

Для процесорів M2 і новіших: `docker build --platform linux/amd64 -t portapackccache -f dockerfile-nogit .`

Без `--platform linux/amd64` запуск контейнера впаде з помилками на кшталт `qemu-x86_64: Could not open '/lib64/ld-linux-x86-64.so.2'`.

## Компіляція

```
docker run -it -v ${PWD}:/havoc portapackccache
```

На машині автора зайняло близько 25 хвилин. Наприкінці ви маєте побачити `[100%] Built target firmware` і згенерований `portapack-h1_h2-mayhem.bin`.
