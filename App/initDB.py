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
weight_kg = 1.0
height_m = 1.0
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


        weight_kg = line['weight_kg']
        if weight_kg == "":
            weight_kg = None

        height_m = line['height_m']
        if height_m =="":
            height_m = None
        
        type_2 = line['type2']
        if type_2 == "":
            type_2 = None

        pokemon_list.append(Pokemon(name = line['name'], attack = line['attack'], defense = line['defense'],
        hp = line['hp'], height = height_m, sp_attack = line['sp_attack'], sp_defense = line['sp_defense'],
        speed = line['speed'], type1 = line['type1'], type2 = type_2, weight = weight_kg
        ))

    
for pokemon in pokemon_list:
    db.session.add(pokemon)
db.session.commit()
    
# add code to parse csv, create and save pokemon objects

# replace any null values with None to avoid db errors
