# INFO330: Exploring Document Databases
A homework assignment for my INFO 330 course, building around the Pokemon CSV file from [INFO330-CreatingRelations2](https://github.com/tedneward/INFO330-ExploringRelations2).

## Goals
Using either the CSV file or the SQLite database provided (whichever you find easier to use), import the data into a MongoDB database and make sure it is usable from a Python program (which will simulate some pokemon battles). You may need to use the `mongosh` client to manipulate the imported documents to match the desired format.

### Details

Next, [install MongoDB](https://www.mongodb.com/docs/manual/installation/) on your personal machine. (If you have technical difficulties doing that, you are free to explore using one of the free cloud MongoDB providers, but keep in mind that the TAs may not be able to help much if you run into issues.) Create a database called `pokemon`.

Once MongoDB (the MongoDB server program is called `mongod`) is running, connect to it with `mongosh` to make sure you can connect to it. (If you are having difficulties, try running `mongod --config mongo.conf` from this directory; it will make use of the configuration file in this directory to hopefully make it easier to connect.)
You should see this:

```
~/Projects/UW/INFO330-ExploringDocDBs % mongosh
Current Mongosh Log ID:	644a0ee87ac72be6cf6689ee
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.1
Using MongoDB:		6.0.5
Using Mongosh:		1.8.1
```

... along with (potentially) a lot more information. At the end of all that, however, you should see something like this:

```
test>
```

This is the *MongoDB Shell prompt*, and it is similar in some ways to running `sqlite3` from the command prompt: It is an interactive shell that you can use to interact with a MongoDB program. You can tyoe `help()` to get a list of commands that the shell recognizes, or `db.help()` to get a list of methods on the top-level `db` object.

Once you know that MongoDB is up and running, you can dive into the bulk of the assignment.

### Collections

In your `pokemon` database, you will need to have a collection `pokemon_data`, which will contain instances of JSON/BSON documents that look roughly like the following:

```
{
    "_id": (some alphanumeric value),
    "name": "Bulbasaur",
    "pokedex_number": 1,
    "types": ["grass", "poison"],
    "hp": 45,
    "attack": 49,
    "defense": 59,
    "speed": 45,
    "sp_attack": 65,
    "sp_defense": 65
    "abilities": [
        "Chlorophyll", "Overgrow"
    ]
}
```

Notice that this is just the combat statistics of the Pokemon; Team Rocket doesn't care about any data except that which can be used in battles. Keep in mind, this is just one Pokemon; the collection will be an array of Pokemon in JSON format.

## Stories/Rubric

Create Python scripts that do the following:

* Write a query that returns all the Pokemon named "Pikachu". (1pt)
* Write a query that returns all the Pokemon with an attack greater than 150. (1pt)
* Write a query that returns all the Pokemon with an ability of "Overgrow" (1pt)

These can be either in their own `.py` files or all in one file, whichever you find easier. You may find it helpful to use the `Validate.py` script as an example. Run these on your machine, and capture the run in a video. Commit those video files to this repository.

Now it's time to run some battles; use Python to run the `Battle.py` script. If it runs into problems, it will print out an error message. Your job is to correct the database to match the script's expectations. (Do not change the Python code.)

* Python script can execute a battle between Pokemon. (2pts)

Again, run this file and capture the output as a video.

## Extra credit

* **Be your best Team Rocket. (2 pts)** Record a video of yourself saying, "Looks like Team Rocket is blasting off again....!" and submit it in this repository.

* **Improve the Battle.py script. (2 pts)** The algorithm in the Battle.py script is pretty lame. (Team Rocket is NOT known for its skills in evaluating Pokemon.) Improve it and commit the changes to this repository. Make sure to point out to your TA that you have improved it, so they can verify it and give you the extra point.
