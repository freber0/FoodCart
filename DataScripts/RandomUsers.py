from mysql.connector import connect
from foodcart.Connection import cursor, mydb
import random

user_name = ["titoine34", "bob12"]

name = ["Adam", "Raymond"]

user_prenom = ["Adam", "Raymond"]

user_email = ["toto@hotmail.com", "tata@hotmail.com"]

user_addresse = ["43 rue de la chute", "123 rue Ste-Catherine"]

#Fonction servant a creer des tuples dans la table user.
def Users(cursor, number):
    cursor.execute("CREATE DATABASE IF NOT EXISTS FoodCart")
    cursor.execute("USE FoodCart")
    cursor.execute("DROP TABLE  IF EXISTS user")
    cursor.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR(20), password VARCHAR(100), nom VARCHAR(20), prenom VARCHAR(20), email VARCHAR(40), address VARCHAR(40), PRIMARY KEY (username))")

    for i in range(0, number):
        username = random.choice(user_name)
        password = 1234
        nom = random.choice(name)
        prenom = random.choice(user_prenom)
        email = random.choice(user_email)
        address = random.choice(user_addresse)
        sqlFormula = "INSERT INTO user (username, password, nom, prenom, email, address) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sqlFormula, (username, password, nom, prenom, email, address))

    mydb.commit()
