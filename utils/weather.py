import json

import requests


class Weather(object):
    def __init__(self):
        self.key = '6ca2d6f67093ab1d4a855ca84ce1d6a3'
        self.ipaddr = 'https://restapi.amap.com/v3/ip'
        self.weatheraddr = 'https://restapi.amap.com/v3/weather/weatherInfo'

    def getadcode(self, ip):
        response = requests.get(self.ipaddr, {'key': self.key, 'ip': ip})
        adcode = json.loads(response.text)['adcode']
        print(adcode)
        return adcode

    def getliveweather(self, adcode):
        response = requests.get(self.weatheraddr, {'city': adcode, 'extensions': 'base', 'key': self.key})
        try:
            lives = json.loads(response.text)['lives']
            print(lives[0])
            return lives[0]
        except:
            return {}

    def getforecast(self, adcode):
        response = requests.get(self.weatheraddr, {'city': adcode, 'extensions': 'all', 'key': self.key})
        try:
            forecast = json.loads(response.text)['forecasts']
            list = forecast[0]['casts']
            print(list, type(list))
            return list
        except:
            return []


if __name__ == '__main__':
    weather = Weather()
    # weather.getadcode()
    weather.getforecast('510100')
