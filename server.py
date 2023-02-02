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
    return render_template("homepage.html")

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