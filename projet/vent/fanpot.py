import time
import grovepi
# MOSFET SUR  port D5
mosfet = 5
grovepi.pinMode(mosfet,"OUTPUT")
# Digital ports that support Pulse Width Modulation (PWM)
# D3, D5, D6
# Digital ports that do not support PWM
# D2, D4, D7, D8
#potentiomere en A0 pour faire varier la vitesse du moteur
pot = 14 # Pin 14 is A0 Port.
time.sleep(1)
while True :
    rapport_cyclique = int(grovepi.analogRead(pot)/4 )#  /4 pour mettre sur 8 bits : 255 = 100 %
    print( "rapport cyclique  = " , int(rapport_cyclique/255*100), " %")
    grovepi.analogWrite(mosfet,rapport_cyclique)
    time.sleep(1)
    