import requests
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Москва
# "latitude": 55.755864,
# "longitude": 37.617698,


def get_data_openmeteo(latitude, longitude):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["wind_speed_10m", "wind_direction_10m", "wind_gusts_10m", "wind_speed_180m", "wind_direction_180m"],
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()

    current_wind_speed_10m = current.Variables(0).Value()
    current_wind_direction_10m = current.Variables(1).Value()
    current_wind_gusts_10m = current.Variables(2).Value()
    current_wind_speed_180m = current.Variables(3).Value()
    current_wind_direction_180m = current.Variables(4).Value()

    print(f"Current time {current.Time()}")
    print(f"Current wind_speed_10m {current_wind_speed_10m}")
    print(f"Current wind_direction_10m {current_wind_direction_10m}")
    print(f"Current wind_gusts_10m {current_wind_gusts_10m}")
    print(f"Current wind_speed_180m {current_wind_speed_180m}")
    print(f"Current wind_direction_180m {current_wind_direction_180m}")
    answer = {"coord": (response.Latitude(), response.Longitude()), 'wind_speed_10m': current_wind_speed_10m,
              'wind_direction_10m': current_wind_direction_10m, 'wind_gusts_10m': current_wind_gusts_10m,
              'wind_speed_180m': current_wind_speed_180m, 'wind_direction_180m': current_wind_direction_180m}
    return answer




def get_data(coord):
    # http://api.weatherapi.com/v1/current.json?key=b342a3e3f912444ea7d141356241402&q=London&aqi=yes

    host = "http://api.weatherapi.com/v1/current.json"
    key = "b342a3e3f912444ea7d141356241402"

    data = {
        "key": key,
        "q": coord,
        'lang': 'ru'
    }

    responce = requests.post(host, data=data)
    responce = responce.json()
    answer = {"coord": coord, 'wind': responce['current']['wind_kph'], 'wind_degree': responce['current']['wind_degree'], 'gust': responce['current']['gust_kph']}
    print(answer)
    return answer
#
# get_data("55.91285146621604,37.82274786258563")