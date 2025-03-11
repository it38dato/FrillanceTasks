#Подключиться к БД и вывести иноформацию о БД.
# Разработка Соединение с базой.
import mysql.connector
mydb = mysql.connector.connect(
    host="tipWindows",
    #host="tipWindows2",
    user="tuser",
    password="tpassword",
    database="tbase"
    #database="tbase2"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
print(mydb)