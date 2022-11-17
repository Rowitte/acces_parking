import lcddriver
from time import *
lcd = lcddriver.lcd()
from scd30_i2c import SCD30
import time


scd30 = SCD30()

#scd30.set_measurement_interval(2)
#scd30.start_periodic_measurement()


try:
    while True:
        m = scd30.read_measurement()
        lcd.lcd_clear()
        lcd.lcd_display_string("Acces Parking", 1)
        lcd.lcd_display_string(f"C02 ={m[0]:.2f}ppm", 2)
        lcd.lcd_display_string(f"temperature: {m[1]:.2f}'C", 3)
        lcd.lcd_display_string(f" humidite: {m[2]:.2f}%", 4)
        sleep(2)

except KeyboardInterrupt:
    lcd.lcd_clear()

