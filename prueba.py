#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import requests


from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from seeed_dht import DHT
from grove.grove_relay import GroveRelay

def main():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)

    # Grove - Light Sensor connected to port A0
    light_sensor = GroveLightSensor(0)
    # Grove - Temperature&Humidity Sensor connected to port D5
    dht_sensor = DHT('11', 5)
    # Grove - Ultrasonic Ranger connected to port D16
    ultrasonic_sensor = GroveUltrasonicRanger(16)
    # Grove - Relay connected to port D18
    relay = GroveRelay(18)

    while True:
        light = light_sensor.light
        humi, temp = dht_sensor.read()
        distance = ultrasonic_sensor.get_distance()

        print('#########################################################################')
        print('El valor de la luz es {}'.format(light))
        print('La temperatura es {}C, y la humedad {}%'.format(temp, humi))
        print('La distancia de la marea es {} cm'.format(distance))
        print('--------------------------------------------------------------------------')
        
        
        if 0 <= light < 200:
            print('Alumbrado encendido')
            relay.on()
            time.sleep(3)
            relay.off()
        else:
            print('No hace falta el alumbrado')
        
        level = ''
        if 10 <= temp < 15:
            level = 'Demasiado frío, llevar térmica'
        elif 15 < temp < 20:
            level = 'Temperatura normal'
        else:
            level = 'Demasiado calor, NO Recomendable'
            enviar = requests.get("https://api.thingspeak.com/update?api_key=YHOEOMT24EOLBP37&field1=" +str(light)+"&field2="+str(humi)+"&field3="+str(temp))
            GPIO.output(24, True)
            time.sleep(1)
            GPIO.output(24, False)
            time.sleep(1)
           
    

        print(level)
        #CADA 30 MINS VUELVE A ANALIZAR LOS VALORES
        time.sleep(1800)
        



if __name__ == '__main__':
    main()
