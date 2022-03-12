import json
from flask import Flask, request, render_template
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db, User, Pokemon, MyPokemon


''' Begin boilerplate code '''
def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) 
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
''' End Boilerplate Code '''

''' Set up JWT here '''
def authenticate(uname, password):
  #search for the specified user
  user = User.query.filter_by(username=uname).first()
  #if user is found and password matches
  if user and user.check_password(password):
    return user

#Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
  return User.query.get(payload['identity'])

jwt = JWT(app, authenticate, identity)
''' End JWT Setup '''

# edit to query 50 pokemon objects and send to template

@app.route('/')
def index():
  poke = Pokemon.query.all()
  return render_template('index.html', poke=poke) 

@app.route('/pokemon', methods=['GET'])
def pokemon():
  poke = Pokemon.query.all()
  pokemon_list = []
  for p in poke:
    pokemon_list.append(p.toDict())
  return json.dumps(pokemon_list)

@app.route('/signup', methods=['POST'])
def signup():
  userdata = request.get_json()

  olduser = User.query.filter_by(username=userdata['username']).first()

  if not olduser:
    olduser = User.query.filter_by(email=userdata['email']).first()

  if olduser:
    return "username or email already exists"

  else:
    newuser = User(username=userdata['username'], email=userdata['email'])
    newuser.set_password(userdata['password'])
    db.session.add(newuser)
    db.session.commit()
  return "user created"

@app.route('/mypokemon', methods=['POST'])
@jwt_required()
def getmypokemon():
  userdata = request.get_json()
  my_pokemon = MyPokemon(id=current_identity.id, pid=userdata['pid'], name = userdata['name'])

  try:
    db.session.add(my_pokemon)
    db.session.commit()

  except IntegrityError:
    db.session.rollback()
    return 'No Pokemon captured!'
  return my_pokemon.name + ' captured', 201


@app.route('/mypokemon', methods=['GET'])
@jwt_required()
def getlistmypokemon():
  pokemon_l = MyPokemon.query.filter_by(id=current_identity.id).all()
  pokemon_l = [pokemon_l.toDict() for poke in pokemon_l] # list comprehension which converts todo objects to dictionaries
  return json.dumps(pokemon_l)

@app.route('/mypokemon/<n>', methods=['GET'])
@jwt_required()
def getpokemon(n):
  getpokemon = MyPokemon.query.filter_by(id=current_identity.id, bid=n).first()
  if getpokemon == None:
    return 'No pokemon captured'
  return json.dumps(getpokemon.toDict())

@app.route('/mypokemon/<n>',methods=['PUT'])
@jwt_required()
def updatepokemon(n):
  pokemon = MyPokemon.query.filter_by(id=current_identity.id, bid=n).first()
  if pokemon == None:
    return 'no pokemon captured'
  data = request.get_json()
  if 'name' in data: # we can't assume what the user is updating wo we check for the field
    pokemon.name = data['name']
  db.session.add(pokemon)
  db.session.commit()
  return 'Updated', 201

  @app.route('/mypokemon/<n>',methods=['DELE'])
  @jwt_required()
  def deletepokemon(n):
    pokemon = Pokemon.query.filter_by(id=current_identity.id, bid=n).first()
    if pokemon == None:
      return 'No pokemon Captured'
    db.session.delete(pokemon) # delete the object
    db.session.commit()
    return 'Deleted', 204


@app.route('/app')
def client_app():
  return app.send_static_file('app.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)