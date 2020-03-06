from gpiozero import LightSensor
from time import sleep
ldr = LightSensor(5)

while (True):
    print(ldr.value)
    sleep(2)

