from mysql.connector import connect
from foodcart.connection.db_utils import cursor, mydb
import random

bread_type = ["Pain blanc", "Pain brun", "Pain fait maison", "Pain fait a la main", "Pain grain entier", "Croissant", "Pain au raisin",
              "Pain au banane", "Pain au chocolat", "Pain multi grain", "Pain ble entier"]


bread_country = ["Canada", "USA", "Mexique", "Inde", "France", "Maroc", "Colombie", "Afrique", "Chine", "Russie",
                  "Argentine", "Espagne", "Allemagne", 'Bresil', "Portugual", "Vietnam", "Chili"]

#Fonction servant a creer des tuples dans la table Breads
def Breads(cursor, number):
    cursor.execute("CREATE DATABASE IF NOT EXISTS FoodCart")
    cursor.execute("USE FoodCart")
    cursor.execute("CREATE TABLE IF NOT EXISTS Breads (type char(20), country char(20), price integer)")

    for i in range(0, number):
        type = random.choice(bread_type)
        country = random.choice(bread_country)
        price = random.randint(2, 10)
        sqlFormula = "INSERT INTO Breads (type, country, price) VALUES (%s, %s, %s)"
        cursor.execute(sqlFormula, (type, country, price))

    mydb.commit()
