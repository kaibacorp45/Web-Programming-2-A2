from main import db, app, Pokemon
import csv

db.create_all(app=app)

pokemon_list = []
p_name = ""
atk = 0
defen = 0
hp_health = 0
spatk = 0
spdef = 0
p_speed = 0
weight = 1.0
height = 1.0
type_1 = ""
type_2 = ""
with open('/workspace/info2602a2/App/pokemon.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:

        p_name = line['name']
        if p_name == "":
            p_name = None

        atk = line['attack']
        if atk =="":
            atk = None
        
        defen = line['defense']
        if defen == "":
            defen = None

        hp_health = line['hp']
        if hp_health == "":
            hp_health = None

        spatk = line['sp_attack']
        if spatk =="":
            spatk = None
        
        spdef = line['sp_defense']
        if spdef == "":
            spdef = None

        p_speed = line['speed']
        if p_speed == "":
            p_speed = None

        type_1 = line['type1']
        if type_1 =="":
            type_1 = None
        
        defen = line['defense']
        if defen == "":
            defen = None


        weight = line['weight_kg']
        if weight == "":
            weight = None

        height = line['height_m']
        if height =="":
            height = None
        
        type_2 = line['type2']
        if type_2 == "":
            type_2 = None

        pokemon_list.append(Pokemon(name = p_name, attack = atk, defense = defen,
        hp = hp_health, height_m = height, sp_attack = spatk, sp_defense = spdef,
        speed = p_speed, type1 = type_1, type2 = type_2, weight_kg = weight
        ))

    
for pokemon in pokemon_list:
        #print(obj.type2)
    db.session.add(pokemon)
    #print(obj.attack, obj.defense, obj.height_m, obj.hp, obj.name, obj.sp_attack, obj.sp_defense, obj.speed, obj.type1, obj.type2, obj.weight_kg)
    #print(obj.toDict())
db.session.commit

  
poke = Pokemon.query.all()
for w in poke:
    print(w.weight_kg)
    

# add code to parse csv, create and save pokemon objects

# replace any null values with None to avoid db errors
