from gpiozero import DigitalInputDevice
import time 

d0_input = DigitalInputDevice(4)

while True:
    if (not d0_input.value):
        print("Humedad alcanzada")
    else: 
        print("Necesitas regar tus plantas")
        time.sleep(3)