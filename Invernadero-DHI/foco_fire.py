import pyrebase
import RPi.GPIO as GPIO

from time import sleep

config = {
"apiKey": "AIzaSyD_gAAMh_-dPPkw6TwrdNvcD4DuyzyrpTc",
"authDomain": "hack-dhi.firebaseapp.com",
"databaseURL": "https://hack-dhi.firebaseio.com",
"storageBucket": "hack-dhi.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


print ("**********   INICIO  *************")


while True:
    salidaLed1 = db.child("iluminacion/led1").get()
    GPIO.output(17, salidaLed1.val())
    print ("salida led1: "), salidaLed1.val()


    salidaLed2 = db.child("iluminacion/led2").get()
    GPIO.output(27, salidaLed2.val())
    print ("salida led2: "), salidaLed2.val()
    
    sleep(5)

GPIO.cleanup()