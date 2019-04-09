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
