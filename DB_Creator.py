from DataScripts.RandomVegetables import Vegetables
from DataScripts.RandomFruits import Fruits
from DataScripts.RandomBreads import Breads
from DataScripts.RandomMeat import Meats
from DataScripts.RandomDairyProducts import Dairy_products
from DataScripts.RandomUsers import Users
from foodcart.connection.db_utils import cursor



def Create_db():
    Vegetables(cursor, 50)
    Fruits(cursor, 50)
    Breads(cursor, 50)
    Meats(cursor, 50)
    Dairy_products(cursor, 50)
    Users(cursor, 2)


Create_db()
