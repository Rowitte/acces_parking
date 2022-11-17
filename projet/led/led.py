import time
from grovepi import *
 
# Connect the Grove LED to digital port D4
led = 4
 
pinMode(led,"OUTPUT")
time.sleep(1)

print ("Connect the LED to the port labele D4!" )
 
while True:
    try:
        #Blink the LED
        digitalWrite(led,1)     # Send HIGH to switch on LED
        print ("LED ON!")
        time.sleep(1)
 
    except KeyboardInterrupt:   # Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError:             # Print "Error" if communication error encountered
        print ("Error")
