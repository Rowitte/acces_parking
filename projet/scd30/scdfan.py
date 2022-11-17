from scd30_i2c import SCD30
import time
import grovepi

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
            print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
            time.sleep(2)

            if m[0] > seuil_haut :
                rapport_cyclique = 180
                grovepi.analogWrite(mosfet,rapport_cyclique)
                time.sleep(1)

            elif m[0] < seuil_bas:
                rapport_cyclique = 0
                grovepi.analogWrite(mosfet,rapport_cyclique)
                time.sleep(1)

    else:
        rapport_cyclique = 0
        grovepi.analogWrite(mosfet,rapport_cyclique)
        time.sleep(0.2)