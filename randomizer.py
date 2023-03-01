"""CRUD OPERATIONS"""

from model import db, User, Garment, Outfit, connect_to_db 
import requests
import random


# Default outfits dictionary
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

    user = User.query.filter(username == User.user_name).first()
    return user



def get_weather(geocode_params, api_key, geocode_url):
    #part one: gather weather info
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
        temperature = weather_info["main"]['temp']

        if 'Rain' in weather_info["main"]:
            precip = True
        else:
            precip = False

        snow = False
        for weather_type in weather_info['weather']:
            if weather_type['main'] == 'Snow':
                snow = True
      
        
        

        if temperature >= 80:
            temp_word = 'hot'
        elif temperature >= 56:
            temp_word = 'warm'
        elif temperature >= 33:
            temp_word = 'cold'
        else:
            temp_word = 'freezing'

    return temp_word

def choose_outfit_by_weather(temp_word):
    """create the outfits for display by gathering the user's oufits saved in the database 
    then return them based on the user's local weather"""

    tops = Garment.query.filter(Garment.types == 'tops', Garment.temp_rating == temp_rating).all()
    bottoms = Garment.query.filter(Garment.types == 'bottoms', Garment.temp_rating == temp_rating).all()
    footwear = Garment.query.filter(Garment.types == 'footwear', Garment.temp_rating == temp_rating).all()
    accessories = Garment.query.filter(Garment.types == 'accessories', Garment.temp_rating == temp_rating).all()

    if len(tops) < 2 or len(bottoms) < 2 or len(footwear) < 2 or len(accessories) < 2:
        # Use default outfit if there aren't enough items
        tops = Garment.query.filter(Garment.types == 'tops', Garment.default == True).all()
        bottoms = Garment.query.filter(Garment.types == 'bottoms', Garment.default == True).all()
        footwear = Garment.query.filter(Garment.types == 'footwear', Garment.default == True).all()
        accessories = Garment.query.filter(Garment.types == 'accessories', Garment.default == True).all()

    random_tops = random.choice(tops)
    random_bottoms = random.choice(bottoms)
    random_footwear = random.choice(footwear)
    random_accessories = random.choice(accessories)

    outfit = [[random_tops] + [random_bottoms] + [random_footwear] + [random_accessories]]

    return outfit





if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    app.app_context().push

        