from foodcart.connection.db_utils import cursor, mydb
import random

vegetables_name = ["Brocoli", "Carotte", "Betterave", "Courge", "Citrouille", "Aubergine", "Piment", "Navet",
                   "Oignon", "Persil", "Laitue", "Celerie", "Chou", "Epinard" "Asperge", "Haricot"]

vegatables_country = ["Canada", "USA", "Mexique", "Inde", "France", "Maroc", "Colombie", "Afrique", "Chine", "Russie",
                  "Argentine", "Espagne", "Allemagne", 'Bresil', "Portugual", "Vietnam", "Chili"]

#Fonction servant a creer des tuples dans la table Vegetables.
def Vegetables(cursor, number):
    cursor.execute("CREATE DATABASE IF NOT EXISTS FoodCart")
    cursor.execute("USE FoodCart")
    cursor.execute("CREATE TABLE IF NOT EXISTS Vegetables (name char(20), country char(20), price integer)")

    for i in range(0, number):
        name = random.choice(vegetables_name)
        country = random.choice(vegatables_country)
        price = random.randint(2, 10)
        sqlFormula = "INSERT INTO Vegetables (name, country, price) VALUES (%s, %s, %s)"
        cursor.execute(sqlFormula, (name, country, price))

    mydb.commit()
