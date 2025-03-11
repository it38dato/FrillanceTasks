# вывести таблицу из БД.
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
mycursor.execute("SELECT * FROM bss_4g_nokia")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)