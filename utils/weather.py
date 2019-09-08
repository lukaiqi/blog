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
        return adcode

    def getliveweather(self, adcode):
        response = requests.get(self.weatheraddr, {'city': adcode, 'extensions': 'base', 'key': self.key})
        lives = json.loads(response.text)['lives']
        return lives[0]

    def getforecastweather(self, adcode):
        response = requests.get(self.weatheraddr, {'city': adcode, 'extensions': 'all', 'key': self.key})
        forecast = json.loads(response.text)['forecasts']
        list = forecast[0]['casts']
        return list


if __name__ == '__main__':
    weather = Weather()
    # weather.getadcode()
    weather.getforecast('510100')
