
'''
Finish fcc lectures

Finish caleb curry lectures

Redo fcc exercise w/sql alchemy in python

Conect python > sqlalchemy > sqlite > pandas

Redo also in pandas

'''

import sqlite3

# Databases and Python, direct SQL

# Define Conection
conec = sqlite3.connect('education.db')
# This databese dosn't currently exist
# if sqlite3 attempts conection to DB that dosnt exist
# it will just create it 

# Define Cursor
c = conec.cursor()

#inputing data directly with the obj methods

# Create Table
c.execute(''' CREATE TABLE IF NOT EXIST User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE,
        email TEXT
        );''' )

# Enter Data
c.execute(''' INSERT INTO User (name, email) 
    VALUES ('Jane', 'jane@tsugi.org'); ''')

# Multi line commands with semi colons ; 
c.execute(''' 
INSERT INTO User (name, email)
VALUES ('ed', 'ed@tsugi.org');

INSERT INTO User (name, email)
VALUES ('Sue', 'sue@tsugi.org');
''')
#Save and close conection
conec.commit()
c.close()
conec.close()

# Inputing Data with functions
def create_table():
    c.execute(''' CREATE TABLE IF NOT EXISTS Course (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE
); ''')
    
def data_entry():
    c.execute(''' INSERT INTO Course (title)
    VALUES ('Python'); ''')
    conec.commit()
    c.close()
    conec.close()

def create_table()
def data_entry()

# Inputing data with better functions

def dynamic_data_entry():
    title = input('Enter course title')
    c.execute(''' INSERT INTO Course (title)
    VALUES (?); ''', title)
    conec.commit()

# Reading data from the database
def read_from_db():
    # can obv enhance with user input to spec table or vals
    c.execute(''' SELECT * FROM Course ; ''')
    data = c.fetchall()

    # could also expres w/ list comprehension
    # [print(row) for row in data]
    for row in data:
        print(row)
        # can also spec return vals in dif order, or index
        # e.g. print(row[2])

def update_db():
    old = input('Select course value to update : ')
    new = input('Value to replace with : ')

    c.execute(''' UPDATE Course 
    SET title = (?) WHERE title = (?) ; ''', (old, new);)
    conec.commit()

def delete_data():
    delete = input('What courses to delete? : ')
    c.execute(''' DELETE FROM Course
    WHERE title = (?); ''', delete)
    conec.commit()



# Databases and Python, using an ORM
import sqlalchemy


# Databases and Python,
# In-memory DB-ish stuff with Pandas