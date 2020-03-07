# Taller Hack DHI. 

![IoT](https://cambiodigital-ol.com/wp-content/uploads/2018/12/IOT_c.jpg)

## Presentación

En este taller aprenderemos a hacer IoT con ayuda de una Raspberry Pi y Firebase, para emplearlo en la domótica en la activación de iluminación, motores, actuadores y en el sensado de variables con sensores.
Firebase es una plataforma para el desarrollo de aplicaciones web y aplicaciones móviles desarrollada Google en 2014.
Es una plataforma ubicada en la nube, integrada con Google Cloud Platform, que usa un conjunto de herramientas para la creación y sincronización de proyectos que serán dotados de alta calidad, haciendo posible el crecimiento del número de usuarios y dando resultado también a la obtención de una mayor monetización.

![Firebase](https://elandroidelibre.elespanol.com/wp-content/uploads/2016/05/Screen-Shot-2016-05-19-at-00.13.32.png)

### Requerimientos para este curso
En este taller usaremos las siguientes herramientas:

* Un navegador web.
* Una cuenta en Firebase
* Un editor de texto (en mi caso sera Visual Studio Code)
* Conocimientos básicos de Programación
* Una Raspberry Pi.
* Algun sensor
* LEDs
* Motor

### Temario

* Presentacion del curso
* IoT
* Instalación de Node JS
* Firebase
* Demo Web App
* Lógica Java Script
* Raspberry Pi
* Que aprendimos, Despedida

![Flujo](https://i.pinimg.com/474x/b6/aa/97/b6aa97d9dab8ce7dd338c5a3b411c7d5.jpg)

#### Instalación Node JS
https://nodejs.org/es/

#### Firebase   
https://firebase.google.com

1. Crear una cuenta en Firebase con un correo de Gmail.
2. Ir a consola y comenzar un proyecto nuevo.
3. Añade Firebase a tu App Web.
4. Desde terminal entramos a la carpeta en donde vamos a trabajar:
        > npm install -g firebase-tools
        > firebase init 
        > firebase serve

### Demo Web App

Después de haber hecho las configuraciones de Firebase comenzamos con el diseño de nuestra Web App y a darle estilo. Es muy importante agregar las keys para poder utilizar Firebase en nuestra Web App, todo esto dentro del <head></head>.

<pre>
<code>
<script src="https://www.gstatic.com/firebasejs/7.9.3/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/7.9.3/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/7.9.3/firebase-database.js"></script>

<script>
      var config = {
        apiKey: "apiKey",
        authDomain: "hack-dhi.firebaseapp.com",
        databaseURL: "authDomain",
        storageBucket: "storageBucket",
        messagingSenderId: "messagingSenderId",
        appId: "appId"
      };
      firebase.initializeApp(config);
</script>
</pre>
</code>

### Lógica Java Script
Para crear una DB desde código.

<pre>
<code>

var database = firebase.database().ref('iluminacion').set({
            led1:true,
            led2:true
</pre>
</code>

### Raspberry Pi

![Rasp](https://www.programoergosum.com/images/cursos/238-control-de-gpio-con-python-en-raspberry-pi/pines-gpio-rpi-2.png)

Instalar Raspbian, para después instalar las librerias de firebase.

$ sudo pip install requests
$ sudo pip install python-firebase



