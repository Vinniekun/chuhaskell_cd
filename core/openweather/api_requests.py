import requests, json

API_KEY = "6227b12aaca6549ff612b4364641f039"

def get_5days_forecast(lat, lon):
    params = {
        'appid': API_KEY,
        'units': 'metric',
        'lat': float(lat),
        'lon': float(lon)
    }
    url = "http://api.openweathermap.org/data/2.5/forecast"
    resp = requests.post(url=url, params=params)
    return resp.json()

def get_icon_name(id):
    icon_names = [['cloudy',801], ['clear-day',800], ['fog',700], ['snow',600], ['rain',0]]
    for icon, id_ in icon_names:
        if id >= id_:
            return icon

def get_day_forecast(lat,lon):
    params = {
        'appid': API_KEY,
        'units': 'metric',
        'lat': float(lat),
        'lon': float(lon)
    }
    url = "http://api.openweathermap.org/data/2.5/weather"
    resp = requests.post(url=url, params=params)
    return resp.json()