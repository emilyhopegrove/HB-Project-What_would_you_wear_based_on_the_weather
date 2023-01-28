"""CRUD OPERATIONS"""

from model import db, User, Garment, Outfit


def creat_user(email, password, user_name, user_id):
    """Create and return a new user"""

    user = User(
        email=email, 
        password=password, 
        user_name=user_name, 
        user_id=user_id,
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

    outfit = Outfit(

    )





if __name__ == "__main__":
    from server import app

    connect_to_db(app)