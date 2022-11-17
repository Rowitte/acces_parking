#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import argparse
import signal
import sys
import time
import logging
import mysql.connector
from grovepi import *
from rpi_rf import RFDevice
import lcddriver
lcd = lcddriver.lcd()

# Connection   la base de donn es
conn = mysql.connector.connect(host="192.168.12.71",port="3306",user="admin",password="root",database="gestion_abonnes")
cursor=conn.cursor()
req = "select code from abonnes"
#req2 = "INSERT INTO acces (id_abonnes, date) VALUES(%s, %s)"

# Connexion   la LED
led = 4
pinMode(led,"OUTPUT")
time.sleep(1)

# Defnition des angle pour le servo moteur et d finition de l'emplacement
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180
    angle_as_percent = angle * ratio
    
    return start + angle_as_percent

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 


pwm_gpio = 11
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)
pwm.start(angle_to_percent(0))
time.sleep(1)


led = 4
 
pinMode(led,"OUTPUT")
time.sleep(1)

def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

# Cr ation des variable pour le recepteur 433Mhz
logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
args = parser.parse_args()

signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
timestamp = None
logging.info("Listening for codes on GPIO " + str(args.gpio))


try :
    while True:
            
            timestamp = rfdevice.rx_code_timestamp
            
            lcd.lcd_display_string("Acces Parking", 1)
            
            cursor.execute(req)
            info = cursor.fetchall()

            #Initialisation du servo   0 degr 
            pwm.start(angle_to_percent(0))
            time.sleep(1)

            for row in info:
                i=0
                if rfdevice.rx_code == row[i] :
                    logging.info(str(rfdevice.rx_code))

                    digitalWrite(led,1)
                    print ("LED ON!")
                    time.sleep(1)

                    GPIO.cleanup()                    
                    GPIO.setmode(GPIO.BOARD)
                    GPIO.setup(pwm_gpio, GPIO.OUT)
                    pwm = GPIO.PWM(pwm_gpio, frequence)
                    print(pwm)
                    pwm.start(angle_to_percent(0))
       
                    lcd.lcd_display_string("Acces Autoriser", 2)

                    #Placement   l'angle 180
                    pwm.ChangeDutyCycle(angle_to_percent(180))
                    time.sleep(1)

                    #Placement   l'angle 90
                    pwm.ChangeDutyCycle(angle_to_percent(90))
                    time.sleep(10)

                    #Placement   l'angle 180
                    pwm.ChangeDutyCycle(angle_to_percent(180))
                    time.sleep(1)

                    #rfdevice.rx_code = 0
                    rfdevice.cleanup()
                    rfdevice = RFDevice(args.gpio)
                    
                    lcd.lcd_clear()

                    GPIO.setup(pwm_gpio, GPIO.IN)
                    pwm.stop()
                    break
                elif rfdevice.rx_code != row[i] :

                    lcd.lcd_display_string("Acces Refuser", 2)
                    time.sleep (3)
                    lcd.lcd_clear()
                    #pwm.stop()
                    break

                #break
            GPIO.cleanup()  
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(pwm_gpio, GPIO.IN)
                    

except KeyboardInterrupt:
    digitalWrite(led,0)
    print ("LED OFF!")
    time.sleep(1)
    lcd.lcd_clear()

pwm.stop()
GPIO.cleanup()




