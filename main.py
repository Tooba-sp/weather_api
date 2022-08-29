import datetime as dt
import requests
import json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "2b5ac46da58a8e528c94e1ed553b1375"
CITY_LIST = ["Chicago", "San Diego", "Manhattan"]
'''
weather = {
    'cities':
        {
            'Chicago': {
                'temp': temp
                'humidity': humidity
                'over_cast' : over_cast
            },
            'San Diego'{
                'temp': temp,
                'humidity': humidity,
                'over_cast': over_cast
        },
            'Manhattan'{
                'temp': temp
                'humidity': humidity,
                'over_cast': over_cast,
            }
        }
}
'''

city_dict = {}
city_list = []
for CITY in CITY_LIST:

    url = f"{BASE_URL}appid={API_KEY}&q={CITY}"

    response = requests.get(url).json()

#convert json to dict
    response_dict = dict(response)



    temp = response_dict['main']['temp']
    humidity = response_dict['main']['humidity']
    over_cast = response_dict['weather'][0]['main']

    payload = {
        'city': CITY,
        'temp': temp,
        'humidity': humidity,
        'over_cast': over_cast

    }

    city_list.append(payload)

    city_dict[CITY] = payload


weather ={
    'cities' : city_dict
}


