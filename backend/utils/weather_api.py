from .open_api import get_lat_lon, get_weather

def get_weather_by_city(city):
    lat, lon = get_lat_lon(city)
    data = get_weather(lat, lon)
    data['main']['temp'] = round((data['main']['temp'] -273.15), 1)
    data['main']['temp_max'] = round((data['main']['temp_max'] -273.15), 1)
    data['main']['temp_min'] = round((data['main']['temp_min'] -273.15), 1)
    data['main']['feels_like'] = round((data['main']['feels_like'] -273.15), 1)
    return data