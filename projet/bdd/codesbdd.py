import mysql.connector

conn = mysql.connector.connect(host="192.168.12.71",port="3306",user="admin",password="root",database="gestion_abonnes")
cursor=conn.cursor()
req = "select code from abonnes"
cursor.execute(req)
info =cursor.fetchall()


print(info)

i=0
j=1

for row in info:
    print(row[i])
