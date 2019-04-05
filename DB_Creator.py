from DataScripts.RandomUsers import Users
from foodcart.connection.db_utils import cursor


def Create_db():
    Users(cursor,2)


Create_db()
