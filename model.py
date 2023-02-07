"""Models for what to wear based on the weather app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#USER
#create a user class
class User(db.Model):
    """Some user Jane Smith"""
    #create the table, name it 'users' x
    #create the user id as the auto incrementing integer and primary key x
    #create the user name as a string, make it unique x
    #create the user email as a string, make it unique x
    #create the password as a string, make it unique x
    #make a dunder repr to return the user id and email x
    #make a PostgreSQL database (not certain of this)
    #test the User class out by running model.py in interactive mode

    __tablename__ = 'users'

    #make the columns, save to useful names
    user_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_name = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(100))
    #home zip required, other 2 optional
    zip_home = db.Column(db.Integer, nullable=False)
    zip_work = db.Column(db.Integer)
    zip_other = db.Column(db.Integer)
    

    """show information about the user"""
    def __repr__(self):
        return f"<User user_id = {self.user_id} email = {self.email}>"

################################################################
#GARMENTS
#create a garments class and give a __repr__ method
#include the following data:
"""
garment_id | integer x, autoincrementing x, primary key x, not null x, X
user_id |  integer x, autoincrement = True x, foreign key x, reference table = user x, reference field = user_id x, not null x, X
types | string, no char limit, not null X
style | string, no char limit, not null X
style description | text, no char limit, nullable X
temp rating | string, no char limit, not null X
^WANT TO MAKE TEMP RATING ONLY HOT, WARM OR COLD

"""
class Garment(db.Model):
    '''Garments with types (tops, bottoms, footwear and accessories) 
    and styles (t-shirt, hoodie, shorts, jeans, sandals, tennis shoes, hat, sunglasses, etc
    '''
    __tablename__ = 'garments'

#make the columns, save to useful names
    garment_id = db.Column(db.Integer,
                       autoincrement = True, 
                       primary_key = True,
                       nullable = False)

    user_id = db.Column(db.Integer, 
                    db.ForeignKey("users.user_id"),
                    nullable = False)

    types = db.Column(db.String(50),
                  nullable = False)

    style = db.Column(db.String(50),
                  nullable = False)

    style_description = db.Column(db.Text,
                              nullable = False)

    temp_rating = db.Column(db.String(50))

"""show information about the garments including its id number, type and style"""
def __repr__(self):
        return f"<Garment garment_id = {self.garment_id}, types = {self.types}, style = {self.style}>"



################################################################
#OUTFITS
#create an outfits class and give a __repr__ method

#include the following data:
"""
outfit_id | integer, autoincrementing, primary key, not null
user_id |  integer, autoincrementing, foreign key, not null, reference table = user, reference field = user_id
Temperature High of the day | integer, not null
Temperature Low of the day | integer, not null
Precipitation | Boolean, not null

"""

class Outfit(db.Model):
    '''Outfit pieces
    '''
    __tablename__ = 'outfits'

#make the columns, save to useful names
    outfit_id = db.Column(db.Integer,
                       autoincrement = True, 
                       primary_key = True,
                       nullable = False)
    user_id = db.Column(db.Integer, 
                    db.ForeignKey("users.user_id"),
                    nullable = False)

    temp_high = db.Column(db.Integer,
                  nullable = False)

    temp_low = db.Column(db.Integer,
                  nullable = False)

    precipitation = db.Column(db.Boolean, nullable = False)

"""show information about the outfits including its id number, and temp"""
def __repr__(self):
        return f"<Outfit outfit_id = {self.outfit_id}, temp_high = {self.temp_high}, temp_low = {self.temp_low}>"





################################################################
#BRIDGE TABLE

#create a garment list for outfits class (the bridge) and give a __repr__ method

#include the following data:

"""
garment_id | integer, not null, Foreign Key, reference table = Garments, reference field = Garment_id

outfit_id | integer, not null, Foreign Key, reference table = Outfits, reference field = Outfit_id x
"""


class garmentListForOutfits(db.Model):

    __tablename__= 'garmentListForOutfits'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #make the columns, save to useful names
    garment_id = db.Column(db.Integer,
                       db.ForeignKey('garments.garment_id'),
                       nullable = False)


    outfit_id = db.Column(db.Integer,
                       db.ForeignKey('outfits.outfit_id'),
                       nullable = False)

#



################################################################

#define the connect_to_db function x

def connect_to_db(flask_app, db_uri='postgresql:///whatToWear', echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.app = flask_app
    db.init_app(flask_app)

    print("IT'S WORKING, IT'S WORKING!!! (spoken in the voice of Anakin Skywalker as he gets his podracer to run)")



################################################################

#pulled from ratings lab bottom of model.py
if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False)
    app.app_context().push()
    db.create_all()