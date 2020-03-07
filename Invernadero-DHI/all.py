from firebase import firebase
from gpiozero import DigitalInputDevice , LightSensor , MotionSensor , Servo, LED
from time import sleep

firebase = firebase.FirebaseApplication("https://hack-dhi.firebaseio.com", None)

pir = MotionSensor(25)
ldr = LightSensor(22)
d0_input = DigitalInputDevice(4)
servo = Servo(23)
led1= LED(17)
led2= LED(27)

def miServo():
    print("Abrir valvula")
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)

def miMovimiento():
    
    pir.wait_for_motion()
    data = {'pir': "Hay una presencia"}
    result = firebase.post('/sensores', data)
    print ("se ha detectado un movimiento")
    sleep(2)

    pir.wait_for_no_motion()
    datam = {'pir': "No hay presencia"}
    result = firebase.post('/sensores', datam) 
    print ("No se detecta nada")
    sleep(2)

def miLdr():
    print(ldr.value)
    datal = {'ldr': "Si hay luz"}
    result = firebase.post('/sensores', datal) 
    sleep(2)

def miHumedad():
     if (not d0_input.value):
        datap = {'humedad': "Humedad alcanzada"}
        result = firebase.post('/sensores', datap) 
        print("Humedad alcanzada")
     else: 
        datan = {'humedad': "Necesitas regar tus plantas"}
        result = firebase.post('/sensores', datan) 
        print("Necesitas regar tus plantas")
        sleep(2)
    

def miLed1():
    led1.on()
    sleep(1)
    led1.off()
    sleep(1)

def miLed2():
    led2.on()
    sleep(1)
    led2.off()
    sleep(1)

while True:

    result = firebase.get("iluminacion", None)

    if result["foco1"]== 'true':
        print("Encendido de luces")
        led1.on()
    else:
        print("apagado de luces")
        led1.off()
        

    if result["foco2"]== 'verdad':
        print("Encendido de luces")
        led2.on()
    else:
        print("apagado de luces")
        led2.off()

    result = firebase.get("valvula", None)
    
    if result["valvula1"]== 'min':
        print("Cerrado")
        servo.min()
    else:
        print("Abierto")
        servo.max() 
    
    #miLdr()
    #miMovimiento()
    #miHumedad()


   
    

