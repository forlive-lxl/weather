import requests
import json
from settings import APPID

# 查询城市的经纬度
def get_lat_lon(city, limit=5):
    url = 'http://api.openweathermap.org/geo/1.0/direct'
    params = {'q': city, 'limit': limit, 'appid': APPID}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()[0]
        lat = data['lat']
        lon = data['lon']
        return lat, lon
    else:
        print('请求失败:', response.status_code)


# 查询城市的天气
def get_weather(lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'lat': lat, 'lon': lon, 'appid': APPID}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('请求失败:', response.status_code)