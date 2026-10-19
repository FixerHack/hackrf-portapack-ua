# Доступ до радіообладнання

## Про що це

Тут ми переходимо до дечого складнішого й долучаємо радіо. Якщо ви не знайомі з LPC43xx, спершу прочитайте [Архітектуру прошивки](Firmware-Architecture).

Досі ми мали справу лише з кодом застосунку, що виконується на ядрі M0 LPC43xx. Тепер почнемо працювати з baseband-частиною, що виконується на ядрі M4. Обидва ядра використовують 8 КБ спільної пам'яті (`0x1008_8000`…`0x1008_a000`) для обміну повідомленнями. M0 керує **всіма** операціями PortaPack, а M4 здебільшого обробляє DSP і радіофункції.

Доступ до радіообладнання HackRF спрощено допоміжними класами `TransmitterModel` і `ReceiverModel` — обидва взаємодіють з baseband-процесами M4 й дають зручніший спосіб керувати радіо. Інші класи/структури — `baseband api` і `SharedMemory` — також з'єднують M0 і M4. Навіть попри те, що головна відповідальність M4 — DSP з радіо, M0 теж може декодувати дані (наприклад, класи з `firmware/application/protocols/`, як-от `encoders`, кодують/декодують повідомлення вищого рівня).

## Передавання (TX)

Нижче — приклад OOK TX-застосунку з використанням `TransmitterModel`, `encoders` і `baseband`.

**ui_newapp.hpp** — оголошення функцій `start_tx`, `stop_tx`, `on_tx_progress` і реєстрація обробника повідомлень `TXProgress`:

```cpp
#include "transmitter_model.hpp"

namespace ui {
    class NewAppView : public View {
    private:
        void start_tx(std::string& message);
        void stop_tx();
        void on_tx_progress(const uint32_t progress, const bool done);

        MessageHandlerRegistration message_handler_tx_progress {
            Message::ID::TXProgress,
            [this](const Message* const p) {
                const auto message = *reinterpret_cast<const TXProgressMessage*>(p);
                this->on_tx_progress(message.progress, message.done);
            }};
    };
}
```

**ui_newapp.cpp** — налаштування передавача й запуск OOK:

```cpp
#include "encoders.hpp"
#include "baseband_api.hpp"
using namespace portapack;

namespace ui {
    void NewAppView::start_tx(std::string& message) {   // повідомлення як "101101"
        size_t bitstream_length = make_bitstream(message); // з encoders.hpp

        transmitter_model.set_tuning_frequency(433920000); // центральна частота, Гц
        transmitter_model.set_sampling_rate(OOK_SAMPLERATE);
        transmitter_model.set_rf_amp(true);
        transmitter_model.set_baseband_bandwidth(1750000);
        transmitter_model.enable();

        baseband::set_ook_data(
            bitstream_length,
            OOK_SAMPLERATE / 1766,  // період символу (560 мкс) = Sample Rate / Baud
            4,                      // повторів передачі
            100                     // символи паузи
        );
    }

    void NewAppView::stop_tx() {
        transmitter_model.disable();
        // UI-логіка: повідомити користувача про зупинку TX
    }

    NewAppView::NewAppView(NavigationView &nav) {
        baseband::run_image(portapack::spi_flash::image_tag_ook); // наказати M4 запустити proc_ook.cpp
        // логіка віджетів і виклики start_tx()
    }

    void NewAppView::on_tx_progress(const uint32_t progress, const bool done) {
        if(done) stop_tx();
        else { /* оновити ProgressBar значенням progress */ }
    }
}
```

## Приймання (RX)

Розвиваючи приклад TX, поговорімо про те, як baseband-процеси запускаються на M4. Код застосунку на M0 викликає `baseband::run_image`, щоб наказати M4 запустити процес. Baseband-образи визначені в `spi_image.hpp` як структура `image_tag_t` з 4-символьним тегом-ідентифікатором. Приклад для AFSK RX:

```cpp
constexpr image_tag_t image_tag_afsk_rx { 'P', 'A', 'F', 'R' };
```

