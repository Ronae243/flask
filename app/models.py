from . import db



class HouseProperties(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    num_of_rooms = db.Column(db.Integer())
    num_of_bathrooms = db.Column(db.Integer())
    price = db.Column(db.Integer())
    property_type = db.Column(db.String(30))
    location = db.Column(db.String(30))
    property_photo =db.Column(db.String())
    description = db.Column(db.String(300))

    def __init__(self, title, description, num_of_rooms,  num_of_bathrooms, price, property_type, location, property_photo):
        self.title = title
        self.num_of_rooms = num_of_rooms 
        self.num_of_bathrooms = num_of_bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location 
        self.property_photo = property_photo
        self.description = description
    

    def __repr__(self):
        return f'<User:{self.location}>'
