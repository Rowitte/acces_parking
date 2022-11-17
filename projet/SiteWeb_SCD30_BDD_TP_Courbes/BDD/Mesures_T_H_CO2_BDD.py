import serial
import time
import sqlite3 
ser = serial.Serial('COM10',9600) 
time.sleep(5)
connexion = sqlite3.connect('Capteurs.db')# Cette commande crée le fichier Capteurs.db s'il n'existe pas
with connexion :
    curseur = connexion.cursor()
    curseur.execute("DROP TABLE IF EXISTS DHT11_data")
    curseur.execute("CREATE TABLE  DHT11_data(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,horodatage DATETIME,humidité NUMERIC,temperature NUMERIC,CO2 NUMERIC)")
while True :
    ser.write(b"L")
    humidité = float(ser.readline())
    temperature  = float(ser.readline())
    CO2  = float(ser.readline())
    print(humidité)
    print(temperature)
    print(CO2)
    connexion = sqlite3.connect('Capteurs.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO DHT11_data VALUES (NULL,datetime('now','+1 hours'),(?),(?),(?))",(humidité,temperature,CO2))
    connexion.commit()
    connexion.close()
    time.sleep(2)