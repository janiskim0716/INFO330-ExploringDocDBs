import sqlite3
import sys
import pymongo
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon with an ability of "Overgrow" 
print("Return all Pokemon with an ability of Overgrow")
pokemon_overgrow = pokemonColl.find({"abilities": {"$regex": "Overgrow"}})
for pokemon in pokemon_overgrow:
    print(pokemon)