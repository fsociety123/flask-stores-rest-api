import sqlite3

#Creating a connection
connection= sqlite3.connect("data.db")

#Creating a cursor
cursor= connection.cursor()

#Create table query
query= "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

#Executing the query
cursor.execute(query)

query= "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"

#Executing the query
cursor.execute(query)
item= (None, "soap", 20.99)
insert= "INSERT INTO items VALUES (?, ?, ?)"

cursor.execute(insert, item)

#Saving the table
connection.commit()

#Closing the connection
connection.close()