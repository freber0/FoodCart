from mysql.connector import connect
from foodcart.Connection import cursor, mydb
import random

fruits_name = ["Banane", "Orange", "Cerise", "Ananas", "Bleuet", "Melon", "Pamplemouse", "Pitaya", "Mangue", "Kiwi",
               "Clementine", "Citron", "Lime", "Papaya", "Carambole", "Framboise"]

fruits_country = ["Canada", "USA", "Mexique", "Inde", "France", "Maroc", "Colombie", "Afrique", "Chine", "Russie",
                  "Argentine", "Espagne", "Allemagne", 'Bresil', "Portugual", "Vietnam", "Chili"]

#Fonction servant a creer des tuples dans la table Fruits.
def Fruits(cursor, number):
    cursor.execute("CREATE DATABASE IF NOT EXISTS FoodCart")
    cursor.execute("USE FoodCart")
    cursor.execute("CREATE TABLE IF NOT EXISTS Fruits (name char(20), country char(20), price integer)")

    for i in range(0, number):
        name = random.choice(fruits_name)
        country = random.choice(fruits_country)
        price = random.randint(2, 10)
        sqlFormula = "INSERT INTO Fruits (name, country, price) VALUES (%s, %s, %s)"
        cursor.execute(sqlFormula, (name, country, price))

    mydb.commit()
