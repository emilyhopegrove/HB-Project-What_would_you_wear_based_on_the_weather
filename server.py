#pulled from ratings app server.py
"""Server for wtwbotw app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)



@app.route('/homepage')
def homepage():
    "look at the homepage"

    return render_template("homepage.html")

@app.route('/account')
def account():
    "look at the user's account page"

    return render_template("account.html")

@app.route('/create-new-account')
def create_new_account():
    "look at the create new account page"

    return render_template("create-new-account.html")






if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)