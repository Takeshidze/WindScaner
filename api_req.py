import requests

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