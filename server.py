#pulled from ratings app server.py

"""Server for wtwbotw app."""
import os
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import requests

app = Flask(__name__)



@app.route('/homepage')
def homepage():
    "look at the homepage - display the outfit based on weather condition"
    geocode_url = 'http://api.openweathermap.org/geo/1.0/zip'
    #make the api key super duper safe
    api_key = os.environ['api_key']

    geocode_params = {
    'zip': 78703,
    'appid': api_key
    }

    response = requests.get(geocode_url, params=geocode_params)

    data = response.json()
    lat = data['lat']
    lon = data['lon']

    weather_url = 'https://api.openweathermap.org/data/2.5/weather'

    weather_params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': "imperial"

    }

    weather_response = requests.get(weather_url, params=weather_params)

    weather_info = weather_response.json()

    if(weather_info['cod'] == '404'):
        #eventually need error page
        redirect("\account")
    else:
        #print(weather_info)
        temperature = weather_info["main"]['temp']
        print("temperature", temperature)


        if 'Rain' in weather_info["main"]:
            precip = True
        else:
            precip = False

        snow = False
        for weather_type in weather_info['weather']:
            if weather_type['main'] == 'Snow':
                snow = True
        high_temp = weather_info['main']['temp_max']
        low_temp = weather_info['main']['temp_min']
        
        result = {
            "temperature": temperature,
            "precip": precip,
            "snow": snow,
            "high_temp": high_temp,
            "low_temp": low_temp
        }
    
    return render_template("homepage.html", result=result)

@app.route('/account')
def account():
    "look at the user's account page - user puts in their information"

    return render_template("account.html")

@app.route('/create-new-account')
def create_new_account():
    "look at the create new account page"

    return render_template("create-new-account.html")


# post method zip code form submission, user inputs zip, click submit, hit end point, endpoint grabs zipcode entered
# (look up examples)
#enter zip into api call, return data from api
#figure out what information I want to extract, set new variables to represent the temp and precip





if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)