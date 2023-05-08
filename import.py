import sqlite3
import sys
from pymongo import MongoClient

connection = sqlite3.connect("/Users/janiskim/INFO330-ExploringDocDBs/pokemon.sqlite")
crsr = connection.cursor()

client_mongo = MongoClient("mongodb://localhost/pokemon")
pokemonDB = client_mongo['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

for i in range(1, 802):
    rowPK = crsr.execute("SELECT * FROM pokemon WHERE id = " + str(i)).fetchone()
    Type1PK = crsr.execute("SELECT * FROM type AS T LEFT OUTER JOIN pokemon_type AS PT ON T.id = PT.type_id WHERE pokemon_id = " 
                               + str(i) + " AND which = 1").fetchone()
    Type2PK = crsr.execute("SELECT * FROM type AS T LEFT OUTER JOIN pokemon_type AS PT ON T.id = PT.type_id WHERE pokemon_id = " 
                               + str(i) + " AND which = 2").fetchone()
    AbilitiesPK = crsr.execute("SELECT * FROM ability AS A LEFT OUTER JOIN pokemon_abilities AS PA ON A.id = PA.ability_id WHERE pokemon_id = " 
                                    + str(i)).fetchmany(6)
    new_ability = []

    for j in range(len(AbilitiesPK)):
        new_ability.append(AbilitiesPK[j][1])
    
    pokemon = {
       "name": rowPK[2],
       "pokedex_number": rowPK[1],
       "types": [Type1PK[1], Type2PK[1]],
       "hp": rowPK[5],
       "attack": rowPK[6],
       "defense": rowPK[7],
       "speed": rowPK[8],
       "sp_attack": rowPK[9],
       "sp_defense": rowPK[10],
       "abilities": new_ability
    }

    x = pokemonColl.insert_one(pokemon)
    print(x)
