from gpiozero import MotionSensor
import time

pir = MotionSensor(25)

while True:
    pir.wait_for_motion()
    print ("se ha detectado un movimiento")
    pir.wait_for_no_motion() 
    print ("No se detecta nada")