from mysql.connector import connect
from foodcart.Connection import cursor
from DataScripts.RandomUsers import Users

import random

def Create_db():
    Users(cursor,2)


Create_db()
