from mysql.connector import connect
from foodcart.Connection import cursor, mydb
import random

#Fonction servant a creer des tuples dans la table Fruits.
def Products(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS FoodCart")
    cursor.execute("USE FoodCart")
    cursor.execute("DROP TABLE IF EXISTS Products")
    cursor.execute("CREATE TABLE IF NOT EXISTS Products (product_id integer, class_name varchar(20), name varchar(20), price integer, image varchar(100))")
    sql_formula = "INSERT INTO Products (product_id, class_name, name, price, image) VALUES (%, %, %, %, %)"
    cursor.execute(sql_formula, (1, "produit_laitier", "lait", 2, "www.alimentsduquebec.com"))


    mydb.commit()
