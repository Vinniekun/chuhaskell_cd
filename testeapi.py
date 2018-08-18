import json
import requests

def get_location_weather():
    api_key = "6227b12aaca6549ff612b4364641f039"
    params = {
        'lat': -29.6890913,
        'lon': -53.8034015,
        'appid': api_key,
        'units': 'metric',
    }
    url = "http://api.openweathermap.org/data/2.5/forecast"
    resp = requests.post(url=url, params=params)
    data = resp.json()
    print(resp.text)

get_location_weather()