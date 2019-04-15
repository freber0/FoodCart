from foodcart.connection.db_utils import *
from foodcart.models.User import User
import uuid


def add_checkout_items(user: User, items):
    orderId = str(uuid.uuid1())
    cursor.execute("USE FoodCart;")
    sql = "INSERT INTO orders (orderId, username) VALUES (%s, %s);"
    cursor.execute(sql, (orderId, user.username))
    for item in items:
        for item_id, item_qty in item.items():
            sql = "INSERT INTO orderItem (productId, orderId, quantity) VALUES (%s, %s, %s);"
            cursor.execute(sql, (item_id, str(orderId), item_qty))
    mydb.commit()
