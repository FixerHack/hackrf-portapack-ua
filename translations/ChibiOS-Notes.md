# Нотатки про ChibiOS

Різні корисні нотатки про те, як працює ChibiOS.

## Конфігурація стеків

З crt0.c ChibiOS: для Cortex-M доступні два стеки — основний (main) і стек процесу (process).

- **Thread mode** — для виконання прикладного ПЗ. Процесор входить у Thread mode після виходу зі скидання.
- **Handler mode** — для обробки винятків. Після завершення обробки процесор повертається в Thread mode.

ChibiOS налаштовує Cortex-M у двостековому режимі (CONTROL[1]=1). Коли CONTROL[1]=1, у Thread mode використовується PSP. MSP завжди використовується в Handler mode.

- **`__main_stack_size__`** — для обробників винятків.
- **`__process_stack_size__`** — для main().

Після `chSysInit()` поточний потік інструкцій (зазвичай main()) стає основним потоком.

> Оригінальна вікі — sharebrained, [Operating System Notes](https://github.com/sharebrained/portapack-hackrf/wiki/Operating-System-Notes).
