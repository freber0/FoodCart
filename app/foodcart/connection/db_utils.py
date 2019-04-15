from mysql.connector import connect

# Sert a faire la connection avec la BD
mydb = None

while mydb is None:
    try:
        mydb = connect(
            host="db",
            user="apptester",
            password="1234",
            port="3306",
            database="FoodCart")
        cursor = mydb.cursor()
    except:
        pass