У `firmware/baseband/CMakeLists.txt` baseband-процеси прив'язуються до образів:

```cmake
### AFSK RX
set(MODE_CPPSRC proc_afskrx.cpp)
DeclareTargets(PAFR afskrx)
```

Код процесів («proc») для M4, як-от `proc_afskrx.cpp`, лежить у `firmware/baseband`. Ці класи запускає `BasebandThread`; усі вони успадковують `BasebandProcessor` і мають реалізувати його функції:

```cpp
class BasebandProcessor {
public:
    virtual ~BasebandProcessor() = default;
    virtual void execute(const buffer_c8_t& buffer) = 0; // DSP-код TX/RX; звідси можна слати повідомлення на M0
    virtual void on_message(const Message* const) { };   // повідомлення від M0
protected:
    void feed_channel_stats(const buffer_c16_t& channel);
private:
    ChannelStatsCollector channel_stats { };
};
```

### Повідомлення між ядрами

Клас `Message` — у `firmware/common/` (спільний код для M0 і M4). Повідомлення обробляє EventDispatcher: `event_m4.cpp` для baseband і `event_m0.cpp` для застосунку. У `message.hpp` визначені конкретні класи повідомлень та ID. Приклад для AFSK RX: `AFSKRxConfigureMessage` (M0 → M4, з baudrate, word_length тощо) і `AFSKDataMessage` (M4 → M0, з `is_data` і `value`).

`SharedMemory` (у `firmware/common/`) передає дані між M0 і M4. У `proc_afskrx.cpp` дані повертаються в застосунок так:

```cpp
#include "portapack_shared_memory.hpp"
void AFSKRxProcessor::execute(const buffer_c8_t& buffer) {
    // ... RX-логіка
    shared_memory.application_queue.push(data_message); // data_message — об'єкт AFSKDataMessage
    // ... ще RX-логіка
}
```

Приклад RX AFSK-застосунку:

**ui_newapp.hpp** — реєстрація обробника `AFSKData`:

```cpp
#include "receiver_model.hpp"
namespace ui {
    class NewAppView : public View {
    private:
        void start_rx();
        void stop_rx();
        void on_data();
        MessageHandlerRegistration message_handler_packet {
            Message::ID::AFSKData,
            [this](Message* const p) {
                const auto message = static_cast<const AFSKDataMessage*>(p);
                this->on_data(message->value, message->is_data);
            }};
    };
}
```

**ui_newapp.cpp** — налаштування приймача, модему та аудіо:

```cpp
#include "modems.hpp"
#include "audio.hpp"
#include "baseband_api.hpp"
#include "portapack_persistent_memory.hpp"
using namespace portapack;
using namespace modems;

namespace ui {
    void NewAppView::start_rx() {
        auto def_bell202 = &modem_defs[0];
        persistent_memory::set_modem_baudrate(def_bell202->baudrate); // 1200 бод

        serial_format_t serial_format;
        serial_format.data_bits = 7;
        serial_format.parity = EVEN;
        serial_format.stop_bits = 1;
        serial_format.bit_order = LSB_FIRST;
        persistent_memory::set_serial_format(serial_format);

        baseband::set_afsk(persistent_memory::modem_baudrate(), 8, 0, false);

        receiver_model.set_tuning_frequency(433920000);
        receiver_model.set_sampling_rate(3072000);
        receiver_model.set_baseband_bandwidth(1750000);
        receiver_model.set_modulation(ReceiverModel::Mode::NarrowbandFMAudio);
        receiver_model.enable();

        audio::set_rate(audio::Rate::Hz_24000); // вивід аудіо в роз'єм навушників
        audio::output::start();
    }

    void NewAppView::stop_rx() {
        audio::output::stop();
        receiver_model.disable();
        baseband::shutdown();
    }

    NewAppView::NewAppView(NavigationView &nav) {
        baseband::run_image(portapack::spi_flash::image_tag_afsk_rx);
        // логіка віджетів і виклики start_rx()/stop_rx()
    }

    void NewAppView::on_data(uint32_t value, bool is_data) {
        if(is_data) { /* обробка RX-даних */ }
    }
}
```
