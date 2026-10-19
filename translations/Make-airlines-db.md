# make_airlines_db.py

Цей інструмент створює базу [airlines.db](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/sdcard/ADSB/airlines.db). Вона використовується, щоб знаходити _назву авіакомпанії_ й _країну_ за трилітерним кодом ICAO. Наразі застосовується лише в приймачі ADS-B.

Джерело бази: <https://raw.githubusercontent.com/kx1t/planefence-airlinecodes/main/airlinecodes.txt>

## Збирання бази

- Завантажте найновішу версію за посиланням вище.
- Завантажте скрипт [make_airlines_db.py](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/tools/make_airlines_db/make_airlines_db.py).
- Покладіть їх у одну теку й запустіть скрипт (потрібен Python 3).
- Скопіюйте базу в теку `/ADSB` на SD-картці.
