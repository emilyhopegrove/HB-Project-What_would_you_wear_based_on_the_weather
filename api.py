# practice
import requests
import os
# user_home_zip = input("Enter your home zip: ")
# user_work_zip = input("Enter your work zip: ")
# user_other_zip = input("Enter another favorite zip: ")

geocode_url = 'http://api.openweathermap.org/geo/1.0/zip'

api_key = os.environ['api_key']

geocode_params = {
    'zip': 78703,
    'appid': api_key
}


#geocode api call
response = requests.get(geocode_url, params=geocode_params)

data = response.json()
lat = data['lat']
lon = data['lon']

# print(lat,lon)

#weather api call

weather_url = 'https://api.openweathermap.org/data/2.5/weather'

weather_params = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
    'units': "imperial"

}

weather_response = requests.get(weather_url, params=weather_params)

weather_info = weather_response.json()
# print(weather_info)
#handle for 404 errors
if(weather_info['cod'] == '404'):
    print("sorry the api is down")
else:
    #print(weather_info)
    temperature = weather_info["main"]['temp']
    print("temperature", temperature)
#do we need the umbrella?
    if 'Rain' in weather_info["main"]:
        precip = True
    else:
        precip = False

#do we need a coat?
    snow = False
    for weather_type in weather_info['weather']:
        if weather_type['main'] == 'Snow':
            snow = True

#make a dictionary we can send to the front end     
result = {
    "temperature": temperature,
    "precip": precip,
    "snow": snow
}


#save useful stuff to variables and test

# temperature = weather_info["main"]['temp']
# precip = weather_info['main']['Rain']
# snow = weather_info['current']['weather']['snow']
# description = ["current"]["weather"]["description"]
# icon = ["current"]["weather"]["icon"]

# print("the weather is:", temperature)

# print(temperature, precip)


#demo response
# {'coord': {'lon': -97.7648, 'lat': 30.2907},
# 'weather': [
#             {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}, 
#             {'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}
#            ],
# 'base': 'stations',
# 'main': {'temp': 31.96, 'feels_like': 23.5, 'temp_min': 30.15, 'temp_max': 33.53, 'pressure': 1024, 'humidity': 94}, 
# 'visibility': 8047, 
# 'wind': {'speed': 10.36, 'deg': 350}, 
# 'snow': {'1h': 0.51}, 
# 'clouds': {'all': 100}, 
# 'dt': 1675296384, 
# 'sys': {'type': 2, 'id': 2073627, 'country': 'US', 'sunrise': 1675257715, 'sunset': 1675296433},
# 'timezone': -21600, 
# 'id': 4671654, 
# 'name': 'Austin', 
# 'cod': 200}