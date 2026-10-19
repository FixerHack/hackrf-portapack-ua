# Як швидше компілювати у Windows з WSL 2

*Примітка: лише для Windows.*

Кроки зі сторінки [Збирання прошивки](Compile-firmware) працюють, але кожна компіляція може тривати близько 35 хвилин. Тут показано, як скоротити цей час до 2 секунд – 1 хвилини (залежно від апаратури).

1. Завантажте Ubuntu з Microsoft Store.
2. Відкрийте термінал Windows і виконайте `wsl -l -v` — перевірте, що версія 2. Якщо ні: `wsl --set-default-version 2`, потім `wsl --set-version Ubuntu 2`.
3. Відкрийте застосунок Ubuntu (переконайтеся, що потрапляєте в консоль).
4. У Docker на Windows: Settings → Resources → WSL Integration.
5. Увімкніть Ubuntu (якщо немає — натисніть refresh).
6. У Провіднику Windows перейдіть за адресою `\\wsl$\`.
7. Перейдіть у `Ubuntu/home/{username}/`.
8. Скопіюйте теку portapack-mayhem сюди.
9. Переконайтеся, що WSL бачить її: `cd ~/portapack-mayhem`.
10. Запустіть Docker: `docker run -it -v ~/portapack-mayhem:/havoc portapack-dev`.
11. Готово! Тепер має компілюватися дуже швидко.

Можна налаштувати мережеву теку до `\\wsl$\Ubuntu\home\{username}\portapack-mayhem` і редагувати файли з Windows.

## Помилки при компіляції?

Після кроку 5:

1. Відкрийте Ubuntu.
2. `sudo git clone --recurse-submodules https://github.com/portapack-mayhem/mayhem-firmware.git` (якщо не компілюється — `git submodule update --init --recursive`).
3. Надайте права: `whoami`, потім `sudo chown -R my_user:my_usergroup /home/{username}/portapack-mayhem`.
4. Створіть теку build: `cd portapack-mayhem`, `mkdir build`.

### Передумови

Запобігти помилці `'python/r' not found`: `git config --global core.autocrlf false`.

### Компіляція

```
docker build -t portapack-dev -f dockerfile-nogit .
docker run -it -v ~/portapack-mayhem:/havoc portapack-dev
```

Перша компіляція зайняла близько 8 хв 43 с, друга (після зміни ~25 рядків) — 3 секунди.

Докладніше про WSL 2 — [офіційна документація Microsoft](https://learn.microsoft.com/en-us/windows/wsl/install-manual).
