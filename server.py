#pulled from ratings app server.py

"""Server for wtwbotw app."""
import os
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
import requests


app = Flask(__name__)
#TODO if you deploy hide the secret_key below and keep it secret
app.secret_key = 'thisisacutestring'



################################################################

@app.route('/homepage')
def homepage():
    "look at the homepage - display the outfit based on weather condition, only visible when user is logged in"
    geocode_url = 'http://api.openweathermap.org/geo/1.0/zip'
    #make the api key super duper safe
    api_key = os.environ['api_key']

    if 'user_email' not in session:
        return redirect('/login')

    # make a call to the database then set the variable
    user = crud.get_user_by_email(session["user_email"])

    geocode_params = {
    'zip': user.zip_home,
    'appid': api_key
    }
    
    result = crud.choose_outfit_by_weather(geocode_params, api_key, geocode_url)
    return render_template("homepage.html", result=result, user=user)
#homepage ^
################################################################

@app.route('/account')
def account():
    "look at the user's account page - user puts in their information"

    return render_template("homepage.html")

@app.route('/create-new-account')
def create_new_account():
    "look at the create new account page"

    return render_template("create-new-account.html")
###################################################################

#create a route to register a new user (used ratings-lab solution as a starting poin)
@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    # Check if the request method is POST
    try:
        email = request.form['email']
        password = request.form['password']
        zip_home = int(request.form['homeZip'])
    except KeyError:
        # Return an error message to the user if they don't provide required information
        #need to redirect back to form 
        return "Error: Required information is missing in the form!"

    # Get the other fields, which are not required
    user_name = request.form.get('username', 'No optional username provided')
    zip_work = request.form.get('workZip')
    if zip_work == '':
        zip_work = None

    print('work zip =', zip_work)
    zip_other = request.form.get('otherZips')
    if zip_other == '':
        zip_other = None
    
    # Continue with processing the form data
    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Please try again.")
    else:
        user = crud.create_user(email, password, user_name, zip_home, zip_work, zip_other)
        db.session.add(user)
        db.session.commit()
        flash("Account created! It's time to log in.")

    return redirect("/homepage")




############################################################################
#login / logout
@app.route('/login')
def login():    

    return render_template("login.html")


@app.route("/homepage", methods=["POST"])
# upon successful login credentials being inputted to login.html form, send user to homepage
#otherwise give user an error message and ask them to try again, refresh the page (redirect back to this page)
def handle_login():
    #access user's email and passwords from login form and store in variables
    email = request.form["email"]
    password = request.form["password"]
    #access the user's email from database
    user = crud.get_user_by_email(email)
    #if the username/passwords inputted don't match the record, ask user to try again
    if not user or user.password != password:
        flash("The email or password you entered was incorrect. Please try again.")
        return redirect('/login')
    else:
        # Log in user by storing the user's email in session, redirect to homepage
        session["user_email"] = user.email
        flash(f"Welcome back, {user.user_name}!")

    return redirect('/homepage')


@app.route("/logout")
def logout():
    # clear session data
    session.clear()
    # Redirect the user back to the login page
    return redirect("/login")


###################################################################################
#creating a reusable user name variable to pull over to home page to greet the user

# @app.route('/homepage')
# def index():
#     user = {'email': 'user@example.com'}
#     return render_template('homepage.html', user=user)


if __name__ == "__main__":
    connect_to_db(app)
    app.app_context().push()
    app.run(host="0.0.0.0", debug=True)