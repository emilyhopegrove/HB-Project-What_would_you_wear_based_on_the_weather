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

high_temp = weather_info['main']['temp_max']
low_temp = weather_info['main']['temp_min']

result = {
    "temperature": temperature,
    "precip": precip,
    "snow": snow,
    "high_temp": high_temp,
    "low_temp": low_temp
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
    "top": "T-shirt"
    "sweater": "Hoodie",
    "bottom": "Jeans",
    "footwear": "Tennis shoes",
}

coldWetOutfit = {
    "top": "Hoodie",
    "bottom": "Jeans",
    "footwear": "Tennis shoes",
    "Accessories": "Umbrella"
}
#warm outfits
warmOutfit = {
    "top": "T-Shirt",
    "bottom": "Jeans",
    "footwear": "Tennis shoes",
}

warmWetOutfit = {
    "top": "T-Shirt",
    "bottom": "Jeans",
    "footwear": "Tennis shoes",
    "Accessories": "Umbrella"
}

freezingOutfit = {
    "top": "T-Shirt",
    "sweater": "Hoodie",
    "outerwear": "Coat"
    "bottom": "Jeans",
    "footwear": "Boots",
    "Accessories": "Hat, glove and scarf"

}
#expected output for a warm and cold day 
#imaginaryGarments = {
    # "top": "T-Shirt",
    # "bottom": "Jeans",
    # "footwear": "Tennis shoes",
    # "sweater": "Hoodie"
# }
#

# psudocodalicious
#Input:

# 80+ = 'hot'
# 56-79 = "warm"
# 33-55 = "cold" (sweater = hoodie)
# 32 - = "freezing" (sweater= hoodie)(outerwear = coat)

    # create a set (cold, hot) (since the day may start cold then get warm, or vice versa) x
    # where does the high temp fall (pop into set) x ('pop' into set? doesn't pop() take things out?)
    # where does the low temp fall in a set (pop into set) x
    # set will have 1 or 2 items but never more, only accounting for high and low temps (NOT CERTAIN ABOUT THIS PART)

#check temp and figure out what word to ascribe to it 
#example: if temp is 60 degrees
    #if temp >= 80, 
    #put the word 'hot' into the set 
    #elif temp >= 56
    # put the word 'warm' into the set
    #elif temp >= 33
    #put the word 'cold' into the set
    #else
    #put the word 'freezing' into the set

   
#take the warmest rating in set and fill a garments dict (made a dictionary above for outfits)

#find the hottest word in set, check what the hottest word is, then add its clothing into the dictionary
#if there is one word in the set, do the below (handles the case when temps are in the same range, a consistent day)
#if tempWord = 'hot'
#add hotOutfit to garments
#elif tempWord = 'warm'
#add warmOutfit to garments
#elif tempWord = 'cold'
#add coldOutfit to garments
#elif tempWord = 'freezing'
#add freezingOutfit to garments

#element in set (syntax for word in set)
#if there is 2 words in the set
#if "hot" in temps_for_day:
    #put the  corresponding outfit pieces from the hotOutfit into garments object 
        #then take that word 'hot' and toss it out the window
#if 'warm' in temps_for_day:
    #put the corresponding outfit pieces from the warmOutfit into garments object 
        #then take that word 'warm' and toss it out the window
#if 'cold' in temps_for_day:
    #put the corresponding outfit pieces from the coldOutfit into garments object 
        #then take that word 'cold' and toss it out the window
#if 'freezing' in temps_for_day:
    #put the corresponding outfit pieces from the freezingOutfit into garments object 
        #then take that word 'freezing' and toss it out the window
    
#add missing keys into the garments object (such as if there's no sweater)
#save final word to a variable (ie 'second_temp')
#if second_temp is warm
    #the value of dictionary to check is the warmOutfit dicitonary
#if second_temp is cold
    #the value of dictionary to check is the coldOutfit dicitonary
#if second_temp is freezing
    #the value of dictionary to check is the freezingOutfit dicitonary

#iterate through the dictionary to check
    #if key not in garments dictionary, add that key/value pair to garments dictionary

#check for precipitation
#if precip = True
    #add key/value pair of accessory: umbrella to the garments dictionary

#end of all this pseudo, garments dictionary has the completed outfit for the day huzzah
#(note things will get nested, take it slow, write the if/else, use pass keyword, lots of levels of indentation )

#input: 
#output: garments dictionary with outfit items
temps_for_day = set()
garments = {}
#handle for if 2 words in set
if True:
    pass
else:
    pass
#handle for 1 word in set


        #if anything else in the set it will be a colder rating
            #check colder rating for outerwear and sweater (hoodie or coat) and add to garments list



    #check for precip if rain = yes add umbrella to garments list
    #take the garments list and display to user on homepage
    #wrap together and add into the results dictionary and send to the front end

#Output:
    #user will see a suggestion of what to wear including 
        #tops
        #bottoms
        #footwear
        #sweater
        #outerwear
        #umbrella 



