#pulled from ratings app server.py

"""Server for wtwbotw app."""
import os
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import requests

app = Flask(__name__)

# outfits dictionary
#hot outfits
hotOutfit = {
    "top": "T-Shirt",
    "bottom": "Shorts",
    "footwear": "Sandals",
}

hotWetOutfit = {
    "top": "T-Shirt",
    "bottom": "Shorts",
    "footwear": "Sandals",
    "Accessories": "Umbrella"
}
#cold outfits
coldOutfit = {
    "top": "T-shirt",
    "sweater": "Hoodie",
    "bottom": "Jeans",
    "footwear": "Tennis shoes"
}

coldWetOutfit = {
    "top": "T-Shirt",
    "sweater": "Hoodie",
    "bottom": "Jeans",
    "footwear": "Tennis shoes",
    "Accessories": "Umbrella"
}
#warm outfits
warmOutfit = {"top": "T-Shirt", "bottom": "Jeans", "footwear": "Tennis shoes"}

warmWetOutfit = {
    "top": "T-Shirt",
    "bottom": "Jeans",
    "footwear": "Tennis shoes",
    "Accessories": "Umbrella"
}

freezingOutfit = {
    "top": "T-Shirt",
    "sweater": "Hoodie",
    "outerwear": "Coat",
    "bottom": "Jeans",
    "footwear": "Boots",
    "Accessories": "Hat, gloves and a scarf!"
}

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
    
#Recommended Outfit
#     This function takes a dictionary as input, which contains high_temp, low_temp, and precip,
#     and returns a dictionary which combines the result dictionary with the recommended outfit.
    
#     result: dict
#         Dictionary that contains high_temp, low_temp, and precip
        
#     Returns: dict
#         A dictionary that contains high_temp, low_temp, precip, and recommended outfit
#   


    temps_for_day = set()
    temps = [result["high_temp"], result["low_temp"]]

    for temp in temps:
        if temp >= 80:
            temps_for_day.add('hot')
        elif temp >= 56:
            temps_for_day.add('warm')
        elif temp >= 33:
            temps_for_day.add('cold')
        else:
            temps_for_day.add('freezing')

    garments = {}

    if len(temps_for_day) == 1:
        temp_word = list(temps_for_day)[0]
        if temp_word == 'hot' and result["precip"] == True:
            garments.update(hotWetOutfit)
        elif temp_word == 'hot':
            garments.update(hotOutfit)
        elif temp_word == 'warm' and result["precip"] == True:
            garments.update(warmWetOutfit)
        elif temp_word == 'warm':
            garments.update(warmOutfit)
        elif temp_word == 'cold' and result["precip"] == True:
            garments.update(coldWetOutfit)
        elif temp_word == 'cold':
            garments.update(coldOutfit)
        elif temp_word == 'freezing':
            garments.update(freezingOutfit)

        else:
    
            if 'hot' in temps_for_day and result["precip"] == True:
                garments.update(hotWetOutfit)
            elif 'hot' in temps_for_day:
                garments.update(hotOutfit)
                temps_for_day.remove('hot')

            elif 'warm' in temps_for_day and result["precip"] == True:
                garments.update(warmWetOutfit)
            elif 'warm' in temps_for_day:
                garments.update(warmOutfit)
                temps_for_day.remove('warm')

            elif 'cold' in temps_for_day and result["precip"] == True:
                garments.update(coldWetOutfit)
            elif 'cold' in temps_for_day:
                garments.update(coldOutfit)
                temps_for_day.remove('cold')
            elif 'freezing' in temps_for_day:
                garments.update(freezingOutfit)
                temps_for_day.remove('freezing')

    second_temp = list(temps_for_day)[0]

    if second_temp == 'warm':
        outfit_to_check = warmOutfit
    elif second_temp == 'cold':
        outfit_to_check = coldOutfit
    elif second_temp == 'freezing':
        outfit_to_check = freezingOutfit

    for key in outfit_to_check:
        if key not in garments:
            garments[key] = outfit_to_check[key]

    #combine results with garments 
    for garment in garments:
        result[garment] = garments[garment]

    print(result)


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