from foodcart.connection.db_utils import *
from flask import request


def search():
    search_value = request.form['search']
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products WHERE name LIKE '%" + search_value + "%' OR class_name='" + search_value + "'")
    searched_products = cursor.fetchall()
    return searched_products
