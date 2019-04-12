from mysql.connector import connect

mydb = connect(
    host="db",
    user="root",
    password="1234",
    port="3306")

cursor = mydb.cursor()