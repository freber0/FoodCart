from mysql.connector import connect
import random

dairy_type = ["Lait", "Fromage", "Yogourt", "Fromage en grains", "Lait sans lactose", "Fromage feta", "Fromage Cottage",
              "Lait au chocolat", "Fromage en tranche"]


dairy_country = ["Canada", "USA", "Mexique", "Inde", "France", "Maroc", "Colombie", "Afrique", "Chine", "Russie",
                  "Argentine", "Espagne", "Allemagne", 'Bresil', "Portugual", "Vietnam", "Chili"]

#Fonction servant a creer des tuples dans la table Dairy_products.
def Dairy_products(cursor, number):
    cursor.execute("CREATE DATABASE IF NOT EXISTS FoodCart")
    cursor.execute("USE FoodCart")
    cursor.execute("CREATE TABLE IF NOT EXISTS Dairy_products (type char(20), country char(20), price integer)")

    for i in range(0, number):
        type = random.choice(dairy_type)
        country = random.choice(dairy_country)
        price = random.randint(2, 10)
        sqlFormula = "INSERT INTO Dairy_products (type, country, price) VALUES (%s, %s, %s)"
        cursor.execute(sqlFormula, (type, country, price))

    mydb.commit()
