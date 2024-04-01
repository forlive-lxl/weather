from .open_api import get_lat_lon, get_weather

def get_weather_by_city(city):
    lat, lon = get_lat_lon(city)
    data = get_weather(lat, lon)
    return data