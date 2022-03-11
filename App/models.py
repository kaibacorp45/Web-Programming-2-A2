from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class MyPokemon(db.Model):
  bid = db.Column('bid', db.Integer, primary_key=True)
  id = db.Column('id', db.Integer, db.ForeignKey('user.id'))
  pid = db.Column('pid', db.Integer, db.ForeignKey('pokemon.pid'))
  name = db.Column(db.String(50), nullable = True)
  pokemon = db.relationship('Pokemon')

  def toDict(self):
    return{
      'name':self.name,
      'stats':self.pokemon.toDict()
    }

## my note_ user models
class User(db.Model):
  id = db.Column('id', db.Integer, primary_key=True)
  username = db.Column(db.String(50), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)

  def set_password(self, password):
    """Create hashed password."""
    self.password = generate_password_hash(password, method='sha256')

  def check_password(self, password):
    """Check hashed password."""
    return check_password_hash(self.password, password)
  
  def toDict(self):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email,
      "password": self.password
     }


class Pokemon(db.Model):
  pid = db.Column('pid', db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=True)
  attack = db.Column('attack', db.Integer, nullable=True)
  defense = db.Column('defense', db.Integer, nullable=True)
  hp = db.Column('hp', db.Integer, nullable=True)
  height_m = db.Column('height_m', db.Float, nullable = True)
  sp_attack = db.Column('sp_attack', db.Integer, nullable=True)
  sp_defense = db.Column('sp_defense', db.Integer, nullable=True)
  speed = db.Column('speed', db.Integer, nullable=True)
  type1 = db.Column(db.String(50), nullable=True)
  type2 = db.Column(db.String(50), nullable=True)
  weight_kg = db.Column('weight_kg', db.Float, nullable = True)

  def toDict(self):
    return {
      "pid": self.pid,
      "name": self.name,
      "attack": self.attack,
      "defense": self.defense,
      "hp": self.hp,
      "height_m": self.height_m,
      "sp_attack": self.sp_attack,
      "sp_defense": self.sp_defense,
      "speed": self.speed,
      "type1": self.type1,
      "type2": self.type2,
      "weight_kg": self.weight_kg
    }








  




## Create a User Model
## must have set_password, check_password and to Dict

## Create a Pokemon Model