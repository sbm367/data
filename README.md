
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

Logical Keys - what a user would actualy look up as a key, like a name, often still unique

### Naming conventions


    Table : Users

    primary key : id

    forgien kay : user_id 


## Relationships

One-to-One : can be stored as Attribute in the same table or in a seperate table if it makes sense from a design perspective
    
    example: for a Credit Card company, username would be stored in the User table, but card_number might be stored in the Card table because they are seperate objects despiite being one-to-one

One-to-Many : the Many stores the id of the One as a Forgien Key Atrribute

A One-to-Many relationship is also sometimes called a Parent-Child relationship, with the One Parent having Many Children. The Parent's Primary Key would be the Child's Forgien Key. The Child inherets values from the Parent, but not the other way around. 
    
    example: One Artist has Many Albums
            Each Album has artist_id as a Forgien Key in its row as an Atribute


Mant-to-Many : Broken up into 3 tables, 2 entity tables and a junction table. The junction table with have the IDs of both entety tables as Forgein Key Attributes

Note that the junction table often dosn't have a primary key of its own and unses the unique paring/tuples of FK ids as its uniquenesss constraint / PK for speed and efficiency.

This junction table may contain additional data modeled at the conection.
    
    example: Many Students take Many Classes.
            1) Table of Students with id
            2) Table of Classes with id 
            3) Table Students_Classes with row containg student_id, class_id if student has that class 

## Forgien Key Constraints

If we have dependent One-to-Many / Parent-Child relationships, we need a way to ensure integrity across our data so that when a prent is updated, the update is propogated to its children. 

### Parent Conditions
    ON UPDATE
    ON DELETE

### Child Conditions
    RESTRICT - no chnage allowed, throws error
    CASCADE - changes all dependent values
    SET NULL - sets FK to NULL, will throw error if FK has NOT NULL contraint

## Joins 

Views are created through join statements

example syntax: 

    SELECT ...
    FROM ...
    JOIN ... ON ... = ...;


more concreatly

    SELECT Table_1.attribute, Table_2.attribute_2
    FROM Table_1
    JOIN Table_2 ON Table_1.table_2.id = Table_2.id;


Without the ON statement, the JOIN would return every possible combination of table elements.

So, if Table_1 had 10 rows and Table_2 had 50, a 500 row view would be returned. 

