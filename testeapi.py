import json
import requests

def get_location_weather():
    api_key = "6227b12aaca6549ff612b4364641f039"
    params = {
        'zip': '97000-000,br',
        'appid': api_key,
        'units': 'metric'   
    }
    url = "http://api.openweathermap.org/data/2.5/weather"
    resp = requests.post(url=url, params=params)
    data = resp.json()
    #print(data)

get_location_weather()