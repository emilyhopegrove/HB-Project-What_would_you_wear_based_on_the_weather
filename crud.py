"""CRUD OPERATIONS"""

from model import db, User, Garment, Outfit, connect_to_db


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




def create_garment(types, style, style_description, temp_rating):
    """"create and return garments"""

    garment = Garment(
        types=types, 
        style=style, 
        style_description=style_description, 
        temp_rating=temp_rating,
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




if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    app.app_context().push()

        