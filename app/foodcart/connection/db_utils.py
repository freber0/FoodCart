from mysql.connector import connect
import time

# un sleep de 30s pour s'assurer que la bd soit bien starter avant que l'app essaie de se connecter avec le docker-compose up

# time.sleep(30)

# Sert a faire la connection avec la BD
mydb = None
while mydb is None:
    try:
        mydb = connect(
            #host="localhost",
            host="db",
            user="root",
            password="1234",
            port="3306",
            database="FoodCart")
        cursor = mydb.cursor()
    except:
        pass

