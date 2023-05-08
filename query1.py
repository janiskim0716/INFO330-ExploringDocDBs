import sqlite3
import sys
import pymongo
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon named "Pikachu"
print("Find all pokemon named Pikachu:")
pikachu = pokemonColl.find_one({"name": "Pikachu"})
print(pikachu)