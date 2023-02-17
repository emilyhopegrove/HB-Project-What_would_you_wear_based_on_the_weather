#pulled from ratings app server.py

"""Server for wtwbotw app."""
from apikey import api_key
from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, User
import crud
from jinja2 import StrictUndefined
import requests
from werkzeug.security import generate_password_hash, check_password_hash
import random



app = Flask(__name__)
#TODO if you deploy hide the secret_key below and keep it secret
app.secret_key = 'thisisacutestring'



################################################################
#AirBnB application v
@app.route('/homepage')
def homepage():
    "look at the homepage - display the outfit based on weather condition in home location, only visible when user is logged in"
    geocode_url = 'http://api.openweathermap.org/geo/1.0/zip'

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


#add a new endpoint that handles the AJAX request 
# and returns the weather data and corresponding outfit as a JSON object.
@app.route('/outfit/<location>', methods=["get"])
def workOutfit(location):
    """display the outfit based on weather condition in alternate locations, only visible when user is logged in"""
    zipcode = request.args.get("zipcode")

    geocode_url = 'http://api.openweathermap.org/geo/1.0/zip'

    if 'user_email' not in session:
        return redirect('/login')

    user = crud.get_user_by_email(session["user_email"])

    if location == 'zip_work':
        zipcode = user.zip_work
    elif location == 'zip_home':
        zipcode = user.zip_home
    elif location == 'zip_other':
        zipcode = user.zip_other

    geocode_params = {
        'zip': zipcode,
        'appid': api_key
    }

    result = crud.choose_outfit_by_weather(geocode_params, api_key, geocode_url)

    return jsonify(result)
#AirBnB application ^
################################################################




@app.route('/account', methods=['GET', 'POST'])
def account():
    if 'user_email' not in session:
        return redirect('/login')

   
    return render_template('account.html')

    


    

@app.route('/create-new-account')
def create_new_account():
    "User can input their information to create a new account"

    return render_template("create-new-account.html")
###################################################################

#create a route to register a new user 
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

    #print('work zip =', zip_work)
    zip_other = request.form.get('otherZips')
    if zip_other == '':
        zip_other = None
    
    # Continue with processing the form data
    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Please try again.")
    else:
        hash_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        user = crud.create_user(email, hash_password, user_name, zip_home, zip_work, zip_other)
        db.session.add(user)
        db.session.commit()
        flash("Account created!")

    return redirect("/homepage")


############################################################################
#login / logout
@app.route('/login')
def login():    

    return render_template("login.html", create_account_link="/create-new-account.html")


@app.route("/homepage", methods=["POST"])
# upon successful login credentials being inputted to login.html form, send user to homepage
#otherwise give user an error message and ask them to try again, refresh the page (redirect back to this page)
def handle_login():
    #access user's email and passwords from login form and store in variables
    email = request.form["email"]
    #access the user's email from database
    user = crud.get_user_by_email(email)

#if there's a user, grab the password to see if it matches, if not skip and redirect 
    if user:
        password = request.form["password"]
        if check_password_hash(user.password, password):
            session["user_email"] = user.email
            session["user_id"] = user.user_id
            flash(f"Welcome back, {user.user_name}!")
            return redirect('/homepage')
        else:
            flash(f"Incorrect password.")
            return redirect('/login')
    else:
        flash(f"Email address doesn't match any users.")
        return redirect('/login')



    


@app.route("/logout")
def logout():
    # clear session data
    session.clear()
    # Redirect the user back to the login page
    return redirect("/login")


###################################################################################
#garment adder form route
@app.route("/usersGarments", methods=['POST'])
def userGarments():
    garment_type = request.json.get('garment_type')
    garment_description = request.json.get('garment_description')
    temperature_rating = request.json.get('temperature_rating')
#creating a garment and adding to database
    garment = crud.create_garment(garment_type, garment_description, temperature_rating, session['user_id'])
    db.session.add(garment)
    db.session.commit()
#cute little return post card
    return jsonify({'message': 'Garment added!'})

#user account update form route
@app.route('/accountDetailsUpdater', methods=['POST'])
def accountDetails():
    email = request.json.get('email')
    user_name = request.json.get('username')
    password = request.json.get('password')
    homeZip = request.json.get('homeZip')
    workZip = request.json.get('workZip')
    otherZip = request.json.get('otherZip')
    #grab user who is logged in from the database 
    user = User.query.filter(session['user_email'] == User.email).first()

    #ACCOUNT FOR IF THE USER DOESN'T UPDATE ALL THE DETAILS
    if email != '':
        user.email = email
    if user_name != '':
        user.user_name = user_name
    if password != '':
        user.password = password
    if homeZip != '':
        user.homeZip = homeZip
    if workZip != '':
        user.workZip = workZip
    if otherZip != '':
        user.otherZip = otherZip

    #don't need to add just commit
    db.session.commit()

    return jsonify({'message': 'Account details updated!'})


if __name__ == "__main__":
    connect_to_db(app) 
    app.app_context().push()
    app.run(host="0.0.0.0", debug=True)