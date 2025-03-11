# Разработка Погода
#/usr/bin/python
# -*- encoding: utf-8 -*-
import pyowm
city=input('Какой город вас интересует? ')
owm = pyowm.OWM('566b41c32a6a99107ba96c215e9fafea')  # Yeu MUST provide a valid API key
# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('city')
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
print("В городе" + city  +" Сейчас температура: " + str(temperature))                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>
# Weather details
#w.get_wind()                  # {'speed': 4.6, 'deg': 330}
#w.get_humidity()              # 87
#w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-2257, -43.12)