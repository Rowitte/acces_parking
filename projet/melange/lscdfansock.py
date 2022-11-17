from scd30_i2c import SCD30
import lcddriver
lcd = lcddriver.lcd()
import time
import grovepi
import socket

HOST = "192.168.12.93"  # Standard loopback interface address (localhost)
PORT = 20000  # Port to listen on (non-privileged ports are > 1023)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print ("Connexion vers" + HOST + ":" + str(PORT) + " reussie.")

buffer = client.recv(1024)

scd30 = SCD30()
mosfet = 5

scd30.set_measurement_interval(2)
scd30.start_periodic_measurement()

time.sleep(2)

seuil_haut = 1100
seuil_bas = 900
while True:

    if scd30.get_data_ready():
        m = scd30.read_measurement()

        if m is not None:
            print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, humi: {m[2]:.2f}%")

            co2 = str(m[0])
            temp = str(m[1])
            humi = str(m[2])

            client.send(co2.encode())
            client.send(humi.encode())
            time.sleep(0.2)
            client.send(temp.encode())

            time.sleep(2)

            if m[0] > seuil_haut :
                rapport_cyclique = 180
                grovepi.analogWrite(mosfet,rapport_cyclique)
                time.sleep(1)

            elif m[0] < seuil_bas:
                rapport_cyclique = 0
                grovepi.analogWrite(mosfet,rapport_cyclique)
                time.sleep(1)

                
            except KeyboardInterrupt:
                rapport_cyclique = 0
                grovepi.analogWrite(mosfet,rapport_cyclique)
                time.sleep(0.2)
                lcd.lcd_clear()
                
                            if  :
                print(buffer.decode())
                
#             lcd.lcd_clear()
#             lcd.lcd_display_string("Acces Parking", 1)
#             lcd.lcd_display_string(f"C02 ={m[0]:.2f}ppm", 2)
#             lcd.lcd_display_string(f"temperature: {m[1]:.2f}'C", 3)
#             lcd.lcd_display_string(f" humidite: {m[2]:.2f}%", 4)
