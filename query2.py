import sqlite3
import sys
import pymongo
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon with an attack greater than 150.
print("Pokemon with an attack greater than 150 are:")
attack_150 = pokemonColl.find({"attack": {"$gt":150}})
for i in attack_150:
    print(i)