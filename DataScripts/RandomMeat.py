from mysql.connector import connect
from foodcart.connection.db_utils import cursor, mydb
import random

meat_type = ["Steak", "Côte Levée", "Filet mignon", "Entre cote", "Filet de boeuf", "Faux-filet", "Bavette",
              "Bifteak", "Flanchet", "Paleron", "Entrecôte"]


meat_country = ["Canada", "USA", "Mexique", "Inde", "France", "Maroc", "Colombie", "Afrique", "Chine", "Russie",
                  "Argentine", "Espagne", "Allemagne", 'Bresil', "Portugual", "Vietnam", "Chili"]

#Fonction servant a creer des tuples dans la table Meats.
def Meats(cursor, number):
    cursor.execute("CREATE DATABASE IF NOT EXISTS FoodCart")
    cursor.execute("USE FoodCart")
    cursor.execute("CREATE TABLE IF NOT EXISTS Meat (type char(20), country char(20), price integer)")

    for i in range(0, number):
        type = random.choice(meat_type)
        country = random.choice(meat_country)
        price = random.randint(2, 10)
        sqlFormula = "INSERT INTO Meat (type, country, price) VALUES (%s, %s, %s)"
        cursor.execute(sqlFormula, (type, country, price))

    mydb.commit()
