# Юніт-тести

## Коротко

```
cmake --build . --target build_tests && ctest --output-on-failure
```

## Тести

- Юніт-тести написані з використанням фреймворку [doctest](https://github.com/doctest/doctest).
- Тести розділені на application і baseband залежно від цільового ядра.
- Вихідний код тестів — у `firmware/test/`.
- Тести наразі не інтегровані в пайплайн PR.
- Тести наразі не збираються під час звичайної збірки — їх треба збирати вручну.

## Збирання тестів

У теці збірки CMake виконайте `cmake --build . --target build_tests` — це збере хости тестів для application і baseband.

## Запуск тестів

Після збирання, з теки збірки CMake: `ctest --output-on-failure`.
