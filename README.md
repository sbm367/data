
# Databases and Python 

Database - contains multiple tables
|_
    Relatation / Table - contains multiple tuples and attributes
    |_
        Tuple / Row - set of fields that represent an object
    |_
        Attribute / Column / Field - one of possible many elements of data an object in a row might have 

## CRUD Model

Create - CREATE TABLE, INSERT INTO 
Read - SELECT, FROM, WHERE, ORDER BY
Update - UPDATE, SET, WHERE
Delete - DELETE FROM , WHERE 

## Keys

Primary Keys - unique interger ID of row in a DB, no outside meaing
Forgien Keys - unique interger ID or primary key in other table
Logical Keys - what a user would actualy look up as a key, like a name

naming conventions

Table : Users
primary key : id
forgien kay : user_id 

## Relationships

One-to-One : can be stored as Attribute in the same table or in a seperate table if it makes sense from a design perspective
    example: for a Credit Card company, username would be stored in the User table, but card_number might be stored in the Card table because they are seperate objects despiite being one-to-one
One-to-Many : the Many stores the id of the One as a Forgien Key Atrribute
    example: One Artist has Many Albums
            Each Album has artist_id as a Forgien Key in its row as an Atribute
Mant-to-Many : Broken up into 3 tables, 2 entity tables and a lookup table.
                The lookup table with have the IDs of both entety tables as Forgein Key Attributes
    example: Many Students take Many Classes
            table of Students with id, table of Classes with id
            table Students_Classes with row containg student_id, class_id if student has that class 