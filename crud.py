"""CRUD OPERATIONS"""

from model import db, User, Garment, Outfit, connect_to_db 
import requests

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

# outfit images
cold_outfit_img = "/static/images/outfit-cold_what-to-wear_hamza-nouasria-unsplash.jpeg"
freezing_outfit_img = "/static/images/outfit-freezing_what-to-wear_raphael-nast-unsplash.jpeg"
warm_outfit_img = "/static/images/outfit-warm_what-to-wear_laura-chouette-unsplash.jpeg"
hot_outfit_img = "/static/images/outfit-hot_what-to-wear_ana-itonishvili-unsplash.jpeg"

# TODO  these images need to be put somewhere?
# <img class="outfit-img" src="{{ cold_outfit_img }}" alt="Cold Outfit">
# <img class="outfit-img" src="{{ freezing_outfit_img }}" alt="Freezing Outfit">
# <img class="outfit-img" src="{{ warm_outfit_img }}" alt="Warm Outfit">
# <img class="outfit-img" src="{{ freezing_outfit_img }}" alt="Freezing Outfit">



#weather icon images
rain_icon = "/static/images/icon-hot-warm-rain.png"
hot_warm_icon = "/static/images/icon-hot-warm-day.png"
freezing_snow_icon = "/static/images/icon-freezing-snow.png"
#loading icon image
loading_icon = "/static/images/wait-1.1s-200px.svg"

def create_user(email, password, user_name, zip_home, zip_work, zip_other):
    """Create and return a new user"""

    user = User(
        email=email, 
        password=password, 
        user_name=user_name,
        zip_home=zip_home,
        zip_work=zip_work,
        zip_other=zip_other
        )

    return user




def create_garment(types, style_description, temp_rating, user_id):
    """"create and return garments"""

    garment = Garment(
        types=types, 
        style_description=style_description, 
        temp_rating=temp_rating,
        user_id=user_id,
        )

    return garment



def create_outfit():
    """create and return outfits
    since an outfit will be created using garments, not sure how this works
    """
    #TODO finish this crud

    outfit = Outfit(

    )

def get_user_by_email(email):
    """get the user by their email
    getting user from database using their email
    """

    user = User.query.filter(email == User.email).first()
    return user

def get_user_by_username(username):
    """get the user by their username
    getting user from database using their username
    """

    user = User.query.filter(username == User.username).first()
    return user


def choose_outfit_by_weather(geocode_params, api_key, geocode_url):

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
        pass
        #eventually need error page
        # TODO return redirect("/account")
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
        #if low temp is __ add this image, if low temp is ___ add that image, add image url to results
        
        

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
#         Dictionary that contains high_temp, low_temp, and precip conditions pulled from API
        
#     Returns: dict
#         A dictionary that contains current local weather conditions, 
#         and recommended outfit to be displayed to the user
#   
#this will eventually get tucked into a function and/or put into crud and called here for tidiness sake
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
            
    if 'freezing' in temps_for_day:
        outfit_image = freezing_outfit_img
        icon = freezing_snow_icon
    elif 'cold' in temps_for_day:
        outfit_image = cold_outfit_img
        icon = freezing_snow_icon
    elif 'warm' in temps_for_day:
        outfit_image = warm_outfit_img
        icon = hot_warm_icon
    else:
        outfit_image = hot_outfit_img
        icon = hot_warm_icon

   
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

    # for key in outfit_to_check:
    #     if key not in garments:
    #         garments[key] = outfit_to_check[key]

    #combine results with garments, icons and outfits 
    result['garments'] = garments
    result['icon'] = icon
    result['outfit_image'] = outfit_image
    return result





if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    app.app_context().push