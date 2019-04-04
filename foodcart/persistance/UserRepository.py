from foodcart.connection.db_utils import *
from foodcart.models.User import User


def get_user_from_username(username):
    cursor.execute("USE FoodCart;")
    cursor.execute("SELECT * FROM user WHERE username='" + username + "';")
    data = cursor.fetchone()

    if (data is None):
        print("Nothing found")
        return

    return User(data[0], data[1], data[2], data[3], data[4], data[5])
