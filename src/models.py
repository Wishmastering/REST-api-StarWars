from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }



# ABAJO TODA LA INFORMACION DE FAVORITES
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'),
     nullable=False)
   # characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)

def __repr__(self):
        return '<Favorites %r>' % self.id

def serialize(self):
        return { 
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
           # "characters_id": self.characters_id,
         
        }




# ABAJO TODA LA INFORMACION DE PLANETS 
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    favorites = db.relationship ('Favorites', backref='planets', lazy=True)

    #population = db.Column(String(250), nullable=False)
    #terrain = db.Column(String(250), nullable=False)
    

def __repr__(self):
        return '<Planets %r>' % self.id

def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "planet_id": self.planets_id,
           #"favorites": self.favorites,
           # "population": self.population,
           # "terrain": self.terrain,
           
            
        }




# ABAJO TODA LA INFORMACION DE CHARACTERS
# class Characters(db.Model):
#     __tablename__ = 'Characters'
#     # Here we define db.db.Columns for the table Characters
#     # Notice that each db.Column is also a normal Python instance attribute.
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), nullable=False)
#     gender = db.Column(db.String(250), nullable=False)
#     eye_color = db.Column(db.String(250), nullable=False)
#     hair_color = db.Column(db.String(250), nullable=False)
#     favorites = db.relationship ('Favorites', backref='characters', lazy=True)

# def __repr__(self):
#         return '<Characters %r>' % self.name

# def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
            
#             # PENDIENTE OTROS ARIBUTOS ACA
#         }


