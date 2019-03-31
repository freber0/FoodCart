from mysql.connector import connect

#Sert a faire la connection avec la BD
mydb = connect(
    host="localhost",
    user="root",
    password= "1234",
    database="FoodCart",
    port="3306")

cursor = mydb.cursor()
