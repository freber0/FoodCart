from foodcart.connection.db_utils import cursor


def get_legume():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='legume' ")
    legumes = cursor.fetchall()
    return legumes


def get_fruit():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='fruit' ")
    fruits = cursor.fetchall()
    return fruits


def get_viande():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='viande' ")
    viandes = cursor.fetchall()
    return viandes


def get_pains():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='pain' ")
    pains = cursor.fetchall()
    return pains


def get_produit_laitier():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='produit_laitier' ")
    lait = cursor.fetchall()
    return lait


def get_all():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return products


def get_info_cart_item(product_id):
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products WHERE product_id ='" + product_id + "';")
    products_info = cursor.fetchall()
    return products_info

def get_price_item(product_id):
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT price FROM products WHERE product_id ='" + product_id + "';")
    product_price = cursor.fetchall()
    return product_price
