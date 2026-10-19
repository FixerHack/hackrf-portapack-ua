# make_icao24_db.py

Цей інструмент створює базу [icao24.db](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/sdcard/ADSB/icao24.db). Вона використовується, щоб знаходити інформацію про літак за 24-бітним кодом транспондера ICAO. Наразі застосовується лише в приймачі ADS-B.

Джерело бази: <https://opensky-network.org/datasets/metadata/aircraftDatabase.csv>

## Збирання бази

- Скопіюйте файл із <https://opensky-network.org/datasets/metadata/aircraftDatabase.csv>.
- Запустіть Python 3 [скрипт](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/firmware/tools/make_airlines_db/make_icao24_db.py): `./make_icao24_db.py`.
- Скопіюйте файл у теку `/ADSB` на SD-картці.
