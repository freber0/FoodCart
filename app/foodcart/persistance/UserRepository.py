from foodcart.connection.db_utils import *
from foodcart.models.User import User


def get_user_from_username(username):
    cursor.execute("USE FoodCart;")
    cursor.execute("SELECT * FROM user WHERE username='" + username + "';")
    data = cursor.fetchone()

    if data is None:
        print("Nothing found")
        return

    return User(data[0], data[1], data[2], data[3], data[4], data[5])


def add_user(user):
    cursor.execute("USE FoodCart;")
    sql = "INSERT INTO user (username, password, lastname, firstname, email, address) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (user.username, user.password, user.lastname, user.firstname, user.email, user.address))
    mydb.commit()


def update_user(user):
    cursor.execute("USE FoodCart;")
    sql = "UPDATE user SET password = %s, lastname = %s, firstname = %s, email = %s, address = %s WHERE username =%s "
    cursor.execute(sql, (user.password, user.lastname, user.firstname, user.email, user.address, user.username))
    mydb.commit()
