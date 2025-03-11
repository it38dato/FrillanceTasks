#Заполнить таблицу в БД.
# Разработка баз данных.
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
sql = "INSERT INTO customers (Date, id, BSS, Reg, BS_name, TAC) VALUES (%s, %s, %s, %s, %s, %s)"
val = (datetime.datetime(2022, 1, 30, 5, 13, 36), 249, "OK", "IR", "IR0000", "0000")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")