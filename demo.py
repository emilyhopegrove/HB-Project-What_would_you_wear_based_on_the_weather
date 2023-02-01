# practice
import requests

# user_home_zip = input("Enter your home zip: ")
# user_work_zip = input("Enter your work zip: ")
# user_other_zip = input("Enter another favorite zip: ")

geocode_url = 'http://api.openweathermap.org/geo/1.0/zip'

api_key = '437ebc27db78460bc96c720884188dbb'

geocode_params = {
    'zip': 78703,
    'appid': api_key
}


#call the api for geocode
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
    'appid': api_key
}

weather_response = requests.get(weather_url, params=weather_params)

weather_info = weather_response.json()


temperature = weather_info["main"]['temp']
precip = weather_info['main']['precip']
print("precipitation", weather_info['main']['temp'])

# print(temperature, precip)