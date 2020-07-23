import sqlite3
import os
from pokemon import Pokemon


def createDB():
	# creates a db file if it doesn't exist, else connects
	conn = sqlite3.connect('pokemon.db')

	# cursor allows us to run sql commands using execute method
	c = conn.cursor()

	# triple quotes allows us to run multiple lines without special chars
	c.execute("""CREATE TABLE pokemonlist (
		dex integer,		-- the number the pokemon holds in the pokedex
		pokemon text,		-- the name of the pokemon
		available text,		-- whether it is available in the game (Yes/No)
		evolution text,		-- whether it is available via evolution or breeding
		location text		-- location where pokemon is available
		)""")

	# do this to commit changes made to database
	conn.commit()

	# close connection
	conn.close()


# function to delete the database
def deleteDB():
	# maybe add a confirmation message here
	os.remove('pokemon.db')
	print('File deleted')


# insertion of an entry into the database
def insert(pokemon):
	# dictionary to convert boolean to string
	dict = {True: 'Yes', False:'No'}
	# opening database
	conn = sqlite3.connect('pokemon.db')
	c = conn.cursor()
	# insertion data into database
	# note!!! Will need to format pokemon.locations properly!!!
	c.execute("INSERT INTO pokemonlist VALUES (:dex, :pkmn, :aval, :evol, :loc)",
		{'dex': pokemon.dex, 'pkmn': pokemon.name, 'aval': dict[pokemon.available], 'evol': dict[pokemon.line], 'loc': str(pokemon.locations)})
	conn.commit()
	conn.close()


# delete a pokemon from the database
def delete(pokemon):
	conn = sqlite3.connect('pokemon.db')
	c = conn.cursor()
	# insertion data into database
	# note!!! Will need to format pokemon.locations properly!!!
	c.execute("DELETE from pokemonlist where pokemon = :pkmn",{'pkmn': pokemon.name})
	conn.commit()
	conn.close()


# reference for how to spit a string
def split(data):
	arry = data.split(', ')
	return arry

# testing starts here
# creating class data
pkm1 = Pokemon(1, 'Bulbasaur', False, False, [])
# printing out class data
print(pkm1)
# insert class into database
deleteDB()
createDB()
try:
	insert(pkm1)
	print('\nSuccess!')
except:
	print('\nFailed to insert data')
delete(pkm1)

