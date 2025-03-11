#Вывести список таблиц в БД.
# Разработка Парсинг из баз даных.
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
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)