#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import argparse
import signal
import sys
import time
import logging

from rpi_rf import RFDevice

rfdevice = None

def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180
    angle_as_percent = angle * ratio
    
    return start + angle_as_percent

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 

pwm_gpio = 11
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)
pwm.start(angle_to_percent(0))
time.sleep(1)

def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

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


#le gros if 
while True:
    if rfdevice.rx_code_timestamp != timestamp:
        
        
        #Init at 180°
        pwm.start(angle_to_percent(180))
        time.sleep(1)

        #Go at 90°
        pwm.ChangeDutyCycle(angle_to_percent(90))
        time.sleep(7)

        #Finish at 180°
        pwm.ChangeDutyCycle(angle_to_percent(180))
        time.sleep(1)
        
        
pwm.stop()
GPIO.cleanup()