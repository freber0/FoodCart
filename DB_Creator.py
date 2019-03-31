from mysql.connector import connect
from foodcart.Connection import cursor
from DataScripts.RandomVegetables import Vegetables
from DataScripts.RandomFruits import Fruits
from DataScripts.RandomBreads import Breads
from DataScripts.RandomMeat import Meats
from DataScripts.RandomDairyProducts import Dairy_products


import random

def Create_db():
    Vegetables(cursor, 50)
    Fruits(cursor, 50)
    Breads(cursor, 50)
    Meats(cursor, 50)
    Dairy_products(cursor, 50)

Create_db()
