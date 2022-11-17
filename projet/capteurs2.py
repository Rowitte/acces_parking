#!/usr/bin/env python3
#-- coding: utf-8 --

from scd30_i2c import SCD30
import time
import grovepi
import socket
import mysql.connector

# Adresse et port du socket 
HOST = "192.168.12.66"  # Standard loopback interface address (localhost)
PORT = 20000  # Port to listen on (non-privileged ports are > 1023)



# Connexion au socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))  
print ("Connexion vers " + HOST + ":" + str(PORT) + " reussie.")
client.setblocking(False)
#client.settimeout(2)


# Connexion � la base de donnees
conn = mysql.connector.connect(host="192.168.12.71",port="3306",user="admin",password="root",database="gestion_abonnes")
cursor=conn.cursor()

req = "INSERT INTO capteurs (Co2, temperature, humidite) VALUES(%s, %s, %s)"

scd30 = SCD30()
mosfet = 5

scd30.set_measurement_interval(2)
scd30.start_periodic_measurement()
i=0
time.sleep(2)

seuil_haut = 1100
seuil_bas = 900
try :
    while True :

        if scd30.get_data_ready():

            m = scd30.read_measurement()

            if m is not None:

                print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, humi: {m[2]:.2f}%")

                co2 = str(m[0])
                temp = str(m[1])
                humi = str(m[2])

                client.send(co2.encode())
                client.send(temp.encode())
                time.sleep(0.2)
                client.send(humi.encode())
                i = i+1



                if m[0] > seuil_haut :
                    rapport_cyclique = 180
                    grovepi.analogWrite(mosfet,rapport_cyclique)
                    time.sleep(1)

                elif m[0] < seuil_bas:
                    rapport_cyclique = 0
                    grovepi.analogWrite(mosfet,rapport_cyclique)
                    time.sleep(1)

                if rapport_cyclique == 0 :
                client.send(b'off')
                time.sleep(1)
                elif rapport_cyclique == 180:
                client.send(b'on')
                time.sleep(1)

                try :
                    recv = client.recv(1024) 
                    print(recv)
                    if len(recv) >0 :
                        rapport_cyclique = 180
                        grovepi.analogWrite(mosfet,rapport_cyclique)
                        time.sleep(5)

                except:
                    pass      

            if i == 30 :

                reference = (co2, temp, humi)
                cursor.execute(req , reference)
                i = 0
                print (" donnees envoyer a la bdd")
                time.sleep(1)

except KeyboardInterrupt :
    rapport_cyclique = 0
    grovepi.analogWrite(mosfet,rapport_cyclique)
    
rapport_cyclique = 0
grovepi.analogWrite(mosfet,rapport_cyclique)
conn.commit()

