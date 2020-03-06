import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(16, gpio.OUT)
p = gpio.PWM(16,50)
p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(4.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10.5)
        time.sleep(0.5)

except KeyboardInterrupt:
    p.stop()
    gpio.cleanup()
