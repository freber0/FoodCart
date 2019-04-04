from mysql.connector import connect
from foodcart.Connection import cursor
from DataScripts.RandomVegetables import Vegetables
from DataScripts.RandomFruits import Products
from DataScripts.RandomBreads import Breads
from DataScripts.RandomMeat import Meats
from DataScripts.RandomDairyProducts import Dairy_products


import random

def Create_db():
    Products(cursor)

Create_db()
